# 14 — GEO and AEO Checklist

> Improve how clearly and reliably a project can be understood, sourced, and answered by search answer systems and generative AI. GEO = Generative Engine Optimization; AEO = Answer Engine Optimization. Neither guarantees citation or inclusion.

> **Scope: Frontend-specific.** This file is one part of the 14_GEO_and_AEO.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Review ownership:** The consolidated checklist is frontend-led for website content, answer quality, authority, and discovery; involve editorial, analytics, legal, and other cross-team reviewers for relevant checks. Related backend and AI domain files retain their specialized checks.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Audience, answer intent, and coverage

- [ ] **GEO-001** `P1` High-value user questions, follow-ups, and conversational queries are inventoried.
- [ ] **GEO-002** `P1` Questions are mapped to authoritative, relevant pages with a clear intended answer.
- [ ] **GEO-003** `P1` Content distinguishes definitions, instructions, comparisons, FAQs, and decision criteria.
- [ ] **GEO-004** `P1` Answers reflect audience knowledge level and include scope, caveats, and applicability.
- [ ] **GEO-005** `P1` Important topics have sufficient depth and context beyond isolated keyword phrases.
- [ ] **GEO-037** `P1` Include legitimate comparison and follow-up questions without making redundant doorway pages.
- [ ] **GEO-038** `P1` Evaluate whether visitors can independently verify critical claims from the cited primary evidence.
- [ ] **GEO-039** `P2` Identify authoritative, public canonical pages for each product, concept, service, or policy.

## Answer-ready structure and clarity

- [ ] **GEO-006** `P1` Priority pages state a concise, accurate answer close to the related question or heading.
- [ ] **GEO-007** `P1` Headings, short paragraphs, numbered steps, and tables organize information where useful.
- [ ] **GEO-008** `P1` Terms, entity names, units, dates, and product/version details are explicit and unambiguous.
- [ ] **GEO-009** `P1` Key claims include methodology, assumptions, limitations, and dates where relevant.
- [ ] **GEO-010** `P1` FAQs address genuine user needs and avoid repetitive or fabricated question-answer blocks.
- [ ] **GEO-011** `P1` Structured examples or comparisons are accurate and consistent with the surrounding narrative.
- [ ] **GEO-040** `P1` State prerequisites, limitations, and conditions near short answers where omission would mislead.
- [ ] **GEO-041** `P1` Ensure charts, figures, and videos have textual context sufficient to convey important facts.
- [ ] **GEO-042** `P1` Test that extracted answer snippets still make sense without the original page title or navigation.

## Authority, provenance, and factual reliability

- [ ] **GEO-012** `P1` Claims that could affect decisions are backed by trustworthy, attributable sources.
- [ ] **GEO-013** `P1` First-party data, original research, real examples, or demonstrated expertise are identified when available.
- [ ] **GEO-014** `P1` Authors, organizations, editorial responsibility, and update history are stated accurately.
- [ ] **GEO-015** `P1` Statistics and time-sensitive facts are dated, checked, and scheduled for refresh.
- [ ] **GEO-016** `P1` Citations and outbound links lead to the actual source and do not imply endorsements.
- [ ] **GEO-017** `P1` Product names, specifications, organization facts, and public profiles are consistent across owned channels.
- [ ] **GEO-043** `P2` Maintain a provenance record for changing datasets, prices, statistics, and public statements.
- [ ] **GEO-044** `P1` Set a review schedule and visible update date for pages with material time-sensitive facts.

## Machine readability and discovery

- [ ] **GEO-019** `P1` Relevant public pages are crawlable and render essential content in accessible HTML.
- [ ] **GEO-020** `P1` Canonical URLs, sitemap entries, internal links, and index directives are consistent with the SEO checklist.
- [ ] **GEO-021** `P1` Schema.org markup is used only where appropriate, valid, and supported by visible page content.
- [ ] **GEO-022** `P1` Important assets, downloads, and data tables have descriptive text or accessible alternatives.
- [ ] **GEO-047** `P1` Use provider-published crawler guidance to distinguish search crawling from model-training controls where relevant.
- [ ] **GEO-048** `P1` Check structured data is consistent with page text and avoid fabricated organization/entity identifiers.

## Trustworthy answer experience

