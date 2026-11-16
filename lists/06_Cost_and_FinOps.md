# 06 — Cost and FinOps Checklist

> Verify that technology spending is attributable, visible, forecastable, and optimized for business value without compromising required quality, reliability, security, or user outcomes. FinOps is a shared product, engineering, finance, and procurement practice—not simply a directive to minimize the cloud bill.

> **Scope: Shared / cross-cutting.** This file is one part of the 06_Cost_and_FinOps.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Cost ownership and allocation

- [ ] **COST-001** `P2` Inventory all material technology costs for the product, including cloud infrastructure, SaaS subscriptions, data platforms, licensing, AI services, and contracted support where relevant.
- [ ] **COST-002** `P2` Assign an accountable product or business owner and an engineering owner for each material spending scope.
- [ ] **COST-003** `P2` Document the cost allocation hierarchy across accounts, projects, subscriptions, environments, cost centers, products, and teams.
- [ ] **COST-004** `P2` Define a versioned naming and tagging/labeling policy that makes resource ownership, environment, and cost center discoverable.
- [ ] **COST-005** `P1` Apply ownership and allocation metadata when provisioning new resources rather than depending only on retrospective cleanup.
- [ ] **COST-006** `P1` Check tag or label completeness and accuracy for a representative sample of cost-bearing resources.
- [ ] **COST-007** `P2` Identify services whose spend cannot be directly attributed and maintain a documented process to investigate unallocated charges.
- [ ] **COST-009** `P2` Document the chosen method for allocating shared costs, or explicitly decide to retain them in a central budget.
- [ ] **COST-010** `P1` Validate shared-cost allocations reconcile to the underlying charge without double counting or omitted amounts.
- [ ] **COST-011** `P1` Distinguish directly metered costs from allocated, estimated, or centrally funded costs in reports.
- [ ] **COST-012** `P2` Identify how credits, discounts, taxes, support fees, marketplace charges, and commitments are distributed for the reporting purpose.
- [ ] **COST-013** `P2` Maintain clear definitions for billed, effective/amortized, list, and contracted costs where these differ.
- [ ] **COST-014** `P1` Ensure invoices, provider billing exports, and cost reports use compatible billing periods, currencies, and cost semantics.
- [ ] **COST-015** `P1` Verify that financial chargeback figures can be reconciled to the relevant ledger or approved invoiced totals.
- [ ] **COST-016** `P2` Document how newly launched services, regions, environments, and vendors are added to the allocation model.
- [ ] **COST-017** `P2` Track allocation coverage and report material cost with missing, invalid, or conflicting ownership metadata.
- [ ] **COST-018** `P1` Review ownership after personnel, organizational, product, or environment changes so orphaned resources do not remain unassigned.
- [ ] **COST-019** `P1` Set access controls so each owner can see their costs without exposing unrelated customer or financial data.
- [ ] **COST-020** `P1` Agree ownership and escalation for unusual spend that spans multiple business units or shared platform dependencies.

## Budgets and visibility

