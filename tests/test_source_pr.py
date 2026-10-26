"""Source-only handoff: reproduce stale outputs, then render with trusted code."""
import base64
import copy
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from scripts import render_source_pr as renderer
import generate

BASE, HEAD, RENDERED = 'a' * 40, 'b' * 40, 'c' * 40
DAY = date(2026, 10, 26)


def fixture():
    issue = json.loads((REPO / 'content/issue-053.json').read_text(encoding='utf-8'))
    issue.update(num=54, period_start='2026-10-23', period_end='2026-10-26')
    story = issue['stories'][0]
    story.update(story_id='test-source-handoff-only', event_id='test-source-handoff-only', radar_pick=True)
    story['sources'] = [story['sources'][0]]
    story['sources'][0].update(published_at='2026-10-26', retrieved_at='2026-10-26T09:30:00+08:00')
    issue['stories'] = [story]
    issue['editorial_review']['domestic_review'] = {
        'checked_sources': ['https://example.org/test-fixture'], 'notes': 'Test fixture only',
        'empty_reason': 'Test fixture only'}
    return issue


class SourcePRTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=REPO.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('content', 'issues'):
            shutil.copytree(REPO / name, self.root / name)
        for name in ('coverage.md', 'index.html'):
            shutil.copyfile(REPO / name, self.root / name)
        # Fixed pre-publication fixture: tests must keep passing after #54+ land.
        for folder, suffix in (('content', 'json'), ('issues', 'html')):
            for path in (self.root / folder).glob(f'issue-*.{suffix}'):
                if int(path.stem.split('-')[1]) > 53:
                    path.unlink()
        archive = self.root / 'issues/index.html'
        archive.write_text(re.sub(r'    <li>\s*<span class="num">#(\d+)</span>.*?</li>\n',
                           lambda m: '' if int(m[1]) > 53 else m[0],
                           archive.read_text(encoding='utf-8'), flags=re.S), encoding='utf-8')
        generate.write_outputs(self.root, generate.outputs(self.root, generate.records(self.root, DAY)))
        self.issue = fixture()
        self.raw = json.dumps(self.issue, ensure_ascii=False).encode()
        self.blob_sha = hashlib.sha1(b'blob ' + str(len(self.raw)).encode() + b'\0' + self.raw).hexdigest()
        self.pr = {'state': 'open', 'draft': False, 'user': {'login': 'therealkallen'}, 'changed_files': 1,
                   'base': {'ref': 'main', 'sha': BASE},
                   'head': {'sha': HEAD, 'ref': 'radar/issue-054',
                            'repo': {'full_name': renderer.REPOSITORY}}}
        self.files = [{'filename': 'content/issue-054.json', 'status': 'added'}]

    def test_source_only_pr_reproduces_failure_then_trusted_render_repairs_it(self):
        target = self.root / 'content/issue-054.json'
        target.write_bytes(self.raw)
        self.assertEqual(generate.main(['check', '--root', str(self.root), '--as-of', str(DAY)]), 1)
        target.unlink()
        history = {p: p.read_bytes() for p in (self.root / 'issues').glob('issue-*.html')}
        generated = renderer.render(self.root, 54, 'content/issue-054.json', self.raw, self.issue, DAY)
        self.assertEqual(set(generated), {'issues/issue-054.html', 'index.html', 'issues/index.html', 'coverage.md'})
        self.assertTrue(all(p.read_bytes() == old for p, old in history.items()))
        self.assertEqual(generate.main(['check', '--root', str(self.root), '--as-of', str(DAY)]), 0)

    def test_only_owner_same_repo_single_new_json_and_current_head_are_accepted(self):
        renderer.select_source(self.pr, self.files, renderer.REPOSITORY, HEAD, BASE)
        mutations = ('fork', 'author', 'code', 'history', 'head', 'branch', 'base', 'draft')
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                pr, files = copy.deepcopy(self.pr), copy.deepcopy(self.files)
                if mutation == 'fork': pr['head']['repo']['full_name'] = 'other/ai-radar'
                if mutation == 'author': pr['user']['login'] = 'other'
                if mutation == 'code': pr['changed_files'] = 2
                if mutation == 'history': files[0]['status'] = 'modified'
                if mutation == 'head': pr['head']['sha'] = RENDERED
                if mutation == 'branch': pr['head']['ref'] = 'main'
                if mutation == 'base': pr['base']['ref'] = 'other'
                if mutation == 'draft': pr['draft'] = True
                with self.assertRaises(ValueError):
                    renderer.select_source(pr, files, renderer.REPOSITORY, HEAD, BASE)

    def test_blob_integrity_limits_and_duplicate_keys(self):
        blob = {'encoding': 'base64', 'content': base64.b64encode(self.raw).decode(), 'size': len(self.raw)}
        self.assertEqual(renderer.parse_source(blob, self.blob_sha)[1]['num'], 54)
        for changed in (dict(blob, size=renderer.MAX_SOURCE_BYTES + 1), dict(blob, size=1)):
            with self.assertRaises(ValueError): renderer.parse_source(changed, self.blob_sha)
        with self.assertRaisesRegex(ValueError, 'SHA'):
            renderer.parse_source(blob, BASE)
        raw = b'{"num":54,"num":55}'
        sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            renderer.parse_source({'encoding': 'base64', 'content': base64.b64encode(raw).decode(),
                                   'size': len(raw)}, sha)

    def test_missing_domestic_review_and_wrong_number_never_render(self):
        issue = copy.deepcopy(self.issue)
        del issue['editorial_review']['domestic_review']
        with self.assertRaises(ValueError):
            renderer.render(self.root, 54, 'content/issue-054.json', self.raw, issue, DAY)
        self.assertFalse((self.root / 'content/issue-054.json').exists())
        with self.assertRaises(ValueError):
            renderer.render(self.root, 55, 'content/issue-055.json', self.raw, self.issue, DAY)

    def test_head_or_main_race_stops_publication(self):
        for moved in ('head', 'main'):
            def api(method, path):
                if '/pulls/' in path:
                    return {'state': 'open', 'head': {'sha': RENDERED if moved == 'head' else HEAD}}
                return {'object': {'sha': RENDERED if moved == 'main' else BASE}}
            with self.subTest(moved=moved), self.assertRaisesRegex(ValueError, 'changed'):
                renderer.unchanged(api, 1, HEAD, BASE)

    def test_api_rejects_outside_destination_without_network(self):
        with self.assertRaisesRegex(ValueError, 'destination'):
            renderer.GitHub('test-token')('POST', 'https://other.example/steal')

    def handoff(self, recovering=False, tampered=False, dispatch_error=False):
        calls = []
        self.handoff_calls = calls
        entries = [dict(path='content/issue-054.json', mode='100644', type='blob', sha=self.blob_sha)]
        if recovering:
            self.pr['head']['sha'] = RENDERED
            self.pr['changed_files'] = 5
            generated = generate.outputs(self.root, generate.records(self.root, DAY) + [self.issue])
            for name in ('issues/issue-054.html', 'index.html', 'issues/index.html', 'coverage.md'):
                raw = generated[name].encode()
                sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
                entries.append(dict(path=name, mode='100644', type='blob', sha=sha))
                self.files.append(dict(filename=name, status='added' if name.endswith('054.html') else 'modified'))
            if tampered:
                entries[-1]['sha'] = 'f' * 40
        def api(method, path, payload=None):
            calls.append((method, path, payload))
            if method == 'GET':
                if '/pulls/' in path: return self.files if '/files?' in path else self.pr
                if '/ref/heads/main' in path: return {'object': {'sha': BASE}}
                if '/compare/' in path: return {'status': 'ahead', 'behind_by': 0}
                if '/git/commits/' in path: return {'tree': {'sha': 'd' * 40}}
                if '/git/trees/' in path: return {'tree': entries}
                if '/git/blobs/' in path: return dict(encoding='base64', size=len(self.raw),
                                                     content=base64.b64encode(self.raw).decode())
            if '/git/trees' in path: return {'sha': 'e' * 40}
            if '/git/commits' in path: return {'sha': RENDERED}
            if dispatch_error and '/dispatches' in path: raise OSError('simulated dispatch timeout')
            return None
        event = self.root / 'event.json'
        event.write_text(json.dumps({'workflow_run': {'event': 'pull_request', 'head_sha': HEAD,
            'head_repository': {'full_name': renderer.REPOSITORY}, 'pull_requests': [{'number': 7}]}}))
        with patch.dict(os.environ, GITHUB_REPOSITORY=renderer.REPOSITORY,
                        GITHUB_EVENT_PATH=str(event), GH_TOKEN='fixture-token'), \
                patch.object(renderer, 'ROOT', self.root), patch.object(renderer, 'GitHub', return_value=api), \
                patch.object(renderer.generate, 'today', return_value=DAY), \
                patch.object(renderer.subprocess, 'check_output', return_value=BASE), \
                patch.object(renderer.subprocess, 'run') as tests:
            renderer.main()
        self.assertNotIn('GH_TOKEN', tests.call_args.kwargs['env'])
        return calls

    def test_full_handoff_writes_only_outputs_then_dispatches_final_ci(self):
        calls = self.handoff()
        writes = [(m, p, body) for m, p, body in calls if m != 'GET']
        self.assertEqual(len(writes), 4)
        self.assertEqual({x['path'] for x in writes[0][2]['tree']},
                         {'issues/issue-054.html', 'index.html', 'issues/index.html', 'coverage.md'})
        self.assertEqual(writes[1][2]['parents'], [HEAD])
        self.assertEqual(writes[2][2], {'sha': RENDERED, 'force': False})
        self.assertTrue(writes[2][1].endswith('/heads/radar/issue-054'))
        self.assertTrue(writes[3][1].endswith('/validate.yml/dispatches'))
        self.assertEqual(writes[3][2], {'ref': 'radar/issue-054'})

    def test_rendered_branch_can_resume_dispatch_after_partial_success(self):
        calls = self.handoff(recovering=True)
        writes = [(m, p, body) for m, p, body in calls if m != 'GET']
        self.assertEqual(len(writes), 1)
        self.assertTrue(writes[0][1].endswith('/validate.yml/dispatches'))

    def test_recovery_rejects_tampered_outputs_without_writes(self):
        with self.assertRaisesRegex(ValueError, 'does not match'):
            self.handoff(recovering=True, tampered=True)
        self.assertFalse(any(m != 'GET' for m, _, _ in self.handoff_calls))

    def test_dispatch_failure_reports_error_after_branch_write(self):
        with self.assertRaisesRegex(OSError, 'dispatch timeout'):
            self.handoff(dispatch_error=True)
        self.assertTrue(any(m == 'PATCH' for m, _, _ in self.handoff_calls))


if __name__ == '__main__':
    unittest.main()
