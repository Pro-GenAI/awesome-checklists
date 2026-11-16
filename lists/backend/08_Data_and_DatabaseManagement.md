# 08 — Data and Database Management Checklist

> Review data ownership, schema design, migration safety, transactional correctness, data quality, and lifecycle management. This checklist covers the integrity and governance of information throughout its use; apply the separate Security, Legal, Reliability, and Performance checklists for their deeper controls.

> **Scope: Backend / API-specific.** This file is one part of the 08_Data_and_DatabaseManagement.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Data modeling and governance


- [ ] **DATA-009** `P1` Use schema-level primary key, unique, foreign key, and check constraints for invariants that the chosen database can enforce.
- [ ] **DATA-016** `P2` Define tenant, organization, and ownership boundaries for shared tables, object storage, search indexes, and analytical datasets.
- [ ] **DATA-127** `P1` Use parameterized SQL or equivalent safe driver bindings for untrusted values, and allowlist structural query choices such as column names, table names, and sort directions; review dynamic SQL inside stored procedures and ORM queries.
- [ ] **DATA-128** `P0` Where RLS is used, test SELECT, INSERT, UPDATE (existing and resulting rows) and DELETE with real anonymous, member, tenant and admin roles; reject forged ownership/cross-tenant access and audit owner/service/BYPASSRLS-equivalent bypass.
- [ ] **DATA-129** `P1` Verify runtime, reporting, migration, and administrator database accounts have only required table, schema, function, and default privileges, and test denial of unauthorized direct database access.
- [ ] **DATA-141** `P1` Test pooled-connection reuse for leakage of tenant identity, row-security context, session variables, search paths, temporary objects, and transaction state between unrelated requests.
- [ ] **DATA-153** `P1` For encrypted database connections, verify certificate-chain and hostname validation, credential handling, and trusted proxy behavior rather than assuming transport encryption alone authenticates the destination.

- [ ] **DATA-001** `P2` Inventory authoritative data stores, major datasets, data products, and ownership boundaries across the system.
- [ ] **DATA-002** `P2` Assign a business owner and technical steward to each critical dataset and record their escalation contacts.
- [ ] **DATA-003** `P2` Document the purpose, intended consumers, sensitivity, and expected lifecycle of each important data category.
- [ ] **DATA-004** `P2` Identify the source of truth for each business entity and avoid conflicting writable replicas without defined reconciliation.
- [ ] **DATA-005** `P1` Model entities, relationships, identifiers, and cardinality in an up-to-date conceptual or logical schema.
- [ ] **DATA-006** `P2` Define stable primary keys and public identifiers with explicit uniqueness and lifecycle expectations where applicable.
- [ ] **DATA-007** `P2` Document the semantics, units, timezone, precision, and allowed values of important fields.
- [ ] **DATA-008** `P2` Define nullability, defaults, optionality, missing-value semantics, and field deprecation rules consistently.
- [ ] **DATA-010** `P2` Define ownership and accepted consequences of cascade, restrict, and soft-delete relationships rather than relying on defaults.
- [ ] **DATA-011** `P1` Choose normalization or deliberate denormalization based on measured access needs and consistency trade-offs.
- [ ] **DATA-012** `P1` Assess document, graph, time-series, key-value, or relational models against actual access patterns and integrity requirements.
- [ ] **DATA-013** `P2` Document event, audit, operational, analytical, and derived data separately so consumers do not treat derived copies as authoritative.
- [ ] **DATA-014** `P2` Map data flows across services, integrations, queues, analytics stores, caches, and external recipients.
- [ ] **DATA-015** `P2` Record classifications such as public, internal, confidential, or restricted, tied to real processing and access controls.
- [ ] **DATA-017** `P2` Document data lineage from source capture to processing, transformation, publication, and downstream consumption.
- [ ] **DATA-018** `P1` Establish change ownership and approval for material schema, data contract, and governance decisions.
- [ ] **DATA-019** `P2` Identify regulatory, contractual, or sector-specific handling obligations with the qualified legal or privacy owner.
- [ ] **DATA-020** `P2` Define discoverable data dictionaries and schema documentation with accountable maintenance responsibility.
- [ ] **DATA-124** `P1` For each business-critical workflow, specify acceptable database read consistency, acknowledged-write durability, and maximum staleness; test these guarantees under normal operation and failover.
- [ ] **DATA-125** `P1` Establish and exercise a database-provider exit or data-portability plan using a representative export and re-import that preserves identifiers, constraints, encodings, and dependent consumer mappings.

