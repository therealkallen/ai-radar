# -*- coding: utf-8 -*-
"""生成第 38 期归档，刷新 index.html，并把第 38 期插入 issues/index.html 归档列表。"""
import os
import re
import rebuild
import data_38

BASE = "/workspace/ai-radar"
ISSUES_DIR = os.path.join(BASE, "issues")

for iss in data_38.ISSUES:
    p = os.path.join(ISSUES_DIR, f"issue-{iss['num']:03d}.html")
    open(p, "w", encoding="utf-8").write(rebuild.render(iss))
    print("gen", p)

latest = max(data_38.ISSUES, key=lambda x: x["num"])
open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(rebuild.render(latest))
print("update index.html ->", latest["num"])

# 归档列表
arch = os.path.join(ISSUES_DIR, "index.html")
html = open(arch, encoding="utf-8").read()
num, date = latest["num"], latest["date"]
entry = (
    f'    <li>\n'
    f'      <span class="num">#{num}</span>\n'
    f'      <span class="info">\n'
    f'        <a href="issue-{num:03d}.html">第{num}期</a>\n'
    f'        <div class="date">{date}</div>\n'
    f'      </span>\n'
    f'    </li>\n'
)
if f'issue-{num:03d}.html' not in html:
    html = html.replace('  <ul class="archive-list">\n', '  <ul class="archive-list">\n' + entry, 1)
    open(arch, "w", encoding="utf-8").write(html)
    print("update issues/index.html -> add #", num)
else:
    print("issues/index.html already has #", num)
