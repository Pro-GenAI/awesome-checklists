# 16 — Reliability and Disaster Recovery Checklist

> Verify that critical user journeys remain usable under expected failures and can recover within agreed downtime and data-loss targets. Reliability, backup/restore, disaster recovery, and business continuity must be demonstrated with evidence, not assumed from redundancy alone.

> **Scope: Frontend-specific.** This file is one part of the 16_Reliability_and_DisasterRecovery.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **REL-098** `P2` Define a clear user-facing experience when essential backend services are unavailable or degraded.
- [ ] **REL-099** `P1` Provide understandable loading, retry, offline, maintenance, and recovery states for critical user workflows.
- [ ] **REL-100** `P1` Distinguish transient connectivity failures from account, permission, validation, and permanent application errors.
- [ ] **REL-101** `P1` Prevent repeated submission of high-impact actions when an API outcome is unknown, and explain how the user can verify completion.
- [ ] **REL-102** `P1` Preserve in-progress form content and other recoverable user input during temporary failures when appropriate.
- [ ] **REL-103** `P1` Ensure failed background saves and offline edits are surfaced rather than silently discarded.
- [ ] **REL-104** `P2` Define how stale or cached content is labeled when freshness could change a user decision.
- [ ] **REL-105** `P1` Test deep links and core navigation when an origin server, CDN, or supporting API becomes unreachable.
- [ ] **REL-106** `P1` Verify cached frontend assets and service-worker versions remain compatible with recovered backend contracts.
- [ ] **REL-107** `P1` Provide an accessible alternative to live, auto-updating UI status messages for screen-reader and keyboard users.
- [ ] **REL-108** `P1` Explain temporarily disabled features and offer useful alternatives rather than presenting controls that fail without feedback.
- [ ] **REL-109** `P1` Use bounded client retries and avoid refresh loops or aggressive polling that amplify backend outages.
- [ ] **REL-110** `P1` Test session expiration, authentication-provider outages, and recovery without losing unrelated user state where feasible.
- [ ] **REL-111** `P1` Check that dynamic application content remains coherent during cross-region traffic changes or cached DNS transitions.
- [ ] **REL-112** `P1` Verify that outage banners, status pages, and support links remain accessible using an independently resilient channel when warranted.
- [ ] **REL-113** `P1` Confirm UI behavior when partial data loads, individual widgets fail, or several API requests return inconsistent versions.
- [ ] **REL-114** `P1` Test that primary user journeys recover correctly after service restoration without requiring unsafe manual cache clearing.
- [ ] **REL-115** `P1` Make post-recovery data reconciliation or duplicate transaction warnings visible where the business workflow requires them.

## Release gate

- [ ] Critical service journeys and data have assigned owners and measurable availability, RTO, and RPO targets appropriate to their business impact.
- [ ] Important failure modes and dependency risks are assessed, and resilience controls have been exercised or supported by an explicitly accepted risk-based plan.
- [ ] Required backups are current, access-controlled, and demonstrated restorable through recent drills that verify data integrity and recovery objectives.
- [ ] Disaster-recovery activation, roles, communications, recovery order, cutover, and failback procedures are documented and rehearsed to the level required by service risk.
- [ ] Critical API and frontend flows degrade safely, avoid unintended duplicate actions or data loss, and recover coherently where those interfaces exist.
- [ ] Outstanding reliability risks, failed recovery tests, and objective breaches have a documented disposition, owner, remediation date, and authorized release decision.

**Domain-specific approval rule:** Block reliability sign-off when an unaccepted failure mode can disable an essential service, when required backups cannot be restored, when recovery targets are demonstrably missed without authorization, or when data integrity and recovery ownership are unresolved. A written runbook or backup job success alone does not prove recoverability.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#16_reliability_and_disasterrecovery), not prerequisites or verification evidence.

## Trusted references and scope

These verifiable review questions are informed by authoritative engineering and contingency-planning guidance. They are not copied standards language and do not imply universal compliance or guaranteed availability.

- [Microsoft Azure Well-Architected — Reliability design review checklist](https://learn.microsoft.com/en-us/azure/well-architected/resiliency/design-requirements) — critical-flow prioritization, failure-mode analysis, SLO/RTO/RPO targets, resilience, and recovery testing.
- [Microsoft Azure Well-Architected — Disaster recovery strategies](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) — DR architecture, roles and communication, infrastructure, failover, failback, and drills.
- [AWS Well-Architected — Reliability design principles](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html) — automatic recovery, resilience, and repeatable recovery testing.
- [AWS Well-Architected — Disaster recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html) — distinguishing recovery time objectives from recovery point objectives.
- [AWS Well-Architected — Back up data](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/back-up-data.html) — backup identification, encryption, automation, and restoration.
- [AWS Well-Architected — Test backup recovery](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html) — verifying restored integrity and RTO/RPO outcomes.
- [AWS Well-Architected — Plan for disaster recovery](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html) — documented recovery plans, configuration drift, and recovery drills.
- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — business impact assessment, contingency plans, and exercises.
- [Google SRE — Production Services Best Practices](https://sre.google/sre-book/service-best-practices/) — user-centric service-level objectives and error budgets.
- [Google SRE — Handling Overload](https://sre.google/sre-book/handling-overload/) — bounded retries, load shedding, and overload prevention.
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — failure propagation, overload recovery, and isolating dependencies.
- [Kubernetes — PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) — protecting against voluntary disruptions where Kubernetes is used; not a guarantee against all failures.

**Applicability:** Define targets and test depth according to criticality, business impact, and actual platform. Multi-region deployments, active-active replication, Kubernetes disruption budgets, and zero-data-loss objectives are not universally required. A PodDisruptionBudget addresses supported voluntary Kubernetes evictions, not all outages. Avoid fault tests that could harm production users without proper authorization and safeguards.

**Source review date:** 2026-11-12.
