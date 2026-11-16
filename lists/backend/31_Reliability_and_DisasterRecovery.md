# 31 — Reliability and Disaster Recovery Checklist

> Verify that critical user journeys remain usable under expected failures and can recover within agreed downtime and data-loss targets. Reliability, backup/restore, disaster recovery, and business continuity must be demonstrated with evidence, not assumed from redundancy alone.

> **Scope: Backend / API-specific.** This file is one part of the 31_Reliability_and_DisasterRecovery.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Availability objectives


- [ ] **REL-011** `P1` Measure critical workflow success from a user perspective instead of relying only on instance or server uptime.
- [ ] **REL-013** `P2` Record expected regional, network, vendor, identity-provider, and data-store dependencies for each critical journey.

## Resilience and redundancy


- [ ] **REL-017** `P2` Document fault domains and single points of failure across compute, storage, network, identity, DNS, and external providers.
- [ ] **REL-018** `P1` Select redundant capacity and isolation boundaries according to actual service objectives rather than assuming multi-region deployment is always required.
- [ ] **REL-028** `P2` Define queue limits, dead-letter handling, retry limits, and recovery from accumulated backlog for asynchronous systems.
- [ ] **REL-029** `P1` Protect durable state from accidental loss during restarts, worker relocation, or autoscaling.
- [ ] **REL-030** `P1` Test database replication, replica promotion, split-brain prevention, and transaction behavior under failures when replication is used.
- [ ] **REL-032** `P1` Check maintenance/disruption controls such as rolling updates and Kubernetes PodDisruptionBudgets where relevant, recognizing limits on involuntary failures.
- [ ] **REL-035** `P1` Run controlled fault-injection or game-day scenarios covering representative instance, dependency, network, or storage failures.
- [ ] **REL-019** `P1` Verify replacement instances or replicas can receive traffic without relying on unavailable local or ephemeral state.
- [ ] **REL-020** `P1` Use health and readiness checks that reflect ability to serve important requests without restarting healthy instances during dependency outages.
- [ ] **REL-021** `P1` Test load-balancing and failover behavior when an instance, node, or availability zone becomes unhealthy.
- [ ] **REL-022** `P1` Check that shared components and control planes do not create hidden correlated-failure paths.
- [ ] **REL-023** `P2` Define timeouts and deadlines on cross-service calls so partial outages cannot exhaust caller resources indefinitely.
- [ ] **REL-024** `P1` Use bounded retries with backoff and jitter where appropriate; prevent amplification by stacked retry layers.
- [ ] **REL-025** `P2` Specify idempotency or deduplication for operations that may be repeated after timeouts or failover.
- [ ] **REL-026** `P1` Apply concurrency limits, backpressure, circuit breaking, or load shedding to preserve useful service during overload.
- [ ] **REL-027** `P1` Separate background work, bulk operations, and critical interactive requests where competition could jeopardize reliability.
- [ ] **REL-031** `P1` Determine how stale reads, eventual consistency, or replication lag affect customer-visible correctness.
- [ ] **REL-033** `P1` Verify critical third-party dependencies have documented degraded modes, alternative workflows, or accepted outages.
- [ ] **REL-034** `P1` Provide operational controls for disabling high-risk features, stopping runaway jobs, or reducing load during incidents.
- [ ] **REL-036** `P1` Measure how quickly normal service is restored after a simulated failure and compare against the relevant target.
- [ ] **REL-037** `P1` Retest resilience assumptions after major topology, dependency, data architecture, or traffic-pattern changes.

## Backup and restoration


- [ ] **REL-038** `P2` Inventory business-critical data, database schemas, configuration, object storage, secrets references, and other state required for recovery.
- [ ] **REL-043** `P1` Encrypt backup data in transit and at rest with controlled key management and recovery access.
- [ ] **REL-044** `P1` Separate backup administration and deletion privileges from ordinary application and deployment identities.
- [ ] **REL-048** `P1` Verify consistency across related data stores, queues, object storage, and transactional boundaries at the chosen recovery point.
- [ ] **REL-039** `P2` Document data that is backed up versus deliberately reproducible from authoritative sources, including rebuild procedures.
- [ ] **REL-040** `P1` Choose backup frequency and retention to satisfy RPO, legal retention, storage cost, and business risk.
- [ ] **REL-041** `P1` Automate backup creation and verify job completion rather than assuming a schedule means backups succeed.
- [ ] **REL-042** `P1` Alert an accountable owner when backups are stale, fail, become inaccessible, or exceed expected completion time.
- [ ] **REL-045** `P1` Protect recovery copies against accidental or malicious deletion using isolation, immutability, offline copies, or an equivalent risk-based control.
- [ ] **REL-046** `P2` Document backup location, region/account/provider dependence, replication, and survivability of the relevant failure scenario.
- [ ] **REL-047** `P1` Capture versioned schema, application configuration, encryption-key availability, and external dependencies needed to use restored data.
- [ ] **REL-049** `P1` Test point-in-time recovery or equivalent granularity when the business RPO requires it.
- [ ] **REL-050** `P1` Periodically restore backups to an isolated environment using documented or automated procedures.
- [ ] **REL-051** `P1` After test restoration, query representative records and execute relevant business operations to validate usability and integrity.
- [ ] **REL-052** `P1` Measure actual restore duration and recovered data age and compare them with RTO and RPO targets.
- [ ] **REL-053** `P1` Ensure restore testing does not leak sensitive data into insecure nonproduction environments.
- [ ] **REL-054** `P1` Test recovery from corrupted, missing, outdated, or compromised backup copies where risk warrants.
- [ ] **REL-055** `P2` Maintain recoverable backup credentials, key material, and operational documentation even if the primary environment is unavailable.
- [ ] **REL-056** `P2` Document safe disposal, retention expiry, and post-incident access revocation for recovery copies.
- [ ] **REL-057** `P2` Record restoration drill results, deviations, corrective actions, and the next scheduled verification in project-specific records.

