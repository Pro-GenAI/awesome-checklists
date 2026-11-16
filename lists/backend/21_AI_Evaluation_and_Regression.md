# 21 — AI Evaluation and Regression Checklist

> Verify that AI-enabled applications have representative, measurable, repeatable evaluation of task quality and safety, and that changes are held to defined regression and release standards. Scores from a benchmark, a model judge, or a dashboard alone do not prove real-world correctness or absence of harm.

> **Scope: Backend / API-specific.** This file is one part of the 21_AI_Evaluation_and_Regression.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **EVAL-097** `P1` Expose evaluation job creation, status, result retrieval, and deletion only to authorized roles and scopes where an eval API exists.
- [ ] **EVAL-098** `P1` Separate staging, evaluation, and live production model endpoints and prevent sandbox cases from changing real customer records.
- [ ] **EVAL-099** `P1` Version API and grader input/output contracts for test cases, responses, scores, and artifact references.
- [ ] **EVAL-100** `P1` Verify stored evaluation runs identify exact model, prompt, retrieval, tool, safety policy, and dataset revisions.
- [ ] **EVAL-101** `P1` Validate all evaluation input fields, tool fixtures, requested models, and maximum output or context sizes.
- [ ] **EVAL-102** `P1` Use strictly scoped service credentials when invoking third-party judge models or provider evaluation endpoints.
- [ ] **EVAL-103** `P0` Ensure evaluation traffic cannot bypass standard tenant isolation, data rights, or secret handling policies.
- [ ] **EVAL-104** `P1` Test that external graders receive only approved sanitized content and required contextual fields.
- [ ] **EVAL-105** `P1` Use safe mock or idempotent tools to assess agent side effects without executing real payments, deletions, or messages.
- [ ] **EVAL-106** `P1` Distinguish model refusals, malformed outputs, policy blocks, tool failures, timeouts, and evaluator infrastructure errors.
- [ ] **EVAL-107** `P1` Validate structured output and tool-call assertions independently of model-generated explanations.
- [ ] **EVAL-108** `P1` Keep input data, reference labels, predictions, grades, and evaluator reasoning separate so expected answers cannot contaminate generation.
- [ ] **EVAL-109** `P1` Limit retries, concurrency, total job duration, per-model requests, and spend for bulk evaluation runs.
- [ ] **EVAL-110** `P1` Check job cancellation and partial evaluation behavior preserves accurate denominators and does not produce false passes.
- [ ] **EVAL-111** `P1` Protect result exports, trace logs, raw prompts, grader comments, and sensitive test fixtures with access and retention controls.
- [ ] **EVAL-112** `P1` Verify comparability of production and evaluation API versions, rate limits, streaming, and context-window behavior.
- [ ] **EVAL-113** `P1` Emit safe correlation identifiers for run, test case, model response, tool activity, and judge verdict.
- [ ] **EVAL-114** `P1` Test APIs with missing or malformed grader outputs and fail or escalate safely rather than recording zero-risk success.
- [ ] **EVAL-115** `P1` Enforce release gates on server-validated evaluation results rather than editable dashboard summaries.
- [ ] **EVAL-116** `P1` Test representative API contract and model-quality regressions together before promoting the release.

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

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#21_ai_evaluation_and_regression), not prerequisites or verification evidence.

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
