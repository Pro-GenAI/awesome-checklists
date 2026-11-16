# 16 — AI Red Teaming and Guardrails Checklist

> Verify that AI-enabled products have risk-based adversarial coverage and enforceable defenses against harmful outputs, unauthorized actions, data disclosure, and abuse. Red teaming seeks to discover failures; passing a finite test suite does not prove a model or product cannot be bypassed.

> **Scope: AI-specific.** This file is one part of the 16_AI_Red_Teaming_and_Guardrails.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Threat modeling and abuse cases

- [ ] **RED-001** `P2` Define the AI product's intended purpose, users, allowed content, model authority, external dependencies, and highest-consequence decisions.
- [ ] **RED-002** `P2` Assign named security, product, safety, privacy, and operational owners to the threat-model review and risk acceptance.
- [ ] **RED-003** `P2` Inventory models, prompts, retrieval collections, fine-tuning sources, guardrail services, tools, agents, and data-processing providers.
- [ ] **RED-004** `P2` Identify all trusted and untrusted entry points, including user messages, files, retrieved documents, websites, tool responses, and conversation memory.
- [ ] **RED-005** `P2` Map where content crosses boundaries between untrusted data, privileged instructions, authenticated identities, and executable tool actions.
- [ ] **RED-006** `P2` Identify sensitive assets such as secrets, protected customer data, proprietary prompts, privileged workflows, and financial operations.
- [ ] **RED-007** `P1` Enumerate plausible threats to confidentiality, integrity, availability, user safety, and trustworthy product decisions.
- [ ] **RED-008** `P1` Classify direct and indirect prompt injection, malicious context, forged tool messages, and instruction laundering as separate test surfaces.
- [ ] **RED-009** `P1` Model data poisoning in retrieval sources, memory, feedback loops, model artifacts, and other relevant supply-chain inputs.
- [ ] **RED-010** `P2` Identify excessive agency and privilege-escalation paths from model-suggested tool calls or delegated credentials.
- [ ] **RED-011** `P2` Consider cross-user, cross-tenant, and cross-session access and leakage via prompts, caches, retrieval, or persistent state.
- [ ] **RED-012** `P2` Identify risks from unsafe output handling, including generated markup, code, SQL, shell commands, and network destinations.
- [ ] **RED-013** `P1` Model misinformation, unsupported factual claims, harmful advice, and overconfident outputs where consequential to users.
- [ ] **RED-014** `P1` Assess possible discrimination, harassment, self-harm, or other safety policy failures within the application's allowed use case.
- [ ] **RED-015** `P1` Account for misuse of multimodal inputs, hidden document layers, captions, metadata, and mixed-script content when supported.
- [ ] **RED-016** `P2` Identify resource-exhaustion, denial-of-wallet, rate-limit evasion, and unbounded inference or tool-loop risks.
- [ ] **RED-017** `P2` Map attacker capabilities, reachable surfaces, likely preconditions, and expected impact without claiming the test set is exhaustive.
- [ ] **RED-018** `P1` Prioritize attack paths by severity, exposure, exploitability, and affected people, not just frequency in a benchmark.
- [ ] **RED-019** `P2` Define which unacceptable outcomes automatically block a release and what residual risks require human authorization.
- [ ] **RED-020** `P2` Identify tests that require specialist legal, privacy, child-safety, security, or domain expertise and obtain qualified review.
- [ ] **RED-021** `P2` Record authorized red-team scope, permitted environments, test identities, prohibited targets, and the response contact for exercises.
- [ ] **RED-022** `P1` Revisit the threat model when model versions, tool permissions, retrieval sources, markets, modalities, or guardrail configurations change.

## Adversarial evaluation

