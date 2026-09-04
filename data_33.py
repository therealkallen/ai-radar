# -*- coding: utf-8 -*-
"""AI Radar 第 33 期（2026.09.02 — 09.04）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- 全部条目均为 Source-First：先检索到事件，再定位 Allowlist 内的 primary / trusted media 原文，
  逐条 WebFetch 或读取官方页面正文后撰写，摘要中的每一个数字都来自 canonical 页面。
- 本期最终来源域名：blogs.nvidia.com（NVIDIA primary）、techcrunch.com（国际 trusted media）、
  blog.google（Google AI primary）、openai.com（OpenAI primary）、github.com（技术/开源来源）、
  aliyun.com（Qwen primary）、36kr.com（中文 trusted media）、theverge.com（国际 trusted media）、
  digital-strategy.ec.europa.eu（政策来源）、news.ycombinator.com（社媒/开发者社区）。
- 沙箱网络对部分主域（reuters.com、deepmind.google、openai.com 直连等）存在抓取拦截；
  凡遇拦截，均改用官方同等页面（如 deepmind.google → blog.google）或 Allowlist 内 trusted media 原文，
  与第 32 期既有做法一致。

去重说明（对照 coverage.md）：
- 英伟达收购 Hugging Face：第 30 期曾报「深度谈判、交易未最终签署」；本期为签署最终协议并官宣
  （129.303 亿美元、开放平台承诺），属 material new development，作为 follow_up 收录。
- OpenAI Astra：第 32 期曾报「达到《准备框架》Critical 网络安防门槛、限流开放」；本期为模型正式发布
  （开放节奏、编码/计算机使用基准、不透明循环推理争议、AGI 表态），属 material new development，
  作为 follow_up 收录，不重复。

DROP 记录（本期未收录及理由）：
- Meta Muse Spark 1.3（9/2）：仅见 techtimes.com、百度百科及门户转载，无 ai.meta.com 官方原文，
  亦无 36kr/jiqizhixin/qbitai/tmtpost 覆盖 → 按 Skill §17 DROP。
- 腾讯开源混元 Hy4 preview（9/3）：与第 31 期「腾讯混元开源 Hy4 Preview」为同一事件，无新硬进展 → DROP。
- 智谱 GLM-5.3-Flash 原生多模态（9/3）：与第 30 期「智谱认领 Ox Alpha = GLM-5.3-Flash 并 MIT 开源」
  为同一模型无新硬进展 → DROP。阿里 Qwen3.8-Flash-Next 同理（对照第 30 期 Qwen3.8-Flash）→ DROP。
- Cursor Self-Hosted Machines（9/2）：官方博客 cursor.com 不在 Allowlist → DROP。
- World Labs Atlas（9/1）：官方域 worldlabs.ai 不在 Allowlist，且无 trusted media 原报道 → DROP。
- Google Workspace 推出 AI 设计工具 Pics：blog.google 目标页返回 404，未找到官方原文 → DROP。
- 开源项目关闭外部 PR / Vercel 软件工厂：canonical 仅见 Latent Space 转述（oo.news、aibreakingwire 等聚合），
  无 vercel.com 官方原文 → 按 Skill §17 DROP。
- 中央网信办「清朗·整治 AI 应用乱象」第二阶段（9/3）：原文在 paper.people.com.cn，不在 Allowlist，
  未找到 cac.gov.cn 同源公告 → DROP。
- Anthropic × Lambda 350 亿美元云协议：未见合规 reuters.com 原文 URL（多为镜像/转载域），
  与第 32 期 BoE/FSB 同样处理 → DROP。
- 燧原科技科创板申购（9/2）：仅见 21 财经、新浪、证券时报等，未定位到 36kr/jiqizhixin/tmtpost 原文 → DROP。
- AI Token 价格指数跌至 97 美分：首报方 CNBC 未检索到可直接引用的 cnbc.com 原文 URL → DROP。
"""

