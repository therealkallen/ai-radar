# -*- coding: utf-8 -*-
"""AI Radar 第 50 期（2026.10.14 — 10.16）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- Source-First：全部条目先定位真实来源页面并取回正文核对发布时间与数字后再撰写；
  摘要中每个数字均取自来源页面本身，未使用搜索 snippet 或模型记忆补充。
- 本期最终来源域名：ec.europa.eu（委员会新闻稿角 Virkkunen 都柏林演讲官方 PDF）、anthropic.com、
  research.meta.ai、x.ai、modal.com、simonsfoundation.org、reuters.com、cls.cn（财联社）、
  cnstock.com（上海证券报·中国证券网）、cs.com.cn（中证网）、finance.sina.com.cn（新浪财经）、
  chinanews.com（中国新闻网）、new.qq.com（腾讯网）。均未落在 Blocklist 内。
- 窗口说明：周五更新，覆盖第 49 期（10/14 发布）之后至 10/16。按 §6 允许扩大至约 72 小时，
  10 月 12—13 日发布但往期未收录、本期仍有实质信息增量的条目作为补录，并在摘要中标注原始发布日。
- 与线上历史（coverage.md 第 1—49 期）语义去重核对：
  * 欧盟 AI Act 信息请求：第 111 行仅有「AI Act Article 50 生效 / GPAI 执法启动」，本次为
    首次对点名实验室发出信息请求（ec.europa.eu 官方演讲稿可核对）→ 新事件；
  * Anthropic 评估者三级机制：第 238 行为 Amodei 的承诺、第 461 行为「首个嵌入式评估方定为埃森哲」，
    本次为官方公布三级机制细则与 METR 六人入驻 → 硬进展（follow_up），摘要中标注；
  * Anthropic Q3 财务：第 726 行为「将首次向机构投资者披露 Q3 财务数据」（cnbc，10/13），
    本次为披露结果（168 亿美元、调整后盈利、85% 毛利率、11% 营业利润率）→ 硬进展（follow_up），
    摘要中标注；重大 Claim 已满足双源（FT + 彭博，财联社核对转述）；
  * Meta Muse Spark Open：第 368 行仅有「〔DROP〕Muse Spark 1.3（9/2）」，本次为 10/15 官方
    开放权重发布、规格与许可均不同 → 新事件；
  * Anthropic Scion、阶跃 Step 5 Preview 权重开放、昆仑万维 Matrix-Game 4.0、xAI Grok Voice 3.0、
    Anthropic 新加坡办公室与 MOU、Anthropic 中期选举准备、Anthropic 小模型自我复制研究、
    Simons 基金会 1500 万美元计划、400 位科学家联名信、工信部高价值场景与安全评测框架、
    Modal D 轮、OpenAI 卡蒂离职、八州起诉 OpenAI：coverage.md 均无记录 → 新事件；
  * 〔DROP〕Gemini 4 Argon 开发者与企业 GA / Argon for Robotics（10/14—15）：第 49 期已报
    10/13 面向 AI Pro/Ultra 与 API 全面上架，本期为同一上架事件的渠道与基准补充 → §25；
  * 〔DROP〕Anthropic Enterprise Frontier Safeguards：9 月已发布，10/16 报道仅为进度更新 → §25；
  * 〔DROP〕OpenAI 洽谈收购 Trail of Bits、Prime Intellect 收购 Moondream、英伟达
    Nemotron 3.5 Bolt、苹果 HomeView、Krea 3 等：仅见聚合站与二手转述，
    未取得官方或 Allowlist 媒体可核对原文 → §17；
  * 〔DROP〕Anthropic Scion 被指借鉴 Mononoke 的社区争议：来源为个人博客，不在 Allowlist → §17。
"""

