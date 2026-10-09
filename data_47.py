# -*- coding: utf-8 -*-
"""AI Radar 第 47 期（2026.10.07 — 10.09）素材。

来源纪律（依《AI Radar Content Pipeline Skill》）：
- Source-First：全部条目先定位真实来源页面，curl/打开核对发布时间与正文后撰写；
  摘要中每个数字均取自来源页面本身，未使用搜索 snippet 或模型记忆补充。
- 本期最终来源域名：openai.com、anthropic.com、blogs.nvidia.com、perplexity.ai、
  community.perplexity.ai、liquid.ai、github.blog、digitaltrends.com、cnstock.com（上海证券报）、
  m.chinanews.com（中新经纬）、commonsensemedia.org、trahan.house.gov、politico.com、
  fortune.com、the-decoder.com、36kr.com、pandaily.com、sohu.com（凤凰网科技）、
  finance.sina.com.cn（新浪科技）、livemint.com（彭博社转载）、econotimes.com（金融时报转述）、
  cna.com.tw（中央社，转述《华尔街日报》/《金融时报》）、proactiveinvestors.com（转述彭博社）、
  ibtimes.co.uk、toutiao.com（环球网/财联社转述）、news.qq.com（腾讯新闻）、aa.com.tr。
- 与线上历史（coverage.md 第 1—46 期）语义去重核对：
  * GPT-6：模型实体早已存在（第 35 期纳维-斯托克斯、第 45 期 GPT-6 Astra 作弊等），
    本次「GPT-6 向 ChatGPT 全线推送 + Intelligent UI 上线」为产品分发的硬进展 → follow_up 保留；
  * Claude Haiku 5.5：第 41 期 Sonnet 5.5 条目预告「Haiku 新版数周内发布」，本次为正式发布 → follow_up 保留；
  * 博通：第 44 期为借予 Anthropic 420 亿美元、第 46 期为 Anthropic 600 亿银团分销，
    本次「为 OpenAI 定制芯片项目筹资逾 500 亿美元」为不同主体不同交易 → 新事件（早期洽谈，双源）；
  * Manus：此前已报「脱离 Meta 恢复独立运营」与 DROP 的「估值或翻倍」，本次为官宣落地融资 → follow_up 保留；
  * OpenAI 与数学界：第 46 期报道 722 份手稿发布，本次为人类数学协会呼吁抵制与结果撤回 → follow_up 保留；
  * 豆包：此前已报大模型 2.1 系列、豆包工作、手机助手，本次为鸿蒙 PC 原生应用落地 → 新事件；
  * SpaceX：此前条目为 Grok/被指收购 Cursor 等，本次 400 亿美元芯片融资为独立新事件（洽谈中，双源）；
  * SynthID Detector、GitHub 密钥分类器、Perplexity 嵌入模型、Liquid d1、Biohub、
    Common Sense 评估、CLAIM 法案、厘清智能、甲骨文融资：coverage.md 均无记录 → 新事件。
"""

