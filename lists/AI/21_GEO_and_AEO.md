# 21 — GEO and AEO Checklist

> Improve how clearly and reliably a project can be understood, sourced, and answered by search answer systems and generative AI. GEO = Generative Engine Optimization; AEO = Answer Engine Optimization. Neither guarantees citation or inclusion.

> **Scope: AI-specific.** This file is one part of the 21_GEO_and_AEO.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Authority, provenance, and factual reliability

- [ ] **GEO-018** `P1` AI-assisted content receives human factual review and does not invent sources, testimonials, or experience.
- [ ] **GEO-045** `P1` Evaluate claims about models, AI features, and performance against current official provider documentation.

## Machine readability and discovery

- [ ] **GEO-024** `P1` Robots and AI-crawler policies reflect business/legal choices; provider-specific crawler guidance is checked before changes.
- [ ] **GEO-025** `P1` Optional experimental files such as `llms.txt` are not treated as required standards or as guarantees of AI ingestion.
- [ ] **GEO-046** `P1` Confirm Google Search AI visibility uses ordinary index/snippet eligibility rather than unverified special-schema requirements.

## Measurement and iteration

- [ ] **GEO-034** `P1` Monitoring distinguishes verified referrals from estimates and avoids attributing unobservable AI usage.
- [ ] **GEO-035** `P1` Missing or incorrect AI-generated answers trigger content/source improvements, not attempts to manipulate models.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve deceptive, fabricated, or unsubstantiated content. Verify essential public facts and make evidence available; AI answer visibility cannot be promised.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#21_geo_and_aeo), not prerequisites or evidence of PASS.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Central — Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

GEO/AEO techniques are not separate eligibility requirements for Google AI Overviews or AI Mode. Google documents ordinary Search eligibility, helpful content, and no required AI-specific markup. Other providers differ; inclusion and citations are not guaranteed.

**Source review date:** 2026-11-12.
