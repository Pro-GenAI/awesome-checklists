#!/usr/bin/env python3
"""Build a dependency-light, SEO-ready static site from repository Markdown files."""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import mistune

WEBSITE_DIR = Path(__file__).resolve().parent
REPO_ROOT = WEBSITE_DIR.parent.parent
LISTS_DIR = REPO_ROOT / "lists"
DEFAULT_SITE_URL = "https://pro-genai.github.io/awesome-checklists/"
GITHUB_REPO = "https://github.com/Pro-GenAI/awesome-checklists"
SCOPES = ("shared", "frontend", "backend", "AI")
SCOPE_LABELS = {"shared": "Shared", "frontend": "Frontend", "backend": "Backend", "AI": "AI"}
SKIP_DIRS = {".git", ".github", ".venv", "node_modules", "__pycache__", "website", "skills"}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def slugify(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]*>", "", text))
    text = unicodedata.normalize("NFKD", text).casefold()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", text).strip("-") or "section"


def pretty_title(title: str) -> str:
    return re.sub(r"^\d{2}\s*[—-]\s*", "", title)


def text_only(markdown: str) -> str:
    markdown = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", markdown)
    markdown = re.sub(r"[*_`~#>]", "", markdown)
    return " ".join(markdown.split())


def scope_for(source: Path) -> str:
    parts = source.relative_to(REPO_ROOT).parts
    if len(parts) == 3 and parts[0] == "lists" and parts[1] in SCOPES[1:]:
        return parts[1]
    return "shared"


def output_path(source: Path) -> Path:
    rel = source.relative_to(REPO_ROOT)
    if rel == Path("README.md"):
        return Path("index.html")
    if len(rel.parts) == 2 and rel.parts[0] == "docs" and rel.name in {"AUTHORSHIP.md", "AWESOME.md", "CHANGELOG.md", "CONTRIBUTING.md", "DEVELOPMENT.md"}:
        return Path(rel.name).with_suffix(".html")
    if rel.parts[0] == "lists":
        # Preserve stable public URLs for relocated source and reference Markdown.
        if rel.as_posix() in {
            "lists/frontend/references/seo-redesign-url-map-template.md",
            "lists/references/source-coverage-audit.md",
        }:
            return Path(rel.name).with_suffix(".html")
        return Path(*rel.parts[1:]).with_suffix(".html")
    return rel.with_suffix(".html")


def relative_link(target: Path, current: Path) -> str:
    return os.path.relpath(str(target), start=str(current.parent)).replace(os.sep, "/")


def all_sources() -> list[Path]:
    return sorted(
        (p for p in REPO_ROOT.rglob("*.md") if not any(part in SKIP_DIRS for part in p.relative_to(REPO_ROOT).parts)),
        key=lambda p: p.relative_to(REPO_ROOT).as_posix().casefold(),
    )


@dataclass
class Page:
    source: Path
    output: Path
    scope: str
    title: str
    description: str
    content: str


def make_page(path: Path) -> Page:
    content = path.read_text(encoding="utf-8")
    heading = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
    title = text_only(heading.group(1)) if heading else path.stem.replace("_", " ")
    # The first introductory blockquote typically supplies the checklist's purpose.
    lead = re.search(r"^>\s*(?!\*\*Scope:|\[!)(.+)$", content, re.MULTILINE)
    if lead is None:
        lead = re.search(r"^(?![#>|\s-])(.{40,})$", content, re.MULTILINE)
    description = text_only(lead.group(1)) if lead else f"Review {title.lower()} with the Awesome Checklists reference collection."
    return Page(path, output_path(path), scope_for(path), title, description[:190], content)


