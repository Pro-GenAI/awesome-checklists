# External checklist coverage audit — 2026-11-13

> **Source-by-source provenance archive, not a numbered checklist.** The source assessments below document evidence, existing controls, exclusions, and access limitations across multiple review domains. Actionable verified controls belong in the corresponding numbered files in [`lists/`](../); do not convert historical notes into duplicate checks. Moved to `lists/references/` on 2026-11-14; historical dates and conclusions are retained.

**Current-source mapping note (2026-11-15):** The earlier archive uses `SEC-012` as shorthand for multiple injection controls. In current source, input-contract verification is SEC-012, database and command injection are SEC-118/119, and unsafe deserialization is SEC-120. This historical coverage narrative is **not a current per-ID PASS record**.

**Status:** Topic-by-topic review of both specifically requested source READMEs. This is a coverage assessment and source mapping, **not** a guarantee that every third-party link on the internet has been visited or that recommended tools were installed or executed.

**Sources:**
- [Tuts+ SEO Checklist for Web Designers](https://github.com/tutsplus/SEO-Checklist-for-Web-Designers/blob/master/seo_checklist.md)
- [dhilipsiva/webapp-checklist README](https://github.com/dhilipsiva/webapp-checklist/blob/master/README.md)
- [israelroldan/awesome-checklists](https://github.com/israelroldan/awesome-checklists) (parent curated resource index, reviewed separately)

## SEO source: all major topic groups

| Topic in source | Coverage decision |
| --- | --- |
| Crawlability, robots directives, canonical URLs, redirects, 404s, mobile accessibility, speed | Already represented in SEO-006–013, SEO-021–026, SEO-036–039, SEO-061–073 and related backend SEO checks |
| Pagination | **New SEO-074**, verifying independently crawlable pages and sound canonical selection rather than obsolete Google next/prev signals |
| URL architecture, hostname, hyphens, folders/subdomains, parameters | Existing SEO-010, SEO-016, SEO-026, SEO-035 and migration checks; no mandatory subdomain-versus-subfolder rule |
| HTML/XML/image/video sitemaps | Existing SEO-009 and backend SEO-054; **new SEO-075** for appropriate optional media extensions |
| Keywords, descriptive titles, headings, quality content, freshness, hreflang | SEO-001–004, SEO-014–019, SEO-027–028, SEO-033–034; no rigid single-keyword, word count, or title-length requirement |
| Image alt text/size, metadata, structured results | SEO-017–020, SEO-040–046 and accessibility/performance checks |
| Social sharing previews | SEO-020, SEO-041; preview correctness rather than historical fixed thumbnail dimensions |
| Local business and multiple locations | **New SEO-076**, per-location landing pages and consistent business data, conditional on physical locations |
| Off-site links, inbound reputation, organic links | Existing SEO-027–031 and reputation/measurement practice; **new SEO-077** to distinguish UGC, sponsored, and editorial links |
| Search appearance favicons | **New SEO-078**, icon availability and supported presentation |

**Obsolete, misleading, or non-universal rules excluded:** Google+ Local, the deprecated `#!` / `_escaped_fragment_` protocol, Google's no-longer-used `rel=next/prev` indexing signal, Google Authorship/AuthorRank as a ranking promise, mandatory 300-word pages or 70-character titles, one keyword per page, automatic disavow of backlinks, and guaranteed rich results.

## Webapp source: all major topic groups

| Topic in source | Coverage decision |
| --- | --- |
| UI/UX, browser variants, responsive design, accessibility, user-friendly errors, progressive enhancement | Existing UX, A11Y, TST; **new TST-084** tests blocked/disabled JavaScript and an appropriate fallback when applicable |
| Staging, version control, automated deploy, backup/restore, monitoring | Existing OPS, REL, OBS, LAUNCH, DOC |
| Security: injection, password hashing, XSS, CSRF, session hijacking, clickjacking, credit cards, least privilege | Existing SEC, LEG, DATA, and API/architecture checks, with current primary standards |
| User-generated link spam | **New SEO-077** maps appropriate `ugc`, `sponsored`, and `nofollow` according to provenance |
| Redirect-after-POST / duplicate form submissions | **New APID-120**: use a safe browser navigation pattern such as HTTP 303 where appropriate, plus server-side idempotency for consequential mutations |
| Caching, gzip, resource optimizations, CDN, load speed, images, JavaScript | Existing PERF, REL, frontend release and performance tools; recommendations are conditional |
| SEO links, robots, sitemap, canonical, crawlable content, analytics | Existing SEO/ANL, plus SEO-074–078 |
| HTTP, HTML semantics, JS behaviors, deployment platform, resource dependencies | Existing ARC, DOC, APID, TST |
| Error handling, logs, feedback, incident response, backups | Existing OBS, REL, DOC, TST, security and operations |

**Obsolete or non-universal practices excluded:** Google escaped-fragment AJAX crawling, HTML5 AppCache, mandatory CSS sprites, unconditional script concatenation or cookie-free static domains, legacy IE/Opera browser versions, mandatory XHTML, vendor-specific dated performance utilities such as YSlow, and a universal requirement that JS-driven applications work without scripting.

## Tool and reference coverage

The SEO checklist recommends [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/), [Rich Results Test](https://search.google.com/test/rich-results), [Google Search Console](https://search.google.com/search-console/about), [Bing Webmaster Tools](https://www.bing.com/webmasters/about), [Schema Markup Validator](https://validator.schema.org/), [PageSpeed Insights](https://pagespeed.web.dev/), [Playwright](https://playwright.dev/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Vitest](https://vitest.dev/), and other applicable validation libraries. Testing adds [Chrome DevTools disable-JavaScript instructions](https://developer.chrome.com/docs/devtools/javascript/disable); API workflow checks reference [MDN 303 See Other](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303) and browser E2E tests.

Prefer current Google Search Central documentation for [pagination](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview), [local business data](https://developers.google.com/search/docs/appearance/structured-data/local-business), [outbound link attributes](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links), [JavaScript indexing](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), and [structured-data constraints](https://developers.google.com/search/docs/appearance/structured-data/sd-policies). Use MDN HTTP documentation for submission flow behavior.

## Limits and follow-up process

All **major topic groups and recommendations in the two named source files** were assessed as already covered, newly added, or excluded for clear applicability/currency reasons. This does not mean every resource linked by the larger israelroldan index has been fetched or that any tool-based tests were run against a real application. Continue evaluating linked resources individually; add a check only if it introduces an independently verifiable, presently relevant requirement not already covered by an existing ID. Preserve global ID uniqueness, scoped ownership, and evidence-based release gates.


## Supplemental audit (2026-11-13): Marco Biedermann SEO and Docker Secure Deployment

Sources: [Search Engine Optimization](https://github.com/marcobiedermann/search-engine-optimization/blob/main/readme.md) and [Docker Secure Deployment Guidelines](https://github.com/strozfriedberg/Docker-Secure-Deployment-Guidelines/blob/master/README.md).

| Source topics | Coverage decision |
| --- | --- |
| SEO URL structure, indexability, content, keywords, headers, mobile, media, sitemaps, social metadata | Existing SEO, UX, A11Y and PERF checklists; no hard keyword-density, content-length, title-length, mandatory plugins or ranking promises |
| Website/app linking and native-app promotion | New SEO-079, with Apple/Android domain association, deep-link destination and fallback tests |
| Destination-specific social sharing previews | New SEO-080; existing SEO-020/041 cover generic metadata |
| SEO tools for webmasters, analytics, crawlers, social validation, competition, keywords and platform plugins | Existing Search Console, Bing, Lighthouse, PageSpeed, Rich Results Test, Schema Markup Validator; newly referenced Screaming Frog, WebPageTest, Meta Sharing Debugger, Google Trends, Moz Keyword Explorer; other vendor tools, bookmarklets, CMS-specific plugins, and historical books/courses remain optional, not universal release gates |
| Docker daemon/API, Linux namespaces and privileged containers | New SEC-086–088, verified against current official Docker daemon access and rootless/userns documentation |
| Docker seccomp, SELinux/AppArmor, capabilities, SUID/SGID | New SEC-089; default hardening coverage already exists in SEC-026 |
| Docker host mounts, devices, cgroups, network isolation and inter-container communication | New SEC-090–092; tested boundaries instead of obsolete link/ICC flags |
| Container image origin/signing, vulnerabilities | New SEC-093 complements existing SEC-015 and OPS-032 |
| Host/kernel patching, security audits/logging, failure resilience, sensitive services, tenant isolation | Existing SEC/OPS/OBS/REL checklists; site-specific evidence required |

**Outdated guidance excluded:** Google sitelinks search boxes were retired in 2024; legacy meta-keyword percentages, exact 300-word rules, universal subdomain preference, always-add-title-to-links, authorship ranking claims, fixed text-length limits, and nofollow for every external link are not current SEO requirements. Old Docker 1.x LXC driver invocation, the assertion user namespaces/seccomp are unavailable, legacy --icc=false / --link isolation, and recommendations to use privileged Docker-in-Docker as isolation were not imported. Rootless mode and modern seccomp support are documented in current Docker documentation. Do not assume all optional vendor tools or CMS extensions are maintained or warranted.

This audit covers the principal topic groups of the two named source README files. It does not test actual production Docker configurations or verify every link in the SEO tool catalog.


## Supplemental review (2026-11-13): README and website launch

Sources: [ddbeck/readme-checklist](https://github.com/ddbeck/readme-checklist/blob/main/checklist.md) and [Tuts+ Website Launch Checklist for Web Designers](https://github.com/tutsplus/Website-Launch-Checklist-for-Web-Designers/blob/master/launch_checklist.md).

| Source topic | Existing coverage or new check |
| --- | --- |
| README naming, heading, project description, URL, author or organization | Existing DOC-002/003, supplemented by **new DOC-120** for explicit responsible owner and working public link |
| README project usage and distribution rights | Existing LEG/IP and contributor checks, supplemented by **new DOC-121** on discoverable usage/license terms |
| README prerequisites, installation, basic examples, documentation links, support, contribution, table of contents, skimmability, review cadence | Existing DOC-003, DOC-014, DOC-022–042, DOC-064–082 and DOC-119; **new DOC-122** for independent end-to-end README-first-use verification |
| Launch content spelling, placeholders, contact, legal notices, client approval | Existing UX, LEG, DOC and LAUNCH-119; **new LAUNCH-126** for final representative production content and accountable acceptance |
| Launch compatibility, icon, 404, redirects, functional links, forms, JavaScript, validation, accessibility, sitemaps, SEO, analytics, security and performance | Existing TST, SEO, SEC, A11Y, PERF, LAUNCH; **new LAUNCH-127** for actual receiving-mailbox routing and confirmation on production contact forms |
| Launch hosting, backup/restore, uptime monitoring, policy/legal terms and IP obligations | Existing REL, OPS, OBS, LEG and LAUNCH |
| Client deliverables (live site, style guide, design assets, site export and access) | **New LAUNCH-128** for contract-appropriate handover and ongoing ownership |
| Launch-day staffing, incident response, communication and post-launch maintenance | Existing LAUNCH-004/017/081, OPS and REL; **new LAUNCH-129** for release windows tailored to actual staffing and recovery support |

**Tools:** Existing lychee, markdownlint-cli2, Playwright, browser/device testing, PageSpeed Insights, Lighthouse, and analytics tools cover the relevant workflows. Added explicit clean-environment README walkthrough and contact-form delivery verification; these require real-world evidence, not only automated scores.

**Obsolete or non-general prescriptions excluded:** unsupported Flash fallback guidance, blanket no-JavaScript requirements, keyword density and minimum 300-word SEO content, universal client contract/payment terms, mandatory twice-daily backups, fixed Monday–Wednesday launch slots, and unqualified claims that robots.txt protects sensitive/private information. Use authorization for confidential resources and documented recovery objectives for backups.

**Limitations:** This records topic-level review of both complete Markdown pages, not execution of their recommended tools or verification of client-specific contracts. Treat all new checks as conditional and preserve unchecked project-agnostic templates.


## Supplemental audit (2026-11-13): Strong Node.js and DataMade Site Launch

**Sources:** [jesusprubio/strong-node](https://github.com/jesusprubio/strong-node/blob/main/README.md) and [datamade/site-launch-checklist](https://github.com/datamade/site-launch-checklist/blob/master/README.md).

| Source section | Coverage or addition |
| --- | --- |
| Strong Node errors (safe messages, handling, fatal process state) | Existing SEC-069, OBS/REL/OPS; **new SEC-094** verifies safe Node fatal-error shutdown and independent supervisor recovery |
| Strong Node input/output (XSS, SQL, CSRF, headers, uploads, paths, dynamic execution, ReDoS) | Existing SEC, API/DATA and header/validation checks; **new SEC-095** makes Node-specific execution/path/regex sinks testable |
| Strong Node auditing/logging, sensitive redaction, privilege and auth events | Existing OBS, SEC and API checks; no broad vendor-specific logging mandates added |
| Strong Node cryptography, authentication, authorization, session cookies | Existing SEC/LEG controls; **new SEC-097** covers durable Express production session stores, proxy configuration and revocation |
| Strong Node environment (CI, npm lockfiles, vulnerabilities, lifecycle scripts, fuzzing, OS privilege, incident plans, testing) | Existing OPS/SEC/TST; **new SEC-096** addresses Node/npm dependency-install script trust and CI boundaries |
| DataMade load tests, caching, deployments, DNS/TLS, search, analytics | Existing PERF, OPS, SEO, ANL and LAUNCH checklists; Locust, Lighthouse and search webmaster tooling already covered |
| DataMade site accessibility and browser/mobile QA | Existing A11Y, UX, TST checks; optional axe-core, Accessibility Insights, BrowserStack added to launch verification tools |
| DataMade robots/sitemaps and staging | Existing SEO-006–010, LAUNCH-117; **new LAUNCH-130** clarifies staging authentication and production/staging directive separation |
| DataMade sharing metadata and preview card | Existing SEO-020/041/080; **new LAUNCH-131** verifies a launch-ready real share preview and image URL |
| DataMade favicon, custom 404/500, print stylesheet, README instructions | Existing SEO-078, UX-103, frontend UX/TST, DOC-120–122 |

**Current corrections:** Avoid obsolete X-XSS-Protection recommendations, blanket disabling of all caches/ETags, continuing normal operation after uncaught Node exceptions, unqualified default framework recommendations, or relying on robots.txt to keep confidential staging sites private. Prefer current Node.js, Express, npm, OWASP, and Google documentation; require actual evidence rather than automatic certification. The two source READMEs were reviewed by subject, not every linked third-party project or penetration-testing utility fetched and independently validated.


## Supplemental audit (2026-11-13): Eight-point SEO + GEO launch readiness

User-supplied eight topics mapped to stable checks:

| Launch topic | Existing checks or additions |
| --- | --- |
| Custom domain for long-term growth | **SEO-081** — optional strategic control and migration plan, not a direct ranking boost |
| HTTPS and canonical URL per page | SEO-010, SEO-016, SEO-081 |
| Sitemap and Search Console | SEO-009, SEO-029 |
| Googlebot and targeted AI-search crawler access | SEO-006, SEO-007, GEO-047, **GEO-079** |
| Important text in crawlable HTML | SEO-013, SEO-061, GEO-019 |
| Titles, structured data, author and organization | SEO-014, SEO-018, SEO-027, **GEO-080** |
| Original useful referenceable content | SEO-003, GEO-013 |
| Legitimate references and consistent brand mentions | **SEO-082**, GEO-017, GEO-030 |

The eight-line reference is published in `lists/frontend/20_Release_and_LaunchReadiness.md`; existing checks are not duplicated. New genuine scope additions: **SEO-081, SEO-082, GEO-079, GEO-080**.

**Evidence interpretation:** crawlability and useful original content are foundational for public discovery; accessible HTML, citations, credible authorship, and accurate visible-content-matching structured data remain important. These priority labels are operational guidance, not publicly documented search ranking weights. A branded custom domain can improve ownership, portability and clarity, but neither `github.io` nor `pages.dev` has a proven direct ranking handicap merely from its hostname suffix. Google explicitly states [Google Search doesn't use `llms.txt`](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), including generative AI features. `llms.txt` can optionally support other consumers; it is not a mandatory Google Search or AI visibility task. Refer to [Google's AI-features guidance](https://developers.google.com/search/docs/appearance/ai-features), [crawler overview](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers), and [site migration guide](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes). Entity matching and citations by third-party AI providers remain uncertain and cannot be guaranteed through consistent profile/schema naming alone.

## Supplemental audit (2026-11-13): Eight Instagram reels on launch, legal and security

**Provenance:** User-supplied reel URLs; author/topic identified from accessible captions and transcripts on 2026-11-13. Original publication dates were unavailable. Claimed comment/DM-only prompts generally were not accessible; the provided [Next Alphabet episode link](https://www.nextalphabet.com/build/episodes/5) was not verified in full. The reels are leads, not technical standards or legal advice.

| Reel / creator | Coverage decision |
| --- | --- |
| [Dd8beLqSP-Y — Kush Desai](https://www.instagram.com/reel/Dd8beLqSP-Y/) | Children's data LEG-019; fonts/third-party transfers LEG-040; subscription disclosures LEG-021/065; **new LEG-073/074, ANL-146** for DMCA agent, commercial email and session-replay privacy |
| [Ddb8FK7S0wy — Krishanu](https://www.instagram.com/reel/Ddb8FK7S0wy/) | Policies, cookie/form consent, data minimization, SDKs, deception, A11Y, rights, licensing: existing LEG, A11Y, UX, ANL, DATA; no duplicate check |
| [DecGaf1A4Fe — Krishanu](https://www.instagram.com/reels/DecGaf1A4Fe/) | Mobile/browser/forms/links/performance/HTTPS/SEO/sharing/payments/backups: existing LAUNCH, SEO, TST, PERF, SEC; **new LAUNCH-133** for verified sender domain and mail delivery |
| [Ddv_d_sPx4l — Aashish Pahwa](https://www.instagram.com/reel/Ddv_d_sPx4l/) | Privacy, policies, cookies, accessible UI, deceptive claims, copyright: existing LEG, A11Y, UX; no duplicate check |
| [DePJrTNgh3b — Krishanu](https://www.instagram.com/reels/DePJrTNgh3b/) | API keys, auth, admin, XSS, headers, databases, dependencies: existing SEC, DATA, APID; strengthened **SEC-019/071** for historical secrets and privileged actions |
| [Decehkfh711 — Manvendra Kumar](https://www.instagram.com/reel/Decehkfh711/) | RLS, IDOR, API authorization, rate limiting, uploads, CORS, webhooks: existing DATA-128/129, SEC-045/049/061/070/071, APID-089 |
| [DeUKCUDtprn — Rahul Singh](https://www.instagram.com/reels/DeUKCUDtprn/) | Terms/privacy, trademark clearance, Apple/Google store privacy labels: existing LEG-008/013/020, LAUNCH-124; strengthened **LEG-008** and added **LAUNCH-132** |
| [DeD0tDvJu0i — Teju](https://www.instagram.com/reel/DeD0tDvJu0i/) | Meta tags, social sharing, favicons, sitemap, robots, image speed, 404, responsive UI, forms: existing SEO, PERF, TST, LAUNCH-117/127/131 |

**Verified primary sources:** [USPTO trademark clearance](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks), [U.S. Copyright Office DMCA directory](https://www.copyright.gov/dmca-directory/), [FTC CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), [Apple privacy details](https://developer.apple.com/app-store/app-privacy-details/), [Google Play Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en), [Clarity recording masking](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking), [GitHub secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning), [Gmail sender guidelines](https://support.google.com/mail/answer/81126).

**Not adopted:** Promotional per-violation penalty figures as universal risks; asserted flat DMCA agent fees; universal CAPTCHA and age-gate mandates; claims that Claude automated fixes guarantee compliance or a flawless launch. Context and applicable jurisdiction govern requirements.

**Inventory impact:** +5 distinct checks (2 shared, 2 frontend, 1 backend). **92 files / 4,178 unique checks**.

## Supplemental audit (2026-11-13): Four security reels, five pasted images and attached guidance

**Sources reviewed:** [BreakingBreach API-spend](https://www.instagram.com/reels/DfPWAoNS0AL/), [techwithprateek OWASP-style](https://www.instagram.com/reels/DfPOALGyaWR/), [Cooked Dev](https://www.instagram.com/reels/DfCZB0kIZh7/), [BreakingBreach pre-launch](https://www.instagram.com/reels/DfEpwT9SRHe/) (accessible reel captions/transcripts), five user-pasted screenshots from [@aiwithshivang](https://www.instagram.com/p/Deimr_DgWk5/) (original post deliberately not loaded), and the [supplied Google Doc](https://docs.google.com/document/d/1VfPgsPy8DMi68Zck9z8B5511MCN3uSQGjeWqhRHLnDs/edit) attributed there to Mike/@mikenwo.ai (dated October 31, 2026). Reviewed November 13, 2026; original dates for reels/images unavailable. Extra comment/DM-gated resources not accessed. The linked document's template-file creation instructions were out of scope; substantive security controls were assessed.

| Source and atomic topic | Decision (stable IDs, not folder-local numbers) |
| --- | --- |
| API-spend: exposed keys, rotation and environment separation | Covered SEC-019/074, APID-043 |
| API-spend: fake signups, trials, bot checks, verification SMS/emails | Revised SEC-010/063; covered SEC-048, COST-103 |
| API-spend: per-IP/user limits, concurrent calls and metered tokens/models | Covered SEC-062, COST-091/095, SERVE-069/094/095/098 |
| API-spend: quota bypass by simultaneous calls | **New COST-127** (atomic reservation and race test) |
| API-spend: retries, duplicate calls, permanent failures | Revised COST-092/093; covered SEC-070, SERVE-074 |
| API-spend: scheduled overlap, recursive triggers, job timeouts and batch limits | Revised COST-093; covered REL-028/034, COST-089/090 |
| API-spend: zip bombs, huge images, signed file access and temp deletion | **New SEC-099/100**; covered SEC-049, DATA-082, MULTI-102/104 |
| API-spend: tenant/service spend alerts and hard stop | Covered COST-030–036/100/102; **new COST-128** |
| OWASP-style: SQL/command/deserialization and prompt injection | Covered SEC-012/036/038/095 and AI guardrail checks |
| OWASP-style: RLS, mass assignment, privilege escalation | Revised DATA-128; covered SEC-007/058/060/061 |
| OWASP-style: redirects, XSS, CSP, clickjacking, stack traces | Covered SEC-072/073/077/082; revised SEC-069 |
| OWASP-style: secrets, admin logs, debug and token expiry | Covered SEC-019/026/059/071/074 |
| OWASP-style: password hashes, malicious/invented dependencies and SRI | Revised SEC-006/015/047; **new SEC-098** |
| OWASP-style: public storage buckets | **New SEC-100**, covered SEC-025/049 |
| Cooked Dev: keys, Git leaks, public DB keys, server auth, RLS, encryption | Covered SEC-007/019/020/022/074; revised DATA-128 |
| Cooked Dev: ownership, field tampering, cookie sessions and hashing | Covered SEC-058/060/075; revised SEC-006/009 |
| Cooked Dev: login bot control, SQL/XSS, inputs and API response minimization | Revised SEC-010; covered SEC-012/060/065/072/080 |
| Cooked Dev: files, headers, HTTPS and vulnerable packages | New SEC-099; revised SEC-015/021; covered SEC-027/049/073 |
| BreakingBreach prelaunch: authentication, admin routes, history secret scan, monitoring | Covered SEC-006/007/019/030/061/071 |
| BreakingBreach prelaunch: reset tokens, CSRF, validation, sessions | Revised SEC-009/010; covered SEC-012/065/075/076 |
| BreakingBreach prelaunch: server-side price and payment verification | **New SEC-101**; covered SEC-070 |
| BreakingBreach prelaunch: uploads, dependencies, production debug and security testing | New SEC-099; revised SEC-015; covered SEC-017/018/026/049/055 |
| @aiwithshivang images: HTTPS, HSTS, mixed content | Revised SEC-021; covered SEC-075 |
| @aiwithshivang images: cookie flags, inactivity, rotation and logout | Revised SEC-009; covered SEC-075/083 |
| @aiwithshivang images: API auth, minimized responses and safe errors | Revised SEC-069; covered SEC-007/060/079 |
| @aiwithshivang images: outdated, unused or risky dependencies | Revised SEC-015; new SEC-098 |
| Attached Google Doc: session resets, role/tenant checks and data isolation matrix | Revised SEC-009/DATA-128; covered SEC-007/043/058/089 |
| Attached Google Doc: webhook checks, secrets, threat modeling and negative tests | Covered SEC-002/012/019/031/054/055/070, APID-046/048, TST-050/063 |

**Primary validation:** [OWASP API4](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/), [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [MDN TLS/HSTS](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Transport_Layer_Security), [MDN SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity), [GitHub dependency review](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request), [Stripe card-testing protection](https://support.stripe.com/questions/how-do-i-prevent-card-testing-attacks?locale=en-GB) and [Stripe checkout fulfillment](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted). Security checks are conditional on applicable product features and are not certification.

**Not adopted as universal rules:** exactly 30-minute idle expiry, mandatory SameSite=Strict, CAPTCHA on every form, HSTS preload on all hosts, promises of zero overspend, blind trust in CVE-free or AI-suggested packages, frontend redirects as proof of payment, or claims that AI audits guarantee safety. Original screenshot post and gated resource not opened.

**Inventory:** +6 new checks (SEC-098–101, COST-127–128), 11 revised checks; 92 files / 4,184 unique checks (727 shared, 634 frontend, 1,116 backend, 1,707 AI).

## Supplemental review (2026-11-13): Cloudflare security-audit skill

**Source and provenance:** [Cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), a public Cloudflare GitHub repository. Reviewed its [README](https://github.com/cloudflare/security-audit-skill/blob/main/README.md) and [actual skill instructions](https://github.com/cloudflare/security-audit-skill/blob/main/skills/security-audit/SKILL.md) on 2026-11-13. The repository describes a six-phase agent-assisted audit: architecture reconnaissance; coverage-led hunting; independent candidate validation; machine-readable finding records; fresh-source verification; and reports. Codebase audit requests use full audit mode; security advice and focused reviews use guidance mode.

| Candidate | Existing coverage and decision |
| --- | --- |
| Run a codebase security audit using Cloudflare's security-audit skill | **Revised SEC-017 in `05_Security.md`** to mention the optional tool and evidence-backed audit and finding verification. Existing SEC-017 already required static analysis, secret scanning, and risk-based dynamic/penetration testing; adding a duplicate ID would violate deduplication guidance. |
| Produce verifiable coverage, separate confirmed/needs-validation/rejected findings, and track fixes | Strengthened **SEC-017**; related existing **SEC-018/055** cover security regression testing and release-linked evidence. No new ID. |
| Execute untrusted target-controlled tests under strict OS-level isolation; avoid live systems | Documented the tool's sandbox, restricted execution and prerequisites in **`05_Security.md` Suggested testing tools**. This is a tool-specific safety condition, not a universal requirement to install this particular skill. |

**Limitations:** The skill was reviewed, not installed or run against any codebase. It requires appropriate tooling and an OS-enforced sandbox for local target-controlled builds/tests. A missing sandbox means the skill should retain an unresolved validation blocker rather than executing unsafe tests. Automated or agent-generated reports are evidence leads, not security certification. No new IDs, file renames, or additional template files; repository total remains **4,184 unique checks across 92 scope files**.


## Supplemental audit (2026-11-13): Six Instagram SEO/GEO reels and linked resources

**Provenance and limitations:** All six reel transcripts/captions were obtained via Insta Loader; publication dates were not established, and review occurred 2026-11-13. The Telugu reel transcript is incomplete. The linked fullbytedeveloper.com SEO page was unavailable; DM- or pinned-link-only extras were not fetched. Social recommendations are leads, not standards. No agent skill, MCP, automation, or production website was installed, executed, or audited.

| Source | Extracted independent topics | Decision and stable IDs |
| --- | --- | --- |
| Vibha: [reel](https://www.instagram.com/reel/DZVsGZGt8dd/) + [setup guide](https://vibha-ramprakash.github.io/seo-geo-tracker/) | Auditor, Search Console, Core Web Vitals, AI citation sampling, answer gaps, schema, robots rules, llms.txt, fixes, recurring comparisons | Existing SEO-006/009/018/022/029/030/031/034/036/047 and GEO-001/002/024/025/031/032/033/052/053/079; **revised SEO-031**. Do not mandate an audit score, llms.txt, daily runs, or claims of top rankings. |
| Udayan: [launch reel](https://www.instagram.com/reel/Dd6qP9CRxax/) | Search Console, sitemap, Bing, robots, Analytics, Business Profile, titles/descriptions, mobile, PageSpeed, reviews | Existing SEO-007/009/014/021/022/029/030/043/069/071/076; **revised SEO-029** for target-engine diagnostics; **new SEO-083** for eligible local profile accuracy and review handling. |
| Kamil: [reel](https://www.instagram.com/reel/DexHMFmx4Ev/) + [resource page](https://fullbytedeveloper.com/seo) | SEO audit, GEO, JSON-LD schema, programmatic SEO pages, blog production | Existing SEO-002/003/018/028/035/040/063/066 and GEO-006/021/031/032/033; **new SEO-084** for pre-index validation of generated page batches. Resource page inaccessible, so exact skills/install commands not verified. |
| Ritu: [reel](https://www.instagram.com/reel/Dd5Y9roxjWn/) | Technical SEO, AI search, keywords, site audits, competitor home/product URL crawling | Covered by SEO-002/006/018/028/029/031 and GEO-001/002/031/032/033. Competitor scraping and unseen pinned list of ten skills are not universal obligations; check rights and access conditions independently. |
| Pramodh: [reel](https://www.instagram.com/reel/DVfEh18koyo/) + [seo-geo skill](https://skills.sh/resciencelab/opc-skills/seo-geo) + [ai-seo skill](https://skills.sh/coreyhaines31/marketingskills/ai-seo) | SEO/GEO skills, crawler accessibility, content structure, schema and AI visibility sampling | Covered by SEO-018/029, GEO-001–021/031–033/047–053/079/080 and AI GEO-024/025. Added optional seo-geo review-aid link in frontend GEO; ai-seo was already listed. Reel transcript in Telugu was garbled, so detailed claims are attributed to linked pages only. |
| Udayan: [SEO schedule reel](https://www.instagram.com/reels/DenK3zzhHOC/) | Daily: rankings, reviews, leads, uptime. Weekly: blogging, Search Console, internal links, business updates. Monthly: audit, refresh, backlinks, AI citations | Existing SEO-004/011/028/030/031/034/047/082, GEO-031/032/033/052/053 and relevant OBS/REL/ANL; **revised SEO-031**, **new SEO-083**. Exact daily/weekly/monthly tasks and backlink quotas are suggestions, not universal requirements. |

**Primary verification (reviewed 2026-11-13):** [Google AI features](https://developers.google.com/search/docs/appearance/ai-features) (ordinary Search eligibility and no special AI markup); [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies) and [AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) (people-first value, scaled content and doorway abuse); [Google Business Profile eligibility](https://support.google.com/business/answer/3038177) and [customer reviews](https://support.google.com/business/answer/3474050); [Bing Sitemaps](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed) and [URL Inspection](https://www.bing.com/webmasters/help/url-inspection-55a30305). Linked skill pages were inspected as third-party references, not verified efficacy or official mandates.

**Outcome:** New **SEO-083**, **SEO-084**; revised **SEO-029**, **SEO-031**, all in `lists/frontend/13_SEO.md`. Optional `seo-geo` review-aid link added to `lists/frontend/14_GEO_and_AEO.md`. No new GEO ID, vendor mandate or checked template. **91 scope files / 4,186 unique checks** (682 root, 681 frontend, 1,116 backend, 1,707 AI).


### Classification follow-up (2026-11-13): Separate questionable tactics from standard checklists

The six-reel audit was re-examined for potentially unethical or unsupported tactics. Details on scaled AI/programmatic page production, scraping-and-republishing, link schemes/quotas, fake business engagement, attempts to game AI citations, speculative `llms.txt` ranking claims, and unreviewed auto-publishing workflows now live in [`seo-aeo-geo-tricks.md`](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md) as **cautionary reference material, not checklist requirements**. `lists/frontend/13_SEO.md` retains the protective **SEO-084** quality gate but no longer names a programmatic content-production tactic. The newly introduced `resciencelab` skill reference and optional `llms.txt` factor row were removed from `lists/frontend/14_GEO_and_AEO.md`; the skill and experimental-file context are cataloged only in the caution reference, while existing safeguards such as **AI GEO-025** remain. Ethical **SEO-083**, **SEO-029** and **SEO-031** are unchanged. No IDs were moved, deleted or added; totals stay **91 files / 4,186 checks**.


## Supplemental coverage audit (2026-11-13): Five additional reels — parasite SEO, UX, CRAWLKIT and outreach

**Review scope:** Reels #7–#11 shared after the previous SEO/GEO update. Original reel publishing dates were not reliably supplied; reviewed 2026-11-13. Reel summaries/captions were previously retrieved through the Instagram video loader. The complete David Roberts 11-tactic Google Doc was accessible (Drive metadata created 2026-10-26, modified 2026-10-28). The creator-promised 50-tactic Avi playbook and inaccessible/gated material were **not** audited. Primary validation used Google Search spam/AI-content policies, the original Unlighthouse/Lighthouse CI/web-vitals repositories, and the WordRocket provider MCP documentation. Techniques are assessed individually; mention is not endorsement.

### Source A: David Roberts — parasite SEO

**Provenance:** [Instagram reel](https://www.instagram.com/reels/De-IHn-Bf8t/) and [complete 11-tactic Google Doc](https://docs.google.com/document/d/1_a-meFPIdCw9_Y-wzELji4Ht9E9OYmD9fHxYfV3DHVE/edit?usp=sharing). The central 'borrow domain authority and rank in two weeks' claim is not an assured mechanism or result. Each accessible tactic was classified as follows.

| Atomic source recommendation | Existing check / disposition |
| --- | --- |
| Publish next-year comparisons early | Existing SEO-002/003/028 and GEO-009/015: original comparisons with actual evidence are allowed; predicted ranking dominance excluded |
| Upload ostensibly academic 'research' to Zenodo for citations | Existing SEO-028 and GEO-012/014/016; misleading pseudo-scholarship moved to risk file |
| Use short LinkedIn answer articles | Existing GEO-006/007 and SEO-028; mandatory 330-word tactic not adopted |
| Create ~20 Gamma decks for query variations | Existing SEO-084 and GEO-037; indexable thin/duplicative scaled pages flagged in risk file |
| Answer relevant Reddit threads with product mentions | Existing SEO-082 and GEO-026/035; authentic helpful participation only, spam flagged |
| Publish hosted Google comparison sheets with own product first | Existing GEO-011/016/026; biased self-ranking flagged as disclosure/accuracy risk |
| Retain keyword URL slug by editing LinkedIn titles | Already covered by SEO-028/016; no justified new checklist or tactic endorsement |
| Publish useful Chrome extension | Existing UX/SEC/DOC/LAUNCH where applicable; an actual product is fine, not a Google-domain ranking guarantee |
| Buy aged website and redirect for inherited ranking | Existing SEO-032/048/081 and Google spam policies; expired-domain abuse added to risk file |
| Publish public GitHub README/Pages/awesome list | Existing DOC-014 and SEO-003/028; value and truthful attribution matter, not domain reputation |
| Answer underserved Quora queries | Existing SEO-082 and GEO-001/002; real expert answers, avoid spam |

### Source B: Krishanu — twenty UI enhancements

**Provenance:** [Instagram reel](https://www.instagram.com/reels/DfmnzMlAhqh/), caption enumerates 20 features. These are conditional product decisions, not universally necessary or SEO ranking requirements. No new check added; the already existing **UX-103** explicitly tests printing.

| Feature | Existing coverage and scope |
| --- | --- |
| Dark mode | A11Y-096/102; UX-048; optional, test contrast and theme behavior |
| Cookie banner | ANL-128/129 and UX-100; actual consent where applicable |
| Site search | UX-025/028/029/099; only where it aids discovery |
| Back-to-top | UX-023/025 and A11Y-022; optional navigation convenience |
| Mobile menu | UX-031/084/087 and A11Y-026/101 |
| Loading animations | UX-039–041/095 and A11Y-104; truthful state and reduced motion |
| Hover states | A11Y-022/103 and UX-048; cannot be hover-only |
| Scroll progress bar | UX-022/048; optional and should not distract |
| Copy button | UX-037/039 and A11Y-028/059; verify actual clipboard outcome |
| Print stylesheet | UX-103; explicitly covered |
| Sticky header | A11Y-024/096 and UX-097; must not obscure focus/content |
| Skip to content | A11Y-092; explicitly covered |
| Password visibility | A11Y-028/093 and UX-037/094; appropriate toggle semantics |
| UTM tracking | ANL-128/130/136, SEO-030; privacy-aware campaign attribution |
| Form success state | UX-039/092, A11Y-059/100, LAUNCH-127 |
| Form error state | UX-047/089/090, A11Y-051/067 |
| Confirmation modal | UX-042/044/051 and A11Y-026/101 |
| Last updated date | SEO-034 and GEO-015/044; genuine dates, not fabricated freshness |
| Expandable FAQ | GEO-010, A11Y-028/101; actual user questions and keyboard operability |
| Floating contact button | UX-019/025/097, A11Y-024; optional, avoid blocking content |

### Source C: Kamil Kamili — CRAWLKIT

**Provenance:** [Instagram reel](https://www.instagram.com/reel/DfVDkD8lUka/) and supplied [Lighthouse](https://github.com/GoogleChrome/lighthouse), [Unlighthouse](https://github.com/harlan-zw/unlighthouse), [lychee](https://github.com/lycheeverse/lychee), [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci), [web-vitals](https://github.com/GoogleChrome/web-vitals) and [Search Console](https://search.google.com/search-console) references. Creator reports testing only Lighthouse, Unlighthouse and lychee on a small owned test site; no independent audit outputs were supplied. It would be improper to import the reported SEO scores, timing or broken-link count as universal benchmarks.

| Atomic source recommendation | Existing check / disposition |
| --- | --- |
| Lighthouse single-page SEO | SEO-014/017/018/025/063/067; Lighthouse already in optional testing tools, score is diagnostic only |
| Unlighthouse multi-page scan | Existing SEO-031/036, PERF-037/039; added optional sampled site-audit tool references |
| lychee broken-link scan | SEO-011/012 and documentation testing; added optional HTML/Markdown checker reference |
| Lighthouse CI per commit | OPS-109, PERF-039/106; CI tool already in performance appendix, clarified configuration and thresholds |
| web-vitals real-user signals | SEO-022/043 and PERF-038/039/040/088/089; added optional RUM integration reference |
| Single-page fixes: description, alt text, descriptive links | SEO-014/017/011/067, A11Y-030/037; already covered |

**Tool caveats:** Unlighthouse uses smart sampling and currently requires Node >=22.18 according to its upstream README. Lighthouse CI requires a configured `lighthouserc` **and** an actual CI job; `lhci autorun` by itself does not schedule per-commit runs. The web-vitals npm package requires integration of metric callbacks and a receiving/reporting pipeline; installation alone does not collect field data. Keep a 75th-percentile view of LCP/INP/CLS for real traffic, and distinguish lab audits from RUM. Run active site crawling only against owned or authorized targets.

### Sources D and E: expert journalism and Claude/WordRocket link-building

**Provenance:** [foundr0 journalist answers reel](https://www.instagram.com/reels/DfVX-VUxHSi/) mentions [Featured](https://featured.com/) and [SERPtag](https://serptag.com/). [Avi backlink/Claude reel](https://www.instagram.com/reels/DfVED1fOvbk/) mentions [WordRocket MCP](https://app.wordrocket.ai/docs/public-api/mcp-server) and [creator's resource page](https://digitalcreatoravi.com/free/seo?k=skills). The link to the promised 50 tactics was not available as the complete material; no exact install flow or output was run or verified. WordRocket's own documentation confirms a remote MCP service, available publishing capabilities, and plan-scoped API access; this is not a finding that its output secures backlinks.

| Atomic recommendation | Existing check / disposition |
| --- | --- |
| Authentic journalist request responses (Featured) | Revised SEO-082 for independently selected expert coverage; a quote or link is not guaranteed |
| Backlink/rank tracking (SERPtag) | Existing SEO-031/082; vendor-specific capability and comprehensive backlink detection not verified |
| Unlinked brand mentions and polite attribution requests | Revised SEO-082; no coercion, quota, or mass-solicitation requirement |
| Guest articles and resource-page pitches | Revised SEO-082; editorial independence, quality and disclosures required |
| Relevant product references on Reddit/LinkedIn/YouTube | Existing SEO-082/028; automated promotional posting excluded and cataloged in risk file |
| WordRocket-assisted content and Claude MCP integration | Existing SEO-003/028/084 and agent/vendor security review; tool is optional, publishing needs human review |
| 50 ranked backlink tactics promised via gated playbook | Not audited because content unavailable; not adopted |

**Classification:** The ethically useful discovery/research/pitch process is retained by **revised SEO-082** in `lists/frontend/13_SEO.md`. Manipulative third-party-hosted ranking schemes, fake research, disguised comparisons, link schemes, keyword-slug gaming, expired-domain ranking transfers, and mass AI outreach are cataloged only in [`seo-aeo-geo-tricks.md`](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md) as cautionary scenarios, not recommended implementation tasks. Changes to `lists/frontend/13_SEO.md` and `lists/frontend/12_Performance_and_Scalability.md` only add optional tools and clarify existing requirements.

**Primary evidence checked (2026-11-13):** [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies), [Google AI-generated content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [Unlighthouse repository README](https://github.com/harlan-zw/unlighthouse), [Lighthouse CI configuration](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md), [web-vitals README](https://github.com/GoogleChrome/web-vitals/blob/main/README.md), [WordRocket MCP docs](https://app.wordrocket.ai/docs/public-api/mcp-server), and the established [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) for optional UI controls. All detailed upstream versions, claimed rankings, or vendor efficacy were **not** independently benchmarked.

**Inventory:** Revised **SEO-082**; no new stable IDs and no duplicates; **91 scope files / 4,186 unique checks** (682 shared, 681 frontend, 1,116 backend, 1,707 AI). Main checklists remain unchecked. The separate risk catalog is not a checklist and is excluded from inventory.


## Supplemental review (2026-11-13): Tim / Keytomic — claims of ChatGPT-generated backlinks

**Source:** [Instagram reel](https://www.instagram.com/reels/DfikXW5BcXQ/) by Tim (`@tim_keytomic`) and the separately supplied [Keytomic landing page](https://keytomic.com/) plus [Keytomic MCP documentation](https://keytomic.com/docs/mcp). **Publication date:** not confirmed. **Review date:** 2026-11-13. **Source limitation:** The reel's accessible metadata says "ChatGPT can really get us backlinks now??" and asks viewers to comment SEO for a tool, but its extracted transcript is **empty**. Do not infer a detailed in-video procedure or that backlinks were actually obtained.

| Claim or promoted capability | Verification, existing controls and disposition |
| --- | --- |
| ChatGPT/AI can "get backlinks" | The reel poses this as a promotional question, not a documented demonstration. `lists/frontend/13_SEO.md` **SEO-082** already requires genuine, independently selected editorial links and actual referrals; AI-proposed outreach cannot guarantee placements. Added provider-neutral caution to the separate questionable-tactics reference, not a new recommended checklist step |
| Backlink audits and high-DR link opportunities | Keytomic's own site advertises backlink discovery and opportunities, not a demonstrated ability to cause external sites to link. SEO-031/082 already cover monitoring and link quality. No automated link creation, rankings or editorial acceptance verified |
| Reddit AI brand-mention agent | Vendor advertises finding conversations and **drafting** replies, while some pricing copy markets "daily Reddit AI brand authority automation". No direct evidence the product posts autonomously was established. If used for bulk undisclosed promotional replies or links, SEO-028/082 anti-spam controls apply; a research/draft aid is not itself unethical |
| AI-generated articles and CMS publishing | Vendor advertises recurring AI content and one-click CMS publishing. SEO-003/028/084 already require independently useful content, factual checks, distinct page purposes and non-manipulative publication. Do not prescribe a universal quota or unreviewed direct-to-production changes |
| "Instant auto-indexing" | The phrase appears on the vendor landing page; Google's own crawling/indexing FAQ states that indexing cannot be guaranteed and sitemap submission is merely a hint. Existing SEO-029 explicitly rejects guaranteed indexing. Treat the marketing claim as unverified rather than accept it as a search-engine capability |
| "ChatGPT citations generated" / AI citation tracking | Vendor promotes AI visibility tracking and citation-style counters, but no methodology, audited sample, causal efficacy or independent citations from the reel were provided. Existing GEO-031/032/033/052/053 call for dated reproducible sampling and separating measured citations from ranking, referrals and conversions; no promised AI inclusion |
| Remote MCP connector for ChatGPT/Claude | Official provider guide describes authenticated audits, Google Search Console reads and sitemap submission within account/project permissions; it does **not** document a guaranteed backlink-creation tool. Vet third-party OAuth scopes, data retention, CMS writes and human approvals under existing integration/security reviews; not added to recommended skill/tool lists |

**Policy comparison:** [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies) expressly list automated programs or services creating ranking links as link spam and address low-value scaled content. [Google Search crawling/indexing FAQ](https://developers.google.com/search/help/crawling-index-faq) rejects indexing guarantees. [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features) gives no special required AI-only SEO optimization or inclusion guarantee. Keytomic documentation is a **vendor description, not an independent test**. No service connection, payment, link placement, or publishing action was made.

**Disposition:** Two conditional caution rows and a provenance note added to [`seo-aeo-geo-tricks.md`](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md); legitimate existing SEO-082/029/084 and GEO measurement controls retained unchanged. **No new or revised numbered check** and no changes to checklist inventory (**91 files / 4,186 unique checks**). The creator or product is **not accused** of having performed prohibited behavior; concerns are hypothetical implementations and unsupported guarantees.


## Supplemental coverage audit (2026-11-13): Reels #12–#18 and user-supplied backlink screenshot

**Scope and provenance:** This batch covers seven new reels since the previously consolidated five-reel SEO update. Reel #19 (Tim / Keytomic) was already separately recorded in the preceding source audit and risk register, so is **not** counted twice. Original publishing dates were unavailable. Review date **2026-11-13**. Where reel captions/transcripts were previously retrieved, decisions are grounded in their available text. One reel (#13) had an accessible [full PDF](https://drive.google.com/file/d/18D1yjZBmh0jZ5qyHqcxiTzpgS3M4r-MU/view), which was re-read. User-provided tier-chart labels were assessed as a screenshot, with no reel retrieval. Four creator resource pages could not be fetched; no gated claims or exact numbered lists were invented.

### Reel #12 — Pawan Rochwani: durable SEO/AEO/GEO distribution

Source: [Instagram reel](https://www.instagram.com/reels/DcJAcTfNdTu/); the caption supplies five strategies, and the audio mainly explains why distribution and platform assumptions change.

| Strategy | Existing coverage and outcome |
| --- | --- |
| Publish genuine first-party research, benchmarks and original industry data | Covered by GEO-012/013/014/015 and SEO-003/028; no fabricated statistics or automatic AI-citation claims |
| Become a trusted community participant without spam | SEO-082, SEO-028 and GEO-026; legitimate replies only, no minimum 'months without links' rule |
| Build topical expertise rather than follower count | GEO-005/014 and SEO-002/003; platform algorithm simplifications and ranking promises unverified |
| Provide authentic quotations to journalists | Revised earlier SEO-082 covers editorial sourcing, accurate credentials and independent selection; no guaranteed link or bypass of publisher crawl restrictions |
| Structure website content as clear, evidence-backed answers | GEO-001/002/006/007/009/042 and SEO-003; snippets not guaranteed |

### Reel #13 — Suket: five-method parasite SEO PDF

Sources: [Instagram reel](https://www.instagram.com/reels/DfhVC3Gg5PU/) (no retrievable transcript) and [Google Drive PDF 'Pageone, no website'](https://drive.google.com/file/d/18D1yjZBmh0jZ5qyHqcxiTzpgS3M4r-MU/view) (retrieved in full; dated 9 November 2026 as the author's example/search-check date, not proof of reel publication).

| PDF method / guardrail | Existing check / decision |
| --- | --- |
| Upcoming-year buyer comparisons grounded in actual updated prices and testing | SEO-002/003/034 and GEO-009/015; an unused future-year query does not guarantee ranking; misleading freshness rejected |
| Deposit real product-derived, properly anonymized empirical research on Zenodo | GEO-012/013/043, SEO-028 and privacy/data review; confirmed [Zenodo's unsuitable-content policy](https://support.zenodo.org/help/en-gb/2-content/141-what-content-is-not-suitable-for-zenodo) disallows promotional pseudo-research and AI-only fabrications |
| Publish direct-answer LinkedIn articles with meaningful sources | GEO-006/007/009, SEO-003; no universal ideal word count or AI citation guarantee |
| Publish a relevant Gamma deck and ensure platform discoverability where permitted | SEO-084/GEO-037/SEO-028; unique substance only, not decks scaled solely by keyword; paid plan/platform claims not treated as permanent defaults |
| Answer real Reddit questions; identify one's own product and respect rules | SEO-082/028 and GEO-026; no promotional spam or automated link placement |
| Five safeguards: independently useful, authentic authorship, affiliation disclosures, fewer better pages, realistic indexing delays | Existing SEO-003/028/029/084 and GEO-014/031; adopted as already-covered safeguards, not five redundant boxes |

### Reel #14 — Ritik Namdev: '24 free backlinks'

Sources: [Instagram reel](https://www.instagram.com/reels/DfiWwOzDF7D/) and [linked resource](https://ritiknamdev.com/resources/free-backlinks) (**resource page inaccessible**). The audio/caption identifies **17** named services; the remaining seven of the advertised 24 were not verified.

| Platform group | Classification and existing check |
| --- | --- |
| Eligible business profiles (Google Business Profile, Bing Places, Apple Business Connect, Yelp, LinkedIn, YouTube) | SEO-083/SEO-082: only real, eligible, audience-relevant profiles; no promise of ranking value |
| Product/review discovery (G2, Clutch, Trustpilot, Product Hunt) | SEO-082/083/028: genuine product listings, accurate details, real reviews; independent eligibility applies |
| Useful content or answers (GitHub, Medium, DEV, Reddit, Quora) | SEO-003/028/082, GEO-026: original contribution, disclosed connection and host-community policies; no spam |
| Editorial quote sourcing (Featured, Qwoted) | SEO-082: authentic expert participation, editorial decision and measured mentions; no guaranteed article/backlink |
| '24 free links by this weekend' | Claim not verified: profile links are not necessarily crawlable, editorial, followed, free or beneficial; do not add a quota or promise |

### Reel #15 — Ritik Namdev: redesign URL migration

Sources: [Instagram reel](https://www.instagram.com/reels/DfVew84gj42/), [unretrievable 21-point checklist + map](https://ritiknamdev.com/resources/redesign-seo-checklist), and [Google's current site-move guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes). The reel advocates an old-to-new map; the exact claimed 21 checks could not be audited.

| Relevant instruction | Checklist update |
| --- | --- |
| Inventory and map old URLs to genuinely equivalent new destinations before a move | **Revised SEO-032** for URL inventory, baselines, approved mapping and removals; no redirect mandate when URLs unchanged |
| Test permanent redirects, canonical destinations, 404/410 and updated internal links/sitemaps | **Revised SEO-048** with actual HTTP verification, final URLs, indexing rules, no chains/irrelevant homepage redirects |
| Keep actual migration redirects for generally at least one year; monitor old/new traffic and indexing | **Revised SEO-048/032** using Google's official guidance; linked new [optional project worksheet](../frontend/references/seo-redesign-url-map-template.md). Temporary fluctuation is not proof of failure |
| Protect staging/production differences and deploy a safe release | Already LAUNCH-117/130 and SEO-029; no new release checklist IDs |

### Reel #16 — Ritik Namdev: topic map

Sources: [Instagram reel](https://www.instagram.com/reels/DfngWYQEZ8y/) and [unavailable starter template](https://ritiknamdev.com/resources/topic-map). The reel proposes one real service, buyer questions, a primary service page, related supporting pages and contextual internal links. **Revised SEO-002** to make this planning testable; SEO-005/011/033 and GEO-001/002/005/037 already cover information architecture, linking, unique intent and topic depth. 'Eight planned posts beat twenty random posts' is a creator opinion, not an SEO numeric standard; do not manufacture extra pages or insist that every child must always link to one parent.

### Reel #17 — tier-ranked backlinks screenshot from user

Source: [Instagram reel link supplied with screenshot](https://www.instagram.com/reels/DfCfb08gR6W/); the user explicitly said the screenshot was sufficient. The visible screenshot labels, **not a fetched transcript**, were: S 'worth citing'; A 'Business Profile' / 'Journalist requests'; B 'Broken links' / 'Resource pages' / 'Product Hunt'; C 'Guest posts'; D 'Link swaps' / 'Directories'; F 'Buying links' / 'PBNs' / 'Comment links'.

| Tiers / candidate | Coverage / caution |
| --- | --- |
| S/A: cite-worthy resources and genuine business/editorial presence | SEO-003/028/082/083; no automatic link quality or guarantee |
| B: relevant broken-link/resource research and legitimate product launches | SEO-012/082, user benefit and editorial choice; avoid intrusive bulk link swaps |
| C: independent, relevant guest contributions | SEO-082, SEO-077; not a blanket ban on guest articles |
| D: reciprocal links and directories | Ordinary mutual references/eligible directories may be fine; excessive exchanges and low-quality directories are in risk catalog |
| F: purchased ranking links, PBNs and comment-link spam | Google link-spam examples; classified as avoid rather than recommended steps. Qualified advertising links are distinct |

**Caution:** S–F tiers are subjective creator judgments, **not a Google-defined scale**.

### Reel #18 — Srikanth Kishan: Google-owned domain link shortcuts

Sources: [Instagram reel](https://www.instagram.com/reels/DfZcjXsqsnV/) (Telugu auto-transcript partially garbled, caption states the four tactics) and [linked article](https://itsmy.website/blog/free-backlinks-get-cited-by-chatgpt) (**not retrievable**).

| Tactic | Evidence and disposition |
| --- | --- |
| Chrome Web Store extension with website link | SEO-003/028 and app quality/security/release checks: a useful maintained extension is legitimate, but the store's domain is no ranking shortcut |
| Public Google Doc targeting a competitor keyword | SEO-028/084/GEO-011: independent, accurate comparison is fine; thin keyword-targeted link farm / borrowed authority caution added |
| Thin Google Sites page with a 'Visit this website' link | SEO-003/084: real microsites may be useful; a link-only doorway is a risky manipulation |
| Search Console Community post for a backlink | [Official community guide](https://support.google.com/webmasters/community-guide/290502373) explicitly says forum links are `nofollow` with no SEO benefit and prohibits promotional drops; documented as **not a backlink tactic**, not recommended |
| 'Free Google backlinks' that get ChatGPT citations | No independent evidence; Google's [AI Search guidance](https://developers.google.com/search/docs/appearance/ai-features) requires ordinary eligibility and offers no special citation guarantee |

### Batch verification and remaining limitations

Primary references rechecked 2026-11-13: [Google Search spam/link policies](https://developers.google.com/search/docs/essentials/spam-policies), [Google Search SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [Google internal-link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), [Google site-move guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), [Search Central community participation](https://support.google.com/webmasters/community-guide/290502373), and [Zenodo disallowed content](https://support.zenodo.org/help/en-gb/2-content/141-what-content-is-not-suitable-for-zenodo). The creator resource pages and absent reel transcripts remain limitations. No social platform, backlink product, third-party ranking result, exact '21' / '24' count, or AI citation promise was independently certified.

**Outcome:** Existing **SEO-002**, **SEO-032** and **SEO-048** clarified; all other recommendations were covered, qualified or rejected as unsupported. Added the optional non-checklist [`lists/frontend/references/seo-redesign-url-map-template.md`](../frontend/references/seo-redesign-url-map-template.md); added link-scheme and Google-hosted shortcut cautions to [`seo-aeo-geo-tricks.md`](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md). Reel #19/Keytomic already had its own source audit and no duplicate edits were made. **No added or deleted check IDs: 91 scope files, 4,186 unique checks** (682 shared, 681 frontend, 1,116 backend, 1,707 AI).


## Supplemental audit (2026-11-14): Alex Chen — 20-step SEO checklist and Claude audit prompt

**Intake and provenance:** User supplied [Instagram reel](https://www.instagram.com/reels/DfonmYuOGZj/) and [Chen Media's linked 20-step guide](https://chen.media/guides/the-20-step-seo-checklist-that-gets-your-website-onto-google). **Guide author:** Alex Chen (`@nocodealex`). **Reel publication date:** not confirmed. **Reviewed:** 2026-11-14. The Instagram media loader failed and the reel page could not be fetched directly, so the **linked guide is the directly inspected source**; do not claim its audio or any inaccessible instructions were verified. The web guide displayed all 20 numbered items and the visible audit-and-fix prompt. Its further 'How to check your work', 'The catch', 'Sources', and email-only setup material are gated/not available for this review.

**Guide premise:** Make a website discoverable and provide a Claude Code prompt that audits 20 items, shows a pass/fail table, then fixes failures one by one and retests. This describes a possible development workflow, **not a proof of Google indexing or a safe unattended fixer**. Existing `AGENTS.md` review procedure and frontend SEO/test/release checks require reproducible evidence, project-specific N/A decisions, and human approval.

### Complete 20-item source-to-check mapping

| Guide section / numbered recommendation | Existing coverage and resolution |
| --- | --- |
| Search visibility / crawl: 1. `noindex` on eligible pages | SEO-006/064; review intentional indexability per environment, not ban deliberate exclusions |
| Search visibility / crawl: 2. Canonical URL tags | SEO-010/063; use canonicals correctly on duplicate/variant URLs rather than forcing identical declarations everywhere |
| Search visibility / crawl: 3. `robots.txt` rules | SEO-006/007; avoid accidental blocks, but robots.txt is not privacy access control |
| Search visibility / crawl: 4. XML sitemap | SEO-009/029; list canonical indexable URLs as relevant, **not every site URL** and not a ranking/indexing guarantee |
| Search visibility / crawl: 5. HTTPS | SEO-024; verify real TLS/mixed-content behavior rather than inferring safety only from the padlock |
| Search visibility / crawl: 6. Google Search Console ownership + sitemap submission | SEO-029/031; confirm access and inspect actual crawl/index diagnostics; submission is not a guarantee |
| Page metadata / semantics: 7. Unique page titles (guide suggests 50–60 characters) | SEO-014/063; useful differentiated titles matter, but Google's title-link documentation sets **no mandatory character limit** |
| Page metadata / semantics: 8. Meta descriptions | SEO-014/063; prioritize important pages; descriptions can help snippets, but Google may select on-page text instead |
| Page metadata / semantics: 9. One `h1` per page | SEO-015/067; clear primary heading and hierarchy already covered; exactly one `h1` is not a standalone Google ranking requirement |
| Page metadata / semantics: 10. Ordered `h2`/`h3` headings with no skipped levels | SEO-015/067 and accessibility; logical heading order improves user/screen-reader comprehension, but Google says heading order is not a ranking requirement |
| Page metadata / semantics: 11. Short readable URL slugs | SEO-016; stable, understandable URLs, do not rename good URLs merely for keywords |
| Page metadata / semantics: 12. Structured data / JSON-LD | SEO-018/040/066; **supported, applicable types** consistent with visible content only; not mandatory on every page |
| Page metadata / semantics: 13. Image alternative text | SEO-017/067 and A11Y-037/038; meaningful alt for informative images, decorative images handled appropriately; avoid stuffing |
| Page metadata / semantics: 14. Open Graph sharing image | SEO-020/080; conditional social previews, not a direct Google ranking requirement |
| Performance / usability: 15. Compress and resize images | SEO-023, PERF-046/092; retain image quality, responsive sizes and supported formats where useful |
| Performance / usability: 16. Mobile usability | SEO-021/071, A11Y and LAUNCH-108; representative devices and responsive interaction testing |
| Performance / usability: 17. Core Web Vitals LCP/INP/CLS | SEO-022/043/069, PERF-038/039/040; field p75 segmented mobile/desktop and lab/field distinction; passing metrics alone does not guarantee rankings |
| Performance / usability: 18. Broken links | SEO-011/012, SEO-072; verify important links and relevant errors using representative scan evidence, not an unproven claim that a scan catches all |
| Trust / discovery: 19. Descriptive internal links | SEO-005/011/062; help people and crawlers reach relevant pages |
| Trust / discovery: 20. Legitimate backlink plan | SEO-082/077/083; independently earned editorial references, accurate profiles and qualified sponsored/UGC links without schemes or guaranteed ranking effects |

### AI-assisted workflow and source corrections

| Guide recommendation or claim | Evaluation and disposition |
| --- | --- |
| Prompt Claude Code for a pass/fail SEO audit and individual fixes | Existing review/verification workflow already requires evidence and retesting; audit results must be independently checked. Publishing edits to `robots.txt`, canonicals, redirects, metadata, schema, or sitemap without review can deindex/break a real site. Existing `SEO-028/029/084`, launch and test controls suffice; strengthened the **reference-only** caution in the risk catalog rather than making automatic fixes a checkbox |
| '50–60 characters' for each title | Google's [title-link documentation](https://developers.google.com/search/docs/appearance/title-link) states there is no fixed `<title>` length limit; title results may be truncated by device width. Do not create a mandatory numeric requirement |
| 'One `h1`' and never skip `h2`/`h3` | Clear structure and logical headings are good for people/accessibility; Google's [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) says the number/order is not an ideal SEO ranking factor. Keep existing SEO-015 and A11Y review instead of rigid Google rules |
| 'Schema markup' and 'alt text on every image' | Use supported schema only when relevant and consistent with visible content; meaningful alt for informative imagery and appropriate empty alt/semantics for decoration. The guide does not establish universal applicability; see SEO-017/018 and A11Y-037/038 |
| 'Sitemap lists every page' and 'all broken links fixed' | Sitemap should list relevant preferred canonical indexable URLs, not blocked, duplicate or intentionally excluded pages. Audit and fix material broken links with evidence; no crawler demonstrates every possible external link is permanently reachable |
| 'Open Graph image' and backlink plan as necessary to get onto Google | Social preview metadata is optional and not a direct ranking signal; artificial backlink quotas, purchases and mass promotion are excluded. See SEO-020/080/082 |
| 'Pass Core Web Vitals' as a promise of ranking | Core Web Vitals are measured contextually at p75 and are one part of user experience, not a certification of rank/index status. See SEO-022/043 and PERF-039/040 |

**Primary documentation reviewed 2026-11-14:** [Google Search SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide); [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link); [Google meta descriptions/snippets](https://developers.google.com/search/docs/appearance/snippet); [Google structured-data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) and [structured-data rules](https://developers.google.com/search/docs/appearance/structured-data/sd-policies); [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies); and [web.dev Web Vitals](https://web.dev/articles/vitals). These are constraints on implementing the source ideas, not content claimed to appear in the creator's guide.

**Outcome:** **All 20 visible guide recommendations already have appropriate check IDs** in `lists/frontend/13_SEO.md` and related performance, accessibility and launch scopes. **No new numbered checks, no existing check edits**, and no extra SEO score or universal title/heading/markup obligations. Expanded only the separate information-only risk note for unrevised AI auto-fix prompts and documented per-item coverage. Counts remain **91 populated scope files / 4,186 unique checks** (682 root, 681 frontend, 1,116 backend, 1,707 AI).


## Supplemental audit (2026-11-14): Lawrence Hitches — GITZ seven free SEO repositories

**Original source:** [Instagram reel](https://www.instagram.com/reels/De3lwqQzv29/) and linked [GITZ seven-repo guide](https://www.lawrencehitches.com/watch/gitz/), credited to Lawrence Hitches. **Source dates:** The guide reports the repository details and comparison prices were checked 2026-10-24; no reliable reel publication date was available. **Reviewed:** 2026-11-14. The Instagram transcript loader failed and the reel page was unavailable, so the **complete linked guide** is the directly verified material, not a claimed audio transcription.

**Source thesis:** Seven open-source SEO/analytics/crawling tools can replace some tasks of paid tools. It explicitly acknowledges server hosting costs and notes that Unlighthouse, lychee and Crawl4AI are laptop-friendly, while SerpBear, SEOnaut, Umami and Plausible Community Edition require service hosting. Some subscription prices and vendor feature comparison claims are time-sensitive and were **not** independently checked against each paid competitor's live price sheet. The guide's phrase 'runs Lighthouse on every page' does not account for Unlighthouse's documented smart sampling.

### Complete tool-by-tool coverage map

| Source item | Verified capabilities / caveat from upstream | Existing checks and disposition |
| --- | --- | --- |
| 1. SerpBear (`towfiqi/serpbear`) | Self-hosted rank tracking and optional Search Console metrics; upstream README says Google ranking checks use SERP scraping APIs or proxy IPs | **Revised SEO-031**: check data-source authorization and target provider policies, avoid mandatory daily rankings. Added a conditional warning in the risk register; not listed as an approved default rank-scraping tool. |
| 2. SEOnaut (`StJudeWasHere/seonaut`) | Self-hosted SEO crawler and audit tool for links, metadata, redirects; Docker Compose and MySQL | SEO-011/012/014/031/035/036 already cover diagnostics; added as an **optional, authorization-scoped** SEO audit reference. Review example Docker passwords and exposed ports rather than copying insecure defaults. |
| 3. Unlighthouse (`harlan-zw/unlighthouse`) | Multi-page Lighthouse runner with smart sampling, operated locally | Already referenced in `lists/frontend/13_SEO.md` and `lists/frontend/12_Performance_and_Scalability.md`; **not** evidence of testing every URL. No duplicate recommendation. |
| 4. Umami (`umami-software/umami`) | Open-source privacy-oriented analytics, available self-hosted or cloud | Existing ANL-124–145 and root ANL governance cover goals, event QA, privacy, identity, consent, retention and measurement gaps. Added optional implementation in frontend analytics tool appendix. |
| 5. Plausible Community Edition (`plausible/community-edition`) | Self-hosted lightweight analytics with Docker/ClickHouse system requirements | Same existing analytics IDs; added as optional frontend analytics tool with legal/operational caveats. Community Edition may differ from paid cloud; infrastructure, HTTPS, updates and database are maintained by deployer. |
| 6. lychee (`lycheeverse/lychee`) | Local/CI link checking for HTML, Markdown and websites | Already in `lists/frontend/13_SEO.md` optional toolkit, SEO-011/012 and documentation tests. External links may intermittently fail or be inaccessible; do not promise exhaustive link coverage. |
| 7. Crawl4AI (`unclecode/crawl4ai`) | Browser-powered extraction/crawling; can turn page content into structured/Markdown text for downstream AI analysis | Legitimate for owned or authorized crawling; existing SEO-028/084 and data/privacy/security controls reject scraping/reposting without rights or user value. Kept as conditional caution rather than a required SEO tool. |

**Upstream project documentation checked:** [SerpBear](https://github.com/towfiqi/serpbear) explicitly states it relies on third-party SERP scrapers/proxies for Google result collection; [SEOnaut](https://github.com/StJudeWasHere/seonaut) covers site crawls with a Docker/MySQL setup; [Unlighthouse](https://github.com/harlan-zw/unlighthouse) uses smart sampling; [Umami](https://github.com/umami-software/umami) offers self-hosted/cloud analytics; [Plausible CE](https://github.com/plausible/community-edition) requires Docker and a supported ClickHouse CPU plus adequate RAM; [lychee](https://github.com/lycheeverse/lychee) checks links; and [Crawl4AI](https://github.com/unclecode/crawl4ai) extracts web content for downstream applications.

**Primary policy distinction:** [Google Search Central spam policies](https://developers.google.com/search/docs/essentials/spam-policies) state that machine-generated Google Search queries for rank checking without express permission violate policies. A third-party scraper API is not automatic permission. Crawling one's own site or a duly authorized site is distinct from scraping search results or copying protected third-party content. Deployment of 'privacy-friendly/cookieless' analytics must still be checked against actual data collection and applicable privacy/consent law; see ANL-068–085 and ANL-128–145.

**Decision:** Existing SEO-011/012/014/022/029/031, PERF-037–040 and ANL privacy/measurement checks already cover tool outcomes. **Revised SEO-031** to require compliant rank-measurement sources. Added **SEOnaut** as a conditional optional site-audit tool, and **Umami/Plausible CE** as optional frontend analytics implementations. Unlighthouse/lychee remain already referenced. SerpBear/Crawl4AI are documented for review, not recommended as universal or unvetted scraping tools. Risk scenarios live exclusively in [`seo-aeo-geo-tricks.md`](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md). **No new checklist IDs**; inventory remains **91 populated scope files / 4,186 unique checks** (682 root, 681 frontend, 1,116 backend, 1,707 AI).


## Supplemental audit (2026-11-14): Four Claude Code SEO repositories and image-carousel intake

**Sources:** User linked [Instagram reel](https://www.instagram.com/reels/DfDdLPMDQFa/) and explicitly identified four repositories. The Instagram media extractor failed and no reel transcript was available, so the repository list and actual upstream README/security/privacy pages are the direct evidence; spoken demonstrations, installation results and personal SEO outcomes are **not verified**. Repository project metadata and main-branch README files were inspected on **2026-11-14**, and the tools were **not installed or executed**. This audit separates feature descriptions from supported standards, independent measurements and recommended baseline requirements.

### Source-by-source coverage map

| Repository | Verified upstream scope / limitations | Existing check and disposition |
| --- | --- | --- |
| [Claude SEO](https://github.com/AgriciDaniel/claude-seo) by AgriciDaniel | SEO technical/crawl audits, site speed, content, schema, GEO, local and reporting via 26 sub-skills/19 subagents; optional extension APIs and browser setup. README notes data travels through Claude Code and third-party extensions where configured; documented SSRF/browser and install-signature residual risks. | Existing SEO-003/018/029/031/084, GEO-031–033/052–053, AGENT-023–048 and release/testing controls. Optional audit aid only; do not import proprietary success metrics or automatic publishing as mandatory checks. Risk reference entry added. |
| [GEO SEO Claude](https://github.com/zubair-trabzada/geo-seo-claude) by zubair-trabzada | Multi-subagent AI visibility, brand/crawler and schema audits, PDF/client reports, `llms.txt` generator, 'citability' calculation. Publishes weighted 0–100 score (25% citability, 20% brand, 20% E-E-A-T, 15% technical, 10% schema, 10% platform) and 134–167-word passage recommendation. | Existing GEO-001–017, GEO-031–033/047–053, SEO-018/028; no empirically established citation probability from score. Google's AI guidance says special markup/`llms.txt` and content chunking not required. Risk reference only; not added to recommended list. |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) by ChromeDevTools | Inspect and control Chromium, network/console/screenshot/performance traces from agent clients. The project's README says the MCP client can see/alter browser content, and official configuration documents `--no-usage-statistics`, `--redact-network-headers` and URL allow/deny controls; statistics enabled by default. | Existing AGENT-023–048, SEC-051/083/084, PERF-037–040, SEO-013/036; added to optional SEO diagnostic appendix with browser-profile isolation and sensitive-data constraints. Debugging is not ranking/citation evidence. |
| [Search Console MCP](https://github.com/saurabhsharma2u/search-console-mcp) by saurabhsharma2u | Aggregates Google Search Console, Bing Webmaster, GA4 and AdSense with OAuth. README describes read-only default, optional explicit write-scope authorization, property-resolution fixes and heuristic (not official) GenAI-query insights. IndexNow and Google's Indexing API differ, and `indexing_submit` is not a guarantee of general URL indexing. | Revised SEO-029 for correct property resolution, least-privilege OAuth, independent write approval and eligible URL submissions; existing AGENT-023–048 and GEO-033/053 handle security/measurement. Added as optional diagnostic connector, not a required SEO service. |

### Cross-cutting platform and safety validation

- [Google Search's current AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) states that special AI files such as `llms.txt` and content chunking are not required for Google Search/AI features. [AI feature eligibility](https://developers.google.com/search/docs/appearance/ai-features) remains based on ordinary Search eligibility, not a vendor-specific GEO score.
- [Google's Indexing API](https://developers.google.com/search/apis/indexing-api/v3/using-api) is restricted to `JobPosting` or `BroadcastEvent` embedded in `VideoObject` pages. An accepted URL notification is not an indexing confirmation. Sitemap processing and Google Search Console API access are distinct.
- [Official Chrome DevTools configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration) documents default-on usage statistics and controls for allowed/blocked URL patterns, network-header redaction and opting out of telemetry. Agent/browser access to live customer sessions needs a separate authorization and privacy decision.
- Both audit bundles are third-party agent code, not official Search requirements. README examples and provider-reported performance/traffic/citability claims were **not independently reproduced**. `Claude SEO` documents optional external API disclosures and known residual URL-fetch/browser supply-chain risks; `GEO SEO Claude` documents weighted proprietary scoring and retains runtime prospect/report data. Existing AI tool/agent risk gates and source validation already cover these concerns.

**Disposition:** **Revised SEO-029** in `lists/frontend/13_SEO.md` for correct webmaster-property resolution, least-privilege read scopes, approved write/submission actions and no indexing guarantee. Added **Chrome DevTools MCP** and **Search Console MCP** as conditional, version-reviewed optional diagnostics in the SEO appendix. Added four classified risk/tool rows with no allegations of misconduct; **Claude SEO/GEO SEO Claude remain in the informational risk register, not default recommended skills**. No new checklist IDs, check states or release gates were altered. Repository inventory stays **91 scope files / 4,186 unique checks**.

### Additional user screenshot carousel — completed review (2026-11-14)

**Source:** The user supplied nine visible screenshots from [@swiperightai's Instagram carousel](https://www.instagram.com/p/Dfi6VdzlNB1/) (one cover and **eight** project cards) and instructed **not to load the post**. The cards themselves, not a fetched Instagram caption or transcript, are primary evidence for the names, screenshots' approximate GitHub star labels and short claimed use cases. Review date 2026-11-14; post publication date not verified. We checked each named project's current GitHub metadata and README, corrected two image URL errors, and reviewed overlapping existing checklist IDs. Stars are a changeable popularity metric, **not** evidence of product effectiveness, code security or rank/citation improvement. Neither projects nor skills were installed or connected.

| Card and original screenshot claim | Upstream verification/correction | Checklist and disposition |
| --- | --- | --- |
| **1. Geo-Sleuth**, '6k stars', `Oldcircle/geo-sleuth`; infer photo location from skylines, satellite, maps | [Actual repository](https://github.com/Oldcircle/geo-sleuth) is a visual OSINT photo-geolocation agent, **not Search SEO or GEO**. Its README explicitly limits responsible use to owned/permitted photos and warns against locating non-consenting people; EXIF metadata is not needed for its visual inference | **Revised `MULTI-037`** in `lists/AI/13_Multimodal_AI_Quality.md` with visual-location inference and permission/granularity tests. Complements existing MULTI-010/012/030/031, security and privacy checks. **Excluded from SEO tools**, despite the image being grouped with SEO examples |
| **2. OpenSEO**, '26k stars', `every-app/open-seo`; Semrush/Ahrefs alternative | [Verified upstream](https://github.com/every-app/open-seo): keyword research, rank/backlink data, SEO tooling, MCP, hosted/Cloudflare/Docker variants. Its documentation requires a **paid DataForSEO API key** for self-hosted SEO data, warns that the **first visitor can claim the initial admin account**, and describes other optional service costs | Existing SEO-029/031, SEC and AGENT permissions cover results and secure integrations. Added a **conditional optional SEO research-tool reference** in `lists/frontend/13_SEO.md` with first-admin hardening, provider/query permission, real cost and validation caveats; no blanket feature parity |
| **3. SEO Machine**, '7k stars', `TheCraigHewitt/seomachine`; research, write, update and optimize | [Verified upstream](https://github.com/TheCraigHewitt/seomachine) is a Claude Code editorial workspace with research, draft, rewrite, metadata, internal-link, performance and draft-publication flows; optional GA4/GSC/DataForSEO, Docker/credentials and Claude API costs. Its own quality scores are internal workflow metrics, not Google certification | **Revised `SEO-004`** to require an accountable human editor to fact-check public AI content **and generated metadata before publication**, backed by [Google Search's AI-content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content). SEO-003/028/084, AGENT-043 and release controls already block unsupported mass publication. Conditional risks documented separately, no generic content quota |
| **4. Open SEO MCP Skills**, '9k stars', screenshot path `Ryze-AI-Agent/open-seo-mcp-skills` | **Screenshot URL contains a misspelling:** verified working repository is [`Ryze-AI-Adgent/open-seo-mcp-skills`](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) (**Adgent**). Skills call a **hosted Ryze remote MCP connector** with GSC, GA4, Google Ads and third-party DataForSEO, not a fully local free SEO data warehouse. README claims AI-referral traffic indicates cited pages; that is **not evidence of an observed answer/link citation** | **Revised `GEO-033`** to separate measured referral traffic from observed AI citations. SEO-029/031 and AGENT-023–048 already cover OAuth, provider permissions, data access and costs. Remote vendor integration remains a conditional risk reference, not a required tool |
| **5. Claude SEO**, '27k stars', `AgriciDaniel/claude-seo` | [Verified repository](https://github.com/AgriciDaniel/claude-seo) and security/privacy documents were **fully reviewed in the prior four-tool audit**. Local skills process content inside Claude Code; optional external APIs and browser/installer risks apply. No official AI-citation readiness guarantee | Already covered by the previous `SEO-029` / AGENT and SEO controls, prior audit and risk catalog. **No duplicate check/tool entry** |
| **6. Marketing Skills**, '59k stars', `coreyhaines31/marketingskills` | [Verified repository](https://github.com/coreyhaines31/marketingskills); existing `seo-audit`, `ai-seo`, and `schema` SKILL.md paths still resolve. The current README covers SEO, marketing, CRO, advertising and content workflows with optional integrations; repo popularity is not vetting | **Already linked** in `lists/frontend/13_SEO.md` and `lists/frontend/14_GEO_and_AEO.md` as optional review aids. No duplicate skill, checklist ID or popularity-based mandate |
| **7. NotFair**, '4k stars', screenshot `nowork-studio/NotFair`; SEO/GEO tied to GSC, ads and code | Screenshot link/name is **not** the active GitHub repository. Verified path: [`nowork-studio/notfair-plugin`](https://github.com/nowork-studio/notfair-plugin). README describes workflows that can work with **Google/Meta/other ads**, GA4/GSC, WordPress and GoHighLevel CRM, including privileged changes via connected accounts | Existing SEO-029/030, AGENT-023–048, privacy, advertising and deployment/release checks already govern OAuth scopes and external writes. Document risk of connecting paid-ad, site-editing and CRM authority to a general AI agent; **not** a default SEO requirement |
| **8. GEO SEO Claude**, '11k stars', `zubair-trabzada/geo-seo-claude` | [Verified upstream](https://github.com/zubair-trabzada/geo-seo-claude) and score methodology **already reviewed in the prior four-tool audit**. 0–100 citability scores, fixed 134–167-word target and `llms.txt` recommendations are vendor heuristics, not Google's AI Search eligibility requirements | Already GEO-031–033/052/053 and informational risk reference; reinforced **GEO-033** against substituting scores for observed citations. No new vendor-specific checklist rule |

**Across-card findings:** The carousel depicts eight GitHub projects, **not eight required SEO skills**. Two links in the supplied image require correction, two named tool bundles overlap the previous four-repository audit, and Marketing Skills was previously maintained. Screenshots' star counts were **not** copied as current metrics. Full repository security audits, vendor data-processing attestations, paid-provider pricing, software installations, remote OAuth connections, and SEO effectiveness tests were **not** conducted.

**Primary verification:** [Google Search's October 2026 AI-generated content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) calls for manual fact-checking before publication, including generated page metadata. [Google Search AI features](https://developers.google.com/search/docs/appearance/ai-features) documents ordinary eligibility and Search Console's aggregated Web search reporting; [Google's AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) rejects mandatory `llms.txt` and chunk sizing. [Privacy International's AI-geolocation research](https://privacyinternational.org/report/5736/nowhere-hide-privacy-risks-and-policy-implications-ai-geolocation/) documents inference risks without GPS metadata. Third-party README claims are identified as vendor descriptions, **not independent proof of rank improvements or AI citations**.

**Disposition:** Revised existing **SEO-004**, **GEO-033**, **MULTI-037**; added one conditional OpenSEO option and risk-reference entries. No new numbered check, no changes to 91 populated scope files or 4,186 globally unique checks. This section **supersedes the earlier pending-intake note** for the nine screenshots.



## Reconciliation since the last consolidated request (2026-11-14)

All subsequently supplied material was reviewed by source, including **previous commits**. Earlier updates remain in place and were not duplicated: [Alex Chen's 20-step SEO guide](https://www.instagram.com/reels/DfonmYuOGZj/) had all twenty items mapped and no new IDs (commit [`32dc737`](https://github.com/Pro-GenAI/awesome-checklists/commit/32dc7376e12c90e88915f05be5e98a5fe597b41b)); [Lawrence Hitches' seven-tool GITZ guide](https://www.instagram.com/reels/De3lwqQzv29/) had all seven mapped, **SEO-031** revised, and conditional SEOnaut/Umami/Plausible CE references added (commit [`87ebb074`](https://github.com/Pro-GenAI/awesome-checklists/commit/87ebb074a42300a1510c1e0805399bca319bd04d)); [the four Claude SEO tools](https://www.instagram.com/reels/DfDdLPMDQFa/) had all four verified from GitHub and **SEO-029** revised with optional Chrome DevTools/Search Console MCP references (commit [`43447f7`](https://github.com/Pro-GenAI/awesome-checklists/commit/43447f7fb8cb7d7a10b34b7c136aaa090f6b34bc)).

| Remaining reel | Evidence and status |
| --- | --- |
| [DfnE3jHjPvy](https://www.instagram.com/reels/DfnE3jHjPvy/) | Retried Instagram extractor 2026-11-14; internal failure. Public indexed caption/transcript not located. **No verifiable source claims; no checklist adoption.** Original caption or supplied screenshot needed |
| [Dey_dvNIBD6](https://www.instagram.com/reels/Dey_dvNIBD6/) | Retried Instagram extractor 2026-11-14; internal failure. Public indexed caption/transcript not located. **No verifiable source claims; no checklist adoption.** Original caption or supplied screenshot needed |

The nine-slide [@swiperightai carousel](https://www.instagram.com/p/Dfi6VdzlNB1/) is **now fully extracted from the user-supplied images** in the prior section; Instagram was intentionally **not fetched**, per user request. The two inaccessible reels remain genuinely unreviewed, rather than implied to have been audited. **No checklist counts were increased for tools, screenshots or risk notes.**


## Supplemental audit (2026-11-14): Anylancer five free Claude Code SEO skills and subsequent reel retries

**Discovery material:** The user pasted the full five-skill install/usage guide titled **“5 FREE SEO SKILLS FOR CLAUDE CODE”**, attributed to [Anylancer.com](https://anylancer.com/), alongside [Instagram reel DfEg0iKyaqQ](https://www.instagram.com/reels/DfEg0iKyaqQ/). The guide says its README commands were checked **6 November 2026**; that is the guide's stated check date, not a separately verified publication date. The Instagram media extractor subsequently returned an **empty media response**, so the video's spoken content was **not** authenticated. This audit uses the **user-provided text** for the five names/claims/commands and individually fetched **current upstream README and skill files** on **14 November 2026** for verification. It does not treat a sponsored/creator marketing message as a standard or independent performance study.

### Five-point source-to-existing-check audit

| Supplied item | Independently verified upstream capability and limitations | Coverage and disposition |
| --- | --- | --- |
| **1. [Claude SEO](https://github.com/AgriciDaniel/claude-seo)** by AgriciDaniel; `/plugin marketplace add`, `/plugin install`, `/seo setup`, `/seo audit`, `/seo page` | README documents Claude Code plugin with **26 sub-skills/19 agents**, audit and page commands, browser/runtime setup, MIT licensing; optional APIs, Claude execution costs and third-party processing remain possible. The reel video was unavailable. | **Already covered** by the [four-project Claude/MCP audit](#supplemental-audit-2026-11-14-four-claude-code-seo-repositories-and-image-carousel-intake), SEO-004/013/018/022/029/031 and AGENT-023–048. No new check or duplicate mandatory tool. Prior claims of fast audits/AI visibility are not guarantees. |
| **2. [GEO SEO Claude](https://github.com/zubair-trabzada/geo-seo-claude)**; `curl .../install.sh \| bash`, `/geo quick`, `/geo audit` | README documents GEO technical/citability/crawler/brand analysis, 0–100 vendor score and OS-specific installation scripts (Python 3.10+). Remote script execution requires version/code review; readme citations and a score do not prove actual AI-answer inclusion. | **Already covered** by GEO-031/032/033/047/052/053, AGENT-023–048 and prior [risk classification](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md). **Not** installed; no new checklist ID or mandatory `llms.txt`/passage length. |
| **3. [Schema](https://github.com/coreyhaines31/marketingskills/blob/main/skills/schema/SKILL.md)** from Marketing Skills; `npx skills add ... --skill schema` | Current skill instructs validation of JSON-LD matching visible content and current Google feature eligibility; distinguishes Schema.org markup from Google rich results. Its feature notes state **FAQ rich results ceased May 7, 2026**; verified against [official Google Search changelog](https://developers.google.com/search/updates), which also says docs removed in June. Google also retired HowTo rich results and its sitelinks search box. | Existing **SEO-018/040** cover valid, accurate schema. **Revised SEO-046** for explicit **currently supported** search-appearance checks, retirement cases and actual Search Console diagnostics. Existing `schema` tool link retained, with clarified purpose; no extra skill/check. |
| **4. [Programmatic SEO](https://github.com/coreyhaines31/marketingskills/blob/main/skills/programmatic-seo/SKILL.md)** from Marketing Skills; `npx skills add ... --skill programmatic-seo` | Skill discusses templates populated by a lawful, useful dataset; unique content for every page, correct URL/indexation controls, missing/outdated data, and quality-vs-volume. Its output examples are advice rather than Google approval or proof that 100s of pages should be indexed. | Existing SEO-002/003/028/033/034/035/**084**, plus navigation/metadata checks. **Strengthened SEO-084** to include rights/accuracy/freshness/completeness of source rows and representative duplicate/missing/stale variants; added `programmatic-seo` to the **optional review-aid list**. No new ID, page-count target or mass-publishing mandate. |
| **5. [Claude Blog](https://github.com/AgriciDaniel/claude-blog)** by AgriciDaniel; `/blog write`, `/blog analyze` | README documents **32 skills**, 5 agents, source research, fact-checking, scored internal review and five delivery gates; outputs may include Markdown/HTML/PDF/hero assets, optional translation/media. MIT licensed, requires Claude Code and Python 3.11+. Reviewer threshold and generated citation-readiness score are **internal**. Optional Gemini images/narration cost money, Openverse fallback sends a title/tags, and author warns the `v2.2.0` installer/uninstaller can delete user files; use pinned/reviewed safe version `v2.3.0+` or full commit SHA. | Existing **SEO-004/028/084**, source rights, AGENT-035/041/043 and release gates already mandate independently verified content, rights, approvals and safe publishing. **New optional editorial-aid reference** in `lists/frontend/13_SEO.md`, plus informational installer/score caution in risk catalog. No need for a new `BLOG-...` or SEO ID. |

**Installation-command caveat:** The source mixes `/plugin` instructions meant for **interactive Claude Code** with `curl`, `npx`, Git/shell commands meant for a **terminal**. Marketing Skills explicitly notes that installs initiated by an agent can put skills in the universal `.agents/skills` folder rather than `.claude/skills`; specifying `-a claude-code` avoids this ambiguity. Tool installation, configuration, file changes, credentials, outputs and release gates were **not** tested here. The five skill labels correspond to **four** MIT-licensed upstream repositories, not five independently maintained source repositories. MIT licensing does not cover Claude subscriptions or paid optional APIs.

**Primary search guidance:** [Google Search Central structured-data feature list](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) and [updates](https://developers.google.com/search/updates) verify the supported-appearance distinction and 2026 FAQ retirement; [Google's generative AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) requires manual fact-checking of AI-produced pages and metadata and warns against scaled low-value output; [general structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) state that valid structured data does not guarantee rich results. **No source demonstrates guaranteed Google indexing, rankings, AI citations or audit revenue.**

### Other summaries and retry requests since commit `b8a705d`

- [Alex Chen — 20-step SEO](https://www.instagram.com/reels/DfonmYuOGZj/) and [Lawrence Hitches — seven free tools](https://www.instagram.com/reels/De3lwqQzv29/) were **repeated summary requests**, not new evidence. All 20 and seven items remain covered by previous complete source audits and their respective revisions **SEO-031** and others; no duplicate checks.
- [Four Claude SEO plugins](https://www.instagram.com/reels/DfDdLPMDQFa/), [Suket SEO PDF](https://www.instagram.com/reels/DfhVC3Gg5PU/) and [Tim/Keytomic](https://www.instagram.com/reels/DfikXW5BcXQ/) were included in the subsequent failed-extractor retry batch but their available linked guides, screenshots or public vendor documentation had previously been analyzed. The extractor's empty response is **not new source content**.
- [DfnE3jHjPvy](https://www.instagram.com/reels/DfnE3jHjPvy/), [Dey_dvNIBD6](https://www.instagram.com/reels/Dey_dvNIBD6/) and newly added [Dd30vAhivDq](https://www.instagram.com/reels/Dd30vAhivDq/) remain **unreviewable**: the Instagram extractor returned empty media responses and searches did not locate trustworthy text for their claims. No content-based requirements can legitimately be imported. Caption, transcript or user-provided screenshot required.
- The extractor also returned empty media responses for **two previously accessible control reels** ([Dd6qP9CRxax](https://www.instagram.com/reels/Dd6qP9CRxax/), [DfmnzMlAhqh](https://www.instagram.com/reels/DfmnzMlAhqh/)), supporting a general Instagram access/authentication limitation rather than nine separate missing SEO findings. The submitted nine-image carousel was already audited from the supplied images and was not fetched anew.

**Final disposition:** **Revised SEO-046 and SEO-084**, added **one existing Marketing Skills subskill link** and **one conditional Claude Blog reference**, plus two informational risks. **No new IDs, no release-gate/checkbox changes; 91 populated scope files and 4,186 unique checks remain unchanged**.

## Supplemental review (2026-11-14): Five distinct SEO/GEO/marketing repositories from six submitted URLs

**Intake and provenance:** User supplied six GitHub URLs on 2026-11-14. Five distinct repositories were independently opened: the two spellings `AgriciDaniel/claude-seo` and `AgricIDaniel/claude-seo` both resolve to the same GitHub repository owned by **AgriciDaniel**. The other four are maintained by **iamjeeth**, **Albert-Weasker**, **every-app**, and **msitarzewski**. Original publication dates were not established; the date here is the review date, not an invented release date. Reviewed upstream READMEs, `launch-seo/SKILL.md`, Agency Agents marketing division and relevant documented tool/skill paths. This is source/feature and checklist-coverage review, **not** an installation, security audit, API-authenticated test or measured SEO/GEO outcome.

| Upstream source and independently reviewed capability | Existing check IDs and disposition |
| --- | --- |
| **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)** (also submitted with `AgricIDaniel` spelling). Claude Code SEO plugin documents technical, content, schema, local and GEO auditing via 26 subskills/19 agents, with browser and optional data-provider integrations. | Already covered by **SEO-004/013/018/022/029/031/084**, **GEO-031–033/052/053**, and AI agent/tool safeguards. Existing [risk analysis](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md) remains authoritative for unverified scores, installer/browser access, data recipients and unreviewed publishing. Added only a visibly **non-endorsed optional reference** to `lists/frontend/13_SEO.md`; no duplicate check, no unattended site changes. |
| **[iamjeeth/launch-seo-skill](https://github.com/iamjeeth/launch-seo-skill)** by Jeet Bhanushali. [SKILL.md](https://github.com/iamjeeth/launch-seo-skill/blob/main/SKILL.md) enumerates ten initial setup checks and ten week-one checks: Search Console/Bing, robots/noindex, sitemaps, host, metadata, rendering, schema, 404s, forms, analytics and distribution. Upstream discloses **scorebadge.com** as the author's optional product. | Already covered by **SEO-009/012/013/014/018/029/031**, **LAUNCH-117/127/130/131**, accessibility and analytics/consent controls. Added a conditional launch-skill note to `lists/frontend/20_Release_and_LaunchReadiness.md`; no new numbered checks. Product Hunt, G2/Capterra, Clarity/GA4 and an outbound badge are **not universal mandates**. Check first-party property/index data, privacy consent, owner approval of badges and authorized end-to-end form tests; do not present fixed title limits, redirect-hop prescriptions or arbitrary bot permissions as Google policy. |
| **[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**. NiubiGEO documents self-hosted multi-model answer/competitor comparisons, raw answer/source inspection, export, repeatable snapshots and v0.3.x keyword monitoring (including beta features). | **GEO-031–033/052/053** already require baseline prompts, dated answer/citation samples and separate metric classes. Added it as an optional evidence research platform in `lists/frontend/14_GEO_and_AEO.md`, without elevating its measurements to an SEO/GEO standard or adding IDs. External model APIs still process submitted prompts; costs, data retention and credentials require review. |
| **[every-app/open-seo](https://github.com/every-app/open-seo)**. OpenSEO provides self-hosted/hosted SEO research, MCP/agent integration and [plugin skill definitions](https://github.com/every-app/open-seo/tree/main/plugins/openseo/skills), including AI visibility and SEO auditing. | **Already listed** with paid DataForSEO/API-cost and first-admin security warnings in `lists/frontend/13_SEO.md` and the risk catalog; **SEO-029/031** and **GEO-031–033/052/053** cover safe research interpretation. Added a context-specific cross-reference for its AI visibility workflows in `lists/frontend/14_GEO_and_AEO.md`, **not** a duplicate standalone SEO entry. Secure initial admin before public exposure, inspect tokens/permissions and validate evidence. |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/tree/main/marketing)**, marketing division. Verified the [SEO Specialist](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-seo-specialist.md), [AI Citation Strategist](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-ai-citation-strategist.md), [AEO Foundations Architect](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-aeo-foundations.md) and [Agentic Search Optimizer](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-agentic-search-optimizer.md). These are agent-role prompts/workflows, not installed verification test suites. | Mapped to **SEO-002/018/029/031/082**, **GEO-031–033/047/052/053/079**, and relevant **AGENT-023–048**. Added the SEO role as a caveated reference in `lists/frontend/13_SEO.md`, and three GEO/agent roles in `lists/frontend/14_GEO_and_AEO.md`. Excluded compulsory `llms.txt`, token budgets, fabricated citation scores, automatically added FAQ rich-result markup, or WebMCP agent actions as universal checkboxes. Human-reviewed content, authenticated actions and experimental browser compatibility must be verified. |

**Primary-policy reconciliation:** [Google's current generative-AI Search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) says `llms.txt` and special AI-only files are **not needed or used** by Google Search, with no mandatory content chunk size. [Google's SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [crawling/index FAQ](https://developers.google.com/search/help/crawling-index-faq) do not guarantee indexing or rankings from checklist compliance or sitemap submission. [Chrome's WebMCP Imperative API](https://developer.chrome.com/docs/ai/webmcp/imperative-api) and [Declarative API](https://developer.chrome.com/docs/ai/webmcp/declarative-api) documentation describe experimental/origin-trial interfaces rather than a universally deployed browser standard. These third-party repositories are **leads and optional aids**, not independent evidence of search rankings, AI citations, or production-safe behavior.

**Outcome:** Five distinct sources reviewed; three primary frontend appendices and the informational SEO/GEO risk catalog updated, with this provenance record and `AGENTS.md` log kept in sync. **No new or revised numbered checklist IDs**; 91 numbered scope files and **4,186 globally unique unchecked checklist items** remain, with the unchanged breakdown of 682 shared / 681 frontend / 1,116 backend / 1,707 AI. Skill/tool installation, running scans, attaching accounts, verifying all source-code security properties, and reproducing vendor metrics were **not performed**.

## Supplemental audit (2026-11-14): Six pasted SEO prompt and "tricks" posts (69 backlink steps included)

**Provenance:** All six items arrived as user-pasted text on **2026-11-14**. Original links, verified authors, publication dates, private dashboards and the advertised 150+ "SEO Wins" database were not provided. A public third-party social-post index contains similar "BACKLINKS MAXXING" wording attributed to `@borjafat`, but does not independently corroborate the claimed 133k AI mentions for `distribb.io`, the tier ranking, or any causal link to those outcomes. These claims are treated as leads, not verified results.

### Post 1 — Vibe-coded site "full SEO checklist"

| Pasted steps / grouped assertion | Relevant IDs and verified disposition |
| --- | --- |
| Switch to SSR | **Revised SEO-013**, **SEO-036/061**, backend **SEO-050**. Check initial/rendered HTML and use SSR/SSG when needed; no universal SSR requirement. |
| XML sitemap, submit via Search Console | **SEO-009/029**, backend **SEO-054**. Validate actual sitemap and indexing diagnostics; submission isn't a ranking/indexing guarantee. |
| Allow Googlebot; remove every noindex | **Revised SEO-007**, **SEO-006/064**, backend **SEO-008**. Correct accidental blocks on intended public pages; retain intentionally excluded pages and secure private assets with authentication. |
| Collapse redirects, fix links, canonicals | **SEO-010/011/012/016/048**, backend **SEO-038/057**. Confirm real HTTP states and equivalent redirect destinations. |
| Unique titles/descriptions, one H1, breadcrumb navigation, orphan links | **SEO-005/011/014/015/063/067**. Clear accessible headings and navigation; no fixed one-H1 Google ranking rule. |
| FAQ/Article schema | **SEO-018/040/046/066**. Only applicable truthful markup; Google FAQ rich results retired **2026-05-07**. |
| Alt on every image, WebP all images, CLS below 0.1, complete load under 2s | **SEO-017/022/023/043/044/069/070**. Useful alt for informative images, decorative empty alt where suitable, appropriate formats, measured CWV. Good CLS is below 0.1; Google's good LCP threshold is **2.5s**, not mandatory whole-page loading in 2s. |
| Replace AI slop, genuine author, trust-based links | **SEO-004/027/028/082**. Fact-check public copy, use real author information where relevant, seek voluntary editorial links. |
| "Page one by Monday", "full" checklist, no mistakes | **Rejected** as unsupported universal ranking/time guarantees and non-exhaustive SEO advice. Independent quality checks and review remain essential. |

### Post 2 — "69 backlink tactics" (all numbered steps grouped)

| Source steps | Coverage, exclusions and acceptance boundary |
| --- | --- |
| **1–5** Editorial exchanges, networks, topical fit, reader purpose, published-link log | **SEO-082 revised.** Contextual editorial references may help users; **excessive reciprocal exchanges** are link spam under Google's [policy](https://developers.google.com/search/docs/essentials/spam-policies). No forced swaps or tier guarantee. |
| **6–12** Buyer lists/competitor roundups, identify missing needs, send truthful additions, keep entries fresh | **SEO-002/003/028/082**: independent editorial choice, original accurate product facts and maintenance. |
| **13–19** Original research/statistics, sampling and methods, useful quotable findings, persistent research URLs | **SEO-003/004/028/082**, **GEO-038/043**: source methodology, limitations, stable verifiable evidence. |
| **20–27** Journalist requests (e.g., Qwoted), qualified profile, relevant deadlines, direct quotes and research links, pitch log | **SEO-027/028/082**: truthful qualifications, first-hand data, respectful outreach. Qwoted isn't mandatory. |
| **28–32** Competitor-linked pages, surrounding context, fill evidence gaps, targeted pitches | **SEO-002/028/082**: lawful competitor research and new independent value; no copying or fabricated findings. |
| **33–37** Unlinked mentions, missing chart credits, own old URL restoration/equivalent redirects | **SEO-032/048/082**: verify existing mention/rights, preserve reader-accessible relevant destinations, no blanket redirect. |
| **38–43** Useful calculators, AI-assisted builds, ordinary/edge test inputs, permanent URLs, guide outreach | **SEO-003/028/082** + testing controls: verify actual utility, correctness, accessibility and publisher interest. |
| **44–49** Dead/outdated resources, archived context, accurate replacements, editor notification | **SEO-003/011/012/028/082**: do not appropriate copyrighted archived text; offer independent accurate alternatives. |
| **50–55** Consented illustrations, author-vetted facts, source-credit embedding | **SEO-017/028/082** and rights/accessibility checks; avoid misleading graphics. |
| **56–60** Author-approved video explainers, original recordings, credit | **SEO-028/082** plus media accessibility/copyright; publishing is the author's choice. |
| **61–64** Vendor case study from tools actually used | **SEO-027/028/082**: true permissioned first-party experience and relevant attribution. |
| **65–69** Supplier/government directories and accurate allowed URLs | **SEO-076/083/028/082**: eligible factual listings only, not mass link submissions. |

**No S/A/B/C/D ranks or claimed 133k AI mentions independently verified.** Separate live backlinks/referrals (**SEO-031/082**) from actual model-answer citations (**GEO-033/052/053**). Broadened SEO-082; no redundant backlink IDs.

### Post 3 — Publisher Center, Preferred Sources and news traffic

1. **Publisher Center "become a publisher":** **Outdated.** [Google ended new Google News publication setup in Publisher Center in 2024](https://support.google.com/news/publisher-center/answer/14859160), and eligibility is determined algorithmically.
2. **Preferred Sources button or deeplink:** **New conditional SEO-085.** [Google's current publisher guidance](https://developers.google.com/search/docs/appearance/preferred-sources) confirms an official JS button and `https://www.google.com/preferences/source?q=example.com` fallback if the domain/subdomain appears in its source selector. Users opt in; presence of a button alone is not a requirement or appearance guarantee.
3. **Place button several times / collect 10,000+ users:** Multiple placements and any numeric threshold are *not* mandatory. No fixed traffic or feed-placement guarantee.
4. **"SEO Wins" 150+ hacks:** Gated resource absent; no claims or steps imported.

### Post 4 — Eight-word GSC query sample

Regex `^(?:\S+\s+){7,}\S+$` matches eight-plus whitespace-delimited tokens in Search Console's **RE2** custom query filter, not necessarily eight semantic words, all questions or AI prompts. With actual property access, identify true page-to-query relevance and high-impression/low-click opportunities, update a helpful answer, compare dates/CTR, and recognize missing anonymized/truncated rows. **SEO-031 revised**, existing **SEO-002/028/033**; optional appendix includes expression.

### Post 5 — Competitor robots.txt, sitemap, subdomain and headlines

| User assertion | Coverage / outcome |
| --- | --- |
| `robots.txt` disallow reveals private ad pages | **Misleading:** robots rules publicly describe crawling, **not confidentiality** or guaranteed URL suppression. **SEO-007 revised**, **LAUNCH-130** access-control considerations. |
| `/sitemap.xml` reveals every page with future target launch dates | **Unsupported:** XML sitemaps are discretionary and may not list all URLs; `lastmod` is intended for meaningful factual modifications. **SEO-009/035**; treat public observations as incomplete signals. |
| Search `site:` and marketing vendor subdomains to reveal all gated offers | **Not exhaustive**; public results do not authorize bypassing restricted/gated content. Respect site rules; no claims about protected offers. |
| Three repeated headlines prove winning ads or future campaign | **No supporting experiment/conversion evidence:** repetition is not a controlled comparison. **SEO-002/003/028/084** favor original research over copied or speculative `vs` content. |

### Post 6 — English question-opening GSC query sample

Regex `^(who|what|when|where|why|how|which|can|does|is|should)\s` is a valid anchored case-insensitive-by-default **RE2** sample for certain English question starts, not all user questions. Add relevant factual answers to already suitable pages based on actual intent, not automatic FAQ/schema/page inflation. **SEO-031 revised** with **SEO-002/003/014/028/046**. No automatic AI citation assumption.

**Independent verification (2026-11-14):** [Google technical eligibility](https://developers.google.com/search/docs/essentials/technical), [JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Robots](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [Publisher Center](https://support.google.com/news/publisher-center/answer/14859160), [Preferred Sources](https://developers.google.com/search/docs/appearance/preferred-sources), [Search Console RE2](https://support.google.com/webmasters/answer/17011165), [query omissions](https://support.google.com/webmasters/answer/17011259), [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals), [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies), [FAQ feature changes](https://developers.google.com/search/updates).

**Outcome:** **One new SEO-085**, **revised SEO-007/013/031/082**, expanded optional safe research methods and non-recommended shortcut warnings. No claims of live project testing, source-post authentication, external backlinks, Google or AI performance. **91 scope files / 4,187 unique checks** (682 root, 682 frontend, 1,116 backend, 1,707 AI).

## Supplemental intake (2026-11-14): AI bot-log method, Reddit SEO, hosted-content SEO, cited-source outreach, and Okara GEO poster

**Provenance:** The user pasted **four full social-post texts** (crawler-log filter; Reddit participation; hosted-platform “parasite SEO”; AI answer-source outreach) and a **fifth caption with an uploaded Okara PNG** (1304×2048), reviewed directly from the supplied image on 2026-11-14. No original post URLs, publication dates, validated author identities, website access logs, AI answer screenshots or performance datasets were supplied. The image contains **six sections and 36 individual suggestions**; its headline, “The only GEO checklist you'll need,” is a promotional claim, not a standard. The 36 suggestions are mapped verbatim by short label below, without importing them as 36 redundant checks.

### 1. AI-search/User-Agent server-log filter

**Submitted regex:** `OAI-SearchBot|ChatGPT-User|Claude-SearchBot|Claude-User|PerplexityBot|Perplexity-User`. Each string has an independently documented provider role: [OpenAI search/user fetchers](https://developers.openai.com/api/docs/bots), [Anthropic search/user bots](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), [Perplexity search/user fetchers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers). The expression is a **candidate User-Agent substring filter**, not an authenticated crawler detector or a single “AI search” category. Some providers publish IP ranges while Anthropic does not currently publish a reliable independent range; IP verification must be conditional.

- **New verified coverage:** **GEO-081** in `lists/backend/29_GEO_and_AEO.md` for privacy-safe, authorized server/CDN bot-request analysis (time, canonical route, status, WAF/robots/auth blocks, provenance and missing log sources). Separate automatic search crawling from user-triggered fetches, and provider training bots if analyzed. This is distinct from existing **GEO-079** (live crawler access tests), **GEO-033** (AI citation/referral distinctions), **OBS-018/019** (telemetry privacy), and **GEO-023** (server bot rules).
- **Excluded inferences:** A 0-log row cannot prove a page was never crawled (CDN may intercept, logs may sample/drop); User-Agent can be spoofed; 200 response alone is not proof the intended text was served; page request counts do **not** prove AI indexing, citation, demand or rank. A failed important URL is a reason to examine actual robots, link graph, accessible HTML and WAF first rather than publish arbitrary articles.
- **Optional operational example:** Start with the user-supplied regex; verify supported bot identities, aggregate by canonical path/time/status, review redirects, 403, 429 and 5xx, evaluate excluded/unknown traffic and protect sensitive request URLs. No tool runs or logs inspected in this audit.

### 2. Reddit SEO/community participation post

The claimed **“2,100%+ visibility growth,” “15% of Google AI Search,” and “$60M partnership”** are source marketing assertions, **not** verified site-specific forecasts or rankings; no verifiable source/date/methodology accompanied them. [Reddit's spam rules](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam) prohibit mass repetitive promotion and automated spam. [Reddit moderation guidance](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community) says **some** communities use a 90/10 promotion guideline, while others prohibit self-promotion entirely; 15 minutes/day, karma accumulation and avoiding every CTA are **not universal conditions**.

| Posted method | Outcome / checklist evidence |
| --- | --- |
| Find relevant active subreddits through legitimate public search and genuine questions | **SEO-002/031**, **GEO-001**: user-intent research; don't collect private threads or scrape prohibited data |
| Contribute useful first-hand answers, maintain accurate affiliation/profile | **Revised SEO-082**, **SEO-027/028**: authentic participation, sub rules and disclosure rather than gaming karma |
| Turn repeated pain points into original articles or videos | **SEO-003/004**, **GEO-013**: source rights, original facts and reader value |
| Interpret Reddit links, including alleged dofollow sidebar exceptions | **SEO-077/082**, [Google outbound link guidance](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links): attributes vary; neither UGC/nofollow nor rare followed links prove any direct ranking or citation boost |
| Advertised “SEO Wins” 150+ tactics library | **Not reviewed**: no accessible database or exact source content was supplied |

### 3. Hosted-platform / “parasite SEO” post

| Source steps | Source-derived point, verified treatment and existing ID |
| --- | --- |
| 1–2 | Select relevant intent and host from public SERPs; **SEO-002/028/082**. Do not choose a host *mainly* to exploit its unrelated existing reputation. |
| 3–4.8 | Standalone helpful answer; clear question title, direct introduction, audience, practical comparison, original evidence, natural mention, relevant link and optional CTA; **GEO-006/007/009/042**, **SEO-003/028/082**. A rigid template, verbatim keyword title or compulsory CTA is not a ranking requirement. |
| 5–5.3 | Match Reddit, LinkedIn or YouTube formats and avoid mass copying; **SEO-003/004/082**, **GEO-041**. Honor platform policies and rights, plus transcripts for accessibility where useful. |
| 6–6.7 | First-hand testing, screenshots, methods, real results, original images and explicitly labeled perspective; **SEO-004/028**, **GEO-009/012/013**. Do not fabricate proof. |
| 7 | One appropriate contextual link vs promotional link farm; **SEO-077/082**, but even a single link can violate host policies or become undisclosed promotion. |
| 8 | Monitor indexed/public material and actual value; **SEO-029/031**, no guaranteed search appearance. |
| 9–9.5 | Update facts, internal links, evidence, legitimate comments and truly useful supplementary pages; **SEO-011/028/082**, **GEO-015/036**. Avoid coordinated host-site posting to manipulate rankings. |

[Google's 2026 site reputation abuse policy](https://developers.google.com/search/docs/essentials/spam-policies) targets third-party pages published chiefly to borrow a host's ranking signals; legitimate editorial work and ordinary forum contributions are not inherently prohibited. No distinct new numbered “parasite SEO” action is recommended. The informational risk document gains a clearer boundary.

### 4. AI-cited source outreach / “ChatGPT backlink” process

| Source stage | Existing coverage and verified limitations |
| --- | --- |
| 1. Select 20–50 buyer prompts from actual sales questions | **GEO-001/031/052**; credible audience samples and bounded comparisons; 20–50 is an example, not a required quota |
| 2. Observe ChatGPT, Google AI answers and Perplexity, repeat for volatility | **Revised GEO-032/052**; log answer text, direct cited URLs, platform, date, locale and settings. Two runs are not a statistical guarantee |
| 3. Classify URLs as editorial list, directory, review, forum or video | **GEO-032/033/052**; categorization can prioritize research but is neither a proof of trust nor a guaranteed source-to-answer transfer |
| 4. Offer original factual updates/case studies to list editors | **SEO-028/082**; voluntary editorial decisions, independent review, rights and proper link disclosure |
| 5. Claim only eligible G2/Clutch/review profiles and invite genuine reviews | **SEO-083/028/082**; reject fabricated, paid undisclosed or coerced reviews |
| 6. Contribute genuinely useful forum answers with affiliation disclosed | **Revised SEO-082**, **GEO-026**; follow local rules and no mass promotional posting |
| Re-run weekly, assume most citations are from third parties and "get on that page = get cited" | **Revised GEO-033/052**; a week is only a possible review cadence, source distribution varies by query/provider, and neither publisher inclusion nor mentions imply future AI citations. Track observed links separately from impressions, crawl logs and referrals |

### 5. Okara image: “The only GEO checklist you'll need” — all 36 image points

The image's wording is the **user-supplied visual**, not proof that Okara's claims are an exhaustive or vendor-independent standard. Each of the six groups below has its six visible checkboxes mapped to *one or more existing check IDs* (or the new **GEO-081** for underlying server-log evidence). All shared templates remain unchecked.

| Image checkbox (group and order) | Existing or new coverage and necessary qualification | Decision |
| --- | --- | --- |
| Access 1 — Allow AI search bots in robots.txt | GEO-047/079, AI GEO-024; search versus user/training control, conditional | Covered |
| Access 2 — Check your CDN isn't blocking them | GEO-079, backend GEO-023 and new GEO-081; verified requests / statuses | Covered + new diagnostic |
| Access 3 — Submit your sitemap and use IndexNow | SEO-009/029, backend SEO-054; IndexNow optional for participating engines, not Google | Covered / qualified |
| Access 4 — Fix noindex and canonical issues | SEO-010/064, GEO-020; fix unintended issues only | Covered |
| Access 5 — Key text in HTML, not JS or images | GEO-019/070, SEO-013; test initial/rendered accessible output | Covered |
| Access 6 — No login walls on key pages | GEO-079, backend GEO-065; only intended public pages | Covered / conditional |
| Content 1 — Original research and data | GEO-009/013/043; sample/provenance/methodological accuracy | Covered |
| Content 2 — First-hand experience and opinions | GEO-013/014, SEO-004; authentic expertise, not invented persona | Covered |
| Content 3 — How-to, best-of and comparison pages | GEO-003/037, SEO-003; only distinct helpful intent | Covered |
| Content 4 — A page for every use case | GEO-002/037, SEO-084; reject thin/duplicated variants and mandatory page quota | Covered / qualified |
| Content 5 — Update outdated stats and examples | GEO-015/044, SEO-034; source dates/owners | Covered |
| Content 6 — Add what cited pages are missing | GEO-032/036, SEO-002/028; genuine independently verified value, not copying | Covered / qualified |
| Structure 1 — Question H2s, answer right below | GEO-006/007/066; helpful semantic headings, not universal H2 requirement | Covered |
| Structure 2 — Answer the follow-up questions | GEO-001/037; pertinent follow-ups only | Covered |
| Structure 3 — Each section makes sense on its own | GEO-040/042; retain necessary caveats and context | Covered |
| Structure 4 — Tables for comparisons | GEO-007/011/067; only when readable and useful | Covered |
| Structure 5 — Internal links to key pages | GEO-020, SEO-011; descriptive relevant links | Covered |
| Structure 6 — Schema markup where it fits | GEO-021/071, SEO-018/046; currently supported factual features | Covered |
| Mentions 1 — Show up in Reddit threads | SEO-082 revised, GEO-026, SEO-028; disclose, respect moderators and no spam | Revised |
| Mentions 2 — Get into listicles that rank | SEO-082/028; independent editorial assessment, no guaranteed placement | Covered |
| Mentions 3 — Get mentioned on pages AI already cites | GEO-032/033, SEO-082; observed URLs are only outreach leads | Revised / qualified |
| Mentions 4 — Reviews on G2 and Capterra | SEO-083/028; eligible products, authentic consented reviews | Covered / conditional |
| Mentions 5 — YouTube videos about you | GEO-041/068, SEO-028; only useful original videos | Covered / conditional |
| Mentions 6 — Coverage on trusted news sites | SEO-082/028; authentic journalist value, no payment-for-ranking scheme | Covered |
| Trust 1 — Author name and bio on posts | GEO-014, SEO-027; truthful where appropriate | Covered |
| Trust 2 — Visible last-updated date | GEO-015/044; accurate substantive update dates | Covered |
| Trust 3 — Link to reputable sources | GEO-012/016; original verifiable claims | Covered |
| Trust 4 — Screenshots, demos, customer quotes | GEO-013/041, SEO-028; permissions and truthful evidence | Covered |
| Trust 5 — Current pricing on a public page | GEO-027/043; only when business model/disclosure permits | Covered / conditional |
| Trust 6 — Same brand and founder info everywhere | GEO-017/080; consistently verified real identity, founder detail not always required | Covered / qualified |
| Tracking 1 — List 20 prompts your buyers ask | GEO-031/052; authentic questions and representative sampling, no mandatory 20 | Revised / qualified |
| Tracking 2 — Re-run them in ChatGPT, Claude, Gemini | GEO-032/052; provider availability, repeat variation, no mandated schedule | Revised |
| Tracking 3 — Study the section that got cited | GEO-033/042/052; distinguish actual evidence from aggregate stats | Revised |
| Tracking 4 — Track citation share vs competitors | GEO-033/053; denominator/provider scoped; Bing preview where available | Revised / qualified |
| Tracking 5 — Track AI referrals and signups | GEO-033/053, SEO-030; referrals are not citations | Revised |
| Tracking 6 — Check GSC and Bing AI reports monthly | GEO-033/053; GSC Web aggregate, Bing AI Performance sampled citation data, cadence justified | Revised / qualified |

**Important image-specific corrections:** “Allow AI search bots” depends on content owner's search/training choices; a successful crawl cannot guarantee citation. [IndexNow](https://www.indexnow.org/faq) is optional and applies to **participating** engines, not as a Google Indexing API for all URLs. A public site need not have a distinct page for every use case, list a founder, publish pricing irrespective of business model, register on G2/Capterra, publish YouTube media or run exactly 20 prompts. There is no universal 30-day Google Search Console AI citation report; Google aggregates AI Search feature clicks within Web search, whereas [Bing Webmaster AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) reports sampled citation/grounding activity across its defined Microsoft and partner experiences, with citation share preview available. Avoid misreading its outputs as all AI systems' ranking, user clicks or causal attribution. [Google's official AI guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) rejects special mandatory GEO formats and inauthentic mentions.

**Overall disposition (2026-11-14):** **New GEO-081** in backend, **revised GEO-032/033/052** in frontend, **revised SEO-082** for safe Reddit/forum participation, added optional tool/context references and prevention notes. All other image and post concepts were already covered by identified SEO/GEO/OBS controls or conditionally applicable. Five submitted items reviewed (four pasted texts and one 36-point image), with no original source permalinks or verified outcome datasets. **91 populated files, 4,188 globally unique unchecked checklist IDs** (682 shared, 682 frontend, 1,117 backend, 1,707 AI); domain **GEO** total now **81**. No installed tooling, live-site audits or actual AI answer experiments were run.

## Supplemental review (2026-11-14): Three pasted SEO posts — commercial-intent GSC regex, on-page tools and low-KD content iteration

**Provenance:** All three posts arrived as user-pasted text in this conversation on 2026-11-14. No original post URLs, verified author names, publication timestamps, campaign dashboards or live Search Console exports were supplied. Source instructions are discovery leads, not Google requirements; tool descriptions below were checked against linked provider documentation. The advertised 150+ SEO Wins tactics were neither provided nor verified.

### Post 1 — Commercial/comparison query research in owned Search Console

**Exact user expression:** `\b(best|vs|versus|alternatives?|pricing|cost|reviews?)\b`.

| Pasted action | Verification and mapping | Decision |
| --- | --- | --- |
| Search Console Performance → Search results → Query → Custom (regex) | Official [GSC advanced filtering](https://support.google.com/webmasters/answer/17011165) uses RE2, whose [word-boundary definition](https://github.com/google/re2/wiki/Syntax) includes ASCII `\b`. | Covered by SEO-031; added this exact optional regex to frontend tools |
| best / vs / versus / alternative(s) / pricing / cost / review(s) | This is a subset of English potential commercial/comparison queries, not all commercial intents or actual customers. Query-only filtering can omit anonymized and truncated data. | Revised SEO-031 for real page-query context, position/device/date/sample-size and conversion interpretation |
| High impressions and low clicks → rewrite every title | First inspect the **Pages** tab, actual relevant URL, intent, result title, search appearance and dated CTR. [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link) says search title links may be generated from multiple sources. | Revised SEO-014 for evidence-backed, honest title changes and measurement; no guaranteed clicks or sales |

### Post 2 — Ten named on-page SEO tools, each assessed

| Number / tool | Publisher-documented capability | Disposition |
| --- | --- | --- |
| 1. [Google Search Console](https://search.google.com/search-console/about) | Owner-authorized Google Search query/click/CTR, indexing and sitemap diagnostics | SEO-029/031; already linked in frontend tools |
| 2. [Ahrefs](https://help.ahrefs.com/en/articles/9025740-how-to-use-content-gap-to-find-keyword-ideas-from-competitor-websites) | Keyword ideas, estimated difficulty/volume and competitor content gaps | Optional content and market research; not Google metrics |
| 3. [Semrush](https://www.semrush.com/kb/292-on-page-seo-checker) | On Page SEO Checker with page-level ideas and competitive comparison | Optional optimization aid; suggestions and traffic forecasts require validation |
| 4. [Yoast SEO](https://yoast.com/features/seo-analysis/) | CMS content/readability and title/meta analysis, notably WordPress and other supported integrations | Optional when supported by the stack; scores are vendor-defined |
| 5. [Surfer SEO](https://docs.surferseo.com/en/articles/5700347-content-editor-overview) | Content Editor comparing search results and offering proprietary content scores | Optional writing research; not a Google word-count standard |
| 6. [MarketMuse](https://docs.marketmuse.com/workflows/optimize/) | Optimize and topical-coverage/competing content analysis | Optional research with accountable human fact-checking |
| 7. [Rank Math](https://rankmath.com/kb/seo-analysis/) | WordPress SEO Analyzer and content/metadata review, with optional AI services | Optional WordPress tool; review tier, automated changes and permissions |
| 8. [SE Ranking](https://help.seranking.com/hc/en-us/articles/16333726680988-On-Page-SEO-Checker-Overview) | On-Page SEO Checker, keyword and competitor comparison reports | Optional on relevant paid plans; no objective ranking grade |
| 9. [Bing Webmaster Tools](https://www.bing.com/webmasters/about) | Verified Bing search performance, crawl/index information | SEO-029/031; already covered and listed |
| 10. SEO Wins | Advertised 150+ SEO / AI SEO tactics; only a marketing name in the user text | Not independently accessible: no complete library link or content supplied |

**Coverage decision:** Google Search Console and Bing Webmaster Tools were already present in `lists/frontend/13_SEO.md`. Seven additional commercial/CMS products are recorded only as optional on-page research and editing diagnostics; the tenth, SEO Wins, remains **unverified**. No product is endorsed as a mandatory tool, no private account or paid provider was connected, and vendor traffic, KD, word-count or content scores were not independently benchmarked.

### Post 3 — Fifteen numbered SEO steps and AI-assisted prompts

| Post step / topic | Existing or revised checklist IDs | Verified disposition |
| --- | --- | --- |
| **1. SEO without backlinks, AI prompt assistance** | SEO-004/028 | AI is conditional research/drafting support, not a complete automated replacement or guaranteed ranking process. |
| **2. Prioritize 0 KD / 0–10 estimated monthly searches** | SEO-001/002/031 | Underserved real user questions are useful; third-party KD/search-volume predictions are not proof no one competes, nor mandatory thresholds. |
| **3. Keyword tool or MCP prompt: seeds, KD filters, group search intent, select 15** | SEO-002/029/031; agent tool permissions | Use authorized read-only data and group queries sharing intent; table fields are optional and 15 groups is an example, not a requirement. |
| **4. Inspect current SERP to select landing/listicle/guide type** | SEO-002/003/028 | SERP and user intent are diagnostic context, not proof that copying competitor formatting is optimal. |
| **5. AI top-10 SERP audit, five-page word count, headings, missing information** | SEO-002/003/004/084 | Validate real sources and permissions, avoid unauthorized search scraping or reproducing top-page headings/word counts as fixed goals. |
| **6. Publish 10–15 articles and add useful internal links** | SEO-002/005/011/084 | Ship only genuinely distinct, owned, accurate pages; do not create arbitrary page batches or keyword variations with no independent value. |
| **7. AI writing prompt: question first, keyword repetition, title under 60, meta under 155** | SEO-003/004/014/015/016/028 | Direct answers and readable accurate headings are good if useful; reject keyword stuffing, compulsory first-100-word formula and title/meta character limits. Google meta snippets have no fixed character cap. |
| **8. AI internal linking prompt with source/target/anchor, max 3–5 links** | SEO-005/011/062 | Relevant navigable source-to-target links and descriptive anchors matter; neither AI-generated sentences nor a fixed 3–5 link budget is required. |
| **9. Wait exactly seven days and optionally build free backlinks** | SEO-029/031/082 | GSC volume and index delays vary; avoid fixed seven-day deadlines and manufactured free backlinks. |
| **10. Review per-page GSC queries, absent terms and average positions 10–30** | SEO-002/031/028 | Evaluate matching actual URL, meaningful query intent, real sample size and page need; 10–30 average position is not a guaranteed opportunity or a command to stuff keywords. |
| **11. GSC MCP/export prompt to rewrite targeted sections only** | SEO-004/029/031 | Verify account access and source data; editors approve fact-checked, rights-safe sections before production. Small edits are a useful workflow choice, not universal. |
| **12. GSC URL Inspection request-indexing every seven days** | SEO-029/031 | Optional for newly published or materially changed owned URLs; Google has quota limits and repeated unchanged requests cannot speed crawling or guarantee indexing. |
| **13. Build 2–5 backlinks each month; assess after three months** | SEO-031/082 | No required rate, no guaranteed ranking timeline; evaluate independently earned links and real referrals rather than volume targets. |
| **14. AI prompt for 10 competitor-gap/broken-link/directory/guest-post prospects** | SEO-028/082 | Prospect research, original resources and voluntary editor decisions are legitimate; no link purchases, paid pass-through rank credit or forced backlinks. |
| **15. Recap: low-KD, 10–15 pages, 7-day iteration, 2–5 links monthly, 3–12-month success** | SEO-002/004/011/029/031/082/084 | Retain intent, original helpful writing and measured review; reject exact output/volume/timing thresholds and promises of outcomes. |

**Main corrections:** Search Console report filters are not sales attribution; Google can replace page title links; Google documents **no fixed meta-description character cap** and **no minimum/maximum ranking word count**. Google [recrawl requests](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) have quotas and do not guarantee indexing or speed up by repeated unchanged submissions. Google [spam policy](https://developers.google.com/search/docs/essentials/spam-policies) rejects scaled low-value pages, keyword stuffing, automated unpermitted SERP queries and link schemes. Exact seven-day cycles, positions 10–30, 10–15 article releases, 2–5 links monthly, or 3–12-month success are *not* universal requirements.

**Primary verification checked 2026-11-14:** [GSC regex filtering](https://support.google.com/webmasters/answer/17011165), [RE2 syntax](https://github.com/google/re2/wiki/Syntax), [Search Console report definitions](https://support.google.com/webmasters/answer/7576553/performance-report-search), [Google result title links](https://developers.google.com/search/docs/appearance/title-link), [meta snippets](https://developers.google.com/search/docs/appearance/snippet), [recrawl guidance](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl), [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [helpful-content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), and [spam policies](https://developers.google.com/search/docs/essentials/spam-policies).

**Outcome:** Revised **SEO-014, SEO-029, SEO-031**; added optional tool references, exact search-query regex and non-prescriptive audience-intent-to-improvement process in `lists/frontend/13_SEO.md`. Added four marketing-risk entries separately. **No new checklist IDs, files, checked states or release gates**; repository inventory remains **91 scope files / 4,188 unique checks** (682 shared, 682 frontend, 1,117 backend, 1,707 AI). No original posts or gated SEO Wins database were authenticated, and no user site or search accounts were audited.

## Supplemental intake (2026-11-14): User-pasted “only SEO/GEO article” — section audit, linked repositories, skill paths and agent prompt

**Provenance:** The article was pasted in chat, not provided as a source URL. It claims to summarize 66 SEO/GEO articles, 48 skills and 13 other repos/14 ranked repos, with vendor information reportedly viewed on November 10, 2026; neither that corpus, the original publication, the claimed SpaceCut website audit, underlying citation studies nor account data were available to independently reproduce. **Only nine** distinct GitHub repositories were linked by the author, and all nine were resolvable. The **RomeoSEO main tree currently exposes 50 `skills/*/SKILL.md` files**; all ten specifically linked skills exist. Neither star counts nor proprietary scores demonstrate correctness, current API behavior, safe code or rankings.

### Playbook section-by-section dispositions

| Source segment | Supported concept, correction or exclusion | Relevant checklist IDs |
| --- | --- | --- |
| Opening/source claims | The article says 66 articles, 48 skills, 13 additional repositories and 14 ranked repositories, but only 9 repository URLs appear in the provided article. Linked 9 GitHub repos were opened; the RomeoSEO main tree currently contains 50 SKILL.md entries, not 48. Original 66 readings, vendor comparisons and SpaceCut results were not supplied. | Provenance; no checkbox |
| 1. Foundation: HTML, bots, live robots, CDN, www, canonical, sitemaps, schema | Google can render JavaScript; non-rendering crawlers may not. Test actual initial and rendered HTML, WAF challenges, preferred host, per-bot robots controls and true response bodies. OAI-SearchBot concerns ChatGPT Search, GPTBot training, ChatGPT-User user requests; Google-Extended is a product-control token, not a separate HTTP bot, while Googlebot controls Google Search AI. A spoofable curl User-Agent and HTTP 200 are insufficient. Apply truthful eligible markup, no fictitious ratings. | SEO-006/009/010/013/016/018/029/036/046/064, GEO-047/079/081; **new SEO-086** |
| 2. Bing, IndexNow, AI Performance | Owner Bing Webmaster Tools, sitemap and site inspection are useful; IndexNow applies to participating engines (not Google). Bing AI Performance reports sampled citation URLs/grounding phrases across supported experiences, not verbatim prompts, rankings, clicks or complete AI citations. | SEO-009/029, GEO-033/053 |
| 3. Search decisions and comparison pages | Review actual user intent and permitted results; original comparison/pricing facts, dated vendor sources, genuine shortcomings and transparent self-comparison improve content. Mandatory six of top ten SERPs, four shared results, 40–80 words, five to eight choices and a fixed own-product rank are unsupported heuristics. | SEO-002/003/004/014/028/084, GEO-006/009/012/013/027/037/042 |
| 4. GEO hidden searches, citations, brand fact sheets, video | Internal searches are not guaranteed inspectable or stable. The 44,070 citation, 85% external, under 4% first-party, and weekly source swap claims lack underlying methods. Dated authoritative product facts, wrong-claim/source tracing and later retests strengthen GEO-051. Video, caption/chapter choices depend on audience, accessibility and observed SERP features. | GEO-014/015/032/033/041/042/**051**/052 |
| 5. Measurement and free stack | Use authentic questions with dated answer-and-link samples; separately log mentions, citations, referrals, signups and self-reported discovery with privacy. Under-100 visits and the 3.4x example are heuristic and unverified. GSC aggregates Google AI Search under Web; Bing AI Performance is sampled/provider-specific. Free tiers, URL caps and billing can change. | GEO-031/032/033/052/053, SEO-029/030/031 |
| 6. Links, reviews, directories and forums | Original editorial research, suitable listings, legitimate unlinked brand credit and disclosed Reddit/Quora help are useful. No mandatory 20–30 listings, 120–180 word pitches or one self-promotion/week. Excessive link exchanges, paid fake profiles, fabricated reviews and scaled AI pages may be spam. | SEO-028/077/082/083/084, GEO-026 |
| 7. Agent-run SEO permission tiers, numbers and regression snapshots | Model must not invent Google clicks, rank, traffic, price or benchmark numbers. Tool/page provenance and 'not checked' strengthen SEO-004. Existing AGENT-018/023–048/099–100 handle tool-side permissions, approvals and destructive actions. New SEO-086 establishes separate production pre/post deployment crawlability and indexability diffs. A 32/40 editorial score is not a Google standard. | **Revised SEO-004, new SEO-086**; AGENT-018/043/048/099–100, LAUNCH-117/130 |
| 8. New domain schedule, pages and evidence | Choose cadence based on real audience, resources and available baseline; 1–4 weekly pages, 2–3 months, one video/page and a month-three optimization start are not universal controls or performance promises. | SEO-002/004/029/031/082/084, GEO-031/052 |

### Nine linked repository sources (the asserted “14” is not evidenced by this list)

| GitHub source | Source-reviewed disposition |
| --- | --- |
| [RomeoSEO/seo-skills](https://github.com/RomeoSEO/seo-skills) | README and tree inspected; 50 skills in current main tree and all ten requested paths present; optional, uninstalled. No security or outcome audit. |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | Already reviewed previously; useful technical/schema checks but provider-reported readiness scores and installers need scrutiny; avoid duplicate references. |
| [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) | README confirms Google Search Console MCP, local setup and default read-only; destructive/write operations can be enabled via GSC_ALLOW_DESTRUCTIVE=true. Check auth, tokens, connector and scopes before use. |
| [every-app/open-seo](https://github.com/every-app/open-seo) | Already reviewed optional platform; paid DataForSEO/data and initial-admin self-hosted risks remain; no independent feature parity test. |
| [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) | README confirms hosted MCP workflows including campaign and CMS tools; inspect permission/data recipients. The asserted outdated FAQ rating was not independently reproduced at an exact file/commit. |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | README documents agentic scores, curl-pipe-bash installer; prior risk catalog covers incorrectly conflated GPTBot/search, unsupported citability metrics. |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | README covers Claude SEO draft/publish pipeline and proprietary scores; alleged fictional-stories/density snippet was not reproduced at a fixed revision. |
| [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) | README points to remote connector.get-ryze.ai/mcp with GSC/GA4/ads and DataForSEO; hosted data and scope/cost approval required. |
| [i365dev/awesome-seo](https://github.com/i365dev/awesome-seo) | Linked reading-list repository accessible; not a verification or search ranking authority. Cloudflare mitigation claims checked against Cloudflare docs. |

### Ten requested RomeoSEO skill paths

All ten linked `skills/<name>/SKILL.md` paths were verified in the main tree on 2026-11-14; their presence is **not an installation, security review or performance endorsement**. The first six are optional references in `lists/frontend/13_SEO.md`, and the other four are in `lists/frontend/14_GEO_and_AEO.md`.

| Skill path | Mapped check(s) |
| --- | --- |
| [technical-seo-audit](https://github.com/RomeoSEO/seo-skills/tree/main/skills/technical-seo-audit) | SEO-006/013/036 |
| [schema-markup](https://github.com/RomeoSEO/seo-skills/tree/main/skills/schema-markup) | SEO-018/040/046 |
| [ai-agent-readiness](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-agent-readiness) | GEO-047/079/081 |
| [xml-sitemap-check](https://github.com/RomeoSEO/seo-skills/tree/main/skills/xml-sitemap-check) | SEO-009/029 |
| [seo-change-monitor](https://github.com/RomeoSEO/seo-skills/tree/main/skills/seo-change-monitor) | **SEO-086**, SEO-047 |
| [comparison-page-writer](https://github.com/RomeoSEO/seo-skills/tree/main/skills/comparison-page-writer) | SEO-002/003/028/084 |
| [ai-prompt-research](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-prompt-research) | GEO-001/031/052 |
| [ai-brand-facts](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-brand-facts) | **GEO-051**, GEO-017 |
| [seo-content-qa](https://github.com/RomeoSEO/seo-skills/tree/main/skills/seo-content-qa) | SEO-004/028 |
| [ai-traffic-analytics](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-traffic-analytics) | GEO-033/053 |

### Included “Hand this to your AI” prompt — seven stages

This is an **example prompt**, not permission to fetch a specific site, install a repo, connect owner accounts or make production changes.

| Proposed stage | Existing or added safe control |
| --- | --- |
| Read-only site audit with raw HTML, real robots, live sitemap and preferred host; cite status/content | SEO-006/009/013/016/036, GEO-079/081; site URL and permission not supplied so no run |
| Fix list with actual files, evidence and retest method | SEO-004/047 and review notes; do not invent paths or state |
| Approve before publish/change robots/canonical/redirects/noindex; no autonomous deletion | AGENT-023–048/099–100; server-enforced policy and reviewed diffs, not only an instruction |
| Retest after every approved edit | **SEO-086** and LAUNCH-117/130; no change executed |
| Owner-only GSC/Bing, directory, outreach and video tasks | SEO-029/082; conditional permissions |
| 20 buyer prompts marked sourced versus guessed | GEO-001/031/052; exact 20 not mandatory |
| Five decision-page candidates, inspect actual current SERPs, wait for editorial selection | SEO-002/003/004/084; avoid prohibited automated Google scraping and auto-publishing |

### Independently verified platform distinctions (2026-11-14)

- [OpenAI official crawlers](https://developers.openai.com/api/docs/bots): `OAI-SearchBot` supports ChatGPT Search, `GPTBot` training, `ChatGPT-User` user-requested fetching. Blocking GPTBot alone does **not** mean ChatGPT Search exclusion. [Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended) is **not** a separate HTTP User-Agent; for Google Search AI, [Googlebot/indexability controls](https://developers.google.com/search/docs/appearance/ai-features) are relevant.
- [Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics): raw HTML may differ from Google-rendered content. [Cloudflare Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/) may challenge legitimate traffic; a single spoofed `curl -A` HTTP status is not verified crawler access or proof the relevant content rendered. Treat all external site and provider access as conditional.
- [IndexNow](https://www.indexnow.org/faq) notifies participating engines (not Google). [Bing AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) exposes **sampled aggregate** citation/grounding reports, not exact end-user prompts, ranking or total AI citations. Google Search Console includes Google Search AI results under aggregate Web, not isolated citation rows.
- [SoftwareApplication markup](https://developers.google.com/search/docs/appearance/structured-data/software-app) is eligible only under applicable Google guidelines; no fabricated review/rating data. [Google spam policy](https://developers.google.com/search/docs/essentials/spam-policies) prohibits link schemes and scaled unhelpful content. A fixed 32/40 scoring rubric, exact sample counts, keyword and editorial quotas, monthly timelines or third-party-citation ratios have no provided primary dataset and must not become universal pass/fail requirements.
- **Agent protection:** [RomeoSEO `seo-change-monitor`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/seo-change-monitor) supplies a representative before/after status/indexability diff. This prompted the distinct new **SEO-086**, while claim-level fact tracing from [`ai-brand-facts`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-brand-facts) strengthened **GEO-051**. Existing agent restrictions **AGENT-018/023–048/099–100** already require real authorization, and are not implemented by the user-provided prompt.
- **Vendors:** The article mentions ChatSEO and Distribb prices, paid MCP tools, DataForSEO connections, link networks and CMS automation. These are **unverified author-supplied vendor claims**, not a live price or authorization review. No vendor was connected, installed, paid, or asked to publish. The claims about 85% third-party citations, 44,070 observations, 3.4x attribution and weekly citation churn lack inspectable source studies in the pasted text.

**Outcome:** Added **SEO-086** (versioned, live production SEO regression snapshots) and revised **SEO-004**, **GEO-051**, **GEO-079**. Added ten optionally linked agent skills to appropriate frontend appendices and informational risk warnings for crawler taxonomy, unsupported thresholds, tool permissions and vendor assertions. The existing SEO, GEO, launch and AGENT checks cover the rest. **91 scope files; 4,189 globally unique unchecked checks** (682 shared, **683 frontend**, 1,117 backend, 1,707 AI). No modifications of customer sites, no skill installations and no external Search Console/GSC credentials used.

## Supplemental intake (2026-11-14): Pasted “#1 Google ranking for a social post” technique

**Source/provenance boundary:** The user pasted the social post text on **2026-11-14** with no original post permalink, identifiable author, supported platform/account name, keyword, screenshot, date of the purported ranking, verified Search Console property, referral report or sale evidence. Consequently the writer's **“ranked #1”** and guaranteed traffic/sales statements are **anecdotal and not independently verified**. The generic post recommends four steps; **the feature it describes is genuinely new since the previous SEO checklist**: Google introduced **platform properties** for creators in July 2026 and [announced global availability July 29, 2026](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide). Its [current platform-property documentation](https://support.google.com/webmasters/answer/17148418) says Instagram, TikTok, X and YouTube are supported. The Help Center still contains older gradual-rollout wording; confirm actual access, ownership and data availability in the selected account, not from a screenshot.

| User step or assertion | Verified applicability and limitations | Check disposition |
| --- | --- | --- |
| **1. Search Console → Add property → connect your social media; see “all search traffic”** | **Real but specific:** add a distinct **platform property** for each supported owned account or channel, verify via account authorization or existing authorized association, inspect **Google Search** performance and Discover/News where reported. [Google Help](https://support.google.com/webmasters/answer/17148418) distinguishes these metrics from views **inside** social platforms; account additions do not change Search ranking, data processing can take time, and properties require ownership/access. Not a generic property for every platform or an unauthenticated third-party post. | **New SEO-087** in `lists/frontend/13_SEO.md`; existing **SEO-029/030/031** cover ownership/measurement and privacy but not platform-specific controls |
| **2. Choose a keyword and inspect SERPs; Ahrefs optional** | Audience search intent and current SERP research are legitimate research; Ahrefs keyword/competition estimates are vendor-defined, not necessary or verified ranking predictions. Use lawful/manual search, observed Google platform property query data if available, and original useful content. | Already **SEO-002/003/031/084**, existing optional Ahrefs reference; **no duplicated check** |
| **3. Write a platform-native post with keyword at the beginning** | Relevant truthful language, understandable titles/captions and self-contained helpful posts may be useful, but Google has **no blanket “keyword must be first” rule**; platform content controls, visibility and indexing differ by host. Avoid keyword stuffing or publishing repetitive low-value content solely to exploit social-domain reputation. | Already **SEO-003/004/028/082/084**; optional **SEO-087** workflow note, **no new content quota or fixed placement rule** |
| **4. Share with followers; post will appear on Google and bring traffic/sales** | Distribution to followers is not an indexing, ranking, or purchase guarantee. Independent public content **can** appear in Search where eligible; measure actual Google impressions/clicks in platform properties, separate from native engagement, website sessions/leads and sale attribution. [Google's technical guidance](https://developers.google.com/search/docs/essentials/technical) explicitly states that Google eligibility does not guarantee indexing. | **SEO-087/030/031**; outcome guarantee **rejected**, risk entry in `seo-aeo-geo-tricks.md` |
| **“Ranked #1” illustrative outcome** | No actual query, country, device, search date, URL, observed SERP or verified account data supplied, so the success story cannot be reproduced or used as a general benchmark. | **Unverified anecdote, not an acceptance criterion** |

**Authoritative evidence reviewed 2026-11-14:** [Google Search Console platform properties launch](https://developers.google.com/search/blog/2026/07/search-console-social-video-platforms) (July 7), [global availability announcement](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) (July 29), [platform property setup and data definitions](https://support.google.com/webmasters/answer/17148418), [Google's social/video analysis guide](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content), [Search Console property ownership](https://support.google.com/webmasters/answer/34592) and [Search technical requirements](https://developers.google.com/search/docs/essentials/technical). Google-related reporting and in-app platform traffic are distinct; no ranking, social account, external API or actual post was checked.

**Outcome:** Added one conditional **SEO-087** in `lists/frontend/13_SEO.md`, official primary references, an optional verified account workflow and one caution row. Related keyword research, on-page writing, distribution, site analytics and anti-spam checks were **already covered** and not duplicated. **91 scope files; 4,190 globally unique unchecked checklist items** (682 shared, **684 frontend**, 1,117 backend, 1,707 AI), SEO domain **87** (72 frontend SEO checks plus 15 backend SEO checks; earlier narrative counts underreported the domain).

## Pending source intake (2026-11-14): Two inaccessible Instagram SEO-tricks reels

**Requested sources:** [Instagram reel Dfj7faNyjrm](https://www.instagram.com/reels/Dfj7faNyjrm/) and [Instagram reel DfIFN3dk5VK](https://www.instagram.com/reels/DfIFN3dk5VK/), both submitted by the user as candidate “SEO tricks.” No post authors, original publication dates, captions, transcripts, screenshots, or explanatory text accompanied the URLs.

| Source | Direct retrieval performed | Evidence available and disposition |
| --- | --- | --- |
| [Dfj7faNyjrm](https://www.instagram.com/reels/Dfj7faNyjrm/) | Called the user-requested Insta Loader `process_instagram_video` using both `/reels/Dfj7faNyjrm/` and `/reel/Dfj7faNyjrm/`; attempted public-web exact URL/shortcode searches and direct page access | **Not retrieved.** Insta Loader returned “Instagram sent an empty media response”; public web access did not yield the actual caption, spoken words or usable footage. The technique and any associated statistics are **unknown**; **no SEO/GEO check created or revised** |
| [DfIFN3dk5VK](https://www.instagram.com/reels/DfIFN3dk5VK/) | Called Insta Loader using both `/reels/DfIFN3dk5VK/` and `/reel/DfIFN3dk5VK/`; attempted public-web exact URL/shortcode searches and direct page access | **Not retrieved.** Same empty-media error and no verifiable caption/audio/video from the alternate route or public results. The technique and any associated statistics are **unknown**; **no SEO/GEO check created or revised** |

**Evidence limitation and next step:** Public access without an Instagram-authenticated media session was insufficient. No cookies, credentials, authenticated downloads, fabricated captions or speculative SEO methods were used. The source URL alone cannot establish a method, a claim, an outcome, or a suitable checklist ID. If the user supplies the transcripts, captions or screenshots from these exact reels, reassess each actionable point against the existing SEO/GEO and adjacent checklist IDs and verify any platform claims before editing scope checks.

**Repository impact:** Provenance-only entry; no new or revised numbered checklist IDs, no instructions adopted as facts, no change to scope files or release gates. The verified latest repository inventory remains **91 scope files / 4,190 unique unchecked checks** (682 root, 684 frontend, 1,117 backend, 1,707 AI).

## Classification update (2026-11-14): Practical SEO/GEO methods versus shortcuts

At the user's request, actionable, audience-serving methods from the previously pasted SEO/GEO posts were placed in the normal **Suggested testing tools** appendices of `lists/frontend/13_SEO.md` and `lists/frontend/14_GEO_and_AEO.md`. They cover first-party Search Console page–query research, useful decision pages with original evidence, earned editorial mentions and community contributions, accessible social/video publishing, AI-answer source sampling, brand-fact corrections and privacy-conscious crawler-access diagnostics. They reuse existing checks **SEO-002/003/004/011/014/018/028/029/030/031/077/082/083/084/085/086/087** and **GEO-001/006/013/027/031/032/033/040/042/043/044/047/051/052/053/079/081**, without adding duplicate IDs.

Fixed growth formulas, guaranteed ranking and traffic promises, artificial link/review exchanges, attempts to infer hidden competitor plans from public paths, karma farming, host-domain exploitation, citation-percentage shortcuts, and uncontrolled agent auto-publishing were consolidated as **twelve source-reported trick categories** in `seo-aeo-geo-tricks.md`. The earlier detailed **69-step backlink breakdown**, search query regex strings, platform notes, and all 36 Okara image items remain in this existing source audit. The two user-submitted Instagram Reel links [Dfj7faNyjrm](https://www.instagram.com/reels/Dfj7faNyjrm/) and [DfIFN3dk5VK](https://www.instagram.com/reels/DfIFN3dk5VK/) are also linked from the tricks file; their captions and speech were not accessible from the earlier request, so the repository does not assign them invented procedures.

**Outcome:** Main checklist **appendices** expanded, existing separate tricks file expanded, provenance recorded. **No added/changed numbered checks and no installed tools or site actions.** Inventory unchanged: **91 populated scope files / 4,190 unique unchecked checks** (682 shared, 684 frontend, 1,117 backend, 1,707 AI).

## Supplemental intake (2026-11-15): Stef Builds launch QA and Tuts+ indie game marketing

**Sources:** User-pasted Stef Builds email description with [launch-readiness checklist](https://stefbuilds.com/checklist?utm_source=email&utm_medium=launch&utm_campaign=delivery-checklist) and [100 places to launch a product](https://stefbuilds.com/launch-sites?utm_source=email&utm_medium=launch&utm_campaign=delivery-checklist); Tuts+ [indie game developer marketing checklist](https://github.com/tutsplus/Marketing-Checklist-For-Indie-Game-Developers/blob/master/Indie%20Game%20Developer%20Marketing%20Checklist.md) (GitHub `master` file directly inspected, blob `b783700c838b0c84abfd8cb440abf6c2af581c5f`; repository source dates to 2013). Source links, scope and limitations are expanded in the root informational [outreach.md](https://github.com/Pro-GenAI/checklists-2/blob/main/outreach.md#20-stef-builds-app-launch-checks-and-100-site-bonus-limited-access) and [indie-game section](https://github.com/Pro-GenAI/checklists-2/blob/main/outreach.md#21-tuts-indie-game-developer-marketing-checklist-historical-2013).

**Stef's customer journey:** A five-stage set of steps: **homepage → main CTA → signup → using the app → purchase and purchased feature access**, including the source's instruction to make **one real purchase from a new account** and independently verify the app actually unlocks what was bought. Existing checklist mapping (examples, **not** proof of completing them): `UX-083` primary CTA, `UX-020` labels, `TST-012` onboarding/signup, `TST-002` user journeys, `LAUNCH-041/066/068/078` critical journeys and payment integrations, and frontend `LAUNCH-110/111` form/billing feedback and entitlements. These controls already address the actionable, general-purpose concepts; no additional stable checklist ID was justified by the supplied source text.

**Stef's money-loss checks:** Email says **eight** categories, but only **four examples** are explicitly identified: API-key exposure, personal-data leakage, unsolicited/unwanted marketing and tax omissions. Existing `SEC` controls, `LEG-014/021/074` (consent, taxation/subscriptions, email opt-out) and release-readiness safeguards are the suitable review entry points. The remaining four exact categories, underlying examples, master agent prompt and the bonus **100-site list** are **not available**; both webpage links were attempted but inaccessible. Do not invent their specifics or authorize unsandboxed production credential sharing. Financial/tax/legal checks need qualified review where applicable.

**Game marketing:** Tuts+'s 2013 source supplies game-focused website/blog/social/RSS/trailer/demo assets, seven press-kit elements, a press-email structure, ten historical press outlets and seven alternatives (crowdfunding, Alphafunding/Desura, Steam Greenlight, indie databases, r/indiegames, conventions, contests/game jams). These are marketing/promotional workflows rather than a new general-purpose software launch quality gate; recorded in the outreach catalog. **Historical correction:** Valve's [June 6, 2017 announcement](https://store.steampowered.com/news/posts/?enddate=1496780339) documents Steam Greenlight's retirement and June 13, 2017 Steam Direct launch; original outlet links, rights/licensing and other platform status should be rechecked before use.

**Disposition:** Source references and existing-ID mappings added; **no new/changed numbered checklist IDs**, no check completion, no AI prompt executed, site scan performed, purchases tested, press emails sent or directory submissions made. Keep the checked-template inventory at **91 numbered scope files / 4,190 unique checks**.


## Supplemental intake (2026-11-15): Stef Builds legal scan and reel

**Sources:** [Stef Builds Scan](https://stefbuilds.com/scan) and [Instagram reel DfnqAxaMdjG](https://www.instagram.com/reels/DfnqAxaMdjG/), supplied by the user and classified as **prelaunch legal-issue prevention** resources. Related previously cataloged source: [Stef Builds checklist](https://stefbuilds.com/checklist).

**What is available:** Direct source URLs and the user's classification. The web page did not return a readable body and Instagram extraction failed, so no specific scan behavior, tests, output claims, provider prices or reel statements can be independently established. The earlier Stef email supplies four named risk areas (exposed secrets, customer-data leaks, unwanted marketing, tax obligations) and five customer-flow stages; these are **previous sources**, not newly inspected `/scan` features.

**Existing controls:** `LEG-004` (legal risk inventory), `LEG-011/013/014/018` (personal-data practices and consent), `LEG-021` (subscriptions/pricing/tax), `LEG-074` (commercial email), `SEC-017/020/023/024` (testing, secrets and data), and `LAUNCH-066/068` (signup/payment smoke coverage). The legal checklist's **Suggested testing tools** section now links the external scan as a candidate.

**Disposition:** Source indexing and current-check mapping only; no scan executed, legal clearance claimed or checklist checkbox modified. Inventory unchanged: **91 scope files / 4,190 checks**.

