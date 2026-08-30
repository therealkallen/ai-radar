# AI Radar Content Pipeline Skill

## 0. 任务目标与最高原则

维护并自动更新 AI Radar：

https://therealkallen.github.io/ai-radar/

更新频率：

- 每周一
- 每周三
- 每周五

AI Radar 的目标不是尽可能多地收集 AI 新闻，而是持续提供：

- 真实
- 重要
- 有信息增量
- 来源可信
- 可以追溯到原文

的 AI 行业动态。

### 最高原则

> **先找到真实来源，再生成新闻。禁止先想新闻，再寻找能够支持它的来源。**

任何新闻条目都必须从一个已经实际检索并验证过的 `source_record` 创建。

**没有 source_record，就没有新闻。**

以下内容不能单独作为新闻事实来源：

- 模型自身记忆
- 模型训练数据中的历史知识
- 上一期 AI Radar 内容
- 搜索结果 snippet
- AI 搜索摘要
- 其他 AI 的回答
- 聚合站生成的摘要
- 未打开的网页标题

如果当前周期没有足够多高质量新闻：

> **少发，不凑数。**

如果当前周期恰好发生大量重要新闻：

> **可以增加条数，不受固定总量限制。**

质量和重要性始终高于数量。

---

# 1. 页面与 UI

保持当前页面 UI、视觉设计和整体布局。

除非收到明确要求，否则不要主动修改：

- 配色
- 字体
- 卡片样式
- 动画
- 页面布局
- 导航结构
- 页面整体视觉风格

当前主要任务是维护内容生成与新闻数据管道。

---

# 2. 页面栏目

保持以下栏目：

1. Radar Picks
2. 模型与技术进展
3. 企业应用与工具观察
4. 国内 AI 动态
5. 国际 AI 动态
6. AI 与金融
7. 政策、监管与风险
8. 社媒与开发者社区观察

---

# 3. 新闻数量原则

## 3.1 不设置固定新闻总数

禁止为了达到固定数量而填充低价值新闻。

整个页面没有强制总条数。

新闻数量应该由当前周期实际发生的重要事件决定。

---

## 3.2 各栏目常态数量

通常情况下，每个普通栏目可展示：

**2–5 条**

但这只是常态范围，不是硬限制。

例如：

- 某栏目只有 1 条真正值得关注的新闻 → 展示 1 条
- 某栏目本期发生 7 条重要且相互独立的事件 → 可以展示 7 条

禁止为了栏目看起来“完整”而凑数。

---

## 3.3 Radar Picks

通常：

**3–5 条**

但同样不是强制数量。

Radar Picks 只选择本期最值得关注的事件。

---

# 4. Radar Picks 的数据逻辑

Radar Picks 不是一个独立新闻池。

它是本期全部 canonical stories 中的精选。

每个 canonical story 可包含：

```json
{
  "radar_pick": true
}
```

生成流程必须是：

```text
生成全部 verified canonical stories
↓
完成分类
↓
根据重要性选出 Radar Picks
```

禁止先单独生成一批 Radar Picks，再生成其他栏目新闻。

---

## 4.1 Radar Picks 选择标准

优先选择：

- 重大模型发布
- 重要产品或平台变化
- AI 龙头公司的重要战略变化
- 重大政策或监管事件
- 明显技术突破
- 重大商业交易
- 对企业 AI 应用产生明显影响的变化
- 对整个 AI 行业未来方向具有较强信号意义的事件

---

# 5. Source-First Pipeline

每次更新必须严格按照以下顺序执行。

```text
SEARCH
↓
OPEN SOURCE
↓
VERIFY SOURCE
↓
CREATE SOURCE RECORD
↓
CREATE CANONICAL STORY
↓
SEMANTIC EVENT DEDUPLICATION
↓
CLASSIFY
↓
SELECT RADAR PICKS
↓
WRITE SUMMARY
↓
VALIDATE
↓
BUILD
↓
PUBLISH
```

绝对禁止以下流程：

```text
THINK OF NEWS
↓
WRITE STORY
↓
SEARCH FOR SOMETHING THAT LOOKS LIKE SUPPORTING EVIDENCE
```

---

# 6. 更新时间窗口

时区：

```text
Asia/Shanghai
```

默认搜索当前更新周期产生的新内容。

### 周一

覆盖：

```text
上周五上一次更新之后 → 当前时间
```

### 周三

覆盖：

