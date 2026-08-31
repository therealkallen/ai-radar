# -*- coding: utf-8 -*-
"""第 31 期真实新闻素材（2026.08.28 — 08.31，周一窗口）。

按《AI Radar Content Pipeline Skill》规范生成（2026-08-31）。
说明：本期为周一更新，覆盖「上周五更新（第 30 期，8.26–8.28）之后 → 当前」的窗口，
其中 8/28 当天数条重大新闻（Hy4、Gemini Omni、五角大楼裁定、Cursor 断供、AWS 采购）
因第 30 期未收录，本期一并补入，并叠加 8/29–8/31 的新进展。

来源纪律（Source-First / Allowlist 约束）：
- 每条新闻均经 WebSearch/WebFetch 实际检索并核实来源页面，给出完整 canonical URL。
- 最终来源（final source）全部落在 Skill Allowlist 内：
  国际/国内 Primary Source：tencent.com、deepmind.google、openai.com；
  国际 Trusted Media：reuters.com、techcrunch.com、bloomberg.com；
  中文 Trusted Media：tmtpost.com。
- 未被 Allowlist 收纳的线索源（aistart.ai、n8nlab.io、aibreakingwire.com、genaidaily.com、
  thecodew.com、10news.xyz、aitoolsrecap.com、xiaoyuzhoufm.com 等聚合/搬运站）仅用于发现，
  最终 canonical 一律指向上述官方或权威原始来源。
- 语义去重（对照 coverage.md）：本期权目均未在第 30 期及更早各期作为独立条目出现
  （第 30 期含 Hugging Face 自主入侵复盘、Nvidia 收购 HF、Nscale 算力、Nvidia Q2 等，
  与本期各事件均为不同事实，不构成重复）。
- 摘要均中性、80–150 字，禁用「重磅/炸裂/史诗级/颠覆/遥遥领先」等夸大词。
- Radar Picks 由全部 canonical story 按重要性选取 4 条。
- 「AI 与金融」条目显式标注 FINANCE_ANGLE。
"""

