# 15 — AI Evaluation and Regression Checklist

> Verify that AI-enabled applications have representative, measurable, repeatable evaluation of task quality and safety, and that changes are held to defined regression and release standards. Scores from a benchmark, a model judge, or a dashboard alone do not prove real-world correctness or absence of harm.

> **Scope: AI-specific.** This file is one part of the 15_AI_Evaluation_and_Regression.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Task metrics and success criteria

- [ ] **EVAL-001** `P2` Define each AI-enabled user task, its intended outcome, and which system components the evaluation covers.
- [ ] **EVAL-002** `P1` Distinguish model-only capability evaluation from full product workflow and user-outcome evaluation.
- [ ] **EVAL-003** `P2` Assign a named business owner, evaluation owner, and qualified risk reviewer for each release-critical task.
- [ ] **EVAL-004** `P1` Choose task-specific primary quality metrics and document the units, calculation, direction, and acceptance threshold.
- [ ] **EVAL-005** `P2` Define separate severe-failure categories such as unauthorized actions, data disclosure, misleading high-impact advice, and materially incorrect decisions.
- [ ] **EVAL-006** `P1` Select safety, privacy, reliability, latency, accessibility, and cost guardrails appropriate to the deployment risk.
- [ ] **EVAL-007** `P2` Define whether precision, recall, F1, exact match, task completion, calibration, or human preference appropriately reflects success.
- [ ] **EVAL-008** `P1` Distinguish false positives from false negatives and agree which error types have greater real-world impact.
- [ ] **EVAL-009** `P2` Define correct abstention, refusal, request-for-clarification, and human-escalation behavior as measurable outcomes.
- [ ] **EVAL-010** `P1` Set acceptable rates for unsupported factual claims and incorrect citations where evidence-grounded answers are promised.
- [ ] **EVAL-011** `P1` Measure retrieval relevance separately from answer groundedness and completeness when the workflow uses RAG.
- [ ] **EVAL-012** `P1` Evaluate tool selection, argument correctness, permissions, side effects, and handoff completion when agents are used.
- [ ] **EVAL-013** `P2` Specify output-schema validity, required fields, parser errors, and downstream contract success where structured responses are required.
- [ ] **EVAL-014** `P1` Include multilingual, multimodal, long-context, and relevant subgroup metrics when supported by the product and allowed by applicable rules.
- [ ] **EVAL-015** `P2` Record target user cohorts, task difficulty, acceptable task duration, and normal versus adverse operating conditions.
- [ ] **EVAL-016** `P1` Agree baseline and candidate comparison rules before looking at the evaluation results.
- [ ] **EVAL-017** `P2` Define appropriate sample sizes, uncertainty reporting, and acceptable statistical or practical change in each critical metric.
- [ ] **EVAL-018** `P2` Document the expected cost per successful task and latency under representative concurrency rather than only per-model token prices.
- [ ] **EVAL-019** `P2` Specify which metrics must not regress even if the aggregate task-quality score improves.
- [ ] **EVAL-020** `P2` Document known unmeasurable harms, evaluation blind spots, and required compensating review for consequential use cases.
- [ ] **EVAL-021** `P1` Require relevant stakeholders to sign off on evaluation definitions before promoting a new model, prompt, or workflow.
- [ ] **EVAL-022** `P1` Review metric relevance when product goals, user populations, model authority, or supported modalities change.

## Golden datasets and representative cases

