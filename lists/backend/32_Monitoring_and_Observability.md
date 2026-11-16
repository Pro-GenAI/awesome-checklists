# 32 — Monitoring and Observability Checklist

> Verify that critical services and user journeys can be understood through trustworthy telemetry, actionable alerts, service-level measurements, and effective incident investigation. Monitoring systems must also be reliable, proportionate, and privacy-conscious.

> **Scope: Backend / API-specific.** This file is one part of the 32_Monitoring_and_Observability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Telemetry and instrumentation


- [ ] **OBS-001** `P2` Inventory the critical services, infrastructure, data pipelines, background jobs, and user journeys that require observability.
- [ ] **OBS-002** `P2` Assign an accountable owner to the telemetry produced by each service and to its collection and storage pipeline.
- [ ] **OBS-005** `P1` Use stable service, environment, version, and deployment identifiers to support filtering and release comparisons.
- [ ] **OBS-011** `P1` Instrument database, cache, message queue, storage, and third-party calls where they materially affect critical workflows.
- [ ] **OBS-012** `P1` Capture background-job start, completion, failure, retry, and queue-lag signals where asynchronous work is used.
- [ ] **OBS-013** `P1` Measure resource utilization and saturation for compute, memory, disk, connections, and other constrained pools.
- [ ] **OBS-014** `P1` Choose metric labels with controlled cardinality; avoid unbounded user, request, URL, or document identifiers as dimensions.
- [ ] **OBS-016** `P1` Verify telemetry timestamps, time zones, and clock synchronization are sufficient for cross-service investigations.
- [ ] **OBS-018** `P1` Review automatic instrumentation and telemetry schemas for accidental capture of personal data, tokens, credentials, or sensitive request content.
- [ ] **OBS-019** `P1` Configure filtering, redaction, or attribute allowlists before sensitive telemetry enters broadly accessible stores where feasible.
- [ ] **OBS-020** `P1` Secure telemetry ingestion, exports, and collectors with authenticated transport and appropriate privilege boundaries.
- [ ] **OBS-022** `P1` Test telemetry pipeline behavior during backend unavailability, queue saturation, restart, and recovery, including acceptable data-loss assumptions.
- [ ] **OBS-024** `P1` Confirm deployed services emit the expected signals in the actual production environment before treating monitoring as complete.
- [ ] **OBS-006** `P2` Publish structured application logs with consistent timestamps, severity levels, event names, and correlation fields.
- [ ] **OBS-007** `P1` Include enough context in error logs to investigate failures without dumping entire payloads or secrets.
- [ ] **OBS-008** `P1` Propagate trace context across synchronous service boundaries and compatible asynchronous message flows where appropriate.
- [ ] **OBS-009** `P1` Create spans around critical work and downstream calls, identifying bottlenecks and failures without excessive instrumentation.
- [ ] **OBS-010** `P1` Correlate logs with traces through valid trace or span identifiers when supported by the chosen stack.
- [ ] **OBS-015** `P1` Choose trace sampling and metric aggregation that preserve meaningful error and tail-latency visibility within cost limits.
- [ ] **OBS-021** `P1` Monitor collector ingestion, processing failures, queues, export errors, and dropped or delayed data as first-class reliability signals.
- [ ] **OBS-023** `P1` Keep instrumentation, collector configuration, and dashboard queries under reviewable version control where supported.

## Alerting and on-call


- [ ] **OBS-026** `P1` Page primarily on actionable symptoms of user impact rather than every infrastructure event or transient cause.
- [ ] **OBS-037** `P1` Alert when a critical monitoring target disappears or the telemetry pipeline stops delivering expected data.
- [ ] **OBS-038** `P1` Distinguish missing or stale telemetry from a healthy zero value in relevant alerts and dashboards.

## Service-level indicators and objectives


- [ ] **OBS-047** `P1` Select indicators that reflect actual user experience instead of relying only on server or instance uptime.
- [ ] **OBS-048** `P1` Measure successful and failed request latency separately where error responses could distort normal latency distributions.
- [ ] **OBS-053** `P1` Use synthetic or external probes for critical endpoints or journeys when internal telemetry could miss a total outage.
- [ ] **OBS-056** `P1` Evaluate multi-window or burn-rate alerts for SLO exhaustion where request volume supports reliable calculations.
- [ ] **OBS-058** `P1` Validate monitoring queries and dashboard aggregations against known examples, raw samples, or controlled failures.

## Incident investigation and learning


- [ ] **OBS-066** `P1` Correlate deploys, configuration changes, infrastructure events, and feature-flag updates with changing service health.
- [ ] **OBS-067** `P1` Provide reliable access to production observability for authorized responders, including suitable emergency access procedures.

## API Checks