ISSUES = [

{
 "num": 31,
 "date": "2026.08.28 — 08.31",
 # Radar Picks：从全部 canonical story 中按重要性选取 4 条
 "picks": [
  ("国内 AI 动态", "腾讯混元开源 Hy4 Preview：770B MoE、1M 上下文、Apache 2.0",
   "8 月 28 日，腾讯混元发布并开源新一代旗舰大模型 Hy4 Preview：MoE 架构，总参数 770B、激活 49B，上下文窗口突破 1M tokens，采用 Apache 2.0 许可。内部 163 名专家、203 个工程任务盲测中得分 2.99/4.00，略优于 GLM-5.3（2.92）与 Kimi K3（2.94）；模型已接入 WorkBuddy/CodeBuddy、元宝、ima，并可通过腾讯云 TokenHub 与 OpenRouter 调用 API。",
   "tencent.com", "https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/"),

  ("模型与技术进展", "Google 发布 Gemini Omni 1.1 Flash：视频续写至 40 秒、支持 4K 与首尾帧",
   "Google DeepMind 发布 Gemini Omni 1.1 Flash，面向开发者提供更可控的生成视频能力：可将片段续写至累计 40 秒，支持首尾帧控制与运镜，360p 草稿模式渲染快约 60%、成本约 720p 的三分之一，成片可放大至 4K，并带 SynthID 水印。模型已通过 Gemini API、AI Studio 与 Gemini Enterprise Agent Platform 开放。",
   "deepmind.google", "https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control"),

  ("政策、监管与风险", "联邦法官裁定五角大楼将 Anthropic 列为供应链风险「非法且毫无根据」",
   "据路透社，美国加州北区联邦法官 Rita Lin 于 8 月 27 日裁定，五角大楼以「供应链风险」封禁 Anthropic 的决定属「非法且毫无根据」，构成对第一修正案的报复、并违反第五修正案正当程序。裁定源于 Anthropic 拒绝为自主武器与大规模监控开放 Claude 安全护栏。政府预计将上诉，Anthropic 另一起相关诉讼仍在华盛顿特区审理。",
   "reuters.com", "https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28/"),

  ("国际 AI 动态", "AWS 追加部署 200 万块英伟达 GPU（2027–28），总承诺超 300 万",
   "据 TechCrunch，AWS 与英伟达在英伟达二季度财报电话会上宣布扩大合作：AWS 将在 2027–2028 年追加部署 200 万块英伟达 GPU（Blackwell Ultra、Rubin、Rubin Ultra），叠加 3 月承诺后总规模超 300 万块；协议还涵盖 Vera CPU、NVLink Fusion 网络与物理 AI 机器人栈。英伟达将供应链义务扩至 2790 亿美元，需求超出预期。",
   "techcrunch.com", "https://techcrunch.com/?p=3110724"),
 ],

 # 八个栏目，顺序遵循规范 §2
 "sections": [
  ("模型与技术进展", [
    ("视频", "Google 发布 Gemini Omni 1.1 Flash：视频续写至 40 秒、支持 4K 与首尾帧",
     "Google DeepMind 发布 Gemini Omni 1.1 Flash，面向开发者提供更可控的生成视频能力：可将片段续写至累计 40 秒，支持首尾帧控制与运镜，360p 草稿模式渲染快约 60%、成本约 720p 的三分之一，成片可放大至 4K，并带 SynthID 水印。模型已通过 Gemini API、AI Studio 与 Gemini Enterprise Agent Platform 开放。",
     "deepmind.google", "https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control"),

    ("产品", "OpenAI 停用 ChatGPT 官方 DALL·E GPT（8/30 生效），图像生成由 ChatGPT Images 承接",
     "据 OpenAI 帮助中心版本说明，ChatGPT 中的官方 DALL·E GPT 已于 8 月 30 日停用，用户被建议在停用前下载所需图像；图像生成功能由 ChatGPT Images（基于 gpt-image-1 系列）承接，覆盖全部套餐，启用图像生成的自定义 GPT 不受影响。这延续了 OpenAI 围绕新模型整合产品的清理动作（本月 o3、ChatGPT Atlas 亦陆续下线）。",
     "openai.com", "https://help.openai.com/zh-hans-cn/articles/6825453-chatgpt-%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E"),
  ]),

  ("企业应用与工具观察", [
    ("开发工具", "OpenAI 切断 Cursor 模型供应：SpaceX 收购触发变更控制权条款，拟定 11/12 断供",
     "据钛媒体，OpenAI 于 8 月 28 日通知 SpaceX，拟终止向 Cursor 提供模型的合同，拟定 11 月 12 日断供，期间不再提供未来模型。触发原因为 SpaceX 以 600 亿美元收购 Cursor 母公司 Anysphere 触发的「变更控制权」条款；OpenAI 称无法确信马斯克旗下公司遵守服务条款。Cursor 联合创始人 Michael Truell 称双方仍在沟通，Anthropic 表示将增加 Cursor 上 Claude 的算力支持。",
     "tmtpost.com", "https://www.tmtpost.com/8121865.html"),
  ]),

  ("国内 AI 动态", [
    ("模型", "腾讯混元开源 Hy4 Preview：770B MoE、1M 上下文、Apache 2.0",
     "8 月 28 日，腾讯混元发布并开源新一代旗舰大模型 Hy4 Preview：MoE 架构，总参数 770B、激活 49B，上下文窗口突破 1M tokens，采用 Apache 2.0 许可。内部 163 名专家、203 个工程任务盲测中得分 2.99/4.00，略优于 GLM-5.3（2.92）与 Kimi K3（2.94）；模型已接入 WorkBuddy/CodeBuddy、元宝、ima，并可通过腾讯云 TokenHub 与 OpenRouter 调用 API。",
     "tencent.com", "https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/"),
  ]),

  ("国际 AI 动态", [
    ("算力", "AWS 追加部署 200 万块英伟达 GPU（2027–28），总承诺超 300 万",
     "据 TechCrunch，AWS 与英伟达在英伟达二季度财报电话会上宣布扩大合作：AWS 将在 2027–2028 年追加部署 200 万块英伟达 GPU（Blackwell Ultra、Rubin、Rubin Ultra），叠加 3 月承诺后总规模超 300 万块；协议还涵盖 Vera CPU、NVLink Fusion 网络与物理 AI 机器人栈。英伟达将供应链义务扩至 2790 亿美元，需求超出预期。",
     "techcrunch.com", "https://techcrunch.com/?p=3110724"),
  ]),

  ("AI 与金融", [
    ("融资", "Nvidia 支持的 Lambda 募资 10 亿美元私募短债采购 GPU 租给微软",
     "据彭博社，AI 云厂商 Lambda（英伟达支持）通过 JPMorgan 安排的私募短债募资约 10 亿美元，用于采购英伟达 GPU 并租给微软，为其本月第二笔债务融资（上笔 9.26 亿美元）。彭博统计 2026 年全球 AI 相关债务发行已超 4000 亿美元，反映出新云厂商以债务而非股权支撑算力扩张的趋势，亦引发监管对抵押品披露与流动性的关注。FINANCE_ANGLE：AI 基建债务融资与抵押品风险。",
     "bloomberg.com", "https://origin.www.bloomberg.com/news/articles/2026-08-28/nvidia-backed-lambda-inks-1-billion-private-debt-for-chip-deal"),
  ]),

  ("政策、监管与风险", [
    ("判例", "联邦法官裁定五角大楼将 Anthropic 列为供应链风险「非法且毫无根据」",
     "据路透社，美国加州北区联邦法官 Rita Lin 于 8 月 27 日裁定，五角大楼以「供应链风险」封禁 Anthropic 的决定属「非法且毫无根据」，构成对第一修正案的报复、并违反第五修正案正当程序。裁定源于 Anthropic 拒绝为自主武器与大规模监控开放 Claude 安全护栏。政府预计将上诉，Anthropic 另一起相关诉讼仍在华盛顿特区审理。",
     "reuters.com", "https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28/"),

    ("版权", "索尼音乐、华纳查普尔起诉 Anthropic 盗用版权音乐训练 Claude",
     "据 TechCrunch，索尼音乐出版公司与华纳查普尔等出版商于 8 月 28 日向加州北区联邦法院起诉 Anthropic，指控其通过盗版、抓取与下载数万首歌词与曲谱用于训练 Claude，CEO Dario Amodei 与联合创始人 Benjamin Mann 同为被告，每首作品索赔最高 15 万美元。Anthropic 表示将「有力抗辩」。该案紧接其 15 亿美元作者版权和解之后。",
     "techcrunch.com", "https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/"),
  ]),

  ("社媒与开发者社区观察", [
  ]),
 ]
}

]
