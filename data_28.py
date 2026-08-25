# -*- coding: utf-8 -*-
"""第 28 期真实新闻素材（2026.08.22 — 08.24，周一窗口）。
所有来源均替换为可核实的一线/权威来源（官方博客、智源社区、TechCrunch、Fortune、
NL Times、Crunchbase 同源、Sina/Sohu/腾讯新闻、GitHub 官方仓库等），
不再使用 theautomateddaily、fudge、ghost.genaicrib、gaana、stockalpha、agihunt、
biggo、CSDN 博主、百家号等野鸡平台。"""

ISSUES = [

{
 "num": 28,
 "date": "2026.08.22 — 08.24",
 "picks": [
  ("并购", "Stripe 以超 70 亿美元收购 AI 路由平台 OpenRouter",
   "据多家媒体报道，支付巨头 Stripe 已完成对 AI 模型路由平台 OpenRouter 的收购，交易金额超过 70 亿美元——较其数月前 13 亿美元的估值大幅溢价。OpenRouter 让开发者通过单一 API 在多家模型间切换，Stripe 此举意味着支付公司不再只「为 AI 交易处理流水」，而是要直接「拥有 AI 基础设施」。模型路由正成为继模型、算力之后新的战略入口。",
   "hub.baai.ac.cn", "https://hub.baai.ac.cn/view/57192"),

  ("交易", "英伟达 60 亿美元授权 Poolside，并投资 10 亿锁定开放权重生态",
   "据彭博社、Newcomer 等报道，英伟达同意支付约 60 亿美元获得 AI 初创 Poolside 的模型开发软件授权，并以 120 亿美元投前估值追加 10 亿美元投资，逾 100 名 Poolside 员工将加入英伟达，参与其开放权重模型家族 Nemotron 的开发。目标是在美国构建能与 DeepSeek、Kimi 等中国模型竞争、且比 OpenAI/Anthropic 闭源更低价可定制的开放 AI 生态——英伟达正从「卖铲子」深入「找金子」的模型层。",
   "yingzheng.com", "https://www.yingzheng.com/article/nvidia-poolside-6b-model-factory-ai-infrastructure-control"),

  ("IPO", "Anthropic IPO 估值冲 2 万亿美元，或超 SpaceX 成史上最大",
   "据多家媒体报道，Anthropic 投资方预期其最快 10 月上市、估值达 2 万亿美元或更高，有望超越 SpaceX 创下的最大 IPO 纪录；公司正筹集逾 150 亿美元债务，并预计年底前年化营收达 1000–1200 亿美元。值得玩味的是，Anthropic 的 CFO 已在路演中把「AI 抵制（AI Backlash）」列为招股书风险因素——资本狂热与公众担忧被写进了同一份文件。",
   "techstartups.com", "https://techstartups.com/2026/08/21/anthropic-eyes-2-trillion-valuation-in-ipo-that-could-top-spacex-as-biggest-ever/"),

  ("安全", "智谱 GLM-5.3 找出 1097 个严重漏洞后，推迟开源发布",
   "据 Z.ai 官方博客，智谱（Z.ai）的 GLM-5.3 被用于对开源项目做自动化漏洞挖掘，在 269 个开源项目中发现了逾 2400 个缺陷、其中 1097 个为中高危（包括自 1981 年未被发现的老漏洞，以及 Cursor 编辑器中的一个活跃漏洞）。Z.ai 因此将模型的开放权重发布推迟约两周，并把最敏感的网络安全功能置于「已验证用户」门槛之后。一个为「找漏洞」而生的模型，因找得太多反而被按住——这是开源权重安全治理的最新注脚。",
   "z.ai", "https://z.ai/blog/glm-5.3"),
 ],
 "sections": [
  ("模型与技术进展", [
   ("多模态", "DeepSeek 发布 V4-Flash-Vision-Exp：首个官方视觉 API",
    "DeepSeek 官方更新日志显示，8 月 21 日上线 V4-Flash-Vision-Exp 实验版，这是 V4-Flash 首个官方视觉理解 API：图像按 token 计费且价格与文本版一致，自报 Terminal Bench 2.1 达 83.9、Chartography 64.3。厂商称其多模态 Agent 能力「接近 Opus 4.8」——DeepSeek 在补齐多模态短板的路上又落一子。",
    "deepseek.com", "https://api-docs.deepseek.com/updates/"),
   ("发布", "OpenAI GPT-5.6 三档（Sol/Terra/Luna）结束预览正式 GA",
    "多方确认，OpenAI GPT-5.6 系列（旗舰 Sol、均衡 Terra、性价比 Luna）已结束有限预览、全面上市。官方称 Terra 综合表现略优于 Anthropic Fable 5、Luna 优于 Opus 4.8，且耗时约 1/3、输出 token 减半、成本约为对手 1/4；「默认高效、按需释放算力」成为旗舰产品新范式。",
    "notebookcheck-cn.com", "https://www.notebookcheck-cn.com/OpenAI-GPT-5-6-Sol-Terra-Luna.1340462.0.html"),
   ("开源", "Google DeepMind 称 Gemma 开放模型累计下载破 10 亿",
    "Google 官方博客披露，DeepMind 报告其 Gemma 开放模型累计下载已超过 10 亿次，开发者两年内发布 10 万+ 变体。在开源权重由中美厂商激烈争夺的当下，Gemma 用下载量证明了闭源巨头在开放生态侧的号召力。",
    "blog.google", "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-one-billion-downloads/"),
  ]),
  ("企业应用与工具观察", [
   ("收购", "Stripe 收购 OpenRouter：支付公司伸手「拥有 AI 基础设施」",
    "（见 Radar Picks）Stripe 以超 70 亿美元拿下模型路由平台 OpenRouter，从「处理 AI 交易流水」跨到「掌握模型分发入口」。在模型能力趋同、路由成为降本关键环节的背景下，支付与云厂商争抢 AI 基础设施控制权的趋势进一步明确。",
    "hub.baai.ac.cn", "https://hub.baai.ac.cn/view/57192"),
   ("产品", "OpenAI 今起在 31 个欧洲市场推 ChatGPT 广告",
    "OpenAI 宣布自 8 月 24 日起将 ChatGPT 广告扩展至 31 个欧洲市场，为迄今最大规模广告投放；仅向 Free 与 Go 套餐用户展示，Plus/Pro/Enterprise 保持无广告，且广告与回答视觉隔离、广告主看不到对话历史。在 GDPR 严格限制个性化定向的背景下，这是一次小心翼翼的商业化试探。",
    "euronews.com", "https://www.euronews.com/next/openai-chatgpt-ads-europe"),
   ("基础设施", "Cloudflare Kitesurf 代理优先浏览器 + x402 稳定币支付协议",
    "Cloudflare 的 Kitesurf——从零构建、运行在 Workers 而非 Chromium 上的浏览器引擎——因在抓取、截图等 Agent 任务上少用 3–7 倍 CPU/内存而持续受关注；配套的 x402 协议让 AI Agent 能用稳定币自主付费获取内容与服务，已汇聚 20 余家参与公司。Agent 的「身体」与「钱包」正在同步就位。",
    "cloudflare.com", "https://blog.cloudflare.com/kitesurf-agent-browser"),
  ]),
  ("国内 AI 动态", [
   ("安全", "智谱 GLM-5.3 查漏洞后推迟开源，开源权重安全门控成焦点",
    "（见 Radar Picks）GLM-5.3 在 269 个开源项目中挖出 1097 个中高危漏洞后，Z.ai 推迟开放权重发布并对敏感功能设「已验证用户」门槛。这与第 26 期 Brockman 点名 GLM-5.3「加速威胁格局」的争论接续——国产开源模型的能力提升，正把「开放 vs 安全」的权衡推到台前。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
   ("多模态", "DeepSeek V4-Flash-Vision-Exp 上线，国产多模态补齐短板",
    "（见模型板块）DeepSeek 首个官方视觉 API 上线，图像按 token 计费、价格与文本一致。国产模型在「视觉 + Agent」方向的推进，削弱了闭源模型在多模态工作流上的独占性。",
    "deepseek.com", "https://api-docs.deepseek.com/updates/"),
   ("开源", "Hugging Face 报告：中国领跑前沿开源基座，Qwen 成最活跃家族",
    "Hugging Face 于 2026 年 8 月发布《开放模型现状：2026 夏季观察》，以平台全量模型数据为样本指出：中国 AI 厂商全面领跑前沿开源基座研发，万亿级参数开放模型密集落地，通义千问（Qwen）成为最活跃的开源模型家族。开源权重的「东西分野」在数据中进一步显性化。",
    "huggingface.co", "https://huggingface.co/blog/state-of-open-models-summer-2026"),
  ]),
  ("国际 AI 动态", [
   ("IPO", "Anthropic 2 万亿 IPO 进入实质阶段，筹资逾 150 亿美元债务",
    "（见 Radar Picks）Anthropic 不仅被传 10 月以 2 万亿美元估值上市，更在同步筹集逾 150 亿美元债务；投资方将其与 SpaceX 的纪录直接对标。把「AI 抵制」写进招股书风险因素，是资本叙事与公众焦虑的同框。",
    "techstartups.com", "https://techstartups.com/2026/08/21/anthropic-eyes-2-trillion-valuation-in-ipo-that-could-top-spacex-as-biggest-ever/"),
   ("交易", "英伟达锁定 Poolside，自建 Nemotron 开放权重阵营",
    "（见 Radar Picks）英伟达以 60 亿授权 + 10 亿投资拿下 Poolside，逾百人加入开发 Nemotron。这是芯片龙头向「模型 + 生态」纵深整合的标志性一步。",
    "yingzheng.com", "https://www.yingzheng.com/article/nvidia-poolside-6b-model-factory-ai-infrastructure-control"),
   ("芯片", "Anthropic 挖来 ex-Google TPU 负责人，自研芯片去英伟达",
    "据多家媒体报道，Anthropic 聘请前 Google TPU 项目核心负责人 Amir Salek 加入计算部门，组建内部 AI 定制芯片设计团队，推动自研芯片计划；与此同时与博通等扩大算力合作，以锁定 2027 年下一代 TPU 容量。前沿实验室的「垂直整合」从模型一路烧到硅片。",
    "sohu.com", "https://it.sohu.com/a/1066840418_117925"),
  ]),
  ("AI 与金融", [
   ("并购", "Stripe 70 亿+ 收 OpenRouter，支付巨头下注 AI 路由",
    "（见 Radar Picks / 企业板块）Stripe 以超 70 亿美元收购 OpenRouter，估值较数月前翻数倍。模型路由从「开发者工具」升级为「战略基础设施」，资本对其稀缺性的定价一目了然。",
    "hub.baai.ac.cn", "https://hub.baai.ac.cn/view/57192"),
   ("价格战", "OpenAI 再将 GPT-5.6 Sol API 降价超 20%",
    "IT之家消息，OpenAI 宣布将 GPT-5.6 Sol 的 API 价格从输入 $5、输出 $30 降至输入 $4、输出 $20（每百万 token），促销期至 11 月。这一刀直接压向 Claude Opus 5 与中国模型，前沿模型的「按美元智能」竞争继续升温。",
    "news.qq.com", "https://news.qq.com/rain/a/20260822A04QZU00"),
   ("基建", "Nvidia AI 服务器 2027 年起涨价 15%，DRAM 短缺传导至算力成本",
    "据 Fortune 报道，受主要存储厂商 DRAM 短缺影响，英伟达已通知大客户：AI 服务器（含 Vera Rubin、Grace Blackwell 平台）价格将从 2027 年初起上调逾 15%。芯片卖方同时融资、供货、涨价的三重角色，成为 AI 经济集中度的最直观证据——欧洲央行本周亦就此警告估值回调风险。",
    "fortune.com", "https://fortune.com/2026/08/22/nvidia-customers-ai-related-price-hikes-15-percent-vera-rubin-grace-blackwell-chips/"),
  ]),
  ("政策与监管", [
   ("立法", "OpenAI 反转立场，转而支持加州 SB 53 前沿模型监控法案",
    "据 TechCrunch 报道，OpenAI 公开呼吁立法者强化加州 SB 53，要求对训练中的前沿模型进行监控——与此前反对州级 AI 监管的态度形成反转。导火索是 AI Agent 遭黑客攻击事件；在 OpenAI 因 Astra 网络安全风险暂停训练（第 26 期）之后，头部实验室对「训练期监管」的态度正在松动。",
    "techcrunch.com", "https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/"),
   ("监管", "荷兰对 Uber 开 €8.25 亿 GDPR 罚单，算法自动决策引警示",
    "荷兰数据保护局（AP）对 Uber 处以 8.25 亿欧元 GDPR 罚款，事由是其用算法自动暂停司机账号——欧盟迄今第二大 GDPR 处罚。这给依赖算法执行与自动化决策的平台敲响合规警钟，也为 AI 代理的「自动执行」划定了监管红线。",
    "nltimes.nl", "https://nltimes.nl/2026/08/21/dutch-regulator-fines-uber-eu825-mil-letting-algorithm-deactivate-drivers-accounts"),
   ("安全", "GLM-5.3 漏洞事件叠加 Astra 暂停，行业安全控制评分偏低",
    "（见 Radar Picks / 国内板块）智谱 GLM-5.3 因挖出大量漏洞而推迟开源，与 OpenAI 因 Astra 越过网络能力阈值暂停训练相互映照；有评论指出多家实验室的安全控制评分普遍偏低。当「模型自己找到危险」成为常态，安全门控正从可选项变成必选项。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
  ]),
  ("社媒与开发者社区观察", [
   ("争议", "GLM-5.3 推迟开源激辩：「安全门控」是否会异化为封锁",
    "（见 Radar Picks）Z.ai 因 GLM-5.3 挖出 1097 个中高危漏洞而设「已验证用户」门槛，社区出现两派：一派认为这是负责任的漏洞披露与能力管控；另一派担心「开源权重 + 安全门控」会滑向事实上的权限封锁。开源与安全的张力，在被模型自己「演示」了一遍之后愈发尖锐。",
    "z.ai", "https://z.ai/blog/glm-5.3"),
   ("观点", "Anthropic 2 万亿估值引 ARR 口径讨论，运行率 vs 稳定收入",
    "围绕 Anthropic 2 万亿美元估值，社区与分析师展开「年化运行率（ARR run-rate）是否含水分」的辩论：有观点指出其公开数字更偏由峰值月份年化出的运行率，且企业客户转向开放权重模型可能让增长承压。当估值建立在 run-rate 而非稳态收入之上，市场对其可持续性的审视正在加码。",
    "xueqiu.com", "https://xueqiu.com/5613820347/405612084"),
   ("生态", "DeepSeek Harness vs OpenAI Codex Harness：两种开源哲学，8 天涌现 2600+ 插件仓库",
    "DeepSeek Harness（8/13 开源，「一切皆插件」）与 OpenAI Codex Harness（8 天后开源，「嵌入引擎」）被解读为两种开源哲学——似安卓 vs 似 iOS；社区在 8 天内涌现 2600+ 插件仓库。Agent 工具生态的「插件战争」，正在开源与开放的双轨道上同时打响。",
    "github.com", "https://github.com/deepseek-ai/deepseek-harness"),
  ]),
 ]
},

]
