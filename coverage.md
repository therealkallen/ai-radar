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

### 第 7 期 (index.html) — 当前（已定稿，全部为 7.3–7.6 窗口内、1–6 期均未报道的内容）
- 欧盟 AI Act 7.1 全面生效（ec.europa.eu）
- Microsoft Frontier Company 成立（$2.5B、6000 人，blogs.microsoft.com / cnbc.com）
- Gemini Spark 登陆 Mac（techcrunch.com）
- Dartmouth AI 导师 0.71–1.30 SD（uu.nl）
- 代码整洁度 vs coding agent（arxiv 2605.20049）
- AgenticDataBench 数据智能体基准（arxiv 2607.01647）
- PACE 智能体能力评估代理（arxiv 2607.02032）
- 财富中国科技 50 强（DeepSeek 进前五，ifeng.com）
- 中国 AI 核心产业突破 1.2 万亿（cloud.tencent.cn）
- 中国 AI 上半年融资 3000 亿（IT桔子，aisort.net）
- NVIDIA 逼近 $200（intellectia.ai）
- Tom Tunguz：AI 支出 2029 年盈亏平衡（tomtunguz.com）

> ⚠️ 第 7 期初稿曾误放 Sonnet 5 / Claude Science / Claude Tag / Daybreak / Jalapeño /
> GPT-5.6 / HP Frontier / 首尔办公室 / NVIDIA 等——这些均已在 Issue 1–5 实时报道过。
> 已剔除，仅保留上述真正属于本窗口的新内容。

## 去重机制（每次生成前必做）

1. **扫描往期**：生成新一期前，先 `python3 check_dup.py` 校验 index.html 与 issues/ 全部归档是否重复。
2. **硬阻断词**：`check_dup.py` 内置 `HARD_BLOCK` 列表（Fable 5、CJS、越狱、HackerOne、SpaceX、OpenAI S-1、Jalapeño、Claude Sonnet 5、Claude Science、Claude Tag、Daybreak、GeneBench、GPT-5.6、HP Frontier、首尔办公室……），命中即告警。
3. **实义短语近似**：以待校验标题的 5+ 字实义短语匹配往期标题，命中即疑似重复。
4. **本清单同步更新**：每发布一期，把其真实覆盖内容补进对应「第 N 期」小节，并视情况把一次性故事词加入 `HARD_BLOCK`。

> ⚠️ 关键教训：late-June 的集中发布（Sonnet 5、Claude Science、Daybreak、Jalapeño、
> GPT-5.6、Claude Tag 等）在 Issue 1–5 已**实时**报道过。新一期只报**本窗口内、且往期未报**
> 的内容；同一事件只有在出现**全新硬进展**（如正式上市定价、监管裁决）时才作为后续放入。

## 注意事项
- 「Fable 5 / 越狱 / CJS / HackerOne」已在第 5、6 期密集报道，**后续除非有全新的监管裁决或安全事件，否则不再单独成条**。
- 「IPO / SpaceX / OpenAI S-1 / Anthropic 估值」已在第 3、5、6 期报道，**除非有正式招股书/上市定价等硬进展，否则不再成条**。
- 「Jalapeño / GPT-5.6 系列」已在多期作为背景提及，新一期若要报道须是**全新进展**（如芯片量产、新合作方），而非重复产品发布。
