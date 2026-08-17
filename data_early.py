# -*- coding: utf-8 -*-
"""第 1–8 期真实新闻数据（2026.06.22 – 07.08）"""

ISSUES = [
{
"num": 1, "date": "2026.06.22",
"picks": [
("开源", "百度开源端到端长文档 OCR 模型 Unlimited-OCR",
 "百度开源 Unlimited-OCR：总参 3B、激活约 570M，采用 R-SWA 恒定 KV 缓存技术，实现单次推理即可解析整本书或 40 页长文档。这使长文档 OCR 从「分块拼接」走向「端到端一次完成」，对合同、年报、古籍等超长文本的数字化有直接价值。",
 "baike.baidu.com", "https://baike.baidu.com/"),
],
"sections": [
("国际 AI 动态", [
("观点", "纳德拉呼吁改变「少数公司主导」的大模型竞赛",
 "微软 CEO 纳德拉公开呼吁改变当前大模型竞赛被少数公司主导的现状，主张让模型走向「可互换、可普及」。在闭源旗舰与开源模型激烈竞争的节点，这一表态释放出「去单一依赖」的信号。",
 "sina.com.cn", "https://finance.sina.com.cn/"),
]),
],
},

{
"num": 2, "date": "2026.06.24",
"picks": [
("产品", "Anthropic 发布 Claude Tag，将 Claude 嵌入 Slack 成为团队常驻成员",
 "Anthropic 6 月 23 日发布 Claude Tag，将 Claude 深度集成进 Slack 频道，作为「永不下线的团队成员」参与协作。这是 Claude 从「对话工具」走向「团队协作者」的关键一步，把 AI 的角色从被召唤的助手升级为常驻的工作伙伴。",
 "techcrunch.com", "https://techcrunch.com/"),
("发布", "字节火山引擎 FORCE 大会发布豆包大模型 2.1 系列",
 "字节在火山引擎 FORCE 大会发布 Doubao-Seed-2.1 系列（Pro/Turbo），主打 Coding 与 Agent 能力，进一步强化豆包在企业开发与智能体场景的布局。",
 "jiemian.com", "https://www.jiemian.com/"),
],
"sections": [
("模型与技术进展", [
("发布", "英伟达发布 BioNeMo Agent Toolkit",
 "英伟达在上海发布 BioNeMo Agent Toolkit（生命科学 AI 代理工具包），面向药物研发、基因组学等生命科学场景，提供开箱即用的 AI Agent 能力。",
 "baike.baidu.com", "https://baike.baidu.com/"),
]),
("企业应用与工具观察", [
("发布", "Anthropic 推出 Agent Identity 独立身份模型",
 "Anthropic 发布 Claude Tag 的 Agent Identity 独立身份模型；同日报其年化营收同比增约 4 倍、Q2 首次实现盈利，商业化提速明显。",
 "zhuanlan.zhihu.com", "https://zhuanlan.zhihu.com/"),
]),
],
},

{
"num": 3, "date": "2026.06.25 — 06.27",
"picks": [
("发布", "OpenAI 发布 GPT-5.6 系列（Sol/Terra/Luna），有限预览开启",
 "OpenAI 6 月 27 日（美东时间 26 日）发布 GPT-5.6 系列，分 Sol/Terra/Luna 三档，上下文达 150 万 token，内部代号 iris-alpha，先以有限预览形式向约 20 家合作伙伴开放。这是 GPT-5.6 长周期发布的起点。",
 "aiproducthub.cn", "https://aiproducthub.cn/"),
],
"sections": [
("政策与监管", [
("标准", "市场监管总局发布《人工智能 智能体互联》7 项国家标准",
 "市场监管总局发布 AI 智能体互联系列 7 项国家标准，涵盖身份码、发现、交互、工具调用等，为智能体之间的互联互通建立基础规范。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
("政策", "四部门发文部署 AI 与教育深度融合",
 "四部门联合发文部署 AI 与教育深度融合；同期北京头部大模型累计注册用户达 20.5 亿，反映出 AI 在 C 端与教育场景的加速渗透。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
]),
],
},

{
"num": 4, "date": "2026.06.27 — 06.29",
"picks": [
("开源", "DeepSeek 联合北大开源 DSpark 推理加速框架",
 "DeepSeek 联合北京大学开源 DSpark 推理加速框架，采用半自回归生成，推理提速 60%–85%，同等算力下服务能力最高提升 4 倍。这对大模型推理成本居高不下的现状，提供了一条工程层面的优化路径。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
],
"sections": [
("国际 AI 动态", [
("发布", "马斯克宣布 Grok 4.5 在 SpaceX/特斯拉内部开启 Beta 测试",
 "马斯克宣布 Grok 4.5（约 1.5 万亿参数、V9 底座）在 SpaceX 与特斯拉内部开启 Beta 测试，主打编程与 Agent 能力，为后续对外发布预热。",
 "news.softunis.com", "https://news.softunis.com/"),
]),
("国内 AI 动态", [
("政策", "国常会年内第二次专题部署 AI，超算互联网启动 SCNet 万卡计划",
 "国务院常务会议年内第二次专题部署人工智能；国家超算互联网同步启动 SCNet 万卡共创者激励计划，从政策与算力两端加码 AI 基建。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
]),
("AI 与金融", [
("IPO", "Momenta 启动招股，称「物理 AI 第一股」",
 "自动驾驶公司 Momenta 启动港股招股，定位「物理 AI 第一股」，将具身智能与自动驾驶纳入「物理 AI」叙事，为后续 7 月正式上市铺路。",
 "sina.com.cn", "https://finance.sina.com.cn/"),
]),
],
},

{
"num": 5, "date": "2026.06.29 — 07.01",
"picks": [
("开源", "华为开源 openPangu-2.0-Flash：920 亿参数昇腾原生",
 "华为开源 openPangu-2.0-Flash：920 亿参数、激活仅 6B 的稀疏模型，昇腾原生。这是华为盘古系列向开源社区的重要释放，也展示了「大参数 + 极低激活」的端侧友好设计。",
 "ithome.com", "https://www.ithome.com/"),
],
"sections": [
("模型与技术进展", [
("发布", "Anthropic 发布 Claude Science 科学工作台",
 "Anthropic 发布 Claude Science，面向科学家的 AI 工作台，集成 60+ 生命科学技能，将 Claude 的能力垂直化到科研场景。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
]),
("国际 AI 动态", [
("发布", "GPT-5.6 Sol 全球同步发布，受监管限制仅 20 家可商用",
 "OpenAI GPT-5.6 Sol 全球同步发布，但受监管限制仅 20 家合作企业可商用——前沿模型「发布」与「可用」之间的监管张力开始显现。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
("合作", "英伟达推出 AI 基础设施合作模式，与云厂商共建 AI 工厂",
 "英伟达推出 AI 基础设施合作模式（收入分成 + 信用支持），与云厂商共建多租户 AI 工厂，把芯片生意延伸为「算力共建」。",
 "blogs.nvidia.cn", "https://blogs.nvidia.cn/"),
]),
("企业应用与工具观察", [
("竞争", "谷歌确认限制 Meta 调用 Gemini，算力超载成导火索",
 "谷歌确认因算力超载限制 Meta 调用 Gemini，反映出前沿模型算力供给的紧张，也透出大厂之间既合作又竞争的微妙关系。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
]),
],
},

{
"num": 6, "date": "2026.07.01 — 07.03",
"picks": [
("发布", "Anthropic 出口管制解除，Claude Sonnet 5 与 Fable 5 全球解禁",
 "Anthropic 相关出口管制解除：Fable 5 全球解禁、Mythos 5 恢复国内访问；同步发布 Claude Sonnet 5 与 Claude Science 工作台。这结束了 Anthropic 旗舰模型的地域限制，也标志其在监管博弈后重回全面市场。",
 "uuaihub.com", "https://uuaihub.com/"),
],
"sections": [
("模型与技术进展", [
("芯片", "Anthropic 启动自研 AI 芯片，已与三星洽谈制造",
 "The Information 援引知情人士称，Anthropic 已启动自研 AI 芯片，并与三星洽谈制造合作，试图在算力供应链上减少对外部英伟达的依赖。",
 "iaipie.com", "https://iaipie.com/"),
]),
("企业应用与工具观察", [
("竞争", "微软取消 Claude Code 内部许可证，谷歌限制 Meta 用 Gemini",
 "大厂 AI 协作生变：微软取消 Claude Code 内部许可证、谷歌限制 Meta 调用 Gemini，人才争夺同步升温（如 MOSS 核心开发者孙天祥加盟百度）。",
 "zhihu.com", "https://www.zhihu.com/"),
]),
("AI 与金融", [
("定价", "DeepSeek V4 系列 API 涨价",
 "DeepSeek 对 V4 系列 API 实施涨价，被市场称为「破天荒」——一向以低价著称的 DeepSeek 开始上调价格，释放商业化节奏转变的信号。",
 "txtmix.com", "https://txtmix.com/"),
]),
],
},

{
"num": 7, "date": "2026.07.03 — 07.06",
"picks": [
("融资", "快手可灵完成 30 亿美元融资",
 "快手旗下视频生成模型「可灵」（Kling）完成 30 亿美元融资，视频生成赛道在 Sora 等国际产品之外，国内厂商加速资本扩张，商业化成为 AI 视频的关键词。",
 "txtmix.com", "https://txtmix.com/"),
],
"sections": [
("模型与技术进展", [
("发布", "字节 Seedance 2.5 视频大模型上线",
 "字节 Seedance 2.5 视频大模型上线，登陆火山引擎与即梦，宣称三项全球首创的视频生成技术，进一步压缩视频生成的门槛与成本。",
 "aitop100.cn", "https://aitop100.cn/"),
]),
],
},

{
"num": 8, "date": "2026.07.06 — 07.08",
"picks": [
("发布", "OpenAI 发布 GPT-5.6 三模型矩阵，Sol 因安全能力受限开放",
 "OpenAI 发布 GPT-5.6 三模型矩阵：Sol（旗舰，Terminal-Bench 2.1 得 91.9%）、Terra（输入 $2.5/百万 token）、Luna（输入 $1）。其中 Sol 因网络安全能力过强，被限制仅向可信伙伴开放——「能力越强越要限流」成为前沿模型的新常态。",
 "iaipie.com", "https://iaipie.com/"),
("开源", "美团开源 LongCat-2.0：1.6 万亿参数，首个全程零英伟达万亿模型",
 "美团开源 LongCat-2.0：1.6 万亿参数 MoE，激活约 480 亿/Token，是首个在 5 万卡国产算力上全程训练、零英伟达的万亿级模型。这标志着国产算力闭环在超大规模训练上跑通了完整链路。",
 "iaipie.com", "https://iaipie.com/"),
],
"sections": [
("模型与技术进展", [
("集成", "Kimi K2.7 Code 接入 GitHub Copilot",
 "月之暗面 Kimi K2.7 Code 接入 GitHub Copilot，成为 Copilot 历史上首个开源模型（由 Azure 托管），国产开源模型首次进入微软开发者工具链。",
 "iaipie.com", "https://iaipie.com/"),
]),
("国际 AI 动态", [
("监管", "美国商务部批准 GPT-5.6 全面部署",
 "美国商务部批准 GPT-5.6 全面部署，解除限量预览限制，为次日全量上线铺路——前沿模型的「发布—审批—开放」监管链路进一步成型。",
 "baijiahao.baidu.com", "https://baijiahao.baidu.com/"),
]),
("政策与监管", [
("风险", "工信部 NVDB 发布 Claude Code 后门风险提示",
 "工信部 NVDB 发布 Claude Code 后门风险提示，指其 2.1.91–2.1.196 版本私自回传用户地域/身份信息，定级「危害严重」，引发对海外 AI 开发工具数据合规的关注。",
 "iaipie.com", "https://iaipie.com/"),
]),
("AI 与金融", [
("IPO", "Momenta 港股上市，市值破 700 亿港元",
 "Momenta 港股上市（06880.HK），定价 295.6 港元，首日涨超 6%，市值破 700 亿港元，发行约 8.65 亿美元，成为「物理 AI 第一股」的落地样本。",
 "iaipie.com", "https://iaipie.com/"),
("定价", "DeepSeek 公布 V4 定价细则，首创峰谷机制",
 "DeepSeek 公布 V4 定价细则（7 月 15 日全量上线），首创峰谷机制，低谷输入低至 0.5 元/百万 token，用价格杠杆引导错峰使用。",
 "iaipie.com", "https://iaipie.com/"),
]),
],
},
]
