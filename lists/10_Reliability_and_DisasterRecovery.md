# 10 — Reliability and Disaster Recovery Checklist

> Verify that critical user journeys remain usable under expected failures and can recover within agreed downtime and data-loss targets. Reliability, backup/restore, disaster recovery, and business continuity must be demonstrated with evidence, not assumed from redundancy alone.

> **Scope: Shared / cross-cutting.** This file is one part of the 10_Reliability_and_DisasterRecovery.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Availability objectives


- [ ] **REL-001** `P2` Identify the business-critical services, user journeys, and supporting dependencies that require explicit reliability targets.
- [ ] **REL-002** `P1` Rank business processes and data by the impact of disruption through a documented business impact analysis or equivalent risk assessment.
- [ ] **REL-003** `P1` Set measurable service-level indicators for user-visible availability, successful operations, latency, and correctness where applicable.
- [ ] **REL-004** `P2` Define service-level objectives with calculation methods, target values, review windows, and accountable owners.
- [ ] **REL-005** `P1` Distinguish customer commitments and service-level agreements from internal reliability objectives and alert thresholds.
- [ ] **REL-006** `P1` Set recovery time objectives (RTOs) for each critical service or business process based on acceptable downtime.
- [ ] **REL-007** `P1` Set recovery point objectives (RPOs) for critical data and state based on acceptable data loss.
- [ ] **REL-008** `P1` Ensure RTO and RPO targets explicitly address dependency order, customer obligations, and realistic restoration constraints.
- [ ] **REL-009** `P2` Document planned maintenance windows and whether they are included in availability calculations and customer commitments.
- [ ] **REL-010** `P1` Use appropriate error-budget or equivalent change-risk controls when service-level objectives are defined.
- [ ] **REL-012** `P2` Define failure-severity thresholds and distinguish localized degradation, service incidents, and disaster declarations.
- [ ] **REL-014** `P2` Identify data integrity and consistency expectations during outages, failover, retries, and restoration.
- [ ] **REL-015** `P2` Assign a business owner and technical owner to each critical reliability and recovery target.
- [ ] **REL-016** `P1` Review reliability objectives after material changes to customer impact, criticality, workload, or contractual obligations.

## Disaster recovery and continuity


- [ ] **REL-058** `P0` Define disaster scenarios relevant to the service, including regional outage, data corruption, ransomware, operator error, and critical vendor unavailability.
- [ ] **REL-059** `P1` Choose a recovery strategy (restore, cold standby, warm standby, active-passive, or active-active) with explicit cost and RTO/RPO trade-offs.
- [ ] **REL-060** `P2` Document when an incident qualifies as a disaster and who may declare, escalate, and end the event.
- [ ] **REL-061** `P2` Maintain a step-by-step disaster-recovery runbook with prerequisites, named roles, decision points, validation, and escalation paths.
- [ ] **REL-066** `P1` Verify alternate-site resources, DNS, routing, certificates, monitoring, and permissions are compatible with recovery procedures where applicable.
- [ ] **REL-067** `P1` Test failover traffic routing, DNS propagation, session behavior, and dependent client resolution where relevant.
- [ ] **REL-068** `P1` Verify replicated data and promoted stores meet integrity and RPO expectations before reopening writes.
- [ ] **REL-069** `P1` Use controlled cutover and rollback/forward-recovery criteria to avoid repeated failover or inconsistent simultaneous writers.
- [ ] **REL-070** `P2` Define how customer transactions accepted during degradation or recovery are reconciled and audited.
- [ ] **REL-071** `P1` Include staff coverage, supplier contacts, manual workarounds, and business communications in the continuity plan.
- [ ] **REL-072** `P1` Prepare accurate internal and external outage status updates that can be published through alternate channels when needed.
- [ ] **REL-073** `P1` Rehearse disaster recovery through tabletop exercises and staged restoration drills with appropriate frequency and risk controls.
- [ ] **REL-074** `P1` Perform representative end-to-end recovery exercises safely, including cold-start and loss-of-primary-control-plane scenarios where feasible.
- [ ] **REL-075** `P1` Measure recovery times and data loss in drills against objectives rather than accepting the existence of a plan as proof.
- [ ] **REL-076** `P2` Define a controlled failback sequence, including data reconciliation, traffic migration, and verification of the restored primary site.
- [ ] **REL-077** `P2` Document risks of switching back too early, including replication lag, split-brain, and stale client connections.
- [ ] **REL-078** `P2` Assign owners and deadlines to every failed drill, broken dependency, documentation gap, and unproven recovery assumption.

## Release gate


- [ ] Critical service journeys and data have assigned owners and measurable availability, RTO, and RPO targets appropriate to their business impact.
- [ ] Important failure modes and dependency risks are assessed, and resilience controls have been exercised or supported by an explicitly accepted risk-based plan.
- [ ] Required backups are current, access-controlled, and demonstrated restorable through recent drills that verify data integrity and recovery objectives.
- [ ] Disaster-recovery activation, roles, communications, recovery order, cutover, and failback procedures are documented and rehearsed to the level required by service risk.
- [ ] Critical API and frontend flows degrade safely, avoid unintended duplicate actions or data loss, and recover coherently where those interfaces exist.
- [ ] Outstanding reliability risks, failed recovery tests, and objective breaches have a documented disposition, owner, remediation date, and authorized release decision.

**Domain-specific approval rule:** Block reliability sign-off when an unaccepted failure mode can disable an essential service, when required backups cannot be restored, when recovery targets are demonstrably missed without authorization, or when data integrity and recovery ownership are unresolved. A written runbook or backup job success alone does not prove recoverability.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#10_reliability_and_disasterrecovery), not prerequisites or verification evidence.

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
