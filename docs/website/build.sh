#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

# Use a local virtualenv by default; CI or managed environments can use
# WEBSITE_NO_VENV=1 after installing docs/website/requirements.txt themselves.
if [[ "${WEBSITE_NO_VENV:-0}" != "1" ]]; then
  if [[ ! -x "${ROOT}/.venv/bin/python" ]]; then
    "${PYTHON}" -m venv "${ROOT}/.venv"
  fi
  PYTHON="${ROOT}/.venv/bin/python"
  "${PYTHON}" -m pip install --disable-pip-version-check -q -r "${ROOT}/requirements.txt"
fi

exec "${PYTHON}" "${ROOT}/build.py" "$@"