- [ ] **EVAL-023** `P2` Maintain a versioned golden or reference dataset whose records have stable IDs, expected outcomes, and task-specific metadata.
- [ ] **EVAL-024** `P2` Document source, consent or licensing restrictions, sampling method, review owner, and permissible use for each evaluation dataset.
- [ ] **EVAL-025** `P1` Sample representative authorized production task patterns or well-founded synthetic cases without including prohibited personal data.
- [ ] **EVAL-026** `P1` Keep a frozen holdout set separate from examples used to tune prompts, select models, or train evaluators.
- [ ] **EVAL-027** `P1` Audit train, tuning, evaluation, and holdout overlap including duplicate, near-duplicate, translated, and augmented examples.
- [ ] **EVAL-028** `P1` Include ordinary, edge, ambiguous, adverse, and high-consequence cases based on real expected use.
- [ ] **EVAL-029** `P1` Use realistic multi-turn conversations and full workflow state for tasks that depend on conversational history.
- [ ] **EVAL-030** `P1` Include negative cases requiring safe refusals, abstention, missing-context handling, or clarification.
- [ ] **EVAL-031** `P1` Add adversarial prompt injection and untrusted retrieved-content cases with safe test accounts and simulated tool effects.
- [ ] **EVAL-032** `P1` Include malformed, long, truncated, encoded, multilingual, and mixed-modality inputs relevant to supported interfaces.
- [ ] **EVAL-033** `P1` Represent major customer cohorts, feature flags, locales, supported channels, and risk-relevant conditions where permissible.
- [ ] **EVAL-034** `P1` Test time-sensitive facts, outdated knowledge, conflicting evidence, and stale or missing retrieved documents where applicable.
- [ ] **EVAL-035** `P1` Include scenarios with third-party API errors, retrieval failures, tool timeouts, partial work, and safe retries.
- [ ] **EVAL-036** `P2` Record expected outcomes as objective assertions, acceptable alternative answers, rubric grades, or authorized reference judgments.
- [ ] **EVAL-037** `P1` Use expert adjudication where valid answers vary or ground truth is genuinely uncertain rather than inventing one exact answer.
- [ ] **EVAL-038** `P1` Check that labels and expected answers remain aligned with current product policies, authoritative sources, and versioned schemas.
- [ ] **EVAL-039** `P1` Mark examples that became obsolete due to product changes and retain a review history before updating expectations.
- [ ] **EVAL-040** `P2` Track dataset size, coverage gaps, class balance, source freshness, and severe-case counts at every released version.
- [ ] **EVAL-041** `P0` Protect sensitive golden cases from unauthorized access, public embedding, and external model-evaluator transmission.
- [ ] **EVAL-042** `P1` Create an approved process for adding sanitized production incidents and user feedback to the regression collection.
- [ ] **EVAL-043** `P1` Require test records to reference versioned tool responses, search results, model inputs, and environment fixtures where needed for replay.
- [ ] **EVAL-044** `P1` Verify dataset parsing, evaluation prompt rendering, and expected-answer mapping on hand-checked fixtures.
- [ ] **EVAL-045** `P1` Ensure test labels, scoring rationales, and sample metadata cannot leak into the model input unless the task requires them.
- [ ] **EVAL-046** `P1` Freeze a released dataset manifest and checksum or equivalent immutable reference for reproducible comparisons.

## Human and automated evaluation

