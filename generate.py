#!/usr/bin/env python3
"""Build the existing layout from verified records; research is done by the editor."""
import argparse
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit
import rebuild

ROOT = Path(__file__).resolve().parent
SECTIONS = tuple(rebuild.IDS)[0:5] + ("政策、监管与风险", "社媒与开发者社区观察")
PRIMARY = {
    "OpenAI": ("openai.com",), "Anthropic": ("anthropic.com",),
    "Google": ("deepmind.google", "blog.google", "ai.google.dev", "cloud.google.com"),
    "Meta": ("ai.meta.com", "about.fb.com", "research.meta.ai"),
    "Microsoft": ("microsoft.com",), "Microsoft AI": ("microsoft.ai",),
    "GitHub": ("github.com", "github.blog"), "NVIDIA": ("nvidia.com",),
    "AWS": ("aws.amazon.com",), "Mistral AI": ("mistral.ai",),
    "Hugging Face": ("huggingface.co",), "Cloudflare": ("cloudflare.com",),
    "Salesforce": ("salesforce.com",), "ServiceNow": ("servicenow.com",),
    "UiPath": ("uipath.com",), "SAP": ("sap.com",), "Adobe": ("adobe.com",),
    "Slack": ("slack.com",), "Notion": ("notion.com",), "Zoom": ("zoom.com",),
    "Vercel": ("vercel.com",), "LangChain": ("langchain.com",),
    "LlamaIndex": ("llamaindex.ai",),
    "Qwen": ("qwenlm.github.io", "aliyun.com", "alibabacloud.com",
             "github.com/QwenLM/", "huggingface.co/Qwen/"),
    "DeepSeek": ("deepseek.com", "huggingface.co/deepseek-ai/", "github.com/deepseek-ai/"),
    "智谱 AI": ("zhipuai.cn", "z.ai", "github.com/zai-org/", "huggingface.co/zai-org/"),
    "Moonshot AI": ("moonshot.cn", "kimi.com", "github.com/MoonshotAI/", "huggingface.co/moonshotai/"),
    "腾讯": ("hunyuan.tencent.com", "tencent.com"),
    "百度": ("baidu.com", "cloud.baidu.com"),
    "字节跳动": ("seed.bytedance.com", "volcengine.com"),
    "科大讯飞": ("iflytek.com", "xfyun.cn"),
    "ModelScope": ("modelscope.cn",), "arXiv": ("arxiv.org",),
    "OpenReview": ("openreview.net",),
    "European Commission": ("digital-strategy.ec.europa.eu", "ec.europa.eu"),
    "EUR-Lex": ("eur-lex.europa.eu",), "NIST": ("nist.gov",), "OECD": ("oecd.ai",),
    "UK Government": ("gov.uk",), "White House": ("whitehouse.gov",),
    "US Congress": ("congress.gov",), "Federal Register": ("federalregister.gov",),
    "Regulations.gov": ("regulations.gov",), "FTC": ("ftc.gov",),
    "US Department of Justice": ("justice.gov",), "国家网信办": ("cac.gov.cn",),
    "工信部": ("miit.gov.cn",), "中国政府网": ("gov.cn",), "市场监管总局": ("samr.gov.cn",),
    "商务部、科技部": ("mofcom.gov.cn",),
}
MEDIA = {
    "Reuters": "reuters.com", "AP": "apnews.com", "Bloomberg": "bloomberg.com",
    "FT": "ft.com", "WSJ": "wsj.com", "The Information": "theinformation.com",
    "MIT Technology Review": "technologyreview.com", "Wired": "wired.com",
    "The Verge": "theverge.com", "TechCrunch": "techcrunch.com", "CNBC": "cnbc.com",
    "Semafor": "semafor.com", "Fortune": "fortune.com",
    "机器之心": "jiqizhixin.com", "量子位": "qbitai.com", "InfoQ": "infoq.cn",
    "36氪": "36kr.com", "极客公园": "geekpark.net", "智东西": "zhidx.com", "钛媒体": "tmtpost.com",
    "Stanford HAI": "hai.stanford.edu", "CSET": "cset.georgetown.edu",
    "Brookings": "brookings.edu", "Tech Policy Press": "techpolicy.press",
}
SOCIAL = {"X": ("x.com",), "Reddit": ("reddit.com",),
          "Hacker News": ("news.ycombinator.com",), "GitHub Community": ("github.com",)}
