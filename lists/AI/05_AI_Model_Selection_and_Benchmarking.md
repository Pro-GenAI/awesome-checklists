# 05 — AI Model Selection and Benchmarking Checklist

> Choose AI models against the actual application workload, operating constraints, safety requirements, and measurable outcomes. Public leaderboards help identify candidates but do not prove suitability, compliance, or reliability for a particular deployment.

> **Scope: AI-specific.** This file is one part of the 05_AI_Model_Selection_and_Benchmarking.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Use-case fit and constraints

- [ ] **MODELS-001** `P2` Define the exact model-supported task, target users, expected outcomes, and whether AI adds measurable value over a deterministic approach.
- [ ] **MODELS-002** `P2` Identify critical workflows where incorrect, delayed, biased, or missing model output could materially harm users.
- [ ] **MODELS-003** `P2` Specify supported languages, scripts, regions, modalities, input formats, and output formats required by the product.
- [ ] **MODELS-004** `P2` Describe task-specific quality criteria such as factuality, instruction following, extraction accuracy, recall, or answer usefulness.
- [ ] **MODELS-005** `P2` Document unacceptable failures and safe abstention, escalation, or fallback conditions before choosing candidates.
- [ ] **MODELS-006** `P2` Define model input context requirements, typical and worst-case prompt sizes, and output length limits.
- [ ] **MODELS-007** `P1` Measure representative input/output size distributions rather than selecting a model based only on its advertised context window.
- [ ] **MODELS-008** `P2` Identify tool calling, constrained output, streaming, multimodal, batch, and structured response capabilities required for the integration.
- [ ] **MODELS-009** `P2` Record target throughput, concurrency, p95/p99 latency, time-to-first-output, and completion-time budgets as applicable.
- [ ] **MODELS-010** `P2` Specify per-request and monthly cost constraints, including input/output tokens, provider charges, infrastructure, and storage.
- [ ] **MODELS-011** `P2` Define uptime, data residency, processing location, privacy, retention, and network dependency requirements.
- [ ] **MODELS-012** `P1` Review candidate licensing, redistribution, usage restrictions, and relevant commercial terms before evaluation.
- [ ] **MODELS-013** `P1` Evaluate whether hosted APIs, self-hosting, or hybrid deployment fit the team's security, reliability, and operational capacity.
- [ ] **MODELS-014** `P1` Check hardware compatibility, available accelerator memory, model size, quantization support, and inference runtime constraints.
- [ ] **MODELS-015** `P2` Identify training-data or model provenance gaps that could affect legally permitted use or output reliability.
- [ ] **MODELS-016** `P1` Assess the allowed uses of supplied personal, confidential, copyrighted, or regulated content for each candidate provider.
- [ ] **MODELS-017** `P2` Specify observability, version pinning, audit requirements, and ability to reproduce or investigate model behavior.
- [ ] **MODELS-018** `P2` Document what happens if the candidate is deprecated, replaced, unavailable, or materially changed by its provider.
- [ ] **MODELS-019** `P1` Include human review and non-AI escalation requirements for consequential decisions or autonomous external actions.
- [ ] **MODELS-020** `P2` Assign accountable product, engineering, risk, and evaluation owners to the selection criteria.
- [ ] **MODELS-021** `P2` Record the initial acceptance thresholds and mandatory exclusions before reviewing benchmark rankings.
- [ ] **MODELS-022** `P1` Revisit requirements when audience, task, input distribution, external integrations, or market obligations change.

## Candidate comparison and baseline