- [ ] **GEO-026** `P1` Direct answers avoid exaggerated certainty, misleading superlatives, and unsupported comparisons.
- [ ] **GEO-027** `P1` Policies, pricing, availability, support details, and product limitations are easy to locate and current.
- [ ] **GEO-028** `P1` Where appropriate, content identifies geographic, regulatory, language, or version differences.
- [ ] **GEO-029** `P1` Answer snippets preserve context and do not omit material safety, cost, or eligibility caveats.
- [ ] **GEO-030** `P1` Public contact, entity, and brand information is consistent and can be verified independently.
- [ ] **GEO-049** `P1` Make sources and important qualifications accessible from short answer sections and summaries.
- [ ] **GEO-050** `P1` Test quotations and paraphrases for faithful context rather than optimizing only for answer length.
- [ ] **GEO-051** `P1` Provide explicit correction paths when publicly shared answers or data are found to be wrong. For material inaccuracies in sampled AI-generated brand/product answers (prices, plans, supported platforms, policies, ownership or identity), maintain a dated canonical fact sheet and claim/source log, trace the claim to stale first-party pages, PDFs, feeds or independently cited third-party pages where observable, correct the authoritative source with the responsible owner, and resample actual answers over an appropriate period; do not mark a model answer fixed from one run or promise a two-month convergence deadline.

## Measurement and iteration

- [ ] **GEO-031** `P1` Baseline questions and evaluation criteria are documented before optimization.
- [ ] **GEO-032** `P1` For a representative set of real audience questions and relevant competitors, inspect the actual answers and linked sources across chosen AI answer/search systems, retaining model/platform, search mode, location/language if relevant, dates and multiple observations. Treat a repeatedly cited third-party page as a lead for truthful editorial improvement, not a guarantee that outreach or placement will cause future citations.
- [ ] **GEO-033** `P2` Track sampled AI/search-answer brand mentions, observed linked citations, factual accuracy, crawler requests, referral traffic and conversions **as distinct measurements**, with source, date, coverage and uncertainty. Bing Webmaster Tools' AI Performance report can provide **aggregated, sampled citations and grounding queries across its supported Microsoft/partner experiences**, not individual answers, rankings or click counts; its preview Citation Share is contextual and non-causal. Google Search Console's overall Web report, GA4 AI referrers and tool-defined visibility scores are not direct evidence of individual cited answers or AI-wide citation share. Retain actual answer-and-link evidence separately; never equate an observed crawl with a citation.
- [ ] **GEO-036** `P1` Changes are reviewed for measurable user benefit and aligned with SEO, accessibility, privacy, and legal constraints.
- [ ] **GEO-052** `P1` Keep a dated, reproducible sample of representative, genuinely asked prompts/questions and observed answer-linked citations, including model/platform, language/locale, retrieval settings, source URLs and repeat-run variation; select a review cadence justified by change risk and sampling cost, not a compulsory number of prompts or weekly rerun.
- [ ] **GEO-053** `P1` Separate ranking, crawl/index diagnostics, referral logs, answer sampling, and conversions in reports.

- [ ] **GEO-079** `P1` For public content intended for search and answer discovery, test the **live public response** for each production hostname, HTTP access, current robots directives (including CDN/edge-managed rules), authentication/WAF challenges and initial versus rendered essential text for Googlebot and each explicitly targeted AI search crawler using current provider documentation. Distinguish search discovery from model-training/grounding policies and user-triggered fetch controls; a spoofed User-Agent in a single curl request, a 200 without usable content or an IP address alone does not authenticate the actual provider bot or establish index/citation eligibility.
- [ ] **GEO-080** `P1` When organization or product entity identification matters, reconcile the public canonical domain, official name, authorship, organization markup, contact details, and controlled social/business profiles; check for ambiguous names or inconsistent identifiers without claiming search/AI systems require a custom domain or guarantee entity recognition.

## Frontend Checks

> Apply to browser-based, mobile-web, embedded, or other user-facing interfaces. Record N/A with reasons for headless services.

**Reference basis:** [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features); [Google Search Central — Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide); [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics).

