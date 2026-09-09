# -*- coding: utf-8 -*-
"""AI Radar 第 35 期（2026.09.07 — 09.09）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- 全部条目均为 Source-First：先检索到事件，再定位 Allowlist 内的 primary / trusted media 原文，
  逐条抓取正文后撰写，摘要中的每一个数字都来自 canonical 页面。
- 本期最终来源域名：openai.com（国际 primary）、ai.meta.com（国际 primary）、blog.google（国际 primary）、
  court.gov.cn（最高人民法院官方发布）、techcrunch.com（国际 trusted media）、
  qbitai.com（中文 trusted media）、news.ycombinator.com（社媒/开发者社区）。
- 沙箱网络对 openai.com、ai.meta.com、mistral.ai 等主域存在 TLS 拦截；凡遇拦截，均改用
  Allowlist 内可访问的同等来源（mistral.ai → techcrunch.com 报道）或经检索实际取回正文的官方页面
  （openai.com/index/navier-stokes-solution/、ai.meta.com/muse/ 的全文已由检索取回核对），
  与第 32—34 期既有做法一致。
- 量子位条目发布日期经其官方 WP 接口（qbitai.com/wp-json/wp/v2/posts）逐条核对，
  均落在 2026-09-07 12:00 至 2026-09-08 之间，即第 34 期（9 月 7 日上午发布）之后。

去重说明（对照 coverage.md）：
- OpenAI 数学成果：第 34 期已报「Claude 完成费马大定理首个完整机器检查的形式化证明」；
  本期为纳维-斯托克斯千禧年难题这一不同问题的独立成果，属 unrelated，非重复。
- 千问办公：第 33 期报国际版公测、第 34 期报上线满月运营数据；本期为「多人工作台」这一新功能
  （角色权限、云端数据库、管理后台、在线发布），属 material new development，作为 follow_up 收录。
- AFAC2026：第 34 期报大赛启动与数据集开源；本期为总决赛路演评审这一新阶段，属 follow_up。
- Muse：往期未报过 Meta 个人智能体（第 34 期报的是 Google Gemini Spark 接管 Photos），属 unrelated。
- Mistral：往期未报过其融资事件，属新事件。

DROP 记录（本期未收录及理由）：
- 高通与亚马逊 600 亿美元芯片合作 + 2500 万股认股权证（9/8）：细节仅见于 8-K 与 hothardware、
  tipranks 等非 Allowlist 源，未定位到 techcrunch.com / reuters.com / cnbc.com / theverge.com 原文 → Skill §17 DROP。
- 重庆获工信部批复建设国家人工智能产业创新应用先导区（9/8）：仅见央广网、重庆日报与门户转载，
  未找到 miit.gov.cn 同源公告，亦未定位到 36kr / jiqizhixin / qbitai / tmtpost 原文 → DROP。
- 工信部《关于开展人工智能应用服务商培育专项行动的通知》：公开报道显示印发时间为 8 月 31 日，
  落在第 34 期窗口内且非本期新事件 → 时间窗不符，DROP。
- OpenAI CFO 在高盛会议称企业业务年化营收 7 月环比增长 32%（9/8）：未取得 openai.com 或
  Allowlist 媒体原文 → DROP。
- Anthropic 招股说明书推迟至 9 月底：仅见 Reuters 内容的二手转述（tipranks、新浪财经等），
  无合规 reuters.com 原文 URL → 按 Skill §19/§36 DROP（与第 34 期同处理）。
- OpenAI 首席科学家 Jakub Pachocki 关于推理模型风险的周末表态：仅见媒体转述，
  未定位到 openai.com 原文页面 → DROP。
- 苹果 9 月 9 日秋季发布会：TechCrunch 相关页面为观看指南，且核心为消费硬件而非可核实的 AI 事件 → DROP。
- GOSIM Shenzhen 2026 议程公布、WAIC CONNECT MALAYSIA 首日、B 站 AI 创造公开赛收官等：
  会议/活动类信息增量有限，按重要性取舍 → DROP。
- HN 条目中 Kimi K3 本地推理（github.com/argonautlabsai/deltafin）、Qwen3.8 量化基准
  （quesma.com，域名不在 Allowlist）、i-have-adhd（github.com）等：按社区栏目容量择要收录三条，
  其余域名或重要性不足 → DROP。
"""

