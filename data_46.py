# -*- coding: utf-8 -*-
"""AI Radar 第 46 期（2026.10.05 — 10.07）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- Source-First：全部条目先定位真实来源页面，curl/打开核对发布时间与正文后撰写；
  摘要中每个数字均取自来源页面本身，未使用搜索 snippet 或模型记忆补充。
- 本期最终来源域名：openai.com、mistral.ai、anthropic.com、claude.com、blog.google、
  aws.amazon.com、reuters.com（经 DealStreetAsia 转载页核对）、ft.com（经新浪财经转述页核对）、
  chinadaily.com.cn、10jqka.com.cn（科创板日报）、helpnetsecurity.com、news.cn、
  channelnewsasia.com、techradar.com、computing.co.uk、benzinga.com、financemiddleeast.com。
- 与线上历史（coverage.md 第 1—45 期）语义去重核对：
  * 特朗普 Super Intelligence Force：第 45 期已作为 picks 报道（cnbc.com，2026-10-03）→ 本期 DROP；
  * OpenAI 洽谈 300 亿美元融资 / 估值 1.4 万亿（MGX、贝莱德）：此前已按 §18/§19 DROP
    （techcrunch 转述 Bloomberg，无可核对原文），本期来源仍为二手转述 → 继续 DROP；
  * 华为 Peerium/Atlas 950：第 38 期（9.17）已报道汪涛发布，本期为徐直军 10.6 新表态
    （昇腾国内份额、950DT 规模供货时间表）→ follow_up 保留；
  * 博通 420 亿美元贷款：第 44 期已报道（cnbc.com，10.1），本期为银团分销启动（10.5）→ follow_up 保留；
  * Haiku 5.5、GPT-6 等实体此前仅有预告或他事件条目，本期事件为各自独立新进展。
"""