## Disaster recovery and continuity


- [ ] **REL-062** `P1` Keep recovery documentation and communication channels accessible when the primary identity, network, or documentation platform is unavailable.
- [ ] **REL-063** `P1` Confirm recovery staff can obtain approved emergency access without weakening controls or depending on the failed infrastructure.
- [ ] **REL-064** `P2` Map restoration order across identity, networking, storage, databases, application services, APIs, and end-user interfaces.
- [ ] **REL-065** `P1` Prepare required infrastructure definitions, machine images, artifacts, configuration, and secrets references outside the affected failure domain.
- [ ] **REL-079** `P1` Review disaster-recovery exercises, incidents, and infrastructure changes to keep the runbook and target values current.

## API Checks


- [ ] **REL-080** `P2` Define availability and data-correctness indicators for each business-critical API operation and consumer group.
- [ ] **REL-081** `P1` Verify API clients have bounded timeouts and can distinguish transient outages from permanent validation or authorization errors.
- [ ] **REL-082** `P2` Define response codes and stable error representations for overload, unavailable dependencies, and temporary maintenance.
- [ ] **REL-083** `P2` Specify retry policies with budgets and jitter; document when a failed request must not be retried.
- [ ] **REL-084** `P1` Ensure repeated or ambiguous write requests use idempotency keys or documented deduplication where necessary.
- [ ] **REL-085** `P1` Test partial failures when downstream APIs, databases, message brokers, or identity services become slow or unavailable.
- [ ] **REL-086** `P1` Provide readiness and liveness signals appropriate for routing decisions without disclosing internal secrets.
- [ ] **REL-087** `P1` Confirm long-running API tasks expose durable status or resumption mechanisms when interruptions are expected.
- [ ] **REL-088** `P1` Test API behavior when read replicas lag, failover changes leaders, or cached data becomes temporarily stale.
- [ ] **REL-089** `P1` Verify queues, webhooks, and event handlers tolerate duplicate delivery, delayed delivery, and replay according to their contracts.
- [ ] **REL-090** `P2` Document API maintenance and degraded-mode semantics for client developers, including relevant retry guidance.
- [ ] **REL-091** `P1` Test graceful shutdown and connection draining for active requests and streaming responses during deployment and failover.
- [ ] **REL-092** `P1` Assess rate limiting, traffic prioritization, and load shedding for preserving critical endpoints during overload.
- [ ] **REL-093** `P1` Validate that failed authentication or authorization dependencies cannot accidentally permit unauthorized API access.
- [ ] **REL-094** `P1` Test backward compatibility and version negotiation when old and new API instances coexist during failover or phased recovery.
- [ ] **REL-095** `P1` Retain useful request IDs, trace context, and version metadata for API errors without unnecessarily logging sensitive data.
- [ ] **REL-096** `P1` Verify API contract-test and failover-test coverage for critical consumer/provider dependencies before sign-off.
- [ ] **REL-097** `P1` Confirm recovery actions do not silently lose, reorder, or duplicate committed business operations contrary to the documented API contract.

## Release gate


- [ ] Critical service journeys and data have assigned owners and measurable availability, RTO, and RPO targets appropriate to their business impact.
- [ ] Important failure modes and dependency risks are assessed, and resilience controls have been exercised or supported by an explicitly accepted risk-based plan.
- [ ] Required backups are current, access-controlled, and demonstrated restorable through recent drills that verify data integrity and recovery objectives.
- [ ] Disaster-recovery activation, roles, communications, recovery order, cutover, and failback procedures are documented and rehearsed to the level required by service risk.
- [ ] Critical API and frontend flows degrade safely, avoid unintended duplicate actions or data loss, and recover coherently where those interfaces exist.
- [ ] Outstanding reliability risks, failed recovery tests, and objective breaches have a documented disposition, owner, remediation date, and authorized release decision.

**Domain-specific approval rule:** Block reliability sign-off when an unaccepted failure mode can disable an essential service, when required backups cannot be restored, when recovery targets are demonstrably missed without authorization, or when data integrity and recovery ownership are unresolved. A written runbook or backup job success alone does not prove recoverability.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#31_reliability_and_disasterrecovery), not prerequisites or verification evidence.

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