## Database operations and migrations


- [ ] **DATA-022** `P1` Apply schema changes through a consistent, automated or controlled deployment workflow rather than untracked manual updates.
- [ ] **DATA-026** `P1` Verify that application versions coexisting during deployment remain compatible with the intended transitional schema.
- [ ] **DATA-032** `P1` Detect schema drift between the expected migration history and actual deployed database definitions.
- [ ] **DATA-033** `P1` Use distinct, narrowly scoped database identities for applications, migration automation, and administrators.
- [ ] **DATA-035** `P1` Ensure database connection pool configuration, timeouts, and retry behavior are documented for expected load.
- [ ] **DATA-040** `P1` Ensure database versions, extensions, drivers, and client libraries have an owner and supported upgrade plan.
- [ ] **DATA-041** `P1` Test scheduled maintenance, failover, and database upgrades for client compatibility and connection recovery.
- [ ] **DATA-042** `P1` Review storage and database configuration for availability, durability, performance, and applicable access-control requirements.
- [ ] **DATA-130** `P1` Keep representative execution-plan and latency baselines for high-impact SQL queries across realistic table sizes, parameter values, and data skew; investigate regressions after schema, statistics, or engine changes.
- [ ] **DATA-131** `P1` Choose and benchmark composite, partial, expression, or covering indexes against actual predicates and sort orders where supported, measuring read gains against write amplification, storage, and maintenance costs.
- [ ] **DATA-132** `P1` Review index-usage statistics for redundant, duplicate, or consistently unused indexes and validate workload and rollback safety before removing an index.
- [ ] **DATA-133** `P1` Detect and correct N+1 database queries caused by ORM relations or resolver loops using representative list and nested-object workloads, rather than relying only on API request counts.
- [ ] **DATA-134** `P1` Benchmark deep pagination and large sort/filter workloads; use bounded queries and keyset or cursor techniques where appropriate to avoid high-offset scans and unstable ordering.
- [ ] **DATA-135** `P1` For partitioned data, test partition pruning, partition-boundary reads/writes, default-partition growth, and the safe expiry or detachment of old partitions under production-like data distributions.
- [ ] **DATA-136** `P1` For sharded databases, validate shard-key cardinality, skew, monotonic hot spots, query-routing efficiency, and resharding recovery plans against observed access patterns.
- [ ] **DATA-137** `P1` Monitor long-running and idle-open transactions, lock waits, deadlocks, and blocked writers with workload-specific thresholds, diagnostic attribution, and escalation ownership.
- [ ] **DATA-138** `P1` Set and exercise appropriate database statement, lock-wait, and idle-in-transaction time budgets, including cancellation and connection-pool behavior when those limits are reached.
- [ ] **DATA-140** `P1` Capacity-test aggregate database connection-pool limits across all service instances, background jobs, and tenants, reserving operational headroom and applying backpressure before exhausting server connections.
- [ ] **DATA-143** `P1` Where replication slots or log-based CDC are used, monitor lag, retained-log/WAL bytes, abandoned slots, and disk thresholds; define safe consumer recovery or retirement procedures.
- [ ] **DATA-144** `P1` For logical database replication, verify how DDL, indexes, privileges, sequence values, and incompatible column changes are synchronized and tested during cutovers rather than assuming data replication covers them.
- [ ] **DATA-148** `P1` Demonstrate point-in-time recovery to a selected timestamp or log position using a valid base backup and complete incremental/log chain; reconcile recovered business records with the agreed recovery objective.
- [ ] **DATA-149** `P1` Alert on failed, delayed, or missing transaction-log/WAL archiving and validate that backup retention never deletes a base or incremental dependency required for the promised recovery window.
- [ ] **DATA-150** `P1` For MVCC databases such as PostgreSQL, monitor vacuum or compaction backlog, long-lived snapshots, and transaction-ID age; verify anti-wraparound maintenance completes before write availability is threatened.
- [ ] **DATA-151** `P1` After bulk data changes or material shifts in column-value distributions, verify planner statistics and relevant multicolumn correlations are refreshed before accepting critical query performance.
- [ ] **DATA-152** `P1` Test protections against unbounded scans, expensive sorts, temporary-disk spill, and runaway database queries using representative adversarial but authorized workloads.
- [ ] **DATA-155** `P1` During long-running backfills or dual-read/dual-write transitions, test concurrent inserts, updates, and deletes for lost changes, reconciliation gaps, and safe restart at checkpoints.

