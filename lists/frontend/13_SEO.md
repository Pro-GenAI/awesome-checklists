# 13 — SEO Checklist

> Check discoverability, crawl/index controls, content quality, usability, and measurement for sites meant to appear in search results.

> **Scope: Frontend-specific.** This file is one part of the 13_SEO.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Goals, audience, and content plan


- [ ] **SEO-005** `P1` Navigation and information architecture make important pages easy to find.

- [ ] **SEO-001** `P1` Target audiences, markets, languages, priority pages, and conversion goals are documented.
- [ ] **SEO-002** `P1` For priority services and topics, map actual audience questions and distinct search intents to an appropriate primary page and useful supporting pages; identify relevant contextual internal links without keyword stuffing, compulsory article counts, or creating overlapping pages merely to target variants.
- [ ] **SEO-003** `P1` Each important page serves a distinct purpose and provides original, accurate, maintained content.
- [ ] **SEO-004** `P1` Content ownership, independent editorial review, factual sources, and update cadence are assigned. Where AI tools generate or substantially rewrite public pages or SEO metadata, verify an accountable reviewer fact-checks originality, accuracy, source rights, titles/descriptions, schema and image alt text **before publishing**. Numeric search volumes, clicks, rankings, pricing, traffic and research claims in AI-assisted reports must be attributable to authorized tools or actual fetched sources with a date and scope; mark unavailable values **not checked** rather than estimating from the model. Neither an agent's readiness score nor its asserted tool result substitutes for review approval.
- [ ] **SEO-033** `P2` Map editorial intent to canonical destination URLs and eliminate overlapping pages without distinct value.
- [ ] **SEO-034** `P1` Review content freshness for facts dependent on pricing, availability, laws, and time-sensitive product updates.
- [ ] **SEO-035** `P2` Document metadata and canonical rules for dynamically generated page types.
- [ ] **SEO-084** `P1` For sites with automatically assembled or data/template-driven page collections, verify the source dataset's rights, accuracy, required fields and update schedule; test representative, duplicate, incomplete and stale data rows for distinct, independently useful, fact-checked page content, working links, and accurate canonical/indexing and metadata signals. Exclude or appropriately `noindex` thin, repetitive, misleading or doorway-style variants rather than mass-publishing keyword substitutions.

## Crawlability and indexation


- [ ] **SEO-013** `P1` Site rendering exposes essential text and navigation to crawlers, including JavaScript-heavy pages; test initial and crawler-rendered HTML on representative routes and use server-side or static rendering when necessary rather than mandating SSR for every site.
- [ ] **SEO-036** `P1` Inspect live URL samples in Search Console to verify actual fetched HTML, rendering, and indexability.
- [ ] **SEO-037** `P1` Ensure JavaScript route links are real anchor elements with crawlable href values, not hash-only navigation.

- [ ] **SEO-006** `P1` Production pages intended for search are accessible to search-engine crawlers without unintended blocks.
- [ ] **SEO-007** `P1` `robots.txt` expresses deliberate crawling rules and does not accidentally block required resources; confirm `Disallow` only manages crawling, not privacy or guaranteed deindexing, and protect confidential material with authentication.
- [ ] **SEO-009** `P1` XML sitemaps list canonical, indexable URLs and are submitted where useful.
- [ ] **SEO-010** `P1` Canonical tags resolve duplicate/parameter variants consistently with intended URLs.
- [ ] **SEO-011** `P1` Internal links use descriptive anchor text and lead to working, relevant pages.
- [ ] **SEO-012** `P1` Redirects, broken links, soft 404s, and redirect chains are reviewed.
- [ ] **SEO-039** `P1` Confirm pagination links expose discoverable URLs rather than infinite-scroll-only content.

## Technical experience and performance


- [ ] **SEO-021** `P1` Mobile usability and responsive design work across supported devices.
- [ ] **SEO-024** `P1` HTTPS, browser security basics, and safe mixed-content behavior are verified.
- [ ] **SEO-025** `P1` Accessible navigation, semantic markup, and usable interactions support page quality.
- [ ] **SEO-026** `P1` Pagination, faceted navigation, infinite scroll, and filtering avoid unwanted index bloat where applicable.
- [ ] **SEO-044** `P1` Check for cumulative layout shifts from delayed images, fonts, banners, and dynamic data loads.

