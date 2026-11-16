# 24 — AI Monitoring and Drift Checklist

> Verify that production AI systems are observable, that distribution changes are separated from demonstrated model-quality regressions, and that emerging user harm or operational failures trigger accountable responses. A drift alarm alone does not establish a decline in accuracy, fairness, or safety.

> **Scope: Backend / API-specific.** This file is one part of the 24_AI_Monitoring_and_Drift.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **DRIFT-093** `P1` Emit safe, correlatable request and operation IDs across inference, retrieval, tool calls, and external providers.
- [ ] **DRIFT-094** `P1` Capture the actual serving model and relevant approved configuration revision without exposing internal secrets.
- [ ] **DRIFT-095** `P1` Measure HTTP and provider errors, timeouts, rate limiting, refusal responses, and business validation failures separately.
- [ ] **DRIFT-096** `P1` Instrument streaming time to first chunk, interrupted streams, completion rates, and malformed partial outputs where applicable.
- [ ] **DRIFT-097** `P1` Measure inference token consumption and other billable units consistently with vendor-reported totals when available.
- [ ] **DRIFT-098** `P1` Monitor safe schema and contract failures at API boundaries after model or prompt updates.
- [ ] **DRIFT-099** `P1` Check that tool-call and agent-run telemetry distinguish proposed actions from authoritative completed external effects.
- [ ] **DRIFT-100** `P1` Apply high-cardinality and sensitive-data restrictions to telemetry attributes, sampling, and logs.
- [ ] **DRIFT-101** `P1` Test that instrumentation does not persist private prompts, retrieved documents, access tokens, or protected model output without explicit approval.
- [ ] **DRIFT-102** `P1` Correlate delayed labels and confirmed outcomes to the original prediction or task using stable permitted IDs.
- [ ] **DRIFT-103** `P1` Validate that API monitoring includes fallback routes, canary deployments, batch operations, and retries.
- [ ] **DRIFT-104** `P0` Verify tenant isolation and role-based access for monitoring endpoints, traces, dashboards, and anomaly exports.
- [ ] **DRIFT-105** `P1` Test monitoring behavior when a provider silently changes a model alias or serving version.
- [ ] **DRIFT-106** `P1` Check input validation, response output-format compliance, and authorization signals alongside quality telemetry.
- [ ] **DRIFT-107** `P1` Apply server-enforced cost, quota, and tool-loop limits so alerts are not the only control against runaway spend.
- [ ] **DRIFT-108** `P1` Test whether monitoring survives API deployments, provider outages, queue backlogs, and instrumentation agent restarts.
- [ ] **DRIFT-109** `P1` Expose safe operational health and monitoring-job status without leaking protected model internals.
- [ ] **DRIFT-110** `P1` Ensure alert callbacks or remediation automation require appropriate authentication, authorization, and approval.
- [ ] **DRIFT-111** `P1` Verify that telemetry retention, export, deletion, and geographic processing satisfy the actual data policy.
- [ ] **DRIFT-112** `P1` Include model-specific latency, success, quality, and security signals in production API release checks.

## Release gate

- [ ] Critical AI user journeys, production components, responsible teams, and actual serving model/configuration versions have verifiable monitoring coverage.
- [ ] Availability, error, tail-latency, workload, cost, safety, and high-impact task-quality indicators have approved baselines, thresholds, and accountable escalation paths.
- [ ] Feature input quality, training-serving skew, output changes, and where feasible ground-truth quality are tracked with suitable reference populations, sampling, and freshness controls.
- [ ] Monitoring distinguishes observed distribution drift from confirmed quality degradation, accounts for missing or delayed labels, and identifies unreliable/inconclusive comparisons.
- [ ] Production privacy, security, access, sampling, cardinality, and retention controls protect telemetry, feedback, and evaluation records.
- [ ] Alerts and monitoring-failure detection have been exercised; critical incidents trigger tested containment, human response, emergency disablement, or model rollback as applicable.
- [ ] Relevant API and frontend monitoring detects errors, incomplete/unsafe outputs, user-visible failures, and problematic model or feature-rollout changes.
- [ ] A named risk/release approver has reviewed remaining monitoring blind spots, observation windows, accepted residual risk, and the plan for drift investigation and remediation.

**Domain-specific approval rule:** Block monitoring readiness when serious user harm or unauthorized tool effects cannot be detected or escalated appropriately, monitoring is materially blind on critical workflows, an essential safety guardrail can fail open unnoticed, or required privacy controls for monitored data are absent. Stable feature distributions and passing infrastructure health checks do not certify model quality or the safety of the user experience.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#24_ai_monitoring_and_drift), not prerequisites or verification evidence.

## Trusted references and scope

The following primary and authoritative sources informed the monitoring questions. Vendor-specific services and algorithms are examples rather than universal requirements.

- [NIST AI RMF Playbook — Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) — post-deployment risk monitoring, impact tracking, escalation, and decommissioning.
- [Google Cloud — Model Monitoring overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) — training-serving feature skew, prediction drift, and supported data types.
- [Google Cloud — Monitor feature skew and drift](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/using-model-monitoring) — reference datasets, analysis windows, sampling, alert thresholds, and monitoring jobs.
- [Google Cloud — Feature attribution skew and drift](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/monitor-explainable-ai) — monitoring changes in feature contributions where model explanations are available.
- [Evidently — Data drift](https://docs.evidentlyai.com/metrics/explainer_drift) — reference/current comparison, statistical tests, and missingness limitations.
- [AWS — SageMaker Model Monitor availability change](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-availability-change.html) — legacy-service status, replacement monitoring architectures, delayed labels, and operational considerations.
- [AWS — Model quality monitoring with delayed ground truth](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html) — prediction-to-label joining and quality monitoring in existing SageMaker Model Monitor deployments.
- [Microsoft Foundry — Evaluation of deployed AI applications](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-generative-ai-app) — production conversation and trace evaluation as complements to offline regression.
- [OpenTelemetry — Generative AI semantic conventions (maintained repository)](https://github.com/open-telemetry/semantic-conventions-genai) — GenAI spans, metrics, events, and model/tool metadata; schema and capture rules are version-specific.
- [Google SRE — Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — reliable user-impact indicators, actionable alerts, and error budgets.
- [Prometheus — Alerting best practices](https://prometheus.io/docs/practices/alerting/) — actionable alert names, metadata, and effective incident routing.
- [OpenTelemetry — General metrics semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/) — metric-unit, naming, and cardinality conventions applicable to service telemetry.

**Applicability:** The NIST AI RMF is voluntary guidance. Statistical drift test behavior depends on baseline size, measurement type, missing values, thresholds, and cohort composition; drift may warrant investigation but is not proof of concept drift or degraded ground-truth performance. AWS states SageMaker Model Monitor is no longer open to new customers as of this review; its older model-quality documentation applies to existing deployments, and the availability-change page describes recommended alternatives. Google Cloud feature-skew/drift features depend on supported deployment types and configurations. In 2026, OpenTelemetry GenAI semantic conventions moved to the dedicated `open-telemetry/semantic-conventions-genai` repository; verify schema and instrumentation support before adopting fields. Monitor sensitive content only where approved and avoid exporting raw prompts, protected documents, or personally identifying labels by default.

**Source review date:** 2026-11-12.