- [ ] **RED-023** `P1` Develop an adversarial test plan linked to the threat model, defined security objectives, and observable failure outcomes.
- [ ] **RED-024** `P1` Include a realistic benign control set so aggressive refusals are not mistaken for successful safeguards.
- [ ] **RED-025** `P1` Test direct attacks through authorized user input and indirect attacks through each actually supported untrusted content channel.
- [ ] **RED-026** `P1` Use sandboxed tools, dummy accounts, and synthetic secrets so testing cannot trigger live harmful or unauthorized side effects.
- [ ] **RED-027** `P1` Test prompt-injection attempts that impersonate trusted roles or try to override the application's instruction hierarchy.
- [ ] **RED-028** `P1` Test malicious directions hidden within retrieved text, file contents, tool responses, and formatted documents where relevant.
- [ ] **RED-029** `P1` Include encoding, obfuscation, Unicode confusables, and multilingual or code-switched attempts suitable for supported inputs.
- [ ] **RED-030** `P1` Test attacks that ask for internal instructions, authentication tokens, private user histories, or unauthorized documents using dummy values.
- [ ] **RED-031** `P1` Check whether an injection can change tool selection, arguments, permissions, destinations, or human-approval requirements.
- [ ] **RED-032** `P1` Test attempts to exploit multi-agent handoffs, shared memories, resumed sessions, and stale approval state where supported.
- [ ] **RED-033** `P1` Probe output handling with harmless simulated markup, code, commands, URLs, and structured payloads that must remain untrusted.
- [ ] **RED-034** `P1` Evaluate ingestion or retrieval poisoning with a controlled, reversible test corpus and independent source-access checks.
- [ ] **RED-035** `P1` Test whether the system refuses unsafe or disallowed tasks while still completing permitted tasks in the same domain.
- [ ] **RED-036** `P1` Include ambiguous, contradictory, boundary-condition, and missing-context prompts to evaluate safe clarification or abstention.
- [ ] **RED-037** `P1` Test long-context crowding, repeated turns, partial tool failures, and adversarially timed input within authorized limits.
- [ ] **RED-038** `P1` Exercise multimodal attack surfaces using synthetic test images, audio, or files where those modalities exist.
- [ ] **RED-039** `P1` Measure actual unauthorized actions, data disclosure, policy violations, and invalid outputs rather than relying only on refusal wording.
- [ ] **RED-040** `P1` Distinguish blocked attacks, successful attacks, inconclusive cases, and test-environment failures in results.
- [ ] **RED-041** `P2` Record attack identifier, intended violation, input channel, expected behavior, and observed outcome for every test case.
- [ ] **RED-042** `P1` Version the model, prompt, guardrails, tools, corpus, dataset, decoding settings, and test harness for each evaluation.
- [ ] **RED-043** `P1` Repeat nondeterministic cases within approved budgets to measure variability and avoid conclusions from a single passing sample.
- [ ] **RED-044** `P1` Report severity-weighted failure counts and attack success with explicit denominators, sampling limitations, and uncertainty where justified.
- [ ] **RED-045** `P1` Measure legitimate-request false-positive blocks, false-negative harmful passes, latency, and user-task completion together.
- [ ] **RED-046** `P1` Review adversarial case quality and automated judge decisions against competent human assessments on a representative sample.
- [ ] **RED-047** `P1` Retest fixed issues with regression cases and confirm remediations do not merely suppress visible error messages.
- [ ] **RED-048** `P1` Run targeted tests after each material change to the model, prompt, retrieval, tool permissions, guardrails, or user workflow.

## Content and tool guardrails