- [ ] **DATA-021** `P2` Track schema definitions and migrations in version control, with reviewed ownership and change descriptions.
- [ ] **DATA-023** `P2` Test migrations against representative data volumes, versions, constraints, indexes, and realistic schema history.
- [ ] **DATA-024** `P1` Estimate and measure migration duration, lock impact, resource consumption, and required maintenance windows.
- [ ] **DATA-025** `P1` Use additive/expand-contract migration steps where compatible rolling releases or independent consumers require them.
- [ ] **DATA-027** `P1` Ensure required data backfills are restartable or safely resumable after partial completion.
- [ ] **DATA-028** `P2` Specify batching, checkpoints, and throttling for long-running updates to avoid exhausting transactions or production resources.
- [ ] **DATA-029** `P1` Test safe handling of preexisting invalid data before introducing stronger constraints or new required fields.
- [ ] **DATA-030** `P2` Define an explicit strategy for changes that cannot be rolled back, including forward remediation or restoration plans.
- [ ] **DATA-031** `P2` Record migration ordering, application dependencies, ownership, and go/no-go decision points.
- [ ] **DATA-034** `P1` Require appropriate approval and auditability for production data fixes, destructive migrations, and privileged operations.
- [ ] **DATA-036** `P1` Monitor query execution plans and slow queries before introducing or removing performance-critical indexes.
- [ ] **DATA-037** `P1` Measure index creation or rebuild impact and choose online/concurrent methods when supported and warranted.
- [ ] **DATA-038** `P1` Review storage growth, vacuum/compaction, maintenance tasks, partitioning, and capacity thresholds for the selected engine.
- [ ] **DATA-039** `P2` Document replica topology, consistency/lag behavior, and rules for sending read and write traffic where replicas are used.

## Integrity and quality


- [ ] **DATA-050** `P1` Use optimistic locking, version numbers, database locking, or equivalent controls where concurrent edits would cause data loss.
- [ ] **DATA-064** `P1` Retest critical integrity guarantees after schema changes, new integrations, and database engine upgrades.
- [ ] **DATA-139** `P1` For deadlock or serialization failures, test bounded retries of the complete transaction with backoff and no repeated irreversible side effects; distinguish retryable errors from permanent constraint failures.
- [ ] **DATA-142** `P1` When a connection drops or times out near commit, reconcile the authoritative transaction outcome before repeating a write so uncertain success does not cause duplicate or missing effects.
- [ ] **DATA-145** `P1` Test change-data-capture initial snapshot-to-stream handoff, resume-position persistence, duplicate delivery, missing event detection, and out-of-order replay using representative updates and deletes.
- [ ] **DATA-146** `P1` Where database changes publish events, verify that state updates and durable outbox records commit atomically, and that downstream publication/consumption can recover without losing or duplicating business effects.
- [ ] **DATA-147** `P1` For outbox or CDC consumers, verify event identifiers, per-entity ordering assumptions, retry/dead-letter handling, and idempotent reprocessing after a consumer outage.
- [ ] **DATA-154** `P1` For replica-backed reads, test freshness thresholds and read-after-write routing during replica lag or failover so workflows requiring current values do not silently consume stale results.