class DocRenderer(mistune.HTMLRenderer):
    def __init__(self, page: Page, path_map: dict[Path, Path]) -> None:
        super().__init__(escape=True)
        self.page = page
        self.path_map = path_map
        self.headings: list[tuple[int, str, str]] = []
        self.slug_counts: dict[str, int] = {}

    def heading(self, text: str, level: int, **attrs: object) -> str:
        clean = html.unescape(re.sub(r"<[^>]*>", "", text))
        base = slugify(clean)
        number = self.slug_counts.get(base, 0)
        self.slug_counts[base] = number + 1
        slug = base if number == 0 else f"{base}-{number + 1}"
        if level in (2, 3):
            self.headings.append((level, clean, slug))
        return f'<h{level} id="{esc(slug)}">{text}<a class="heading-anchor" href="#{esc(slug)}" aria-label="Link to {esc(clean)}">#</a></h{level}>\n'

    def image(self, text: str, url: str, title: str | None = None) -> str:
        # The repository README uses docs/website/assets/...; the published site
        # copies docs/website/assets/ to dist/assets/.
        if self.page.source == REPO_ROOT / "README.md" and url.startswith("docs/website/assets/"):
            url = "assets/" + url.removeprefix("docs/website/assets/")
        return super().image(text, url, title)

    def link(self, text: str, url: str, title: str | None = None) -> str:
        parts = urlsplit(url)
        if not parts.scheme and not parts.netloc and parts.path:
            requested = unquote(parts.path)
            target = (self.page.source.parent / requested).resolve()
            if target in self.path_map:
                new_path = relative_link(self.path_map[target], self.page.output)
                url = urlunsplit(("", "", quote(new_path, safe="/._-~"), parts.query, parts.fragment))
            elif requested.endswith("/") or target.is_dir():
                rel = target.relative_to(REPO_ROOT) if target.is_relative_to(REPO_ROOT) else None
                if rel is not None:
                    index = None
                    if not rel.parts:
                        index = Path("index.html")
                    elif rel.parts[0] == "lists" and len(rel.parts) <= 2:
                        # Render lists/ and lists/{scope}/ as legacy site collection URLs.
                        section = rel.parts[1:]
                        index = Path(*section) / "index.html"
                    elif rel.parts[0] in SCOPES[1:]:
                        index = rel / "index.html"
                    if index is not None:
                        url = urlunsplit(("", "", relative_link(index, self.page.output), parts.query, parts.fragment))
        return super().link(text, url, title)


def canonical(base: str, path: Path) -> str:
    # Prefer clean directory URLs for landing pages; assets still link to index.html.
    if path.name == "index.html":
        return base if path.parent == Path(".") else base + quote(path.parent.as_posix(), safe="/._-~") + "/"
    return base + quote(path.as_posix(), safe="/._-~")