- [ ] **EVAL-047** `P1` Use deterministic assertions for machine-verifiable outputs such as schema validity, field values, authorized tool calls, and required refusals.
- [ ] **EVAL-048** `P1` Choose task-specific algorithmic metrics only when their assumptions match the expected output and user need.
- [ ] **EVAL-049** `P2` Define human grading rubrics with observable criteria, anchors, positive/negative examples, and explicit scoring instructions.
- [ ] **EVAL-050** `P1` Recruit qualified reviewers with domain, language, and cultural knowledge appropriate to sensitive and consequential tasks.
- [ ] **EVAL-051** `P1` Calibrate human reviewers on a representative set of examples before collecting release-critical judgments.
- [ ] **EVAL-052** `P1` Measure inter-rater agreement or disagreement using methods appropriate to the rating scale and task.
- [ ] **EVAL-053** `P1` Use independent adjudication for disputed high-impact labels or reviews rather than averaging away genuine differences.
- [ ] **EVAL-054** `P1` Randomize answer order and blind candidate identities where feasible to reduce preference and position bias.
- [ ] **EVAL-055** `P1` Check human reviewers are not shown sensitive information beyond their authorized role and approved purpose.
- [ ] **EVAL-056** `P1` Assess annotator burden and exposure to potentially distressing content; provide appropriate support and escalation.
- [ ] **EVAL-057** `P1` Validate model-based graders against expert human labels and known good/bad examples before trusting their verdicts.
- [ ] **EVAL-058** `P1` Check model-judge position, verbosity, language, self-preference, and reference-answer leakage biases where relevant.
- [ ] **EVAL-059** `P1` Version automated grading prompts, judge model snapshots, thresholds, and any external evaluation services.
- [ ] **EVAL-060** `P1` Test scorer behavior for empty outputs, formatting errors, timeouts, parse failures, and partial evaluation jobs.
- [ ] **EVAL-061** `P1` Distinguish a failed system response from a failed judge or unavailable evaluation service in reporting.
- [ ] **EVAL-062** `P1` Use paired candidate comparisons where practical and keep model settings and test fixtures comparable.
- [ ] **EVAL-063** `P1` Repeat stochastic model evaluations enough to characterize variance for release-critical decisions.
- [ ] **EVAL-064** `P2` Record confidence intervals or suitable uncertainty estimates and avoid claiming significance from small score differences.
- [ ] **EVAL-065** `P1` Report per-case and per-subgroup results along with aggregate scores so serious failures are not hidden.
- [ ] **EVAL-066** `P1` Separate retrieval ranking quality, groundedness, citation validity, and answer completeness in RAG evaluations.
- [ ] **EVAL-067** `P1` Grade agent task success using confirmed tool states and correct authorization, not merely persuasive model narratives.
- [ ] **EVAL-068** `P1` Evaluate user-visible task success, comprehension, safe behavior, and recovery through targeted usability testing where suitable.
- [ ] **EVAL-069** `P1` Compare automatic grades and real-user complaints to detect metric gaming or poor agreement with human utility.
- [ ] **EVAL-070** `P1` Control evaluation compute budget, data retention, external judge permissions, and reproducibility settings.
- [ ] **EVAL-071** `P1` Store failures and reviewer rationales securely for investigation without retaining unnecessary private full transcripts.
- [ ] **EVAL-072** `P1` Require an explicit evaluator-quality review before changing the scoring approach that blocks or approves releases.

## Regression and release thresholds