- [ ] **DATA-043** `P2` Define required field completeness, uniqueness, validity, consistency, accuracy, and freshness checks for critical datasets.
- [ ] **DATA-045** `P1` Validate schema types, ranges, formats, references, and expected enumerations before accepting new data.
- [ ] **DATA-046** `P1` Establish rules for duplicate detection, entity identity resolution, and permitted legitimate duplicates.
- [ ] **DATA-047** `P2` Define transaction boundaries for multi-step operations that must commit or fail as one unit.
- [ ] **DATA-048** `P1` Choose transaction isolation and concurrency controls that preserve required invariants under simultaneous writes.
- [ ] **DATA-049** `P1` Test lost-update, write-conflict, double-submit, and transaction retry scenarios on high-risk workflows.
- [ ] **DATA-051** `P1` Test that retries, repeated messages, and redelivered events cannot duplicate committed effects beyond the defined contract.
- [ ] **DATA-052** `P2` Define validation and reconciliation rules between source records, derived tables, replicas, and downstream consumers.
- [ ] **DATA-053** `P1` Measure data freshness and replication or processing lag where consumers depend on timely updates.
- [ ] **DATA-054** `P2` Specify handling for missing, stale, late, out-of-order, or malformed data in scheduled and streaming pipelines.
- [ ] **DATA-055** `P1` Add automated data-quality checks to ingestion and transformation pipelines with ownership for failures.
- [ ] **DATA-056** `P2` Define quarantine, rejection, correction, and replay behavior for invalid records without silently discarding them.
- [ ] **DATA-057** `P1` Reconcile record counts, checksums, totals, or domain-level invariants after migrations and bulk imports.
- [ ] **DATA-058** `P1` Ensure numerical precision and rounding rules are appropriate for financial, scientific, and other exact-value fields.
- [ ] **DATA-059** `P1` Verify character encoding, locale-aware comparisons, case rules, and timezone conversion do not corrupt meaning.
- [ ] **DATA-060** `P1` Check that tenant identifiers and access boundaries are preserved in joins, exports, transformations, and background jobs.
- [ ] **DATA-061** `P1` Capture auditable changes to regulated or high-impact data with sufficient context without logging protected secrets unnecessarily.
- [ ] **DATA-062** `P1` Investigate and track failed quality assertions with severity, data owner, affected scope, and remediation status.
- [ ] **DATA-063** `P1` Monitor for unexpected schema changes and data distributions that indicate upstream defects.

## Retention and lifecycle


- [ ] **DATA-065** `P2` Inventory personal, sensitive, transactional, audit, analytical, temporary, and derived data with their retention owners.
- [ ] **DATA-066** `P2` Document the purpose and applicable contractual, regulatory, or business justification for each retention period.
- [ ] **DATA-067** `P2` Define retention start events and durations precisely, including time zones, inactivity, account closure, or other triggers.
- [ ] **DATA-068** `P2` Identify data that must not be retained after its processing purpose ends, subject to applicable exceptions and obligations.
- [ ] **DATA-069** `P2` Document circumstances requiring retention holds, disputes, investigations, or other authorized suspensions of deletion.
- [ ] **DATA-070** `P2` Define archival tiers, data access limits, and permitted downstream uses for information kept beyond active operation.
- [ ] **DATA-071** `P1` Automate expiry, archive, anonymization, or deletion workflows where appropriate, with observable completion signals.
- [ ] **DATA-072** `P1` Verify deletion affects derived stores, search indexes, analytics replicas, exports, and caches to the extent required.
- [ ] **DATA-073** `P1` Account for backup retention and delayed erasure processes under the applicable legal framework and documented policy.
- [ ] **DATA-074** `P1` Ensure soft-delete records, tombstones, and archived copies have clear lifecycle and access semantics.
- [ ] **DATA-075** `P1` Provide processes to handle valid user or customer access, correction, portability, and erasure requests where legally applicable.
- [ ] **DATA-076** `P1` Distinguish pseudonymization from irreversible anonymization in internal data classification and deletion claims.
- [ ] **DATA-077** `P1` Verify anonymization or aggregation prevents reasonable reidentification before treating resulting datasets as anonymous.
- [ ] **DATA-078** `P1` Control access and log authorized retrieval of archived or previously restricted data.
- [ ] **DATA-079** `P2` Identify minimum necessary data fields and avoid collecting additional attributes only for speculative future use.
- [ ] **DATA-080** `P2` Document external recipients and processors that must receive corrections, deletion requests, or retention changes where required.
- [ ] **DATA-081** `P2` Define purge/reconciliation checks that detect orphaned records and expired data in secondary systems.
- [ ] **DATA-082** `P1` Check that temporary uploads, export files, failed jobs, and staging datasets do not remain indefinitely.
- [ ] **DATA-083** `P2` Define secure media disposal, credential destruction, and device-level data sanitization when hardware or storage is retired.
- [ ] **DATA-084** `P1` Review retention schedules and lifecycle controls periodically as products, data use, and obligations change.
- [ ] **DATA-126** `P1` Review data residency and authorized cross-border transfer boundaries for database replicas, backups, snapshots, analytics copies, and disaster-recovery environments before provisioning them.

