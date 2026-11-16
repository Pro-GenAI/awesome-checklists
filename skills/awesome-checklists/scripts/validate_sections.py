#!/usr/bin/env python3
"""Verify checklist headings and GitHub-style local Markdown section anchors.

This is a structural test, not external URL validation or a safety audit.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote

REQUIRED = ("Release gate", "Trusted references and scope")
SOURCE_DATE = re.compile(r"^\*\*Source review date:\*\* \d{4}-\d{2}-\d{2}\b", re.MULTILINE)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
INLINE_LINK = re.compile(r"!?\[([^\]]+)\]\([^)]+\)")
HTML_TAG = re.compile(r"<[^>]+>")
CODE_FENCE = re.compile(r"^\s*(\x60{3,}|~{3,})")


def headings(text: str) -> list[tuple[int, str]]:
    found = []
    fence = None
    for line in text.splitlines():
        m = CODE_FENCE.match(line)
        if m:
            marker = m.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence:
            continue
        h = HEADING.match(line)
        if h:
            found.append((len(h.group(1)), h.group(2).strip()))
    return found


def slug(value: str) -> str:
    value = INLINE_LINK.sub(lambda m: m.group(1), value)
    value = HTML_TAG.sub("", value)
    value = re.sub(r"[\x60*~]", "", value)
    value = unicodedata.normalize("NFKC", value).lower().strip()
    value = "".join(ch for ch in value if ch.isalnum() or ch in (" ", "-", "_"))
    return re.sub(r"\s+", "-", value)


def anchors(text: str) -> set[str]:
    used = Counter()
    ids = set()
    for _, title in headings(text):
        raw = slug(title)
        suffix = used[raw]
        used[raw] += 1
        ids.add(raw if suffix == 0 else f"{raw}-{suffix}")
    ids.update(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', text, re.IGNORECASE))
    return ids


def source_structure(path: Path, content: str, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    h = headings(content)
    h2 = Counter(title for level, title in h if level == 2)
    failures = []
    for required in REQUIRED:
        if h2[required] != 1:
            failures.append(f"{rel}: expected exactly one ## {required}, found {h2[required]}")
    dates = [i for i, line in enumerate(content.splitlines()) if SOURCE_DATE.match(line)]
    if len(dates) != 1:
        failures.append(f"{rel}: expected exactly one dated source review line")
    elif any(line.strip() for line in content.splitlines()[dates[0] + 1:]):
        failures.append(
            f"{rel}: source review date must be the last nonblank line; "
            "move links and optional tools above the date or into references"
        )
    seq = [title for level, title in h if level == 2]
    if all(t in seq for t in REQUIRED) and seq.index(REQUIRED[0]) >= seq.index(REQUIRED[1]):
        failures.append(f"{rel}: Release gate must precede Trusted references and scope")
    return failures


def check_fragment(root: Path, source: Path, target: Path, fragment: str) -> str | None:
    if not fragment or target.suffix.lower() != ".md":
        return None
    fragment = unquote(fragment)
    if re.fullmatch(r"L\d+(?:-L\d+)?", fragment):
        return None
    try:
        content = target.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return f"{source.relative_to(root)}: unreadable Markdown link target {target}"
    if fragment in anchors(content):
        return None
    return f"{source.relative_to(root)}: missing Markdown section #{fragment} in {target.relative_to(root)}"