- [ ] **RED-049** `P2` Define a written policy for allowed, restricted, disallowed, and escalated content and actions that matches the deployed use case.
- [ ] **RED-050** `P1` Separate input screening, model response checking, tool-call authorization, and final user-visible output controls by their trust boundaries.
- [ ] **RED-051** `P1` Select moderation or classification tools suited to the supported modalities and documented policy categories.
- [ ] **RED-052** `P1` Validate guardrail accuracy with domain-specific allowed and prohibited examples, including ambiguous and long-tail cases.
- [ ] **RED-053** `P1` Measure classifier performance by language, modality, category, and relevant user context rather than assuming one global threshold is sufficient.
- [ ] **RED-054** `P2` Document moderation thresholds, manual-review routes, and the consequences of false positives and false negatives.
- [ ] **RED-055** `P1` Apply appropriate screening to retrieved documents and untrusted tool output in addition to the initial user request.
- [ ] **RED-056** `P1` Do not rely on prompt wording, delimiter syntax, regular expressions, or classifier verdicts as the sole authorization boundary.
- [ ] **RED-057** `P0` Enforce user, tenant, role, scope, resource, and destination permissions in trusted execution code for every consequential tool call.
- [ ] **RED-058** `P1` Validate model-generated tool names and arguments against allowlists, schemas, type constraints, and business invariants.
- [ ] **RED-059** `P1` Require action-specific authenticated human approval for risk-defined irreversible or high-impact tool actions before execution.
- [ ] **RED-060** `P1` Ensure guardrails that must block side effects run before those effects, including through handoffs, nested agents, and resumed tasks.
- [ ] **RED-061** `P1` Check the actual runtime's coverage of agent-level, tool-level, hosted-tool, and delegated-agent guardrail hooks.
- [ ] **RED-062** `P1` Choose fail-safe behavior for guardrail timeout, service outage, malformed verdict, or missing required classification.
- [ ] **RED-063** `P1` Test whether disabling or bypassing a guardrail causes the appropriate service degradation or blocks privileged actions.
- [ ] **RED-064** `P1` Prevent generated HTML, Markdown, scripts, SQL, and URLs from being used in sensitive downstream sinks without context-appropriate validation.
- [ ] **RED-065** `P1` Restrict code execution, filesystem access, browsing, and network egress to permitted sandboxes and destinations.
- [ ] **RED-066** `P1` Protect secrets and private data through scoped credentials and data minimization, not concealment in system prompts.
- [ ] **RED-067** `P1` Apply safe storage and rendering rules to uploaded and model-generated text, images, audio, and files where applicable.
- [ ] **RED-068** `P1` Check that policy changes and moderation model updates are versioned, reviewed, and tested for regressions.
- [ ] **RED-069** `P1` Limit input/output size, tokens, calls, retries, recursion depth, concurrency, and spend independently of model requests.
- [ ] **RED-070** `P1` Ensure safety filters do not silently erase important evidence needed for authorized incident investigation or escalation.
- [ ] **RED-071** `P2` Record guardrail decisions and tool authorization outcomes without retaining unnecessary sensitive full prompts or outputs.
- [ ] **RED-072** `P1` Test that user permissions and policy changes take effect in caches, sessions, agents, and pending tool executions.
- [ ] **RED-073** `P2` Define clear and auditable exception handling for allowed research, security testing, or regulated domain workflows.
- [ ] **RED-074** `P1` Reassess the entire guardrail chain after adding a new model, modality, connector, output channel, or privileged capability.

## Safety response and monitoring