## API Checks


- [ ] **DATA-085** `P2` Define the canonical meaning and authoritative source of every critical field exposed by an API.
- [ ] **DATA-086** `P2` Publish stable request and response schemas with explicit field types, nullability, units, and identifier semantics.
- [ ] **DATA-087** `P1` Validate required fields, ranges, enum values, and nested structures at trusted API boundaries.
- [ ] **DATA-088** `P1` Check that errors for invalid data identify affected fields without disclosing protected internal data.
- [ ] **DATA-089** `P1` Enforce tenant, role, and object ownership boundaries for reads, writes, bulk operations, exports, and data searches.
- [ ] **DATA-090** `P1` Prevent mass assignment or unintended field updates by limiting writable fields to the approved contract.
- [ ] **DATA-091** `P2` Document idempotency and deduplication requirements for write operations that may be retried.
- [ ] **DATA-092** `P2` Define concurrency behavior for edits, including version preconditions, conflict responses, and retry guidance.
- [ ] **DATA-093** `P1` Ensure transaction semantics are documented when one API call changes multiple related records.
- [ ] **DATA-094** `P2` Specify pagination and filtering rules that provide stable identity and predictable results across changes.
- [ ] **DATA-095** `P2` Document read-after-write consistency, stale replica behavior, and expected freshness for important endpoints.
- [ ] **DATA-096** `P1` Treat schema evolution and data migration as API compatibility concerns; test old and new clients during rollout.
- [ ] **DATA-097** `P1` Make bulk imports, exports, and background jobs resumable or observable when partial failure is possible.
- [ ] **DATA-098** `P1` Validate API-supplied timestamps, decimal values, localization-sensitive fields, and encoding round trips.
- [ ] **DATA-099** `P1` Ensure sensitive fields are redacted or omitted from logs, API errors, and traces while retaining useful diagnostic context.
- [ ] **DATA-100** `P2` Define rate limits, quotas, and payload-size constraints for expensive data operations.
- [ ] **DATA-101** `P1` Ensure data deletion, correction, and export APIs propagate required lifecycle actions to dependent stores.
- [ ] **DATA-102** `P1` Test API responses for missing data, duplicates, concurrent updates, stale caches, and data-integrity failures.
- [ ] **DATA-103** `P2` Document consumers and deprecation plans before modifying field semantics or removing stored data they depend on.

## Release gate


