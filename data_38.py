# -*- coding: utf-8 -*-
"""AI Radar 第 38 期（2026.09.14 — 09.16）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- 全部条目均为 Source-First：先检索到事件线索，再定位 Allowlist 内的 primary / trusted media 原文，
  抓取页面正文（或经浏览器读取全文）后撰写；摘要中的每个数字都来自 canonical 页面本身。
- 本期最终来源域名：cac.gov.cn（政策官方源）、blog.google（国际 primary source）、
  claude.com（Anthropic 官方产品博客，primary source）、techcrunch.com（国际 trusted media）、
  36kr.com（中文 trusted media）、qbitai.com（中文 trusted media）、
  tmtpost.com（中文 trusted media）、news.ycombinator.com（社媒/开发者社区）。
- blog.google 三篇均 curl 取回并核对 datePublished：Gemini 3.8 Live 两文为 2026-09-15T17:00:00Z。
- techcrunch.com 三篇均 curl 取回并核对 datePublished 与正文段落。
- cac.gov.cn 页面 curl 取回核对标题与正文；框架 3.0 的章节结构（五原则、三类风险、附件 1—3）
  取自网安标委同步公布的框架 PDF 目录。
- claude.com 官方博客经浏览器全文读取（Anthropic 官网 anthropic.com 在沙箱内不可达），
  canonical 指向官方公告本身，不使用转载或聚合页。
- 36kr.com 文章页为 JS 渲染，curl 仅返回骨架，改用浏览器取出全文后核对事实与发布时间。
- Hacker News 三条经 hn.algolia.com 官方 API 按 created_at 过滤本期窗口，分数与评论数取自 API，
  canonical_url 统一指向 news.ycombinator.com/item?id=...。

去重说明（对照 coverage.md）：
- 《人工智能安全治理框架 3.0》：往期未报过该版本框架（第 37 期报的是工信部《"人工智能+软件"专项行动实施方案》），
  本期为 2026 年国家网络安全宣传周开幕式上的新发布，属新事件。
- Gemini 3.8 Live 与 3.8 Live Extended Thinking：往期报的是 8 月 Gemini Omni 1.1 Flash 与 9 月 WeatherNext 3，
  本期为全新语音模型代际（计划经济型 + 后台推理型双版本），属新事件。
- Claude for Financial Advisors：往期未报过该产品，本期为新品类（连接器 + 技能插件）首发，属新事件。
- OpenAI 收购 Glass Imaging：往期报的是 OpenAI 收购 io（2025 年 65 亿美元），本期为新的并购标的与交易，属新事件。
- 豆包手机助手消费者版：往期未报过该版本（第 30 期前后涉及的是技术预览版与排查风波），
  本期为消费者版正式发布 + SAEP 协议公示，属 material new development。
- DeepSeek 首位 CFO：第 36/37 期均因缺 Allowlist 原文而 DROP 了「DeepSeek 委托中信证券筹备科创板 IPO」，
  本期 36 氪 + 量子位双源到位、且事件是「首位 CFO 人选落定」这一新事实，属新事件。
- 智谱：第 37 期报的是 9/13 晚融资公告本身；本期为后续硬进展——资金投向明细（约六成 235 亿港元）、
  完成收购中科加禾、上半年收入结构与单位成本数据首次对外，属 follow_up。
- OpenAI/Anthropic/Google 安全协调与 FRONTIER Act：第 37 期报的是 Amodei 单独发文与单边承诺，
  本期为三家公司实际接触已持续数周 + OpenAI 对联邦立法的具体立场，属 material new development。
- HN「RubyGems 缓存漏洞」：第 37 期报的背景事件是 OpenAI–Hugging Face 智能体集群越界，
  RubyGems 是另一起不同目标的自披露事件，本期为维护者视角的技术复盘，属新事件。

DROP 记录（本期未收录及理由）：
- Anthropic 选定纳斯达克 IPO、拟募资至多 1000 亿美元、英伟达洽谈 100 亿美元基石投资（9/13—9/14 报道）：
  仅有 FT/Reuters/Business Insider 的二手转述，未取回 reuters.com / ft.com 原文页面可核对的 URL → Skill §19/§36。
- Anthropic 连续第二个季度调整后营业利润为正、毛利率超 80%（FT 9/14）：同上，无 Allowlist 原文 → §19。
- Factory AI 2 亿美元融资、估值 50 亿美元（Reuters，9/15）：reuters.com 在沙箱内不可达，
  仅第三手聚合站转述，URL 无法逐字核实 → §36 DROP。
- OpenAI 新一轮融资估值约 1.2 万亿美元、年化营收破 400 亿美元（9/15 报道）：出处为每日经济新闻转述，
  未定位到 Reuters / CNBC / The Information 可核对原文 → §18/§19 DROP。
- 马斯克在 All-In 峰会提议巨头发布前交叉测试（9/15）：仅见早报与日报类转述，无 Allowlist 原文 → §17。
- OpenAI 已开放 GPT-Live-1 语音模型 API（9/14）：首报为 X 帖子，openai.com 页面未能取回 → §17。
- DeepSeek-V4.1-Flash 进入 Agent Arena 开源第 3、每任务约 0.07 美元（9/14）：
  榜单数据来自 X 账号 @arena 与 AI 日报类转述，属 benchmark claim 且无第二家 Allowlist 源 → §18 DROP。
- 三星 2.31 亿美元参投 Euclyd（CNBC，9/15）：未取回可逐字核对的 cnbc.com 原文 URL → §17。
- Gemini app for Windows（blog.google）：datePublished 为 2026-09-10，超出本期窗口 → 时间窗不符。
- 讯兔科技超 3 亿元 B 轮（qbitai）：页面日期落在第 37 期窗口内且未构成新进展 → 时间窗不符。
- 苹果 Siri 可替换为 Claude / ChatGPT 的私有 API（9/14）：原始发现者为开发者社交账号，转述全为搬运转载 → §17。
- HN 条目「Show HN: 会听鸟叫的电子墨水相框」1283 分、「25 years of mass surveillance」793 分、
  「Introducing System One Models and Jev」722 分等：或与 AI 无关，或社区栏目容量所限择要收录三条 → 按重要性取舍。
"""