- [ ] **EVAL-073** `P1` Establish an approved production baseline for each critical evaluation suite, including exact model, prompt, data, tool, and evaluator versions.
- [ ] **EVAL-074** `P1` Trigger relevant evaluation suites for changes to model snapshots, prompts, retrieval, fine-tuning, tool definitions, policy, or output parsers.
- [ ] **EVAL-075** `P2` Define smoke, targeted, full regression, and adversarial suites with risk-based execution times and ownership.
- [ ] **EVAL-076** `P1` Run relevant quality and safety gates in CI or equivalent controlled release workflows, not only manually after launch.
- [ ] **EVAL-077** `P1` Preserve run identifiers, timestamps, source revisions, dataset manifests, judge versions, environment, and inference settings.
- [ ] **EVAL-078** `P1` Compare candidate and baseline results using identical cases and fair configurations wherever possible.
- [ ] **EVAL-079** `P1` Set predeclared absolute performance floors and maximum allowed regression deltas for each launch-critical metric.
- [ ] **EVAL-080** `P1` Make severe safety, unauthorized-action, or privacy violations individually blocking when required rather than averaging them into a quality score.
- [ ] **EVAL-081** `P1` Account for stochastic variability, repeated runs, and confidence limits when deciding whether a small observed delta is meaningful.
- [ ] **EVAL-082** `P1` Detect flaky tests and isolate environmental or evaluator failures without silently ignoring real application regressions.
- [ ] **EVAL-083** `P1` Require owner review of newly failing cases, newly passing cases, and cases whose scores moved materially.
- [ ] **EVAL-084** `P1` Prevent test-set edits or metric-weight changes from being used to conceal a known regression without review.
- [ ] **EVAL-085** `P2` Define a documented waiver process with rationale, severity, accountable approver, expiration, and retest plan.
- [ ] **EVAL-086** `P1` Check that low-frequency but high-consequence tests stay visible in release reports even when their sample size is small.
- [ ] **EVAL-087** `P1` Validate API schema, error handling, permissions, and downstream integration behavior alongside model-level metrics.
- [ ] **EVAL-088** `P1` Test representative production load, latency, token usage, context size, throughput, and per-task cost for changed configurations.
- [ ] **EVAL-089** `P1` Use shadow, canary, feature flags, or limited rollout when offline tests cannot capture important real-world outcomes.
- [ ] **EVAL-090** `P2` Define production guardrails and stop conditions for unexpected refusal changes, user complaints, harmful outputs, or task failures.
- [ ] **EVAL-091** `P1` Ensure rollback or fallback configurations have been tested against compatible prompts, schemas, and permitted tool capabilities.
- [ ] **EVAL-092** `P1` Correlate production quality indicators and incident reports with the exact deployed evaluation baseline and model/configuration revisions.
- [ ] **EVAL-093** `P1` Collect privacy-preserving production feedback and representative user reports as candidates for future regression fixtures.
- [ ] **EVAL-094** `P1` Review whether data or concept drift makes the held-out evaluation set less representative of current traffic.
- [ ] **EVAL-095** `P1` Reevaluate evaluation metrics and samples when business policy, user population, or downstream consequences change.
- [ ] **EVAL-096** `P2` Record a final go/no-go decision and remaining accepted risks against the exact candidate release.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **EVAL-117** `P1` Evaluate complete user journeys and representative device/browser conditions in addition to isolated model text outputs.
- [ ] **EVAL-118** `P1` Show appropriate uncertainty, no-answer, refusal, or escalation UI for cases where the model cannot meet the task.
- [ ] **EVAL-119** `P1` Verify citations and factual evidence displayed in the UI support the corresponding claims when source-grounding is promised.
- [ ] **EVAL-120** `P1` Test how users perceive model-generated suggestions compared with independently verified facts or committed external actions.
- [ ] **EVAL-121** `P1` Check output rendering for malformed markup, long text, unsupported characters, streaming, tables, and structured widgets.
- [ ] **EVAL-122** `P1` Ensure user-visible failures, timeouts, missing context, and rejected tool actions have accessible recovery paths.
- [ ] **EVAL-123** `P1` Test keyboard, assistive-technology, and focus behavior for AI-generated dynamic content and error states.
- [ ] **EVAL-124** `P1` Validate that localization, multilingual input, and supported multimodal flows are represented in regression tests.
- [ ] **EVAL-125** `P1` Compare page/task latency, time-to-first-content, and completion time before and after model or prompt changes.
- [ ] **EVAL-126** `P1` Test how frontend caches, old browser tabs, or feature flags behave with new prompt and response formats.
- [ ] **EVAL-127** `P1` Confirm client-side validation and rendering cannot make an unsafe model response executable.
- [ ] **EVAL-128** `P1` Verify agent actions appear as proposed, pending, approved, or confirmed only when supported by authoritative state.
- [ ] **EVAL-129** `P1` Include approved user research and comprehension checks where automation bias or overreliance is a material risk.
- [ ] **EVAL-130** `P1` Ensure test interfaces do not display restricted golden answers, private evaluation prompts, or secret reference data to unauthorized users.
- [ ] **EVAL-131** `P1` Make feedback and report-an-error controls usable for incorrect, harmful, or inaccessible AI output.
- [ ] **EVAL-132** `P1` Check that production feedback tagging records the deployed model/configuration without collecting unnecessary personal data.
- [ ] **EVAL-133** `P1` Evaluate user experience of staged rollout and fallback when a different model changes output length, tone, or available features.
- [ ] **EVAL-134** `P1` Test visible safety warnings and confirmations for high-impact workflows before release.
- [ ] **EVAL-135** `P1` Review mobile and low-bandwidth behavior under slow or failing evaluation-relevant AI services.
- [ ] **EVAL-136** `P1` Check important frontend regressions and support escalations against release-approved user-task metrics.