```text
周一上一次更新之后 → 当前时间
```

### 周五

覆盖：

```text
周三上一次更新之后 → 当前时间
```

为了防止遗漏，可以扩大搜索窗口至最近约 72 小时。

但是：

**搜索窗口扩大 ≠ 可以重复发布旧新闻。**

所有候选内容仍需与历史 archive 进行事件级检查。

---

# 7. Source Record

只有在实际打开并检查来源页面之后，才能创建 `source_record`。

标准结构：

```json
{
  "source_url": "",
  "canonical_url": "",
  "source_name": "",
  "source_domain": "",
  "source_tier": "primary | trusted_media | social_signal",
  "raw_title": "",
  "published_at": "",
  "retrieved_at": "",
  "evidence_type": "",
  "raw_excerpt": ""
}
```

---

## 7.1 source_url

实际检索并打开的页面。

---

## 7.2 canonical_url

最终展示给用户的原始来源链接。

禁止使用：

- 搜索结果页
- 跳转页
- URL shortener
- 聚合页
- 镜像页
- 转载页

---

## 7.3 raw_title

来源页面的真实标题。

不能自行编造。

---

## 7.4 published_at

来源页面显示的真实发布日期或发布时间。

无法确认发布时间时：

- 默认降低优先级
- 如果新闻高度依赖时效性，则不收录

---

## 7.5 raw_excerpt

保存足以证明事件真实存在的简短证据。

不得根据 raw_excerpt 推断来源没有明确陈述的事实。

---

# 8. 来源等级

来源分为：

```text
primary
trusted_media
social_signal
```

---

## 8.1 Primary Source

最高优先级。

用于：

- 模型发布
- 产品发布
- API 更新
- 公司公告
- 技术报告
- 开源项目
- 论文
- 政府政策
- 监管文件

如果存在可靠 primary source：

**优先使用 primary source 作为 canonical_url。**

---

## 8.2 Trusted Media

用于：

- 融资
- 并购
- IPO
- 人事变化
- 商业战略
- 市场变化
- 调查报道
- 法律纠纷
- 监管调查
- 尚未发布官方公告但已有可靠报道的重要事件

---

## 8.3 Social Signal

用于：

- X
- Reddit
- Hacker News
- GitHub Discussions / Issues
- 开发者社区

社媒内容只能表示：

- 观点
- 社区讨论
- 开发者反馈
- 使用体验
- 争议
- 早期信号

不能自动升级成“事实新闻”。

---

# 9. 国际 Primary Source Allowlist

```yaml
international_primary_sources:

  openai:
    name: OpenAI
    domains:
      - openai.com

  anthropic:
    name: Anthropic
    domains:
      - anthropic.com

  google_deepmind:
    name: Google DeepMind
    domains:
      - deepmind.google

  google_ai:
    name: Google AI
    domains:
      - blog.google
      - ai.google.dev

  meta:
    name: Meta AI
    domains:
      - ai.meta.com
      - about.fb.com

  microsoft:
    name: Microsoft
    domains:
      - microsoft.com
      - news.microsoft.com

  github:
    name: GitHub
    domains:
      - github.com
      - github.blog

  nvidia:
    name: NVIDIA
    domains:
      - nvidia.com
      - blogs.nvidia.com

  aws:
    name: AWS
    domains:
      - aws.amazon.com

  mistral:
    name: Mistral AI
    domains:
      - mistral.ai

  huggingface:
    name: Hugging Face
    domains:
      - huggingface.co

  cloudflare:
    name: Cloudflare
    domains:
      - cloudflare.com
      - blog.cloudflare.com

  salesforce:
    name: Salesforce
    domains:
      - salesforce.com

  servicenow:
    name: ServiceNow
    domains:
      - servicenow.com

  uipath:
    name: UiPath
    domains:
      - uipath.com

  sap:
    name: SAP
    domains:
      - sap.com
      - news.sap.com

  adobe:
    name: Adobe
    domains:
      - adobe.com
      - blog.adobe.com

  slack:
    name: Slack
    domains:
      - slack.com

  notion:
    name: Notion
    domains:
      - notion.com

  zoom:
    name: Zoom
    domains:
      - zoom.com

  vercel:
    name: Vercel
    domains:
      - vercel.com

  langchain:
    name: LangChain
    domains:
      - langchain.com
      - blog.langchain.com

  llamaindex:
    name: LlamaIndex
    domains:
      - llamaindex.ai
```

