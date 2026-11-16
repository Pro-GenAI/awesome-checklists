# 20 — Release and Launch Readiness Checklist

> Verify that a new product, service, or significant change is ready for controlled customer exposure, has an explicit go/no-go decision, and can be operated and supported safely after launch. This release-level checklist consolidates sign-offs from deeper reviews rather than duplicating all of their technical tests.

> **Scope: Frontend-specific.** This file is one part of the 20_Release_and_LaunchReadiness.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Post-launch verification

- [ ] **LAUNCH-070** `P1` Review browser or client-side crashes, failed navigation, page performance, and user-visible errors for targeted cohorts.

## Frontend Checks

- [ ] **LAUNCH-103** `P1` Verify public URLs, app entry points, deep links, navigation, and refresh behavior on the production domain.
- [ ] **LAUNCH-104** `P1` Check production HTML, JavaScript, CSS, images, fonts, and asset manifests load consistently without incompatible cached versions.
- [ ] **LAUNCH-105** `P1` Confirm CDN policies and release invalidation allow users to retrieve the correct application assets after rollout and rollback.
- [ ] **LAUNCH-106** `P1` Validate service-worker update, offline-cache, and installed-app behavior where the product uses these features.
- [ ] **LAUNCH-107** `P1` Verify runtime configuration points to intended production APIs and that no private credentials are embedded in client bundles.
- [ ] **LAUNCH-108** `P1` Run essential workflows on representative supported browsers, devices, viewport sizes, and network conditions.
- [ ] **LAUNCH-109** `P1` Check first-time visits, returning sessions, expired sessions, and account switching for coherent login and state recovery.
- [ ] **LAUNCH-110** `P1` Verify forms, payments, subscriptions, downloads, and other high-impact tasks display correct completion or failure feedback.
- [ ] **LAUNCH-111** `P1` Confirm staged feature flags and user-entitlement rules expose features only to the intended release cohort.
- [ ] **LAUNCH-112** `P1` Review production error boundaries, loading states, and unavailable-service messages for meaningful recovery paths.
- [ ] **LAUNCH-113** `P1` Verify client performance and key page templates against the launch's agreed real-user and laboratory budgets.
- [ ] **LAUNCH-114** `P1` Check that analytics, consent notices, and conversion tracking work without leaking sensitive user data.
- [ ] **LAUNCH-115** `P1` Validate accessibility of critical interactions, including keyboard navigation, focus, form errors, and dynamic status updates.
- [ ] **LAUNCH-116** `P1` Confirm supported languages, currency and date formatting, right-to-left handling, and localized content where applicable.
- [ ] **LAUNCH-117** `P1` Verify production-specific page metadata, canonical URLs, indexing rules, and redirects for externally discoverable sites.
- [ ] **LAUNCH-118** `P1` Check browser error reporting, client-side crash monitoring, and deployed build version tagging after exposure.
- [ ] **LAUNCH-119** `P1` Verify customer-facing release notes, help links, pricing information, and legal notices reflect the released functionality.
- [ ] **LAUNCH-120** `P1` Confirm mobile app store listing, package signing, staged distribution, and rollback limitations when releasing native clients.
- [ ] **LAUNCH-121** `P1` Test concurrent old/new client versions against active API contracts until safe update propagation is expected.
- [ ] **LAUNCH-122** `P1` Ensure that rollback or feature-disablement does not strand users in unfinished transactions or inaccessible flows.

- [ ] **LAUNCH-123** `P1` For native app-store submissions with authenticated, restricted, regional, or paid features, verify reviewers have working, appropriately scoped demo access, relevant test data, and instructions to exercise every review-critical flow.
- [ ] **LAUNCH-124** `P1` For applicable Apple-platform distributions, reconcile the app and included third-party SDK privacy manifests, required-reason API declarations, SDK signatures, and store privacy disclosures against the exact release dependencies and observed data flows.
- [ ] **LAUNCH-132** `P1` For Google Play releases, reconcile the published Data safety declarations and linked privacy policy with the actual app, embedded webviews, requested permissions, and third-party SDK data collection/sharing for the submitted build; verify updates after relevant changes.
- [ ] **LAUNCH-125** `P1` For native releases, generate, retain, and deliver matching crash-symbol or deobfuscation artifacts (such as dSYM, Android native symbols, or mapping files) and confirm a sample release crash report can be decoded.