BLOCKED = {"aitoolly.com", "thirdruntime.com", "csdn.net", "baijiahao.baidu.com",
           "biggo.com", "gaana.com", "stockalpha.ai", "agihunt.info",
           "theautomateddaily.com", "genaicrib.com"}
BEGIN, END = "<!-- RADAR CONTENT START -->", "<!-- RADAR CONTENT END -->"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def today():
    return datetime.now(timezone(timedelta(hours=8))).date()


def text_field(obj, key):
    value = obj.get(key)
    require(isinstance(value, str) and bool(value.strip()), f"Missing {key}")
    return value


def validate_source(source, start, end):
    url = text_field(source, "canonical_url")
    require(source.get("source_url") == url, "Source and canonical URL must match")
    parsed = urlsplit(url)
    host = (parsed.hostname or "").removeprefix("www.")
    require(parsed.scheme == "https" and host and not parsed.username and not parsed.password,
            "Invalid source URL")
    require(not parsed.fragment and not any(c in url for c in '"<>\r\n'), "Unsafe source URL")
    require(source.get("source_domain") == host, "Source domain mismatch")
    require(not any(host == d or host.endswith("." + d) for d in BLOCKED), "Blocked source")
    name, tier = source.get("source_name"), source.get("source_tier")
    if tier == "primary":
        identity = host + parsed.path
        require(any(identity.startswith(d) if "/" in d else host == d or host.endswith("." + d)
                    for d in PRIMARY.get(name, ())), "Primary source name/domain not allowlisted")
    elif tier == "trusted_media":
        domain = MEDIA.get(name)
        require(domain and (host == domain or host.endswith("." + domain)), "Media name/domain mismatch")
    else:
        require(tier == "social_signal" and host in SOCIAL.get(name, ()), "Social name/domain mismatch")
    published = date.fromisoformat(text_field(source, "published_at"))
    require(start <= published <= end, "Source outside issue window")
    retrieved = datetime.fromisoformat(text_field(source, "retrieved_at"))
    require(retrieved.tzinfo is not None and retrieved.date() >= published, "Invalid retrieval timestamp")
    for key in ("raw_title", "evidence_type", "raw_excerpt", "evidence_notes"):
        text_field(source, key)
    require(source.get("opened_and_verified") is True, "Source not opened and verified")


def validate_issue(issue, as_of):
    require(type(issue.get("num")) is int and issue["num"] > 50, "Continue after issue 50")
    start = date.fromisoformat(text_field(issue, "period_start"))
    end = date.fromisoformat(text_field(issue, "period_end"))
    require(start < end <= as_of and end.weekday() in (0, 2, 4), "Invalid issue dates")
    require(end == next_date(start), "Skipped publication date")
    text_field(issue, "window_note")
    review = issue.get("editorial_review", {})
    require(review.get("source_first") is True and review.get("semantic_dedup") is True,
            "Editorial source and semantic dedup review required")
    text_field(review, "notes")
    stories = issue.get("stories")
    require(isinstance(stories, list) and stories, "No verified stories: refuse empty issue")
    ids = set()
    for story in stories:
        for key in ("story_id", "event_id", "title", "summary", "label", "dedup_notes"):
            text_field(story, key)
        require(story["story_id"] not in ids, "Duplicate story ID within issue")
        ids.add(story["story_id"])
        require(story.get("primary_category") in SECTIONS, "Unknown section")
        require(story.get("verified") is True, "Unverified story")
        require(type(story.get("radar_pick")) is bool, "radar_pick must be boolean")
        require(type(story.get("major_claim")) is bool, "major_claim must be boolean")
        sources = story.get("sources")
        require(isinstance(sources, list) and sources, "Missing source_record")
        for source in sources:
            validate_source(source, start, end)
            if source["source_tier"] == "social_signal":
                require(story["primary_category"] == "社媒与开发者社区观察",
                        "Social signals must stay in community observations")
                require(story.get("evidence_type") == "community_observation",
                        "Identify community observations explicitly")
        if story.get("major_claim"):
            official = any(s["source_tier"] == "primary" for s in sources)
            outlets = {MEDIA[s["source_name"]] for s in sources if s["source_tier"] == "trusted_media"}
            require(official or len(outlets) >= 2, "Major claim lacks official or two independent sources")
    require(any(s["radar_pick"] for s in stories), "Select Radar Picks from canonical stories")
    if issue["num"] >= 54:
        domestic = review.get("domestic_review")
        require(isinstance(domestic, dict), "Domestic source review required")
        checked = domestic.get("checked_sources")
        require(isinstance(checked, list) and checked and
                all(isinstance(s, str) and s.strip() for s in checked),
                "Record checked domestic sources")
        text_field(domestic, "notes")
        if not any(s["primary_category"] == "国内 AI 动态" for s in stories):
            text_field(domestic, "empty_reason")


