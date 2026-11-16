# 34 — Cost and FinOps Checklist

> Verify that technology spending is attributable, visible, forecastable, and optimized for business value without compromising required quality, reliability, security, or user outcomes. FinOps is a shared product, engineering, finance, and procurement practice—not simply a directive to minimize the cloud bill.

> **Scope: Backend / API-specific.** This file is one part of the 34_Cost_and_FinOps.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Cost ownership and allocation

- [ ] **COST-008** `P2` Assign owners to shared infrastructure and platform services such as observability, networking, security tooling, and build systems.

## Budgets and visibility

- [ ] **COST-022** `P2` Record forecast assumptions for baseline demand, launch peaks, growth, storage, data transfer, third-party APIs, and nonproduction environments.

## Usage efficiency

- [ ] **COST-045** `P1` Detect idle, unattached, orphaned, and consistently underused infrastructure and remove or right-size it with owner approval.
- [ ] **COST-048** `P1` Investigate overprovisioned compute, databases, containers, caches, and managed-service tiers.
- [ ] **COST-051** `P1` Assess network egress, cross-region transfers, CDN misses, and repeated service-to-service calls for avoidable spend.
- [ ] **COST-053** `P1` Review cache placement, cache hit rates, expiry, and invalidation to reduce repeat work without serving incorrect or private data.
- [ ] **COST-058** `P1` Check that performance tuning does not shift disproportionate costs to database, storage, network, or another internal team.

## Forecasting and optimization

- [ ] **COST-073** `P1` Differentiate resource efficiency from business unit economics so cheaper compute is not mistaken for improved customer value.
- [ ] **COST-082** `P1` Review cost-related regressions after software, infrastructure, workload, vendor, and pricing changes.

## API Checks

- [ ] **COST-087** `P2` Map critical API operations to their principal cost drivers, including compute, database I/O, storage, data transfer, and billable external calls.
- [ ] **COST-088** `P1` Measure cost or resource use per representative API request or completed business transaction where feasible.
- [ ] **COST-089** `P2` Define and validate request-size, response-size, pagination, and query-complexity limits for expensive endpoints.
- [ ] **COST-090** `P1` Test that filters, sorting, joins, and batch endpoints do not trigger unbounded database or analytics costs.
- [ ] **COST-091** `P1` Set appropriate quotas, throttling, concurrency limits, and timeouts for expensive consumer or tenant usage.
- [ ] **COST-127** `P1` Before metered provider calls, atomically reserve per-user/tenant/service quota across instances, reconcile actual use and failed calls, and test parallel requests cannot bypass the approved spend bound.
- [ ] **COST-092** `P1` Enforce finite retry budgets, backoff and idempotency; avoid retrying permanent errors and test ambiguous timeouts cannot multiply billable side effects.
- [ ] **COST-093** `P1` Prevent duplicate billable webhooks, message redelivery, overlapping scheduled jobs and recursive triggers using idempotency, bounded runs or single-run guards; test replay and concurrent triggers.
- [ ] **COST-094** `P1` Capture third-party API consumption and applicable usage tiers, price units, quotas, and overage policies.
- [ ] **COST-095** `P1` Use approved cost guardrails for AI inference or other metered APIs, such as token, context, payload, or call budgets, where relevant.
- [ ] **COST-096** `P2` Identify and control excessive fan-out, N+1 requests, and repeated downstream calls across a single logical operation.
- [ ] **COST-097** `P0` Review cache eligibility and per-tenant isolation for GET/read responses that can safely avoid repeated work.
- [ ] **COST-098** `P1` Monitor error, timeout, and canceled-request costs so failed operations are not invisible in unit economics.
- [ ] **COST-099** `P1` Ensure async job APIs expose status and cancellation to prevent redundant polling and duplicate submissions.
- [ ] **COST-100** `P1` Attribute API usage to an appropriate service, product, or tenant without exposing customer-identifying labels in high-cardinality telemetry.
- [ ] **COST-101** `P1` Distinguish real customer usage from tests, monitoring probes, load generation, and internal automation in cost analysis.
- [ ] **COST-102** `P1` Set usage anomaly alerts for clients, keys, routes, tenants, or vendors with financially material spend exposure.
- [ ] **COST-103** `P1` Review authorization and rate limits so unauthorized or abusive requests cannot trigger unlimited cost.
- [ ] **COST-104** `P1` Make cost-affecting API contract changes, new metered fields, or third-party dependencies visible during release review.
- [ ] **COST-105** `P1` Verify safe behavior when a billing-related quota is reached, including appropriate errors and recovery guidance.
- [ ] **COST-106** `P1` Confirm API cost optimizations preserve response correctness, availability objectives, and compatibility guarantees.

## Release gate

- [ ] The release has named product, engineering, and financial owners for its material technology costs, with an approved allocation approach for shared and direct costs.
- [ ] Budget, baseline, forecast, principal assumptions, and potential cost-impacting launch or growth scenarios are documented at an appropriate level of detail.
- [ ] Critical spending and usage reports reconcile to trusted provider or financial data within accepted tolerances, and material unallocated charges are explained or assigned for investigation.
- [ ] Budget threshold, unusual-spend, and quota alerts or equivalent guardrails have owners and a tested escalation route appropriate to release risk.
- [ ] Significant compute, storage, data-transfer, SaaS, API, and frontend cost drivers are reviewed for avoidable use without undermining performance, accessibility, security, or reliability commitments.
- [ ] Applicable API and frontend operations have controls against unbounded or duplicate billable actions, with appropriate behavior when quotas or limits are reached.
- [ ] Any material over-budget forecast, unaffordable unit economics, unapproved commitment, or other significant cost risk has an explicit authorized disposition and remediation owner.

**Domain-specific approval rule:** Block cost readiness approval if material spend is unowned and invisible, foreseeable high-impact cost exposure lacks acceptable bounds, or a required budget/contract approval is missing. Meeting a cost target does not justify bypassing legal, security, quality, accessibility, or reliability requirements.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#34_cost_and_finops), not prerequisites or verification evidence.

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

- [OWASP API4:2023](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/) — costly downstream calls and quotas.

**Source review date:** 2026-11-12.