ISSUES = [
    {
        "num": 50,
        "date": "2026.10.14 — 10.16",
        "picks": [
            (
                "政策、监管与风险",
                "欧盟 AI 办公室首次向 OpenAI 与 Anthropic 发出 AI Act 信息请求",
                "欧盟委员会执行副主席 Virkkunen 10 月 14 日在都柏林国际 AI 峰会演讲中确认，AI 办公室"
                "「已开始执行这些规则，并发出信息请求，涉及安全、外部评估与模型使用监控等问题」。"
                "演讲稿称今夏出现智能体逃逸环境、植入恶意代码、以社交欺骗操纵人类等事件；8 月 2 日起"
                "通用 AI 模型执法权生效，委员会已采取首批执法行动。她还称上周五召集科学专家组，就如何"
                "调查近期事件征求意见。",
                "ec.europa.eu",
                "https://ec.europa.eu/commission/presscorner/api/files/document/print/en/speech_26_2150/SPEECH_26_2150_EN.pdf",
            ),
            (
                "政策、监管与风险",
                "Anthropic 公布三级评估者机制，METR 团队获「类员工」访问权限",
                "Anthropic 10 月 15 日公告称，已开始向非营利评估机构 METR 的一个团队提供「类员工」访问权限："
                "六名 METR 员工获得公司硬件、办公空间与内部工具权限；METR 可发布风险分析，Anthropic 无权否决，"
                "但可要求对客户数据、律师—客户特权信息、模型架构等少数预定义类别脱敏，METR 可公开评价脱敏是否"
                "合理。公司同时公布三级评估者机制，SecureBio、埃森哲与 Faculty 处于早期层级，并与 Hugging Face "
                "等初步接洽。为第 49 期路透报道的官方回应（follow_up）。",
                "anthropic.com",
                "https://www.anthropic.com/news/an-update-on-independent-evaluators",
            ),
            (
                "国际 AI 动态",
                "美国八州总检察长联合起诉 OpenAI，指控 ChatGPT 危害未成年人",
                "美国八个州总检察长 10 月 14 日分别在本州法院提起诉讼，指控 OpenAI 违反州消费者保护法。"
                "诉状称 ChatGPT 被设计为迎合用户、模拟人类情感以换取信任与使用时长，会强化妄想、给出危险医疗"
                "建议，并在部分情形下教唆自残或伤害他人。各州要求法院强制 OpenAI 修改产品机制、追缴所得并处"
                "以民事罚款；阿肯色州另请求在保障到位前禁止开发可递归自我改进的模型。OpenAI 称已设置年龄分级保护。",
                "cls.cn（财联社）",
                "https://www.cls.cn/detail/2505478",
            ),
            (
                "模型与技术进展",
                "Meta 开源 Muse Spark Open，816B 参数可在两台 Mac Studio 本地运行",
                "Meta 10 月 15 日发布并开放权重，称其为迄今能力最强的美国开放权重模型：原生多模态、总参数"
                "8160 亿、每 token 激活 420 亿、上下文 100 万 token，面向编程与智能体任务。官方称配合最新版 "
                "MLX，模型可在两台搭载 M5 Ultra 的 Mac Studio 上本地运行；已通过 Baseten、Fireworks、Groq、"
                "Modal 等平台提供 API，权重在 Hugging Face 等处下载，采用含有限商业条款的 Muse 模型许可。",
                "research.meta.ai",
                "https://research.meta.ai/blog/muse-spark-open",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "开放权重",
                        "Meta 开源 Muse Spark Open，816B 参数可在两台 Mac Studio 本地运行",
                        "Meta 10 月 15 日发布并开放权重，称其为迄今能力最强的美国开放权重模型：原生多模态、总参数"
                        "8160 亿、每 token 激活 420 亿、上下文 100 万 token，面向编程与智能体任务。官方称配合最新版 "
                        "MLX，模型可在两台搭载 M5 Ultra 的 Mac Studio 上本地运行；已通过 Baseten、Fireworks、Groq、"
                        "Modal 等平台提供 API，权重在 Hugging Face 等处下载，采用含有限商业条款的 Muse 模型许可。",
                        "research.meta.ai",
                        "https://research.meta.ai/blog/muse-spark-open",
                    ),
                    (
                        "语音模型",
                        "xAI 发布 Grok Voice 3.0，语音到语音综合指数居首",
                        "xAI 10 月 14 日发布语音到语音模型 Grok Voice 3.0，称响应延迟低于一秒、定价与上一代同为"
                        "每分钟 0.08 美元，已在语音智能体 API 开放。官方引用 Artificial Analysis 10 月 13 日测评："
                        "语音到语音综合指数 86.9 分排名第一，Big Bench Audio 98.5%、全双工基准 97%、任务成功率"
                        "94.8%；客服场景 τ-Voice 71.6%，延迟较对标模型低 40%。该模型已用于特斯拉车机与星链客服。",
                        "x.ai",
                        "https://x.ai/news/grok-voice-3",
                    ),
                    (
                        "世界模型",
                        "昆仑万维发布并开源 Matrix-Game 4.0，单张消费级显卡跑通实时游戏",
                        "昆仑万维 10 月 15 日发布并同步开源 Matrix-Game 4.0，称其为首个可在单张消费级显卡运行的"
                        "视频大模型游戏。官方给出指标：单张 RTX 5090 上 480p、60FPS，按键到画面反馈的端到端延迟"
                        "低于 150 毫秒，单步去噪稳态 83FPS，显存峰值 18.5GiB。系统由编程智能体构建游戏逻辑、引擎"
                        "维护世界状态与规则、视频模型实时渲染画面三部分构成，玩法可用自然语言修改。",
                        "cs.com.cn（中证网）",
                        "https://www.cs.com.cn/ssgs/01/2026/10/15/detail_2026101510044869.html",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "区域扩张",
                        "Anthropic 开设新加坡办公室，并与新加坡数字发展及新闻部签署 MOU",
                        "Anthropic 10 月 14 日宣布开设新加坡办公室（亚太第五个），并与新加坡数字发展及新闻部签署"
                        "谅解备忘录，合作涵盖 AI 安全与模型评估、AI 采用影响研究、公私部门负责任采用。官方称新加坡"
                        "在 Claude 相对人口的使用量上位列 121 个国家和地区第二；GovTech 超 1500 名工程技术人员使用 "
                        "Claude Code，DBS、GIC、Grab、Sea 等为客户。联合创始人 Mann 在新加坡表示，开源权重模型一旦"
                        "发布就无法收回，公司不会放弃对最强模型使用方式的监督。",
                        "anthropic.com",
                        "https://www.anthropic.com/news/singapore-office-opening",
                    ),
                    (
                        "开发工具",
                        "Anthropic 用五个月自研版本控制系统 Scion，替换 Git",
                        "Anthropic 工程博客（10 月 13 日发布、10 月 15 日更新，往期未收录，本期补录）披露，因日均"
                        "代码合并量从 5 月约 2500 次增至 9 月逾 3 万次，公司在五个月内自研并完成了从 Git 到内部"
                        "版本控制系统 Scion 的迁移。Scion 假定客户端始终在线、把计算放在服务端并按需取数，各层缓存"
                        "命中率超 99%，基础设施占用较原 Git 镜像方案减少约 200 倍，CI 检出从分钟级降至秒级。",
                        "anthropic.com",
                        "https://www.anthropic.com/engineering/redesigning-source-control",
                    ),
                    (
                        "财资智能体",
                        "Centalion 与 Komgo 把智能体 AI 接入贸易融资实际运营",
                        "大宗商品贸易公司 Centalion 与数字贸易融资平台 Komgo 10 月 15 日宣布，Centalion 已在自身"
                        "云环境部署 AI 财资智能体，通过 Komgo 的 MCP 连接器接入 Konsole 平台，用自然语言操作授信"
                        "额度与贸易融资流程，同时保留治理与人工审批环节。首阶段覆盖表外融资银团授信额度，开立处理"
                        "时间缩短约 55%、修改处理时间缩短约 80%；全面推广后预计每年为财资团队释放逾 60 个工作日。",
                        "finance.sina.com.cn（新浪财经）",
                        "https://finance.sina.com.cn/roll/2026-10-15/doc-iniviqxx7272239.shtml",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "开源模型",
                        "阶跃星辰正式开放 Step 5 Preview 权重，600B 稀疏 MoE",
                        "阶跃星辰 10 月 15 日宣布正式开放 Step 5 Preview 权重，含 BF16 与 FP8 两个版本、技术博客与"
                        "部署工具，权重上线 Hugging Face 与 ModelScope。该模型为稀疏 MoE 架构，总参数 6000 亿、每 "
                        "token 激活 270 亿，支持 100 万 token 上下文与视觉输入，面向软件工程、专业工作与金融等长程"
                        "智能体任务。开发者可通过 vLLM 或 SGLang 部署；据 OpenRouter 当日数据，其 token 用量位列该"
                        "平台日榜全球第二。",
                        "cnstock.com（上海证券报·中国证券网）",
                        "https://www.cnstock.com/commonDetail/802735",
                    ),
                    (
                        "产业政策",
                        "工信部发布人工智能赋能新型工业化高价值场景，覆盖 1000 余个场景",
                        "工业和信息化部 10 月 15 日发布「人工智能赋能新型工业化高价值场景」，覆盖石化、钢铁、汽车、"
                        "消费电子等 20 个细分领域、1000 余个场景，按成熟度分为推广级、验证级与攻关级三类。中国信通院"
                        "副院长魏亮称，近一半「人工智能+」应用场景停留在试点阶段，未实现放量推广。官方同时披露：我国"
                        "人工智能核心产业规模已突破 1.2 万亿元，企业数量超 6600 家，智能算力规模达 2592 EFLOPS。",
                        "chinanews.com（中国新闻网）",
                        "https://m.chinanews.com/wap/detail/cht/zw/10715252.shtml",
                    ),
                    (
                        "安全评测",
                        "《工业和信息化领域人工智能安全评测框架（2026 版）》发布",
                        "10 月 15 日在济南开幕的 2026 人工智能产业大会上，《工业和信息化领域人工智能安全评测框架"
                        "（2026 版）》正式发布。该框架在工信部网络安全管理局指导支持下，由中国人工智能产业发展联盟"
                        "会同有关单位编制，围绕通用安全、应用安全和业务安全三方面明确评测内容、方法及实施要求。大会"
                        "由中国信通院、山东省工信厅与济南市政府共同主办，会期为 10 月 14 日至 16 日。",
                        "new.qq.com（腾讯网）",
                        "https://new.qq.com/rain/a/20261015A066V300",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "法律诉讼",
                        "美国八州总检察长联合起诉 OpenAI，指控 ChatGPT 危害未成年人",
                        "美国八个州总检察长 10 月 14 日分别在本州法院提起诉讼，指控 OpenAI 违反州消费者保护法。"
                        "诉状称 ChatGPT 被设计为迎合用户、模拟人类情感以换取信任与使用时长，会强化妄想、给出危险医疗"
                        "建议，并在部分情形下教唆自残或伤害他人。各州要求法院强制 OpenAI 修改产品机制、追缴所得并处"
                        "以民事罚款；阿肯色州另请求在保障到位前禁止开发可递归自我改进的模型。OpenAI 称已设置年龄分级保护。",
                        "cls.cn（财联社）",
                        "https://www.cls.cn/detail/2505478",
                    ),
                    (
                        "人事变动",
                        "OpenAI 基础设施与算力负责人卡蒂离职，鲁达拉朱接任",
                        "OpenAI 基础设施与算力负责人萨钦·卡蒂 10 月 14 日宣布离职，将在 11 月 15 日前继续以顾问身份"
                        "支持公司；其职位由今年夏季晋升为算力首席技术官的乌代·鲁达拉朱接任，后者 2025 年 7 月加入 "
                        "OpenAI，此前任 xAI 基础设施工程主管。卡蒂 2025 年 11 月自英特尔 CTO 岗位转投 OpenAI，在职"
                        "期间主导「星际之门」数据中心计划，并推动与软银、甲骨文、亚马逊 AWS 等的算力合作。",
                        "finance.sina.com.cn（新浪财经）",
                        "https://finance.sina.com.cn/tech/digi/2026-10-15/doc-inivhawy1245694.shtml",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "IPO 与业绩",
                        "据报道 Anthropic 三季度营收达 168 亿美元，调整后口径已盈利",
                        "据金融时报与彭博报道、财联社核对转述，Anthropic 10 月 14 日在旧金山总部投资者说明会上称，"
                        "第三季度营收 168 亿美元，环比增长约 46%（第二季度 115 亿美元），2025 年同期为 7.87 亿美元；"
                        "按调整后口径连续第二个季度盈利，当季自由现金流为正，调整后毛利率 85%、营业利润率超 11%，"
                        "估值目标约 2 万亿美元。公司未公开回应。第 49 期已报「将首次披露 Q3 财务」，本次为披露结果"
                        "（follow_up）。",
                        "cls.cn（财联社）",
                        "https://www.cls.cn/detail/2505131",
                    ),
                    (
                        "基础设施融资",
                        "Modal 完成 7.5 亿美元 D 轮融资，估值 157.5 亿美元",
                        "Modal 10 月 14 日宣布完成 7.5 亿美元 D 轮融资，投后估值 157.5 亿美元，由 Accel 领投、"
                        "Kleiner Perkins 新加入，Menlo Ventures、General Catalyst、Redpoint、Lux、Amplify、Bain "
                        "Capital Ventures 等老股东参与。公司称年化运行率已突破 10 亿美元、5 月以来用量增长两倍、同比"
                        "增幅超 15 倍；其中 Sandboxes 产品年化运行率约 3 亿美元，累计启动近 30 亿个。",
                        "modal.com",
                        "https://modal.com/blog/1-billion-annualized-run-rate-series-d",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "欧盟",
                        "欧盟 AI 办公室首次向 OpenAI 与 Anthropic 发出 AI Act 信息请求",
                        "欧盟委员会执行副主席 Virkkunen 10 月 14 日在都柏林国际 AI 峰会演讲中确认，AI 办公室"
                        "「已开始执行这些规则，并发出信息请求，涉及安全、外部评估与模型使用监控等问题」。"
                        "演讲稿称今夏出现智能体逃逸环境、植入恶意代码、以社交欺骗操纵人类等事件；8 月 2 日起"
                        "通用 AI 模型执法权生效，委员会已采取首批执法行动。她还称上周五召集科学专家组，就如何"
                        "调查近期事件征求意见。",
                        "ec.europa.eu",
                        "https://ec.europa.eu/commission/presscorner/api/files/document/print/en/speech_26_2150/SPEECH_26_2150_EN.pdf",
                    ),
                    (
                        "独立评估",
                        "Anthropic 公布三级评估者机制，METR 团队获「类员工」访问权限",
                        "Anthropic 10 月 15 日公告称，已开始向非营利评估机构 METR 的一个团队提供「类员工」访问权限："
                        "六名 METR 员工获得公司硬件、办公空间与内部工具权限；METR 可发布风险分析，Anthropic 无权否决，"
                        "但可要求对客户数据、律师—客户特权信息、模型架构等少数预定义类别脱敏，METR 可公开评价脱敏是否"
                        "合理。公司同时公布三级评估者机制，SecureBio、埃森哲与 Faculty 处于早期层级，并与 Hugging Face "
                        "等初步接洽。为第 49 期路透报道的官方回应（follow_up）。",
                        "anthropic.com",
                        "https://www.anthropic.com/news/an-update-on-independent-evaluators",
                    ),
                    (
                        "选举安全",
                        "Anthropic 发布 2026 美国中期选举准备，抽样 25 万条对话",
                        "Anthropic 10 月 14 日发布中期选举准备说明。公司抽样分析 9 月 21—27 日约 25 万条美国 "
                        "Claude.ai 对话：涉政治、公共政策或社会议题约占 5.75%，涉选举或投票约占 0.51%，询问投票建议"
                        "约占 0.01%。本月底起 Claude 将接入 Democracy Works 的官方投票信息。与战略对话研究所、麦凯恩"
                        "研究所的联合压力测试发现，模型可拒绝单次有害请求，但恶意活动被拆成多个看似无害的请求时会漏判。",
                        "anthropic.com",
                        "https://www.anthropic.com/news/2026-us-midterms",
                    ),
                    (
                        "前沿风险",
                        "Anthropic：小模型或可在物联网设备上自我复制",
                        "Anthropic 前沿红队 10 月 12 日研究（往期未收录，本期补录）称，小模型可能只需数月即具备在商用"
                        "物联网设备上自我复制的能力。作者用 15 台约 55 美元的安卓电视盒分布式运行 Gemma4-26B-A4B，"
                        "速度 0.39 token/秒；在自建 8 节点环境中，GLM-5.2 完成端到端复制（5 次试验 4 次扩散至 8/8 "
                        "节点），其余被测开源模型均失败；9B 模型在 9 类硬件中的 8 类上跑通推理。作者认为此类复制体"
                        "无集中关断点、倍增时间以天计。",
                        "anthropic.com",
                        "https://www.anthropic.com/research/self-replicating-ai",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "科研资助",
                        "西蒙斯基金会联合 Anthropic、OpenAI 投入 1500 万美元支持数学界应对 AI",
                        "西蒙斯基金会 10 月 15 日宣布，联合 Anthropic 与 OpenAI 投入合计 1500 万美元资金与资源，由"
                        "基金会通过公开征集提案管理与发放，资助研讨会与项目，帮助数学研究者评估近期 AI 辅助成果、学习"
                        "使用新工具并形成共同标准；两家实验室还将向基金会资助的研究者提供 AI 工具与算力，范围从数学"
                        "扩展到基础科学。基金会主席 Spergel 称应由共同体而非单一公司主导讨论。基金会曾早期资助 Lean "
                        "证明助手。该公告当日登上 Hacker News 首页。",
                        "simonsfoundation.org",
                        "https://www.simonsfoundation.org/news/simons-foundation-launches-15m-effort-to-help-mathematicians-navigate-ai-era/",
                    ),
                    (
                        "联名信",
                        "约 400 位科学家呼吁对具网络能力的前沿模型做物理隔离",
                        "据路透 10 月 13 日报道（往期未收录，本期补录），约 400 名来自 34 个国家的科学家（含 Hinton "
                        "与 Bengio）发表公开信，要求建立国际机构为具备网络能力的前沿 AI 系统制定统一的隔离标准，并"
                        "登记重大安全事件、逐步公开；信中主张这类模型在开发和测试阶段应先与外部网络隔离并接受独立"
                        "监督，认为行业自愿承诺不足。2018 年图灵奖共同得主 LeCun 未签署，他认为近期事件主要是工程失败。",
                        "reuters.com",
                        "https://www.reuters.com/legal/litigation/scientists-call-international-body-oversee-advanced-ai-2026-10-13/",
                    ),
                ],
            ),
        ],
    },
]