## Release gate

- [ ] The exact release has approved task definitions, meaningful primary metrics, severe-failure conditions, risk guardrails, and predeclared acceptance thresholds.
- [ ] Golden and held-out evaluation cases are representative of the intended deployment, versioned, permissioned, contamination-checked, and reviewed for major coverage gaps.
- [ ] Deterministic assertions and model-based graders are fit for purpose; human rubrics and automated judge scores have suitable calibration and auditability.
- [ ] Candidate and approved baseline results are compared with reproducible settings, adequate repeatability, and explicit statistical or practical uncertainty where needed.
- [ ] All release-blocking privacy, safety, authorization, and consequential task failures are resolved or have the specifically required authorized disposition; averaging does not waive critical failures.
- [ ] API, retrieval, agent/tool, and frontend end-to-end paths meet the relevant quality, contract, usability, accessibility, latency, and cost requirements.
- [ ] CI/controlled release gates, anomaly and regression review, safe rollback, production observation, and accountable incident response are ready.
- [ ] A named release approver has reviewed run artifacts, per-case regressions, coverage limitations, accepted risks, and the precise model/data/prompt/guardrail versions promoted.

**Domain-specific approval rule:** Block sign-off when the evaluation suite is materially unrepresentative or contaminated, scoring is unvalidated for decisions it controls, a severe user-impacting or unauthorized-action failure is unresolved, or an important metric regresses beyond its approved threshold without qualified acceptance. Passing these checks is not proof of complete AI safety, impartiality, or compliance with any particular jurisdiction.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#15_ai_evaluation_and_regression), not prerequisites or evidence of PASS.

## Trusted references and scope

The following official frameworks, provider documentation, and tool-maintainer references informed these project-specific verification questions. They are not universal requirements or substitutes for independent evaluation design.

- [NIST AI RMF Playbook — Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) — risk-based evaluation methods, uncertainty, deployment conditions, and measurement gaps.
- [NIST AI RMF Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — generative AI risk identification, evaluation, and trustworthiness considerations.
- [OpenAI API — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — task-specific evals, representative cases, model variability, calibration, and development-driven regression.
- [OpenAI API — Graders](https://developers.openai.com/api/docs/guides/graders) — deterministic and model-based grading, human reference scores, grader limitations; note platform deprecation.
- [Microsoft Foundry — Evaluation overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-overview) — evaluation workflow, datasets, response generation, quality/safety metrics, and production traces.
- [Microsoft Foundry — Built-in Evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators) — task completion, retrieval, groundedness, safety, and textual similarity metrics.
- [Microsoft Foundry — RAG Evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators?view=foundry) — separate retrieval-process and grounded-answer system evaluation.
- [Google Cloud — Gen AI evaluation service overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) — adaptive task rubrics, version/model comparisons, production sampling, and synthetic test cases.
- [Amazon Bedrock — Automatic model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create.html) — task-specific dataset jobs, settings, built-in metrics, and evaluation artifacts.
- [Amazon Bedrock — Human model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create-human.html) — human review teams, task-specific instructions, qualitative comparisons, and grading controls.
- [Amazon Bedrock — LLM-as-a-judge evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-judge-create.html) — judge-model evaluation configuration, IAM, datasets, and permissions.
- [Ragas — Available evaluation metrics](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/) — RAG faithfulness/retrieval and agent task/tool metrics where this library is chosen.

**Applicability:** NIST AI RMF and its GenAI profile are voluntary risk frameworks, not certifications. As of November 2026, the OpenAI Evals platform and associated graders are being retired (read-only after October 31; scheduled closure November 30); avoid building new long-lived release gates dependent on that service and verify the latest migration guidance. Microsoft, Google, and AWS evaluation features, model judges, and scoring thresholds are platform-specific and may have version, regional, or preview limitations. Ragas metrics are implementation choices, not a universal scientific gold standard. Protect evaluation data and check legal rights before sharing it with third-party judges.

**Source review date:** 2026-11-12.