def next_date(day):
    day += timedelta(days=1)
    while day.weekday() not in (0, 2, 4):
        day += timedelta(days=1)
    return day


def records(root, as_of):
    issues, ids, previous = [], set(), None
    for path in sorted((root / "content").glob("issue-*.json"), key=lambda p: int(p.stem.split("-")[1])):
        issue = json.loads(path.read_text(encoding="utf-8"))
        validate_issue(issue, as_of)
        require(path.name == f"issue-{issue['num']:03d}.json", "Filename/number mismatch")
        if previous:
            require(issue["num"] == previous["num"] + 1, "Gap in issue numbers")
            require(issue["period_start"] == previous["period_end"], "Gap in coverage windows")
            require(issue["period_end"] == next_date(date.fromisoformat(previous["period_end"])).isoformat(),
                    "Skipped publication date")
        for story in issue["stories"]:
            require(story["story_id"] not in ids, "Duplicate canonical story across issues")
            ids.add(story["story_id"])
        issues.append(issue)
        previous = issue
    return issues


def date_label(issue):
    start, end = date.fromisoformat(issue["period_start"]), date.fromisoformat(issue["period_end"])
    return start.strftime("%Y.%m.%d") + " — " + end.strftime("%m.%d" if start.year == end.year else "%Y.%m.%d")


def render_issue(issue, archived=False):
    def row(story, pick=False):
        source = story["sources"][0]
        return (story["primary_category"] if pick else story["label"], story["title"],
                html.escape(story["summary"]), source["source_name"], source["canonical_url"])
    data = {"num": issue["num"], "date": date_label(issue),
            "picks": [row(s, True) for s in issue["stories"] if s["radar_pick"]],
            "sections": [(name, [row(s) for s in issue["stories"] if s["primary_category"] == name])
                         for name in SECTIONS]}
    output = rebuild.render(data)
    return output.replace('href="issues/"', 'href="index.html"') if archived else output


