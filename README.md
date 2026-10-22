# AI Radar

AI 行业新闻雷达，每周一、三、五更新；当前页面与历史归档部署在 GitHub Pages。

## 内容与构建

阅读 [内容管道规范](AI_Radar_Content_Pipeline_Skill.md)。新闻必须先打开真实可靠来源，再核对事实、语义去重和写中文摘要。`rebuild.py` 保留现有版式，旧期的 `data_XX.py` / `gen_XX.py` 仅保留为历史素材，不再作为新刊入口。

从第 51 期开始，每期素材和证据放在 `content/issue-NNN.json`。参考第 52 期格式。日期以 UTC+8 为准；重大 claim 保留一手证据或两家独立可靠媒体。`opened_and_verified` 和编辑复核字段是实际编辑工作的记录，程序不能替代来源阅读或语义事实判断。

需要 Python 3.11+，无需安装依赖、令牌文件或配置固定工作区路径：

```sh
python generate.py plan                         # 列出应补的日期和连续期号
python generate.py build                        # 先校验所有素材，再生成页面与台账
python generate.py check                        # 检查已提交页面与素材是否一致
python -m unittest discover -s tests -v
python generate.py plan --require-current        # 漏刊时退出码为 1
```

`--as-of YYYY-MM-DD` 可重放某一天；例如补刊后的 `--as-of 2026-10-22` 无缺失，`--as-of 2026-10-23` 应提示第 53 期。新一期必须接续上期截止日，并在下一个周一/三/五出版。重复 build 不增加重复档案，不重置期号。新来源的名称与域名须在构建器 allowlist 中有可审查的对应关系。

`bash auto-update.sh` 只构建和校验，不读取凭证、不提交也不推送。提交时应同时包含新素材、`issues/issue-NNN.html`、首页、归档列表与 `coverage.md`。构建器先暂存后替换，普通写入失败会恢复旧字节；并发构建使用 `.radar-build.lock`。进程被强制结束后，先确认没有其他构建在运行、检查工作区差异，再清理遗留锁并重建；不要盲删锁或直接发布部分文件。

## 自动化

- `.github/workflows/validate.yml` 在 PR 和 main 更新时运行回归测试与生成一致性校验；每周一三五 10:30（UTC+8）检查漏刊。它**不生成新闻**，运行失败是需要处理的真实信号。
- 新闻研究与编辑应使用云端定时任务，指令见 [.github/radar-editor.md](.github/radar-editor.md)，建议周一三五 09:30，Asia/Singapore。需要联网工具、GitHub 连接器以及可执行 Python 的云端环境。每期提交 PR，合并后由现有 Pages 部署更新站点。
- **当前状态：云端任务尚未激活，未完成首次云端试跑。** 当前 PR 合入后，校验工作流才会在 main 上定时运行。不要把仅有校验工作流或本地定时器视为云端新闻自动化已启用。
- 在网页端创建云端定时任务后，先手动运行，核对可访问来源、完整生成及 PR 权限，再启用常规定时。遇到失败保存任务记录和日志，不以“没有新改动”掩盖抓取或推送失败。

排查证据、修复范围及补刊说明见 [docs/takeover-2026-10-22.md](docs/takeover-2026-10-22.md)。