- [ ] **LAUNCH-126** `P1` Before public website launch, inspect representative production pages for unfinished placeholder text, sample accounts, test imagery, stale client branding, inaccurate contact details, and nonfinal policy/help links; obtain accountable editorial or client acceptance for important content.
- [ ] **LAUNCH-127** `P1` For production contact, lead-generation, support, or notification forms, submit safe end-to-end test messages and verify validation, user confirmation, anti-abuse behavior, delivery/routing to the correct monitored destination, and recoverability of failures without exposing private submissions.
- [ ] **LAUNCH-128** `P1` Where a project includes a client handover, reconcile the agreed deliverables with actual production access, maintained style/design guidelines, source assets and license rights, documentation, backups/export formats, and ongoing ownership of hosting, domains, analytics, and support.
- [ ] **LAUNCH-129** `P1` Schedule customer-facing launches according to actual staffing, support and incident-response coverage, vendor/change windows, and rollback readiness; explicitly document and approve exceptions instead of enforcing an arbitrary weekday-only rule.

- [ ] **LAUNCH-130** `P1` For public website launches with a staging or preview environment, verify non-public content is protected by access controls rather than relying on `robots.txt`, and confirm production versus staging robots/noindex rules, canonical URLs, and analytics identifiers are correct after deployment.
- [ ] **LAUNCH-131** `P1` Before public launch, inspect actual share previews and preview-image availability on important public entry pages, including social metadata, crop/safe-area readability and URL consistency, while avoiding publication of staging or confidential preview imagery.

## SEO + GEO launch quick pass

For publicly discoverable websites, use this **eight-point cross-reference** before launch. These refer to existing and new checklist IDs rather than duplicating criteria or inflating the checklist count. Record evidence in the linked source checklist, and mark out-of-scope items as not applicable.

1. **Domain and long-term continuity:** `SEO-081` — choose and control a domain if it fits the product's long-term needs; plan migrations and redirects.
2. **HTTPS and canonical pages:** `SEO-010`, `SEO-016`, `SEO-081` — validate HTTPS, preferred host, and one appropriate canonical URL per page.
3. **Sitemap and Search Console:** `SEO-009`, `SEO-029` — generate/verify `sitemap.xml`, verify property ownership, and submit relevant sitemaps.
4. **Appropriate crawler access:** `SEO-006`, `SEO-007`, `GEO-047`, `GEO-079` — verify Googlebot and explicitly targeted AI-search crawlers can access public pages; review training-bot policies separately.
5. **Crawlable primary text:** `SEO-013`, `SEO-061`, `GEO-019` — expose important text, headings, and links in usable rendered HTML.
6. **Metadata, identity and structured data:** `SEO-014`, `SEO-018`, `SEO-027`, `GEO-080` — use accurate titles, organization/author details and visible-content-matching structured data where appropriate.
7. **Original reference-worthy information:** `SEO-003`, `GEO-013` — publish useful original data, examples, or research with verifiable claims.
8. **Legitimate third-party references:** `SEO-082`, `GEO-017`, `GEO-030` — encourage relevant editorial references and maintain consistent public identity, without link schemes or guaranteed citations.

**Interpretation:** A `github.io` or `pages.dev` address is not inherently disqualified from search or AI answers; a controlled custom domain is primarily a portability/branding choice. `llms.txt` is optional for clients that consume it and **not a Google AI Search requirement**. There is no guaranteed inclusion, ranking, entity-match, or citation outcome.

## Release gate

- [ ] The release scope, exact artifact, target environment, deployment window, and accountable go/no-go owner are documented and agreed.
- [ ] Required technical, operational, security, privacy, accessibility, and business reviews are complete, with no unaccepted release-blocking findings.
- [ ] Production dependencies, migration prerequisites, secrets and access, capacity, monitoring, on-call coverage, and customer-support handoffs are ready for the intended launch.
- [ ] The rollout procedure has clear steps, audience/exposure controls, health thresholds, stop conditions, and safe recovery options, including treatment of irreversible changes.
- [ ] Critical API and frontend journeys are verified in production or an explicitly approved equivalent, with defined follow-up checks after live exposure.
- [ ] Stakeholder/customer communication plans, documentation, known limitations, and escalation channels are approved where applicable.
- [ ] A designated approver has recorded **Go**, **Go with authorized time-bound exceptions**, or **No-go** against the exact release and its residual risks.
- [ ] Post-launch observation, stabilization ownership, completion criteria, and remediation tracking are agreed before the release is declared finished.