- [ ] **RED-075** `P2` Define severity levels, containment actions, decision owners, and escalation timelines for AI-specific security and safety incidents.
- [ ] **RED-076** `P1` Instrument relevant safety events such as policy blocks, injection attempts, tool denials, data exposure indicators, and unsafe output reports.
- [ ] **RED-077** `P2` Track harmful-output passes and benign-task blocks with separate metrics to avoid optimizing only for refusals.
- [ ] **RED-078** `P1` Monitor changes in moderation results, refusal categories, policy exceptions, and observed failure rates across releases.
- [ ] **RED-079** `P1` Monitor anomalous tool sequences, unusual destinations, privilege requests, repeated abuse attempts, and cost spikes where relevant.
- [ ] **RED-080** `P2` Record safe identifiers for model, prompt, policy, guardrail, tool, dataset, and release versions to support investigations.
- [ ] **RED-081** `P1` Restrict access to security telemetry and redact protected content, credentials, and test secrets by policy.
- [ ] **RED-082** `P1` Set actionable alert thresholds with named responders and test routing before production exposure.
- [ ] **RED-083** `P2` Define procedures to freeze a rollout, disable a capability, revoke credentials, quarantine data, or suspend a connector.
- [ ] **RED-084** `P1` Test that emergency suspension reaches active runs, queued actions, child agents, and external integrations where feasible.
- [ ] **RED-085** `P1` Ensure error handling does not substitute a fabricated success, source citation, or action confirmation after a safety stop.
- [ ] **RED-086** `P1` Provide safe user messaging for blocked requests, uncertain outcomes, service failures, and human escalation.
- [ ] **RED-087** `P1` Offer a visible user reporting channel for harmful, inaccurate, or unauthorized AI behavior where users interact with the system.
- [ ] **RED-088** `P1` Ensure reporting and complaint workflows distinguish immediate safety concerns from normal quality feedback.
- [ ] **RED-089** `P2` Record significant findings with owners, severity, mitigation, user impact, and validated retest evidence in project-specific records.
- [ ] **RED-090** `P2` Define appropriate customer, partner, regulator, or provider notification review when exposure or contractual obligations may apply.
- [ ] **RED-091** `P1` Review incidents for root causes involving model behavior, unsafe tool authority, guardrail gaps, and organizational process.
- [ ] **RED-092** `P1` Add confirmed incidents and newly discovered attack paths to maintained regression suites using sanitized fixtures.
- [ ] **RED-093** `P1` Reassess thresholds, monitoring, and escalation arrangements as traffic, threat patterns, and supported languages change.
- [ ] **RED-094** `P1` Perform post-deployment safety review during initial canary exposure and after material model or policy updates.
- [ ] **RED-095** `P1` Train designated reviewers on automation bias, sensitive data handling, escalation limits, and evidence preservation.
- [ ] **RED-096** `P2` Track residual high-severity risks and prohibit release without explicit qualified authorization and documented mitigations.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **RED-117** `P1` Clearly identify the AI feature's intended use, meaningful limitations, and the types of requests it may reject or escalate.
- [ ] **RED-118** `P1` Distinguish a policy refusal, an uncertain answer, a request for human review, and a system error in user-visible feedback.
- [ ] **RED-119** `P1` Provide an accessible way to appeal false blocks or report harmful generated output where appropriate.
- [ ] **RED-120** `P1` Explain when an external action requires explicit confirmation and do not present a proposed action as completed.
- [ ] **RED-121** `P1` Require comprehensible user approval for material transactions, messages, publishing, or other consequential tool actions.
- [ ] **RED-122** `P1` Ensure safety notices, refusals, and reporting flows remain usable with keyboard and assistive technologies.
- [ ] **RED-123** `P1` Test supported languages and scripts for appropriate safety messaging and overblocking of legitimate requests.
- [ ] **RED-124** `P1` Protect user-upload previews, model-generated markup, and linked content from active script injection or misleading destinations.
- [ ] **RED-125** `P1` Verify that sensitive text, tokens, uploads, and safety reports are not unnecessarily stored in browser logs or analytics.
- [ ] **RED-126** `P1` Test streaming interfaces so blocked or incomplete content does not appear as a finalized approved answer.
- [ ] **RED-127** `P1` Provide useful recovery options after refusal, moderation errors, network loss, or a guardrail service failure.
- [ ] **RED-128** `P1` Explain human-review waiting states, relevant data use, and expected escalation path without promising unavailable support.
- [ ] **RED-129** `P1` Make it possible to stop, cancel, or retract supported ongoing AI actions and communicate any irreversible side effects.
- [ ] **RED-130** `P1` Test authentication changes, shared-device use, and tenant switching for leaked protected responses or review history.
- [ ] **RED-131** `P1` Check that safety controls and user reports still work in mobile, offline, screen-reader, and low-bandwidth scenarios as relevant.
- [ ] **RED-132** `P1` Ensure generated citations, evidence links, and safety disclaimers do not misleadingly imply independent verification.
- [ ] **RED-133** `P1` Assess whether users understand model limitations and avoid unsafe overreliance in representative task testing.
- [ ] **RED-134** `P1` Provide clear consequences and recovery for content that is moderated after initial streaming or draft display.
- [ ] **RED-135** `P1` Ensure frontend feature flags align with approved API guardrail and model versions during staged rollouts.
- [ ] **RED-136** `P1` Verify safety-related feedback, user complaints, and critical UI failures are routed to monitored incident channels.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#16_ai_red_teaming_and_guardrails), not prerequisites or evidence of PASS.

## Trusted references and scope

**2026 source update:** See the [AI source-currency watch](../references/ai-source-watch.md) for verified NIST/OWASP 2026 editions and the amended EU AI Act timeline. Use current official publications for applicability; source lists do not certify compliance.



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

**Source review date:** 2026-11-12; headline AI-risk sources rechecked 2026-11-15.
