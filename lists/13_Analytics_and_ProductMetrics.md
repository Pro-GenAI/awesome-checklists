# 13 — Analytics and Product Metrics Checklist

> Verify that product metrics answer meaningful decisions and are built on well-defined events, trustworthy data, privacy-aware collection, and sound experimentation. This template does not certify that a particular analytics vendor's reports or causal claims are correct.

> **Scope: Shared / cross-cutting.** This file is one part of the 13_Analytics_and_ProductMetrics.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Measurement strategy and metric definitions


- [ ] **ANL-001** `P2` Identify primary product goals and the user behaviors that demonstrate progress toward each goal.
- [ ] **ANL-002** `P2` Define a concise North Star or comparable primary outcome metric only where it meaningfully reflects customer value.
- [ ] **ANL-003** `P2` Assign an accountable business owner and a technical measurement owner to every critical product metric.
- [ ] **ANL-004** `P1` Write a metric dictionary with numerator, denominator, eligible population, time window, units, data source, and calculation logic.
- [ ] **ANL-005** `P2` Specify how active users, sessions, new users, conversions, orders, and retained users are defined before comparing reports.
- [ ] **ANL-006** `P2` Document user and account identity semantics, anonymous identifiers, and the rules for connecting sessions across devices when allowed.
- [ ] **ANL-007** `P1` Distinguish user-level, account-level, session-level, event-level, and transaction-level metrics to avoid denominator mistakes.
- [ ] **ANL-009** `P2` Define acquisition, activation, engagement, retention, monetization, and referral metrics only when relevant to the product.
- [ ] **ANL-010** `P2` Record baselines, expected ranges, targets, measurement frequency, and owners for important outcomes.
- [ ] **ANL-011** `P1` Establish the cohort entry event, eligibility window, observation period, and retention calculation for cohort analyses.
- [ ] **ANL-012** `P2` Document what counts as successful task completion and how abandoned, retried, failed, and partial transactions are treated.
- [ ] **ANL-013** `P2` Define attribution windows and rules for organic, paid, referral, direct, and unknown acquisition sources when relevant.
- [ ] **ANL-014** `P2` Identify limitations introduced by consent, blockers, offline use, cross-device identity, and missing events before making comparisons.
- [ ] **ANL-015** `P1` Ensure monetary metrics distinguish gross/net amounts, refunds, currencies, taxes, discounts, and exchange-rate conversions where applicable.
- [ ] **ANL-016** `P2` Define whether metrics are observed, sampled, modeled, estimated, or derived and label dashboards accordingly.
- [ ] **ANL-017** `P1` Plan segmentation by platform, cohort, geography, customer tier, and accessibility-relevant user experience where justified and lawful.
- [ ] **ANL-018** `P1` Check that dashboards distinguish operational health metrics from user or business outcome metrics.
- [ ] **ANL-019** `P2` Record known risks of survivorship bias, selection bias, changing populations, and seasonality for major analyses.
- [ ] **ANL-020** `P1` Review the metric definitions with product, engineering, analytics, privacy, and finance owners as applicable.
- [ ] **ANL-021** `P2` Define escalation and correction procedures when a key metric's business meaning or computation changes.
- [ ] **ANL-022** `P1` Use a decision log tying metric movements and experiments to actual product or investment decisions.

## Event taxonomy and implementation