- [ ] **OBS-082** `P1` Instrument each critical API route or operation with request rate, latency distributions, and error counts.
- [ ] **OBS-083** `P1` Distinguish server failures, expected client errors, authentication failures, and throttling in API dashboards.
- [ ] **OBS-084** `P1` Tag operations using stable route templates or endpoint identifiers instead of raw, high-cardinality URL paths.
- [ ] **OBS-085** `P1` Capture service version, deployment environment, and dependency identity to support regression investigations.
- [ ] **OBS-086** `P1` Propagate trace context through API gateways, application handlers, downstream calls, and compatible message consumers.
- [ ] **OBS-087** `P1` Correlate a safe request identifier between API error responses, server logs, and tracing where appropriate.
- [ ] **OBS-088** `P2` Record upstream and downstream dependency latency, failures, retries, timeouts, and circuit-breaker events.
- [ ] **OBS-089** `P1` Monitor database-query and connection-pool metrics when API performance or reliability depends on them.
- [ ] **OBS-090** `P1` Observe async API jobs, queues, webhook delivery, consumer lag, and dead-letter volume where applicable.
- [ ] **OBS-091** `P1` Capture API authorization and security-relevant events through access-controlled logs without disclosing credentials or sensitive payloads.
- [ ] **OBS-092** `P1` Use rate-limit and quota metrics to distinguish intended throttling from widespread overload or abuse.
- [ ] **OBS-093** `P1` Monitor request and response size distributions where payload growth could impair availability.
- [ ] **OBS-094** `P1` Test that long-running streams and bidirectional protocols emit meaningful connection, cancellation, and failure signals.
- [ ] **OBS-095** `P1` Make SLI queries distinguish critical routes and consumer groups without excessive label cardinality.
- [ ] **OBS-096** `P1` Verify telemetry for API validation, not-found, conflict, and degraded-dependency outcomes is interpretable.
- [ ] **OBS-097** `P1` Check API traces and logs during a staged failure or controlled test to confirm correct causal relationships.
- [ ] **OBS-098** `P2` Document expected status codes and failure semantics before defining alert rules to avoid paging on normal behavior.
- [ ] **OBS-099** `P1` Keep API instrumentation overhead bounded and confirm failure of exporters does not disable core requests.
- [ ] **OBS-100** `P1` Ensure outbound telemetry strips secrets and personal fields that may appear in headers, query strings, and bodies.

## Release gate


- [ ] Critical user journeys and dependent services have identifiable monitoring owners, useful health indicators, and working observability access.
- [ ] Service-level objectives or other accepted reliability expectations have clearly defined measurement and incident-detection methods where applicable.
- [ ] Meaningful user-impact alerts reach appropriate responders; alert routing, escalation, and at least one representative trigger have been tested.
- [ ] Logs, metrics, traces, and dashboard views needed to investigate a critical failure are usable, correlated where necessary, and tagged with the deployed version or environment.
- [ ] Telemetry pipelines report their own health or absence of data, and logging/monitoring does not expose prohibited sensitive information.
- [ ] API and frontend error, latency, and critical-journey indicators are reviewed where those interfaces exist, including known collection and sampling limits.
- [ ] Incident response roles, escalation procedures, relevant runbooks, and unresolved observability gaps have accountable owners and authorized dispositions in project-specific records.

**Domain-specific approval rule:** Block monitoring sign-off if a critical user-impacting failure cannot reasonably be detected or investigated, required alerts do not reach responders, monitoring is materially blind without accepted mitigation, or sensitive telemetry exposure remains unresolved. Dashboard existence alone does not establish production observability.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#32_monitoring_and_observability), not prerequisites or verification evidence.

## Trusted references and scope


These checks translate authoritative observability and operations guidance into practical verification tasks. They do not mandate a specific vendor, instrumentation SDK, or SLO target.

- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/) — core telemetry concepts and selecting logs, metrics, and traces.
- [OpenTelemetry — Semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) — consistent operation, resource, metric, log, and trace attributes.
- [OpenTelemetry — Logs](https://opentelemetry.io/docs/concepts/signals/logs/) — structured logging, stable schema, and correlation.
- [OpenTelemetry — Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/) — data minimization, redaction, and telemetry privacy.
- [OpenTelemetry — Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/) — telemetry queueing, exporter failures, and data-loss controls.
- [Google SRE — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — four golden signals and symptom-driven monitoring.
- [Google SRE Workbook — Monitoring](https://sre.google/workbook/monitoring/) — service and dependency signals and operational dashboards.
- [Google SRE Workbook — Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — error-budget and multi-window burn-rate alerting.
- [Google SRE Workbook — Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — blameless incident learning and follow-up ownership.
- [Prometheus — Alerting best practices](https://prometheus.io/docs/practices/alerting/) — actionable, user-impact-focused alerts and monitoring of monitoring.
- [Prometheus — Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) — alerting thresholds, pending durations, labels, and annotations.
- [Grafana — Alerting best practices](https://grafana.com/docs/grafana/latest/alerting/guides/best-practices/) — routing, severity, useful alerts, and alert noise management.
- [web.dev — Web Vitals](https://web.dev/articles/vitals) — client-side loading, interactivity, and layout stability metrics.

**Applicability:** Monitoring requirements depend on the service's criticality, traffic, architecture, user population, jurisdiction, and available operational coverage. Tracing across distributed services, browser Web Vitals, SLO burn-rate paging, and OpenTelemetry Collector configuration are conditional, not universal. Sample size and low-traffic behavior must be considered before configuring percentage-based alerts. Keep sensitive personal, financial, health, and credential data out of broadly visible telemetry.

**Source review date:** 2026-11-12.
