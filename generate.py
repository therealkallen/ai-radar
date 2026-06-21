#!/usr/bin/env python3
"""AI Radar 自动生成器
每周一三五自动：搜索AI新闻 → 生成HTML → 推送到GitHub Pages
"""

import json, os, re, subprocess, sys, textwrap, time, urllib3
from datetime import date, datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

REPO_DIR = Path("/workspace/ai-radar")
TOKEN_FILE = Path("/root/.config/ai-radar/gh_token")
USER = "therealkallen"
REPO = "ai-radar"

MONTH_NAMES = ["", "1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]

def get_token():
    return TOKEN_FILE.read_text().strip()

def fetch_news():
    """从多个来源获取本周AI新闻"""
    today = date.today()
    news = []

    # 来源1: AI Daily Post 月度存档
    try:
        r = requests.get(f"https://aidailypost.com/archives/{today.year}/{today.month:02d}", timeout=15)
        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            # 尝试提取文章列表
            articles = soup.select("article, .post, .entry, li a[href*='ai']")
            for a in articles[:30]:
                title_el = a.select_one("h2, h3, .entry-title, a")
                if title_el and title_el.get_text(strip=True):
                    title = title_el.get_text(strip=True)
                    link = title_el.get("href", "")
                    if link and not link.startswith("http"):
                        link = "https://aidailypost.com" + link
                    if title and len(title) > 10:
                        news.append({"title": title, "url": link, "source": "AI Daily Post"})
    except Exception as e:
        print(f"  [warn] AI Daily Post: {e}")

    # 来源2: TrendingAI
    try:
        r = requests.get("https://trendingai.cn/", timeout=15)
        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            for item in soup.select("a[href*='trending'], .item, .post-title, h2 a, h3 a")[:20]:
                text = item.get_text(strip=True)
                link = item.get("href", "")
                if text and len(text) > 10:
                    if link and not link.startswith("http"):
                        link = "https://trendingai.cn" + link
                    news.append({"title": text, "url": link, "source": "TrendingAI"})
    except Exception as e:
        print(f"  [warn] TrendingAI: {e}")

    return news


def fetch_reddit():
    """获取 Reddit AI 热门讨论"""
    posts = []
    
    for sub, label in [("LocalLLaMA", "r/LocalLLaMA"), ("singularity", "r/singularity")]:
        try:
            r = requests.get(
                f"https://www.reddit.com/r/{sub}/hot/.json?limit=15",
                headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) ai-radar/1.0"},
                timeout=15,
                verify=False
            )
            if r.ok:
                data = r.json()
                for post in data.get("data", {}).get("children", []):
                    p = post["data"]
                    if p.get("title"):
                        posts.append({
                            "title": p["title"],
                            "score": p.get("score", 0),
                            "comments": p.get("num_comments", 0),
                            "url": f"https://reddit.com{p.get('permalink', '')}",
                            "subreddit": label
                        })
        except Exception:
            pass  # Reddit 可能被网络限制，跳过

    posts.sort(key=lambda x: x["score"], reverse=True)
    return posts[:10]


