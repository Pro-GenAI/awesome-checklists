# Optional testing tools — frontend checklists

**Editorial relocation: 2026-11-15.** This file preserves optional browser/client testing examples previously appended after source-review dates in numbered frontend checklists. Its commands and vendor links are not automatically approved, necessary for every stack, or proof of security, accessibility or quality. Test only authorized environments, minimize credentials/data, pin dependencies and record per-ID evidence. Prefer established project tools and the [shared review method](review-method.md); security-specific suggestions remain in the [dedicated security catalog](security-testing-tools.md).

## 01_Requirements_and_Planning

Source: [lists/frontend/01_Requirements_and_Planning.md](../frontend/01_Requirements_and_Planning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** acceptance criteria, negative scenarios, and scope changes; include browser and client behavior where applicable.
- **Cross-stack:** [Cucumber](https://cucumber.io/docs/guides/overview/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest-bdd](https://pytest-bdd.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 02_LegalIssues

Source: [lists/frontend/02_LegalIssues.md](../frontend/02_LegalIssues.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** consent, retention, access, export, deletion, and policy-enforcement behavior (legal interpretation remains manual); include browser and client behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 03_Architecture_and_CodeQuality

Source: [lists/frontend/03_Architecture_and_CodeQuality.md](../frontend/03_Architecture_and_CodeQuality.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** dependency boundaries, code quality, interface contracts, and architectural regression; include browser and client behavior where applicable.
- **Cross-stack:** [Semgrep](https://semgrep.dev/docs/) + [dependency-cruiser](https://github.com/sverweij/dependency-cruiser).
- **Python:** [Ruff](https://docs.astral.sh/ruff/) + [mypy](https://mypy.readthedocs.io/en/stable/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeScript tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html) + [ESLint](https://eslint.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [ESLint](https://eslint.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 04_UI_UX_and_Usability

Source: [lists/frontend/04_UI_UX_and_Usability.md](../frontend/04_UI_UX_and_Usability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** navigation, responsive layouts, form errors, visual states, and user flows; include browser and client behavior where applicable.
- **Cross-stack:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) + [Storybook](https://storybook.js.org/).
- **Python:** [Playwright](https://playwright.dev/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Storybook](https://storybook.js.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Storybook](https://storybook.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 05_Accessibility

Source: [lists/frontend/05_Accessibility.md](../frontend/05_Accessibility.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** keyboard navigation, focus order, accessible names, contrast, and assistive-tech flows; include browser and client behavior where applicable.
- **Cross-stack:** [axe DevTools](https://www.deque.com/axe/devtools/) + [WAVE](https://wave.webaim.org/).
- **Python:** [Playwright](https://playwright.dev/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 06_Internationalization_and_Localization

Source: [lists/frontend/06_Internationalization_and_Localization.md](../frontend/06_Internationalization_and_Localization.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** plural rules, locale formatting, missing strings, RTL, and long-text layouts; include browser and client behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/).
- **Python:** [Babel](https://babel.pocoo.org/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [FormatJS](https://formatjs.github.io/docs/getting-started/installation) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [i18next](https://www.i18next.com/) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 07_API_Design_and_Integrations

Source: [lists/frontend/07_API_Design_and_Integrations.md](../frontend/07_API_Design_and_Integrations.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** API schemas, auth, errors, compatibility, and dependency failures; include browser and client behavior where applicable.
- **Cross-stack:** [Redocly CLI](https://redocly.com/docs/cli/) + [Pact](https://docs.pact.io/).
- **Python:** [Schemathesis](https://schemathesis.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Supertest](https://github.com/ladjs/supertest) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Dredd](https://dredd.org/en/latest/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 08_Data_and_DatabaseManagement

Source: [lists/frontend/08_Data_and_DatabaseManagement.md](../frontend/08_Data_and_DatabaseManagement.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** migrations, constraints, permissions, data integrity, rollback, and concurrent writes; include browser and client behavior where applicable.
- **Cross-stack:** [pgTAP](https://pgtap.org/) + [Testcontainers](https://testcontainers.com/).
- **Python:** [testcontainers-python](https://testcontainers-python.readthedocs.io/) + [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 10_Documentation_and_DeveloperExperience

Source: [lists/frontend/10_Documentation_and_DeveloperExperience.md](../frontend/10_Documentation_and_DeveloperExperience.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** links, snippets, onboarding setup, and API documentation examples; include browser and client behavior where applicable.
- **Cross-stack:** [lychee](https://github.com/lycheeverse/lychee) + [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2).
- **Python:** [doctest](https://docs.python.org/3/library/doctest.html) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeDoc](https://typedoc.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [JSDoc](https://jsdoc.app/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 11_Testing

Source: [lists/frontend/11_Testing.md](../frontend/11_Testing.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** unit/integration, API contract, end-to-end, and regression test runs; include browser and client behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Pact](https://docs.pact.io/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/) + [coverage.py](https://coverage.readthedocs.io/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/) + [Playwright](https://playwright.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/) + [Playwright](https://playwright.dev/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Manual browser modes:** Use Chrome DevTools with JavaScript disabled, network throttling/offline mode, and representative supported browsers for applicable test paths.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 12_Performance_and_Scalability

Source: [lists/frontend/12_Performance_and_Scalability.md](../frontend/12_Performance_and_Scalability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** throughput, latency percentiles, browser responsiveness, and resource budgets; include browser and client behavior where applicable.
- **Cross-stack:** [k6](https://grafana.com/docs/k6/latest/) + [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).
- **Python:** [Locust](https://docs.locust.io/) + [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [autocannon](https://github.com/mcollina/autocannon) + [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Browser measurement options:** [Unlighthouse](https://github.com/harlan-zw/unlighthouse) for sampled multi-page lab audits; [Lighthouse CI configuration](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md) for appropriately calibrated CI assertions; and [web-vitals](https://github.com/GoogleChrome/web-vitals) for client-side LCP/INP/CLS callbacks sent to a privacy-reviewed reporting endpoint. Merely installing `web-vitals` does not enable RUM, and lab Lighthouse scores cannot replace measured field percentiles.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 13_SEO

Source: [lists/frontend/13_SEO.md](../frontend/13_SEO.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** crawlability, robots/canonical, rendered metadata, and structured data; include browser and client behavior where applicable.
- **Cross-stack:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) + [Rich Results Test](https://search.google.com/test/rich-results) + [Google Search Console](https://search.google.com/search-console/about) (URL Inspection and Sitemaps) + [Bing Webmaster Tools](https://www.bing.com/webmasters/about).
- **Specialized:** [Schema Markup Validator](https://validator.schema.org/) for schema.org syntax + [PageSpeed Insights](https://pagespeed.web.dev/) for field/lab metrics; inspect actual live URLs and representative paginated, media, and regional pages.
- **Python:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [schema-dts](https://github.com/google/schema-dts) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Optional SEO research and validation:** [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/), [WebPageTest](https://www.webpagetest.org/), [Meta Sharing Debugger](https://developers.facebook.com/tools/debug/), [Google Trends](https://trends.google.com/), and [Moz Keyword Explorer](https://moz.com/explorer). Choose only suitable, maintained tools for the project.
- **Optional crawl/CI toolkit (own or authorized sites only):** [SEOnaut](https://github.com/StJudeWasHere/seonaut) for self-hosted site crawling, redirect/link and metadata diagnostics (Docker/database required; secure credentials, instance exposure and crawl rate); [Unlighthouse](https://github.com/harlan-zw/unlighthouse) for representative multi-page Lighthouse audits (uses sampling, not proof that every URL was tested); [lychee](https://github.com/lycheeverse/lychee) for broken links in HTML/Markdown; and [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) with a configured `lighthouserc` and actual CI trigger for repeatable lab checks. An SEO score is not a ranking guarantee or a real-user performance measurement.
- **Conditional agent-connected diagnostics (not required for SEO):** [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) can inspect an approved, isolated Chrome session, network traffic and performance traces; review which browser data the agent can read/change, disable or disclose usage telemetry where appropriate, and exclude logged-in customer sessions and secrets. [Search Console MCP](https://github.com/saurabhsharma2u/search-console-mcp) can query owned, authorized GSC/Bing/GA4 properties, but verify OAuth scope, property matching, token storage, optional writes and provider-supported URL submission; do not mistake Indexing API notifications for guaranteed indexing. Inspect the tools and their permissions before installation, and independently validate findings.
- **Optional SEO research platform (not a mandated skill or ranking replacement):** [OpenSEO](https://github.com/every-app/open-seo) offers keyword, backlink, rank and crawl research with hosted, Cloudflare and Docker variants and MCP access. Self-hosted data calls require a paid [DataForSEO](https://dataforseo.com/) account and may use additional provider APIs. **Register the first admin before exposing the URL publicly**, protect credentials/session and agent endpoints, inspect provider/query permissions and hosting limits, and verify measurements against Search Console. An open-source 'Semrush/Ahrefs alternative' description does not establish feature parity or zero cost.
- **Optional Search Console intent research (owned property):** Performance → Search results → Add filter → Query → Custom (regex) accepts RE2. The sample `^(?:\S+\s+){7,}\S+$` finds eight-or-more whitespace-separated query tokens; `^(who|what|when|where|why|how|which|can|does|is|should)\s` samples selected English question starts. Match each query to its *actual* landing page, intent and dates; provide a truthful concise answer on the appropriate existing page and review impressions, clicks and CTR. These are not exhaustive (anonymized/truncated queries and language variants), do not prove AI citations or conversion intent, and are not a mandate to create thin FAQ pages or retired Google FAQ rich-result markup. See **SEO-002/031/046**.
- **Optional earned editorial discovery:** Research relevant buyer roundups, journalist requests, original studies with documented sample/method, unlinked factual credits, relevant broken/outdated resource replacements, tested free calculators, consented visual/video explanations, authentic case studies and eligible directories. Obtain independent editor approval, verify rights and claims, prefer permanent accurate URLs, and log actual links/referrals. Restore/redirect your own old URLs only to equivalent successors; avoid manufactured link swaps, automated pitches and guaranteed AI citations. See **SEO-082**.
- **Optional public competitor-content research:** Public `/robots.txt`, `/sitemap.xml`, accessible subdomains and live pages can suggest *incomplete* topic/offer leads, not secret plans. `Disallow` is not a privacy boundary; XML sitemaps are not exhaustive; `lastmod` does not reliably forecast campaigns, and repeated headlines cannot prove winning A/B tests. Respect content rights and access policies; publish original value rather than copying competitive materials.

- **Optional community-led intent research:** Read relevant public Reddit/forum discussions and rules to identify recurring unanswered customer problems; write original, sourced content for owned properties and participate only where you can help. Use an authentic account, accurate affiliation disclosure and community-appropriate links; neither a universal **90/10 posting rule**, daily karma schedule nor `nofollow`/UGC treatment guarantees ranking or AI citations. Do not automate promotional posts, manufacture reviews, disguise link targets, or treat public posts as reusable proprietary copy. See **SEO-002/028/077/082**.
- **Optional GSC commercial-query research (owned properties only):** Performance → Search results → Add filter → Query → Custom (regex). Paste `\b(best|vs|versus|alternatives?|pricing|cost|reviews?)\b`. This RE2 filter finds selected English comparison/purchase-related words, not customers or guaranteed sales. Inspect the matching page in Pages, SERP context, search appearance, average position, impressions, clicks, CTR, device and dates; change titles only when an accurate improvement serves that page and monitor real outcomes. ASCII word boundaries miss some languages and variants; hidden/anonymized Search Console rows limit completeness. See **SEO-014/031**.
- **Optional on-page optimization toolkit (source-checked 2026-11-14):** [Google Search Console](https://search.google.com/search-console/about) and [Bing Webmaster Tools](https://www.bing.com/webmasters/about) for authorized search data; [Ahrefs](https://ahrefs.com/keywords-explorer) for keyword and content-gap research; [Semrush On Page SEO Checker](https://www.semrush.com/kb/292-on-page-seo-checker) for competitor/page ideas; [Yoast SEO](https://yoast.com/features/seo-analysis/) and [Rank Math](https://rankmath.com/kb/seo-analysis/) for applicable CMS/WordPress work; [Surfer Content Editor](https://docs.surferseo.com/en/articles/5700347-content-editor-overview), [MarketMuse Optimize](https://docs.marketmuse.com/workflows/optimize/) and [SE Ranking](https://help.seranking.com/hc/en-us/articles/16333726680988-On-Page-SEO-Checker-Overview) for optional content/on-page research. Vet plan availability, permitted use, API/AI data sharing, and human sign-off. Proprietary KD, search-volume, content scores and suggested word counts are not Google grading standards; the separately promoted SEO Wins library was unavailable for audit.
- **Optional smaller-site content workflow:** Group genuine audience queries by intent into distinctive useful pages; inspect permitted search results and differentiate them with independently fact-checked substance. Use AI as a drafting assistant, not an auto-publisher, and add only contextually useful internal links. Inspect page-specific Search Console evidence after enough data accrues, edit only relevant passages, and optionally request recrawls after meaningful changes. No mandatory KD=0, volume=0–10, 10–15-page batch, 3–5 internal links, fixed title/meta character limits, seven-day loop, 2–5 monthly backlinks, or 3–12-month ranking guarantee. See **SEO-002/004/011/014/029/031/082/084**.
- **Optional live-site SEO change-monitoring workflow (2026-11-14):** Use a stored baseline and a post-release diff for representative and high-traffic production pages, `www`/preferred-host behavior, response status, `X-Robots-Tag`, initial/rendered content, canonical, sitemap and `robots.txt` (including edge/CDN-managed behavior), rather than relying on local source files or a superficial `curl -A` User-Agent/status-only check. Identify actual WAF challenges, redirect targets, and content served; a spoofable User-Agent string cannot verify a crawler identity. Keep a remediation owner, human approval for destructive/sitewide SEO changes and an actionable rollback. See **SEO-086**, **SEO-029**, **GEO-079/081**, **AGENT-043/048**.
- **Optional source-reviewed RomeoSEO skills (not installed or independently security-audited):** [`technical-seo-audit`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/technical-seo-audit), [`xml-sitemap-check`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/xml-sitemap-check), [`schema-markup`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/schema-markup), [`seo-change-monitor`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/seo-change-monitor), [`comparison-page-writer`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/comparison-page-writer) and [`seo-content-qa`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/seo-content-qa) are task-specific agent-skill prompts. Verify their current content and scripts before running them, restrict filesystem/network/CMS permissions, and treat all numeric audits and pass scores as unverified until measured against your own site. Tool use is optional; prefer observed URLs, response evidence, accessible content, genuine reviews, accurate vendor pricing/date and human editorial approval. Do not use these skills to install or publish automatically.
- **Optional social-post Google Search discovery workflow (reviewed 2026-11-14):** For a creator/business that controls a supported public Instagram, TikTok, X or YouTube account, use Search Console → property selector → **Add property** → supported platform → complete account/channel verification (or select an already connected property). Analyze genuine query–post pairs, impressions, clicks and other **Google-side** performance across the actually available Google Search surfaces, then use audience intent and independent fact-checking to inform helpful, platform-native titles/captions and distribution. Google announced global access on **2026-07-29**, but still verify the actual account and report availability; new properties can show partial/initially empty data. This does **not** measure all social-platform views, guarantee post indexing or make a keyword at the beginning mandatory. Separate Google clicks from platform engagement, site referrals and actual sales. See **SEO-087**, **SEO-002/028/031**.
- **Actionable Search Console content-opportunity worksheet (owned properties):** Export a dated **page–query** sample, group queries by actual intent, and compare impressions, clicks, CTR, position and destination URL. Optionally use the existing question, eight-token and commercial-word regex samples. Select one relevant page and make a specific improvement: a clear first-paragraph answer, accurate comparison, better internal link or descriptive title that matches the page. Record the old text, update date, and observed results; never infer purchases solely from query wording. Maps to **SEO-002/004/011/014/031**.
- **Ethical decision-page and first-hand research workflow:** Start with genuine buyer questions from product support, search data or customer feedback; inspect permitted public search results for the type of answer people need. Consolidate overlapping queries into one useful page, test competing solutions or a free calculator with unusual input cases, publish original examples/limitations and cite dated, source-checked pricing. Add only relevant internal links and appropriate schema. Revisit for factual changes instead of using a keyword-density, page-count, title-length or weekly-publication target. Maps to **SEO-002/003/004/011/014/018/028/034/084**.
- **Editorial coverage and community workflow:** Find accurate category roundups, unlinked credits, active public forum discussions, journalist questions, genuine vendor case-study opportunities and relevant organizations/directories. Contribute a distinct original statistic, tested product example, permissioned diagram/video, or useful explanation; send targeted, low-pressure messages and maintain factual publisher entries with editor consent. Follow forum rules, disclose affiliation and log live references and actual referrals separately from AI mentions. Maps to **SEO-028/031/077/082/083**.
- **Public competitive-content research, limited to accessible pages:** Review public navigation, published comparison pages, sitemaps and robots rules to find topical gaps worth answering *independently*. Record the exact source and date, and treat URL prefixes and repeated headlines as observations rather than proof of private marketing plans or conversion experiments; never try to bypass access controls or copy protected assets. Maps to **SEO-002/003/007/009/028/082**.
- **Social and video discoverability:** On supported accounts the owner controls, review Search Console platform-property post/query reports, and compare them with native analytics and actual referrals. Publish useful platform-specific descriptions, accessible subtitles/transcripts and real demos where audience interest supports them. A post's position in Google Search is a result to measure, not an outcome created merely by adding an account, putting a term first or sharing. Maps to **SEO-020/030/031/080/087**.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 14_GEO_and_AEO

Source: [lists/frontend/14_GEO_and_AEO.md](../frontend/14_GEO_and_AEO.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** machine-readable answers, structured data, citation links, and content consistency (not rankings); include browser and client behavior where applicable.
- **Cross-stack:** [Schema.org Validator](https://validator.schema.org/) + [lychee](https://github.com/lycheeverse/lychee).
- **Python:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [schema-dts](https://github.com/google/schema-dts) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Optional AI-answer visibility research platforms (upstream reviewed 2026-11-14; not required or independently benchmarked):** [NiubiGEO](https://github.com/Albert-Weasker/niubigeo) offers self-hosted multi-model brand and competitor prompt research with saved original responses/citations, repeatable observations, dated comparison and keyword monitoring (some monitoring features are beta). Keep explicit model/search settings and baseline prompts, export answer/link evidence, capture failed runs, and protect API keys; self-hosting does not eliminate external model-API disclosure or provider/hosting charges. [OpenSEO](https://github.com/every-app/open-seo) also provides optional SEO and AI-visibility research with [agent plugin skills](https://github.com/every-app/open-seo/tree/main/plugins/openseo/skills); its self-hosted data features can require paid DataForSEO and additional APIs. Secure/claim the initial admin **before** any public exposure. For either product, map results to **GEO-031–033/052/053**; do not confuse tool-derived scores, brand mentions or referral analytics with independently observed AI citation links.
- **Optional answer-source research:** With a responsible owner's permission, sample authentic buyer questions across selected AI answer tools; retain observed answers, dated source URLs and changing results before proposing original data, helpful comparisons, corrections, publisher outreach or genuine review profiles. An independent editor may decline a pitch, no platform is obligated to cite the page, and citation share requires a **defined provider/query/timeframe denominator**. When available, compare separately with [Bing Webmaster Tools AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) (aggregate cited pages and preview Citation Share) and Search Console Web search/analytics (clicks/impressions, not an isolated Google AI citation report). Do not equate log fetches, backlinks or GA4 referrers with AI answer links; see **GEO-031–033/052/053**.
- **Optional RomeoSEO GEO/AI-agent skills (source paths verified 2026-11-14, not installed):** [`ai-agent-readiness`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-agent-readiness), [`ai-prompt-research`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-prompt-research), [`ai-brand-facts`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-brand-facts) and [`ai-traffic-analytics`](https://github.com/RomeoSEO/seo-skills/tree/main/skills/ai-traffic-analytics) can inform **GEO-031–033/047/051–053/079–081** as reviewer aids. Pin and inspect instructions, scripts, connector scope, data recipients and costs before use. Independently validate actual source URLs, dated answer samples and brand facts; avoid confusing a model's hidden searches, GSC impressions, crawler hits, traffic attribution, Bing AI Performance aggregate citations and an observed answer's linked citation.
- **AI-answer citation opportunity register:** Build a small, dated set of *real* customer questions; record the answer, displayed brand names, direct cited URLs, provider/model, relevant language/locale and repeats. Group cited sources as independent buyer guides, review directories, forums, videos and official websites. Where a third-party page is genuinely missing a tested product fact, original dataset or meaningful alternative, contact its editor with the supporting evidence and respect their choice. Treat published mentions, linked AI citations, crawls and conversions as distinct observations. Maps to **GEO-001/031/032/033/052/053** and **SEO-082**.
- **Brand-fact and practical answer upkeep:** Maintain a dated canonical product reference (features, supported platforms, current plans/prices, availability and limits) and test representative answers against it. For a discrepancy, preserve the quoted answer and linked source if visible, correct your own authoritative pages or send a documented correction request to independent publishers, then resample the relevant questions. Use source-complete short answers and appropriate accessible comparison tables/videos, without fixed 40–80-word, 20-prompt or two-month thresholds. Maps to **GEO-006/013/027/042/043/044/051/052**.
- **Search-access diagnostics from owned telemetry:** For explicitly targeted AI search crawlers, compare live robots and WAF/CDN policy with aggregated permitted edge/origin logs, meaningful HTTP status/blocked-event reasons and delivered HTML. Keep search crawler traffic separate from training bots and user-triggered requests; when a key public page has no visible requests, also check the logging window and crawler identity before changing the site. Maps to **GEO-047/079/081**, **SEO-013/086**.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 15_DevOps_and_CI_CD

Source: [lists/frontend/15_DevOps_and_CI_CD.md](../frontend/15_DevOps_and_CI_CD.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** pipeline definitions, IaC policy, build artifacts, and deploy smoke checks; include browser and client behavior where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Checkov](https://www.checkov.io/) + [Trivy](https://trivy.dev/latest/).
- **Python:** [pytest-testinfra](https://testinfra.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 16_Reliability_and_DisasterRecovery

Source: [lists/frontend/16_Reliability_and_DisasterRecovery.md](../frontend/16_Reliability_and_DisasterRecovery.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** network/service failure injection, retries, restore, and recovery objectives; include browser and client behavior where applicable.
- **Cross-stack:** [Toxiproxy](https://github.com/Shopify/toxiproxy) + [k6](https://grafana.com/docs/k6/latest/).
- **Python:** [testcontainers-python](https://testcontainers-python.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 17_Monitoring_and_Observability

Source: [lists/frontend/17_Monitoring_and_Observability.md](../frontend/17_Monitoring_and_Observability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** trace propagation, metrics/logs, alert conditions, and SLO visibility; include browser and client behavior where applicable.
- **Cross-stack:** [Prometheus promtool](https://prometheus.io/docs/prometheus/latest/command-line/promtool/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [OpenTelemetry](https://opentelemetry.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 18_Analytics_and_ProductMetrics

Source: [lists/frontend/18_Analytics_and_ProductMetrics.md](../frontend/18_Analytics_and_ProductMetrics.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** event naming, consent, schemas, experiments, and reporting integrity; include browser and client behavior where applicable.
- **Cross-stack:** [GA4 DebugView](https://support.google.com/analytics/answer/7201382).
- **Optional first-party/self-hosted analytics implementations:** [Umami](https://github.com/umami-software/umami) and [Plausible Community Edition](https://github.com/plausible/community-edition) may suit basic web/product measurement. Verify actual tracker payloads, identity and storage behavior, consent/lawful basis for each deployment and jurisdiction, retention, performance impact, access control, updates, backups, container/database security and hosting costs; "privacy-first" or "cookie-free" does not automatically exempt a deployment from privacy obligations. Confirm CE versus paid-cloud feature differences before selection.
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 19_Cost_and_FinOps

Source: [lists/frontend/19_Cost_and_FinOps.md](../frontend/19_Cost_and_FinOps.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** usage tagging, budget alerts, cost estimates, and anomaly scenarios; include browser and client behavior where applicable.
- **Cross-stack:** [Infracost](https://www.infracost.io/docs/).
- **Python:** [Cloud Custodian](https://cloudcustodian.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 20_Release_and_LaunchReadiness

Source: [lists/frontend/20_Release_and_LaunchReadiness.md](../frontend/20_Release_and_LaunchReadiness.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** release smoke suites, security gates, rollback, and post-deploy verification; include browser and client behavior where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Trivy](https://trivy.dev/latest/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Launch handover and delivery verification:** [Playwright](https://playwright.dev/) or a similar browser runner can test safe contact-form submissions, while manual review verifies final copy, receiving mailboxes, client handover artifacts, and staffed response windows.
- **Website launch checks:** [axe-core](https://github.com/dequelabs/axe-core), [Accessibility Insights](https://accessibilityinsights.io/), [BrowserStack](https://www.browserstack.com/), [metatags.io](https://metatags.io/), and [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) may supplement actual production tests; use manual keyboard, screen-reader, and receiving-mailbox verification where applicable.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.
