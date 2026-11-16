# 20 — Analytics and Product Metrics Checklist

> Verify that product metrics answer meaningful decisions and are built on well-defined events, trustworthy data, privacy-aware collection, and sound experimentation. This template does not certify that a particular analytics vendor's reports or causal claims are correct.

> **Scope: AI-specific.** This file is one part of the 20_Analytics_and_ProductMetrics.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Measurement strategy and metric definitions

- [ ] **ANL-008** `P1` Choose meaningful leading, lagging, and guardrail indicators instead of relying on a single aggregate KPI.

## Experimentation and decision quality

- [ ] **ANL-087** `P1` Choose a primary outcome metric and a limited set of guardrail metrics before observing results.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#20_analytics_and_productmetrics), not prerequisites or evidence of PASS.

## Trusted references and scope

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

**Source review date:** 2026-11-12.