def jsonld(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def is_checklist(page: Page) -> bool:
    rel = page.source.relative_to(REPO_ROOT)
    if not (rel.parts and rel.parts[0] == "lists"):
        return False
    valid_folder = (len(rel.parts) == 2 or
                    (len(rel.parts) == 3 and rel.parts[1] in SCOPES[1:]))
    return valid_folder and bool(re.fullmatch(r"\d{2}_.+\.md", page.source.name))


def is_resource(page: Page) -> bool:
    rel = page.source.relative_to(REPO_ROOT)
    if page.source.name in {"README.md", "AGENTS.md"} or is_checklist(page):
        return False
    return len(rel.parts) == 1 or (len(rel.parts) == 2 and rel.parts[0] == "docs" and rel.name in {"AUTHORSHIP.md", "AWESOME.md", "CHANGELOG.md", "CONTRIBUTING.md", "DEVELOPMENT.md"}) or (
        len(rel.parts) >= 3 and rel.parts[0] == "lists" and
        (rel.parts[1] == "references" or rel.parts[-2] == "references")
    )


def nav_html(page_path: Path, current_scope: str, pages: list[Page]) -> str:
    groups = {scope: [p for p in pages if p.scope == scope and is_checklist(p)] for scope in SCOPES}
    blocks = [f'<a class="sidebar-main-link" href="{esc(relative_link(Path("index.html"), page_path))}">Overview</a>',
              f'<a class="sidebar-main-link" href="{esc(relative_link(Path("AGENTS.html"), page_path))}">Contribution guide</a>']
    for scope in SCOPES:
        group = groups[scope]
        intro = Path(scope) / "index.html" if scope != "shared" else Path("index.html")
        entries = ""
        for p in group:
            active = page_path == p.output
            active_class = " active" if active else ""
            current = ' aria-current="page"' if active else ""
            entries += (f'<a class="sidebar-item{active_class}" href="{esc(relative_link(p.output, page_path))}"'
                        f'{current}>{esc(pretty_title(p.title))}</a>')
        opened = " open" if scope == current_scope else ""
        blocks.append(f'<details class="sidebar-group"{opened}><summary>{esc(SCOPE_LABELS[scope])}<span class="count">{len(group)}</span></summary>'
                      f'<a class="sidebar-collection" href="{esc(relative_link(intro, page_path))}">Browse collection</a>{entries}</details>')
    resources = [p for p in pages if is_resource(p)]
    if resources:
        entries = ""
        for p in resources:
            active_class = " active" if p.output == page_path else ""
            current = ' aria-current="page"' if p.output == page_path else ""
            entries += (f'<a class="sidebar-item{active_class}" href="{esc(relative_link(p.output, page_path))}"'
                        f'{current}>{esc(p.title)}</a>')
        opened = " open" if any(p.output == page_path for p in resources) else ""
        blocks.append(f'<details class="sidebar-group"{opened}><summary>Resources<span class="count">{len(resources)}</span></summary>{entries}</details>')
    return "".join(blocks)


def toc_html(headings: list[tuple[int, str, str]]) -> str:
    headings = [h for h in headings if h[0] in (2, 3)]
    if not headings:
        return '<p class="toc-empty">Browse the collection using the sidebar.</p>'
    return "".join(f'<a class="toc-link level-{level}" href="#{esc(slug)}">{esc(title)}</a>' for level, title, slug in headings[:45])


def page_html(page_path: Path, title: str, description: str, scope: str, body: str,
              headings: list[tuple[int, str, str]], pages: list[Page], base: str, homepage: bool = False) -> str:
    home_href = relative_link(Path("index.html"), page_path)
    prefix = "" if page_path.parent == Path(".") else "../" * len(page_path.parent.parts)
    collection_href = relative_link(Path(scope) / "index.html", page_path) if scope != "shared" else home_href
    collection_label = "Resources" if any(is_resource(p) and p.output == page_path for p in pages) else SCOPE_LABELS[scope]
    crumbs = f'<a href="{esc(home_href)}">Home</a>'
    if not homepage:
        crumbs += f'<span aria-hidden="true">/</span><a href="{esc(collection_href)}">{esc(collection_label)}</a>'
        crumbs += f'<span aria-hidden="true">/</span><span aria-current="page">{esc(title)}</span>'
    url = canonical(base, page_path)
    website = {"@type": "WebSite", "name": "Awesome Checklists", "url": base, "description": "Reference checklists for software and AI product development."}
    if homepage:
        structured: object = {"@context": "https://schema.org", "@graph": [website, {"@type": "Organization", "name": "Pro-GenAI", "url": "https://github.com/Pro-GenAI"}]}
    else:
        trail = [{"@type": "ListItem", "position": 1, "name": "Home", "item": canonical(base, Path("index.html"))},
                 {"@type": "ListItem", "position": 2, "name": collection_label, "item": canonical(base, Path(scope) / "index.html") if scope != "shared" else canonical(base, Path("index.html"))},
                 {"@type": "ListItem", "position": 3, "name": title, "item": url}]
        structured = {"@context": "https://schema.org", "@graph": [
            {"@type": "TechArticle", "headline": title, "description": description, "mainEntityOfPage": url,
             "author": {"@type": "Organization", "name": "Pro-GenAI"}, "isPartOf": website},
            {"@type": "BreadcrumbList", "itemListElement": trail}]}
    page_title = "Awesome Checklists — Practical Software & AI Review Guides" if homepage else f"{title} | Awesome Checklists"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(description[:160])}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{esc(url)}">
  <meta property="og:type" content="{'website' if homepage else 'article'}">
  <meta property="og:site_name" content="Awesome Checklists">
  <meta property="og:title" content="{esc(page_title)}">
  <meta property="og:description" content="{esc(description[:160])}">
  <meta property="og:url" content="{esc(url)}">
  <meta name="twitter:card" content="summary">
  <link rel="alternate" type="text/plain" title="LLM content index" href="{esc(prefix)}llms.txt">
  <link rel="stylesheet" href="{esc(prefix)}assets/site.css">
  <script src="{esc(prefix)}assets/site.js" defer></script>
  <script type="application/ld+json">{jsonld(structured)}</script>