- [ ] Critical datasets have identified owners, documented data definitions, authoritative sources, and appropriate access/classification boundaries.
- [ ] Schema and migration changes have been reviewed and tested against realistic data volumes and compatible application versions, with a credible path to recovery or remediation.
- [ ] Business-critical invariants, transaction and concurrency guarantees, and data-quality checks have been validated; material discrepancies are reconciled or have accepted remediation plans.
- [ ] Data retention, deletion, and archival controls have documented purposes and responsible owners, including relevant downstream and derived data copies.
- [ ] API and frontend data contracts are consistent with authoritative semantics and remain compatible with the proposed release, where those interfaces exist.
- [ ] Unresolved integrity, schema-change, or lifecycle risks have a named owner, priority, deadline, and authorized disposition recorded outside this shared template.

**Domain-specific approval rule:** Do not approve a release when critical records can be corrupted or silently lost, required migrations lack a safe plan, authoritative data ownership is unresolved, or significant retention and lifecycle risks remain unaccepted. Passing this review does not establish privacy-law compliance, database recoverability, or security certification.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#08_data_and_databasemanagement), not prerequisites or verification evidence.

## Trusted references and scope


The following primary sources inform these practical verification questions. The checks are not direct quotations of standards and do not imply that one data architecture is universally required.

- [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — database-level uniqueness, checks, keys, and referential integrity.
- [PostgreSQL — Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html) — transaction isolation, locking, and consistency under concurrent access.
- [PostgreSQL — Modifying Tables](https://www.postgresql.org/docs/current/ddl-alter.html) — schema evolution and constraint changes.
- [PostgreSQL — ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — schema changes, lock behavior, and constraints in live databases.
- [Microsoft Azure Well-Architected — Data platform considerations](https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-data-platform) — governance, consistency, and schema evolution.
- [Microsoft Azure Well-Architected — Partitioning data](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/partition-data) — partition management, consistency, and lifecycle implications.
- [AWS Well-Architected — Data classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html) — classifications and related data protection/lifecycle decisions.
- [AWS Well-Architected — Data lifecycle management](https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_data_classification_lifecycle_management.html) — handling, retention, transformation, and disposal policy.
- [AWS Well-Architected — Back up data](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/back-up-data.html) — recovery prerequisites for critical data and configurations.
- [UK ICO — Storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/) — personal-data retention and erasure considerations where applicable; guidance is under review.
- [OpenAPI Specification](https://spec.openapis.org/oas/v3.2.1.html) — machine-readable API data contracts when applicable.
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — parameterized queries and safe query structures.
- [PostgreSQL — Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) — isolation and privileged bypass considerations.
- [PostgreSQL — Indexes](https://www.postgresql.org/docs/current/indexes.html) — index design, types, usage and maintenance costs.
- [PostgreSQL — EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) — query plan instrumentation and regressions.
- [PostgreSQL — Client Connection Defaults](https://www.postgresql.org/docs/current/runtime-config-client.html) — query, lock, and idle-transaction timeouts.
- [PostgreSQL — Routine Vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html) — long-lived snapshots and transaction-ID aging.
- [PostgreSQL — Planner Statistics](https://www.postgresql.org/docs/current/planner-stats.html) — selectivity and multicolumn statistics.
- [PostgreSQL — Monitoring Statistics](https://www.postgresql.org/docs/current/monitoring-stats.html) — database performance and replication monitoring.
- [PostgreSQL — Logical Replication Restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html) — limitations of replicated DDL and sequences.
- [PostgreSQL — Continuous Archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) — WAL retention, base backups, and point-in-time recovery.
- [MongoDB — Choose a Shard Key](https://www.mongodb.com/docs/manual/core/sharding-choose-a-shard-key/) — distributed data placement, skew and hot keys.
- [Debezium — Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — atomic event creation and CDC consumers.
- [Microsoft Azure — Hybrid architecture considerations](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/hybrid-considerations) — portability, residency constraints, and disaster recovery planning.

**Applicability:** PostgreSQL-specific constraints and transaction behavior apply only to PostgreSQL or as illustrative relational concepts; verify equivalent capabilities for other engines. The UK ICO source is relevant only where the applicable data-protection framework requires it and is currently under review; do not apply UK-specific duties automatically to other jurisdictions. This checklist does not replace qualified legal, security, or data-architecture review.

**Source review date:** 2026-11-12.
