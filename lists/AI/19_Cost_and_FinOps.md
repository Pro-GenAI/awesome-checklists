# 19 — Cost and FinOps Checklist

> Verify that technology spending is attributable, visible, forecastable, and optimized for business value without compromising required quality, reliability, security, or user outcomes. FinOps is a shared product, engineering, finance, and procurement practice—not simply a directive to minimize the cloud bill.

> **Scope: AI-specific.** This file is one part of the 19_Cost_and_FinOps.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Forecasting and optimization

- [ ] **COST-083** `P2` Define financial guardrails for new services, experiments, generative AI workloads, and tenant-level demand spikes where relevant.

## Release gate

- [ ] The release has named product, engineering, and financial owners for its material technology costs, with an approved allocation approach for shared and direct costs.
- [ ] Budget, baseline, forecast, principal assumptions, and potential cost-impacting launch or growth scenarios are documented at an appropriate level of detail.
- [ ] Critical spending and usage reports reconcile to trusted provider or financial data within accepted tolerances, and material unallocated charges are explained or assigned for investigation.
- [ ] Budget threshold, unusual-spend, and quota alerts or equivalent guardrails have owners and a tested escalation route appropriate to release risk.
- [ ] Significant compute, storage, data-transfer, SaaS, API, and frontend cost drivers are reviewed for avoidable use without undermining performance, accessibility, security, or reliability commitments.
- [ ] Applicable API and frontend operations have controls against unbounded or duplicate billable actions, with appropriate behavior when quotas or limits are reached.
- [ ] Any material over-budget forecast, unaffordable unit economics, unapproved commitment, or other significant cost risk has an explicit authorized disposition and remediation owner.

**Domain-specific approval rule:** Block cost readiness approval if material spend is unowned and invisible, foreseeable high-impact cost exposure lacks acceptable bounds, or a required budget/contract approval is missing. Meeting a cost target does not justify bypassing legal, security, quality, accessibility, or reliability requirements.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#19_cost_and_finops), not prerequisites or evidence of PASS.

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