</head>
<body data-root="{esc(prefix or './')}" data-search-index="{esc(prefix)}search-index.json">
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar">
  <a class="brand" href="{esc(home_href)}" aria-label="Awesome Checklists home"><span class="brand-mark" aria-hidden="true">✓</span><span>awesome<span class="brand-highlight">checklists</span></span></a>
  <div class="topbar-actions"><a class="topbar-link" href="{esc(prefix)}llms.txt">llms.txt</a><a class="topbar-link" href="{GITHUB_REPO}" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div>
  <div class="search-wrap"><label class="visually-hidden" for="search">Search checklists</label><input id="search" type="search" placeholder="Search all checklists…" autocomplete="off" aria-controls="search-results" aria-expanded="false"><kbd>/</kbd><div id="search-results" class="search-results" hidden></div></div>
</header>
<div class="site-layout">
  <aside class="sidebar" aria-label="Checklist navigation"><div class="sidebar-inner"><div class="sidebar-kicker">THE LIBRARY</div>{nav_html(page_path, scope, pages)}</div></aside>
  <main id="main" class="main"><nav class="breadcrumbs" aria-label="Breadcrumb">{crumbs}</nav><article class="prose{' prose-home' if homepage else ''}">{body}</article><div class="page-footer"><strong>Reference, not a certification.</strong> Check applicability, verify important claims against current primary sources, and seek expert review where necessary. <a href="{esc(relative_link(Path('index.html'), page_path))}#contributions-and-suggestions-are-encouraged">Suggest an improvement</a>.</div></main>
  <aside class="on-this-page" aria-label="On this page"><div class="toc-title">ON THIS PAGE</div>{toc_html(headings)}</aside>