- [ ] **MODELS-023** `P1` Create a shortlist with exact model name, provider, model/checkpoint revision, license, deployment location, and evaluation date.
- [ ] **MODELS-024** `P1` Include the existing production model and a simpler or non-model baseline where practical.
- [ ] **MODELS-025** `P1` Choose candidates based on mandatory capabilities before optimizing for public leaderboard placement.
- [ ] **MODELS-026** `P1` Read candidate model cards and system documentation for intended uses, limitations, safety notes, and provenance.
- [ ] **MODELS-027** `P1` Check vendor claims against test conditions, workload distribution, and evidence supplied with each benchmark.
- [ ] **MODELS-028** `P1` Compare variants with the same task definition and equivalent retrieval, tools, and workflow context wherever possible.
- [ ] **MODELS-029** `P1` Use the same evaluation examples and scoring logic for all candidates; document any justified exceptions.
- [ ] **MODELS-030** `P1` Control prompt templates, message roles, system policies, few-shot examples, and tool access during baseline comparisons.
- [ ] **MODELS-031** `P2` Record decoding settings such as temperature, top-p, seed support, maximum outputs, and stop conditions for every run.
- [ ] **MODELS-032** `P1` Differentiate base, instruction-tuned, fine-tuned, quantized, distilled, and reasoning-oriented model variants.
- [ ] **MODELS-033** `P1` Check candidate context-window behavior on representative long and short inputs, not only advertised maximum limits.
- [ ] **MODELS-034** `P1` Test refusal, abstention, and uncertainty behavior on ambiguous or unsupported questions.
- [ ] **MODELS-035** `P1` Assess hallucination or unsupported assertion rates in tasks expecting evidence-grounded factual outputs.
- [ ] **MODELS-036** `P1` Measure task-relevant robustness to typos, formatting changes, distractors, and long-tail inputs.
- [ ] **MODELS-037** `P1` Run safety and policy probes proportionate to the product's foreseeable risk rather than relying on general safety claims.
- [ ] **MODELS-038** `P1` Compare subgroup and language-specific outcomes when those groups and characteristics are justified by the deployment context.
- [ ] **MODELS-039** `P1` Compare output-schema adherence, tool-call argument validity, and retry needs if structured outputs or tools are required.
- [ ] **MODELS-040** `P1` Measure time-to-first-token, completion latency, throughput, and errors at representative concurrency.
- [ ] **MODELS-041** `P1` Calculate normalized cost per successful task, not solely advertised price per token or per inference.
- [ ] **MODELS-042** `P2` Record output lengths and reasoning-token or other hidden billable usage when the provider exposes those values.
- [ ] **MODELS-043** `P1` Assess response variability and repeatability across multiple samples for non-deterministic tasks.
- [ ] **MODELS-044** `P1` Check how each candidate handles provider rate limits, regional restrictions, and transient unavailable states.
- [ ] **MODELS-045** `P2` Document functional features that do not work for a candidate rather than treating them as zero-cost alternatives.
- [ ] **MODELS-046** `P1` Compare quality, safety, latency, availability, operating effort, and cost as a multi-criteria decision, not a single composite score without rationale.

## Benchmark datasets and methodology

