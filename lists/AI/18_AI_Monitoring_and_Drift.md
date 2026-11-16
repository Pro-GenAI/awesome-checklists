# 18 — AI Monitoring and Drift Checklist

> Verify that production AI systems are observable, that distribution changes are separated from demonstrated model-quality regressions, and that emerging user harm or operational failures trigger accountable responses. A drift alarm alone does not establish a decline in accuracy, fairness, or safety.

> **Scope: AI-specific.** This file is one part of the 18_AI_Monitoring_and_Drift.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Production performance signals

- [ ] **DRIFT-001** `P2` Define the monitored AI task, served model or provider, intended users, and accountable production monitoring owner.
- [ ] **DRIFT-002** `P2` Map every inference path, retrieval service, tool call, batch job, streaming endpoint, and fallback path that can affect user outcomes.
- [ ] **DRIFT-003** `P1` Establish pre-release baselines for task completion, policy/safety failures, model errors, latency, throughput, and resource cost.
- [ ] **DRIFT-004** `P1` Set availability and responsiveness objectives for the AI-powered user journey rather than only the underlying model endpoint.
- [ ] **DRIFT-005** `P1` Measure request success, model refusal, guardrail block, incomplete response, timeout, and canceled operation as distinct outcomes.
- [ ] **DRIFT-006** `P2` Record model, prompt, retrieval, tool, evaluator, and safety-policy revisions with approved low-cardinality identifiers.
- [ ] **DRIFT-007** `P1` Trace a representative request through orchestration, inference, retrieval, tool execution, and any human-approval step.
- [ ] **DRIFT-008** `P1` Monitor end-to-end latency, model service latency, time to first output, streaming duration, and queue or batch processing delays.
- [ ] **DRIFT-009** `P2` Track p50, p95, and p99 latency under normal, peak, and degraded traffic with meaningful sample counts.
- [ ] **DRIFT-010** `P1` Monitor request, token, batch, image, audio, or other billable usage consistent with the actual provider pricing model.
- [ ] **DRIFT-011** `P2` Track provider quotas, rate limiting, timeouts, transient errors, model loading, cold starts, and failover events.
- [ ] **DRIFT-012** `P1` Measure CPU, GPU, accelerator memory, cache, retrieval index, storage, and queue saturation for self-hosted components where applicable.
- [ ] **DRIFT-013** `P1` Monitor the share of traffic handled by each active model, experiment, region, tenant category, and rollout cohort where permitted.
- [ ] **DRIFT-014** `P1` Verify that online and batch inference monitoring report job completion, failed records, retry counts, and data freshness.
- [ ] **DRIFT-015** `P1` Set sampling and telemetry completeness targets so measured behavior remains representative without collecting prohibited data.
- [ ] **DRIFT-016** `P1` Detect missing tracing spans, dropped metrics, pipeline outages, and failed dashboard refreshes independently of actual model health.
- [ ] **DRIFT-017** `P1` Validate that request identifiers enable incident correlation without exposing user identity, prompts, credentials, or private outputs by default.
- [ ] **DRIFT-018** `P1` Review metric-label cardinality and retention costs before adding tenant IDs, document IDs, prompts, or other high-cardinality attributes.
- [ ] **DRIFT-019** `P2` Define operational runbooks for provider outages, inference overload, guardrail failure, and model-specific latency regression.
- [ ] **DRIFT-020** `P1` Compare actual deployed model/configuration versions with the approved release manifest and detect unexpected alias changes.
- [ ] **DRIFT-021** `P1` Test monitoring under partial provider failure, network partition, canary rollback, and simultaneous model versions.
- [ ] **DRIFT-022** `P2` Document telemetry ownership, storage locations, access controls, deletion obligations, and time synchronization.

## Input and output drift

