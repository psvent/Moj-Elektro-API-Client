#!/bin/sh
# Shared test runner for Git hooks.

set -euo pipefail

HOOK_NAME="${1:-hook}"
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

if command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON="python"
else
    echo "No python interpreter found; cannot run tests." >&2
    exit 1
fi

echo "Running tests (pytest) before $HOOK_NAME..."
if ! "$PYTHON" -m pytest; then
    echo "Tests failed. $HOOK_NAME aborted." >&2
    exit 1
fi

echo "Tests passed."
