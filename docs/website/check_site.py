#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Sanity-check generated pages, SEO files, and the Markdown inventory."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

import build


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = False
        self.description = False
        self.canonical = False
        self.schema = False
        self.favicon_href: str | None = None
        self.page_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        self.title |= tag == "title"
        self.description |= tag == "meta" and data.get("name") == "description" and bool(data.get("content"))
        self.canonical |= tag == "link" and data.get("rel") == "canonical" and bool(data.get("href"))
        self.schema |= tag == "script" and data.get("type") == "application/ld+json"
        if tag == "link" and data.get("rel") == "icon" and data.get("type") == "image/svg+xml":
            self.favicon_href = data.get("href")
        if tag == "a" and data.get("href"):
            self.page_links.append(data["href"])


def main() -> None:
    assert build.canonical("https://awesome-checklists.pro-genai.com/", Path("AI/example.html")) == "https://awesome-checklists.pro-genai.com/AI/example"
    assert build.relative_link(Path("frontend/index.html"), Path("frontend/example.html")) == "./"
    assert build.relative_link(Path("AI/example.html"), Path("frontend/index.html")) == "../AI/example"
    output = build.WEBSITE_DIR / "dist"
    sources = build.all_sources()
    expected = {build.output_path(p) for p in sources}
    expected.update(Path(scope) / "index.html" for scope in build.SCOPES[1:])
    present = {p.relative_to(output) for p in output.rglob("*.html")}
    assert expected == present, f"Missing: {expected - present}; unexpected: {present - expected}"
    favicon = (output / "assets" / "favicon.svg").resolve()
    assert favicon.is_file(), "Favicon was not copied into site assets"
    for path in present:
        parser = HeadParser()
        parser.feed((output / path).read_text(encoding="utf-8"))
        assert all((parser.title, parser.description, parser.canonical, parser.schema)), f"SEO metadata missing: {path}"
        for link in parser.page_links:
            url = urlsplit(link)
            assert url.netloc not in ("", "awesome-checklists.pro-genai.com", "awesome-checklists.pages.dev") or not url.path.endswith(".html"), f"HTML URL in {path}: {link}"
        assert parser.favicon_href, f"Favicon link missing: {path}"
        linked_favicon = ((output / path).parent / parser.favicon_href).resolve()
        assert linked_favicon == favicon, f"Incorrect favicon path: {path}"
    sitemap = ElementTree.parse(output / "sitemap.xml")
    locs = [node.text for node in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    base = os.environ.get("SITE_URL", build.DEFAULT_SITE_URL).rstrip("/") + "/"
    assert len(locs) == len(expected), "Sitemap does not list every HTML page"
    assert len(set(locs)) == len(locs), "Sitemap contains duplicate URLs"
    assert set(locs) == {build.canonical(base, path) for path in expected}, "Sitemap URLs do not match canonical site URL"
    robots = (output / "robots.txt").read_text(encoding="utf-8")
    assert f"Sitemap: {base}sitemap.xml" in robots, "robots.txt sitemap URL is incorrect"
    for path in present:
        content = (output / path).read_text(encoding="utf-8")
        assert f'<link rel="canonical" href="{build.canonical(base, path)}">' in content, f"Canonical URL is incorrect: {path}"
    llms = (output / "llms.txt").read_text(encoding="utf-8")
    for source in sources:
        page = build.make_page(source)
        if build.is_checklist(page) or build.is_resource(page):
            assert build.canonical(base, page.output) in llms, f"Missing llms index entry: {source}"
    assert (output / "robots.txt").is_file()
    search = json.loads((output / "search-index.json").read_text(encoding="utf-8"))
    assert all(not item["url"].endswith(".html") for item in search), "Search contains HTML URLs"
    print(f"Validated {len(expected)} HTML pages, metadata, sitemap, llms.txt, and search assets")


if __name__ == "__main__":
    main()
