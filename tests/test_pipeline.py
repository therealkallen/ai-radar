"""Regression coverage for the failure modes in the legacy publisher."""
import copy
from datetime import date
import hashlib
from html.parser import HTMLParser
import json
import re
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate
import rebuild

REPO = Path(__file__).resolve().parents[1]
AS_OF = date(2026, 10, 22)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.hrefs.append(attrs["href"])


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=REPO.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "issues").mkdir()
        (self.root / "content").mkdir()
        for number in range(1, 51):
            name = f"issue-{number:03d}.html"
            shutil.copyfile(REPO / "issues" / name, self.root / "issues" / name)
        for number in (51, 52):
            name = f"issue-{number:03d}.json"
            shutil.copyfile(REPO / "content" / name, self.root / "content" / name)
        archive = (REPO / "issues/index.html").read_text(encoding="utf-8")
        archive = re.sub(r'    <li>\s*<span class="num">#(\d+)</span>.*?</li>\n',
                         lambda m: "" if int(m[1]) > 50 else m[0], archive, flags=re.S)
        (self.root / "issues/index.html").write_text(archive, encoding="utf-8")
        for name in ("index.html", "coverage.md"):
            shutil.copyfile(REPO / name, self.root / name)
        self.issue = json.loads((self.root / "content/issue-051.json").read_text(encoding="utf-8"))
        generate.write_outputs(self.root, generate.outputs(self.root, generate.records(self.root, AS_OF)))

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.root.rglob("*") if p.is_file()}

    def save(self, issue):
        (self.root / "content" / f"issue-{issue['num']:03d}.json").write_text(
            json.dumps(issue, ensure_ascii=False), encoding="utf-8")

    def test_original_missing_dates_and_numbering(self):
        for number in (51, 52):
            (self.root / "issues" / f"issue-{number:03d}.html").unlink(missing_ok=True)
        self.assertEqual(generate.missing_dates(self.root, AS_OF),
                         [{"num": 51, "date": "2026-10-19"}, {"num": 52, "date": "2026-10-21"}])

    def test_month_and_year_boundaries(self):
        self.assertEqual(generate.next_date(date(2026, 10, 30)), date(2026, 11, 2))
        self.assertEqual(generate.next_date(date(2026, 12, 30)), date(2027, 1, 1))
        issue = dict(self.issue, period_start="2026-12-30", period_end="2027-01-01")
        self.assertEqual(generate.date_label(issue), "2026.12.30 — 2027.01.01")

    def test_empty_content_cannot_overwrite_site(self):
        self.issue["stories"] = []
        self.save(self.issue)
        before = self.snapshot()
        self.assertEqual(generate.main(["build", "--root", str(self.root), "--as-of", str(AS_OF)]), 1)
        self.assertEqual(self.snapshot(), before)

    def test_unverified_missing_or_mismatched_sources_are_rejected(self):
        for mutation in ("unverified", "no_record", "domain", "publisher", "blocked", "future"):
            with self.subTest(mutation=mutation):
                issue = copy.deepcopy(self.issue)
                story = issue["stories"][0]
                source = story["sources"][0]
                if mutation == "unverified":
                    source["opened_and_verified"] = False
                elif mutation == "no_record":
                    story["sources"] = []
                elif mutation == "domain":
                    source["source_domain"] = "reuters.com"
                elif mutation == "publisher":
                    source["source_name"] = "OpenAI"
                elif mutation == "blocked":
                    source.update(source_url="https://thirdruntime.com/a",
                                  canonical_url="https://thirdruntime.com/a", source_domain="thirdruntime.com")
                else:
                    source["published_at"] = "2026-10-22"
                with self.assertRaises(ValueError):
                    generate.validate_issue(issue, AS_OF)

    def test_major_claim_requires_independent_evidence(self):
        source = self.issue["stories"][0]["sources"][0]
        source.update(source_name="Reuters", source_tier="trusted_media",
                      source_url="https://reuters.com/a", canonical_url="https://reuters.com/a",
                      source_domain="reuters.com")
        self.issue["stories"][0]["sources"] = [source, copy.deepcopy(source)]
        with self.assertRaisesRegex(ValueError, "Major claim"):
            generate.validate_issue(self.issue, AS_OF)
        second = self.issue["stories"][0]["sources"][1]
        second.update(source_domain="cn.reuters.com", source_url="https://cn.reuters.com/b",
                      canonical_url="https://cn.reuters.com/b")
        with self.assertRaisesRegex(ValueError, "Major claim"):
            generate.validate_issue(self.issue, AS_OF)

    def test_policy_permitted_sources_and_social_boundaries(self):
        source = copy.deepcopy(self.issue["stories"][0]["sources"][0])
        for name, domain, tier in (("NVIDIA", "blogs.nvidia.com", "primary"),
                                   ("The Verge", "theverge.com", "trusted_media"),
                                   ("Hacker News", "news.ycombinator.com", "social_signal")):
            with self.subTest(name=name):
                source.update(source_name=name, source_domain=domain, source_tier=tier,
                              source_url=f"https://{domain}/a", canonical_url=f"https://{domain}/a")
                generate.validate_source(source, date(2026, 10, 16), date(2026, 10, 19))
        story = self.issue["stories"][0]
        story.update(sources=[source], major_claim=False)
        with self.assertRaisesRegex(ValueError, "community observations"):
            generate.validate_issue(self.issue, AS_OF)
        story.update(primary_category="社媒与开发者社区观察", evidence_type="community_observation")
        generate.validate_issue(self.issue, AS_OF)
        story["major_claim"] = True
        with self.assertRaisesRegex(ValueError, "Major claim"):
            generate.validate_issue(self.issue, AS_OF)

    def test_domestic_review_required_for_future_issues_even_when_empty(self):
        issue = copy.deepcopy(self.issue)
        issue["num"] = 54
        issue["stories"] = [s for s in issue["stories"] if s["primary_category"] != "国内 AI 动态"]
        with self.assertRaisesRegex(ValueError, "Domestic source review"):
            generate.validate_issue(issue, AS_OF)
        review = {"checked_sources": [], "notes": "Checked official announcements"}
        issue["editorial_review"]["domestic_review"] = review
        with self.assertRaisesRegex(ValueError, "checked domestic sources"):
            generate.validate_issue(issue, AS_OF)
        review["checked_sources"] = ["https://www.deepseek.com/"]
        with self.assertRaisesRegex(ValueError, "empty_reason"):
            generate.validate_issue(issue, AS_OF)
        review["empty_reason"] = "All candidates predate the issue window or repeat previous coverage."
        generate.validate_issue(issue, AS_OF)
        del review["empty_reason"]
        issue["stories"][0]["primary_category"] = "国内 AI 动态"
        generate.validate_issue(issue, AS_OF)

    def test_iflytek_identity_is_limited_to_official_domains(self):
        source = copy.deepcopy(self.issue["stories"][0]["sources"][0])
        source.update(source_name="科大讯飞", source_tier="primary")
        for host, accepted in (("edu.iflytek.com", True), ("maas.xfyun.cn", True),
                               ("iflytek.com.example.org", False), ("notiflytek.com", False)):
            with self.subTest(host=host):
                source.update(source_domain=host, source_url=f"https://{host}/news",
                              canonical_url=f"https://{host}/news")
                if accepted:
                    generate.validate_source(source, date(2026, 10, 16), date(2026, 10, 19))
                else:
                    with self.assertRaisesRegex(ValueError, "allowlisted"):
                        generate.validate_source(source, date(2026, 10, 16), date(2026, 10, 19))

    def test_duplicate_story_is_rejected_but_followup_allowed(self):
        issue52 = json.loads((self.root / "content/issue-052.json").read_text(encoding="utf-8"))
        issue52["stories"][0]["story_id"] = self.issue["stories"][0]["story_id"]
        self.save(issue52)
        with self.assertRaisesRegex(ValueError, "Duplicate canonical"):
            generate.records(self.root, AS_OF)
        issue52["stories"][0]["story_id"] += "-new-stage"
        issue52["stories"][0]["event_id"] = self.issue["stories"][0]["event_id"]
        self.save(issue52)
        self.assertEqual(len(generate.records(self.root, AS_OF)), 2)

    def test_gap_and_wrong_filename_rejected(self):
        issue52 = json.loads((self.root / "content/issue-052.json").read_text(encoding="utf-8"))
        issue52["period_start"] = "2026-10-20"
        self.save(issue52)
        with self.assertRaisesRegex(ValueError, "Gap in coverage"):
            generate.records(self.root, AS_OF)
        self.save(dict(issue52, period_start="2026-10-19"))
        (self.root / "content/issue-053.json").write_bytes((self.root / "content/issue-052.json").read_bytes())
        with self.assertRaisesRegex(ValueError, "Filename"):
            generate.records(self.root, AS_OF)

    def test_build_is_idempotent_and_preserves_history(self):
        before = {p.name: p.read_bytes() for p in (self.root / "issues").glob("issue-*.html")
                  if int(p.stem.split("-")[1]) <= 50}
        args = ["--root", str(self.root), "--as-of", str(AS_OF)]
        self.assertEqual(generate.main(["build", *args]), 0)
        first = self.snapshot()
        self.assertEqual(generate.main(["build", *args]), 0)
        self.assertEqual(first, self.snapshot())
        for name, value in before.items():
            self.assertEqual((self.root / "issues" / name).read_bytes(), value)
        archive = (self.root / "issues/index.html").read_text(encoding="utf-8")
        self.assertEqual(archive.count('href="issue-051.html"'), 1)
        self.assertEqual(archive.count('href="issue-052.html"'), 1)
        self.assertEqual(generate.main(["check", *args]), 0)

    def test_stale_outputs_fail_check(self):
        (self.root / "index.html").write_text("broken", encoding="utf-8")
        self.assertEqual(generate.main(["check", "--root", str(self.root), "--as-of", str(AS_OF)]), 1)

    def test_ambiguous_archive_refuses_all_writes(self):
        path = self.root / "issues/index.html"
        path.write_text("lost insertion point", encoding="utf-8")
        before = self.snapshot()
        self.assertEqual(generate.main(["build", "--root", str(self.root), "--as-of", str(AS_OF)]), 1)
        self.assertEqual(before, self.snapshot())

    def test_write_failure_restores_original_files(self):
        before = self.snapshot()
        replace = generate.os.replace
        attempts = 0

        def failing_replace(source, target):
            nonlocal attempts
            attempts += 1
            if attempts == 2:
                raise OSError("simulated disk failure")
            return replace(source, target)

        with patch.object(generate.os, "replace", side_effect=failing_replace):
            with self.assertRaises(OSError):
                generate.write_outputs(self.root, {"index.html": "changed", "coverage.md": "changed"})
        self.assertEqual(before, self.snapshot())

    def test_concurrent_build_keeps_existing_lock(self):
        lock = self.root / ".radar-build.lock"
        lock.mkdir()
        self.assertEqual(generate.main(["build", "--root", str(self.root)]), 1)
        self.assertTrue(lock.exists())

    def test_rollback_to_older_issue_refused(self):
        (self.root / "issues/issue-053.html").write_text("a newer issue", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "roll back"):
            generate.outputs(self.root, generate.records(self.root, AS_OF))

    def test_untrusted_text_is_escaped_and_layout_retained(self):
        self.issue["stories"][0]["title"] = "<script>alert(1)</script>"
        self.issue["stories"][0]["summary"] = '<img src=x onerror="alert(1)">'
        output = generate.render_issue(self.issue)
        self.assertNotIn("<script>", output)
        self.assertNotIn("<img ", output)
        self.assertIn(rebuild.CSS, output)
        self.assertIn(rebuild.NAV, output)

    def test_all_local_links_and_sections_resolve(self):
        for relative, output in generate.outputs(self.root, generate.records(self.root, AS_OF)).items():
            if not relative.endswith(".html"):
                continue
            links = Links()
            links.feed(output)
            for href in links.hrefs:
                if href.startswith("#"):
                    self.assertIn(href[1:], links.ids)
                elif not href.startswith("https://"):
                    self.assertTrue((self.root / relative).parent.joinpath(href).exists(), (relative, href))

    def test_currentness_has_failure_exit_status(self):
        self.assertEqual(generate.main(["plan", "--root", str(self.root),
                                       "--as-of", "2026-10-23", "--require-current"]), 1)


if __name__ == "__main__":
    unittest.main()
