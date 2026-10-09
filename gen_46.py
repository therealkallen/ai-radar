# -*- coding: utf-8 -*-
"""生成第 46 期归档。"""
import os
import rebuild
import data_46

BASE = os.path.dirname(os.path.abspath(__file__))
ISSUES_DIR = os.path.join(BASE, "issues")

for iss in data_46.ISSUES:
    p = os.path.join(ISSUES_DIR, f"issue-{iss['num']:03d}.html")
    open(p, "w", encoding="utf-8").write(rebuild.render(iss))
    print("gen", p)