ISSUES = [
    {
        "num": 47,
        "date": "2026.10.07 — 10.09",
        "picks": [
            (
                "模型与技术进展",
                "GPT-6 与 Intelligent UI 向 ChatGPT 全部套餐开放",
                "OpenAI 10 月 7 日向 ChatGPT Plus、Pro、Business 与 Enterprise 推送 GPT-6，次日扩展至 Free 与 Go："
                "付费档使用 GPT-6 Sol、免费档使用 Luna，Work 与 Codex 所用模型不变。同期上线 Intelligent UI，"
                "回答可混合文字、图表、按钮与表单并在生成过程中逐步呈现。官方称需联网问题的开始作答时间平均提前 44%，"
                "ChatGPT 周活跃用户超 12 亿——两项均为厂商自述口径，无第三方独立复测。"
                "GPT-6 模型本体此前已多次见于报道（第 35 期纳维-斯托克斯证明、第 45 期 Astra 作弊事件），"
                "本次为正式全线分发给普通用户。",
                "openai.com",
                "https://openai.com/index/gpt-6-for-everyone/",
            ),
            (
                "模型与技术进展",
                "Anthropic 发布 Claude Haiku 5.5，平均运行成本降约 75%",
                "Anthropic 10 月 7 日发布 Claude Haiku 5.5，定位高频、成本敏感任务：10 万 token 以内请求输入每百万 "
                "token 0.10 美元、输出 0.50 美元，超出部分分别为 0.50 与 2.50 美元，公司称平均运行成本较 Haiku 4.5 "
                "低约 75%（自述口径）。官方给出 OSWorld 2.1 离线子集 72.4%、Terminal-Bench 4.0 39.2%，"
                "为该系列首个支持推理强度调节的模型，同步上线 AWS、谷歌云与 Azure。"
                "第 41 期 Sonnet 5.5 发布时预告「Haiku 新版数周内发布」，本次为兑现。",
                "anthropic.com",
                "https://www.anthropic.com/claude-haiku-5-5",
            ),
            (
                "AI 与金融",
                "博通为 OpenAI 定制芯片项目筹措逾 500 亿美元融资",
                "据《华尔街日报》10 月 7 日报道，博通正为与 OpenAI 联合开发的定制 AI 芯片项目筹措逾 500 亿美元融资，"
                "已与阿波罗、黑石等机构初步接洽，资金对应数吉瓦规模算力，目标年内完成。项目内部代号 Nexus，"
                "两代芯片分别命名 Jalapeño 与 Serrano，源自双方 2025 年宣布的 10 吉瓦部署计划"
                "（Jalapeño 跑分已于 8 月 Hot Chips 披露，见前刊）。博通与 OpenAI 均未置评，谈判处于早期阶段、"
                "额度仍可能调整。与第 44/46 期的 Anthropic 芯片信贷为不同主体、不同交易。",
                "wsj.com（经中央社转述）",
                "https://www.cna.com.tw/news/ait/202610080026.aspx",
            ),
            (
                "企业应用与工具观察",
                "微软与英伟达发布 RTX Spark 平台，Windows 智能体容器正式可用",
                "10 月 7 日微软旧金山活动上，英伟达与微软公布 RTX Spark 平台：Surface Laptop Ultra 起售 2599 美元、"
                "10 月 16 日上市，顶配 128GB 统一内存，FP4 算力峰值 1 PFLOPS（厂商规格口径），紧凑型桌面主机 11 月上市。"
                "微软同时宣布 Microsoft Execution Containers 正式可用：在系统层限制智能体可访问的文件与网络范围，"
                "并按任务在本地与云端模型之间调度——把智能体运行边界写进消费级操作系统。",
                "blogs.nvidia.com",
                "https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event",
            ),
        ],
        "sections": [
            (
                "模型与技术进展",
                [
                    (
                        "开源模型",
                        "Perplexity 开源 0.6B/9B 多模态晚交互嵌入模型",
                        "10 月 7 日开源 pplx-embed-v2-late 晚交互嵌入模型，含 0.6B 与 9B 两个版本，MIT 许可、"
                        "权重上线 Hugging Face。两者共享同一嵌入空间，可用小模型查询大模型建立的索引；"
                        "文本、图像与渲染后的 PDF 页面可在同一索引内检索，无需 OCR。官方称 9B 版 MADQA 得分 92.4%"
                        "（自测），托管 API 与定价尚未公布。",
                        "perplexity.ai",
                        "https://www.perplexity.ai/hub/blog/multimodal-embeddings-beyond-a-single-vector",
                    ),
                    (
                        "开源模型",
                        "Liquid AI 开源 d1 决策模型：一次前向输出结构化判断",
                        "10 月 7 日开源 d1 系列决策模型：3B 的 d1 与额外支持音频的 d1-omni-600M。两者不生成自然语言，"
                        "而在一次前向传播中从给定选项输出结构化判断与置信度，支持 llama.cpp 本地部署。"
                        "公司称 3B 版在 RTX 4090 上单次判断约 8 毫秒（自测）；600M 版本官方标注为实验性检查点。"
                        "与第 45 期 StartLux-Decision、Intern-Decision 同属小参数决策模型赛道。",
                        "liquid.ai",
                        "https://www.liquid.ai/blog",
                    ),
                ],
            ),
            (
                "企业应用与工具观察",
                [
                    (
                        "内容检测",
                        "Google SynthID Detector 面向全球开放，支持识别合作方水印",
                        "谷歌 10 月 7 日宣布 SynthID Detector 面向全球开放：用户可上传图片、视频与音频，检测其中是否含有 "
                        "SynthID 隐形水印（界面暂为英文）。除谷歌自身内容外，也可识别 OpenAI、英伟达、Kakao 等合作方水印，"
                        "苹果支持待上线。公司称已为超过 1800 亿张图片与视频添加水印，并提示未检出不等于内容非 AI 生成——"
                        "该工具仅识别兼容水印，非通用 AI 检测器。",
                        "digitaltrends.com",
                        "https://www.digitaltrends.com/computing/googles-synthid-detector-just-launched-globally-to-help-you-spot-ai-generated-media/",
                    ),
                    (
                        "开发平台",
                        "GitHub：每三个 PR 就有一个涉及 AI 智能体，上线非结构化密钥分类器",
                        "GitHub 10 月 7 日披露，平台上每三个 pull request 就有一个涉及 AI 智能体，一年前这一比例不足十分之一"
                        "（平台自身统计口径）。同期上线与微软应用科学团队合建的 ModernBERT 分类器：在推送环节以不到两毫秒"
                        "评估整批候选密钥，可识别无固定格式的口令与内部令牌。文章称推送保护目前仅拦下约三成新检测到的密钥，"
                        "人工撤销平均耗时约 40 天。",
                        "github.blog",
                        "https://github.blog/ai-and-ml/github-copilot/secret-protection-must-scale-with-software/",
                    ),
                ],
            ),
            (
                "国内 AI 动态",
                [
                    (
                        "生态合作",
                        "字节豆包以原生应用登陆华为鸿蒙电脑",
                        "10 月 7 日，字节跳动旗下豆包以原生应用形式登陆华为鸿蒙电脑，用户可在鸿蒙应用市场直接下载。"
                        "首版内置 Doubao-Seed-2.1 Pro 与 Turbo 两个模型，分对话与工作两种模式：工作模式支持设定目标、"
                        "挂载本地文件夹、创建定时任务，并提供深度研究、PPT 生成与图像生成等能力。华为称豆包位列鸿蒙电脑"
                        "用户心愿单首位。鸿蒙 PC 应用需原生重建，AI 助手此前是鸿蒙生态的主要缺口。",
                        "pandaily.com",
                        "https://pandaily.com/bytedance-doubao-app-huawei-harmonyos-pc-doubao-seed-2-1-pro-turbo",
                    ),
                    (
                        "融资落地",
                        "Manus 母公司蝴蝶效应完成超 5 亿美元融资，博裕与 IDG 领投",
                        "10 月 8 日宣布完成超 5 亿美元（约 33.5 亿元人民币）新一轮融资：博裕投资、IDG 资本领投，"
                        "老股东腾讯、红杉中国、真格基金继续加持，为该公司 9 月 1 日宣布恢复独立运营（见前刊）后公布的首笔融资。"
                        "公司未披露估值与资金用途，称正组建团队开发面向国内市场的产品，并与国产模型厂商推进合作。",
                        "cnstock.com（上海证券报）",
                        "https://www.cnstock.com/commonDetail/799131",
                    ),
                    (
                        "早期投资",
                        "Physical AI 公司厘清智能完成天使轮系列数亿元融资，蚂蚁领投",
                        "Physical AI 基础设施公司厘清智能 10 月 8 日宣布完成天使轮系列数亿元融资：蚂蚁集团连续两轮加码并领投"
                        "天使+轮，CMC 资本、国汽投资、中金资本旗下基金、上海人工智能产业系列基金等跟投。资金将用于物理世界"
                        "数据管线、模型研发、物理仿真与跨本体适配部署系统。公司未披露具体金额与估值。",
                        "finance.sina.com.cn（新浪科技）",
                        "https://finance.sina.com.cn/tob/2026-10-08/doc-iniunvxc7644106.shtml",
                    ),
                ],
            ),
            (
                "国际 AI 动态",
                [
                    (
                        "科研合作",
                        "Biohub 扩容「虚拟生物学计划」：总投入约 18 亿美元，用 AI 预测细胞行为",
                        "扎克伯格夫妇支持的研究机构 Biohub 10 月 7 日宣布扩容虚拟生物学计划，总投入约 18 亿美元"
                        "（含资金、既有数据与算力折抵，非单一现金承诺）：谷歌 DeepMind、Isomorphic Labs 与 Meta 合计出资 "
                        "3 亿美元，美国能源部五年内投入逾 5 亿美元，国立卫生研究院提供此前逾 5 亿美元联邦资金形成的数据集。"
                        "目标是生成训练细胞行为预测模型所需的标准化数据，首个数据集预计一年内发布，商业资助方享一年独占期。",
                        "aa.com.tr（引机构公告）",
                        "https://www.aa.com.tr/en/world/zuckerberg-s-biohub-teams-with-google-us-government-in-18b-push-to-model-human-cells-with-ai/4081297",
                    ),
                ],
            ),
            (
                "AI 与金融",
                [
                    (
                        "芯片信贷",
                        "甲骨文洽谈数据中心芯片采购融资，考虑表外租赁结构",
                        "据《华尔街日报》10 月 7 日报道，甲骨文正与阿波罗、高盛等机构洽谈，为一座 1 吉瓦规模数据中心的芯片"
                        "采购安排融资：方案考虑由投资者设立独立实体购买芯片后长期租赁给甲骨文，以缓解硬件支出先行与云收入"
                        "滞后之间的资金错配，并控制自身负债规模。报道未披露金额，甲骨文希望年内完成交易，仍在接触多方。"
                        "与 9 月新墨西哥 Stargate 不可抗力通知（见前刊）为不同事件。",
                        "wsj.com（经中央社转述）",
                        "https://www.cna.com.tw/news/ait/202610080026.aspx",
                    ),
                    (
                        "芯片信贷",
                        "SpaceX 洽谈约 400 亿美元融资采购英伟达芯片",
                        "据同期报道，SpaceX 正与贷款方洽谈约 400 亿美元融资用于采购英伟达 AI 芯片：初步结构为约 100 亿美元"
                        "银行贷款加 300 亿美元投资级债券，阿波罗有望牵头，Pimco 参与讨论，预计 2027 年完成。"
                        "《金融时报》与《华尔街日报》此前已分别披露 OpenAI、Anthropic 的芯片融资安排——"
                        "芯片采购正在成为大额信贷的新标的。交易处洽谈中、条款未定。",
                        "wsj.com / ft.com（经 IBTimes UK 转述）",
                        "https://www.ibtimes.co.uk/broadcom-oracle-spacex-ai-chip-financing-1824473",
                    ),
                    (
                        "财务口径",
                        "OpenAI 披露年化营收约 500 亿美元，低于此前 700 亿口径",
                        "OpenAI 近日向投资者披露：截至 9 月底公司年化营收约 500 亿美元（未审计的运行率口径），低于上月底"
                        "市场流传的 700 亿美元。差异主要来自统计方法——Anthropic 将 AWS、谷歌云等伙伴产生的收入计入年化营收，"
                        "OpenAI 不计入。公司同时披露第三季度整体营收运行率增长 77%、企业业务增长 107%。"
                        "消息传出后 10 月 8 日甲骨文股价跌超 5%。公司未公开回应报道。",
                        "bloomberg.com（经 Livemint 转载）",
                        "https://www.livemint.com/companies/openais-revenue-run-rate-nears-50-billion-less-than-reported-11791485825829.html",
                    ),
                ],
            ),
            (
                "政策、监管与风险",
                [
                    (
                        "未成年人安全",
                        "Common Sense Media 将 ChatGPT 青少年版评为「不可接受风险」",
                        "Common Sense Media 旗下青少年 AI 安全研究所 10 月 7 日发布评估：将 ChatGPT 青少年版评为对 18 岁以下"
                        "用户的「不可接受风险」，建议 OpenAI 在修复完成前将其限定为成人使用。机构在功能上线前后共测试 4000 余条"
                        "提示，称新建关联账户未触发家长通知、危机转介漏掉逾四分之一、学习模式可被「显示答案」绕过、年龄估计"
                        "未生效。结论由儿童精神科医师专家小组评定；OpenAI 对测试方法提出异议。",
                        "commonsensemedia.org",
                        "https://commonsensemedia.org/press-releases/chatgpt-for-teens-poses-unacceptable-risk-to-kids-common-sense-media-finds",
                    ),
                    (
                        "立法草案",
                        "美众议员发布 CLAIM 法案讨论稿：智能体致害由开发者担责",
                        "众议员 Lori Trahan 10 月 7 日发布《CLAIM 法案》讨论稿，拟规定当 AI 系统造成若由人实施即构成过失、"
                        "故意侵权或犯罪的行为时，开发者承担赔偿责任；法院应推定系统具有同等情形下人的主观状态，开发者不得以 "
                        "「AI 不具备意图」抗辩。草案设联邦最低标准且不取代州法，目前为征求意见稿、尚无法案编号，无法律效力。",
                        "trahan.house.gov",
                        "https://trahan.house.gov/news/documentsingle.aspx?DocumentID=3861",
                    ),
                ],
            ),
            (
                "社媒与开发者社区观察",
                [
                    (
                        "学界动态",
                        "人类数学协会呼吁数学界停止与 OpenAI 合作，部分结果已撤回",
                        "OpenAI 10 月 6 日发布 722 份数学手稿（见第 46 期）后，由陶哲轩担任主席的人类数学协会 10 月 7 日发表声明："
                        "一次性发布 700 余份文件「不是学术展示，而是力量展示」，并呼吁数学界停止与 OpenAI 合作；声明指其忽视了"
                        "普林斯顿咨询小组关于不应在未公开内部模型上测试高深数学问题的前提。Fortune 报道称 OpenAI 已撤回至少"
                        "三项结果，结果复核仍在进行。声明全文经陶哲轩博客发布。",
                        "fortune.com",
                        "https://fortune.com/2026/10/07/openai-math-controversy-solutions-370-outstanding-challenges-published-criticisms-celebration/",
                    ),
                ],
            ),
        ],
    },
]