ISSUES = [
    {
        "num": 33,
        "date": "2026.09.02 — 09.04",
        "picks": [
            (
                "国际 AI 动态",
                "英伟达正式宣布 129.303 亿美元收购 Hugging Face，承诺保持开放平台",
                "英伟达 9 月 3 日宣布已就收购 Hugging Face 签署最终协议，交易金额 129.303 亿美元。Hugging Face 聚集约 1800 万名开发者、300 万个模型、50 万个数据集与 100 万个应用。黄仁勋在公开信中表示，收购后将保持其开放平台定位，支持各类模型与硬件，不会要求开发者改用英伟达算力。",
                "blogs.nvidia.com",
                "https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/",
            ),
            (
                "模型与技术进展",
                "OpenAI 正式发布 GPT-6 Astra：Daybreak 客户优先，可监测性引发争议",
                "OpenAI 于 9 月 3 日发布新模型 Astra，称其在计算机与浏览器操作上表现突出，软件工程相关测试成绩高于自家 Sol 与 Anthropic 的 Fable。模型当天先向参与 Daybreak 网络安全计划的客户开放，一周内陆续覆盖各付费档与 API。争议在于其不透明循环推理会遮蔽思维链，Pachocki 承认能力增强会加大监测难度。",
                "techcrunch.com",
                "https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model",
            ),
            (
                "AI 与金融",
                "月之暗面保密递交港交所 A1，Pre-IPO 估值瞄准 500 亿美元",
                "多家媒体报道称，月之暗面本周以保密形式向港交所递交 A1 文件，正式启动港股 IPO 流程，公司回应不予置评。同时其正以约 500 亿美元投前估值推进 Pre-IPO 轮，可能是上市前最后一轮私募融资。该公司估值从 2025 年底约 43 亿美元升至今年 7 月 F 轮投后 350 亿美元；ARR 于 6 月中旬超过 3 亿美元。",
                "36kr.com",
                "https://www.36kr.com/p/3967584794269577",
            ),
            (
                "政策、监管与风险",
                "美国司法部首次就 AI 版权案表态：支持 OpenAI 主张训练属合理使用",
                "美国政府本周在《纽约时报》诉 OpenAI 案中提交利益陈述，支持训练大语言模型属合理使用，这是联邦政府首次就这一波 AI 版权诉讼正式表态。文件称，以对合理使用的误解限制大模型发展将阻碍科学与产业进步；纽约时报回应称政府站在少数万亿市值 AI 公司一边。该陈述仅具咨询性质，对法院无约束力。",
                "theverge.com",
                "https://www.theverge.com/ai-artificial-intelligence/988344/trump-administration-new-york-times-openai-lawsuit",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "模型",
                        "OpenAI 正式发布 GPT-6 Astra：Daybreak 客户优先，可监测性引发争议",
                        "OpenAI 于 9 月 3 日发布新模型 Astra，称其在计算机与浏览器操作上表现突出，软件工程相关测试成绩高于自家 Sol 与 Anthropic 的 Fable。模型当天先向参与 Daybreak 网络安全计划的客户开放，一周内陆续覆盖各付费档与 API。争议在于其不透明循环推理会遮蔽思维链，Pachocki 承认能力增强会加大监测难度。",
                        "techcrunch.com",
                        "https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model",
                    ),
                    (
                        "模型",
                        "谷歌发布 Gemini 3.8 Flash 与 3.8 Flash Cyber：六周内第三款 Flash",
                        "谷歌 9 月 2 日发布 Gemini 3.8 Flash 及其网络安全版本 3.8 Flash Cyber，距上一代约 20 天，为六周内第三款 Flash 模型。推广期定价为每百万 Token 输入 0.75 美元、输出 3.75 美元，2027 年起为 1.50 / 7.50 美元。Flash Cyber 在 CWE-Bench 上 pass@1 达 47.2%，接近前沿模型的 47.8%，仅通过 Fairwind 计划向受审核防御方开放。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
                    ),
                    (
                        "模型",
                        "Google DeepMind 发布 WeatherNext 3：小时级更新、最高 5 公里分辨率",
                        "谷歌 DeepMind 于 9 月 3 日发布气象模型 WeatherNext 3，将预报更新频率提升至每小时一次，关键地表变量分辨率达 5 公里，较上一代约清晰 5 倍。模型融合实时地球静止卫星数据、地面气象站观测、NASA IMERG 降水产品与自研降水再分析数据，已在 Google 搜索、Gemini、地图与 Maps Platform 天气 API 上线。",
                        "blog.google",
                        "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "医疗",
                        "ChatGPT 接入 Epic 电子病历，并推出公共卫生数据插件",
                        "OpenAI 宣布 ChatGPT for Healthcare 可接入 Epic 环境，临床人员可调取授权范围内的患者病历并直接提问，也可在支持部署中把 ChatGPT 嵌入病历界面，接入为只读、不回写。同时推出 Healthcare Public Data 插件，连接临床试验登记库、CMS 覆盖范围、DailyMed、PubMed 等九个官方数据源。UCSF Health 为试点伙伴。",
                        "openai.com",
                        "https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/",
                    ),
                    (
                        "电商",
                        "Anthropic 开源电商智能体蓝图 commerce-agents，含零售等四个可运行示例",
                        "Anthropic 于 9 月 2 日在 GitHub 开源电商智能体参考实现，采用 Apache 2.0 许可，包含面向消费者的购物代理与面向店员的商家代理两套实现，并附零售、旅游、电信、票务四个可运行示例。库存预警、定价建议与营销文案等操作均设人工审批关卡，代码可部署于 Claude API 及三大云平台。",
                        "github.com",
                        "https://github.com/anthropics/commerce-agents",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "模型",
                        "阿里云升级 Qwen3.8-Max 至 0902 快照：编码与协作智能体能力增强",
                        "阿里云 9 月 2 日公告，大模型服务平台百炼将于 9 月 5 日 10:00 起把 qwen3.8-max 自动更新为 qwen3.8-max-0902 快照模型，计费项和价格不变。官方称新快照在编码深度、协作智能体与视觉理解三方面增强，并延续 100 万上下文、思考模式与完整工具生态，用户可在生效前指定该名称提前测试。",
                        "aliyun.com",
                        "https://www.aliyun.com/notice/118616",
                    ),
                    (
                        "生态",
                        "腾讯 WorkBuddy 开放平台上线：首批超百家伙伴，打通硬件、应用与开发者",
                        "腾讯 9 月 2 日在深圳举办生态发布会，宣布 WorkBuddy 开放平台正式上线，首批引入超百家生态伙伴。硬件侧围绕听、看、记、聊、协五类触点接入十余个品类、超 30 个品牌，并推出 9 款联名硬件；应用侧上线 Buddy 应用入口，30 余个行业应用同步接入；开发者侧开放技能、专家与连接器三类能力。",
                        "36kr.com",
                        "https://36kr.com/newsflashes/3965876002381313",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "交易",
                        "英伟达正式宣布 129.303 亿美元收购 Hugging Face，承诺保持开放平台",
                        "英伟达 9 月 3 日宣布已就收购 Hugging Face 签署最终协议，交易金额 129.303 亿美元。Hugging Face 聚集约 1800 万名开发者、300 万个模型、50 万个数据集与 100 万个应用。黄仁勋在公开信中表示，收购后将保持其开放平台定位，支持各类模型与硬件，不会要求开发者改用英伟达算力。",
                        "blogs.nvidia.com",
                        "https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/",
                    ),
                    (
                        "服务",
                        "ChatGPT、Claude、Grok 同日集体宕机，为有报告以来最大规模",
                        "9 月 3 日，OpenAI、Anthropic 与 xAI 三家服务几乎同时出现异常。OpenAI 状态页记录 ChatGPT 与 Codex 错误率升高，影响登录、文件上传、语音模式、搜索与图像生成；Anthropic 技术员工称 Claude 因基础设施问题部分中断，公司约在美东中午 12 时 15 分解决；Grok 自美东上午 9 时 30 分起在网页与移动端中断。",
                        "theverge.com",
                        "https://www.theverge.com/ai-artificial-intelligence/989503/chatgpt-grok-claude-outage-down",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "融资",
                        "月之暗面保密递交港交所 A1，Pre-IPO 估值瞄准 500 亿美元",
                        "多家媒体报道称，月之暗面本周以保密形式向港交所递交 A1 文件，正式启动港股 IPO 流程，公司回应不予置评。同时其正以约 500 亿美元投前估值推进 Pre-IPO 轮，可能是上市前最后一轮私募融资。该公司估值从 2025 年底约 43 亿美元升至今年 7 月 F 轮投后 350 亿美元；ARR 于 6 月中旬超过 3 亿美元。",
                        "36kr.com",
                        "https://www.36kr.com/p/3967584794269577",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "版权",
                        "美国司法部首次就 AI 版权案表态：支持 OpenAI 主张训练属合理使用",
                        "美国政府本周在《纽约时报》诉 OpenAI 案中提交利益陈述，支持训练大语言模型属合理使用，这是联邦政府首次就这一波 AI 版权诉讼正式表态。文件称，以对合理使用的误解限制大模型发展将阻碍科学与产业进步；纽约时报回应称政府站在少数万亿市值 AI 公司一边。该陈述仅具咨询性质，对法院无约束力。",
                        "theverge.com",
                        "https://www.theverge.com/ai-artificial-intelligence/988344/trump-administration-new-york-times-openai-lawsuit",
                    ),
                    (
                        "平台监管",
                        "欧盟委员会依《数字服务法》将 ChatGPT 指定为超大型在线搜索引擎",
                        "欧盟委员会 8 月 31 日宣布，依据《数字服务法》将 ChatGPT 指定为超大型在线搜索引擎，Reddit 与 Roblox 被指定为超大型在线平台。三家服务均自行申报欧盟月均用户达到 4500 万门槛，须在 2027 年 1 月前履行额外义务，包括评估并缓解算法系统在非法内容传播、未成年人影响、选举进程等方面的系统性风险。",
                        "digital-strategy.ec.europa.eu",
                        "https://digital-strategy.ec.europa.eu/en/news/commission-designates-chatgpt-reddit-roblox-under-digital-services-act",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "Hacker News",
                        "Gemini 3.8 Flash 发布帖登顶 HN：1143 分、654 条评论，迭代节奏成焦点",
                        "Gemini 3.8 Flash 与 3.8 Flash Cyber 的发布帖成为本窗口 Hacker News 得分最高的条目，获得 1143 分与 654 条评论，高于同期的 Astra 发布帖与英伟达收购 Hugging Face 帖。讨论集中在六周三款 Flash 的迭代节奏、推广期结束后的真实成本，以及基准分数与实际编码体验之间的落差。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49537553",
                    ),
                    (
                        "Hacker News",
                        "「三大模型为何同时宕机」引发 524 条讨论，社区聚焦共享基础设施风险",
                        "9 月 3 日集体宕机后，Hacker News 上一篇提问帖获得 328 分与 524 条评论，为当日讨论量最高的条目。社区主要围绕共享云基础设施是否构成单点故障展开，多人提到微软 Azure 与 Cloudflare 同期也出现异常报告，但没有厂商确认共同根因。讨论延伸到企业侧容灾：任一环节故障都会使智能体工作流停摆。",
                        "news.ycombinator.com",
                        "https://news.ycombinator.com/item?id=49551096",
                    ),
                ],
            ),
        ],
    }
]