- [ ] **DRIFT-023** `P1` Distinguish training-serving skew, input distribution drift, output distribution drift, and concept or relationship drift in monitoring definitions.
- [ ] **DRIFT-024** `P1` Choose a relevant reference window or training baseline for each feature, model, population, and deployment context.
- [ ] **DRIFT-025** `P2` Record baseline dataset version, data transformations, feature schema, time period, and population composition.
- [ ] **DRIFT-026** `P2` Define feature- and task-specific drift tests suited to numerical, categorical, text, image, embedding, or other applicable data.
- [ ] **DRIFT-027** `P2` Specify drift thresholds, comparison windows, minimum sample counts, and investigation criteria before reviewing alerts.
- [ ] **DRIFT-028** `P1` Test how chosen drift statistics behave with small samples, sparse categories, missing values, and changing class prevalence.
- [ ] **DRIFT-029** `P1` Monitor missingness, unexpected nulls, schema changes, type violations, outliers, and feature ranges separately from statistical drift.
- [ ] **DRIFT-030** `P1` Check that production feature extraction matches the approved training or evaluation preprocessing steps.
- [ ] **DRIFT-031** `P2` Track shifts in input languages, prompt length, document categories, modalities, user cohorts, and request complexity where relevant and lawful.
- [ ] **DRIFT-032** `P1` Distinguish legitimate seasonality, campaigns, product rollouts, and market changes from unexpected distribution shifts.
- [ ] **DRIFT-033** `P1` Monitor output-class frequencies, confidence-score distributions, refusal rates, answer lengths, and response formats where meaningful.
- [ ] **DRIFT-034** `P1` Detect new or unexpected labels, hallucination patterns, tool-use decisions, citation types, and guardrail outputs for relevant AI applications.
- [ ] **DRIFT-035** `P1` Evaluate embedding or semantic drift with task-specific reference data rather than assuming vector distance directly measures accuracy.
- [ ] **DRIFT-036** `P1` Monitor retrieval index version, source freshness, coverage, ranking quality, and source deletion propagation for RAG workloads.
- [ ] **DRIFT-037** `P1` Compare feature attribution or explanation patterns where supported and appropriately validated, noting attribution changes are not proof of causality.
- [ ] **DRIFT-038** `P1` Evaluate drift separately for justified subpopulations and languages, subject to data rights and minimum cohort-size safeguards.
- [ ] **DRIFT-039** `P1` Investigate whether observed shift results from upstream collection bugs, missing identifiers, schema changes, or provider-model updates.
- [ ] **DRIFT-040** `P1` Keep production and reference data comparable in units, time zones, filtering, data quality, and sampling rules.
- [ ] **DRIFT-041** `P1` Test monitoring pipelines against known synthetic shifts and non-drift controls to establish alert sensitivity and false-positive behavior.
- [ ] **DRIFT-042** `P2` Record changes in label-availability windows and account for delayed or biased ground truth before inferring quality trends.
- [ ] **DRIFT-043** `P1` Use independent outcome or adjudicated labels to confirm actual model-quality degradation where the task makes them available.
- [ ] **DRIFT-044** `P2` Document cases where labels are unavailable and clearly mark distribution and proxy metrics as indirect evidence.
- [ ] **DRIFT-045** `P1` Set rebaselining approval rules so a degraded new distribution is not silently accepted as healthy.
- [ ] **DRIFT-046** `P1` Version drift reports and baseline changes so regressions can be traced across model, data, and workflow releases.

## Quality, cost, and failure trends

