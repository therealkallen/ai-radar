# -*- coding: utf-8 -*-
"""生成第 30 期归档，并将 index.html 刷新为最新一期（第 30 期）。"""
import os
import rebuild
import data_30

BASE = "/workspace/ai-radar"
ISSUES_DIR = os.path.join(BASE, "issues")

for iss in data_30.ISSUES:
    p = os.path.join(ISSUES_DIR, f"issue-{iss['num']:03d}.html")
    open(p, "w", encoding="utf-8").write(rebuild.render(iss))
    print("gen", p)

latest = max(data_30.ISSUES, key=lambda x: x["num"])
open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(rebuild.render(latest))
print("update index.html ->", latest["num"])
