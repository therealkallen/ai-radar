# -*- coding: utf-8 -*-
"""生成第 26、27 期归档，并将 index.html 刷新为最新一期（第 27 期）。"""
import os, shutil
import rebuild
import data_new

BASE = "/workspace/ai-radar"
ISSUES_DIR = os.path.join(BASE, "issues")

for iss in data_new.ISSUES:
    p = os.path.join(ISSUES_DIR, f"issue-{iss['num']:03d}.html")
    open(p, "w", encoding="utf-8").write(rebuild.render(iss))
    print("gen", p)

# 最新一期作为首页
latest = max(data_new.ISSUES, key=lambda x: x["num"])
index_path = os.path.join(BASE, "index.html")
open(index_path, "w", encoding="utf-8").write(rebuild.render(latest))
print("update index.html ->", latest["num"])