- [ ] **ANL-023** `P2` Maintain an approved tracking plan mapping each important user journey and business question to the events needed to answer it.
- [ ] **ANL-024** `P2` Define event names, descriptions, trigger conditions, owner, platform, and implementation source before instrumenting them.
- [ ] **ANL-025** `P1` Use consistent event naming and case conventions, avoiding reserved names and vendor-specific limits when a chosen tool has them.
- [ ] **ANL-026** `P2` Document event parameters with types, units, allowed values, nullability, and examples.
- [ ] **ANL-028** `P2` Identify authoritative events for high-impact transactions rather than counting unverified button clicks as completed purchases.
- [ ] **ANL-029** `P1` Distinguish auto-collected, recommended, and custom events in a vendor implementation and avoid unintentional duplication.
- [ ] **ANL-031** `P1` Verify one logical user action does not create multiple identical conversion events unless multiple outcomes are intended.
- [ ] **ANL-032** `P1` Decide how event timestamps, ingestion timestamps, time zones, and late-arriving events are represented.
- [ ] **ANL-033** `P2` Define the lifecycle of anonymous, authenticated, and account identities, including logout and account switching.
- [ ] **ANL-034** `P1` Use stable event or transaction identifiers for deduplication and reconciliation where appropriate.
- [ ] **ANL-035** `P1` Capture campaign/referrer attribution fields consistently without including secrets or personal query parameters.
- [ ] **ANL-036** `P2` Document what happens when users decline measurement, disable storage, or revoke consent in applicable products.
- [ ] **ANL-037** `P1` Include source app/platform, environment, and release version so data from tests and production can be separated.

- [ ] **ANL-043** `P1` Review event instrumentation for performance overhead and avoid blocking critical user interactions on analytics delivery.
- [ ] **ANL-044** `P1` Treat the tracking plan as a maintained contract, updating it in the same release workflow as affected product behavior.

## Data quality and reporting


- [ ] **ANL-045** `P1` Reconcile critical conversions and financial totals against a trusted transactional system rather than assuming analytics collection is complete.

- [ ] **ANL-049** `P2` Document the treatment of bots, internal testers, QA traffic, employee accounts, and automated probes in reporting.
- [ ] **ANL-050** `P1` Verify users, sessions, and conversion deduplication rules against representative edge cases.
- [ ] **ANL-051** `P1` Test metric calculations against small hand-verified examples, including dates, partial periods, and timezone boundaries.
- [ ] **ANL-052** `P1` Check that revenue and currency conversion calculations use documented rounding and exchange-rate rules.
- [ ] **ANL-053** `P2` Document report sampling, thresholding, modeling, export limits, and attribution differences of the selected analytics provider.
- [ ] **ANL-054** `P1` Verify raw-data export frequency and completeness meet dashboard expectations; do not assume streaming exports contain finalized attribution.
- [ ] **ANL-055** `P2` Define whether late and corrected events trigger recomputation, backfill, or permanent historical limitations.
- [ ] **ANL-056** `P1` Audit join keys and identity stitching to prevent multiplying events through many-to-many warehouse joins.
- [ ] **ANL-057** `P1` Use consistent cohort, date, audience, environment, and currency filters in comparisons that are meant to reconcile.
- [ ] **ANL-058** `P1` Verify tracking between consented and non-consented users is handled legally and that any resulting measurement gaps are disclosed.
- [ ] **ANL-059** `P1` Use appropriate row-level controls or aggregation for sensitive reporting dimensions, especially low-count cohorts.
- [ ] **ANL-060** `P2` Document the canonical dashboard or semantic model for each metric to reduce conflicting versions of the truth.
- [ ] **ANL-061** `P1` Include units, owner, source, last refresh, applied filters, and confidence or caveat annotations on important dashboards.
- [ ] **ANL-062** `P1` Restrict edit and publish rights for production dashboards, metric definitions, and business-critical transformations.
- [ ] **ANL-063** `P1` Provide a process for responding to metric anomalies and retroactive corrections, including downstream communication.

- [ ] **ANL-066** `P2` Record the known reporting gaps, unsupported segments, and historical discontinuities that affect business decisions.

## Privacy, consent, and data lifecycle