- [ ] **DRIFT-047** `P2` Define ongoing task-quality measures that connect model outputs to real user outcomes and high-impact failure categories.
- [ ] **DRIFT-048** `P1` Establish how delayed ground-truth labels are collected, joined to predictions, validated, and protected.
- [ ] **DRIFT-049** `P1` Measure label delay, missing outcomes, selective feedback, and survivorship bias before interpreting production accuracy estimates.
- [ ] **DRIFT-050** `P1` Run periodic representative offline or shadow evaluations against recent authorized production-like cases.
- [ ] **DRIFT-051** `P1` Compare current task-quality results against approved baseline and previous production model revisions.
- [ ] **DRIFT-052** `P2` Track RAG groundedness, evidence relevance, citation support, abstention, and no-answer outcomes independently where RAG is used.
- [ ] **DRIFT-053** `P2` Track agent task completion against confirmed tool state, including unauthorized or duplicate side effects, where agents are used.
- [ ] **DRIFT-054** `P1` Monitor policy refusal accuracy and legitimate-task false blocks separately from true unsafe-content passes.
- [ ] **DRIFT-055** `P1` Monitor severe errors as separately actionable events even if average model-quality metrics remain stable.
- [ ] **DRIFT-056** `P1` Watch for model output schema violations, invalid tool arguments, parsing failures, and downstream contract regressions.
- [ ] **DRIFT-057** `P1` Measure relevant subgroup, language, region, and accessibility impacts without drawing conclusions from inadequate samples or unlawful sensitive-data collection.
- [ ] **DRIFT-058** `P1` Compare user-reported harmful or incorrect outputs with evaluator findings and investigate disagreement.
- [ ] **DRIFT-059** `P1` Check for benchmark or evaluator drift after judge model, policy, rubric, or evaluation data changes.
- [ ] **DRIFT-060** `P2` Track prompt, input, output, cache, reasoning, and other metered token categories according to supported provider usage data.
- [ ] **DRIFT-061** `P1` Report cost per successful task and failed/canceled-task costs rather than only aggregate inference spend.
- [ ] **DRIFT-062** `P1` Detect anomalous token growth, recursive agent loops, excessive retries, repeated retrieval, and unnecessary tool fan-out.
- [ ] **DRIFT-063** `P1` Monitor differences in quality, latency, and cost between baseline, canary, and fallback models by comparable traffic segments.
- [ ] **DRIFT-064** `P1` Separate infrastructure outages, provider throttling, input errors, safety blocks, and quality regressions in incident dashboards.
- [ ] **DRIFT-065** `P1` Set review rules for low-volume but high-consequence harms that do not produce reliable aggregate-rate alarms.
- [ ] **DRIFT-066** `P1` Review whether changing demographics or input tasks invalidate historical baselines or evaluation coverage.
- [ ] **DRIFT-067** `P2` Track temporal performance trends and business outcomes with explicit metric definitions and known measurement limitations.
- [ ] **DRIFT-068** `P1` Require investigation and owner sign-off before using drift or quality signals to trigger retraining, model switching, or other material action.
- [ ] **DRIFT-069** `P1` Do not infer fairness, safety, or factual correctness solely from a stable input feature distribution.
- [ ] **DRIFT-070** `P2` Document how production incidents and verified failures become sanitized, versioned regression-evaluation cases.

## Alerts and feedback loops