</div>
<footer class="site-footer"><span>Built from Markdown · Designed for thoughtful reviews</span><span><a href="{GITHUB_REPO}">Source on GitHub</a> · <a href="{esc(prefix)}llms.txt">llms.txt</a></span></footer>
</body>
</html>
'''


def index_page(scope: str, pages: list[Page]) -> tuple[str, str, list[tuple[int, str, str]]]:
    group = [p for p in pages if p.scope == scope and is_checklist(p)]
    label = SCOPE_LABELS[scope]
    details = {"frontend": "User experience, accessibility, browser behavior, client performance, and interface-focused reviews.",
               "backend": "API contracts, databases, service reliability, operations, security, and server-side integrations.",
               "AI": "Model selection, data, evaluation, RAG, agent systems, guardrails, and monitoring."}
    lead = details[scope]
    cards = "".join(f'<a class="collection-card" href="{esc(p.output.name)}"><span class="collection-card-label">CHECKLIST</span><strong>{esc(pretty_title(p.title))}</strong><span>{esc(p.description[:125])}</span><span class="card-action">Explore checklist →</span></a>' for p in group)
    body = f'<h1>{esc(label)} checklists</h1><p class="collection-lead">{esc(lead)}</p><p class="muted">{len(group)} actionable reference checklists. Pick what applies to your project; these are not universal requirements or certifications.</p><div class="collection-grid">{cards}</div>'
    return body, f"{label} software development review checklists. {lead}", []


def write_llms(out: Path, pages: list[Page], base: str) -> None:
    template = (WEBSITE_DIR / "llms.txt").read_text(encoding="utf-8")
    content = template.replace("{{SITE_URL}}", base).replace("{{GITHUB_REPO}}", GITHUB_REPO).rstrip() + "\n"
    for scope in SCOPES:
        group = [p for p in pages if p.scope == scope and is_checklist(p)]
        content += f"\n## {SCOPE_LABELS[scope]} checklists\n\n"
        for p in group:
            content += f"- [{p.title}]({canonical(base, p.output)}): {p.description}\n"
    resources = [p for p in pages if is_resource(p)]
    if resources:
        content += "\n## Additional resources (not checklists)\n\n"
        for p in resources:
            content += f"- [{p.title}]({canonical(base, p.output)}): {p.description}\n"
    (out / "llms.txt").write_text(content, encoding="utf-8")


def build(output_dir: Path, base: str) -> int:
    sources = all_sources()
    if not sources or not any(p.name == "README.md" and p.parent == REPO_ROOT for p in sources):
        raise RuntimeError("Repository root README.md is required")
    pages = [make_page(source) for source in sources]
    path_map = {p.source.resolve(): p.output for p in pages}
    # Resolve to an absolute path before deleting; protect source and repository files.
    output_dir = output_dir.resolve()
    protected = (WEBSITE_DIR / "assets", WEBSITE_DIR / ".venv", WEBSITE_DIR / "__pycache__")
    if (output_dir == WEBSITE_DIR or not output_dir.is_relative_to(WEBSITE_DIR)
            or any(output_dir == directory or directory.is_relative_to(output_dir) for directory in protected)):
        raise ValueError("Output directory must be a subdirectory of docs/website/ (not docs/website/ itself)")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    shutil.copytree(WEBSITE_DIR / "assets", output_dir / "assets")
    for page in pages:
        renderer = DocRenderer(page, path_map)
        markdown = mistune.create_markdown(renderer=renderer, plugins=["table", "task_lists", "strikethrough", "url"])
        body = markdown(page.content)
        target = output_dir / page.output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html(page.output, page.title, page.description, page.scope,
                                    body, renderer.headings, pages, base, page.source.name == "README.md" and page.source.parent == REPO_ROOT), encoding="utf-8")
    for scope in SCOPES[1:]:
        body, description, headings = index_page(scope, pages)
        target = Path(scope) / "index.html"
        (output_dir / target).write_text(page_html(target, f"{SCOPE_LABELS[scope]} checklists", description, scope,
                                                       body, headings, pages, base), encoding="utf-8")
    search_items = []
    for page in pages:
        headings = re.findall(r"^#{2,3}\s+(.+)$", page.content, flags=re.MULTILINE)
        search_items.append({"title": page.title, "url": page.output.as_posix(), "scope": "Resources" if is_resource(page) else SCOPE_LABELS[page.scope],
                             "description": page.description, "terms": text_only(" ".join(headings[:24]))[:900]})
    (output_dir / "search-index.json").write_text(json.dumps(search_items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    urls = [p.output for p in pages] + [Path(scope) / "index.html" for scope in SCOPES[1:]]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{esc(canonical(base, path))}</loc></url>\n" for path in urls)
    sitemap += "</urlset>\n"
    (output_dir / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (output_dir / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n", encoding="utf-8")
    write_llms(output_dir, pages, base)
    print(f"Built {len(pages)} Markdown pages + 3 scope indexes into {output_dir}")
    print(f"Canonical site URL: {base}")
    return len(pages) + 3


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a static HTML site from all repository Markdown files")
    parser.add_argument("--output", type=Path, default=WEBSITE_DIR / "dist", help="output directory inside docs/website/")
    parser.add_argument("--site-url", default=os.getenv("SITE_URL", DEFAULT_SITE_URL), help="public base URL for sitemap/canonical links")
    args = parser.parse_args()
    parsed = urlsplit(args.site_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.query or parsed.fragment:
        parser.error("--site-url must be an absolute HTTP(S) URL without query or fragment")
    base = args.site_url.rstrip("/") + "/"
    try:
        build(args.output, base)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")


if __name__ == "__main__":
    main()
