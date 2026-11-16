# 19 — Cost and FinOps Checklist

> Verify that technology spending is attributable, visible, forecastable, and optimized for business value without compromising required quality, reliability, security, or user outcomes. FinOps is a shared product, engineering, finance, and procurement practice—not simply a directive to minimize the cloud bill.

> **Scope: Frontend-specific.** This file is one part of the 19_Cost_and_FinOps.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **COST-107** `P1` Measure transferred asset bytes and request counts for key frontend routes and representative devices.
- [ ] **COST-108** `P2` Identify oversized images, video, fonts, JavaScript bundles, and third-party assets that increase CDN or transfer costs.
- [ ] **COST-109** `P1` Use compression, responsive images, code splitting, and caching where they reduce cost without harming user experience.
- [ ] **COST-110** `P2` Define cache-control and asset versioning rules that prevent excessive refetching while avoiding stale or private responses.
- [ ] **COST-111** `P1` Check CDN cache-hit trends, geographic delivery, and origin egress for major pages and media.
- [ ] **COST-112** `P1` Avoid unnecessary client polling, repeated API calls, and refetch loops on common interactions.
- [ ] **COST-113** `P1` Cancel obsolete requests and de-duplicate concurrent fetches so navigation does not create avoidable billable work.
- [ ] **COST-114** `P1` Ensure retry logic has bounds and backoff so network disruptions do not produce repeated API or serverless charges.
- [ ] **COST-115** `P1` Review prefetching and preloading strategies so speculative downloads are proportionate to realized user value.
- [ ] **COST-116** `P1` Test service workers and offline caches for runaway retries, unintended repeated downloads, and incompatible asset versions where used.
- [ ] **COST-117** `P1` Measure third-party analytics, ads, maps, video, and chat widgets for load, transfer, and per-use charges where relevant.
- [ ] **COST-118** `P1` Use lazy loading for noncritical assets and modules when appropriate without delaying above-the-fold essentials.
- [ ] **COST-119** `P1` Set limits and clear feedback for user-driven bulk exports, uploads, generated media, and other potentially costly actions.
- [ ] **COST-120** `P1` Explain material user-facing usage limits, quotas, or fees accurately before initiating a chargeable operation where applicable.
- [ ] **COST-121** `P1` Prevent accidental duplicate paid actions from double clicks, repeated submissions, or inconsistent optimistic state.
- [ ] **COST-122** `P1` Verify frontend feature flags and staged rollouts do not unintentionally enable expensive endpoints for unintended cohorts.
- [ ] **COST-123** `P1` Include appropriate client-side resource and API traffic metrics in release cost reviews without collecting prohibited user data.
- [ ] **COST-124** `P1` Ensure savings-focused changes preserve accessibility, responsive behavior, visual quality, and core task completion.
- [ ] **COST-125** `P1` Check that expired sessions, hidden tabs, and background pages do not continue costly polling indefinitely.
- [ ] **COST-126** `P1` Coordinate frontend caching changes with API rate-limit, billing, and version compatibility rules.

## Release gate

- [ ] The release has named product, engineering, and financial owners for its material technology costs, with an approved allocation approach for shared and direct costs.
- [ ] Budget, baseline, forecast, principal assumptions, and potential cost-impacting launch or growth scenarios are documented at an appropriate level of detail.
- [ ] Critical spending and usage reports reconcile to trusted provider or financial data within accepted tolerances, and material unallocated charges are explained or assigned for investigation.
- [ ] Budget threshold, unusual-spend, and quota alerts or equivalent guardrails have owners and a tested escalation route appropriate to release risk.
- [ ] Significant compute, storage, data-transfer, SaaS, API, and frontend cost drivers are reviewed for avoidable use without undermining performance, accessibility, security, or reliability commitments.
- [ ] Applicable API and frontend operations have controls against unbounded or duplicate billable actions, with appropriate behavior when quotas or limits are reached.
- [ ] Any material over-budget forecast, unaffordable unit economics, unapproved commitment, or other significant cost risk has an explicit authorized disposition and remediation owner.

**Domain-specific approval rule:** Block cost readiness approval if material spend is unowned and invisible, foreseeable high-impact cost exposure lacks acceptable bounds, or a required budget/contract approval is missing. Meeting a cost target does not justify bypassing legal, security, quality, accessibility, or reliability requirements.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#19_cost_and_finops), not prerequisites or verification evidence.

## Trusted references and scope

These review questions are informed by the following primary FinOps and architectural guidance. Source recommendations are not universal compliance obligations; adapt them to the workload and commercial model.

- [FinOps Foundation — FinOps Framework](https://www.finops.org/framework/) — cross-functional technology cost accountability, value, and operating model.
- [FinOps Foundation — Allocation](https://framework.finops.org/framework/capabilities/allocation/) — cost ownership, tagging and hierarchy, shared cost treatment, and allocation coverage.
- [FinOps Foundation — Anomaly Management](https://www.finops.org/framework/capabilities/anomaly-management/) — detection, routing, investigation, and resolution of unplanned spend.
- [FinOps Foundation — Forecasting](https://www.finops.org/framework/capabilities/forecasting/) — forecast models, business drivers, scenarios, and variance tracking.
- [FinOps Foundation — Unit Economics](https://www.finops.org/framework/capabilities/unit-economics/) — aligning technology unit costs to product/business outcomes.
- [FOCUS — FinOps Open Cost and Usage Specification 1.3](https://focus.finops.org/docs/specification/v1-3/) — standardized billing vocabulary and cost/usage data when compatible datasets are used.
- [FOCUS — Cost and Usage dataset](https://focus.finops.org/docs/specification/v1-3/datasets/cost-and-usage/) — distinct billed, effective, contracted, and list cost fields; billing period and metadata.
- [Microsoft Azure Well-Architected — Cost Optimization checklist](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/checklist) — financial responsibility, budgets, guardrails, unit cost, utilization, optimization, and trade-offs.
- [Microsoft Azure Well-Architected — Cost Optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/) — usage, rate, and continuous optimization principles.

**Applicability:** FOCUS 1.3 provides a published data specification, not an assertion that every provider export is FOCUS 1.3-compatible or that 1.3 is the newest version. Cloud-specific rate models and tagging practices do not apply unchanged to every SaaS, AI, data center, or on-premises product. Account for billing delays, discounts, currency, shared services, and business value before claiming realized savings.

**Source review date:** 2026-11-12.
