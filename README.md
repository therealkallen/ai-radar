# AI Radar

AI 行业新闻雷达，每周一、三、五更新；当前页面与历史归档部署在 GitHub Pages。

## 内容与构建

阅读 [内容管道规范](AI_Radar_Content_Pipeline_Skill.md)。新闻必须先打开真实可靠来源，再核对事实、语义去重和写中文摘要。`rebuild.py` 保留现有版式，旧期的 `data_XX.py` / `gen_XX.py` 仅保留为历史素材，不再作为新刊入口。

从第 51 期开始，每期素材和证据放在 `content/issue-NNN.json`。参考第 52 期格式。日期以 UTC+8 为准；重大 claim 保留一手证据或两家独立可靠媒体。`opened_and_verified` 和编辑复核字段是实际编辑工作的记录，程序不能替代来源阅读或语义事实判断。

从第 54 期开始，必须填写 `editorial_review.domestic_review` 的 `checked_sources` 与 `notes`；国内栏目为空时另填 `empty_reason`。构建器检查记录完整性，不能证明检索充分或事实正确。实际来源范围、候选取舍及访问失败须按云端编辑任务如实记录，不设机械最低条数。

需要 Python 3.11+，无需安装依赖、令牌文件或配置固定工作区路径：

```sh
python generate.py plan                         # 列出应补的日期和连续期号
python generate.py build                        # 先校验所有素材，再生成页面与台账
python generate.py check                        # 检查已提交页面与素材是否一致
python -m unittest discover -s tests -v
python generate.py plan --require-current        # 漏刊时退出码为 1
```

`--as-of YYYY-MM-DD` 可重放某一天；例如第53期补刊后的 `plan --as-of 2026-10-25` 无缺失，尚未出版第54期时 `plan --as-of 2026-10-26` 会提示第54期。新一期必须接续上期截止日，并在下一个周一/三/五出版。重复 build 不增加重复档案，不重置期号。新来源的名称与域名须在构建器 allowlist 中有可审查的对应关系。

`bash auto-update.sh` 只构建和校验，不读取凭证、不提交也不推送。提交时应同时包含新素材、`issues/issue-NNN.html`、首页、归档列表与 `coverage.md`。构建器先暂存后替换，普通写入失败会恢复旧字节；并发构建使用 `.radar-build.lock`。进程被强制结束后，先确认没有其他构建在运行、检查工作区差异，再清理遗留锁并重建；不要盲删锁或直接发布部分文件。

## 自动化

云端编辑默认只提交一个JSON：从最新main创建 `radar/issue-NNN` 分支，通过GitHub连接器 `create_file` 直接新增 `content/issue-NNN.json` 并开PR。`Radar source PR renderer` 在首轮PR校验完成后，使用main代码构建、测试并将4个生成文件写回该PR；再显式触发现有validation工作流。必须等待**最终PR head SHA**对应的校验成功，再按用户授权合并并核验Pages。首轮因缺生成文件失败仅是中间态，不能据此宣称永久失败或直接合并JSON。完整流程及失败恢复见 [.github/radar-editor.md](.github/radar-editor.md)。

构建作业仅接受仓库所有者在同仓新分支提交的单一新增素材文件；拒绝fork、代码修改、历史覆盖和head竞态，不执行PR代码。用户已批准该作业写内容分支和调度校验所需的临时GITHUB_TOKEN权限；不需要PAT或模型API key，不自动合并main。ChatGPT Python下载artifact和搬运生成页面已退出发刊必经路径。

- `.github/workflows/validate.yml` 在 PR 和 main 更新时运行回归测试与生成一致性校验；每周一三五 10:30（UTC+8）检查漏刊。它**不生成新闻**，运行失败是需要处理的真实信号。
- 新闻研究与编辑应使用云端定时任务，指令见 [.github/radar-editor.md](.github/radar-editor.md)，建议周一三五 09:30，Asia/Singapore。需要联网工具、GitHub 连接器以及可执行 Python 的云端环境。每期提交 PR，合并后由现有 Pages 部署更新站点。
- **2026-10-25 状态：** 用户已在网页端保存并恢复云端任务，手动无缺刊试跑返回第53期已上线且未重复生成内容或PR。下一次实际新刊的云端采编与发布仍需验证；不要将无更新试跑等同于完整发刊成功。
- 在网页端创建云端定时任务后，先手动运行，核对可访问来源、完整生成及 PR 权限，再启用常规定时。遇到失败保存任务记录和日志，不以“没有新改动”掩盖抓取或推送失败。

排查证据、修复范围及补刊说明见 [docs/takeover-2026-10-22.md](docs/takeover-2026-10-22.md)。