- [ ] **COST-021** `P2` Define a budget for the product or workload with accountable approval, billing period, currency, and scope.
- [ ] **COST-023** `P1` Separate recurring run-rate spend from one-time setup, migration, licensing, training, and exceptional project costs.
- [ ] **COST-024** `P1` Distinguish current cash/billed costs from amortized commitment costs when those values support different decisions.
- [ ] **COST-025** `P1` Set a clear reporting cadence for cost owners and finance partners suited to spend volatility.
- [ ] **COST-026** `P1` Provide views by owner, product, environment, provider, service, and major cost driver where supported by source data.
- [ ] **COST-027** `P2` Document data freshness, export lag, estimated charges, and known inaccuracies before using dashboards for budget decisions.
- [ ] **COST-028** `P1` Validate the primary cost dashboard against provider billing data or accepted finance records at an agreed frequency.
- [ ] **COST-029** `P1` Calculate budget variance and explain both volume-related and unit-price-related cost differences.
- [ ] **COST-030** `P1` Monitor cumulative spend, expected end-of-period spend, and material changes in daily run rate.
- [ ] **COST-031** `P1` Configure budget threshold alerts and verify that they reach an accountable team through tested channels.
- [ ] **COST-032** `P1` Use anomaly detection or equivalent checks to identify unusual cost spikes that a static threshold might miss.
- [ ] **COST-033** `P2` Define which spend anomalies require immediate action versus routine financial review.
- [ ] **COST-034** `P2` Track anomaly investigations with owner, suspected cause, financial exposure, decision, and resolution date.
- [ ] **COST-035** `P1` Confirm alerts account for legitimate release events, planned load tests, seasonal traffic, and known provider reporting delays.
- [ ] **COST-036** `P1` Set guards for high-risk provisioning actions, expensive services, quotas, and unrestricted external usage where feasible.
- [ ] **COST-128** `P1` For metered services, exercise an authorized spending kill switch blocking new billable work at an approved ceiling while accounting for delayed provider reports and in-flight charges and preserving safe essential functions.
- [ ] **COST-037** `P2` Define financial escalation and exception procedures for forecast overruns and urgent increases in capacity.
- [ ] **COST-038** `P1` Keep budget and cost views distinguishable from user-facing pricing, revenue, and gross-margin reporting.
- [ ] **COST-039** `P2` Document assumptions in currency conversion, billing increments, and taxes for cross-provider comparisons.
- [ ] **COST-040** `P1` Periodically verify that reporting includes dormant accounts, subscriptions, SaaS seats, and decommissioned resources.
- [ ] **COST-041** `P1` Apply role-appropriate permissions to cost exports, budgets, invoices, and billing configuration.
- [ ] **COST-042** `P2` Define a process for correcting historical allocations and notifying affected stakeholders when material reports change.

## Usage efficiency

- [ ] **COST-043** `P2` Identify the top cost drivers by service, operation, environment, resource, tenant, or workload segment.
- [ ] **COST-044** `P1` Compare observed utilization and service objectives before changing instance sizes, capacity, or redundancy.
- [ ] **COST-046** `P1` Schedule shutdown or reduced capacity for eligible nonproduction environments while preserving needed availability.
- [ ] **COST-047** `P1` Review resource requests, limits, reservations, and autoscaling thresholds against measured traffic and saturation.
- [ ] **COST-049** `P1` Evaluate storage growth, access patterns, object versions, temporary data, backups, and lifecycle rules for avoidable cost.
- [ ] **COST-050** `P1` Optimize data retention, archival, compression, and tier selection without violating recovery, privacy, or compliance requirements.
- [ ] **COST-052** `P1` Reduce unnecessary polling, redundant queries, chatty interfaces, and repeated high-cost computation on critical flows.
- [ ] **COST-054** `P2` Consider batch processing, queueing, deduplication, and event-driven approaches where they lower cost without unacceptable latency.
- [ ] **COST-055** `P1` Evaluate how third-party API usage, tokens, requests, and model selection affect variable service costs when applicable.
- [ ] **COST-056** `P1` Apply safe usage ceilings or budgets to expensive user-triggered operations without unexpectedly breaking essential functionality.
- [ ] **COST-057** `P1` Review autoscaling, graceful overload behavior, and traffic shaping to avoid runaway resource expansion.
- [ ] **COST-059** `P1` Ensure shared services charge or attribute usage sufficiently to expose high-cost consumers when technically and financially appropriate.
- [ ] **COST-060** `P1` Compare optimized configurations under representative load, measuring cost and performance rather than cost alone.
- [ ] **COST-061** `P1` Verify cost reductions preserve agreed reliability, security, privacy, accessibility, and customer-experience requirements.
- [ ] **COST-062** `P1` Remove obsolete artifacts, test data, build caches, and environments according to retention and recovery policies.
- [ ] **COST-063** `P2` Track sustainability or energy-efficiency considerations when they are an explicit business objective, without claiming cost automatically equals emissions.
- [ ] **COST-064** `P2` Document savings estimates separately from realized spend reduction, cost avoidance, and rate improvements.