ISSUES = [
    {
        "num": 38,
        "date": "2026.09.14 — 09.16",
        "picks": [
            (
                "政策、监管与风险",
                "网安标委发布《人工智能安全治理框架 3.0》，单列智能体风险管理框架",
                "9 月 14 日 2026 年国家网络安全宣传周开幕式上，全国网安标委在中央网信办指导下发布《人工智能安全治理框架 3.0》。框架延续「风险分类、技术应对、综合治理」逻辑，更新了风险清单与应对、治理措施，并提出包容审慎等五项原则；正文含模型算法研发、应用建设部署、运行管理与访问使用四类安全指引，附件新增智能体风险管理框架与可信人工智能基本准则。",
                "cac.gov.cn",
                "https://www.cac.gov.cn/2026-09/14/c_1791137092283345.htm",
            ),
            (
                "模型与技术进展",
                "Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking，语音模型支持边说边推理",
                "Google DeepMind 9 月 15 日发布两款实时语音模型。3.8 Live 面向规模化与成本效率，支持近实时视觉理解与 97 种语言自动识别、可在对话中断句切换语言；3.8 Live Extended Thinking 在保持对话连续的同时进行后台多步推理与工具调用，官方称其会用「让我查一下」之类的语句说明进展。两模型同日进入 Gemini API、AI Studio、Search Live、Gemini App 与 Workspace 的 Docs、Gmail、Keep。",
                "blog.google",
                "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
            ),
            (
                "AI 与金融",
                "Anthropic 推出 Claude for Financial Advisors，一次接入贝莱德、嘉信、先锋等 11 家机构工具",
                "Anthropic 在 Future Proof 大会发布面向理财顾问的 Claude 插件。新增连接器覆盖 Addepar、贝莱德、嘉信理财、Envestnet、iCapital、Orion、SS&C Black Diamond、Wealthbox、Wealth.com、先锋领航与 Zocks，可读取托管账户余额、持仓、成本基准、另类投资份额及税务遗产信息。配套的八项工作内容涉及会前准备、组合再平衡审查、按 SEC 营销规则筛查对外话术与会后跟进。",
                "claude.com",
                "https://claude.com/blog/claude-for-financial-advisors",
            ),
            (
                "国际 AI 动态",
                "OpenAI 收购前苹果工程师创办的计算摄影公司 Glass Imaging，交易额超 3 亿美元",
                "据《华尔街日报》报道、TechCrunch 转述，OpenAI 收购加州洛斯阿尔托斯的 Glass Imaging，交易金额超过 3 亿美元。公司由主导 iPhone 人像模式的两名前苹果工程师 Ziv Attar、Tom Bishop 于 2019 年创办，此前累计融资约 3000 万美元、上一轮估值约 1 亿美元。其方案不做事后修图，而是用神经网络学习手机摄像系统的光学缺陷，在按下快门瞬间从原始数据重建画面。OpenAI 未回应置评。",
                "techcrunch.com",
                "https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/",
            ),
            (
                "国内 AI 动态",
                "豆包手机助手消费者版落地努比亚新机，同步推出屏幕自动化操作声明协议 SAEP",
                "随努比亚 NaviX Ultra 于 9 月 16 日开售，字节跳动豆包手机助手消费者版正式面向市场。相比去年 12 月的技术预览版，新版本强化了稳定性与日常可用性：支持语音与带指纹鉴权的 AI 实体键唤醒、基于当前屏幕画面的问答、本地相册与短信便签检索，录音能力接入飞书妙记。最受关注的图形界面智能体以 Beta 开放，并同步启动为期 30 天的 SAEP 规则公示。",
                "tmtpost.com",
                "https://www.tmtpost.com/8140215.html",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "语音模型",
                        "Gemini 3.8 Live 双版本发布：经济型保延迟，Extended Thinking 可后台推理并用 SynthID 打标",
                        "Google DeepMind 9 月 15 日发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking，官方称这是「迄今最先进的实时对话模型」。前者主打规模化与成本效率，兼顾自然对话与视觉定位；后者面向高复杂度任务，可在说话的同时完成多步规划与后台工具调用。两模型均接收文本、图像、音频与视频输入并输出文本或音频，全部音频输出嵌入 SynthID 水印，模型卡同步公布。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
                    ),
                    (
                        "具身推理",
                        "无问芯穹联合清华、上交开源具身端侧推理引擎 APXInf",
                        "无问芯穹与清华大学、上海交通大学联合开源面向具身智能的端侧推理引擎 APXInf，支持 RTX 4090、Jetson Orin、Jetson Thor 等主流计算平台，覆盖从模型开发、效果验证到机器人本体部署的完整链路，官方称其在 Pi 0.5 上取得同级别最优表现。团队认为机器人需要的是在低算力、低功耗约束下兼顾小 batch、低延迟与持续交互的推理系统，而非把云端框架简单搬到本体上。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/489460.html",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "操作系统",
                        "macOS 27 Golden Gate 上线：新 Siri 可读屏问答，Spotlight 可直接提问",
                        "苹果 9 月 14 日推送 macOS 27 Golden Gate，核心是完成重构的 Siri AI。它可在任意界面被调用，回答关于屏幕内容的问题、总结信息或改写文本；配合 Visual Intelligence，Command+Shift+6 可框选屏幕区域直接提问或做图像搜索。Spotlight 支持限定应用、文件、动作与剪贴板的上下文搜索，并可直接运行快捷指令。Safari 新增页面变化追踪与按主题自动整理标签页。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/14/macos-27-new-siri-takes-on-ai-productivity-apps/",
                    ),
                    (
                        "开发者工具",
                        "Gemini Live API 接入 Agora、LiveKit、Vercel 等实时媒体平台",
                        "随新语音模型发布，Google 同日在开发者侧更新 Gemini Live API 的说明。官方称 Gemini Live API 已与 Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel、Vision Agents 等平台打通，由它们承担实时媒体流式传输的基础设施，开发者专注于交互体验；Salesforce、Genspark、Lumeris 为企业侧首发伙伴，官方概括为看重其延迟、连贯性与工具调用能力。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "AI 终端",
                        "豆包手机助手消费者版：从「我能操作你」转向「你愿意让我调用什么」",
                        "首发机型努比亚 NaviX Ultra 于 9 月 16 日开售，搭载豆包手机助手消费者版。钛媒体对比指出，一代走的是图形界面智能体模拟点击的老路，导致主流应用集体封禁；二代改为协议路线——把指令交给应用自身执行，并推出屏幕自动化操作声明协议 SAEP，由第三方自主声明接受或拒绝 AI 助手的屏幕操作。代价是能力边界取决于应用开放意愿，目前微信仅开放语音消息与音视频通话等部分能力。",
                        "tmtpost.com",
                        "https://www.tmtpost.com/8140215.html",
                    ),
                    (
                        "人事与资本",
                        "DeepSeek 首位 CFO 落定：高瓴创投合伙人严文韬或将到岗",
                        "多家独立信源对 36 氪证实，高瓴创投合伙人严文韬即将出任 DeepSeek 首席财务官，目前已在内部启动离职流程。严文韬生于 1991 年，2013 年起先后任职腾讯投资与 H Capital，2020 年加入高瓴，主导或参与过字节跳动、智谱、MiniMax、小红书等项目。DeepSeek 自 2025 年初即挂出 CFO 招聘，此番人选落定距离媒体报道其选定中信证券筹备科创板上市约五天，公司今年 6 月完成超 500 亿元首轮外部融资。",
                        "36kr.com",
                        "https://36kr.com/p/3984129995822724",
                    ),
                    (
                        "融资后续",
                        "智谱披露 50 亿美元融资投向明细，上半年 API 收入占比升至 86.5%",
                        "智谱 9 月 13 日公告约 50 亿美元融资后，进一步披露资金安排：约六成净额（约 235 亿港元）投向下一代 GLM 与「完全自训练」体系，覆盖自动化训练数据、任务环境搭建、长程推理与国产芯片适配。公司称已落地全部采用国产芯片的 1GW 级 AI 算力数据中心，并完成对异构算力软件公司中科加禾的收购。上半年收入 9.54 亿元同比增 399.7%，开放平台与 API 业务占比升至 86.5%，单位 Token 推理成本较年初下降约 80%，经调整净亏损约 19.64 亿元。",
                        "36kr.com",
                        "https://36kr.com/p/3984088056019714",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "并购",
                        "OpenAI 超 3 亿美元买下 Glass Imaging，为硬件版图补视觉感知",
                        "《华尔街日报》首先报道、TechCrunch 跟进：创立于 2019 年、融资约 3000 万美元的 Glass Imaging 被 OpenAI 收购，估值较去年上一轮翻约三倍。公司两名创始人曾带队开发 iPhone 人像模式，其 GlassAI 学习每套手机摄像系统的光学缺陷，在按下快门时重建图像。报道同时提到 OpenAI 传闻中的多条硬件产品线——AI 手机、耳机与陪伴设备，以及 2025 年以 65 亿美元收购 Jony Ive 创办的 io。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/",
                    ),
                    (
                        "行业协调",
                        "OpenAI 称与 Anthropic、谷歌围绕 AI 安全的接触已持续数周，不需要反垄断豁免",
                        "OpenAI 全球政策主管 Chris Lehane 9 月 15 日在华盛顿对记者表示，公司与 Anthropic、谷歌 DeepMind 就 AI 安全事务的沟通已持续数周，且认为三家协调不需要政府给予反垄断豁免；Amodei 上周的长文曾提议设置窄口径豁免，Altman 也提到协调可能触及反垄断。The Information 报道称三家讨论过自行设立标准机构负责模型测试与审计，Hassabis 则在 7 月就呼吁美国建立类似监管机构。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "财富管理",
                        "Claude for Financial Advisors 上线：八项工作内容 + 十一条托管与财富科技连接器",
                        "Anthropic 在 Future Proof 大会发布 Claude for Financial Advisors。连接器让 Claude 读取顾问日常使用的托管方、资产管理与财富科技平台数据；配套八项工作内容覆盖顾问入职、另类投资简报、合规与 AI 政策、遗产税务简报、组合再平衡审查、会后记录跟进、会前准备与潜在客户受理。Anthropic 明确投资建议、客户沟通与合规判定仍由人工审核，Claude 只负责准备初稿，plugin 面向企业版并提供审计日志。",
                        "claude.com",
                        "https://claude.com/blog/claude-for-financial-advisors",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "标准与框架",
                        "《人工智能安全治理框架 3.0》发布，风险分类与治理措施同步更新",
                        "9 月 14 日国家网络安全宣传周开幕式上，全国网安标委发布《人工智能安全治理框架 3.0》。这是继 2024、2025 年 1.0 与 2.0 之后的第三次更新，由网安标委组织中国网络空间研究院、国家网信办数据与技术保障中心等机构共同编制，在国家网信办指导下完成。框架坚持强化风险意识、确保安全可控，更新了内生、应用与衍生三类安全风险的应对措施，进一步优化技术应对与综合治理安排。",
                        "cac.gov.cn",
                        "https://www.cac.gov.cn/2026-09/14/c_1791137092283345.htm",
                    ),
                    (
                        "立法",
                        "OpenAI 表态支持 FRONTIER Act，白宫方面则对「降速」持对立立场",
                        "同场活动中 Lehane 称，OpenAI 支持众议院两党提案 FRONTIER Act 的条款——要求顶级前沿实验室允许「独立验证组织」进入公司评估模型与安全实践，并愿意推动法案通过。TechCrunch 同时记录了对立一侧：总统方面认为 AI 安全担忧被夸大，反对收紧监管，其 AI 顾问 David Sacks 表示生存性风险被过度渲染，理由是放缓会让中国在竞争中占先。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "Hacker News",
                        "苹果 iOS 27 / macOS 27 发布帖引发 700 分、827 条讨论",
                        "苹果官方发布稿成为本窗口 Hacker News 讨论量最高的 AI 相关条目，社区焦点集中在新版 Siri 的实际可用边界：升级后旧机型是否被拖慢、Apple Intelligence 能否彻底关闭、新 Siri 只在支持 Apple Intelligence 的机型上提供，以及思考助手获得屏幕级访问权限之后的隐私边界。多条评论把它与第三方 AI 生产力工具的替代关系放在一起比较。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49701004",
                    ),
                    (
                        "Hacker News",
                        "Ruby on Rails 核心成员复盘 RubyGems 事件，506 分 / 413 条讨论",
                        "Ruby on Rails 核心成员 tenderlove 关于 OpenAI 抓取机器人与 RubyGems 缓存层漏洞的文章在 9 月 14 日登上 Hacker News，引发 506 分、413 条评论。讨论延展到开源基础设施在 AI 抓取压力下的承载能力、维护者在资源匮乏时的工作量，以及智能体越界访问第三方系统后的定责问题。这是继该 RubyGems 事件披露之后的第二轮社区集中讨论。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49695876",
                    ),
                    (
                        "Hacker News",
                        "Andon Labs 发布 Pion：目标为「自主运营任意公司」的智能体",
                        "Andon Labs 9 月 14 日发布智能体产品 Pion，官方定位是可自主运营一家公司，相关帖在 Hacker News 获得 481 分、585 条评论。社区讨论集中在授权边界而非能力本身：高度自主的智能体遇到错误时如何回滚、谁能签字，以及企业是否真愿意把经营决策交给模型。也有评论质疑「运行一家公司」与实际可实现范围之间的落差。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49700477",
                    ),
                ],
            ),
        ],
    },
]
