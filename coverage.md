# AI Radar 覆盖实体清单（去重参考）

> 用途：生成新一期前，先扫描本清单。以下实体已在往期报道过，**除非是明确的后续进展，否则不得再次作为独立新闻条目放入新一期**。
> 规则：往期放过的实体 → 不放（除非后续）；同期内部同一实体只出现一次（Radar Picks 可作头条，专题只在一处展开）。

## 已报道实体（按期）

### 第 1 期 (issue-001)
- Fable 5 / Mythos 5 发布
- 监管（通用）

### 第 2 期 (issue-002)
- Claude Tag
- Daybreak 安全工具
- Fable 5 / Mythos 5
- NVIDIA
- 智能体（通用）
- 监管（通用）

### 第 3 期 (issue-003)
- Broadcom / Jalapeño（首次提及）
- Claude Code
- Fable 5
- GPT-5.6 系列
- IPO / SpaceX
- Micron
- NVIDIA
- 监管

### 第 4 期 (issue-004)
- Claude Code
- Frontier（OpenAI 企业计划）
- GPT-5.6
- HP
- 越狱（Fable 5 绕行事件）
- 监管

### 第 5 期 (issue-005)
- Claude Code / Claude Science / Claude Sonnet 5
- Fable 5 / Mythos 5 / HackerOne
- GeneBench
- GPT-5.6
- HP / IPO / Jalapeño / Micron / SpaceX
- 越狱
- 监管

### 第 6 期 (issue-006)
- AMD / Intel / Micron（Q2 芯片暴涨）
- Broadcom / Jalapeño（作为 OpenAI 估值背景）
- CJS 越狱严重性框架 / Fable 5 安全白皮书 / 四层分类器 / HackerOne
- Claude Code（阿里禁用）
- GPT-5.6 系列（作为 OpenAI 估值背景）
- IPO / SpaceX 1.77 万亿上市 / OpenAI S-1
- Qoder（阿里替代工具）
- Safari MCP Server（WebKit）
- short leash / 短皮带 编程法
- 阿里 / 阿里巴巴 禁用 Claude Code
- 监管（Anthropic 监管策略转变）
- 越狱

### 第 7 期 (index.html) — 当前
- AMD（板块走强）
- Anthropic 首尔办公室
- Broadcom / Jalapeño（产品 + 财务）
- Claude Code（作为 Claude Tag 对比提及，非独立条目）
- Claude Science / Claude Sonnet 5 / Claude Tag
- Daybreak
- DeepSeek（财富50强）
- Frontier / HP
- GeneBench
- GPT-5.6 Sol / Sol Ultra → Codex
- NVIDIA 逼近 $200
- 智能体（中国监管语境）
- 欧盟 AI Act 7.1 生效
- 监管（中国 AI 监管向 B 端扩展 + 7月新规）

## 去重校验脚本

运行 `python3 check_dup.py` 可扫描 index.html 是否出现本清单中的实体（越狱/CJS/Jalapeño/IP O 等已结项话题会告警）。

## 注意事项
- 「Fable 5 / 越狱 / CJS / HackerOne」已在第 5、6 期密集报道，**后续除非有全新的监管裁决或安全事件，否则不再单独成条**。
- 「IPO / SpaceX / OpenAI S-1 / Anthropic 估值」已在第 3、5、6 期报道，**除非有正式招股书/上市定价等硬进展，否则不再成条**。
- 「Jalapeño / GPT-5.6 系列」已在多期作为背景提及，新一期若要报道须是**全新进展**（如芯片量产、新合作方），而非重复产品发布。
