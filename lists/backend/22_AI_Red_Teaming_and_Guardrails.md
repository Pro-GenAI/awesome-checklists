# 22 — AI Red Teaming and Guardrails Checklist

> Verify that AI-enabled products have risk-based adversarial coverage and enforceable defenses against harmful outputs, unauthorized actions, data disclosure, and abuse. Red teaming seeks to discover failures; passing a finite test suite does not prove a model or product cannot be bypassed.

> **Scope: Backend / API-specific.** This file is one part of the 22_AI_Red_Teaming_and_Guardrails.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **RED-097** `P1` Authenticate and authorize safety-sensitive endpoints, moderation routes, policy overrides, and privileged model integrations.
- [ ] **RED-098** `P1` Apply caller, resource, tenant, and purpose restrictions before model-generated tool or retrieval operations execute.
- [ ] **RED-099** `P1` Validate structured outputs, tool arguments, URL destinations, and user-supplied media against strict server-side rules.
- [ ] **RED-100** `P1` Test direct and indirect injection through every API-supported data ingress, including uploaded files and external tool results.
- [ ] **RED-101** `P1` Verify safety filtering covers API requests and relevant outputs without assuming all SDK or hosted tool paths share guardrail hooks.
- [ ] **RED-102** `P1` Check guardrail failure, timeout, and degraded-service behavior for safe treatment of sensitive actions.
- [ ] **RED-103** `P1` Enforce bounded prompt length, response size, tool count, per-user usage, retries, concurrency, and model spending.
- [ ] **RED-104** `P2` Record guardrail verdicts and security decisions with safe correlation IDs and policy revisions, without logging raw secrets.
- [ ] **RED-105** `P1` Test that policy-blocked content cannot leak through streaming fragments, cached responses, asynchronous jobs, or alternate routes.
- [ ] **RED-106** `P1` Measure unauthorized tool attempts and actual state changes rather than trusting only model-produced refusal messages.
- [ ] **RED-107** `P1` Verify API error contracts distinguish blocked, refused, review-required, malformed, unavailable, and timed-out results.
- [ ] **RED-108** `P1` Test moderation and action checks with encoded, non-Latin, long, malformed, and multimodal input where supported.
- [ ] **RED-109** `P1` Ensure approved human-review decisions bind to the correct identity, action, arguments, and current permissions.
- [ ] **RED-110** `P1` Validate that rate limiting and abuse controls cannot be bypassed by switching model aliases, endpoints, or tenants.
- [ ] **RED-111** `P0` Check cross-tenant isolation in retrieval indexes, agent memory, response caches, monitoring, and evaluation exports.
- [ ] **RED-112** `P1` Test safe rollback or feature disablement after a critical guardrail or model-policy regression.
- [ ] **RED-113** `P1` Ensure API integrations with moderation and model providers use approved regions, storage settings, and processing terms.
- [ ] **RED-114** `P1` Run safety and authorization contract tests in CI with isolated sandbox accounts and synthetic payloads.
- [ ] **RED-115** `P1` Check model-, guardrail-, prompt-, and tool-version alignment against the approved production release.
- [ ] **RED-116** `P1` Monitor p95 latency, policy-decision availability, false blocks, and risk-related throughput under representative load.

## Release gate

- [ ] A reviewed threat model covers intended use, attacker-controlled inputs, privileged operations, sensitive data, relevant harms, and approved test boundaries.
- [ ] A versioned adversarial evaluation set covers representative direct/indirect attacks, meaningful tool and data boundaries, high-impact policy failures, and benign controls.
- [ ] No unaccepted high-severity violation remains, including unauthorized access, protected-data disclosure, disallowed external side effects, or serious user harm.
- [ ] Moderation and other guardrails have documented coverage, known limitations, false-positive/false-negative measurements, and safe behavior during outages and handoffs.
- [ ] Independent authentication, authorization, parameter validation, resource limits, and action-specific approval prevent prompt wording from granting privilege or bypassing protections.
- [ ] API, retrieval, and frontend paths have been tested for unsafe output handling, information leakage, improper caching, failure states, and supported multilingual/multimodal behavior where relevant.
- [ ] Safety monitoring, incident escalation, emergency disablement, user reporting, and validated retest/rollback procedures have named owners.
- [ ] Release approvers have reviewed exact model/prompt/policy/tool versions, test results, residual risks, and written risk-acceptance decisions with deadlines.

**Domain-specific approval rule:** Block sign-off if an agent or model can bypass required access controls, execute material unauthorized actions, disclose protected content, or cause serious harm without acceptable mitigation; if required guardrails fail open on dangerous paths; or if critical attack surfaces have not been meaningfully evaluated. No red-team result establishes perfect security, comprehensive legal compliance, or immunity to new attacks.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#22_ai_red_teaming_and_guardrails), not prerequisites or verification evidence.

## Trusted references and scope

These official risk frameworks, test guidance, and provider documentation inform the review items; applicability depends on system capability and the relevant policy.

- [OWASP GenAI LLM Top 10 (2026)](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — current AI-app security risk taxonomy and mitigations for relevant LLM systems.
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — agentic goal hijacking, tool misuse, privilege abuse, and cascading failures.
- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — direct/indirect injection, defense in depth, evaluation design, and limits of text filters.
- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — agentic attack surfaces, scenario-driven threat modeling, and mitigations.
- [MITRE ATLAS](https://atlas.mitre.org/) — empirically grounded adversarial tactics, techniques, mitigations, and AI attack case studies.
- [NIST AI RMF Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — generative AI risk categories and voluntary risk-management recommendations.
- [NIST AI RMF Playbook — Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) — context-specific AI test evaluation, performance, and failure monitoring.
- [OpenAI API — Red teaming](https://developers.openai.com/api/docs/guides/red-teaming) — authorized adversarial probing as distinct from routine model evaluation.
- [OpenAI API — Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) — adversarial testing, human review, user reporting, and safeguards.
- [OpenAI API — Moderation](https://developers.openai.com/api/docs/guides/moderation) — policy screening, input/output handling, and supported text/image modalities.
- [OpenAI Agents SDK — Guardrails](https://openai.github.io/openai-agents-python/guardrails/) — agent and tool guardrail execution boundaries, tripwires, and scope limitations.
- [Anthropic — Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) — risk of tool-output injection, user consent, restricted network access, and approval for consequential actions.

**Applicability:** OWASP GenAI LLM Top 10 (2026) and Agentic Top 10 (2026) are awareness and risk frameworks, not certifications. MITRE ATLAS is a living adversary knowledge base; do not treat its tactics as an exhaustive checklist. NIST AI RMF and its generative AI profile are voluntary guidance. Provider moderation models and agent-guardrail SDKs differ in modalities, integration points, blocking semantics, and coverage; verify the actual runtime. Safety classifiers and prompt instructions are defense in depth, not authorization controls. Only conduct red-teaming where the project has explicit authority.

**Source review date:** 2026-11-12.
