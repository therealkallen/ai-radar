#!/bin/bash
# AI Radar 自动更新脚本
# 搜索最新 AI 新闻 → 生成 HTML → 推送到 GitHub Pages

TOKEN_FILE="/root/.config/ai-radar/gh_token"
REPO_DIR="/workspace/ai-radar"

if [ ! -f "$TOKEN_FILE" ]; then
  echo "Error: Token file not found" >&2
  exit 1
fi

GH_TOKEN=$(cat "$TOKEN_FILE" | tr -d '\n')
cd "$REPO_DIR"

# 拉取最新远程状态避免冲突
git pull origin main

# HTML 已经由 AI agent 在工作区生成好了
# 下面只是推送到 GitHub
git add index.html
git commit -m "chore: auto-update AI Radar $(date +%Y.%m.%d)" || true
git push https://therealkallen:${GH_TOKEN}@github.com/therealkallen/ai-radar.git main
