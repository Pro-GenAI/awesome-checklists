# 10 — AI Evaluation and Governance Checklist

> Review whether a proposed AI use is appropriate, its risks are understood, the system has credible evaluation evidence, human oversight is operational, and organizational accountability is maintained across its lifecycle. This cross-cutting checklist complements detailed model, RAG, agent, red-team, data, and monitoring templates in their respective AI domain checklists.

> **Scope: Backend / API-specific.** This file is one part of the 10_AI_Evaluation_and_Governance.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **AIG-091** `P2` Inventory all model inference, embeddings, retrieval, moderation, feedback, and action-execution APIs that form the AI product.
- [ ] **AIG-092** `P2` Describe the intended purpose and authority of each endpoint, including authenticated caller roles and tenant boundaries.
- [ ] **AIG-093** `P1` Enforce authorization on the server for model outputs, retrieval access, and every external tool action regardless of prompt content.
- [ ] **AIG-094** `P1` Treat model-generated arguments and retrieved content as untrusted input; validate them against strict schemas and permissions.
- [ ] **AIG-095** `P1` Apply output validation and downstream encoding before model content is rendered, stored, executed, or sent to other services.
- [ ] **AIG-096** `P1` Restrict high-impact API actions with explicit user consent or human approval gates appropriate to the operation.
- [ ] **AIG-097** `P1` Protect model credentials, provider tokens, customer input, sensitive prompt content, and retrieved documents from accidental logging.
- [ ] **AIG-098** `P2` Document provider data-use and retention settings and enforce approved endpoint regions and account configuration where applicable.
- [ ] **AIG-099** `P1` Use scoped timeouts, quotas, concurrency bounds, rate limits, and spending controls to prevent unbounded inference or tool calls.
- [ ] **AIG-100** `P2` Define safe retry and idempotency behavior so AI-mediated API timeouts do not duplicate purchases, messages, or data changes.
- [ ] **AIG-101** `P1` Include structured error states for refusal, abstention, invalid output, tool failure, timeout, and policy block where appropriate.
- [ ] **AIG-102** `P1` Make API response contracts distinguish verified facts, model-generated content, citations, tool results, and confidence estimates when supported.
- [ ] **AIG-103** `P1` Do not expose internal instructions, proprietary system prompts, or confidential retrieval data to unauthorized API consumers.
- [ ] **AIG-104** `P1` Propagate safe audit and correlation identifiers across model calls, retrieval steps, guardrails, and human approval actions.
- [ ] **AIG-105** `P2` Record the model, policy, prompt, retrieval, and tool configuration version associated with relevant AI responses for investigation.
- [ ] **AIG-106** `P0` Test multi-tenant isolation in vector searches, caches, prompts, conversation history, and tool results.
- [ ] **AIG-107** `P1` Verify moderation or safety gates fail according to an approved safe policy rather than silently bypassing checks during outages.
- [ ] **AIG-108** `P1` Exercise injection attempts and malicious tool or retrieved-document content against production-equivalent API permissions.
- [ ] **AIG-109** `P1` Monitor per-operation quality, refusal, incident, latency, error, and cost signals in proportion to the deployment risk.
- [ ] **AIG-110** `P1` Ensure API fallback or model substitution does not silently introduce an unapproved capability, data region, or policy change.

## Release gate

- [ ] The AI use case, appropriate non-AI alternatives, intended population, system boundaries, and responsible owners have been documented and approved.
- [ ] Significant foreseeable harms and applicable prohibited uses or legal/contractual obligations have been reviewed, with risk classification and accountable decisions recorded.
- [ ] Representative evaluation evidence meets predeclared task-quality and safety thresholds, including tests for consequential failures, adversarial inputs, and relevant population differences.
- [ ] Human-review, appeal, intervention, and emergency-disablement procedures have been tested for high-impact or externally acting AI workflows where appropriate.
- [ ] Model/provider licensing, processing terms, data handling, versioning, and change controls are reviewed; unauthorized access and unbounded tool actions are not permitted.
- [ ] API and frontend behavior clearly communicates AI limitations and errors and enforces approved roles, output handling, and user-facing disclosures where applicable.
- [ ] Monitoring, incident-response ownership, complaint intake, and change-triggered reevaluation are established for the deployed system.
- [ ] Material gaps or residual risks are either resolved or explicitly accepted by authorized owners with mitigation, review date, and conditions for suspension.

**Domain-specific approval rule:** Block AI governance sign-off if a prohibited use or unaccepted serious harm remains, a critical system action lacks required human authorization, major security/privacy exposures remain uncontrolled, or representative evaluation cannot support the intended use. Human approval must not be inferred from automated quality scores. This checklist does not establish ISO certification, NIST endorsement, or compliance with any specific jurisdiction's AI law.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#10_ai_evaluation_and_governance), not prerequisites or verification evidence.

## Trusted references and scope

These are primary and authoritative sources for cross-cutting AI risk and governance decisions. Recommendations from non-binding frameworks are not universal legal duties, and management-system standards do not themselves certify a particular AI deployment.

- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — voluntary AI risk framework and lifecycle-level assessment; NIST states the 1.0 framework is being revised.
- [NIST — AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) — Govern, Map, Measure, Manage actions; voluntary guidance, not an exhaustive mandatory checklist.
- [NIST — Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — cross-sector generative-AI risk categories and suggested mitigations.
- [ISO — ISO/IEC 42001:2023 AI management systems](https://www.iso.org/standard/42001) — requirements and guidance for an organizational AI management system; full standard requires separate access.
- [ISO — ISO/IEC 23894:2023 AI risk management](https://www.iso.org/standard/77304.html) — contextual AI risk identification, evaluation, and treatment; full guidance requires separate access.
- [OECD — AI Principles](https://oecd.ai/en/ai-principles) — non-binding principles for human rights, fairness, transparency, safety, and accountability.
- [OWASP — GenAI LLM Top 10 (2026)](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10) — current OWASP 2026 risks covering model-integrated application security; detailed threat modeling belongs in the Security and Red Teaming checklists.
- [European Commission — EU AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — changing phased application dates and categories for EU applicability review.
- [EUR-Lex — Regulation (EU) 2024/1689 (consolidated)](https://eur-lex.europa.eu/eli/reg/2024/1689) — official consolidated legal text; consult qualified advisers about the current provisions and their application.
- [European Commission — Navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act) — provider, deployer, transparency, and phased-application guidance.
- [NIST — AI RMF Manage function](https://airc.nist.gov/airmf-resources/playbook/manage/) — risk acceptance, monitoring, mitigation, and go/no-go decisions.
- [W3C WAI — How to Make Your Presentations Accessible to All](https://www.w3.org/WAI/teach-advocate/accessible-presentations/) — illustrative accessible information and communication practices where relevant.

**Applicability:** NIST AI RMF 1.0 and its Playbook are voluntary and were under revision as of this source review. ISO/IEC 42001 and 23894 are published standards with full texts subject to license/access; these links identify their scope but are not a substitute for reading licensed requirements. The EU AI Act has phased, revised application dates as of 2026; distinguish providers, deployers, risk classes, markets, and effective dates with qualified legal counsel. OWASP GenAI LLM Top 10 2026 applies primarily to relevant LLM-integrated systems. Only implement controls proportionate to system risk and actual interfaces.

**Source review date:** 2026-11-12.
