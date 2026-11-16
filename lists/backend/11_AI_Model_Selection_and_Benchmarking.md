# 11 — AI Model Selection and Benchmarking Checklist

> Choose AI models against the actual application workload, operating constraints, safety requirements, and measurable outcomes. Public leaderboards help identify candidates but do not prove suitability, compliance, or reliability for a particular deployment.

> **Scope: Backend / API-specific.** This file is one part of the 11_AI_Model_Selection_and_Benchmarking.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **MODELS-095** `P1` Confirm the selected model supports the API's required input modalities, message roles, schemas, and response modes.
- [ ] **MODELS-096** `P1` Validate context budgeting and truncation behavior against the application’s actual request distributions.
- [ ] **MODELS-097** `P1` Check that model aliases or routing configurations resolve to approved revisions and detect unauthorized silent substitutions.
- [ ] **MODELS-098** `P1` Test structured output and function-call schemas against the real provider endpoint and production-equivalent configuration.
- [ ] **MODELS-099** `P1` Measure p50, p95, and p99 request latency and error rates under realistic API concurrency and quota conditions.
- [ ] **MODELS-100** `P1` Measure time-to-first-token and streaming completion behavior where clients use streaming.
- [ ] **MODELS-101** `P1` Check rate-limit, timeout, backoff, idempotency, and retry behavior without allowing runaway cost or duplicate actions.
- [ ] **MODELS-102** `P1` Validate token usage and other metered inference charges against provider responses or approved estimates.
- [ ] **MODELS-103** `P1` Ensure inference input, stored prompts, and response logs honor provider and internal retention/data-use restrictions.
- [ ] **MODELS-104** `P1` Check provider authentication, deployment regions, permissions, and customer-data isolation for the chosen model.
- [ ] **MODELS-105** `P1` Benchmark actual API request/response payloads, including system instructions, retrieved context, and tool results as applicable.
- [ ] **MODELS-106** `P1` Ensure benchmark harnesses distinguish model refusals, safety blocks, malformed outputs, and transport errors.
- [ ] **MODELS-107** `P1` Test provider interruptions, regional failures, and the documented fallback or degraded-mode response.
- [ ] **MODELS-108** `P1` Monitor model revision, quality signals, rate limits, latency, refusals, token usage, and cost by approved service dimensions.
- [ ] **MODELS-109** `P1` Validate any fallback or model route preserves safety filters, tool permissions, and supported API output contracts.
- [ ] **MODELS-110** `P1` Confirm API responses expose suitable error, abstention, and incomplete-result states rather than silently returning unverified content as fact.
- [ ] **MODELS-111** `P1` Ensure evaluation and monitoring data sent to vendors or external judges is authorized and appropriately sanitized.
- [ ] **MODELS-112** `P1` Test output-format compatibility of the selected model with persisted responses, cached results, and supported consumer versions.
- [ ] **MODELS-113** `P1` Confirm external tool actions are validated and authorized independently of the model selected.
- [ ] **MODELS-114** `P2` Record the model identifier, evaluation version, and review owner alongside the API release decision.

## Release gate

- [ ] Intended use, stakeholder impact, mandatory capabilities, and measurable quality/safety, latency, cost, and data-handling requirements are approved.
- [ ] A relevant baseline and candidate shortlist were tested on representative and held-out workloads using documented, reproducible evaluation settings.
- [ ] Task quality, severe failure rates, robustness, relevant group/language performance, and uncertainty meet predeclared acceptance rules or have approved mitigations.
- [ ] Realistic serving measurements show acceptable latency, throughput, availability, resource use, and cost per successful user task.
- [ ] Provider terms, model licenses, data residency/retention, model-version controls, and safety/authorization constraints are reviewed for intended use.
- [ ] API and frontend application behavior is verified where applicable, including schema adherence, refusals, fallbacks, error states, and user-facing comprehension.
- [ ] Decision makers have reviewed limitations, disqualifying risks, supporting evidence, alternatives, and a rollback/re-evaluation plan.
- [ ] A named approver has accepted the exact model/provider/configuration decision and recorded any residual risks, owners, and trigger for renewed assessment.

**Domain-specific approval rule:** Block model selection when a critical task or safety threshold is missed, validation data is compromised, material license or data-handling constraints are unresolved, or latency/cost at required capacity is not viable without accepted mitigation. A high public benchmark ranking alone cannot override an unsafe or unfit result.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#11_ai_model_selection_and_benchmarking), not prerequisites or verification evidence.

## Trusted references and scope

These primary framework, benchmark, and tool-maintainer sources inform the review questions. They are not proof that any specific model is suitable or that the product is certified by a standards body.

- [NIST AI RMF Playbook — Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) — measurement methods, uncertainty, robustness, operating context, and validation.
- [NIST AI RMF — Core Measure function](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — formal measurement of trustworthiness, uncertainty, independent assessment, and monitoring.
- [NIST AI RMF Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — generative-AI risk categories for candidate evaluation when relevant.
- [Hugging Face — Model Cards](https://huggingface.co/docs/hub/model-cards) — intended use, model limitations, bias, experimental setup, and evaluation documentation.
- [Hugging Face — Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) — benchmark-data provenance, licenses, languages, limitations, and representativeness.
- [Stanford CRFM — HELM](https://crfm.stanford.edu/helm/) — multi-scenario, multi-metric comparison of foundation models; compare only relevant tasks.
- [Stanford CRFM — HELM source and maintenance note](https://github.com/stanford-crfm/helm) — evaluation tooling; entered maintenance mode June 2026, so verify current support before adopting.
- [EleutherAI — LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) — reproducible prompt/task settings and open evaluation tooling.
- [EleutherAI — Custom task guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/new_task_guide.md) — definition and validation of task-specific benchmark configurations.
- [MLCommons — MLPerf Inference](https://mlcommons.org/working-groups/benchmarks/inference/) — fair and representative performance benchmarking across inference configurations.
- [MLCommons — MLPerf Inference Rules](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc) — reproducible workload scenarios, result integrity, and latency/throughput measurements.
- [Amazon Bedrock — Human model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-human.html) — human evaluation workflows for comparing candidate outputs when applicable.
- [Google Cloud — Define generative AI evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval) — task-appropriate grounding, safety, fluency, and customized rubric evaluation.

**Applicability:** NIST AI RMF material is voluntary guidance and the framework was under revision at the source review. HELM entered maintenance mode in June 2026. MLPerf measures defined hardware/software inference scenarios, not arbitrary end-user task quality. Benchmark harnesses and model/dataset cards require independent review of actual model versions, prompt templates, evaluation rights, and workload relevance. The listed proprietary platform documentation applies only when using those platforms; model/provider pricing and capabilities may change without advance notice.

**Source review date:** 2026-11-12.