- [ ] **SEO-022** `P1` Core Web Vitals and real-user performance are measured; material issues have owners.
- [ ] **SEO-023** `P1` Images, fonts, scripts, and caching are optimized without breaking functionality.
- [ ] **SEO-043** `P1` Assess LCP, INP, and CLS at the 75th percentile for mobile and desktop, with regression budgets.
- [ ] **SEO-045** `P1` Verify that cookie dialogs, scripts, and heavy widgets do not obscure primary content or degrade core interactions.

## On-page metadata and semantics


- [ ] **SEO-014** `P1` Priority pages have unique, descriptive titles and useful meta descriptions. Before changing a low-CTR title, inspect the actual page–query pair, user intent, impressions, average position, search appearance, device and date range; compare the title shown in Google with the visible headline. Test truthful title improvements and track subsequent clicks, CTR and conversions without assuming Google will display the supplied title or that a title edit guarantees traffic.
- [ ] **SEO-015** `P1` Each page has a clear primary heading and logical subheading hierarchy.
- [ ] **SEO-016** `P1` URLs are readable, stable, and consistent about protocol, hostname, and trailing slashes.
- [ ] **SEO-017** `P1` Images have useful alternative text where appropriate and are delivered efficiently.
- [ ] **SEO-018** `P1` Structured data uses supported types, matches visible content, and passes relevant validation.
- [ ] **SEO-019** `P1` Hreflang annotations and language/region targets are correct where multilingual or regional versions exist.
- [ ] **SEO-020** `P1` Open Graph and other sharing metadata are accurate where relevant.
- [ ] **SEO-040** `P1` Verify structured-data properties and values are complete, accurate, and match visible content.
- [ ] **SEO-041** `P1` Test canonical, alternate-language, and social metadata across templates and locales.

## Trust, measurement, and maintenance


