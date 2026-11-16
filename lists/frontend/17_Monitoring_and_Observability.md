# 17 — Monitoring and Observability Checklist

> Verify that critical services and user journeys can be understood through trustworthy telemetry, actionable alerts, service-level measurements, and effective incident investigation. Monitoring systems must also be reliable, proportionate, and privacy-conscious.

> **Scope: Frontend-specific.** This file is one part of the 17_Monitoring_and_Observability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **OBS-101** `P1` Capture real-user loading and interaction indicators for representative routes and supported device classes where appropriate.
- [ ] **OBS-102** `P1` Measure applicable Core Web Vitals (LCP, INP, CLS) with sufficient context to separate important page types and user cohorts.
- [ ] **OBS-103** `P2` Track JavaScript exceptions and unhandled promise rejections with release identifiers and useful non-sensitive stack information.
- [ ] **OBS-104** `P1` Correlate frontend error reports with backend request or trace identifiers without exposing sensitive internal context.
- [ ] **OBS-105** `P2` Record critical journey failures and completion outcomes that indicate user impact rather than only page views.
- [ ] **OBS-106** `P1` Monitor API call failure rates and user-visible timeouts from the client perspective in addition to server-side metrics.
- [ ] **OBS-107** `P2` Identify navigation or rendering failures introduced by CDN, edge cache, service workers, or stale asset versions.
- [ ] **OBS-108** `P1` Monitor major variations in client performance across connection types, device capabilities, and browser families where sample sizes support them.
- [ ] **OBS-109** `P1` Associate frontend telemetry with specific deployed versions and feature flags to detect release regressions.
- [ ] **OBS-110** `P1` Configure source-map handling and access so diagnosis is possible without unintentionally exposing private source or secrets.
- [ ] **OBS-111** `P1` Use consent-aware, privacy-conscious instrumentation and respect applicable collection restrictions.
- [ ] **OBS-112** `P1` Exclude credentials, personal form content, authentication tokens, and sensitive URL parameters from client error and analytics reports.
- [ ] **OBS-113** `P1` Protect telemetry endpoints against uncontrolled event floods, duplicate reports, and unbounded payload size.
- [ ] **OBS-114** `P1` Bound frontend instrumentation CPU, memory, network, and battery impact and validate overhead under representative conditions.
- [ ] **OBS-115** `P1` Check that client-side sampling preserves visibility into critical errors and does not turn rare failures invisible.
- [ ] **OBS-116** `P2` Define alerting or triage thresholds for widespread client crashes, broken critical workflows, or severe page regressions.
- [ ] **OBS-117** `P1` Test error capture for routed applications, hydration failures, resource load failures, and error boundaries when relevant.
- [ ] **OBS-118** `P1` Ensure frontend monitoring does not block form submission, navigation, accessibility interactions, or offline recovery when telemetry fails.
- [ ] **OBS-119** `P1` Provide an understandable manual problem-reporting route for users when automatic detection misses issues.

## Release gate

- [ ] Critical user journeys and dependent services have identifiable monitoring owners, useful health indicators, and working observability access.
- [ ] Service-level objectives or other accepted reliability expectations have clearly defined measurement and incident-detection methods where applicable.
- [ ] Meaningful user-impact alerts reach appropriate responders; alert routing, escalation, and at least one representative trigger have been tested.
- [ ] Logs, metrics, traces, and dashboard views needed to investigate a critical failure are usable, correlated where necessary, and tagged with the deployed version or environment.
- [ ] Telemetry pipelines report their own health or absence of data, and logging/monitoring does not expose prohibited sensitive information.
- [ ] API and frontend error, latency, and critical-journey indicators are reviewed where those interfaces exist, including known collection and sampling limits.
- [ ] Incident response roles, escalation procedures, relevant runbooks, and unresolved observability gaps have accountable owners and authorized dispositions in project-specific records.

**Domain-specific approval rule:** Block monitoring sign-off if a critical user-impacting failure cannot reasonably be detected or investigated, required alerts do not reach responders, monitoring is materially blind without accepted mitigation, or sensitive telemetry exposure remains unresolved. Dashboard existence alone does not establish production observability.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#17_monitoring_and_observability), not prerequisites or verification evidence.

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