- [ ] **DRIFT-071** `P2` Assign owners, severity, escalation contacts, and response windows for monitoring coverage and material AI risks.
- [ ] **DRIFT-072** `P2` Define actionable alert thresholds for availability, response latency, critical failure rates, quality and drift, and cost exposure.
- [ ] **DRIFT-073** `P1` Separate immediate page-worthy user harm or service loss from trend investigation and routine analytical review.
- [ ] **DRIFT-074** `P1` Require alerts to identify affected model versions, cohorts, services, time window, and available investigation context.
- [ ] **DRIFT-075** `P1` Set minimum sample counts, aggregation windows, and hysteresis or persistence rules to reduce alert noise.
- [ ] **DRIFT-076** `P1` Test that alerts fire on controlled latency, drift, invalid-schema, guardrail, and provider-failure scenarios.
- [ ] **DRIFT-077** `P1` Detect failed monitoring jobs, absent metrics, stale baselines, and dropped telemetry so lack of alerts is not mistaken for health.
- [ ] **DRIFT-078** `P2` Document a triage procedure to distinguish true model drift from pipeline defects, seasonal traffic, and insufficient data.
- [ ] **DRIFT-079** `P2` Define containment options including rollout freeze, feature disablement, provider switch, model rollback, and human-only fallback.
- [ ] **DRIFT-080** `P1` Test emergency shutdown and rollback after unsafe generation, unexpected tool actions, or confirmed protected-data leakage.
- [ ] **DRIFT-081** `P1` Keep a responsible human approval gate for automated retraining or promotion when risk policy requires it.
- [ ] **DRIFT-082** `P2` Define severity-based communication plans for customer support, security, product, compliance, and relevant external stakeholders.
- [ ] **DRIFT-083** `P1` Provide approved feedback intake channels for harmful, inaccurate, discriminatory, or frustrating AI outcomes.
- [ ] **DRIFT-084** `P1` Validate feedback labeling, review sampling, complaint escalation, and protected-data handling before operational use.
- [ ] **DRIFT-085** `P1` Review false positive alerts and false negative incidents periodically and adjust thresholds with documented rationale.
- [ ] **DRIFT-086** `P2` Record actual negative impacts, near misses, root-cause hypotheses, mitigations, owners, and retest evidence in incident records.
- [ ] **DRIFT-087** `P1` Use canary and experiment guardrails to halt traffic growth when observed user harm or severe regression exceeds approved thresholds.
- [ ] **DRIFT-088** `P1` Schedule recurring post-deployment quality reviews including fairness, privacy, security, robustness, and user value as applicable.
- [ ] **DRIFT-089** `P1` Review alert routing and coverage after staffing, vendor, model, telemetry, or supported-market changes.
- [ ] **DRIFT-090** `P1` Ensure owner dashboards and escalation runbooks remain accessible during a telemetry platform or cloud-provider outage.
- [ ] **DRIFT-091** `P1` Retain reviewable history of alert acknowledgments, corrective actions, approved rebaselines, and lifecycle decisions.
- [ ] **DRIFT-092** `P2` Define decommissioning criteria for models whose residual performance or safety risk exceeds approved tolerance.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **DRIFT-113** `P1` Measure actual AI user-task success and failure indicators from supported frontend journeys rather than only server response codes.
- [ ] **DRIFT-114** `P1` Distinguish user-visible model refusal, uncertainty, partial answer, timeout, and completed task in frontend telemetry.
- [ ] **DRIFT-115** `P2` Track perceived time to first meaningful content and completed response time for streaming AI interfaces.
- [ ] **DRIFT-116** `P1` Test how model output errors, missing citations, invalid structure, and tool failures surface to users.
- [ ] **DRIFT-117** `P1` Keep client error and performance telemetry tied to approved feature/model versions without transmitting unnecessary prompt content.
- [ ] **DRIFT-118** `P1` Provide a usable way to flag harmful, inaccurate, unsupported, or outdated answers where the product supports direct user interaction.
- [ ] **DRIFT-119** `P1` Ensure feedback reports are routed to trained human reviewers and not silently treated as verified ground truth.
- [ ] **DRIFT-120** `P1` Explain optional analytics and data collection purposes, and honor applicable consent or preference controls.
- [ ] **DRIFT-121** `P1` Protect sensitive user input, retrieved passages, conversation history, and feedback from accidental browser logging or third-party analytics.
- [ ] **DRIFT-122** `P1` Test keyboard and screen-reader status announcements for dynamic AI output and error states.
- [ ] **DRIFT-123** `P1` Monitor AI frontend failures across supported browsers, devices, network conditions, and languages with meaningful cohorts.
- [ ] **DRIFT-124** `P1` Check that localized errors, refusers, and human escalation links remain understandable after model changes.
- [ ] **DRIFT-125** `P1` Ensure a frozen, rejected, or blocked AI task is not visually presented as successfully completed.
- [ ] **DRIFT-126** `P1` Test feature-flag canaries, experiment groups, and old cached clients for correct model-response and telemetry association.
- [ ] **DRIFT-127** `P1` Check that changing or disabling a model cannot surface another user's cached answers or previously authorized tools.
- [ ] **DRIFT-128** `P1` Monitor abandoned AI interactions and repeated retries while avoiding unjustified claims about their underlying causes.
- [ ] **DRIFT-129** `P1` Provide appropriate safe recovery after failed requests and clarify when an external action may have already occurred.
- [ ] **DRIFT-130** `P1` Review qualitative user studies and support complaints alongside quantitative model and interface metrics.
- [ ] **DRIFT-131** `P1` Confirm user-facing notices and explanations match the deployed model/provider capabilities and known limitations.
- [ ] **DRIFT-132** `P1` Verify regression-alert investigation can identify the relevant frontend version, model revision, and affected user journey.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#18_ai_monitoring_and_drift), not prerequisites or evidence of PASS.

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
