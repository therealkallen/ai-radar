import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('verify_live', Path(__file__).resolve().parents[1] / 'scripts/verify_live.py')
live = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(live)


class LiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'content').mkdir()
        (self.root / 'issues').mkdir()
        (self.root / 'content/issue-053.json').write_text(json.dumps({'num': 53}))
        self.paths = ['index.html', 'issues/index.html', 'issues/issue-053.html']
        for path in self.paths:
            (self.root / path).write_bytes(path.encode())

    def test_matches_committed_pages(self):
        seen = []
        def read(url):
            path = url.removeprefix(live.BASE)
            seen.append(path)
            return path.encode()
        self.assertTrue(live.verify(self.root, read, attempts=1)['verified'])
        self.assertEqual(seen, self.paths)

    def test_stale_page_cannot_report_success(self):
        report = live.verify(self.root, lambda url: b'old issue', attempts=1)
        self.assertFalse(report['verified'])

    def test_network_failure_is_reported_and_retry_is_bounded(self):
        calls, sleeps = [], []
        def read(url):
            calls.append(url)
            raise OSError('DNS lookup failed')
        report = live.verify(self.root, read, attempts=2, sleep=sleeps.append)
        self.assertFalse(report['verified'])
        self.assertEqual(len(calls), 6)
        self.assertEqual(sleeps, [10])
        self.assertIn('DNS', report['pages'][0]['error'])

    def test_cdn_can_catch_up_on_second_attempt(self):
        calls = []
        def read(url):
            calls.append(url)
            return b'stale' if len(calls) <= 3 else url.removeprefix(live.BASE).encode()
        report = live.verify(self.root, read, attempts=2, sleep=lambda _: None)
        self.assertTrue(report['verified'])
        self.assertEqual(report['attempt'], 2)

    def test_no_records_is_an_error(self):
        (self.root / 'content/issue-053.json').unlink()
        with self.assertRaises(ValueError):
            live.expected_pages(self.root)
