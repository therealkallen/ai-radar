#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Radar 跨期去重校验脚本（v2）

用法:
    python3 check_dup.py            # 校验当前 index.html 与往期归档是否重复
    python3 check_dup.py index.html # 校验指定文件

逻辑:
    1. 收集 issues/issue-0NN.html 中所有标题（.card h3 + .news-item .title）
    2. 收集待校验文件中的标题
    3. 两层校验：
       A. 硬阻断：已停用。原用于按关键词拦截已结项故事，但关键词匹配会误拦
          合理的后续进展（如 GPT-5.6 公开上线、Fable 5 订阅期延长），故不再作为
          把关门槛；是否重复改由编辑按语义判断（见 coverage.md）。
       B. 实义短语近似：仅作参考提示，对待校验标题中的 5+ 字实义短语，去匹配
          往期标题中的 5+ 字实义短语；命中供编辑复核，不代表一定重复。

注意: 这是辅助校验，最终是否「后续进展」由人工判断。
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# A. 已结项的一次性故事词（历史遗留，已弃用为「把关」用途）
#    ⚠️ 用户明确指示：去重应以「是否同一条新闻」的语义判断为准，
#    不得用关键词/子串匹配来拦截——同一实体（如 GPT-5.6、Fable 5）
#    在不同语境下是完全不同的新闻。因此本列表不再作为硬阻断门槛，
#    仅保留作记忆参考。真正的把关由编辑（配合 coverage.md）完成。
HARD_BLOCK = []

# 通用词白名单（这些词出现在标题里不算「实义短语」，匹配时跳过）
STOP = {
    "发布", "合作", "推出", "上线", "模型", "研究", "AI ", "分析", "解读",
    "报告", "试验", "测试", "开源", "更新", "升级", "发布，", "正式", "全球",
    "中国", "美国", "企业", "团队", "安全", "能力", "智能", "神经", "网络",
    "数据", "代码", "视频", "图像", "基准", "评估", "训练", "推理", "代理",
    "助手", "系统", "平台", "公司", "大学", "机构", "计划", "项目", "启动",
}


def extract_titles(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    titles = []
    for m in re.finditer(r'<h3>(.*?)</h3>', html, re.S):
        titles.append(re.sub(r'<.*?>', '', m.group(1)).strip())
    for m in re.finditer(r'class="title">(.*?)</div>', html, re.S):
        titles.append(re.sub(r'<.*?>', '', m.group(1)).strip())
    return [t for t in titles if t]


def significant_phrases(title, min_len=5):
    """从标题中提取长度 >= min_len 的连续中文字符串（视为实义短语）。"""
    phrases = set()
    # 去掉非中文字符，按中文字符段切分
    for seg in re.findall(r'[\u4e00-\u9fff]+', title):
        if len(seg) >= min_len:
            phrases.add(seg)
    return phrases


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "index.html")
    if not os.path.exists(target):
        print(f"[错误] 找不到文件: {target}")
        sys.exit(1)

    past_files = sorted(glob.glob(os.path.join(ROOT, "issues", "issue-0*.html")))
    past_titles = []
    for pf in past_files:
        past_titles.extend(extract_titles(pf))
    past_set = set(past_titles)

    # 往期实义短语集合
    past_phrases = set()
    for pt in past_set:
        past_phrases |= significant_phrases(pt, 5)

    new_titles = extract_titles(target)

    print(f"往期归档文件: {len(past_files)} 个, 往期标题: {len(past_set)} 条")
    print(f"待校验标题: {len(new_titles)} 条\n")

    problems = 0

    # A. 硬阻断
    for t in new_titles:
        for kw in HARD_BLOCK:
            if kw.lower() in t.lower():
                print(f"[硬阻断] 命中已结项故事词「{kw}」: {t}")
                problems += 1

    # B. 实义短语近似
    for t in new_titles:
        matched = False
        for ph in significant_phrases(t, 5):
            if ph in STOP:
                continue
            if ph in past_phrases:
                # 避免把 ST名 误报：仅当短语不在停用词且确实为往期实义短语
                print(f"[近似重复] 新: 「{t}」  ~  往期实义短语: 「{ph}」")
                problems += 1
                matched = True
                break
        if matched:
            continue

    if problems == 0:
        print("✓ 未检测到与往期的明显重复。可发布。")
    else:
        print(f"\n共 {problems} 处疑似重复，请人工确认是否为「后续进展」后再发布。")


if __name__ == "__main__":
    main()
