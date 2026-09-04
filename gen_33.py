# -*- coding: utf-8 -*-
"""生成第 33 期归档，并将 index.html 刷新为最新一期（第 33 期）。"""
import os
import rebuild
import data_33

BASE = "/workspace/ai-radar"
ISSUES_DIR = os.path.join(BASE, "issues")

for iss in data_33.ISSUES:
    p = os.path.join(ISSUES_DIR, f"issue-{iss['num']:03d}.html")
    open(p, "w", encoding="utf-8").write(rebuild.render(iss))
    print("gen", p)

latest = max(data_33.ISSUES, key=lambda x: x["num"])
open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(rebuild.render(latest))
print("update index.html ->", latest["num"])