---

# 10. 国内 Primary Source Allowlist

```yaml
china_primary_sources:

  qwen:
    name: Qwen / 通义千问
    domains:
      - qwenlm.github.io
      - aliyun.com
      - alibabacloud.com

  deepseek:
    name: DeepSeek
    domains:
      - deepseek.com

  zhipu:
    name: 智谱 AI
    domains:
      - zhipuai.cn
      - z.ai

  moonshot:
    name: Moonshot AI / Kimi
    domains:
      - moonshot.cn
      - platform.moonshot.cn

  tencent:
    name: 腾讯 / 混元
    domains:
      - hunyuan.tencent.com
      - tencent.com

  baidu:
    name: 百度
    domains:
      - baidu.com
      - cloud.baidu.com

  bytedance:
    name: 字节跳动 / Seed / 火山引擎
    domains:
      - seed.bytedance.com
      - volcengine.com

  modelscope:
    name: ModelScope
    domains:
      - modelscope.cn
```

同时允许相应公司的：

- 官方 GitHub repository
- 官方 Hugging Face organization
- 官方 ModelScope organization

---

# 11. 国际 Trusted Media Allowlist

```yaml
international_trusted_media:

  - reuters.com
  - apnews.com
  - bloomberg.com
  - ft.com
  - wsj.com
  - theinformation.com
  - technologyreview.com
  - wired.com
  - theverge.com
  - techcrunch.com
  - cnbc.com
  - semafor.com
  - fortune.com
```

重大商业新闻优先：

1. Reuters
2. Bloomberg
3. Financial Times
4. Wall Street Journal
5. Associated Press
6. The Information

Paywall 不构成使用低质量转载站的理由。

如果 Bloomberg / FT / WSJ 原报道存在：

仍然链接原报道。

---

# 12. 中文 Trusted Media Allowlist

```yaml
china_trusted_media:

  - jiqizhixin.com
  - qbitai.com
  - infoq.cn
  - 36kr.com
  - geekpark.net
  - zhidx.com
  - tmtpost.com
```

中文科技媒体主要用于：

- 国内商业动态
- 国内产品新闻
- 国内公司采访
- 行业分析

如果存在官方发布：

仍优先官方来源。

---

# 13. 技术、论文与开源来源

允许：

```yaml
research_sources:

  - arxiv.org
  - openreview.net
  - github.com
  - huggingface.co
  - modelscope.cn
```

Discovery source 可包括：

```yaml
research_discovery_sources:

  - paperswithcode.com
  - GitHub Trending
  - Hugging Face Trending
```

Discovery source 本身不应该优先成为 canonical_url。

最终尽量指向：

- 原论文
- 原 GitHub repo
- model card
- 官方 technical report

---

# 14. 政策与监管来源

优先官方来源。

```yaml
policy_sources:

  - digital-strategy.ec.europa.eu
  - ec.europa.eu
  - eur-lex.europa.eu
  - nist.gov
  - oecd.ai
  - gov.uk
  - whitehouse.gov
  - congress.gov
  - federalregister.gov
  - regulations.gov
  - ftc.gov
  - justice.gov
  - cac.gov.cn
  - miit.gov.cn
  - gov.cn
  - samr.gov.cn
  - hai.stanford.edu
  - cset.georgetown.edu
  - brookings.edu
  - techpolicy.press
```

正式政策、法律、监管处罚：

优先 canonical source：

- 政府
- 监管机构
- 法律文本
- 官方公告

媒体用于补充说明，而不是替代正式文件。

---

# 15. 社媒与开发者社区

允许：

```yaml
social_sources:

  - x.com
  - reddit.com
  - news.ycombinator.com
  - github.com
```

HNRSS：

```text
hnrss.org
```

只能作为 Hacker News discovery feed。

最终 Hacker News URL 应尽量链接：

```text
news.ycombinator.com/item?id=...
```

---

## 15.1 X 重点观察账号

优先关注：

- Sam Altman
- Andrej Karpathy
- Yann LeCun
- François Chollet
- Simon Willison
- Jeremy Howard
- Jack Clark
- Thomas Wolf
- Demis Hassabis
- Ethan Mollick
- Clement Delangue
- Jim Fan
- Omar Sanseviero
- OpenAI Developers
- Anthropic
- Google DeepMind
- Hugging Face
- Meta AI

如果无法访问原始 post：

禁止使用第三方转述冒充原始来源。

