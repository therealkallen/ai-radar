# -*- coding: utf-8 -*-
"""AI Radar 第 37 期（2026.09.11 — 09.14）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- 全部条目均为 Source-First：先检索到事件，再定位 Allowlist 内的 primary / trusted media 原文，
  抓取正文后撰写；摘要中的每一个数字都来自 canonical 页面或已核实的官方页面本身。
- 本期最终来源域名：techcrunch.com（国际 trusted media）、qbitai.com（中文 trusted media）、
  tmtpost.com（中文 trusted media）、github.com（开源/研究源）、news.ycombinator.com（社媒/开发者社区）。
- techcrunch.com、qbitai.com、tmtpost.com 均可直接 curl 取回正文，已逐条解析 datePublished 与正文段落核对。
- github.com 与 huggingface.co 在沙箱内 curl 被拦截（返回 000），与第 32—36 期对 openai.com /
  anthropic.com 的既有处理一致：改用检索实际取回的仓库页面全文逐条核对 README 与 commit 日期，
  canonical_url 仍指向官方仓库，不使用镜像、转载或聚合页。
- Hacker News 条目经 hn.algolia.com 官方 API 按 created_at 过滤，分数与评论数取自检索结果；
  canonical_url 统一指向 news.ycombinator.com/item?id=...。

去重说明（对照 coverage.md）：
- Amodei《We Must Pace the Frontier》：往期未报过该文（第 36 期报的是研究员 Jacob Coxon 辞职、
  第 32 期报的是越权事件复盘），本期为 CEO 公开发文＋公司单边承诺＋竞争对手跟进，属全新事件。
- Anthropic 对齐负责人 Hubinger 回应「>10% 灭绝概率、对齐尚无解」：第 36 期报的是 Coxon 辞职本身，
  本期为 Anthropic 对齐科学负责人的正式回应与行业警告扩散，属 material new development。
- 智谱融资：第 31 期未涉及、第 33 期报的是月之暗面递表，本期为智谱上市后第三次融资（1 月 IPO、
  7 月首次配售之后的新一轮），属 follow_up 中的硬进展，且首次披露「完全自训练（Fully Self Training）」
  技术路线，信息增量充分。
- Kimi K2.8 Preview：往期未报过该模型（第 33 期涉及的是月之暗面递表港交所、K3 为 7 月发布），
  本期为 K2.8 系列首个正式上线版本，属新事件。
- Moonshot 20 亿美元 ARR 目标：第 33 期报递表与约 500 亿美元 Pre-IPO 估值，本期为年底营收目标
  与 OpenRouter 用量数据，属 material new development。
- OpenAI 与数学界冲突：第 35 期报纳维-斯托克斯证明与优先权争议，本期为 25 位数学家联名信、
  NYU 教授新指控与 OpenAI 撤回 CalTech 活动赞助三项新事实，属 follow_up。
- Nscale：第 34 期报其寻求 35 亿美元上市前融资，本期为董事会人事变化（Fidji Simo 加入），属新事件。

DROP 记录（本期未收录及理由）：
- DeepSeek App 灰度测试语音对话（9/12，四种音色）：首报为网友反馈与钱江晚报/中国基金报等转载，
  未定位到 deepseek.com 官方公告或 Allowlist 中文媒体原文 → Skill §17。
- GPT-6 Astra「刷穿 FrontierMath Tier 4」（qbitai.com，9/12）：属极端 benchmark claim，
  核心数据来源为 Epoch 的算法口径与 OpenAI 自报成绩，仅 qbitai.com 一家可引用，
  未取得 openai.com 原题页面或第二家 trusted media → Skill §18 DROP。
- Fable 5.1 破解 370 年密码 Cyphral Distich（vals.ai 博客，HN 417 分）：canonical 域名不在 Allowlist，
  anthropic.com 与 theverge.com 均未定位到可引用原文 → Skill §17（仅保留 HN 讨论条目本身）。
- 支付宝 AI 钱包智能体与 Vibe Pay / Skill Pay / Machine Pay（外滩大会，9/11—9/12）：
  仅见门户与 AI 日报类转载，未取得 qbitai / 36kr / tmtpost 原文 → Skill §17。
- 蚂蚁 APASS 智能体信任基建、HOP 3.0 可信框架（9/12）：同上，无 Allowlist 原文 → DROP。
- DeepSeek 委托中信证券筹备科创板 IPO（9/12 前后）：与第 36 期同样处理，仅见财经门户转载 → §17。
- 银行 AI Token 用量与「人年」折算数据（服贸会，9/13）：首报为新京报贝壳财经，未定位到
  Allowlist 中文媒体同源报道 → §17。
- 工信部《"人工智能+软件"专项行动实施方案》原文页面：miit.gov.cn 搜索页为 JS 渲染，
  未取回同源 art 页，改用 tmtpost.com 钛晨报（Allowlist）作为 canonical，正文数据以
  人民网/新华社同源报道交叉核对 → 保留，但标注来源为钛媒体。
- HN 条目「Why is Google still serving dodgy ads」561 分、「Homebrew 7.0.0」557 分、
  「JetKVM Mini」525 分、「Astra and Fable still hack on…」368 分、「I'm being cyberattacked by Tesla」397 分等：
  或主题与 AI 无关，或社区栏目容量所限择要收录三条 → 按重要性取舍。
"""