- [ ] **GEO-066** `P1` Put a direct, accurate answer near the relevant question while retaining context and meaningful caveats.
- [ ] **GEO-067** `P1` Use descriptive headings, semantic HTML, tables, and lists that remain understandable without interactive widgets.
- [ ] **GEO-068** `P1` Expose primary facts in rendered textual content; give charts, images, and media adequate text alternatives.
- [ ] **GEO-069** `P1` Use stable public URLs and standard anchor links to canonical source pages.
- [ ] **GEO-070** `P1` Verify initial HTML/rendered output shows the essential content to intended crawlers, including JavaScript-based pages.
- [ ] **GEO-071** `P1` Match visible headings, answers, dates, and entities to supported structured data without invisible or invented claims.
- [ ] **GEO-072** `P1` Present citations and source links where a reader can inspect supporting primary information.
- [ ] **GEO-073** `P1` Avoid misleading summaries, unsupported numerical claims, or fabricated quotes in callouts and snippets.
- [ ] **GEO-074** `P1` State geographic scope, eligibility, currency, date, and relevant version in comparative answer sections.
- [ ] **GEO-075** `P1` Test mobile layout, accessibility, readability, and critical interactions so sources are usable by humans.
- [ ] **GEO-076** `P1` Check translated or region-specific pages keep facts, named entities, and caveats consistent across languages.
- [ ] **GEO-077** `P1` Confirm outdated or deleted content results in a clear correction/redirect or appropriate missing-page status.
- [ ] **GEO-078** `P1` Make public contact, organization, product, and publication details consistent across page templates.

## SEO and GEO launch factors — evidence and limits

Use the checks above and the related SEO/launch files to evaluate the following factors; importance labels are practical triage guidance, **not official search-engine weights or proven ranking factors**.

| Factor | Practical priority | Basis |
| --- | --- | --- |
| Public content crawlable by intended search and AI-search systems | Critical when public discovery is a goal | Test robots, HTTP, auth, CDN, links and rendered output; a provider may use distinct crawlers for search, training or user-requested fetches |
| Original, relevant, accurate, useful information | Critical | Prioritize factual usefulness and verifiable firsthand or authoritative information, not content written solely for algorithmic inclusion |
| Accessible textual HTML and clear page structure | High | Use useful headings, descriptive anchors, and important text visible without special interaction |
| Credible authors, source citations and consistent public entity information | High | Identify the actual organization/author; allow readers to verify claims; consistency helps avoid confusion but cannot guarantee AI recognition |
| Structured data consistent with the visible page | Useful where applicable | Use supported types and real entity identifiers; no special AI-only schema is required for Google Search |
| Controlled custom domain versus `github.io` / `pages.dev` hostname | Operational/brand decision | A controlled domain aids portability and stable identity, **not an independently established direct ranking bonus** |
| Organic mentions and relevant editorial links | Context-dependent | Earn real references through useful content and legitimate outreach; avoid link schemes |

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve deceptive, fabricated, or unsubstantiated content. Verify essential public facts and make evidence available; AI answer visibility cannot be promised.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#14_geo_and_aeo), not prerequisites or verification evidence.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Central — Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

GEO/AEO techniques are not separate eligibility requirements for Google AI Overviews or AI Mode. Google documents ordinary Search eligibility, helpful content, and no required AI-specific markup. Other providers differ; inclusion and citations are not guaranteed.

- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — ordinary Search eligibility, crawlable text, visible-content/structured-data consistency, and AI-feature traffic included in Search Console's aggregated Web search reporting.
- [Google Search Central — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — `llms.txt` is not used by Google Search, including AI features.
- [Google — Overview of crawlers and fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers) — crawler and user-triggered fetcher distinctions.
- [Bing Webmaster Tools — AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) — sampled citation, grounding-query, trend and optional citation-share preview data, not rankings or click counts.
- [Bing Webmaster Blog — AI visibility preview](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/) — provenance and limits of Citation Share/Compare.
- [OpenAI — Overview of OpenAI crawlers](https://platform.openai.com/docs/bots) — distinguish OAI-SearchBot, GPTBot, and ChatGPT-User where applicable.

- [Google — Google-Extended crawler control](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended) — product token, not separate HTTP crawler; different from Googlebot's Search role.
- [OpenAI — Crawlers and user agents](https://developers.openai.com/api/docs/bots) — OAI-SearchBot supports search; GPTBot concerns model training; ChatGPT-User is user-triggered.
- [Cloudflare — Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/) — potential edge challenges; inspect actual events and delivered content.

**Source review date:** 2026-11-13. **Targeted citation/referral measurement verification:** 2026-11-14 (Google AI-features documentation and upstream provider descriptions).
