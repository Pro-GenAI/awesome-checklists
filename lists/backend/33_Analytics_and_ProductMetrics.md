# 33 — Analytics and Product Metrics Checklist

> Verify that product metrics answer meaningful decisions and are built on well-defined events, trustworthy data, privacy-aware collection, and sound experimentation. This template does not certify that a particular analytics vendor's reports or causal claims are correct.

> **Scope: Backend / API-specific.** This file is one part of the 33_Analytics_and_ProductMetrics.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Event taxonomy and implementation


- [ ] **ANL-027** `P1` Separate an attempted action from a successful server-confirmed outcome so conversion metrics do not count failed attempts.
- [ ] **ANL-040** `P1` Test client and server event paths for offline use, delayed uploads, process restarts, and transient network failures.
- [ ] **ANL-038** `P1` Add event-schema and required-parameter checks to automated tests or controlled staging validation where feasible.
- [ ] **ANL-041** `P1` Monitor event ingestion, schema violations, duplicates, missing fields, and unexpected changes in volume after releases.
- [ ] **ANL-042** `P1` Version significant event schema changes and coordinate downstream dashboards, warehouses, and consumer migrations.

## Data quality and reporting


- [ ] **ANL-046** `P1` Compare client and server event counts for key journeys and investigate significant discrepancies.
- [ ] **ANL-065** `P1` Verify cost, cardinality, storage, and retention characteristics of analytics ingestion and reporting infrastructure.
- [ ] **ANL-047** `P1` Monitor source collection, ingestion, transformation, and dashboard freshness with documented acceptable delays.
- [ ] **ANL-048** `P1` Detect data gaps, schema drift, unexpected nulls, duplicate event IDs, and anomalous traffic before publishing key metrics.
- [ ] **ANL-064** `P1` Create regression tests for key transformations, aggregates, and conversion funnels affected by code or schema changes.

## Privacy, consent, and data lifecycle


- [ ] **ANL-067** `P2` Inventory each analytics collector, SDK, pixel, cookie, server-side destination, and downstream data recipient.
- [ ] **ANL-072** `P1` Confirm declines, withdrawals, and preference changes propagate to applicable tags, SDKs, server-side collectors, and destinations.

## Experimentation and decision quality


- [ ] **ANL-089** `P1` Determine sample-size and runtime assumptions before launch, including the minimum detectable effect where applicable.
- [ ] **ANL-099** `P1` Check for novelty effects, seasonality, network effects, or interference between users when they could bias interpretation.
- [ ] **ANL-100** `P1` Review contradictory signals between the primary metric and guardrails before recommending deployment.

## API Checks


- [ ] **ANL-105** `P2` Define which business events must be emitted by authoritative server-side API operations rather than browser-only interactions.
- [ ] **ANL-106** `P1` Include stable event or transaction identifiers for deduplication of API analytics events where needed.
- [ ] **ANL-107** `P1` Emit completed transaction events only after the relevant durable business operation succeeds.
- [ ] **ANL-108** `P1` Ensure retries, timeouts, and idempotent API writes cannot accidentally inflate order, signup, or conversion totals.
- [ ] **ANL-109** `P2` Document how API failures, canceled operations, and partial outcomes differ from successful conversions.
- [ ] **ANL-110** `P1` Use consistent user/account identifiers and consent flags across server and client analytics within authorized bounds.
- [ ] **ANL-111** `P1` Validate analytics event schemas, required fields, and permitted values before dispatch to external collectors.
- [ ] **ANL-112** `P1` Keep analytics API secrets and provider credentials on trusted server infrastructure rather than in client code.
- [ ] **ANL-113** `P1` Set limits, retry budgets, and backpressure for telemetry dispatch so analytics failures cannot exhaust primary API capacity.
- [ ] **ANL-114** `P1` Do not block or roll back customer-critical API operations solely because an optional analytics sink is unavailable.
- [ ] **ANL-115** `P2` Define event delivery guarantees, deduplication, replay, and late-arrival behavior for asynchronous collection where used.
- [ ] **ANL-116** `P1` Propagate relevant deployment version, environment, and correlation metadata without attaching sensitive request bodies.
- [ ] **ANL-117** `P1` Confirm server-side events respect applicable consent or collection restrictions rather than assuming server origin removes those duties.
- [ ] **ANL-118** `P1` Test measurement endpoints, payload limits, and validation rules against the selected analytics vendor where applicable.
- [ ] **ANL-119** `P1` Monitor ingestion failure, rejection, sampling, queue lag, and invalid-event rates for critical API-origin events.
- [ ] **ANL-120** `P1` Reconcile important server-emitted metrics with source-of-truth database transactions and finance records.
- [ ] **ANL-121** `P1` Check that analytics exports, enrichment, and external destinations enforce appropriate access and data-retention boundaries.
- [ ] **ANL-122** `P2` Document API version changes that alter event names or business semantics and notify downstream metric owners.
- [ ] **ANL-123** `P1` Keep event timestamps, transaction ordering, and timezone conversions consistent across distributed API services.

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

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#33_analytics_and_productmetrics), not prerequisites or verification evidence.

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
