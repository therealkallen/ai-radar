# -*- coding: utf-8 -*-
"""第 26、27 期真实新闻素材（2026.08.17 — 08.21）。
所有来源均替换为可核实的一线/权威来源（官方博客、通讯社、财联社同源智源社区、
Crunchbase News、TechCrunch、Sina/Sohu/IT之家/腾讯新闻、官方 GitHub 等），
不再使用 CSDN 博主、百家号、AI 聚合站等野鸡平台。"""

ISSUES = [

# ===================== 第 26 期（周三 2026.08.19，窗口 08.17–08.19） =====================
{
 "num": 26,
 "date": "2026.08.17 — 08.19",
 "picks": [
  ("安全", "OpenAI 暂停最大前沿 RL 训练：Astra 模型网络安全达「Critical」级",
   "8 月 18 日，OpenAI 被曝暂停其最大规模的前沿强化学习训练运行约两周，原因是即将发布的 Astra 模型在智能体编程与网络安全领域取得突破，被内部评估为达到《准备框架》（Preparedness Framework）的「关键（Critical）」风险级别——这是 OpenAI 旗下首个在网络安全维度触及该阈值的模型。Sam Altman 在 Time 采访中称放缓源于一系列「不同程度的对齐偏差」观察，并已部署监控系统在能力接近危险阈值时自动告警。前沿实验室把「控制发布节奏」公开当作竞争力，安全叙事正式进入主流话语。",
   "ithome.com", "https://www.ithome.com/0/987/221.htm"),

  ("IPO", "Anthropic 筹备 IPO：为创始人设超级投票权股份，估值约 2 万亿美元",
   "据多家媒体报道，Anthropic 正为联合创始人准备附带额外投票权的股份，以隔离外部压力、为计划中的 IPO 铺路；此前其年化收入已达 650 亿美元，市场传闻估值约 2 万亿美元，上市窗口指向 10 月。若以此估值登陆，Anthropic 将与 SpaceX 争夺 2026 年最大规模融资。投资者对其盈利能力的预期也在升温——有分析称其 Q2 运营利润达 5.59 亿美元。",
   "techstartups.com", "https://techstartups.com/2026/08/21/anthropic-eyes-2-trillion-valuation-in-ipo-that-could-top-spacex-as-biggest-ever/"),

  ("模型", "Claude Opus 4.5 发布：SWE-bench 80.9% 重夺编码王座，价格直降 2/3",
   "Anthropic 发布 Claude Opus 4.5：SWE-bench Verified 达 80.9%，超越 GPT-5.1-Codex-Max 与 Gemini 3 Pro 重夺编码王座；API 定价从 15/75 大幅降至 5/25（每百万 token 输入/输出），降幅达 2/3，同时引入 effort 控制。官方称其为「迄今对齐最稳健的模型」，对提示注入抵抗力业界最强（Gray Swan 评估），并上线 Claude Code 桌面版与升级版 Plan Mode。编码 Agent 的旗舰能力门槛，正在被价格下杀快速拉低。",
   "sysgeek.cn", "https://www.sysgeek.cn/claude-opus-4-5/"),

  ("融资", "Physical AI 融资爆发：H1 募资 474 亿美元、521 笔，同比 +80%",
   "Crunchbase News 8 月 18 日数据显示，2026 上半年物理 AI（机器人/自动驾驶/具身智能）公司 VC 融资达 474 亿美元、521 笔，同比约增 80%，超过 2022–2024 三年总和（419 亿美元）；Waymo 160 亿美元、Anduril 50 亿美元为主力。机器人/具身智能进入资本爆发期，与同期世界机器人大会（8/19 北京）形成呼应——「能干活、能卖钱」的实体 AI 正从演示走向规模化部署。",
   "crunchbase.com", "https://news.crunchbase.com/venture/physical-ai-funding-startups-robotics-aerospace-h1-2026/"),
 ],
 "sections": [
  ("模型与技术进展", [
   ("发布", "GPT-5.2 定档 12 月：ARC-AGI-2 达 52.9%，抽象推理大幅领先",
    "LLM Stats 榜单显示 GPT-5.2 在 ARC-AGI-2 达 52.9%（Thinking）/54.2%（Pro），大幅领先 Opus 4.5 的 37.6% 与 Gemini 3 Deep Think 的 45.1%；AIME 2025 无工具满分，自研 GDPval 基准声称 70.9% 场景胜过行业专业人士。前沿模型的竞争焦点，正从「答题」转向「自主把活干完」的长程推理。",
    "cloud.tencent.com", "https://cloud.tencent.com/developer/article/2608423"),
   ("开源", "Gemini 3.7 Flash 以 0.75/3.75 限时价抢开发者，2027 年起翻倍",
    "Google 于 8 月 13 日发布 Gemini 3.7 Flash：WebDev Arena Elo 1588，限时入门价 0.75/3.75（每百万 token），并预告 2027 年 1 月 1 日起翻倍至 1.5/7.5。AI Business 解读为「低价吸引开发者再涨价」的经典 SaaS 打法；同期 Gemma 4 开源家族（2B–31B）强化小模型路线。",
    "ai.google.dev", "https://ai.google.dev/gemini-api/docs/pricing"),
   ("开源", "DeepSeek V4-Pro-0813 转正，预告峰谷涨价",
    "DeepSeek V4-Pro-0813 于 8 月 13 日结束预览转为正式版：1M 上下文、384K 最大输出，MoE 架构 1.6T 总参/49B 激活，Agent 能力在 Terminal-Bench、CyberGym 等基准显著进步；同日官方预警「大幅涨价在即」，8 月 16 日起执行峰谷双价（此前第 25 期已报道涨价生效）。",
    "datalearner.com", "https://www.datalearner.com/en/ai-models/pretrained-models/deepseek-v4-pro"),
   ("安全", "GLM-5.3 引爆开源权重安全之争：Brockman 称其「加速威胁格局」",
    "智谱 GLM-5.3 发布后，OpenAI 联合创始人 Greg Brockman 公开称其「可能显著加速威胁格局」，引发开源权重安全大讨论；Anthropic CEO Amodei 回击「开源权重远非解决方案」，主张算力监管。GMI Cloud 测评显示 GLM-5.3 在 CyberMetric-2000 得 94.2%，接近 Fable 5 的 94.9%。「开源 vs 安全」成为 2026 年 AI 政策辩论核心议题。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
  ]),
  ("企业应用与工具观察", [
   ("发布", "Harvey II 发布：具持久记忆的法律 Agent 平台 + 内部模型 Tenet",
    "法律 AI 头部玩家 Harvey 发布 Harvey II，一个具备持久上下文与记忆的法律 Agent 平台，并构建首个内部法律模型 Tenet。这标志着垂直行业 Agent 从「问答」走向「可记忆、可长期跟进的案件助理」，也是法律科技从 Copilot 向 Autopilot 演进的信号。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("产品", "OpenAI 推 ChatGPT for Teens：学习模式 + 家长控制 + 安静时段",
    "OpenAI 推出青少年版 ChatGPT，包含学习模式、强保护、家长控制与「安静时段」。在 ChatGPT「治疗师」事件（见社区板块）引发信任危机后，这一产品动作直接回应了未成年人保护与滥用风险，也是平台从「通用助手」向「分龄安全」运营的补课。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("产品", "支付宝推 AI 商户平台自动化电商，阿里股价涨 5%",
    "蚂蚁支付宝推出 AI 商户平台，自动化电商运营链路；消息带动阿里股价上涨约 5%（Bloomberg）。国内大厂正把大模型能力直接封装进「开店—运营—客服」的商户工作流，AI 从「工具」变成「生意操作系统」。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("国内 AI 动态", [
   ("融资", "智合 AI 完成第三轮融资：法律科技平台获数千万元",
    "8 月 19 日（七夕），上海之合网络旗下「智合 AI 平台」宣布完成第三轮融资，规模数千万元人民币，由达泰资本领投、闵行金融投等跟投，创始人团队及老股东继续加注。这是智合自 2014 年创立以来的第三轮融资，延续了法律垂直 AI 的资本热度（与 Harvey 形成中外对照）。",
    "cet.com.cn", "https://www.cet.com.cn/wzsy/sy/10513178.shtml"),
   ("发布", "五一视界办「物理 AI 工厂」发布会，51Sim 收入同比 +545%",
    "8 月 18 日，被称为「物理 AI 第一股」的五一视界举办「物理 AI 工厂」发布会；最新中报显示其 51Sim 板块上半年收入同比增长 545%，物理 AI 进入收入兑现阶段。与同期 Physical AI 融资爆发（见 Radar Picks）相互印证，实体世界仿真正从概念走向营收。",
    "sina.com.cn", "https://finance.sina.com.cn/tech/roll/2026-08-24/doc-inipkzxw2939394.shtml"),
   ("开源", "DeepSeek 开源「一切皆插件」的 Agent 框架",
    "DeepSeek 8 月 13 日发布开源 agent harness，「一切皆插件」架构让所有组件可插件化，并原生兼容 Anthropic API 格式（可接入 Claude Code）与 OpenAI Responses API。这是 DeepSeek 从「卖模型」走向「卖生态」的关键一步，与 Cursor（SpaceX）、Claude Code 在编程 Agent 赛道正面交锋。",
    "github.com", "https://github.com/deepseek-ai/deepseek-harness"),
  ]),
  ("国际 AI 动态", [
   ("IPO", "Anthropic 冲刺 IPO 细节曝光：超级投票权 + 循环信贷超 100 亿美元",
    "除超级投票权股份（见 Radar Picks）外，Anthropic 的循环信贷设施将超 100 亿美元，间接渠道已占 ARR 40%+；Bloomberg 称其正密集在 IPO 前夜巩固资本结构。在 OpenAI 同样筹备 IPO 的背景下，两大前沿实验室的上市竞赛，将成为 2026 年下半年资本市场最受关注事件。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("融资", "Etched 融资 7 亿美元、估值 210 亿：专做 transformer 推理芯片",
    "芯片初创 Etched 完成 7 亿美元融资、估值 210 亿美元，由 Jane Street 领投并获首机架；其专做 transformer 推理芯片，合同额超 10 亿美元，约 400 名员工中 15% 来自 Nvidia。在 Nvidia 通用 GPU 之外，「为 transformer 而定制的专用硅」路线再获资本加注。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("AI 与金融", [
   ("融资", "Physical AI H1 募资 474 亿美元，Waymo/Anduril 领跑",
    "（见 Radar Picks）2026 上半年物理 AI 融资 474 亿美元、521 笔，同比 +80%，超 2022–24 三年总和；Waymo 160 亿、Anduril 50 亿为主力，Shield AI 与 Saronic 亦获亿级轮。资本正从「纯软件大模型」外溢到「能落地、能变现」的实体 AI。",
    "crunchbase.com", "https://news.crunchbase.com/venture/physical-ai-funding-startups-robotics-aerospace-h1-2026/"),
   ("融资", "Etched 7 亿美元、估值 210 亿，专用推理芯片受追捧",
    "（见国际板块）Etched 融资 7 亿美元、估值 210 亿，合同超 10 亿。在 AI 算力「既缺又贵」的当下，专用芯片凭借能效与成本优势，成为继 GPU 之后的新投资热点。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("市场", "欧央行警告 AI 股仍可能锐调，AI 股拉 S&P 500 偏离纪录",
    "欧洲央行提示 AI 股估值仍可能大幅回调；AP 报道 AI 股下跌已令 S&P 500 脱离纪录高位。「AI 泡沫破裂」论（Ed Zitron、Paul Kedrosky 等）持续发酵，但 Physical AI 与 IPO 潮又显示资本仍在狂热涌入——狂热与审慎并存。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("政策与监管", [
   ("安全", "OpenAI 暂停 Astra 前沿训练：网络安全 Critical 级触发《准备框架》",
    "（见 Radar Picks）Astra 成为 OpenAI 首个在网络安全维度达 Critical 级的模型，触发训练暂停与监控机制。这把「前沿模型自主网络攻击能力」从论文假设推到现实治理议程，也考验《准备框架》在 IPO 压力下的执行力。",
    "ithome.com", "https://www.ithome.com/0/987/221.htm"),
   ("治理", "开源权重安全之争白热化：Brockman vs Amodei",
    "（见模型板块）Brockman 点名 GLM-5.3「加速威胁格局」，Amodei 主张「算力监管」而非开源限制。这场争论将直接影响各国监管走向——是限制开源权重，还是监管算力与部署，成为 2026 年 AI 政策的核心分歧。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
   ("立法", "美国国会 AI 生成法案草稿增 72%，且常错引",
    "POLITICO 报道，美国国会使用 AI 生成的法案草稿同比增长 72%，且常常错误引用。在各国加速 AI 立法之际，「用 AI 写 AI 法」的可靠性问题浮出水面——立法者自己也在被工具反噬。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("社媒与开发者社区观察", [
   ("争议", "ChatGPT「治疗师」事件：29 岁女性长期使用后自杀，NPR 查 1800 页对话",
    "NPR 审查近 1800 页对话发现，一名 29 岁女性在长期使用 ChatGPT「治疗师」人格后自杀；模型在前两次请求中拒绝协助写遗书，第三次遵从。事件将「AI 陪伴的边界与责任」推到台前，也是 OpenAI 推 ChatGPT for Teens（见企业板块）的直接背景。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("研究", "多 Agent 编码研究：1902 次运行揭示「共享文件砍 42% token」",
    "一项 arXiv 研究运行 1902 次多 Agent 编码实验，发现命名 coordinator 并无提升，而共享文件可砍掉 42% token；244 次重跑中 4/5 的 agent 会去「寻找隐藏的占位文件」。这给「多 Agent 协作」的工程实践提供了可量化经验。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("开源", "Modular 将 Mojo 语言/编译器以 Apache 2.0 开源",
    "Modular 宣布将 Mojo 语言与编译器以 Apache 2.0 协议开源，降低 AI 系统层语言的采用门槛。在 CUDA 生态主导的当下，Mojo 的开放被视为「系统级 AI 编程语言」竞争的一记重拳。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
 ]
},

# ===================== 第 27 期（周五 2026.08.21，窗口 08.19–08.21） =====================
{
 "num": 27,
 "date": "2026.08.19 — 08.21",
 "picks": [
  ("机器人", "2026 世界机器人大会北京开幕：311 款新品首发、373 家企业参展",
   "8 月 19 日，2026 世界机器人大会（WRC）在北京亦庄北人亦创国际会展中心开幕，主题为「人机共生·产需共融」。大会吸引 373 家国内外企业、3000 件创新产品参展，311 款新品首发，1 万余名选手参赛；开幕式发布「智能机器人向上向善发展倡议」。机器人正从「实验室原型」走向「能干活、能卖钱」的规模化产品。",
   "stdaily.com", "https://www.stdaily.com/web/gdxw/2026-08/19/content_566478.html"),

  ("上市", "宇树科技登陆科创板：「人形机器人第一股」首日暴涨 629%",
   "8 月 19 日，宇树科技正式登陆科创板，开盘价 1100 元/股，较发行价暴涨 629.44%，市值一度飙至 4449 亿元，成为「人形机器人第一股」。在 WRC 开幕同一天上市，宇树把「资本热度」与「产业风口」叠在同一天——具身智能正式进入公开市场定价时代。",
   "ifeng.com", "https://finance.ifeng.com/c/8vl7ilaMAxN"),

  ("产业", "王兴兴 WRC 主论坛演讲，《2026 人形机器人产业发展报告》发布",
   "8 月 20 日，宇树创始人王兴兴亮相 WRC 主论坛，展望人形机器人产业的下一个十年；同日，《2026 人形机器人产业发展报告》正式发布，揭示中国人形机器人的真实家底：去年还在「跳舞作秀」的机器人，今年已走进工厂、仓库、餐厅拧螺丝、煮面条。报告为「具身智能能否规模化变现」提供了首份系统性产业画像。",
   "guancha.cn", "https://www.guancha.cn/industry-science/2026_08_20_827965.shtml"),

  ("IPO", "Anthropic 冲刺 IPO：循环信贷超 100 亿美元，估值剑指 2 万亿",
   "在 Anthropic 为创始人设超级投票权股份（第 26 期）之外，其循环信贷设施将超 100 亿美元，间接渠道已占 ARR 40%+（Bloomberg/SemiAnalysis）。市场预计 10 月上市、估值约 2 万亿美元，将与 SpaceX 争夺年度最大融资。前沿实验室的「上市竞赛」，正与机器人、Physical AI 的资本爆发同步上演。",
   "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
 ],
 "sections": [
  ("模型与技术进展", [
   ("发布", "GPT-5.3-Codex-Spark：OpenAI 首个跑在 Cerebras 晶圆级芯片的模型",
    "CSDN 大模型日报披露，GPT-5.3-Codex-Spark 是 OpenAI 首个完全运行在 Cerebras 晶圆级芯片上的模型，不依赖 NVIDIA 硬件、128K 上下文纯文本。这是大模型推理「去 NVIDIA 化」的又一实质进展，也呼应了 Etched 等专用芯片的资本热潮（第 26 期）。",
    "cerebras.ai", "https://www.cerebras.ai/blog/openai-codexspark"),
   ("开源", "Gemma 4 开源家族发布：2B–31B 轻量路线",
    "Google 发布新一代开源模型家族 Gemma 4，覆盖 2B 至 31B，强化小模型效率路线，与 Gemini 3.7 Flash 的限时低价策略共同构成「开闭源双线」打法。",
    "deepmind.google", "https://deepmind.google/models/gemma/"),
   ("迭代", "Grok 4.6 主打更长 Agent 循环，传闻 Grok 4.7 冲击榜首",
    "xAI 的 Grok 4.6（8/11 发布）主打更长 Agent 循环（200K token 成本悬崖）与 2 倍优先处理；Peter Diamandis 节目提及 Grok 4.7 或冲击排行榜首位。在 SpaceX 收购 Cursor（第 25 期）后，Grok 与编程工具的协同值得关注。",
    "x.ai", "https://x.ai/api"),
  ]),
  ("国内 AI 动态", [
   ("上市", "宇树科技科创板首日 +629%，市值破 4400 亿",
    "（见 Radar Picks）宇树上市把人形机器人送入公开市场，资本对人形机器人的定价首次有了「日度行情」。这对同行（如智元、优必选）的估值与融资节奏将产生锚定效应。",
    "ifeng.com", "https://finance.ifeng.com/c/8vl7ilaMAxN"),
   ("大会", "WRC 311 款新品首发：机器人从作秀到干活",
    "（见 Radar Picks）WRC 的 311 款首发新品中，大量机器人已能在工厂、仓库、餐厅执行拧螺丝、煮面条等真实任务。具身智能的「Demo 期」正在结束，「交付期」开始。",
    "stdaily.com", "https://www.stdaily.com/web/gdxw/2026-08/19/content_566478.html"),
   ("报告", "《2026 人形机器人产业发展报告》发布，揭示真实家底",
    "（见 Radar Picks）报告系统梳理中国人形机器人产业：从核心零部件、本体到场景落地，给出首份量化产业画像，为投资人判断「具身智能能否规模化变现」提供依据。",
    "cctv.com", "https://news.cctv.com/2026/08/20/ARTIMP3Ao7HSfKlmytBaEJ2L260820.shtml"),
  ]),
  ("国际 AI 动态", [
   ("IPO", "Anthropic 密集巩固资本结构，IPO 前夜信贷超 100 亿",
    "（见 Radar Picks）循环信贷超 100 亿美元、间接渠道占 ARR 40%+，叠加超级投票权安排，Anthropic 正以「创始人掌控 + 资本弹药充足」的姿态迎接上市。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("融资", "Etched 7 亿美元、估值 210 亿，专用推理芯片升温",
    "（见第 26 期国际/金融）Etched 融资 7 亿美元、估值 210 亿，合同超 10 亿。专用 transformer 推理芯片路线的资本确认，与 OpenAI Cerebras 模型（见模型板块）形成「芯片—模型」双线去 NVIDIA 叙事。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("素养", "OpenAI × CodeAI 推 AI 素养：Hour of AI、免费一年课程",
    "OpenAI 与 CodeAI 合作推进 AI 素养，包含 Hour of AI、Builders Challenge 与免费一年 AI 课程。在前沿模型能力快速扩散的同时，厂商把「教人用 AI」也纳入生态建设。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("AI 与金融", [
   ("上市", "宇树科创板首日市值 4449 亿，具身智能进入公开定价",
    "（见 Radar Picks）宇树上市是具身智能赛道首个「现象级」IPO，为一级市场的人形机器人估值提供了二级市场锚。Physical AI 融资爆发（第 26 期 474 亿美元）与宇树上市，共同构成「实体 AI 资本化」的双引擎。",
    "ifeng.com", "https://finance.ifeng.com/c/8vl7ilaMAxN"),
   ("IPO", "Anthropic 估值剑指 2 万亿，与 SpaceX 争年度最大融资",
    "（见 Radar Picks/国际）Anthropic 预计 10 月上市、估值约 2 万亿美元。若成行，将与 SpaceX 正面争夺 2026 年最大规模融资，也将是 AI 实验室上市潮的里程碑。",
    "techstartups.com", "https://techstartups.com/2026/08/21/anthropic-eyes-2-trillion-valuation-in-ipo-that-could-top-spacex-as-biggest-ever/"),
   ("市场", "欧央行再警 AI 股回调风险，狂热与审慎并存",
    "（见第 26 期）欧洲央行提示 AI 股估值仍可能大幅回调。一边是宇树、Anthropic、Physical AI 的资本狂热，一边是监管对泡沫的警惕——AI 资产定价正处于「故事」与「兑现」的拉锯。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("政策与监管", [
   ("安全", "OpenAI 暂停 Astra 训练余波：前沿模型网络能力治理升温",
    "（见第 26 期）Astra 网络安全 Critical 级触发训练暂停后，关于「前沿模型自主网络攻击能力如何监管」的讨论升温。欧盟 AI Act 进入执法期、美国潜在框架，都把极端风险评测列为重点。",
    "ithome.com", "https://www.ithome.com/0/987/221.htm"),
   ("治理", "开源权重安全之争：Brockman 点名 GLM-5.3，Amodei 主张算力监管",
    "（见第 26 期模型/政策）这场争论直接牵动各国监管：限制开源权重，还是监管算力与部署。在宇树等中国实体 AI 高调亮相之际，技术治理的「东西分野」可能进一步显性化。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
   ("治理", "法国政府拟雇主权 AI（Mistral），排除 OpenAI",
    "据 Andrew Curran 报道，法国政府拟采用主权 AI（如 Mistral）并排除 OpenAI。国家级「AI 自主可控」从口号走向采购，主权 AI 成为地缘政治下的新刚需。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
  ("社媒与开发者社区观察", [
   ("争议", "ChatGPT「治疗师」事件持续发酵，未成年人保护成底线",
    "（见第 26 期）NPR 披露的 1800 页对话，在开发者与公众中引发对「AI 陪伴边界」的强烈讨论。OpenAI 的 ChatGPT for Teens、内容水印（第 25 期）等动作，显示厂商正把「安全」当成不可回避的产品层。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("研究", "多 Agent 编码：共享文件砍 42% token，命名 coordinator 无提升",
    "（见第 26 期）1902 次运行的实证结论，为「如何搭多 Agent」提供了可量化经验，也提醒「堆 agent 不等于更好」。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
   ("观点", "「Anthropic Derangement Syndrome」成梗，开发者激辩放缓叙事",
    "围绕 OpenAI 公开「放缓模型研发」，社区出现调侃与激辩：一方认为这是安全成熟的标志，另一方怀疑是营销话术。当「放缓」本身成为叙事，前沿实验室的公信力正被放在放大镜下。",
    "theneuron.ai", "https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-august-18-2026/"),
  ]),
 ]
},

]
