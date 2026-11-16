# 28 — SEO Checklist

> Check discoverability, crawl/index controls, content quality, usability, and measurement for sites meant to appear in search results.

> **Scope: Backend / API-specific.** This file is one part of the 28_SEO.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Crawlability and indexation

- [ ] **SEO-008** `P1` `noindex`, authentication, staging restrictions, and HTTP response statuses are correct for each page type.
- [ ] **SEO-038** `P1` Check server-origin 404/410 behavior for missing or permanently removed content, including client-routed pages.

## On-page metadata and semantics

- [ ] **SEO-042** `P1` Validate title and description generation when API-driven content is empty, missing, or duplicated.

## API Checks

> Apply to API endpoints, client integrations, webhooks, or data feeds present in the project. Record N/A with reasons if none exist.

**Reference basis:** [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics); [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data); [Google Search Central — Search appearance guidance](https://developers.google.com/search/docs/appearance/).

- [ ] **SEO-049** `P2` Inventory content APIs feeding indexable pages; determine which fields affect titles, headings, canonical URLs, and main content.
- [ ] **SEO-050** `P1` Verify API-backed pages produce meaningful HTML content for crawlers via the chosen rendering strategy.
- [ ] **SEO-051** `P1` Test slow, failed, and empty API responses so critical pages do not return indexable blank shells or misleading content.
- [ ] **SEO-052** `P2` Map deleted records and API not-found conditions to appropriate page-level 404/410 handling.
- [ ] **SEO-053** `P1` Ensure localized API content, slugs, and hreflang mappings agree with rendered language versions.
- [ ] **SEO-054** `P1` Check sitemap-generation APIs include only correct, canonical, crawlable URLs and update after content changes.
- [ ] **SEO-055** `P1` Verify cache invalidation and freshness for API-fed pricing, availability, dates, and other time-sensitive snippets.
- [ ] **SEO-056** `P1` Prevent API parameters and filter combinations from generating uncontrolled duplicate/indexable URLs.
- [ ] **SEO-057** `P1` Verify URL migrations preserve stable identifiers and emit proper redirects instead of silently breaking content.
- [ ] **SEO-058** `P1` Measure the API and server-render path latency affecting first contentful response and LCP.
- [ ] **SEO-059** `P1` Keep private endpoints, tokens, and user-specific responses out of publicly crawlable page output.
- [ ] **SEO-060** `P2` Publish helpful HTML API documentation only if developers are an intended search audience; raw JSON endpoints are not assumed to be SEO landing pages.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not sign off if important production pages are unintentionally blocked, canonicalized away, broken, or missing essential content. Search ranking is not guaranteed.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#28_seo), not prerequisites or verification evidence.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google Search Central — Search appearance guidance](https://developers.google.com/search/docs/appearance/)
- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals)
- [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)

Search engines may crawl, render, and index differently. Follow documentation for each target engine; passing these checks cannot guarantee indexing, ranking, or rich results.

**Source review date:** 2026-11-12.