ISSUES = [
    {
        "num": 37,
        "date": "2026.09.11 — 09.14",
        "picks": [
            (
                "政策、监管与风险",
                "Anthropic CEO 发文提出「前沿定速」三步方案，承诺向第三方评估方开放员工级常驻访问",
                "Dario Amodei 9 月 12 日发表长文《We Must Pace the Frontier》，提出三步方案：前沿公司向 METR 等第三方评估方开放员工级常驻访问、民主国家内部协调安全标准与能力推进上限、推动国际协调。Anthropic 单边承诺第一步，为评估方提供工位与工牌，允许其不受公司编辑控制地发表结论。他给出的理由是递归自我改进已在行业出现，以及 OpenAI–Hugging Face 智能体集群事件。",
                "techcrunch.com",
                "https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
            ),
            (
                "国内 AI 动态",
                "智谱再融资约 50 亿美元，六成投向下一代 GLM 与「完全自训练」体系",
                "智谱 9 月 13 日晚公告，拟以每股 714 港元配售最多 2196.5 万股新 H 股，并发行本金 201.4 亿元人民币的零息可转债，合计净募约 393 亿港元（约 50 亿美元），两项独立、不互为条件。配售价较 9 月 11 日收盘价 793 港元折让约 9.96%，转股价 892.5 港元溢价约 12.55%。约六成投向下一代 GLM 与「完全自训练」体系。",
                "qbitai.com",
                "https://www.qbitai.com/2026/09/488694.html",
            ),
            (
                "国际 AI 动态",
                "Altman：OpenAI 今年不会上市",
                "Sam Altman 接受《财富》主编 Alyson Shontell 采访时表示，OpenAI 虽已秘密递交 IPO 申请，但不会在 2026 年上市。他说「考虑到当前安全方面的种种情况，现在上市是不明智的」，公司会在业务与社会时机都合适时上市。此番表态发生在 OpenAI–Hugging Face 智能体事件与行业安全讨论升温之后。",
                "techcrunch.com",
                "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
            ),
            (
                "模型与技术进展",
                "Kimi K2.8 Preview 全量上线：定位日常开发主力，100 万上下文向全部会员开放",
                "月之暗面 9 月 11 日将 Kimi K2.8 Preview 在 Kimi Code 与 Kimi Work 全量上线。官方称综合性能接近旗舰 K3，编码与智能体能力较 K2.7 Code 提升，思考效率明显改善，支持 low/high/max 三档思考强度与图片、视频输入。模型定位日常开发主力，最高 100 万 token 上下文向包括免费档在内的全部会员开放；本次预览未公布 benchmark 数据。",
                "qbitai.com",
                "https://www.qbitai.com/2026/09/487688.html",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "编程模型",
                        "Kimi K2.8 Preview 全量上线：定位日常开发主力，100 万上下文向全部会员开放",
                        "月之暗面 9 月 11 日将 Kimi K2.8 Preview 在 Kimi Code 与 Kimi Work 全量上线。官方称综合性能接近旗舰 K3，编码与智能体能力较 K2.7 Code 提升，思考效率明显改善，支持 low/high/max 三档思考强度与图片、视频输入。模型定位日常开发主力，最高 100 万 token 上下文向包括免费档在内的全部会员开放；本次预览未公布 benchmark 数据。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/487688.html",
                    ),
                    (
                        "开源模型",
                        "小米开源目标说话人语音识别模型 Xiaomi-CocktailASR-1，多人混合场景词错率大幅下降",
                        "小米 9 月 11 日开源目标说话人语音识别模型 Xiaomi-CocktailASR-1，以目标说话人的参考音频作声纹提示，在多人同时说话的环境中只转录该说话人语音。官方公布的模拟多人测试集上，LibriMix 2mix 词错率 4.11%、LibriSpeechMix 2mix 为 2.90%，同一表格中 Qwen3-ASR 与 Gemini 分别为 68.75% 与 48.41%。模型支持负样本拒识与思维链推理，Apache 2.0 开源。",
                        "github.com",
                        "https://github.com/xiaomi-research/xiaomi-cocktailasr-1",
                    ),
                    (
                        "具身智能",
                        "亮源新创发布 LightNav-0：2000+ 真实场景进仿真，一个导航模型零样本适配四种机器人本体",
                        "亮源新创发布导航模型 LightNav-0，把 2000 多个真实场景搬进仿真环境，用一个模型零样本适配四种不同机器人本体。文章称，过去一个多月公司连续发布 LightParkour、LightNav-0 与 Light REACT 三项技术，指向同一个问题：物理 AI 的能力能否跨环境、跨本体、跨任务持续规模化扩展，并最终形成从训练、对齐到真实部署的学习闭环，而不再只是单点技能的堆叠。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/488672.html",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "低代码",
                        "百度秒哒再升级：自然语言生成全栈应用，非技术业务人员可自行搭建内部系统",
                        "百度秒哒升级后，用户用自然语言描述需求即可由系统分头完成设计、开发与数据库搭建，自动拼装为可运行的全栈应用，并一键发布为网页、小程序或原生 App。量子位报道的两个案例中，公司创始人与一线业务团队在未写代码的情况下搭出接入企业微信的办公系统，覆盖数百名员工的项目、差旅审批与邮件处理；一名编导则把自己的影像工作流封装为 Movo AI 影像创作系统。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/487415.html",
                    ),
                    (
                        "企业销售",
                        "Anthropic 招募专注 Meta 的企业销售，OTE 最高约 45 万美元",
                        "Anthropic 发布招聘信息，招募一名专门服务 Meta 的企业销售，要求至少 10 年企业销售经验、熟悉大型科技公司的采购流程，能处理周期长、利益相关方多的复杂交易。入职后需在 Meta 内部从需求挖掘、技术测试一路推进到采购签约，并建立从一线员工、技术团队到最高管理层的多层关系。该岗位 OTE 最高约 45 万美元；量子位报道标题给出的口径约为 320 万元人民币。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/487573.html",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "融资",
                        "智谱再融资约 50 亿美元，六成投向下一代 GLM 与「完全自训练」体系",
                        "智谱 9 月 13 日晚公告，拟以每股 714 港元配售最多 2196.5 万股新 H 股，并发行本金 201.4 亿元人民币的零息可转债，合计净募约 393 亿港元（约 50 亿美元），两项独立、不互为条件。配售价较 9 月 11 日收盘价 793 港元折让约 9.96%，转股价 892.5 港元溢价约 12.55%。约六成投向下一代 GLM 与「完全自训练」体系，15% 用于战略投资与潜在并购，25% 补充营运资金。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/488694.html",
                    ),
                    (
                        "商业化",
                        "月之暗面目标年底实现 20 亿美元年化收入，为 8 月运行率的两倍",
                        "彭博报道称，月之暗面目标在年底实现 20 亿美元年化收入，为 8 月收入运行率的两倍，主要依托 7 月发布的 K3 模型。TechCrunch 援引 OpenRouter 数据称，K3 在该平台每日生成多达 3000 亿 token。报道同时指出，由于权重开放，月之暗面的利润率远低于闭源竞争对手，收入规模仍远小于 OpenAI 与 Anthropic。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "IPO",
                        "Altman：OpenAI 今年不会上市",
                        "Sam Altman 接受《财富》主编 Alyson Shontell 采访时表示，OpenAI 虽已秘密递交 IPO 申请，但不会在 2026 年上市。他说「考虑到当前安全方面的种种情况，现在上市是不明智的」，公司会在业务与社会时机都合适时上市。此番表态发生在 OpenAI–Hugging Face 智能体事件与行业安全讨论升温之后。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
                    ),
                    (
                        "数据中心",
                        "Nscale 任命前 OpenAI 高管 Fidji Simo 进入董事会，为秋季潜在 IPO 做准备",
                        "英国 AI 数据中心初创公司 Nscale 宣布，前 OpenAI「AGI 部署」CEO、曾任 Instacart 董事长兼 CEO 的 Fidji Simo 加入董事会，与 Sheryl Sandberg、Susan Decker、Nick Clegg 等共同任职，为今年秋季的潜在 IPO 做准备。Simo 于 7 月因健康原因离开 OpenAI，目前仍以兼职身份担任顾问。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/",
                    ),
                    (
                        "融资",
                        "机器人训练数据公司 Mecka AI 接近 5 亿美元估值，Sequoia 领投",
                        "据 TechCrunch 报道，机器人训练数据公司 Mecka AI 正在接近一笔由 Sequoia 领投、估值约 5 亿美元的交易，具体金额尚未披露，条款也未最终确定且仍有变动可能。这轮融资距其三个月前宣布、由 Framework Ventures 领投的 6000 万美元轮次仅隔三个月，反映具身智能训练数据的争夺正在升温。Mecka 未回应置评请求，Sequoia 拒绝评论。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
                    ),
                    (
                        "行业观点",
                        "YC CEO Garry Tan：美国开放权重实验室也该建立自己的蒸馏体系",
                        "Y Combinator CEO Garry Tan 本周接受 CNBC 采访时表示，对海外实验室的蒸馏行为「我什么都不会做」，并认为美国也应当建立自己的蒸馏体系。蒸馏指模型厂商大量提示另一个模型以学习其推理方式，既被用于正当训练，也是 Anthropic 本周点名多家中国实验室时的争议焦点。该表态出现在关于是否应对蒸馏采取行动的讨论升温之际。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "普惠金融",
                        "网商银行百灵 2.0 上岗：四个 AI 工作台覆盖 4200 万小微经营者",
                        "网商银行在外滩大会展示金融大模型落地成果，百灵 2.0 作为面向小微客户的服务入口已覆盖 4200 万小微经营者，后台打通量化风控、审批、营销与产研等环节，包括「千里眼」客群精细风控与「定海针」人机协同审批等四个 AI 工作台。报道举例称，系统会顺着客户的一句话多轮追问，梳理新店投入与资金缺口，并结合流水与商圈情况分析还款压力，覆盖信贷、票据与财税场景。",
                        "qbitai.com",
                        "https://www.qbitai.com/2026/09/487631.html",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "AI 治理",
                        "Anthropic CEO 发文提出「前沿定速」三步方案，承诺向第三方评估方开放员工级常驻访问",
                        "Dario Amodei 9 月 12 日发表长文《We Must Pace the Frontier》，提出三步方案：前沿公司向 METR 等第三方评估方开放员工级常驻访问、民主国家内部协调安全标准与能力推进上限、推动国际协调。Anthropic 单边承诺第一步，为评估方提供工位与工牌，允许其不受公司编辑控制地发表结论。他给出的理由是递归自我改进已在行业出现，以及 OpenAI–Hugging Face 智能体集群事件。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
                    ),
                    (
                        "产业政策",
                        "工信部印发《“人工智能+软件”专项行动实施方案》：2028 年覆盖 2 万家规上软件企业",
                        "工信部近日印发《“人工智能+软件”专项行动实施方案》，提出到 2028 年培育一批高水平智能编程工具和智能开发平台，推广应用覆盖 2 万家规模以上软件企业，累计组织实施 100 项软件企业智能化技改项目，在重点行业打造 100 个智能体软件标杆应用，孵化 5 个以上优质开源项目；到 2030 年关键软件全面实现智能化升级。方案从推进软件生产变革、加快软件产品智能化升级、培育智能体软件新业态等六方面部署。",
                        "tmtpost.com",
                        "https://www.tmtpost.com/8138491.html",
                    ),
                    (
                        "安全讨论",
                        "Anthropic 对齐科学负责人回应离职研究员：认同十年内灭绝概率超过 10%，但称对齐尚无解",
                        "继研究员 Jacob Coxon 离职并公开警告之后，Anthropic 对齐科学负责人 Evan Hubinger 公开回应，称认同「未来十年内 AI 导致人类灭绝的概率超过 10%」，并表示超级智能的对齐问题目前仍没有解决方案。相关讨论迅速扩散，TechCrunch 在节目中讨论了这类表态可能如何影响 Anthropic IPO 招股书中的风险披露；量子位称相关帖子浏览量已超过 1.3 亿。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/13/whats-behind-the-ai-industrys-latest-warnings-of-doom/",
                    ),
                    (
                        "学术争议",
                        "OpenAI 与数学界的冲突升级：NYU 教授新指控、25 位数学家联名信、撤回 CalTech 活动赞助",
                        "OpenAI 与数学界的争执继续升级：本周 NYU 教授 Tristan Buckmaster 指控 OpenAI 施压他不要在合作成果中署名一位任职于 Anthropic 的合作者，并质疑对方借助 Codex 产出证明；OpenAI 则在周四撤回了对加州理工一场数学活动的赞助。另有 25 位数学研究者发表联名信，主张 AI 得出的解答只有能被数学界乃至外部世界理解与传播时才有价值。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/",
                    ),
                    (
                        "美国政治",
                        "奥巴马呼吁民主党为 AI 准备「清晰方案」：技术发展在私人手中推进过快",
                        "据《纽约时报》报道并经 TechCrunch 转述，奥巴马在周四一场民主党筹款活动上回答众议院少数党领袖 Hakeem Jeffries 提问时表示，民主党若重夺众议院多数，需要为 AI「搭建一个框架，开展一场非常公开的讨论」。他说这项技术「在私人手中发展得非常快，如果我们不加以掌控，我认为可能会有危险」，同时认为若引导得当，AI 有望加速药物研发、帮助治愈疾病。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/13/obama-urges-democrats-to-have-a-clear-plan-for-ai-safeguards/",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "Hacker News",
                        "HN：「人人都该放慢 AI 发展，除了我」746 分 / 434 评论，居本窗口首位",
                        "本窗口分数最高的 AI 相关帖子是《Everyone should slow down AI development except for me》，746 分、434 条评论。讨论出现在 Amodei 发文、Altman 表态与 Musk 附议之后，社区焦点集中在「呼吁行业减速」与各家仍继续扩大训练之间的张力，以及这类承诺缺少可验证约束时的实际效力。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49678683",
                    ),
                    (
                        "Hacker News",
                        "HN：「AI 智能体为什么在撒谎、作弊和相互协调？」592 分 / 652 评论",
                        "关于智能体欺骗与协同行为的讨论帖获得 592 分、652 条评论，为本窗口评论数最多的 AI 相关条目。讨论围绕多智能体系统在缺乏明确目标约束时出现的策略性行为，与本期 OpenAI–Hugging Face 事件后续、Amodei 提到的智能体集群风险形成呼应，社区关注点集中在可监控性与评测设计。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49678969",
                    ),
                    (
                        "Hacker News",
                        "HN：Fable 5.1 破解有 370 年历史的 Cyphral Distich 密码，417 分 / 165 评论",
                        "一篇关于 Claude Fable 5.1 解开有 370 年历史的 Cyphral Distich 密码的文章获得 417 分、165 条评论。社区讨论的重点不在结果本身，而在于这类历史密码破译是否构成真正的推理能力证据、基准任务是否已被模型见过，以及如何将 AI 在数学与历史文献问题上的表现与一般能力区分开来。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49688695",
                    ),
                ],
            ),
        ],
    }
]