---

## 15.2 Reddit

重点关注：

```text
r/LocalLLaMA
r/MachineLearning
r/OpenAI
r/ClaudeAI
r/singularity
```

Reddit 只能描述为：

- 社区反馈
- 用户体验
- 开发者讨论
- 争议
- 观点

---

# 16. Explicit Blocklist

以下来源禁止作为 final source。

```yaml
blocked_final_sources:

  - aitoolly.com
  - thirdruntime.com
  - blog.csdn.net
  - csdn.net
  - baijiahao.baidu.com
  - biggo.com
  - gaana.com
  - stockalpha.ai
  - agihunt.info
  - theautomateddaily.com
  - genaicrib.com
```

同时禁止：

- AI news aggregator
- AI tool directory
- 自动生成新闻网站
- SEO 内容农场
- affiliate 推荐站
- 新闻搬运站
- 新闻镜像页
- 搜索结果页
- Medium 搬运文章
- Substack 搬运文章
- 第三方 URL shortener
- 不明来源 newsletter 镜像

### Blocklist 是硬规则

如果：

```text
source_domain ∈ blocklist
```

则：

```text
VALIDATION_FAIL
```

该 story 不允许进入最终页面。

---

# 17. Allowlist 的正确理解

Allowlist 是最终来源的强约束，但不禁止使用其他网站发现线索。

流程可以是：

```text
野鸡网站 / 聚合站发现一个可能重要的事件
↓
找到官方来源
或
找到 Trusted Media 原报道
↓
验证
↓
进入候选新闻池
```

禁止：

```text
野鸡网站发现事件
↓
直接把野鸡网站作为新闻来源
```

如果始终找不到可靠原始来源：

```text
DROP STORY
```

---

# 18. 重大 Claim 验证

以下事件属于高风险新闻：

- IPO
- 并购
- 大额融资
- 重大估值变化
- 超过 10 亿美元的重要交易
- CEO / Founder / 高管重大变化
- 大规模裁员
- 模型安全事故
- 网络安全事故
- 监管处罚
- 法律重大进展
- 模型停售
- 公司重大战略调整
- 极端 benchmark claim
- “全球第一”
- “史上最大”
- “首次”
- “打破纪录”

必须满足至少一个：

### A

存在直接官方证据。

或：

### B

存在至少两个独立的 Trusted Media 来源。

只有一个低可信来源：

```text
DROP STORY
```

---

# 19. 禁止凭空生成

以下行为属于严重错误：

1. 根据模型记忆生成“最近的新闻”。
2. 根据公司近期趋势推测可能发生的事件。
3. 先写新闻，再搜索支持新闻的页面。
4. 搜不到时自行补充 URL。
5. 根据搜索 snippet 编写完整新闻。
6. 根据上一期故事推测后续。
7. 根据媒体标题自行补充交易金额。
8. 根据模型常识补充 benchmark。
9. 把预测写成事实。
10. 把传言写成官方消息。

如果没有真实、可信新闻：

```text
NO_VALID_STORY
```

---

# 20. Canonical Story

每个独立新闻事件创建一个 canonical story。

```json
{
  "event_id": "",
  "event_fingerprint": "",
  "title": "",
  "summary": "",
  "primary_category": "",
  "radar_pick": false,
  "tags": [],
  "published_at": "",
  "canonical_source": {
    "source_name": "",
    "source_url": "",
    "source_domain": "",
    "source_tier": ""
  },
  "supporting_sources": [],
  "evidence_type": "",
  "verified": true
}
```

---

# 21. 去重原则：基于事件内容，不基于关键词

### 这是强制规则。

禁止仅根据以下内容判断新闻是否重复：

- 标题关键词
- 公司名
- 模型名
- 产品名
- 人物名
- embedding similarity 单独结果
- 标题文字相似度
- tag 重叠
- URL 中的关键词

关键词只能辅助查找候选重复项，不能作为最终去重依据。

---

# 22. 什么才算“重复新闻”

只有当两个 story 实际描述的是：

> **同一个事件、同一个核心事实、同一个阶段的进展**

才视为重复。

例如：

### 重复

新闻 A：

> OpenAI 周一发布 GPT-X。

新闻 B：

> OpenAI 正式推出 GPT-X，新模型今天上线。

如果两篇都只是报道同一次模型发布：

这是同一事件。

应合并为一个 canonical story。

---

