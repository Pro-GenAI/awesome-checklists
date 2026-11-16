#!/usr/bin/env python3
"""Sanity-check generated pages, SEO files, and the Markdown inventory."""
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

import build


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = False
        self.description = False
        self.canonical = False
        self.schema = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        self.title |= tag == "title"
        self.description |= tag == "meta" and data.get("name") == "description" and bool(data.get("content"))
        self.canonical |= tag == "link" and data.get("rel") == "canonical" and bool(data.get("href"))
        self.schema |= tag == "script" and data.get("type") == "application/ld+json"


def main() -> None:
    output = build.WEBSITE_DIR / "dist"
    sources = build.all_sources()
    expected = {build.output_path(p) for p in sources}
    expected.update(Path(scope) / "index.html" for scope in build.SCOPES[1:])
    present = {p.relative_to(output) for p in output.rglob("*.html")}
    assert expected == present, f"Missing: {expected - present}; unexpected: {present - expected}"
    for path in present:
        parser = HeadParser()
        parser.feed((output / path).read_text(encoding="utf-8"))
        assert all((parser.title, parser.description, parser.canonical, parser.schema)), f"SEO metadata missing: {path}"
    sitemap = ElementTree.parse(output / "sitemap.xml")
    assert len(sitemap.getroot()) == len(expected), "Sitemap does not list every HTML page"
    llms = (output / "llms.txt").read_text(encoding="utf-8")
    for source in sources:
        if source.name not in {"README.md", "AGENTS.md"}:
            assert build.output_path(source).name in llms, f"Missing llms index entry: {source}"
    assert (output / "robots.txt").is_file()
    assert (output / "search-index.json").is_file()
    print(f"Validated {len(expected)} HTML pages, metadata, sitemap, llms.txt, and search assets")


if __name__ == "__main__":
    main()
