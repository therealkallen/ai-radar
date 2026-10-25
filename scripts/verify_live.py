"""Read public Pages from a networked runner, comparing exact committed bytes."""
import hashlib
import json
from pathlib import Path
import sys
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://therealkallen.github.io/ai-radar/'


def expected_pages(root):
    records = sorted((root / 'content').glob('issue-*.json'),
                     key=lambda p: int(p.stem.split('-')[1]))
    if not records:
        raise ValueError('No content records: refuse unscoped live check')
    number = json.loads(records[-1].read_text(encoding='utf-8'))['num']
    return ['index.html', 'issues/index.html', f'issues/issue-{number:03d}.html']


def fetch(url):
    request = Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'AI-Radar-live-verification'})
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise ValueError(f'HTTP {response.status}')
        return response.read()


def verify(root=ROOT, read=fetch, attempts=6, delay=10, sleep=time.sleep):
    expected = {path: (root / path).read_bytes() for path in expected_pages(root)}
    report = {'verified': False, 'pages': []}
    for attempt in range(1, attempts + 1):
        pages = []
        for path, body in expected.items():
            url = BASE + path
            try:
                actual = read(url)
                pages.append({'url': url, 'matches_committed_html': actual == body,
                              'sha256': hashlib.sha256(actual).hexdigest()})
            except (OSError, ValueError) as error:
                pages.append({'url': url, 'matches_committed_html': False, 'error': str(error)})
        report = {'verified': all(p['matches_committed_html'] for p in pages),
                  'attempt': attempt, 'pages': pages}
        if report['verified']:
            break
        if attempt < attempts:
            sleep(delay)
    return report


def main():
    report = verify()
    output = json.dumps(report, ensure_ascii=False, indent=2)
    (ROOT / 'live-verification.json').write_text(output + '\n', encoding='utf-8')
    print(output)
    return 0 if report['verified'] else 1


if __name__ == '__main__':
    sys.exit(main())