# 23. 什么不算重复：系列报道和后续进展

即使新闻涉及完全相同的：

- 公司
- 模型
- 产品
- 人物
- 政策
- 并购
- 技术

只要核心事实发生了新的实质性变化，就不是重复新闻。

例如：

### Day 1

> Anthropic 发布 Claude X。

### Day 2

> Claude X API 出现严重服务故障。

### Day 3

> Anthropic 发布 Claude X 的新 context window。

这是三个独立事件。

**不能因为 Anthropic + Claude X 高度重合而去重。**

---

# 24. 系列报道识别

对于同一长期事件，应判断本期报道是否带来：

```text
MATERIAL_NEW_DEVELOPMENT
```

实质性新进展包括但不限于：

- 新官方公告
- 新产品阶段上线
- 新监管决定
- 新交易进展
- 新价格
- 新 benchmark
- 新技术细节
- 新调查结果
- 新法院裁决
- 新公司回应
- 新安全事故
- 新修复措施
- 新合作方
- 新地区上线
- 新商业结果
- 新公开数据

如果存在 material new development：

**可以创建新的 canonical story。**

---

# 25. 仅重复背景不属于新新闻

例如上一期：

> 公司 A 宣布收购公司 B。

本期出现一篇媒体文章：

> 为什么公司 A 收购公司 B 很重要。

如果没有任何新的事实：

不是新新闻。

不应再次发布。

---

# 26. 事件语义比较

判断两个 candidate stories 是否重复时，应比较：

1. **Who**  
   涉及哪些主体？

2. **What happened**  
   核心动作是什么？

3. **Object**  
   动作针对什么模型、产品、公司、政策？

4. **When**  
   属于哪个时间节点？

5. **State / Stage**  
   是宣布、上线、完成、批准、失败、调查还是后续？

6. **Material change**  
   与旧 story 相比是否出现实质新事实？

只有在这些维度高度一致时才认定为重复。

---

# 27. event_id 与 story_id

建议把长期事件和具体新闻更新分开。

例如：

```json
{
  "event_id": "openai-company-x-acquisition",
  "story_id": "openai-company-x-acquisition-announced-2026-08-20"
}
```

后续：

```json
{
  "event_id": "openai-company-x-acquisition",
  "story_id": "openai-company-x-acquisition-regulatory-approval-2026-09-03"
}
```

两条属于同一个长期 event：

```text
event_id 相同
```

但属于不同的实质新闻进展：

```text
story_id 不同
```

因此：

**允许分别发布。**

---

# 28. 去重模型的推荐输出

进行候选新闻对比时返回：

```json
{
  "relationship": "duplicate | follow_up | related | unrelated",
  "reason": "",
  "material_new_development": true
}
```

解释：

### duplicate

同一个核心事实。

→ 合并。

### follow_up

同一长期事件，但出现实质新进展。

→ 可以保留为新 story。

### related

主题有关，但属于独立事件。

→ 分别保留。

### unrelated

完全不同。

→ 分别保留。

---

# 29. 分类原则

每个 story 只有一个：

```text
primary_category
```

可以拥有多个：

```text
tags
```

不要因为一条新闻同时涉及多个主题，就复制成多个完整 story。

例如：

某 AI 公司收购支付公司：

```json
{
  "primary_category": "国际 AI 动态",
  "tags": [
    "并购",
    "FinTech",
    "企业 AI"
  ]
}
```

---

# 30. AI 与金融栏目

保留该栏目。

关注：

- Accounting
- Finance Transformation
- FP&A
- Audit
- Internal Control
- Tax
- Treasury
- Payments
- Banking
- Insurance
- FinTech
- ERP / SAP
- Financial Automation
- Finance Agent
- Financial Data Analytics

必须存在明确的：

```text
FINANCE_ANGLE
```

允许：

- AI 自动 reconciliation
- SAP Finance AI
- AI agent 在财务流程中的应用
- CFO AI adoption
- AI 审计
- AI 税务
- AI financial analytics
- AI 支付基础设施
- 金融机构 AI 风险监管

禁止：

因为一家公司属于金融行业，就把所有该公司的 AI 新闻放进来。

---

# 31. 企业应用与工具观察

重点关注真实可用的 AI 产品和企业应用。

包括：

