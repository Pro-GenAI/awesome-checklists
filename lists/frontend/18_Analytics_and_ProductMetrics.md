# 18 — Analytics and Product Metrics Checklist

> Verify that product metrics answer meaningful decisions and are built on well-defined events, trustworthy data, privacy-aware collection, and sound experimentation. This template does not certify that a particular analytics vendor's reports or causal claims are correct.

> **Scope: Frontend-specific.** This file is one part of the 18_Analytics_and_ProductMetrics.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Event taxonomy and implementation

- [ ] **ANL-030** `P2` Define when events fire across load, route changes, modal interactions, retries, and background processing.
- [ ] **ANL-039** `P1` Validate important browser and app events through actual task flows and the chosen platform's debug tools.

## Frontend Checks

- [ ] **ANL-124** `P2` Define event triggers for critical page views, route transitions, signups, checkout steps, and task-completion states.
- [ ] **ANL-125** `P1` Ensure single-page applications emit intended screen or page events on navigation without duplicate initial-load events.
- [ ] **ANL-126** `P1` Verify primary conversion events reflect confirmed outcomes rather than mere clicks or premature optimism.
- [ ] **ANL-127** `P1` Test form errors, cancellation, abandonment, retries, and successful submission as distinct analytics outcomes.
- [ ] **ANL-128** `P1` Ensure consent preferences are applied before activating optional tags, storage, or advertising measurement where legally required.
- [ ] **ANL-129** `P1` Validate withdrawal and changes of consent in live browser sessions without relying on a page refresh.
- [ ] **ANL-130** `P1` Prevent analytics SDKs from capturing passwords, form contents, query secrets, or personally identifying values in URLs.
- [ ] **ANL-146** `P1` Where session replay, heatmaps, or behavioral-recording SDKs are enabled, verify privacy configuration and required consent, mask sensitive inputs and page content before transmission, and inspect actual recordings/network payloads and exports for unintended capture.
- [ ] **ANL-131** `P1` Keep user and anonymous identities appropriately separated on login, logout, and account switching.
- [ ] **ANL-132** `P1` Verify events across browser back/forward navigation, client-side routing, page refresh, and interrupted flows.
- [ ] **ANL-133** `P1` Test capture when scripts are blocked, the device is offline, or the browser is closed and document expected measurement loss.
- [ ] **ANL-134** `P1` Prevent duplicate events caused by rerenders, repeated effects, double clicks, or multiple tag-manager containers.
- [ ] **ANL-135** `P1` Verify event parameter types and values under localized date, number, currency, and text formats.
- [ ] **ANL-136** `P2` Record applicable device, route, campaign, and feature-flag dimensions without introducing unauthorized sensitive attributes.
- [ ] **ANL-137** `P1` Keep analytics network calls from delaying primary content, form submission, navigation, or accessible interactions.
- [ ] **ANL-138** `P1` Test real-user instrumentation overhead and avoid unnecessary third-party scripts on critical interaction paths.
- [ ] **ANL-139** `P1` Separate testing, preview, staging, and production measurement properties or label datasets reliably.
- [ ] **ANL-140** `P1` Use a vendor debug view or approved network inspection to verify event names and payloads on key journeys.
- [ ] **ANL-141** `P1` Test cross-browser and mobile behaviors, including privacy protections that may change identifier persistence.
- [ ] **ANL-142** `P1` Confirm users can understand and change their tracking preferences through the product's approved interface.
- [ ] **ANL-143** `P1` Check that dashboards and funnels reflect the expected client behavior after release-specific flag, routing, or UI changes.
- [ ] **ANL-144** `P1` Ensure analytics error handling does not leak tokens or sensitive event payloads to browser console logs.
- [ ] **ANL-145** `P1` Verify that dynamic dialogs, accessibility alternatives, and keyboard-triggered actions produce consistent measurement with pointer interactions.

## Release gate

