"""Render one owner-authored JSON PR using only trusted default-branch code."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import generate

REPOSITORY = 'therealkallen/ai-radar'
PREFIX = f'/repos/{REPOSITORY}'
MAX_SOURCE_BYTES = 200_000


def require(value, message):
    if not value:
        raise ValueError(message)


class GitHub:
    def __init__(self, token):
        self.token = token

    def __call__(self, method, path, payload=None):
        require(path.startswith(PREFIX + '/'), 'Unexpected API destination')
        data = None if payload is None else json.dumps(payload).encode('utf-8')
        request = Request('https://api.github.com' + path, data=data, method=method,
                          headers={'Authorization': f'Bearer {self.token}',
                                   'Accept': 'application/vnd.github+json',
                                   'X-GitHub-Api-Version': '2022-11-28',
                                   'Content-Type': 'application/json',
                                   'User-Agent': 'AI-Radar-source-renderer'})
        with urlopen(request, timeout=30) as response:
            body = response.read()
        return json.loads(body) if body else None


def select_source(pr, files, repository, run_head, trusted_sha, rendered=False):
    require(repository == REPOSITORY, 'Unexpected repository')
    require(pr['state'] == 'open' and not pr['draft'], 'PR must be open and ready')
    require(pr['user']['login'] == REPOSITORY.split('/')[0], 'Only owner-authored source PRs')
    require(pr['head']['repo']['full_name'] == REPOSITORY, 'Fork PRs are not rendered')
    require(pr['base']['ref'] == 'main' and pr['base']['sha'] == trusted_sha,
            'PR must target the checked-out main revision')
    match = re.fullmatch(r'radar/issue-(\d{3,})', pr['head']['ref'])
    require(match is not None, 'Unexpected source branch')
    number = int(match[1])
    relative = f'content/issue-{number:03d}.json'
    if rendered:
        expected = {relative: 'added', f'issues/issue-{number:03d}.html': 'added',
                    'index.html': 'modified', 'issues/index.html': 'modified', 'coverage.md': 'modified'}
        require(pr['changed_files'] == len(files) == 5 and
                {f['filename']: f['status'] for f in files} == expected,
                'Recovery accepts only one new JSON and four generated files')
    else:
        require(pr['head']['sha'] == run_head, 'PR head changed after the triggering run')
        require(pr['changed_files'] == 1 and len(files) == 1, 'Only one source file may enter the renderer')
        require(files[0]['filename'] == relative and files[0]['status'] == 'added',
                'Only a new issue JSON is accepted')
    return number, relative


def parse_source(blob, sha):
    require(blob.get('encoding') == 'base64' and blob.get('size', MAX_SOURCE_BYTES + 1) <= MAX_SOURCE_BYTES,
            'Source is missing or too large')
    raw = base64.b64decode(blob['content'].replace('\n', ''), validate=True)
    require(len(raw) == blob['size'] <= MAX_SOURCE_BYTES, 'Source size mismatch')
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    require(actual == sha, 'Source blob SHA mismatch')

    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON key')
            result[key] = value
        return result
    return raw, json.loads(raw.decode('utf-8'), object_pairs_hook=unique)


def render(root, number, relative, raw, issue, as_of):
    existing = generate.records(root, as_of)
    require(existing and number == existing[-1]['num'] + 1 and issue['num'] == number,
            'Continue the current issue sequence')
    require(issue['period_start'] == existing[-1]['period_end'], 'Issue window does not continue main')
    require(not (root / relative).exists(), 'Refuse to replace an existing source record')
    generate.validate_issue(issue, as_of)
    (root / relative).write_bytes(raw)
    require(generate.main(['build', '--root', str(root), '--as-of', str(as_of)]) == 0, 'Build failed')
    require(generate.main(['check', '--root', str(root), '--as-of', str(as_of)]) == 0, 'Generated check failed')
    return [f'issues/issue-{number:03d}.html', 'index.html', 'issues/index.html', 'coverage.md']


def unchanged(api, pr_number, head, base):
    current = api('GET', f'{PREFIX}/pulls/{pr_number}')
    main = api('GET', f'{PREFIX}/git/ref/heads/main')['object']['sha']
    require(current['state'] == 'open' and current['head']['sha'] == head and main == base,
            'Main or PR changed; do not publish stale generated files')


def verify_rendered(root, generated, entries):
    tree = {e['path']: e for e in entries}
    for relative in generated:
        raw = (root / relative).read_bytes()
        sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        entry = tree.get(relative, {})
        require(entry.get('type') == 'blob' and entry.get('mode') == '100644' and entry.get('sha') == sha,
                'Recovery output does not match the trusted renderer')


def main():
    require(os.environ['GITHUB_REPOSITORY'] == REPOSITORY, 'Unexpected repository')
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
    run = event['workflow_run']
    require(run['event'] == 'pull_request' and run['head_repository']['full_name'] == REPOSITORY,
            'Only same-repository PR validation runs are eligible')
    require(len(run['pull_requests']) == 1, 'Expected one associated PR')
    pr_number = int(run['pull_requests'][0]['number'])
    require(pr_number > 0, 'Invalid PR number')
    api = GitHub(os.environ['GH_TOKEN'])
    pr = api('GET', f'{PREFIX}/pulls/{pr_number}')
    files = api('GET', f'{PREFIX}/pulls/{pr_number}/files?per_page=100')
    trusted_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    recovering = pr['changed_files'] == 5
    number, relative = select_source(pr, files, os.environ['GITHUB_REPOSITORY'], run['head_sha'],
                                     trusted_sha, rendered=recovering)
    head = pr['head']['sha']
    require(api('GET', f'{PREFIX}/git/ref/heads/main')['object']['sha'] == trusted_sha,
            'Trusted checkout is stale')
    comparison = api('GET', f'{PREFIX}/compare/{trusted_sha}...{head}')
    require(comparison['status'] == 'ahead' and comparison['behind_by'] == 0, 'Source branch must include main')
    commit = api('GET', f'{PREFIX}/git/commits/{head}')
    entries = api('GET', f'{PREFIX}/git/trees/{commit["tree"]["sha"]}?recursive=1')
    require(not entries.get('truncated'), 'Incomplete source tree')
    entry = next((x for x in entries['tree'] if x['path'] == relative), None)
    require(entry and entry['mode'] == '100644' and entry['type'] == 'blob', 'Source must be an ordinary JSON file')
    raw, issue = parse_source(api('GET', f'{PREFIX}/git/blobs/{entry["sha"]}'), entry['sha'])
    generated = render(ROOT, number, relative, raw, issue, generate.today())
    clean_env = {k: v for k, v in os.environ.items() if k not in ('GH_TOKEN', 'GITHUB_TOKEN')}
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                   cwd=ROOT, env=clean_env, check=True)
    unchanged(api, pr_number, head, trusted_sha)
    if recovering:
        # A previous write can succeed before dispatch times out. Rebuild with
        # main and verify every generated blob; never trust the bot label alone.
        verify_rendered(ROOT, generated, entries['tree'])
        api('POST', f'{PREFIX}/actions/workflows/validate.yml/dispatches', {'ref': pr['head']['ref']})
        print(json.dumps({'pr': pr_number, 'rendered_sha': head, 'issue': number,
                          'recovered': True, 'validation': 'dispatched'}))
        return
    tree = api('POST', f'{PREFIX}/git/trees', {
        'base_tree': commit['tree']['sha'],
        'tree': [dict(path=p, mode='100644', type='blob', content=(ROOT / p).read_text(encoding='utf-8'))
                 for p in generated]})
    result = api('POST', f'{PREFIX}/git/commits', {
        'message': f'chore: render verified issue {number}', 'tree': tree['sha'], 'parents': [head]})
    unchanged(api, pr_number, head, trusted_sha)
    api('PATCH', f'{PREFIX}/git/refs/heads/{pr["head"]["ref"]}', {'sha': result['sha'], 'force': False})
    # Explicit dispatch avoids relying on unattended checks for bot pushes.
    api('POST', f'{PREFIX}/actions/workflows/validate.yml/dispatches', {'ref': pr['head']['ref']})
    print(json.dumps({'pr': pr_number, 'source_sha': run['head_sha'], 'rendered_sha': result['sha'],
                      'issue': number, 'generated': generated, 'validation': 'dispatched'}))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f'SOURCE_RENDER_FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