- [ ] **MODELS-047** `P2` Define the evaluation population and usage scenarios from real product tasks, authorized research, or representative synthetic examples.
- [ ] **MODELS-048** `P1` Split development/tuning examples from a final held-out selection set and restrict access to the held-out set.
- [ ] **MODELS-049** `P2` Document each benchmark dataset's origin, version, license, sensitivity, allowed use, and known representativeness limits.
- [ ] **MODELS-050** `P1` Check for train/test overlap, answer leakage, duplicate examples, and exposure of hidden answers during prompt iteration.
- [ ] **MODELS-051** `P1` Include typical, edge-case, high-risk, low-resource-language, and adverse inputs in proportions suited to deployment risk.
- [ ] **MODELS-052** `P2` Define correct or acceptable outcomes and rationale before running candidate comparisons.
- [ ] **MODELS-053** `P1` Choose task-appropriate metrics with known failure modes rather than relying on an arbitrary aggregate accuracy number.
- [ ] **MODELS-054** `P1` Measure false positives and false negatives separately where their real-world consequences differ.
- [ ] **MODELS-055** `P1` Use reference-free or human assessment where a single exact answer is inappropriate for creative or open-ended tasks.
- [ ] **MODELS-056** `P1` Write clear human-grading rubrics for factual support, completeness, helpfulness, safety, and formatting where relevant.
- [ ] **MODELS-057** `P1` Train or calibrate human reviewers and check disagreement/adjudication on a representative subset.
- [ ] **MODELS-058** `P1` Blind evaluators to candidate identity and randomize answer presentation where feasible to reduce preference bias.
- [ ] **MODELS-059** `P1` Validate model-based judges against qualified human ratings before trusting automated scores.
- [ ] **MODELS-060** `P1` Assess evaluator or judge position bias, verbosity bias, leakage, and self-preference where applicable.
- [ ] **MODELS-061** `P2` Specify score aggregation, weighting, treatment of missing results, and category-level reporting before reviewing outcomes.
- [ ] **MODELS-062** `P1` Report sample size, confidence intervals or other uncertainty estimates, and the frequency of severe failures where appropriate.
- [ ] **MODELS-063** `P1` Repeat stochastic benchmarks enough times to describe variability and distinguish small differences from noise.
- [ ] **MODELS-064** `P2` Record model revisions, evaluation-harness version, benchmark configurations, prompt formats, and seeds or supported reproducibility controls.
- [ ] **MODELS-065** `P1` Preserve input IDs, sanitized outputs, scoring artifacts, and error cases under the project's data-retention and access policy.
- [ ] **MODELS-066** `P1` Verify evaluation scripts and prompt/answer extraction on small known-correct fixtures before scaling runs.
- [ ] **MODELS-067** `P2` Track benchmark cost and rate limits and exclude unauthorized or sensitive data from third-party evaluation endpoints.
- [ ] **MODELS-068** `P1` Compare benchmark run settings against real production settings, including context management, retrieval, guardrails, and tool access.
- [ ] **MODELS-069** `P1` Run offline task tests and end-to-end application tests separately so model quality is not confused with system quality.
- [ ] **MODELS-070** `P1` Include workload-specific adversarial and harmful-output checks with severity-weighted acceptance criteria.
- [ ] **MODELS-071** `P1` Measure latency, time-to-first-output, throughput, and resource usage using representative concurrent load.
- [ ] **MODELS-072** `P1` Test quality changes from quantization, caching, model routing, streaming, or inference optimizations where used.
- [ ] **MODELS-073** `P1` Flag invalid benchmark runs caused by truncation, provider errors, judge failures, incorrect answer parsing, or timeouts.
- [ ] **MODELS-074** `P2` Publish enough methodology, limitations, and reproducible configuration for an independent reviewer to interpret candidate differences.

## Selection and decision records