- Microsoft Copilot
- Google Workspace
- OpenAI
- Anthropic
- GitHub Copilot
- SAP
- Salesforce
- ServiceNow
- UiPath
- Adobe
- Slack
- Notion
- Zoom
- Agent platforms
- Coding agents
- Workflow automation
- Browser agents
- Knowledge management
- Document automation
- Data analysis

该栏目是：

```text
观察
```

不是：

```text
推荐购买
```

---

# 32. 工具类新闻来源

优先：

- 产品官方 blog
- 官方 changelog
- 官方 release notes
- 官方 GitHub
- Trusted Media

禁止：

- Top 10 AI Tools
- 工具榜单站
- affiliate page
- AI 工具导航站
- SEO 工具文章
- 无来源的社媒安利

---

# 33. 摘要写作

所有内容使用中文。

每条新闻通常：

**80–150 字左右**

不要求机械满足字数。

内容回答：

1. 发生了什么？
2. 为什么重要？
3. 对行业、企业 AI、技术趋势或风险有什么意义？

如果第 3 点没有可靠依据：

**不要硬写。**

---

# 34. 写作风格

要求：

- 简洁
- 准确
- 信息密度高
- 中性
- 可读
- 不营销
- 不标题党

禁止：

- 重磅
- 炸裂
- 史诗级
- 行业变天
- 颠覆一切
- 神器
- 遥遥领先
- 彻底改变世界

也不要强行为每条新闻制造“金句”。

事实本身足够有价值时：

直接描述事实。

---

# 35. 数字与具体 Claim

以下数字必须来自 source_record：

- 金额
- 估值
- benchmark
- 参数量
- token 数
- API 价格
- 用户量
- 收入
- 下载量
- 融资规模
- 裁员人数
- 漏洞数量
- 性能提升百分比

禁止：

根据模型记忆补数字。

---

# 36. Source Name 与 Domain Validation

必须验证：

```text
source_name
↓
source_domain
↓
canonical_url
```

三者一致。

例如：

```yaml
Reuters:
  domain: reuters.com

Bloomberg:
  domain: bloomberg.com

TechCrunch:
  domain: techcrunch.com

The Verge:
  domain: theverge.com

OpenAI:
  domain: openai.com

Anthropic:
  domain: anthropic.com
```

例如：

```text
source_name = Bloomberg
source_url = thirdruntime.com/...
```

结果：

```text
VALIDATION_FAIL
```

禁止发布。

---

# 37. 发布前 Story Validation Gate

每条新闻必须检查：

```text
[ ] 已创建真实 source_record
[ ] 来源页面已实际打开
[ ] source_name 正确
[ ] source_domain 正确
[ ] canonical_url 指向真实原文
[ ] source_domain 不在 blocklist
[ ] 最终来源符合 allowlist 规则
[ ] published_at 已确认
[ ] 核心事实与原文一致
[ ] 标题没有夸大
[ ] 所有数字均有明确来源
[ ] 没有根据搜索 snippet 推断事实
[ ] 没有模型自行补充事实
[ ] 重大 claim 已通过额外验证
[ ] 已完成语义事件去重
[ ] 未把 follow-up story 错误删除为重复
[ ] 若为旧事件，存在 material new development
```

关键检查失败：

```text
DO_NOT_PUBLISH
```

---

# 38. 整期 Build Gate

如果任何最终 story 出现：

- blocklisted source
- source_name / domain mismatch
- 无 source_record
- 假 URL
- 无法验证的重大新闻
- 明显模型自行编造的事实

则该 story 必须被删除。

如果问题是系统性的，例如：

- 大量来源无法验证
- 本次搜索流程失败
- 新闻抓取工具异常
- 多条 story 无真实 evidence

则：

```text
BUILD_FAIL
```

不要自动 push 到 GitHub。


---

# 39. 最终原则

AI Radar 不是新闻数量竞赛。

目标不是：

> 今天一定生成 25 条。

目标是：

> 今天发生了哪些真正值得知道、且可以被可靠来源证明的 AI 行业变化？

所以：

### 有 30 条高质量新闻

可以多发。

### 只有 12 条

就发 12 条。

### 某栏目只有 1 条

就放 1 条。

### 某栏目没有重要新闻

可以为空。

### 同一个主题连续三期都有真正的新进展

可以连续三期报道。

### 两篇标题完全不同但其实说的是同一件事

必须去重。

### 两篇标题关键词高度相似但实际是不同进展

必须分别保留。

最后始终遵守：

> **新闻先发生，来源先存在，AI 再负责筛选、组织和摘要。**