#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Warn/fail on archived GitHub repositories referenced by the curated entry points.

Only scans README and drop-in lists; full canonical sources have their own advisory link audit.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")


def main() -> int:
    if not TOKEN:
        print("GH_TOKEN not set: skipping API archive checks (CI provides a token)")
        return 0
    paths = [ROOT / "README.md", *sorted((ROOT / "checklists").glob("*.md"))]
    refs: dict[str, list[str]] = {}
    for path in paths:
        content = path.read_text(encoding="utf-8")
        for owner, name in PATTERN.findall(content):
            full = owner + "/" + name.rstrip(".,)")
            refs.setdefault(full, []).append(str(path.relative_to(ROOT)))
    archived = []
    failures = []
    for full, sources in sorted(refs.items()):
        request = Request(
            "https://api.github.com/repos/" + full,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer " + TOKEN,
                "User-Agent": "awesome-checklists-archive-audit",
            },
        )
        try:
            with urlopen(request, timeout=15) as response:
                data = json.load(response)
            if data.get("archived"):
                archived.append(full)
                print(f"::warning title=Archived upstream::{full} referenced in {', '.join(sorted(set(sources)))}")
        except HTTPError as exc:
            failures.append(f"{full}: HTTP {exc.code}")
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            failures.append(f"{full}: {exc}")
    for failure in failures:
        print("::warning title=Archive-check incomplete::" + failure)
    print(f"Checked {len(refs)} GitHub repositories; archived={len(archived)}; lookup errors={len(failures)}")
    return 1 if archived or failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