- [ ] Launch-critical business and user outcome metrics have stable definitions, owners, targets or baselines, and documented measurement limitations.
- [ ] Critical events have an approved tracking plan, unique trigger semantics, appropriate identity and attribution rules, and validated representative client/server payloads.
- [ ] Key conversion, transactional, or financial metrics reconcile with the authoritative system to an agreed tolerance, or material gaps have an accepted remediation plan.
- [ ] Applicable consent, notices, data minimization, privacy controls, recipient access, and retention requirements have been reviewed and approved by the appropriate owner.
- [ ] Analytics ingestion and dashboards are checked for freshness, missing events, duplicates, inappropriate test traffic, and known export or modeling limits.
- [ ] Any launch-critical experiment has a documented hypothesis, decision metrics, randomization/health checks, and approved stop or rollout rules.
- [ ] Responsible API/frontend owners confirm that relevant user journeys are measured correctly without disrupting functionality or collecting prohibited sensitive data.
- [ ] Unresolved defects that could materially mislead product decisions, harm users, or breach applicable data-processing requirements have an owner, escalation path, and explicit authorized disposition.

**Domain-specific approval rule:** Do not approve measurement as release-ready when critical decisions depend on undefined or demonstrably incorrect metrics, required consent/collection rules are unaddressed, server-side business events systematically double count, or invalid experiment allocation is used to claim causality. Analytics review is not a substitute for legal/privacy compliance review or independent financial audit.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#18_analytics_and_productmetrics), not prerequisites or verification evidence.

## Trusted references and scope

- [Microsoft Clarity — Masking content](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking) — practical vendor example of recording redaction.

These checks translate source guidance into testable measurement and decision controls. Vendor-specific technical details apply only when that platform is used; these references are not a universal compliance standard.

- [Google Analytics — Set up events](https://developers.google.com/analytics/devguides/collection/ga4/events) — user interaction event design, collection, and verification.
- [Google Analytics — Recommended events](https://support.google.com/analytics/answer/9267735) — established event semantics and prescribed parameters for applicable use cases.
- [Google Analytics — Event naming rules](https://support.google.com/analytics/answer/13316687) — naming restrictions, case sensitivity, and reserved names for GA4.
- [Google Analytics — Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4) — server-side/offline events and their intended supplementary use.
- [Google Analytics — Validate Measurement Protocol events](https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events) — payload validation and the difference between transport success and accepted events.
- [Google Analytics — BigQuery Export](https://support.google.com/analytics/answer/9358801) — export timeliness, completeness, attribution limitations, and sampling differences.
- [Google Tag Platform — Consent mode on websites](https://developers.google.com/tag-platform/security/guides/consent) — technically honoring recorded consent choices for Google tags, where used.
- [UK ICO — Final storage and access technologies guidance announcement (2026)](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/04/final-storage-and-access-technologies-guidance-published/) — current UK regulatory context for cookies and analogous tracking technologies where applicable.
- [Microsoft PlayFab — Experiment best practices](https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/game-configuration/experiments/experimentation-keys) — experiment health, sample-ratio mismatch, and unbiased interpretation.
- [Statsig — Experiment health monitoring](https://docs.statsig.com/experiments/monitor) — exposure consistency, sample ratio, and guardrail checks in experiments.
- [Statsig — Experiment decision framework](https://docs.statsig.com/experiments/templates/decision-framework) — predefined primary and guardrail metrics, decisions, and reviews.
- [Statsig — Experiment overview](https://docs.statsig.com/experiments/overview) — randomization and causal inference principles for controlled experiments.

**Applicability:** GA4 event names, API payload limits, and BigQuery export semantics are relevant only to GA4 implementations. UK tracking obligations depend on applicable law and current regulatory guidance, including changes made in 2026; seek qualified legal advice for jurisdiction-specific decisions. Online controlled experiments should be used only when methodologically appropriate. Consent-driven gaps, identity uncertainty, ad blockers, and sampling can affect measurement completeness and must not be ignored.

**Source review date:** 2026-11-13.