**Domain-specific approval rule:** Block launch when essential user journeys are unverified, required sign-offs are missing, critical dependencies or support coverage are unready, the actual deployed artifact is unknown, or material deployment/recovery risks are unaccepted. A launch approval does not supersede legally required approvals or prove that all risks have been eliminated.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#20_release_and_launchreadiness), not prerequisites or verification evidence.

## Trusted references and scope

- [Google Play Console — Data safety requirements](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) — app/SDK declarations.

The following primary sources informed these practical verification questions. Their detailed methods are adaptable rather than mandatory for every organization, and the links are not a claim of any formal launch certification.

- [Google SRE — Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/) — launch checklists, dependency review, capacity, operations, and coordinated readiness.
- [Google SRE — Launch Coordination Checklist](https://sre.google/sre-book/launch-checklist/) — release-day architecture, load, dependencies, reliability, and verification questions.
- [AWS Well-Architected — Operational readiness and change management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-readiness.html) — consistent prelaunch reviews, personnel, runbooks, change decisions, and support planning.
- [AWS Well-Architected — Operational Readiness Reviews](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-tool.html) — tailored readiness checklists, escalation, event handling, and release quality.
- [AWS Well-Architected — Plan for unsuccessful changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_plan_for_unsucessful_changes.html) — recovery, rollback, feature-disablement, and response to failed releases.
- [AWS Well-Architected — Mitigate deployment risks](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/mitigate-deployment-risks.html) — deployment testing, phased exposure, feedback, and rollback.
- [Microsoft Azure Well-Architected — Operational Excellence checklist](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist) — ownership, operations, monitoring, incident response, and safe deployment criteria.
- [Microsoft Azure Well-Architected — Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) — progressive exposure, health gates, emergency changes, and rollback planning.
- [Google Cloud — Operational readiness and performance](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops) — readiness across workforce, processes, tools, governance, and service support.
- [GitHub Docs — Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — protected deployment environments and approval mechanisms, when GitHub Actions is used.
- [OpenAPI Specification](https://spec.openapis.org/oas/v3.2.1.html) — versioned API contracts and interface documentation, when applicable.
- [Chrome for Developers — Service worker deployment](https://developer.chrome.com/docs/workbox/service-worker-deployment) — caching and compatibility considerations for service-worker-enabled web apps.

**Applicability:** The depth of review, number of approvals, exposure strategy, and stabilization period depend on customer impact, release type, team size, and applicable obligations. GitHub Actions protections and Workbox service-worker guidance are relevant only when those technologies are used. Reassess the launch plan after any substantial change to the candidate or target environment.

- [Apple Developer — App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — reviewer access, demo accounts, and complete store submissions.
- [Apple Developer — Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/) — privacy manifests and SDK signatures.
- [Apple Developer — Building your app to include debugging information](https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information) — diagnostic symbols and matching archives.
- [Android Developers — Include native symbols in your release build](https://developer.android.com/build/include-native-symbols) — native crash-symbol upload.

- [Tuts+ — Website Launch Checklist for Web Designers](https://github.com/tutsplus/Website-Launch-Checklist-for-Web-Designers/blob/master/launch_checklist.md) — historic launch editorial, delivery, handoff and support practices, reviewed for current applicability.
- [Google SRE — Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/) — coordinated launch support and operational readiness.

- [Google Search Central — Block search indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing) — noindex semantics; do not use robots directives as confidentiality controls.
- [DataMade — Site Launch Checklist](https://github.com/datamade/site-launch-checklist/blob/master/README.md) — web launch, staging, metadata, accessibility, monitoring, device testing, and site-sharing workflow.
- [Open Graph Protocol](https://ogp.me/) — website sharing metadata and images.

**Source review date:** 2026-11-13.
