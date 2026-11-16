# 08 — Data and Database Management Checklist

> Review data ownership, schema design, migration safety, transactional correctness, data quality, and lifecycle management. This checklist covers the integrity and governance of information throughout its use; apply the separate Security, Legal, Reliability, and Performance checklists for their deeper controls.

> **Scope: Frontend-specific.** This file is one part of the 08_Data_and_DatabaseManagement.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Integrity and quality

- [ ] **DATA-044** `P2` Identify and enforce business invariants at an appropriate durable boundary, not only in frontend validation.

## Frontend Checks

- [ ] **DATA-104** `P1` Ensure forms display clear field labels, required status, units, formatting guidance, and acceptable values.
- [ ] **DATA-105** `P1` Validate inputs for prompt feedback while relying on authoritative server-side or database validation for integrity.
- [ ] **DATA-106** `P1` Display field-level and summary error messages that preserve previously entered valid data.
- [ ] **DATA-107** `P1` Distinguish missing, null, zero, empty string, and unavailable values correctly in user interfaces.
- [ ] **DATA-108** `P1` Format dates, times, timezones, numbers, and currencies consistently with the user's locale and the underlying data semantics.
- [ ] **DATA-109** `P1` Prevent accidental duplicate submissions of transactional or high-impact actions and expose completion status.
- [ ] **DATA-110** `P1` Handle concurrent edits or stale versions with meaningful conflict feedback rather than silently overwriting data.
- [ ] **DATA-111** `P1` Communicate unsaved changes, autosave progress, and failed saves before users navigate away or close a workflow.
- [ ] **DATA-112** `P1` Treat server-confirmed state as authoritative when optimistic UI updates fail, and provide a recovery path.
- [ ] **DATA-113** `P1` Show stale or cached data warnings when freshness could materially affect user decisions.
- [ ] **DATA-114** `P1` Preserve stable record identity and selection through pagination, filtering, sorting, and refreshed results.
- [ ] **DATA-115** `P1` Ensure loading, empty, deleted, forbidden, and failed data states are distinguishable and recoverable.
- [ ] **DATA-116** `P1` Do not expose sensitive data in browser storage, URLs, analytics events, or diagnostic output without a documented approved need.
- [ ] **DATA-117** `P1` Clear or partition private client caches appropriately on logout, account switching, or permission changes.
- [ ] **DATA-118** `P1` Check that deleted or corrected records disappear or update in relevant UI views and accessible search results.
- [ ] **DATA-119** `P1` Provide understandable confirmation and progress for data export, correction, or deletion requests when supported.
- [ ] **DATA-120** `P1` Keep imported or uploaded file validation feedback actionable, including rejected rows and partial success.
- [ ] **DATA-121** `P1` Make large tables, filters, and data visualizations understandable to keyboard and assistive-technology users.
- [ ] **DATA-122** `P1` Verify long text, unusual characters, null values, and internationalized content render without corruption or clipping.
- [ ] **DATA-123** `P1` Check user-facing data summaries and totals against authoritative values after refresh or reconciliation.
- [ ] **DATA-156** `P1` For applications using IndexedDB or another versioned local database, test upgrades from every supported schema version, interrupted upgrades, and multi-tab versionchange or blocked-connection handling without silently losing records.
- [ ] **DATA-157** `P1` Test browser-local database quota exhaustion, storage eviction, private-browsing limitations, and denied persistence requests; protect or clearly disclose the risk to unsynchronized user edits.
- [ ] **DATA-158** `P1` For offline-first local databases, verify crash-safe mutation queues, reconnect replay, deduplication, and conflict resolution against server state after prolonged offline or multi-device changes.

## Release gate

- [ ] Critical datasets have identified owners, documented data definitions, authoritative sources, and appropriate access/classification boundaries.
- [ ] Schema and migration changes have been reviewed and tested against realistic data volumes and compatible application versions, with a credible path to recovery or remediation.
- [ ] Business-critical invariants, transaction and concurrency guarantees, and data-quality checks have been validated; material discrepancies are reconciled or have accepted remediation plans.
- [ ] Data retention, deletion, and archival controls have documented purposes and responsible owners, including relevant downstream and derived data copies.
- [ ] API and frontend data contracts are consistent with authoritative semantics and remain compatible with the proposed release, where those interfaces exist.
- [ ] Unresolved integrity, schema-change, or lifecycle risks have a named owner, priority, deadline, and authorized disposition recorded outside this shared template.

**Domain-specific approval rule:** Do not approve a release when critical records can be corrupted or silently lost, required migrations lack a safe plan, authoritative data ownership is unresolved, or significant retention and lifecycle risks remain unaccepted. Passing this review does not establish privacy-law compliance, database recoverability, or security certification.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#08_data_and_databasemanagement), not prerequisites or verification evidence.

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
- [MDN — Using IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) — local database upgrade and transaction behavior.
- [MDN — IndexedDB blocked event](https://developer.mozilla.org/en-US/docs/Web/API/IDBOpenDBRequest/blocked_event) — handling parallel-tab upgrades.
- [MDN — Storage quotas and eviction criteria](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) — eviction and quota failures.
- [MDN — Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API) — offline replay patterns and limited browser support.

**Applicability:** PostgreSQL-specific constraints and transaction behavior apply only to PostgreSQL or as illustrative relational concepts; verify equivalent capabilities for other engines. The UK ICO source is relevant only where the applicable data-protection framework requires it and is currently under review; do not apply UK-specific duties automatically to other jurisdictions. This checklist does not replace qualified legal, security, or data-architecture review.

**Source review date:** 2026-11-12.