- [ ] **SEO-027** `P1` Organization details, authorship, contact information, and policies are accurate and discoverable.
- [ ] **SEO-083** `P1` For an eligible local or service-area business, verify the claimed business profile and relevant maintained listings reflect its real-world name, category, location or service area, hours, website and contacts; assign ownership for legitimate review responses and profile updates, and avoid duplicate or ineligible profiles.
- [ ] **SEO-085** `P1` For an eligible news publisher considering Google Preferred Sources, confirm its domain/subdomain appears in the current source preferences tool; if inviting readers to add it, verify the official button or deeplink uses the correct eligible site and works with accessible, voluntary user choice, without implying Publisher Center enrollment, a follower quota, guaranteed Top Stories appearance or daily traffic.
- [ ] **SEO-087** `P1` For creators or businesses tracking **their own supported social/video accounts** on Google Search, verify each applicable Instagram, TikTok, X or YouTube account/channel through its distinct Search Console **platform property** (or appropriate authorized owner access), confirm the correct account and connection status, and inspect available post/query-level Google Search performance with date, country and surface filters; distinguish Google Search/Discover/News clicks, impressions and reported positions from in-platform views, all-source traffic, website visits, conversions and sales. Record unavailable/partial reports without treating property creation, a keyword-led post or social sharing as a guarantee of indexing, rankings or revenue.
- [ ] **SEO-028** `P1` Claims and citations are verifiable; no misleading, mass-produced, or manipulative SEO content is used.
- [ ] **SEO-029** `P1` Verify ownership, correct site/property resolution, authorized access, and representative URL-inspection and sitemap-processing diagnostics in webmaster tools for the search engines actually targeted (such as Google Search Console and Bing Webmaster Tools). For new or materially updated owned URLs, optionally request a crawl through the supported URL Inspection workflow; avoid automatic weekly resubmission of unchanged pages or assuming a seven-day indexing deadline. For AI-agent/MCP integrations, use least-privilege read scopes by default, separately approve supported write/URL-submission actions and verify eligible URLs; neither sitemap nor URL submission guarantees crawling, indexing, ranking or a faster recrawl.
- [ ] **SEO-030** `P1` Analytics tracks agreed search goals with privacy-compliant consent and data handling.
- [ ] **SEO-031** `P2` Assign an owner and evidence-based review cadence for indexing, crawl errors, query impressions/clicks/CTR, important landing pages, and conversions. On owned Search Console properties, optionally segment long-tail, question and commercial/comparison queries using RE2 filters (for example, best, versus, alternatives, pricing, cost and reviews). Verify page–query relevance, typical position, search appearance, device, dates and sample size before revising content or titles. Distinguish estimated keyword demand from observed impressions, clicks and actual customers; account for omitted/anonymized queries and truncated reports. Do not infer AI citations or require arbitrary page output, position thresholds, seven-day cycles or publishing quotas. Verify any rank-monitoring provider, query source, automation and permissions comply with search policies; prefer authorized webmaster analytics over unapproved automated SERP scraping.
- [ ] **SEO-032** `P1` For site redesigns or migrations that change URLs, inventory important existing URLs and search/referral baselines before launch, approve old-to-new URL mappings or intentional removals, assign owners, and monitor new and old URL crawl/index status and organic traffic after launch. For eligible domain/subdomain moves, verify required old/new properties and use the Search Console Change of Address process where applicable; do not apply it to path-only changes, HTTP-to-HTTPS changes, or www/non-www switches on the same domain. Do not require redirects when URLs remain unchanged.
- [ ] **SEO-046** `P1` Before implementing or changing schema for a desired Google search appearance, verify that the specific rich-result feature remains supported and applicable to the page, validate the markup and relevant Search Console enhancement reports, and do not promise retired features (such as FAQ, HowTo or sitelinks search-box results) or mistake valid Schema.org vocabulary for Google rich-result eligibility.
- [ ] **SEO-086** `P1` For launches, template/CMS updates, migrations and AI-assisted publishing that could affect organic discovery, capture a versioned **pre-release and post-release** sample of high-value and representative production URLs. Compare actual response and redirect targets, `robots.txt` and HTTP `X-Robots-Tag`/meta index directives, canonical URLs, sitemap entries, rendered essential content and relevant schema, including the intended production hostname; alert or block rollout on unapproved search-critical regressions (for example, an indexable `200` becoming `noindex`, `404`, an unrelated canonical or sitewide bot block), identify the owner and confirm rollback or remediation with a fresh live test. Keep intentional exclusions and changes documented; do not treat snapshots as proof of Google indexing.
- [ ] **SEO-047** `P1` Investigate large indexing or traffic changes by release and page type, not ranking estimates alone.
- [ ] **SEO-048** `P1` For redesigned or migrated URLs, validate sampled and high-value old-to-new mappings against actual HTTP responses (permanent 301/308 redirects for genuine moves, appropriate 404/410 for removals), relevant final destinations, canonical/indexing directives, updated internal links and sitemaps, and absence of redirect loops or irrelevant homepage redirects; retain migration redirects for at least one year where feasible, longer when practical.

## Frontend Checks


> Apply to browser-based, mobile-web, embedded, or other user-facing interfaces. Record N/A with reasons for headless services.