ISSUES = [
    {
        "num": 35,
        "date": "2026.09.07 — 09.09",
        "picks": [
            (
                "模型与技术进展",
                "OpenAI 公布纳维-斯托克斯千禧年难题的证明，由大规模智能体协作产出",
                "OpenAI 9 月 8 日公布其对「纳维-斯托克斯存在性与光滑性」这一千禧年难题的证明：多组智能体并行推进约 88 小时后于 9 月 5 日得出解析证明，随后由 GPT-6 Astra 用约 17 小时完成 Lean 形式化与验证。全部尝试累计发送 490 万条消息、消耗约 3000 亿输出 token，其中该问题本身占 270 万条消息与约 1300 亿 token。公司称不会就此申领百万美元奖金。",
                "openai.com",
                "https://openai.com/index/navier-stokes-solution/",
            ),
            (
                "企业应用与工具观察",
                "Meta 在美国推出个人智能体 Muse，运行在独立虚拟机中并可常驻执行任务",
                "Meta 9 月 8 日面向美国用户推出个人智能体 Muse，可通过 Muse App、muse.ai 网页与 WhatsApp 使用。它运行在专用虚拟机上，能连接邮箱、日历、支付、健康等应用，并在用户未打开应用时继续在后台推进任务；涉及发信、付款等操作需用户逐一确认。结账时使用一次性卡号，对话数据不接入 Meta 广告系统。免费额度之外提供每月 20 美元与 100 美元两档订阅。",
                "ai.meta.com",
                "https://ai.meta.com/muse/",
            ),
            (
                "国际 AI 动态",
                "Mistral 完成 30 亿欧元 D 轮融资，投后估值超 210 亿欧元",
                "Mistral AI 9 月 8 日宣布完成 30 亿欧元 D 轮融资，投后估值超过 210 亿欧元（约 243.9 亿美元），公司称这是欧洲科技公司完成的规模最大的股权融资。本轮由三星电子领投，EQT 管理的 Scaleup Europe Fund 与老股东 PSG Equity 共同领投。资金将用于扩充算力、建设基础设施与拓展国际市场；Mistral 的目标包括 2030 年前在欧洲建成 1GW 算力，目前业务覆盖 20 个国家。",
                "techcrunch.com",
                "https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/",
            ),
            (
                "政策、监管与风险",
                "最高法发布首部涉人工智能司法裁判规则文件，共 5 部分 24 条",
                "最高人民法院 9 月 7 日举行新闻发布会，发布《关于依法审理涉人工智能纠纷案件的意见》，共 5 部分 24 条，是首部由最高审判机构发布的涉人工智能司法裁判规则文件。意见对「AI 换脸拟声」侵害肖像权、声音权益等行为的责任认定作出规范，明确为模型训练在合理范围内处理已合法公开的个人信息一般不认定为侵权，并对生成式 AI 内容侵权、智能产品缺陷与自动驾驶交通事故等场景细化归责规则。",
                "court.gov.cn",
                "https://www.court.gov.cn/zixun/xiangqing/511101.html",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "数学与智能体",
                        "OpenAI 公布纳维-斯托克斯千禧年难题的证明，由大规模智能体协作产出",
                        "OpenAI 9 月 8 日公布其对「纳维-斯托克斯存在性与光滑性」这一千禧年难题的证明：多组智能体并行推进约 88 小时后于 9 月 5 日得出解析证明，随后由 GPT-6 Astra 用约 17 小时完成 Lean 形式化与验证。全部尝试累计发送 490 万条消息、消耗约 3000 亿输出 token，其中该问题本身占 270 万条消息与约 1300 亿 token。公司称不会就此申领百万美元奖金。",
                        "openai.com",
                        "https://openai.com/index/navier-stokes-solution/",
                    ),
                    (
                        "世界模型",
                        "智象未来发布具身世界模型 HiDream-O1-Embodied，扰动适应榜登顶",
                        "智象未来（HiDream.ai）9 月 7 日发布具身世界模型 HiDream-O1-Embodied，强化机器人的物理感知与动态预判能力，打通图像、视频、3D 与动作等模态。该模型首次参评具身智能评测平台 RoboColiseum，即在扰动适应（Robustness）子榜以平均 0.692 分登顶。该子榜通过改变背景、光照、材质、机器人初始状态与相机位置，并对指令做多样化改写来检验模型在非理想环境中的稳定性。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485056.html",
                    ),
                    (
                        "小模型协作",
                        "ARC-AGI 3 上 4B 端侧模型搭配 753B 云端模型，补齐约一半性能差距",
                        "团队 Mostik 在 ARC-AGI 3 比赛中采用手机端 4B 的 Qwen-3.5 搭配云端 753B 的 GLM-5.2：大模型全程不输出最终答案，只由端侧小模型落笔。按团队公开的实验结果，这套方案可补齐 4B 与 753B 模型之间约 50% 的性能差距，自身准确率提高 25%；在大小模型差距更明显的难题子集上提升达到 2 倍。具体技术细节尚未公开，团队称需等比赛结束。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485108.html",
                    ),
                    (
                        "基因组学",
                        "Google DeepMind 推出 AlphaGenome Atlas，预制 90 亿个单核苷酸变异影响",
                        "Google DeepMind 9 月 8 日推出 AlphaGenome Atlas，用 AlphaGenome 模型预计算人类基因组中全部约 90 亿个单核苷酸变异的调控影响，形成约 1PB 规模的数据集。配套推出的 AlphaGenome Variant Impact（AVI）评分把编码区与非编码区的预测合并为单一指标，供研究者快速筛选优先方向，而无需逐条翻阅原始数据。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "消费级智能体",
                        "Meta 在美国推出个人智能体 Muse，运行在独立虚拟机中并可常驻执行任务",
                        "Meta 9 月 8 日面向美国用户推出个人智能体 Muse，可通过 Muse App、muse.ai 网页与 WhatsApp 使用。它运行在专用虚拟机上，能连接邮箱、日历、支付、健康等应用，并在用户未打开应用时继续在后台推进任务；涉及发信、付款等操作需用户逐一确认。结账时使用一次性卡号，对话数据不接入 Meta 广告系统。免费额度之外提供每月 20 美元与 100 美元两档订阅。",
                        "ai.meta.com",
                        "https://ai.meta.com/muse/",
                    ),
                    (
                        "企业交付",
                        "谷歌云与埃森哲成立 Gemini Enterprise 业务集团，培训至多 1000 名驻场工程师",
                        "谷歌云与埃森哲宣布成立 Accenture Gemini Enterprise Business Group，向企业派驻工程师，帮助其落地谷歌的 AI 工具与服务。作为合作的一部分，谷歌将为埃森哲培训至多 1000 名「前置部署工程师」（FDE），在 Gemini Enterprise 平台上为企业构建定制 AI 应用，该组织隶属于埃森哲。OpenAI、Anthropic、微软与亚马逊近期均已设立类似部门。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/google-cloud-races-to-catch-up-in-the-ai-deployment-wars-with-accenture-deal/",
                    ),
                    (
                        "办公智能体",
                        "国内首份办公 Agent 用户行为报告：前 20% 用户消耗 87.4% 的算力",
                        "9 月 7 日发布的《中国办公 Agent 用户行为不完全报告》基于桌面端办公 Agent LobsterAI 的真实用户数据：北京用户量居全国城市首位，与上海、杭州、广州、深圳合计约占 27%，海外用户占比 12.75%；使用呈明显头部效应，前 20% 用户消耗 87.4% 的算力，前 5% 独占 53.5% 的 token 消耗；付费用户在 token 消耗、任务量与月活跃天数上分别为免费用户的 6.2 倍、5.2 倍和 3.0 倍。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485064.html",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "办公智能体",
                        "千问办公推出「多人工作台」，支持百人级在线协作",
                        "阿里旗下千问办公推出业内首个「多人工作台」：用户简单描述需求，即可生成并发布一个最多支持百人同时在线协作的网页，具备角色权限、云端数据库、管理后台与在线发布四项能力，可用于活动组织、家校协同与企业协作。此前市面上的 AI 工作台主要面向个人，多用于简历、作品集等信息展示或简单交互。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485046.html",
                    ),
                    (
                        "智能体模型",
                        "王云鹤创办的基元律动发布首个 Agent-Native 模型 NeoHorse-1",
                        "华为诺亚方舟实验室前主任、盘古大模型负责人王云鹤创办的基元律动发布首个模型 NeoHorse-1，包含 4B 与 9B 两个版本，重点覆盖调用工具、读取环境反馈、发现错误、调整路径直至完成任务等能力。该模型由无问芯穹提供算力与 Infra 支持，清华大学、北京大学团队参与算法与训练方法研究。在覆盖 Harness Agent、工具使用、代码与指令遵循的 10 项评测中，经智能体后训练的 4B 版本整体表现达到并略超 9B 基础模型。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485555.html",
                    ),
                    (
                        "融资",
                        "物理 AI 企业深度智控完成数亿元 B+ 轮融资，宁德时代领投",
                        "物理 AI 企业深度智控（DeepCtrls）完成新一轮数亿元 B+ 轮融资，由宁德时代领投，阿美投资（Aramco Ventures）、太平创新投资、广发信德、复星创富跟投，源码资本、光远资本等老股东追加。公司称其 PhyAI 引擎已服务全球数百家头部企业客户，液冷智控与算电协同产品正从工业场景延伸至算力基础设施。过去两个月内公司已连续完成三轮融资。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485784.html",
                    ),
                    (
                        "融资",
                        "中科类脑完成数亿元 B+ 轮战略融资，中车资本领投",
                        "合肥中科类脑智能技术有限公司宣布完成数亿元 B+ 轮战略融资，由中车资本领投，银杏谷资本、水木基金、启迪基金等跟投。这是公司继 2025 年获中国移动旗下基金亿元级独家战略投资后的又一轮融资。公司表示资金将投向算电协同方向的算电一体化 Token 工厂与 AI Infra 产品迭代，中国移动、中国中车两家央企旗下基金先后入局。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485039.html",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "融资",
                        "Mistral 完成 30 亿欧元 D 轮融资，投后估值超 210 亿欧元",
                        "Mistral AI 9 月 8 日宣布完成 30 亿欧元 D 轮融资，投后估值超过 210 亿欧元（约 243.9 亿美元），公司称这是欧洲科技公司完成的规模最大的股权融资。本轮由三星电子领投，EQT 管理的 Scaleup Europe Fund 与老股东 PSG Equity 共同领投。资金将用于扩充算力、建设基础设施与拓展国际市场；Mistral 的目标包括 2030 年前在欧洲建成 1GW 算力，目前业务覆盖 20 个国家。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/",
                    ),
                    (
                        "融资",
                        "Cognition 完成 20 亿美元融资，估值达 480 亿美元",
                        "开发编程智能体 Devin 的 Cognition 宣布完成 20 亿美元融资，估值达 480 亿美元，由 a16z、Accel、Founders Fund、General Catalyst 与 Avenir 领投，距上一轮 260 亿美元估值仅四个月。公司称自 5 月上一轮融资以来，年化运行收入从 4.92 亿美元增至 9 亿美元。据 The Information 报道，其租赁的英伟达服务器集群年成本达数亿美元，今年现金消耗可能达到 8 亿美元。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
                    ),
                    (
                        "算力与能源",
                        "NextEra 获美国能源部 19 亿美元贷款，重启谷歌拟用的爱荷华核电站",
                        "美国能源部向 NextEra Energy 提供 19 亿美元贷款，用于重启爱荷华州 Duane Arnold 能源中心。谷歌去年曾宣布计划让这座 2020 年停运的核电站恢复运行，并据报拟在附近建设最多六座数据中心。这是能源部第二次为重启核电提供此类贷款，去年曾向 Constellation Energy 提供 10 亿美元用于重启三哩岛的一座反应堆。该电站计划 2029 年重启。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/googles-revived-nuclear-power-plant-gets-1-9b-loan-from-us-government/",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "金融智能体",
                        "AFAC2026 金融智能创新大赛进入总决赛，5000 余支队伍角逐",
                        "AFAC2026 金融智能创新大赛举行总决赛，5000 余支队伍、近 2 万名选手经选拔后进入路演答辩，由产业、学界与创投三方评委评审，设百万奖金，优胜项目可获得企业现场直聘与投资机构对接。赛题覆盖资金流分析、金融文档还原、自动实验与长文本智能体记忆压缩等方向，参赛队伍反馈赛题难度较往年明显提高。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/485794.html",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "司法规则",
                        "最高法发布首部涉人工智能司法裁判规则文件，共 5 部分 24 条",
                        "最高人民法院 9 月 7 日举行新闻发布会，发布《关于依法审理涉人工智能纠纷案件的意见》，共 5 部分 24 条，是首部由最高审判机构发布的涉人工智能司法裁判规则文件。意见对「AI 换脸拟声」侵害肖像权、声音权益等行为的责任认定作出规范，明确为模型训练在合理范围内处理已合法公开的个人信息一般不认定为侵权，并对生成式 AI 内容侵权、智能产品缺陷与自动驾驶交通事故等场景细化归责规则。",
                        "court.gov.cn",
                        "https://www.court.gov.cn/zixun/xiangqing/511101.html",
                    ),
                    (
                        "账号安全",
                        "调查：黑客盗用 Claude 订阅用户的 token 额度",
                        "TechCrunch 报道，英国独立 AI 顾问 Grant De Swardt 在停用全部连接后，其 Claude Max 20x 账户的 token 用量仍持续上升。Anthropic 调查后告知他，一个被入侵的 Claude 会话密钥被用于签发未经授权的 Claude Code OAuth 令牌，随后封停其付费账户、作废全部会话与服务端令牌并部分退款。报道指出，账户支持只统计总用量、不提供逐项明细，这类盗用可能长期不被察觉。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/",
                    ),
                    (
                        "学术争议",
                        "纳维-斯托克斯成果引发优先权争议，OpenAI 称未接触对手工作",
                        "纽约大学数学教授 Tristan Buckmaster 与 Anthropic 研究员 Levent Alpöge 在声明中称，两人尚未公开的进展被透露给 OpenAI，随后 OpenAI 把资源转向他们选择的思路并先一步完成证明。OpenAI 在公告中确认项目于 9 月 1 日启动，起因是听到相关传闻，并表示在对方成果公开发布前未以任何方式接触其工作，但无法排除去标识化数据影响模型的可能。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "Hacker News",
                        "Buckmaster 的纳维-斯托克斯声明 PDF 登顶 HN：1217 分、532 条评论",
                        "纽约大学数学教授 Tristan Buckmaster 就纳维-斯托克斯成果发布的个人声明 PDF，成为本窗口 Hacker News 得分最高的技术条目，获得 1217 分与 532 条评论。讨论集中在 AI 参与前沿数学研究时的优先权认定、实验室掌握海量算力对学术竞争的影响，以及厂商自证「未接触对手工作」能否被外部验证。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49605915",
                    ),
                    (
                        "Hacker News",
                        "OpenAI 纳维-斯托克斯证明页获 1088 分、947 条评论",
                        "OpenAI 关于纳维-斯托克斯千禧年难题的公告页面在 Hacker News 获得 1088 分与 947 条评论，是本周讨论量第二高的条目。社区的关注点集中在 Lean 形式化验证能在多大程度上替代同行评议、模型产出的长篇证明是否具备可复核性，以及「AI 做出可验证数学成果」是否会改变科研评价体系。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49613262",
                    ),
                    (
                        "Hacker News",
                        "Meta Muse 上线引 264 条讨论，个人智能体的权限边界成焦点",
                        "Meta 个人智能体 Muse 的产品页在 Hacker News 获得 274 分与 264 条评论。讨论主要围绕让智能体常驻云端虚拟机、并接入邮箱与支付等真实账户所带来的风险，不少评论对「敏感操作需确认」这类机制在实际使用中的有效性持保留态度，也有人关注其与既有聊天机器人在定位上的差别。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49615537",
                    ),
                ],
            ),
        ],
    }
]