## Forecasting and optimization

- [ ] **COST-065** `P2` Maintain a rolling cost forecast with an owner, horizon, update cadence, and documented methodology.
- [ ] **COST-066** `P1` Use historical spend, workload demand, pricing, deployments, and known business changes as forecast inputs.
- [ ] **COST-067** `P1` Model at least expected and higher-demand scenarios for material variable cost drivers.
- [ ] **COST-068** `P2` Record major forecast assumptions, uncertainty, confidence limitations, and known discontinuities.
- [ ] **COST-069** `P1` Compare actual spend against prior forecasts at a consistent cadence and update the model when drivers change.
- [ ] **COST-070** `P2` Define financially meaningful unit metrics such as cost per successful transaction, active customer, inference, or processed gigabyte where applicable.
- [ ] **COST-071** `P2` Specify numerator, denominator, unit, included direct/shared costs, timeframe, and source for each cost-per-unit metric.
- [ ] **COST-072** `P1` Reconcile cost data with product usage measures before interpreting unit economics or margin movements.
- [ ] **COST-074** `P1` Estimate incremental cost of new features, markets, customers, data growth, and release traffic before approval.
- [ ] **COST-075** `P1` Review alternative architectures, services, regions, and pricing tiers against workload constraints and switching effort.
- [ ] **COST-076** `P1` Analyze on-demand versus commitment-based rates only after forecasting reasonably stable eligible usage.
- [ ] **COST-077** `P1` Validate reservation or commitment utilization and coverage and identify unused or expiring commitments.
- [ ] **COST-078** `P1` Include commitment lock-in, prepayment, minimum spend, cancellation terms, and projected demand uncertainty in purchasing decisions.
- [ ] **COST-079** `P1` Review vendor contracts, SaaS licenses, seat counts, tiers, and renewal dates for unused or poorly matched capacity.
- [ ] **COST-080** `P1` Calculate expected payback, engineering effort, risk, and opportunity cost before prioritizing a material optimization.
- [ ] **COST-081** `P2` Document a baseline and verification method before asserting that an optimization produced savings.
- [ ] **COST-084** `P2` Assign optimization initiatives owners, expected impact, completion dates, and post-change measurement.
- [ ] **COST-085** `P1` Include shutdown, migration, exit, or data-transfer costs in decisions to consolidate or change providers.
- [ ] **COST-086** `P1` Reassess financial targets periodically as product strategy, margin, customer value, and reliability needs change.

## Release gate

- [ ] The release has named product, engineering, and financial owners for its material technology costs, with an approved allocation approach for shared and direct costs.
- [ ] Budget, baseline, forecast, principal assumptions, and potential cost-impacting launch or growth scenarios are documented at an appropriate level of detail.
- [ ] Critical spending and usage reports reconcile to trusted provider or financial data within accepted tolerances, and material unallocated charges are explained or assigned for investigation.
- [ ] Budget threshold, unusual-spend, and quota alerts or equivalent guardrails have owners and a tested escalation route appropriate to release risk.
- [ ] Significant compute, storage, data-transfer, SaaS, API, and frontend cost drivers are reviewed for avoidable use without undermining performance, accessibility, security, or reliability commitments.
- [ ] Applicable API and frontend operations have controls against unbounded or duplicate billable actions, with appropriate behavior when quotas or limits are reached.
- [ ] Any material over-budget forecast, unaffordable unit economics, unapproved commitment, or other significant cost risk has an explicit authorized disposition and remediation owner.

**Domain-specific approval rule:** Block cost readiness approval if material spend is unowned and invisible, foreseeable high-impact cost exposure lacks acceptable bounds, or a required budget/contract approval is missing. Meeting a cost target does not justify bypassing legal, security, quality, accessibility, or reliability requirements.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#06_cost_and_finops), not prerequisites or verification evidence.

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

- [OWASP API4:2023](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/) — third-party spend and resource limits.

**Source review date:** 2026-11-12.