**Reference basis:** [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics); [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data); [Google Search Central — Search appearance guidance](https://developers.google.com/search/docs/appearance/).

- [ ] **SEO-061** `P1` Verify important textual content and links are present in the rendered DOM as seen by search crawlers.
- [ ] **SEO-062** `P1` Use standard `<a href>` links for navigation; test crawlable routes, deep links, and refresh behavior.
- [ ] **SEO-063** `P1` Render unique page titles, meta descriptions, canonical tags, and heading structure for each indexable view.
- [ ] **SEO-064** `P1` Check that meta robots directives are correct in the initial document and are not accidentally inherited from staging.
- [ ] **SEO-065** `P1` Keep URL changes, history navigation, canonical URLs, and visible content synchronized for single-page apps.
- [ ] **SEO-066** `P1` Validate JSON-LD, microdata, or RDFa against visible page content and supported Google features.
- [ ] **SEO-067** `P1` Use semantic headings, clear labels, descriptive image alt text, and accessible main navigation.
- [ ] **SEO-068** `P1` Ensure lazy-loaded content and images become discoverable without requiring a user scroll/click for essential text.
- [ ] **SEO-069** `P1` Measure field Core Web Vitals (LCP, INP, CLS) and mobile UX on important page templates.
- [ ] **SEO-070** `P1` Reserve dimensions for media and dynamic components to minimize layout shift.
- [ ] **SEO-071** `P1` Verify responsive rendering, viewport settings, and content readability on small screens.
- [ ] **SEO-072** `P1` Check error, empty, and not-found UI states do not misleadingly present a successful indexable page.
- [ ] **SEO-073** `P1` Test locale switching and alternate language navigation without duplicating canonical targets.

- [ ] **SEO-074** `P1` For indexable paginated collections, give each page a distinct crawlable URL and a justified canonical target; verify linked page sequences without relying on `rel="next"`/`rel="prev"` as Google indexing signals.
- [ ] **SEO-075** `P1` Where image or video discovery matters and ordinary links are insufficient, assess image/video sitemap extensions, media URL access, metadata accuracy, and submission or validation without assuming sitemap inclusion guarantees indexing.
- [ ] **SEO-076** `P1` For businesses with multiple physical locations, verify each genuinely distinct location has an accurate, useful landing page and consistent name, address, contacts, hours, and applicable `LocalBusiness` data across the site and maintained listings.
- [ ] **SEO-077** `P1` On sites accepting public user-generated or paid outbound links, verify provenance-appropriate `rel="ugc"`, `rel="sponsored"`, or `rel="nofollow"` attributes without indiscriminately marking ordinary editorial links.
- [ ] **SEO-078** `P1` For public sites, verify the declared favicon/icon URL resolves, uses an appropriate supported format and caching behavior, and displays as intended in relevant browsers and search surfaces without treating the icon as a ranking guarantee.

- [ ] **SEO-079** `P1` For sites with related native applications, validate Apple Universal Links or Android App Links, allowed URL associations, appropriate app-promotion surfaces, and usable browser fallbacks where relevant.
- [ ] **SEO-080** `P1` For pages shared through social platforms, validate real destination previews for title, description, URL, and image with supported Open Graph/platform metadata without claiming direct ranking benefits.

- [ ] **SEO-081** `P1` If long-term ownership, branding, or portability matters, choose and document an appropriate controlled domain; verify DNS, HTTPS, preferred host, canonical URLs, and a redirect/URL-mapping plan for any migration from a platform subdomain. Do not claim a custom TLD or hosting suffix directly improves ranking.
- [ ] **SEO-082** `P1` Where off-site discovery is relevant, verify that research and outreach for editorial roundups, original statistics with disclosed methods, useful free tools, journalist requests, unlinked mentions/source credits, relevant broken-resource replacements, author-approved visual/video contributions, real vendor case studies, and eligible listings have distinct reader value. In relevant forums and communities, contribute useful first-hand answers under each community's rules, transparently disclose any material product affiliation, and add links only when genuinely allowed and helpful; do not game karma or mass-post. Validate facts, rights and destination URLs, respect independent publisher choice and disclosure/link attributes, and log only confirmed placements and referrals; reject paid, automated, coercive or excessive reciprocal link schemes and any guaranteed backlink, rank or AI-citation claims.

## Release gate


- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not sign off if important production pages are unintentionally blocked, canonicalized away, broken, or missing essential content. Search ranking is not guaranteed.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#13_seo), not prerequisites or verification evidence.

## Trusted references and scope


The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central — Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google Search Central — Supported structured-data features](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) — distinguish Schema.org validity from a currently supported Google Search appearance.
- [Google Search Central — Documentation updates](https://developers.google.com/search/updates) — Google FAQ rich results stopped May 7, 2026; FAQ feature docs were removed in June 2026. Recheck other retired features rather than relying on static skill examples.
- [Google Search Central — Search appearance guidance](https://developers.google.com/search/docs/appearance/)
- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals)
- [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)

Search engines may crawl, render, and index differently. Follow documentation for each target engine; passing these checks cannot guarantee indexing, ranking, or rich results.

- [Google Search Central — Pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) — distinct paginated URLs, canonicals, and obsolete next/prev signals.
- [Google Search Central — Sitemaps overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) — optional image/video extensions and discovery limitations.
- [Google Search Central — LocalBusiness structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business) — distinct locations and accurate business data.
- [Google Search Central — Qualify outbound links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) — `ugc`, `sponsored`, and `nofollow` link purposes.
- [Google Search Central — Favicons](https://developers.google.com/search/docs/appearance/favicon-in-search) — icon discovery and eligibility.

- [Primary guidance](https://developer.android.com/training/app-links/verify-applinks) — current platform-specific configuration and validation.
- [Primary guidance](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) — current platform-specific configuration and validation.
- [Primary guidance](https://ogp.me/) — current platform-specific configuration and validation.

- [Google Search Central — Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) — approved old-to-new URL maps, permanent redirects (generally at least one year), sitemaps, crawl/index validation, and post-move monitoring.
- [Google Search Central — SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) — organize user-relevant topics logically and provide meaningful internal links; no mandatory cluster size or backlink quota.
- [Google Search Central — Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) — descriptive, contextual internal links and link attributes.
- [Google Search Central — Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — original, useful, credible content rather than link manipulation.
- [Google Search Central — Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) — manipulative links, site reputation abuse, scaled content abuse and prohibited automated ranking queries; includes updated 2026 enforcement details.
- [Reddit Help — Spam policy](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam) — repeated promotion and automated spam prohibited, with individual community rules.
- [Reddit Help — Community moderation](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community) — some subreddits use 90/10, others forbid promotion; not a universal rule.
- [Google Search Central — Using the Indexing API](https://developers.google.com/search/apis/indexing-api/v3/using-api) — currently supports `JobPosting` or `BroadcastEvent` within `VideoObject`, not general pages; successful notifications do not prove indexing.
- [Chrome for Developers — Agent DevTools configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration) — browser access controls and usage-statistics/privacy flags for Chrome DevTools MCP.
- [Google Search Central — Guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) — manual fact-checking and review of AI-generated page text, titles, meta descriptions, structured data and image alt text before publishing; low-value scaled output remains a spam risk.
- [Google Business Profile — Guidelines for representing your business](https://support.google.com/business/answer/3038177) — eligibility and accurate local profile details.
- [Google Business Profile — Manage customer reviews](https://support.google.com/business/answer/3474050) — verified-business review responses where available.
- [Bing Webmaster Tools — Sitemaps](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed) — sitemap processing diagnostics.
- [Bing Webmaster Tools — URL inspection](https://www.bing.com/webmasters/help/url-inspection-55a30305) — actual crawl and index status.

- [Google Search Central — Preferred Sources publisher guide](https://developers.google.com/search/docs/appearance/preferred-sources) — eligible domain/subdomain, official opt-in button and deeplink, no guaranteed exposure.
- [Publisher Center — Publication pages update](https://support.google.com/news/publisher-center/answer/14859160) — new Google News Publisher Center registration stopped in 2024.
- [Search Console — RE2 custom filters](https://support.google.com/webmasters/answer/17011165) and [query-data limitations](https://support.google.com/webmasters/answer/17011259) — regex filters, anonymization and truncated results.
- [Google Search Central — Robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) — crawl disallow is not access control or guaranteed deindexing.
- [Google Search Central — Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) — inclusion is discretionary and `lastmod` should reflect significant verified changes.
- [Google Search Central — Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) — actual LCP, INP and CLS criteria.

- [Google Search Central — Title links](https://developers.google.com/search/docs/appearance/title-link) — Google may derive result titles from multiple page signals.
- [Google Search Central — Search snippets](https://developers.google.com/search/docs/appearance/snippet) — no fixed meta-description character limit.
- [Google Search Central — Request a recrawl](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) — quota-limited and not an indexing guarantee.
- [Google RE2 — Syntax](https://github.com/google/re2/wiki/Syntax) — ASCII word boundaries for Search Console regex.

- [Cloudflare — Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/) — challenges may affect legitimate clients and crawlers; check actual security events.
- [Google Search Central — JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) — initial and rendered HTML, correct status and indexing controls.
- [Google Search Central — Software app structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app) — conditional rich-result properties and genuine review evidence.
- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — ordinary Search eligibility and no special AI-only ranking file.
- [IndexNow — FAQ](https://www.indexnow.org/faq) — use only for participating engines, not a general Google indexing mechanism.

- [Google Search Central — Social/video platform properties globally launched July 29, 2026](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) — supported Instagram, TikTok, X and YouTube accounts; Google-side reporting.
- [Google Search Console Help — About platform properties](https://support.google.com/webmasters/answer/17148418) — account/channel ownership, per-platform properties, Google Search/Discover/News reports and limits; data may be partial or require processing.
- [Google Search Central — Analyze social and video content performance](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) — query, post, country, device and timing analysis for verified accounts.

**Source review date:** 2026-11-14. For a project-specific migration worksheet, see the [optional URL map template](references/seo-redesign-url-map-template.md); do not mark the shared checklist passed based on a plan alone.