- [ ] **MODELS-075** `P1` Summarize each candidate's scores by critical task and risk category alongside benchmark uncertainty and sample sizes.
- [ ] **MODELS-076** `P1` Preserve raw task-level results and severe failure examples in approved restricted review records.
- [ ] **MODELS-077** `P2` Document disqualifying safety, accuracy, policy, license, data processing, or availability failures separately from averaged scores.
- [ ] **MODELS-078** `P1` Use agreed decision criteria and show the trade-offs between quality, latency, cost, privacy, reliability, and operational burden.
- [ ] **MODELS-079** `P1` Check that no hidden metric weighting or selective benchmark subset reverses the documented decision without explanation.
- [ ] **MODELS-080** `P2` Identify contexts where the selected model underperforms and define fallback, abstention, or human-review behavior.
- [ ] **MODELS-081** `P2` Record permitted model uses, unsupported scenarios, and the conditions under which performance claims cease to apply.
- [ ] **MODELS-082** `P2` Define the production model identifier and how the exact artifact or provider revision will be pinned or detected.
- [ ] **MODELS-083** `P2` Document required provider approvals, contracts, data-processing decisions, and audit/documentation dependencies.
- [ ] **MODELS-084** `P1` Estimate ongoing cost for expected and higher-load scenarios, including token distribution, batching, hosting, and failures.
- [ ] **MODELS-085** `P1` Plan cold starts, scaling, concurrency limits, throttling, provider quotas, and operational monitoring for the chosen deployment mode.
- [ ] **MODELS-086** `P1` Agree a staged rollout with measurable task-quality, latency, error, safety, and business guardrails.
- [ ] **MODELS-087** `P2` Define what observed failures trigger automatic downgrade, manual rollback, provider switch, or feature disablement.
- [ ] **MODELS-088** `P1` Test a fallback model or non-model experience for compatibility with the same interface and safety requirements where required.
- [ ] **MODELS-089** `P2` Define a reevaluation schedule and triggers for vendor model updates, drift, major user changes, or changed regulations.
- [ ] **MODELS-090** `P1` Create a versioned decision record with approvers, risk acceptances, model and dataset versions, and review date.
- [ ] **MODELS-091** `P1` Ensure stakeholders can inspect the selection evidence without accessing restricted personal data or proprietary test cases.
- [ ] **MODELS-092** `P1` Link the model-selection decision to AI governance, evaluation/regression, model-card, serving, and monitoring owners.
- [ ] **MODELS-093** `P2` Record where public leaderboards are inapplicable because their tasks, versions, hardware, or prompts differ from deployment.
- [ ] **MODELS-094** `P1` Require fresh approval when switching model families, vendors, training data policy, modalities, or external action capabilities.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **MODELS-115** `P1` Validate the selected model's response quality on realistic user journeys rather than only offline text prompts.
- [ ] **MODELS-116** `P1` Test whether users understand when answers are generated, uncertain, source-grounded, or incomplete.
- [ ] **MODELS-117** `P1` Measure time to first visible response and completion time under representative browser and mobile network conditions.
- [ ] **MODELS-118** `P1` Confirm streaming or partial results do not appear to be final decisions before validation or safety checks finish.
- [ ] **MODELS-119** `P1` Ensure long answers, markdown, code, structured data, and multilingual text render safely and accessibly.
- [ ] **MODELS-120** `P1` Test frontend handling of refusals, abstentions, model errors, timeouts, rate limits, and offline use.
- [ ] **MODELS-121** `P1` Provide understandable feedback and recovery options when the selected model cannot perform the requested task.
- [ ] **MODELS-122** `P1` Check that important citations and evidence are presented truthfully and do not imply unsupported factual verification.
- [ ] **MODELS-123** `P1` Verify model-specific UI affordances such as attachments, image/audio inputs, and tool approvals work across supported devices.
- [ ] **MODELS-124** `P1` Do not expose private model API keys, provider credentials, or confidential evaluation data in client bundles.
- [ ] **MODELS-125** `P1` Test output variability for repeated user tasks and ensure the interface does not promise determinism where none exists.
- [ ] **MODELS-126** `P1` Validate localization and accessibility for error states, safety interventions, and human escalation controls.
- [ ] **MODELS-127** `P1` Test whether the model's tendency to be verbose, terse, or hedged harms task completion or comprehension.
- [ ] **MODELS-128** `P1` Check whether fallback models alter response format, latency, language, or available actions in a way users need to understand.
- [ ] **MODELS-129** `P1` Verify user consent and warning copy reflect the approved provider's actual data handling and model capabilities.
- [ ] **MODELS-130** `P2` Define frontend guardrails for maximum input length, upload types, output length, and cost-sensitive operations as appropriate.
- [ ] **MODELS-131** `P1` Confirm human-review and confirmation steps remain effective for consequential actions regardless of model ranking.
- [ ] **MODELS-132** `P1` Correlate client-side failures and user reports with the deployed model version without exposing sensitive prompts or outputs.
- [ ] **MODELS-133** `P1` Review a representative set of task completions with target users before declaring a model suitable for the workflow.
- [ ] **MODELS-134** `P1` Ensure the selected model's production rollout has client-side health signals and feature-disablement paths.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#05_ai_model_selection_and_benchmarking), not prerequisites or evidence of PASS.

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
