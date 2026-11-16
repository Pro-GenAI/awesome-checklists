# 15 — Prompt Engineering and Versioning Checklist

> Review instructions, templates, prompt revisions, and evaluation gates used in model-integrated software. Treat prompt wording as a behavioral control and engineering artifact, not a guarantee of security or deterministic correctness. Protect trust boundaries and external actions with independent code-level authorization.

> **Scope: Backend / API-specific.** This file is one part of the 15_Prompt_Engineering_and_Versioning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **PROMPT-093** `P1` Confirm the runtime selects the approved prompt revision and model configuration for each endpoint.
- [ ] **PROMPT-094** `P1` Validate required prompt variables against typed schemas before rendering or sending to a model.
- [ ] **PROMPT-095** `P1` Prevent user-controlled strings from becoming executable templates, privileged instructions, or unreviewed tool definitions.
- [ ] **PROMPT-096** `P1` Enforce context length and output budget limits and return explicit errors or safe truncation behavior.
- [ ] **PROMPT-097** `P1` Ensure request-level user, tenant, and resource permissions apply to retrieval and all model-triggered tool operations.
- [ ] **PROMPT-098** `P1` Validate structured model outputs and function-call arguments before storing data or executing downstream actions.
- [ ] **PROMPT-099** `P1` Test missing variable values, malformed input, unsupported modalities, and invalid encodings with predictable responses.
- [ ] **PROMPT-100** `P1` Verify any API caching includes prompt, model, tenant, permissions, and context version when they affect response correctness.
- [ ] **PROMPT-101** `P1` Guard against cross-tenant leakage in prompt histories, retrieval snippets, provider cache, and diagnostic payloads.
- [ ] **PROMPT-102** `P1` Limit and monitor token usage, tool calls, retries, and spending to protect the service during prompt regressions.
- [ ] **PROMPT-103** `P1` Ensure sensitive prompts and response content are not exposed in default HTTP logs, traces, or provider debugging.
- [ ] **PROMPT-104** `P1` Return explicit refusal, abstention, incomplete-result, and validation-error states where required by API contracts.
- [ ] **PROMPT-105** `P1` Test streaming output parsing and guardrails without committing partial, unvalidated data to irreversible actions.
- [ ] **PROMPT-106** `P1` Measure latency, token cost, schema validity, and policy-block rates by approved prompt revision.
- [ ] **PROMPT-107** `P1` Correlate incident events with model, prompt, policy, and tool schema revisions using safe identifiers.
- [ ] **PROMPT-108** `P1` Verify fallback to a prior prompt or alternate model preserves permissions, output format, and safety requirements.
- [ ] **PROMPT-109** `P1` Check prompt injection from external API results, documents, and tool outputs with nonproduction fixtures.
- [ ] **PROMPT-110** `P1` Run CI or deployment contract tests proving prompt changes do not silently break supported API consumers.
- [ ] **PROMPT-111** `P1` Ensure prompt release toggles, rollout cohort selection, and emergency disabling are server-controlled.
- [ ] **PROMPT-112** `P2` Record the prompt-version change and its approval evidence in the API release notes or equivalent change log.

## Release gate

- [ ] The production prompt's intended task, trusted instructions, allowed inputs, output contract, limits, and accountable owners are documented.
- [ ] Prompt templates safely handle variable inputs and untrusted content; model-generated tool calls are checked by independent permissions and schema validators.
- [ ] A reviewed, identifiable prompt revision is tied to an approved model/configuration snapshot, relevant schemas, and the release artifact.
- [ ] Representative held-out and adversarial evaluations meet predefined task-quality, policy, and format thresholds, with severe failures documented.
- [ ] The new prompt is compared against the currently approved baseline for critical regressions, false refusals, task completion, latency, and resource cost.
- [ ] API and frontend integration tests cover prompt-version-specific behavior, unsafe output handling, and useful recovery states where applicable.
- [ ] Rollout, monitoring, incident escalation, prompt rollback, and documented change authorization are ready for the intended release.
- [ ] Material residual privacy, security, quality, or user-harm risks have explicit owner, mitigation, retest deadline, and authorized release disposition.

**Domain-specific approval rule:** Block release when a prompt change can bypass required authorization, misroute sensitive content, break critical output contracts, or introduce significant unaccepted quality or safety regressions. No amount of instruction wording substitutes for enforced permission boundaries, input/output validation, or meaningful evaluation.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#15_prompt_engineering_and_versioning), not prerequisites or verification evidence.

## Trusted references and scope

These primary or authoritative sources inform the verification checks. Apply vendor-specific suggestions only to models and platforms where they have been tested; they are not universal guarantees of reliable or safe model behavior.

- [OpenAI API — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — clear instructions, message roles, examples, context management, and code-managed prompt versioning.
- [OpenAI API — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — task-based testing, held-out scenarios, nondeterminism, human-calibrated graders, and regression evaluation.
- [OpenAI API — Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) — schema-constrained outputs where supported; downstream validation remains necessary.
- [Anthropic — Prompting best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables) — prompt clarity, relevant examples, contextual delimiters, model-specific migration differences.
- [OWASP — LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — direct/indirect injection risks, untrusted inputs, tool authorization, and testing limitations.
- [OWASP — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — model-untrusted action proposals and execution-boundary controls for agentic integrations.
- [OWASP — Server Side Template Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Template_Injection_Prevention_Cheat_Sheet.html) — safe prompt-template rendering with untrusted variables.
- [NIST — Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — cross-cutting risks and evaluations for generative AI applications.
- [NIST AI RMF — Measure function](https://airc.nist.gov/airmf-resources/playbook/measure/) — evaluating AI performance, uncertainty, trustworthiness, and risk-related outcomes.
- [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) — reviewable changes, checks, and branch protection when using GitHub for prompt code.

**Applicability:** OpenAI's November 2026 prompt guidance prefers reviewed, code-managed prompts and notes deprecation of its reusable prompt-object API; check the official migration and deadline before relying on that feature. Prompt advice differs by model generation and vendor. OWASP string delimiters and text filters are defense-in-depth, not prompt-injection prevention guarantees. Use controlled benign and adversarial tests and code-enforced tool permission checks. This file does not replace governance, model selection, RAG, AI red-team, or full regression-evaluation reviews.

**Source review date:** 2026-11-12.
