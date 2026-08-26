# -*- coding: utf-8 -*-
"""重写渲染器：基于真实新闻素材，批量生成 issue-NNN.html"""
import os, html

CSS = """<style>
  *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{font-family:'Georgia','Noto Serif SC','Times New Roman',serif;background:#f7f5f0;color:#2c2c2c;line-height:1.7;font-size:15px;padding-top:56px}
  .topnav{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(247,245,240,.92);backdrop-filter:blur(8px);border-bottom:1px solid #e6e3db;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;overflow-x:auto;scrollbar-width:none}
  .topnav::-webkit-scrollbar{display:none}
  .topnav-inner{display:flex;align-items:center;gap:4px;max-width:768px;margin:0 auto;padding:10px 20px;white-space:nowrap}
  .topnav .brand{font-weight:700;font-size:14px;color:#1a1a1a;margin-right:12px;flex-shrink:0}
  .topnav a{font-size:13px;color:#888;text-decoration:none;padding:5px 12px;border-radius:6px;transition:background .2s;flex-shrink:0}
  .topnav a:hover{background:#edeae3;color:#2c2c2c}
  .container{max-width:720px;margin:0 auto;padding:36px 24px 64px}
  .masthead{margin-bottom:36px}
  .masthead h1{font-size:28px;font-weight:700;color:#1a1a1a}
  .meta{font-size:13px;color:#888;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;border-bottom:1px solid #e6e3db;padding:6px 0 14px;margin-top:2px}
  .meta span{margin-right:16px}
  .section{margin-bottom:40px;scroll-margin-top:72px}
  .section-header{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#999;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-weight:600;margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid #e6e3db}
  .card{background:#fff;border:1px solid #e6e3db;border-radius:8px;padding:24px;margin-bottom:16px}
  .card .tag{display:inline-block;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:11px;font-weight:600;padding:2px 8px;border-radius:3px;margin-bottom:8px;background:#f0ede6;color:#555}
  .card h3{font-size:17px;font-weight:700;color:#1a1a1a;margin-bottom:6px;line-height:1.4}
  .card p{font-size:14px;color:#555;line-height:1.7}
  .card .source-link{display:inline-block;margin-top:10px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:12px;color:#888;text-decoration:none;border-bottom:1px solid #ddd}
  .card .source-link:hover{color:#2c2c2c;border-color:#2c2c2c}
  .news-item{padding:14px 0;border-bottom:1px solid #eeeae1}
  .news-item:first-child{padding-top:0}
  .news-item:last-child{border-bottom:none;padding-bottom:0}
  .news-item .label{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:11px;font-weight:600;color:#999;margin-bottom:3px}
  .news-item .title{font-size:15px;font-weight:700;color:#1a1a1a;margin-bottom:4px}
  .news-item .summary{font-size:14px;color:#555;line-height:1.7}
  .news-item .source-link{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:12px;color:#aaa;text-decoration:none;margin-top:4px;display:inline-block}
  .news-item .source-link:hover{color:#555}
  .footer{text-align:center;font-size:12px;color:#bbb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin-top:40px;padding-top:20px;border-top:1px solid #e6e3db}
  @media(max-width:600px){body{padding-top:50px}.topnav-inner{padding:8px 14px}.topnav .brand{font-size:13px;margin-right:8px}.topnav a{font-size:12px;padding:4px 10px}.container{padding:24px 16px 48px}.masthead h1{font-size:22px}.card{padding:18px}}
</style>"""

NAV = """<nav class="topnav"><div class="topnav-inner">
  <span class="brand">AI Radar</span>
  <a href="#picks">Radar Picks</a>
  <a href="#models">模型与技术</a>
  <a href="#enterprise">企业应用</a>
  <a href="#china">国内动态</a>
  <a href="#international">国际动态</a>
  <a href="#finance">AI 与金融</a>
  <a href="#policy">政策、监管与风险</a>
  <a href="#community">社区观察</a>
</div></nav>"""

IDS = {"模型与技术进展":"models","企业应用与工具观察":"enterprise","国内 AI 动态":"china",
       "国际 AI 动态":"international","AI 与金融":"finance","政策与监管":"policy",
       "政策、监管与风险":"policy","社媒与开发者社区观察":"community"}

def esc(s): return html.escape(s, quote=False)

def render(iss):
    num, date = iss["num"], iss["date"]
    o = ['<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">']
    o.append(f"<title>AI Radar · 第 {num} 期</title>")
    o.append(CSS); o.append("</head>\n<body>"); o.append(NAV); o.append('<div class="container">')
    o.append('<div class="masthead"><h1>AI Radar</h1>')
    o.append(f'<div class="meta"><span>{date}</span><span>第 {num} 期</span></div></div>')
    o.append('<div class="section" id="picks"><div class="section-header">Radar Picks</div>')
    for tag, title, body, src, url in iss.get("picks", []):
        o.append('<div class="card">')
        o.append(f'<span class="tag">{esc(tag)}</span><h3>{esc(title)}</h3><p>{body}</p>')
        o.append(f'<a class="source-link" href="{url}" target="_blank">{esc(src)}</a></div>')
    o.append('</div>')
    for name, items in iss.get("sections", []):
        sid = IDS.get(name, "sec")
        o.append(f'<div class="section" id="{sid}"><div class="section-header">{esc(name)}</div>')
        for label, title, summary, src, url in items:
            o.append('<div class="news-item">')
            o.append(f'<div class="label">{esc(label)}</div><div class="title">{esc(title)}</div><div class="summary">{summary}</div>')
            o.append(f'<a class="source-link" href="{url}" target="_blank">{esc(src)}</a></div>')
        o.append('</div>')
    o.append('<div class="footer"><p><a href="issues/" style="color:#bbb;text-decoration:none;border-bottom:1px solid #ddd;">往期归档</a></p></div>')
    o.append('</div>\n</body>\n</html>')
    return "\n".join(o)

if __name__ == "__main__":
    import data_early, data_mid, data_late
    base = "/workspace/ai-radar/issues"
    all_issues = data_early.ISSUES + data_mid.ISSUES + data_late.ISSUES
    for iss in all_issues:
        p = os.path.join(base, f"issue-{iss['num']:03d}.html")
        open(p, "w", encoding="utf-8").write(render(iss))
        print("gen", p)
