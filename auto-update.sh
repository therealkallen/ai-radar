#!/usr/bin/env bash
# Build verified records. The scheduled editor submits the result as a PR.
set -euo pipefail
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
"$PYTHON" "$REPO_DIR/generate.py" build "$@"
"$PYTHON" "$REPO_DIR/generate.py" check "$@"
echo 'Build and validation passed. Submit content/, HTML and coverage.md together through a reviewed PR.'