def generate_html(news, reddit, today):
    """生成 HTML 页面"""
    date_range = f"{(today.isocalendar()[0])}.{today.month:02d}.{today.day-6:02d} — {today.month:02d}.{today.day:02d}"

    news_items_html = ""
    for n in news[:20]:
        url_part = f'<a class="source-link" href="{n["url"]}" target="_blank">来源 · {n["source"]} →</a>' if n.get("url") else ""
        news_items_html += f"""
    <div class="news-item">
      <div class="label">{n.get("source","")}</div>
      <div class="title">{n["title"]}</div>
      <div class="summary">{n.get("summary","")}</div>
      {url_part}
    </div>"""

    reddit_items = ""
    for p in reddit[:8]:
        reddit_items += f"""
    <div class="news-item">
      <div class="label">{p["subreddit"]} · 👍 {p["score"]} · 💬 {p["comments"]}</div>
      <div class="title">{p["title"]}</div>
      <a class="source-link" href="{p["url"]}" target="_blank">查看讨论 →</a>
    </div>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Radar · {today.month}月{today.day}日</title>
<style>
  *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: 'Georgia', 'Noto Serif SC', 'Times New Roman', serif;
    background: #f7f5f0; color: #2c2c2c; line-height: 1.7; font-size: 15px;
    padding-top: 56px;
  }}
  .topnav {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    background: rgba(247,245,240,0.92); backdrop-filter: blur(8px);
    border-bottom: 1px solid #e6e3db;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none;
  }}
  .topnav::-webkit-scrollbar {{ display: none; }}
  .topnav-inner {{
    display: flex; align-items: center; gap: 4px;
    max-width: 768px; margin: 0 auto; padding: 10px 20px; white-space: nowrap;
  }}
  .topnav .brand {{ font-weight: 700; font-size: 14px; color: #1a1a1a; margin-right: 12px; flex-shrink: 0; }}
  .topnav a {{
    font-size: 13px; color: #888; text-decoration: none;
    padding: 5px 12px; border-radius: 6px; transition: background 0.2s, color 0.2s; flex-shrink: 0;
  }}
  .topnav a:hover {{ background: #edeae3; color: #2c2c2c; }}
  .container {{ max-width: 720px; margin: 0 auto; padding: 40px 24px 64px; }}
  .masthead {{ margin-bottom: 36px; }}
  .masthead h1 {{ font-size: 28px; font-weight: 700; color: #1a1a1a; margin-bottom: 6px; }}
  .masthead .meta {{
    font-size: 13px; color: #888; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    border-bottom: 1px solid #e6e3db; padding-bottom: 14px;
  }}
  .masthead .meta span {{ margin-right: 16px; }}
  .section {{ margin-bottom: 40px; scroll-margin-top: 72px; }}
  .section-header {{
    font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #999;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-weight: 600; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 1px solid #e6e3db;
  }}
  .news-item {{ padding: 12px 0; border-bottom: 1px solid #eeeae1; }}
  .news-item:first-child {{ padding-top: 0; }}
  .news-item:last-child {{ border-bottom: none; padding-bottom: 0; }}
  .news-item .label {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    display: inline-block; font-size: 11px; font-weight: 600; color: #999; margin-bottom: 3px;
  }}
  .news-item .title {{ font-size: 15px; font-weight: 700; color: #1a1a1a; margin-bottom: 4px; }}
  .news-item .summary {{ font-size: 14px; color: #555; }}
  .news-item .source-link {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 12px; color: #aaa; text-decoration: none; margin-top: 4px; display: inline-block;
  }}
  .news-item .source-link:hover {{ color: #555; }}
  .footer {{
    text-align: center; font-size: 12px; color: #bbb;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    margin-top: 40px; padding-top: 20px; border-top: 1px solid #e6e3db;
  }}
  @media (max-width: 600px) {{
    body {{ padding-top: 50px; }}
    .topnav-inner {{ padding: 8px 14px; }}
    .topnav .brand {{ font-size: 13px; margin-right: 8px; }}
    .topnav a {{ font-size: 12px; padding: 4px 10px; }}
    .container {{ padding: 24px 16px 48px; }}
    .masthead h1 {{ font-size: 22px; }}
  }}
</style>
</head>
<body>
<nav class="topnav">
  <div class="topnav-inner">
    <span class="brand">AI Radar</span>
    <a href="#news">新闻</a>
    <a href="#reddit">社区</a>
  </div>
</nav>
<div class="container">
  <div class="masthead">
    <h1>AI Radar</h1>
    <div class="meta"><span>{date_range}</span><span>自动生成</span></div>
  </div>

  <div class="section" id="news">
    <div class="section-header">AI 新闻速览</div>
    {news_items_html}
  </div>

  <div class="section" id="reddit">
    <div class="section-header">Reddit 社区热议</div>
    {reddit_items}
  </div>

  <div class="footer">
    <p>AI Radar · 自动追踪 AI 行业动态</p>
    <p style="margin-top:4px;">数据来源: AI Daily Post / TrendingAI / Reddit</p>
  </div>
</div>
</body>
</html>"""
    return html


def push_to_github(today):
    """推送更新到 GitHub"""
    token = get_token()
    repo_dir = REPO_DIR

    # 更新远程 URL
    subprocess.run(["git", "-C", str(repo_dir), "remote", "set-url", "origin",
                    f"https://therealkallen:{token}@github.com/{USER}/{REPO}.git"],
                   capture_output=True)
    
    # pull
    subprocess.run(["git", "-C", str(repo_dir), "pull", "origin", "main"], capture_output=True)
    
    # commit & push
    r = subprocess.run(["git", "-C", str(repo_dir), "add", "index.html"], capture_output=True)
    r = subprocess.run(["git", "-C", str(repo_dir), "commit", "-m",
                        f"auto: AI Radar {today.year}.{today.month:02d}.{today.day:02d}"],
                       capture_output=True)
    if r.returncode != 0:
        print("  No changes to commit")
        return False
    
    r = subprocess.run(["git", "-C", str(repo_dir), "push", "origin", "main"], capture_output=True)
    if r.returncode == 0:
        print("  Pushed successfully!")
        return True
    else:
        print(f"  Push failed: {r.stderr.decode()}")
        return False


def main():
    today = date.today()
    weekday_names = ["周一","周二","周三","周四","周五","周六","周日"]
    print(f"🤖 AI Radar Auto-Generator")
    print(f"📅 {today.year}年{today.month}月{today.day}日 {weekday_names[today.weekday()]}")
    print()
    
    print("📡 Fetching news...")
    news = fetch_news()
    print(f"   Got {len(news)} news items")
    
    print("👽 Fetching Reddit...")
    reddit = fetch_reddit()
    print(f"   Got {len(reddit)} hot posts")

    print("📝 Generating HTML...")
    html = generate_html(news, reddit, today)
    out_path = REPO_DIR / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"   Written to {out_path}")

    print("🚀 Pushing to GitHub...")
    pushed = push_to_github(today)
    
    if pushed:
        pages_url = f"https://{USER}.github.io/{REPO}/"
        print(f"\n✅ Done! Published at: {pages_url}")
    else:
        print("\n✅ HTML generated (no new changes to push)")


if __name__ == "__main__":
    main()
