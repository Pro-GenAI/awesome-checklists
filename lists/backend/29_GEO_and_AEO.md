# 29 — GEO and AEO Checklist

> Improve how clearly and reliably a project can be understood, sourced, and answered by search answer systems and generative AI. GEO = Generative Engine Optimization; AEO = Answer Engine Optimization. Neither guarantees citation or inclusion.

> **Scope: Backend / API-specific.** This file is one part of the 29_GEO_and_AEO.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Machine readability and discovery

- [ ] **GEO-023** `P1` Server responses, access controls, and bot rules are intentionally configured for the target discovery channels.

## Measurement and iteration

- [ ] **GEO-054** `P1` Recheck content accuracy after changes to source APIs, catalog feeds, and structured data.
- [ ] **GEO-081** `P1` For owned sites where AI-search access monitoring is relevant and authorized, review edge/CDN/origin request logs for provider-documented search crawlers and user-initiated fetchers as **separate** classes. Verify bot identity using current provider IP ranges or verified-bot signals where available (treat user-agent text alone as untrusted); group permitted public-page requests by canonical URL, time window, response status and block/challenge reason, including 3xx/403/429/5xx and missing log coverage. Investigate missing or failed visits against robots, WAF/CDN, authentication, internal links and delivered HTML without treating raw request counts, zero log rows, training bots or user-agent matches as proof of search indexing, AI citations, rankings or demand. Redact sensitive paths/query data and restrict/retain logs according to privacy and security policy.

## API Checks

> Apply to API endpoints, client integrations, webhooks, or data feeds present in the project. Record N/A with reasons if none exist.

**Reference basis:** [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features); [Google Search Central — Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide); [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics).

- [ ] **GEO-055** `P2` Identify authoritative public APIs or feeds that supply facts displayed on answer-oriented pages and their update frequency.
- [ ] **GEO-056** `P1` Verify API-backed claims, entities, units, dates, product versions, and prices match the canonical human-readable pages.
- [ ] **GEO-057** `P2` Publish accurate, maintainable API reference or OpenAPI documentation when developer discovery is an actual use case.
- [ ] **GEO-058** `P1` Ensure public API documentation includes purpose, limits, examples, versioning, and the date of last substantive update.
- [ ] **GEO-059** `P1` Keep canonical pages available as accessible HTML; do not presume raw JSON API responses are indexed or cited as search pages.
- [ ] **GEO-060** `P1` Handle stale cache, failed API calls, and missing records so the site never silently presents inaccurate answer facts.
- [ ] **GEO-061** `P1` Verify schema/data feed identifiers match the intended organization, product, and page URLs.
- [ ] **GEO-062** `P1` Check licensing, provenance, and permitted public reuse before exposing datasets or AI-oriented machine-readable feeds.
- [ ] **GEO-063** `P1` Use structured API error statuses and document fallback behavior for consumers when the source data is unavailable.
- [ ] **GEO-064** `P2` Record change ownership for API schemas and upstream data fields that drive answer summaries and public claims.
- [ ] **GEO-065** `P1` Use access controls for non-public API data; do not publish private facts merely to improve AI discovery.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve deceptive, fabricated, or unsubstantiated content. Verify essential public facts and make evidence available; AI answer visibility cannot be promised.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#29_geo_and_aeo), not prerequisites or verification evidence.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Central — Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [OpenAI — Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots) — search versus training versus user-action bots and provider IP ranges.
- [Anthropic — Crawler access guidance](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) — Claude-SearchBot and Claude-User roles; published IP verification may be unavailable.
- [Perplexity — Crawler guidance](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) — PerplexityBot and Perplexity-User distinction, bot IP sources.
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

GEO/AEO techniques are not separate eligibility requirements for Google AI Overviews or AI Mode. Google documents ordinary Search eligibility, helpful content, and no required AI-specific markup. Other providers differ; inclusion and citations are not guaranteed.

**Source review date:** 2026-11-12. **Crawler-log verification date:** 2026-11-14 (OpenAI, Anthropic and Perplexity provider guidance).