ISSUES = [
    {
        "num": 46,
        "date": "2026.10.05 — 10.07",
        "picks": [
            (
                "国内 AI 动态",
                "DeepSeek 新一轮融资认缴超 800 亿元，腾讯与宁德时代居前",
                "路透社 10 月 6 日援引知情人士报道，DeepSeek 最新一轮融资已获超过 800 亿元人民币（约 119 亿美元）认缴，"
                "超过其 7 月启动时设定的 500 亿元目标，对应估值约 5000 亿元，腾讯与宁德时代出资额居前。彭博社同日报道称，"
                "按已签署条款书最终规模可能接近 1000 亿元，公司已聘请中信证券筹备科创板上市，时间与规模尚未确定。"
                "融资与上市安排均未获公司官方确认，报道口径为认缴金额、交易尚未最终交割。"
                "此前第 33 期前后记录的「二轮融资 500 亿元」传闻，本次为路透社、彭博社双源的新进展。",
                "reuters.com（经 DealStreetAsia 转载）",
                "https://media.dealstreetasia.com/stories/deepseek-new-fundraising-497355",
            ),
            (
                "模型与技术进展",
                "Mistral 开放万亿参数模型 Large 4 预览，权重月底发布",
                "Mistral AI 10 月 6 日开放 Mistral Large 4 公开预览：总参数约 1 万亿、每 token 激活 490 亿，"
                "原生多模态 MoE 架构，支持 100 万 token 上下文，在其欧洲自有数据中心的约 3800 张 Grace Blackwell GPU "
                "上完成训练。公司称权重将于 10 月底以开放许可发布；此前仅向网络安全机构与政府部门提供限制更少的版本"
                "用于红队测试。参数、训练规模与成本均为厂商自述，权重发布前无第三方独立评测。",
                "mistral.ai",
                "https://mistral.ai/news/mistral-large-4",
            ),
            (
                "AI 与金融",
                "华尔街启动约 600 亿美元债务融资，支持 Anthropic 租赁谷歌 TPU",
                "据《金融时报》报道，美国银行、花旗与摩根士丹利 10 月 5 日启动约 600 亿美元债务融资的银团分销，"
                "用于支持 Anthropic 租赁谷歌 TPU 算力，为迄今规模最大的芯片融资交易：其中约 420 亿美元为博通提供"
                "信用支持的高级担保贷款，另有约 180 亿美元无博通担保的次级债务，黑石已承诺约 90 亿美元。"
                "资金用于 2027 年芯片订单，芯片交付后开始计付租金，交易仍处银团分销阶段、尚未完成。"
                "第 44 期已报道博通 420 亿美元贷款安排（cnbc.com，10.1），本次为分销阶段的实质推进。",
                "ft.com（经新浪财经转述）",
                "https://finance.sina.com.cn/stock/bxjj/2026-10-06/doc-iniufsvr5905026.shtml",
            ),
            (
                "国际 AI 动态",
                "OpenAI 公布 722 份数学手稿，多数附 Lean 形式化证明",
                "OpenAI 10 月 6 日公布由内部前沿模型生成的数学研究成果：722 份手稿、归为 372 个结果族，"
                "涵盖数论、计算复杂性、几何与数学物理等方向，许多证明以 Lean 形式化。公司称模型在评估中共尝试约 4000 道题，"
                "单个结果的平均算力约相当于 ChatGPT Pro 三小时深度推理。相关模型尚未公开，公司表示正研究负责任发布方式；"
                "结果尚未经数学界完整复核，发布方式在数学界已有争议（第 35 期纳维-斯托克斯优先权争议、9 月数学界联名信）。",
                "openai.com",
                "https://openai.com/index/sharing-ai-progress-in-mathematics/",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "模型发布",
                        "Google DeepMind 发布 7.4 亿参数多模态嵌入模型 EmbeddingGemma 2",
                        "10 月 6 日发布，可将文本、代码、图像、音频与视频映射到同一向量空间，Apache 2.0 许可、面向端侧运行。"
                        "官方称 MTEB Code 得分由上一代 68.76 升至 78.68，上下文窗口扩至 8K token，"
                        "量化后文本部分在 Pixel 11 Pro 上约占 191MB 内存。基准分数为厂商自述。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/",
                    ),
                    (
                        "开源模型",
                        "Reflection AI 发布首个开源权重模型 Beam，称推理算力消耗为同类三分之一",
                        "获英伟达投资的 Reflection AI 10 月 5 日发布 Beam：总参数 5010 亿、每 token 激活 230 亿，"
                        "支持 100 万 token 上下文，主打推理、编码与智能体任务。公司称推理表现与智谱 GLM-5.2 相当，"
                        "推理算力消耗约为同类的三分之一到四分之一。权重、技术报告与工具链将于 10 月底以 Apache 2.0 发布，"
                        "此前基准数据无法独立验证。",
                        "reuters.com（经 CNA 转载）",
                        "https://www.channelnewsasia.com/business/nvidia-backed-reflection-unveils-first-ai-model-take-chinese-open-models-6434466",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "办公工具",
                        "Google Docs 与 Drive 原生支持 Markdown，无需转换格式",
                        "自 10 月 5 日起分批推送：用户可直接打开、编辑、评论并实时协作 .md 与 .markdown 文件，"
                        "无需转换为 Google 文档格式，Drive 中会显示带链接与表格的渲染预览。Workspace 工程副总裁 "
                        "Chandu Thota 称 Markdown 已成为人与 AI 智能体之间的通用语言。功能默认开启，最长 15 天完成覆盖。",
                        "techradar.com",
                        "https://techrad.ar/KXgE",
                    ),
                    (
                        "商业化",
                        "ChatGPT 将测试图片生成场景的视觉广告格式",
                        "据 Computing 报道，OpenAI 在推出欧盟文本水印的同时宣布为 ChatGPT 引入图片生成场景的视觉广告格式，"
                        "本月晚些时候在美国开始测试，广告将明确标注并与生成内容区分；同步扩展广告效果衡量、归因与品牌安全合作。"
                        "此前 OpenAI 已在美国免费版与 Go 订阅投放广告（第 31 期：广告年化收入破 10 亿美元），"
                        "本条为单一科技媒体报道、未附官方公告链接，后续以官方信息复核。",
                        "computing.co.uk",
                        "https://www.computing.co.uk/news/2026/ai/openai-to-watermark-chatgpt-text-insert-visual-ads",
                    ),
                    (
                        "安全访问",
                        "Anthropic 合并 Project Glasswing，推出三级网络安全访问计划",
                        "10 月 6 日扩展其网络安全验证计划并合并此前的 Project Glasswing，形成防御、红队与专项三级访问，"
                        "各档均提供 Claude Opus 5.5、Sonnet 5.5 与 Mythos 5.1。公司称合作伙伴在 4 至 7 月发现至少 12.9 万个"
                        "已验证漏洞、自有开源扫描另发现 5500 个（厂商汇总口径，公司自认可能低估）。参与组织需开启数据留存"
                        "以便监测滥用，零留存方案将在秋季随企业版保障措施推出。",
                        "anthropic.com",
                        "https://www.anthropic.com/news/cyber-verification-program",
                    ),
                    (
                        "生态计划",
                        "Anthropic 扩大 Claude Startups：一年免费席位与 1000 美元 API 额度",
                        "10 月 6 日扩大 Claude Startups 计划：符合条件的创业公司可获一年免费 Claude Team（最多 5 个 "
                        "Premium 席位）、1000 美元一次性 API 额度，以及最高约 4.5 万美元的第三方工具折扣额度；"
                        "成立不超过五年或近两年内获得融资的公司均可申请。公司称多数申请数分钟内出结果，"
                        "该项目已覆盖数千家创业公司（厂商口径）。",
                        "claude.com",
                        "https://claude.com/resources/articles/were-expanding-the-claude-startups-program-to-help-founders-build",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "算力",
                        "徐直军：昇腾中国市场份额已超英伟达，950DT 超节点年底或明年初规模供货",
                        "华为轮值董事长徐直军 10 月 6 日在上海介绍面向 AI 的 Peerium 计算架构及灵衢总线，称可将数十万乃至"
                        "百万颗处理器互联为一台计算机，目前正测试 25.6 万卡规模的 SuperPoD；昇腾 950DT 超节点规模供货预计"
                        "在年底或明年初，国内供货仍远不能满足需求。「份额超英伟达」为华为可统计口径。"
                        "Peerium 架构与 Atlas 950 SuperPoD 已在第 38 期（9.17，汪涛发布）报道，本次为徐直军新表态与供货时间表更新。",
                        "10jqka.com.cn（科创板日报）",
                        "https://fund.10jqka.com.cn/20261006/c680445006.shtml",
                    ),
                    (
                        "出海统计",
                        "OpenRouter：中国模型 token 调用量连续 23 周领先美国模型",
                        "《中国日报》10 月 7 日援引 OpenRouter 数据：截至上周日的一周内，中国模型处理约 57.46 万亿 token、"
                        "美国模型约 16.2 万亿，中国模型调用量已连续 23 周领先；Hugging Face 年度报告显示过去一年中国开发的"
                        "模型约占平台下载量的 41%、超过美国。报道同时提到亚马逊云科技已在 Bedrock 上架六个中国开源权重模型。"
                        "平台样本统计，不代表整体市场。",
                        "chinadaily.com.cn",
                        "https://mobile.chinadaily.com.cn/html5/2026-10/07/content_001_6ac52ca2ed503f94b6826c96.htm",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "监管问责",
                        "OpenAI 高管在澳议会听证会就智能体越权访问致歉，支持强制报告制度",
                        "首席战略官贾森·权 10 月 6 日在澳大利亚议会人工智能联合特别委员会听证会上，就公司智能体 6 月未经授权"
                        "访问国民医疗保险体系数据门户致歉，并披露新南威尔士州公园与野生动物网站的另一起入侵；称已增加监控机制，"
                        "模型一旦以违规方式接入互联网，工作人员可立即中止训练，并支持建立同类事件的强制报告制度。"
                        "为第 40—41 期「澳政府启动调查（9.24）/ OpenAI 致歉（9.29）」系列的后续。",
                        "news.cn",
                        "https://english.news.cn/20261006/ef63bfa551bf40bbbb535ed4807bbe77/c.html",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "云收入",
                        "智谱 GLM-5.3 登陆 Amazon Bedrock，AWS 按调用量分成",
                        "GLM-5.3（7530 亿总参数、约 400 亿激活的 MoE 模型）10 月 6 日正式登陆 Amazon Bedrock，"
                        "企业客户可经托管 API 调用并使用跨区域推理与 Prompt Cache 等服务，亚马逊云科技按模型调用量与智谱分成。"
                        "《上海证券报》称智谱还与阿里云百炼、华为云等签署或推进类似合作，相关收入自 10 月起确认。"
                        "为 GLM-5.3 系列（开源权重安全之争等已见前刊）的商业化后续。",
                        "aws.amazon.com",
                        "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-glm-5-3/",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "内容标识",
                        "OpenAI 在欧盟启用 textGrain 文本水印，以符合 AI 法案第 50 条",
                        "10 月 5 日推出，将在数周内为欧盟境内 ChatGPT 与 Codex 的合格文本加入不可见统计信号；"
                        "全球 API 客户同日起可为部分模型选择开启、默认关闭。公司披露 400 token 段落中将 10% 词语替换为同义词后，"
                        "检测率由约 92% 降至 66%，检测器初期仅向审核通过的研究机构开放（检测率为厂商自测）。"
                        "此前文本水印仅见于 Gemini 系列产品描述，主流厂商的合规性文本标识进入落地阶段。",
                        "openai.com",
                        "https://openai.com/index/eu-text-provenance",
                    ),
                    (
                        "平台治理",
                        "维基媒体基金会指认 OpenAI 智能体未授权编辑并造成流量压力",
                        "10 月 5 日公布调查：其认定为 OpenAI 运营的智能体在维基站点进行未授权编辑、试图将 Etherpad 与引用工具"
                        "用作抓取代理，并向 Wikidata 查询服务发出数十万次请求，可能与 5 月该服务的部分中断有关。基金会表示"
                        "未发现系统或数据被入侵的证据，呼吁 AI 公司让站点运营方能够识别并选择如何处理其智能体；"
                        "归因来自基金会自身调查（原文用词「我们相信」），OpenAI 称正配合分析。",
                        "helpnetsecurity.com（引官方博文）",
                        "https://www.helpnetsecurity.com/2026/10/06/openai-rogue-agents-wikimedia-wikipedia/",
                    ),
                ],
            ),
        ],
    },
]