def outputs(root, issues):
    require(issues and issues[0]["num"] == 51 and issues[0]["period_start"] == "2026-10-16",
            "Migration must start after issue 50 (2026-10-16)")
    for number in range(1, 51):
        require((root / "issues" / f"issue-{number:03d}.html").is_file(), "Missing historical issue")
    last = max(int(p.stem.split("-")[1]) for p in (root / "issues").glob("issue-*.html"))
    require(last <= issues[-1]["num"], "Refuse to roll back a newer homepage")
    result = {f"issues/issue-{i['num']:03d}.html": render_issue(i, True) for i in issues}
    result["index.html"] = render_issue(issues[-1])
    archive = (root / "issues/index.html").read_text(encoding="utf-8")
    for issue in issues:
        archive = re.sub(r'    <li>\s*<span class="num">#' + str(issue["num"]) + r'</span>.*?</li>\n',
                         "", archive, flags=re.S)
    marker = '  <ul class="archive-list">\n'
    require(archive.count(marker) == 1, "Archive insertion point missing or ambiguous")
    entries = "".join(f'    <li>\n      <span class="num">#{i["num"]}</span>\n'
                      f'      <span class="info">\n        <a href="issue-{i["num"]:03d}.html">第{i["num"]}期</a>\n'
                      f'        <div class="date">{date_label(i)}</div>\n      </span>\n    </li>\n'
                      for i in reversed(issues))
    result["issues/index.html"] = archive.replace(marker, marker + entries, 1)
    coverage = (root / "coverage.md").read_text(encoding="utf-8")
    require(coverage.count(BEGIN) == coverage.count(END) <= 1, "Invalid coverage markers")
    coverage = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END) + r'\n*', "", coverage, flags=re.S)
    block = [BEGIN, "", "## 接手后补刊与更新（来源记录见 content/）", ""]
    for issue in issues:
        block += [f"### 第 {issue['num']} 期（{date_label(issue)}）", "", issue["window_note"], ""]
        block += [f"- {s['title']}（{s['sources'][0]['canonical_url']}；{s['sources'][0]['published_at']}）。{s['dedup_notes']}"
                  for s in issue["stories"]]
        block += [""]
    block += [END, ""]
    anchor = "## 去重机制"
    require(anchor in coverage, "Coverage insertion point missing")
    result["coverage.md"] = coverage.replace(anchor, "\n".join(block) + "\n" + anchor, 1)
    return result


@contextmanager
def build_lock(root):
    lock = root / ".radar-build.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        raise ValueError("Another build holds .radar-build.lock; inspect before removing stale lock")
    try:
        yield
    finally:
        lock.rmdir()


def write_outputs(root, generated):
    """Stage everything before replacement; restore original bytes on write failure."""
    originals, replaced = {}, []
    with tempfile.TemporaryDirectory(prefix=".radar-stage-", dir=root) as temp:
        for relative, content in generated.items():
            target, staged = root / relative, Path(temp) / relative
            originals[relative] = target.read_bytes() if target.exists() else None
            staged.parent.mkdir(parents=True, exist_ok=True)
            staged.write_bytes(content.encode("utf-8"))
        try:
            for relative in generated:
                if originals[relative] != generated[relative].encode("utf-8"):
                    os.replace(Path(temp) / relative, root / relative)
                    replaced.append(relative)
        except OSError:
            for relative in reversed(replaced):
                original = originals[relative]
                if original is None:
                    (root / relative).unlink()
                else:
                    (root / relative).write_bytes(original)
            raise
    return replaced


def missing_dates(root, as_of):
    archives = sorted((root / "issues").glob("issue-*.html"), key=lambda p: int(p.stem.split("-")[1]))
    require(archives, "No archive: refuse to reset numbering")
    latest = archives[-1]
    match = re.search(r'<div class="meta"><span>(\d{4})\.(\d{2})\.\d{2} — (?:(\d{4})\.)?(\d{2})\.(\d{2})</span>',
                      latest.read_text(encoding="utf-8"))
    require(match, "Cannot determine last publication date")
    year, _, end_year, month, day = match.groups()
    due = next_date(date(int(end_year or year), int(month), int(day)))
    number, missing = int(latest.stem.split("-")[1]) + 1, []
    while due <= as_of:
        missing.append({"num": number, "date": due.isoformat()})
        due, number = next_date(due), number + 1
    return missing


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("plan", "build", "check"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--as-of", type=date.fromisoformat, default=today())
    parser.add_argument("--require-current", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == "plan":
            missing = missing_dates(root, args.as_of)
            print(json.dumps({"timezone": "Asia/Shanghai (UTC+8)", "missing": missing}, ensure_ascii=False))
            return int(bool(missing) and args.require_current)
        with build_lock(root):
            issues = records(root, args.as_of)
            generated = outputs(root, issues)
            if args.command == "check":
                stale = [p for p, content in generated.items()
                         if not (root / p).exists() or (root / p).read_bytes() != content.encode("utf-8")]
                require(not stale, "Stale generated files: " + ", ".join(stale))
                print(f"PASS: {len(issues)} content records; {len(generated)} generated files match")
            else:
                changed = write_outputs(root, generated)
                print(json.dumps({"status": "built", "latest_issue": issues[-1]["num"], "changed": changed}))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"BUILD_FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
