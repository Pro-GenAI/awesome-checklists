# 12 — Monitoring and Observability Checklist

> Verify that critical services and user journeys can be understood through trustworthy telemetry, actionable alerts, service-level measurements, and effective incident investigation. Monitoring systems must also be reliable, proportionate, and privacy-conscious.

> **Scope: Shared / cross-cutting.** This file is one part of the 12_Monitoring_and_Observability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Telemetry and instrumentation


- [ ] **OBS-003** `P1` Instrument user-relevant latency, traffic, error, and saturation signals for critical operations.
- [ ] **OBS-004** `P2` Define consistent metric names, descriptions, units, event types, and attributes so data from related components is comparable.

- [ ] **OBS-017** `P1` Set retention, access, encryption, and deletion rules for logs, metrics, traces, and incident records based on risk and applicable obligations.

## Alerting and on-call


- [ ] **OBS-025** `P2` Define on-call coverage, escalation contacts, and response ownership for every business-critical service.
- [ ] **OBS-027** `P2` Define alert severity using expected customer impact, urgency, and required response time.
- [ ] **OBS-028** `P1` Create useful alert descriptions containing affected service, symptom, threshold, time window, and supporting evidence.
- [ ] **OBS-029** `P1` Link alerts to current dashboards, service ownership, and an appropriate remediation or investigation runbook.
- [ ] **OBS-030** `P1` Separate immediate paging alerts from non-urgent tickets, informational notifications, and trend reports.
- [ ] **OBS-031** `P1` Use suitable pending periods, hysteresis, or grouping to reduce transient alert flapping without hiding sustained incidents.
- [ ] **OBS-032** `P1` Deduplicate and correlate related alerts so a single dependency failure does not flood responders with redundant pages.
- [ ] **OBS-033** `P1` Configure silencing, maintenance windows, and inhibition rules with explicit ownership and expiry where supported.
- [ ] **OBS-034** `P2` Define alert routing for business hours, overnight coverage, regional ownership, and emergency fallback.
- [ ] **OBS-035** `P1` Test that alerts actually reach the intended responder through the configured notification path.
- [ ] **OBS-036** `P1` Exercise escalation when the primary responder is unavailable or an alert remains unacknowledged.
- [ ] **OBS-039** `P1` Test representative failure scenarios and verify the associated alerts fire at a useful time and severity.
- [ ] **OBS-040** `P1` Review false positives, missed incidents, repeated noisy rules, and response workload on a regular cadence.
- [ ] **OBS-041** `P1` Ensure critical alert thresholds are related to approved service objectives or demonstrated risk, rather than arbitrary defaults.
- [ ] **OBS-042** `P2` Document how responders can manually declare an incident when monitoring has not yet detected the problem.
- [ ] **OBS-043** `P1` Check that alert routing and contact information remain correct after team or ownership changes.
- [ ] **OBS-044** `P1` Retire obsolete alerts and dashboards when services, dependencies, or metrics are removed.

## Service-level indicators and objectives


- [ ] **OBS-045** `P2` Identify user-visible services and critical transactions that deserve explicit reliability indicators.
- [ ] **OBS-046** `P2` Define each service-level indicator (SLI) with a precise numerator, denominator, scope, exclusions, and measurement source.
- [ ] **OBS-049** `P1` Include traffic, errors, latency, and saturation views for services where those signals are meaningful.
- [ ] **OBS-050** `P1` Set service-level objectives (SLOs) and evaluation windows that match risk, user expectations, and operational capacity.
- [ ] **OBS-051** `P2` Document whether planned maintenance and dependency failures count against SLOs and customer commitments.
- [ ] **OBS-052** `P1` Ensure availability measurements include sufficiently representative traffic and account for low-volume services.
- [ ] **OBS-054** `P2` Track percentile latency and error behavior by relevant service, operation, region, or user segment where justified.
- [ ] **OBS-055** `P1` Make error-budget remaining and consumption trends visible to service owners when error budgets are used.
- [ ] **OBS-057** `P1` Use low-traffic-appropriate detection methods rather than applying high-volume percentage alerts blindly.

