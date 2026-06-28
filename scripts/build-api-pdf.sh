#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PYTHON="${ROOT}/.venv/bin/python"
PIP="${ROOT}/.venv/bin/pip"
PLAYWRIGHT="${ROOT}/.venv/bin/playwright"

if [[ ! -x "$PYTHON" ]]; then
  echo "Missing virtualenv at .venv — create one first:" >&2
  echo "  python -m venv .venv && .venv/bin/pip install -r requirements-dev.txt" >&2
  exit 1
fi

"$PIP" install -q -r requirements-dev.txt
"$PLAYWRIGHT" install chromium
exec "$PYTHON" scripts/build_api_pdf.py "$@"