- [ ] **ANL-068** `P2` Document why each collected field is necessary and remove unnecessary or disproportionately sensitive attributes.
- [ ] **ANL-069** `P1` Determine applicable consent, lawful-basis, transparency, and tracking-technology rules with qualified privacy reviewers.
- [ ] **ANL-070** `P1` Ensure storage/access technologies follow the applicable rules before non-essential collection or access begins.
- [ ] **ANL-071** `P1` Verify analytics and advertising purposes are not silently bundled when the applicable consent framework requires separate choices.
- [ ] **ANL-073** `P1` Check analytics collection after logout, account switching, and consent withdrawal for unintended identifiers or linkage.
- [ ] **ANL-074** `P1` Prevent passwords, authentication tokens, payment details, health information, and other prohibited sensitive values from appearing in analytics payloads.
- [ ] **ANL-075** `P1` Review URL, referrer, search-query, form, and error-message fields for accidental personal-data collection.
- [ ] **ANL-076** `P1` Use appropriately scoped pseudonymous identifiers and documented reidentification controls where tracking is justified.
- [ ] **ANL-077** `P1` Restrict access to user-level event data, exports, dashboards, and third-party accounts by role and actual business need.
- [ ] **ANL-078** `P1` Apply documented retention periods and deletion rules to event stores, identity maps, exports, and derived tables as required.
- [ ] **ANL-079** `P2` Define how correction, access, and erasure requests affect analytics identifiers and derived records when applicable.
- [ ] **ANL-080** `P1` Review cross-border transfers and external processor arrangements where the applicable legal framework requires it.
- [ ] **ANL-081** `P1` Assess whether consent gaps, privacy filters, and signal loss make certain cohorts unrepresentative.
- [ ] **ANL-082** `P1` Validate that debug instrumentation and staging environments do not send real user data into inappropriate production analytics properties.
- [ ] **ANL-083** `P2` Document data-subject or customer inquiries and who responds to analytics-related privacy requests.
- [ ] **ANL-084** `P1` Reassess the privacy impact when adding advertising identifiers, cross-device tracking, new third parties, or sensitive segments.
- [ ] **ANL-085** `P1` Keep public notices and internal data maps aligned with the actual tools, data fields, and processing purposes.

## Experimentation and decision quality


- [ ] **ANL-086** `P1` State an experiment hypothesis and the intended user or business behavior change before allocating users.
- [ ] **ANL-088** `P2` Define randomization unit, audience eligibility, targeting, allocation, and assignment persistence.
- [ ] **ANL-090** `P1` Choose a control group or suitable counterfactual rather than treating before/after movement as automatic proof of causality.
- [ ] **ANL-091** `P1` Confirm exposure events are emitted for the intended population and linked to metric events through the correct identity key.
- [ ] **ANL-092** `P1` Monitor sample-ratio mismatch and investigate persistent imbalance before trusting experiment comparisons.
- [ ] **ANL-093** `P1` Check crossover, unexpected reassignments, missing exposures, and unequal event loss across variants.
- [ ] **ANL-094** `P2` Define an analysis window and rules for multiple comparisons, repeated looks, and early stopping appropriate to the methodology.
- [ ] **ANL-095** `P1` Distinguish statistical uncertainty from practical significance and report effect sizes with uncertainty estimates when supported.
- [ ] **ANL-096** `P1` Monitor reliability, accessibility, user-harm, privacy, and business guardrails during experiment rollout.
- [ ] **ANL-097** `P2` Specify when an experiment must be paused because of safety, severe regressions, or data-quality failures.
- [ ] **ANL-098** `P2` Document platform, device, cohort, and geographic segments selected in advance to avoid overinterpreting post hoc subgroups.
- [ ] **ANL-101** `P2` Record experiment conclusions, metric caveats, decision owners, and whether a result justified launch, iteration, or abandonment.
- [ ] **ANL-102** `P1` Do not present observational correlations, dashboard fluctuations, or statistically invalid experiments as causal evidence.
- [ ] **ANL-103** `P1` Retain the analysis specification and relevant variant/version details to make major decisions reproducible.
- [ ] **ANL-104** `P1` Reassess experiments when tracking implementations, audience eligibility, or key metric definitions change during the test.

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

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#13_analytics_and_productmetrics), not prerequisites or verification evidence.

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