- [ ] **OBS-059** `P1` Distinguish service objectives from individual release performance tests and contractual service-level agreements.
- [ ] **OBS-060** `P1` Ensure dashboards communicate metric units, time ranges, target thresholds, freshness, and known caveats.
- [ ] **OBS-061** `P1` Review SLI and SLO relevance after changes to user journeys, traffic mix, product boundaries, or business commitments.
- [ ] **OBS-062** `P2` Assign owners and review schedules for service objective definitions, measurement quality, and unresolved gaps.

## Incident investigation and learning


- [ ] **OBS-063** `P2` Document incident severity definitions, response roles, communications channels, and escalation conditions.
- [ ] **OBS-064** `P1` Make relevant dashboards, trace search, structured logs, runbooks, and dependency maps discoverable from incident entry points.
- [ ] **OBS-065** `P1` Include a consistent incident identifier or timeline record across alerts, communications, changes, and remediation.
- [ ] **OBS-068** `P1` Validate that responders can traverse from a failed user action to its service requests, dependencies, and error context where feasible.
- [ ] **OBS-069** `P1` Preserve enough diagnostic history to investigate intermittent problems that are discovered after the event.
- [ ] **OBS-070** `P2` Record incident detection time, user impact, affected scope, mitigation actions, and recovery verification.
- [ ] **OBS-071** `P1` Distinguish triggering events, contributing conditions, and systemic weaknesses when analyzing causes.
- [ ] **OBS-072** `P1` Prefer blameless, evidence-based incident reviews over unsupported attribution to individuals.
- [ ] **OBS-073** `P2` Define which incidents require a written postmortem and when the review should occur.
- [ ] **OBS-074** `P1` Capture actions that reduced impact as well as detection gaps, slow investigations, and failed mitigations.
- [ ] **OBS-075** `P2` Assign postmortem follow-up actions owners, priorities, tracking references, and observable completion criteria.
- [ ] **OBS-076** `P1` Verify incident follow-ups are completed and that relevant alerts, tests, dashboards, and runbooks are updated.
- [ ] **OBS-077** `P1` Periodically analyze recurring incident patterns and alert fatigue to identify broader reliability risks.
- [ ] **OBS-078** `P1` Exercise a simulated incident to verify dashboard access, escalation, communication, and diagnosis without harming production.
- [ ] **OBS-079** `P1` Make status updates and customer-facing communications reflect confirmed impact rather than inferred internal health.
- [ ] **OBS-080** `P1` Review incident evidence retention and access controls for confidentiality and applicable policy requirements.
- [ ] **OBS-081** `P1` Keep documented operational handoffs current across on-call changes, teams, and vendor responsibilities.

## Release gate


- [ ] Critical user journeys and dependent services have identifiable monitoring owners, useful health indicators, and working observability access.
- [ ] Service-level objectives or other accepted reliability expectations have clearly defined measurement and incident-detection methods where applicable.
- [ ] Meaningful user-impact alerts reach appropriate responders; alert routing, escalation, and at least one representative trigger have been tested.
- [ ] Logs, metrics, traces, and dashboard views needed to investigate a critical failure are usable, correlated where necessary, and tagged with the deployed version or environment.
- [ ] Telemetry pipelines report their own health or absence of data, and logging/monitoring does not expose prohibited sensitive information.
- [ ] API and frontend error, latency, and critical-journey indicators are reviewed where those interfaces exist, including known collection and sampling limits.
- [ ] Incident response roles, escalation procedures, relevant runbooks, and unresolved observability gaps have accountable owners and authorized dispositions in project-specific records.

**Domain-specific approval rule:** Block monitoring sign-off if a critical user-impacting failure cannot reasonably be detected or investigated, required alerts do not reach responders, monitoring is materially blind without accepted mitigation, or sensitive telemetry exposure remains unresolved. Dashboard existence alone does not establish production observability.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#12_monitoring_and_observability), not prerequisites or verification evidence.

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
