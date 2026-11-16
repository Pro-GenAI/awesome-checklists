# 09 — Prompt Engineering and Versioning Checklist

> Review instructions, templates, prompt revisions, and evaluation gates used in model-integrated software. Treat prompt wording as a behavioral control and engineering artifact, not a guarantee of security or deterministic correctness. Protect trust boundaries and external actions with independent code-level authorization.

> **Scope: AI-specific.** This file is one part of the 09_Prompt_Engineering_and_Versioning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Prompt design and requirements

- [ ] **PROMPT-001** `P2` Define the intended task, user population, allowed inputs, and desired business outcome for every production prompt.
- [ ] **PROMPT-002** `P2` Identify the approved model family or snapshot and any provider-specific behavior the prompt depends on.
- [ ] **PROMPT-003** `P2` Document the output's intended audience, expected level of detail, and appropriate language or tone.
- [ ] **PROMPT-004** `P2` Specify measurable task-success criteria and disallowed outcomes before iterating on prompt wording.
- [ ] **PROMPT-005** `P2` Assign a named engineering owner and product or domain approver to each critical prompt.
- [ ] **PROMPT-006** `P1` Distinguish trusted application instructions, end-user requests, retrieved documents, and tool output in the prompt design.
- [ ] **PROMPT-007** `P1` Express essential requirements with clear, noncontradictory instructions and explicit priorities.
- [ ] **PROMPT-008** `P2` Describe the scope and limits of the assistant's role without overstating expertise, factual certainty, or authority.
- [ ] **PROMPT-009** `P2` Define what the model should do when information is absent, contradictory, stale, or outside its permitted task.
- [ ] **PROMPT-010** `P2` Specify when the assistant must ask for clarification, abstain, escalate, or hand off to a human.
- [ ] **PROMPT-011** `P2` Define how citations or source evidence must support claims when the task requires grounded answers.
- [ ] **PROMPT-012** `P1` Choose an output contract such as structured JSON, prose, or tool arguments that downstream consumers can validate.
- [ ] **PROMPT-013** `P2` Describe any safety, privacy, legal, or accessibility restrictions relevant to the application's task.
- [ ] **PROMPT-014** `P2` Specify the permitted external actions and which actions require explicit, action-specific approval.
- [ ] **PROMPT-015** `P1` Include a representative set of positive and negative examples only when they improve measured task quality.
- [ ] **PROMPT-016** `P1` Ensure examples are diverse and reflect realistic inputs, languages, edge cases, and expected outputs.
- [ ] **PROMPT-017** `P1` Check that examples do not accidentally teach unwanted biases, shortcuts, or unsafe behavior.
- [ ] **PROMPT-018** `P1` Use clear delimiters or structured messages to separate instructions, context, examples, and variable inputs.
- [ ] **PROMPT-019** `P1` Avoid relying on particular delimiters, polite wording, or hidden text as a security or authorization boundary.
- [ ] **PROMPT-020** `P1` Remove redundant, conflicting, stale, or excessively prescriptive instructions that worsen measured output quality.
- [ ] **PROMPT-021** `P2` Document model-specific prompting techniques and avoid assuming instructions work identically across vendors or snapshots.
- [ ] **PROMPT-022** `P1` Set explicit prompt length, token, latency, and inference cost budgets appropriate to the user journey.

## Templates and input handling

- [ ] **PROMPT-023** `P1` Store approved prompt templates in reviewed application code or another supported, versioned configuration system.
- [ ] **PROMPT-024** `P2` Define each template variable with a type, purpose, source, allowable length, and validation policy.
- [ ] **PROMPT-025** `P1` Render untrusted user and external content as data values rather than executable template source.
- [ ] **PROMPT-026** `P1` Use a template rendering system that does not evaluate arbitrary expressions from user-controlled text.
- [ ] **PROMPT-027** `P1` Keep developer/system instructions separate from untrusted user, document, search, or tool-provided content wherever the model API supports roles.
- [ ] **PROMPT-028** `P2` Identify and label retrieved passages or tool results as untrusted evidence, while recognizing labels are not an enforcement boundary.
- [ ] **PROMPT-029** `P1` Validate inputs before invoking provider APIs, including modality, size, encoding, and supported formats.
- [ ] **PROMPT-030** `P1` Apply appropriate truncation, summarization, or chunking policies and document what information may be lost.
- [ ] **PROMPT-031** `P1` Budget system instructions, conversation history, retrieved context, tools, and expected output within the selected model context window.
- [ ] **PROMPT-032** `P1` Verify that context-window overflow and provider truncation do not silently discard critical instructions or necessary evidence.
- [ ] **PROMPT-033** `P1` Check that conversation-history selection does not mix one user's or tenant's data into another context.
- [ ] **PROMPT-034** `P2` Define expiration and deletion of prompt variables, retrieved content, and conversation history according to policy.
- [ ] **PROMPT-035** `P1` Ensure prompts and examples never contain real API keys, production secrets, or unnecessary protected personal information.
- [ ] **PROMPT-036** `P1` Protect internal prompt templates and proprietary context with appropriate code/configuration access controls.
- [ ] **PROMPT-037** `P1` Treat model outputs as untrusted for HTML, code execution, SQL, command invocation, and downstream integrations.
- [ ] **PROMPT-038** `P1` Enforce tool permissions and action-specific approvals in deterministic code rather than relying on model obedience.
- [ ] **PROMPT-039** `P1` Validate model-generated structured outputs and tool arguments against strict schemas at execution boundaries.
- [ ] **PROMPT-040** `P1` Test direct and indirect prompt-injection attempts across user, document, web, tool, and history channels.
- [ ] **PROMPT-041** `P1` Test disguised instructions, encoded content, unexpected markup, and multilingual variations with authorized harmless fixtures.
- [ ] **PROMPT-042** `P1` Measure false refusals on legitimate inputs alongside successful blocking of malicious requests.
- [ ] **PROMPT-043** `P2` Specify stable error handling for malformed variables, missing placeholders, oversized inputs, and failed template rendering.
- [ ] **PROMPT-044** `P1` Confirm request logging, traces, and debugging tools exclude prohibited sensitive prompt data and confidential templates.

## Versioning and change management

- [ ] **PROMPT-045** `P2` Assign an immutable identifier to every production prompt revision and link it to the related feature or workflow.
- [ ] **PROMPT-046** `P1` Keep prompt source in version control with a reviewable history, author, date, and reason for the change.
- [ ] **PROMPT-047** `P1` Capture the exact model snapshot or provider revision associated with each approved prompt version.
- [ ] **PROMPT-048** `P1` Version dependent tool schemas, retrieved-context instructions, safety policies, and output validators together with prompts.
- [ ] **PROMPT-049** `P1` Distinguish prompt content changes from model, temperature, tool, retrieval, and other configuration changes during reviews.
- [ ] **PROMPT-050** `P1` Require review by the responsible domain and safety/security owners for material behavior changes.
- [ ] **PROMPT-051** `P2` Define a risk-based approval process for low-risk copy changes versus changes to tool access, data processing, or sensitive decisions.
- [ ] **PROMPT-052** `P2` Maintain separate development, evaluation, staging, and approved production prompt configurations.
- [ ] **PROMPT-053** `P1` Deploy immutable prompt revisions or recorded code releases rather than mutable, untracked 'latest' behavior.
- [ ] **PROMPT-054** `P2` Document any provider-managed prompt feature's support lifecycle and a migration path if it is deprecated.
- [ ] **PROMPT-055** `P1` Use an auditable release process linking prompt revision, artifact, evaluation results, and approver.
- [ ] **PROMPT-056** `P1` Run required evaluation checks before promoting a prompt revision to production.
- [ ] **PROMPT-057** `P1` Use canary exposure, feature flags, or equivalent staged rollout controls for high-impact prompt changes.
- [ ] **PROMPT-058** `P2` Define measurable post-deployment health signals and rollback conditions for changed prompts.
- [ ] **PROMPT-059** `P1` Keep an approved previous prompt revision and compatible model/configuration available for rollback where feasible.
- [ ] **PROMPT-060** `P1` Confirm rollback does not silently break output schemas, stored conversations, or client expectations.
- [ ] **PROMPT-061** `P1` Require reevaluation when the model version changes even if the prompt text remains unchanged.
- [ ] **PROMPT-062** `P1` Review the user experience and safety implications of prompt changes after incident findings or customer complaints.
- [ ] **PROMPT-063** `P2` Track deprecation or retirement of unused prompts and prevent obsolete versions from being called accidentally.
- [ ] **PROMPT-064** `P2` Record migration guidance for teams and APIs consuming a prompt whose output contract has changed.
- [ ] **PROMPT-065** `P1` Audit access to production prompt editing and promotion, and remove obsolete editor permissions.
- [ ] **PROMPT-066** `P2` Document ownership and expiry for emergency prompt hotfixes, with retrospective review and regression testing.

## Prompt evaluation and regression

- [ ] **PROMPT-067** `P2` Define representative evaluation fixtures based on realistic production tasks and approved synthetic or sanitized data.
- [ ] **PROMPT-068** `P1` Keep a held-out regression set separate from examples used to tune the prompt.
- [ ] **PROMPT-069** `P2` Define task-specific acceptance thresholds for accuracy, completeness, helpfulness, factuality, and format compliance where relevant.
- [ ] **PROMPT-070** `P1` Include expected refusals, clarifications, abstentions, and human escalation cases.
- [ ] **PROMPT-071** `P1` Evaluate ambiguous, adversarial, multilingual, long-context, and missing-context prompts appropriate to deployment risk.
- [ ] **PROMPT-072** `P1` Test both typical and severe-error cases rather than relying only on a small set of happy paths.
- [ ] **PROMPT-073** `P1` Compare prompt candidates against the same model and environment configuration before attributing score changes to prompt text.
- [ ] **PROMPT-074** `P1` Compare new prompt revisions against the last approved production baseline using paired or otherwise comparable cases.
- [ ] **PROMPT-075** `P2` Record prompt/model version, variable fixtures, decoding parameters, evaluation harness, and evaluator versions for every run.
- [ ] **PROMPT-076** `P1` Repeat stochastic tests sufficiently to characterize output variance when results may change between runs.
- [ ] **PROMPT-077** `P1` Use objective assertions for schemas, required fields, forbidden side effects, and supported format constraints.
- [ ] **PROMPT-078** `P1` Use qualified human rubrics where there is no single correct output or automated metrics are insufficient.
- [ ] **PROMPT-079** `P1` Calibrate model-based graders against human judgments before trusting their scores or letting them block deployment.
- [ ] **PROMPT-080** `P1` Test graders for positional, verbosity, language, and self-preference bias when applicable.
- [ ] **PROMPT-081** `P1` Assess how well retrieved evidence and actual output citations support claims for grounded tasks.
- [ ] **PROMPT-082** `P1` Evaluate safety refusals and false positives together so a system that refuses all requests is not deemed successful.
- [ ] **PROMPT-083** `P1` Test prompt injection against meaningful trust boundaries and verify tool permissions independently.
- [ ] **PROMPT-084** `P1` Report security outcomes from observed tool actions and data access, not just harmless-sounding model responses.
- [ ] **PROMPT-085** `P1` Measure p50/p95 latency, output length, token usage, and cost impact of prompt revisions under representative workload.
- [ ] **PROMPT-086** `P1` Test expected structured outputs across error conditions, partial outputs, tool call branches, and streaming where applicable.
- [ ] **PROMPT-087** `P1` Verify multi-turn state and long-context behavior, including stale instructions and conflicting conversational requests.
- [ ] **PROMPT-088** `P1` Include high-impact policy and regulated-workflow cases reviewed by appropriate domain specialists.
- [ ] **PROMPT-089** `P2` Track per-case regressions and severe failures with owners and remediation rather than hiding them in averaged scores.
- [ ] **PROMPT-090** `P1` Collect post-release feedback and incidents as candidates for privacy-preserving regression tests.
- [ ] **PROMPT-091** `P2` Define stop/go criteria and require documented risk acceptance when a new prompt regresses a material metric.
- [ ] **PROMPT-092** `P1` Rerun targeted and full evaluations after changes to provider snapshots, tools, retrieval, or safety controls.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **PROMPT-113** `P1` Confirm user-facing descriptions accurately reflect what the current prompt-supported feature can and cannot do.
- [ ] **PROMPT-114** `P1` Show uncertainty, requests for missing context, and refusals clearly without implying the AI verified unsupported facts.
- [ ] **PROMPT-115** `P1` Distinguish model-generated content from user-authored text, authoritative source excerpts, and confirmed system actions.
- [ ] **PROMPT-116** `P1` Provide an accessible way to correct input, refine a request, retry, or escalate when prompt behavior is inadequate.
- [ ] **PROMPT-117** `P1` Ensure suggested prompts and examples do not imply capabilities or authorizations absent from the deployed API.
- [ ] **PROMPT-118** `P1` Check multilingual and localized prompt suggestions against supported model behavior and policy restrictions.
- [ ] **PROMPT-119** `P1` Test long, malformed, and mixed-script inputs against actual template and context size limits.
- [ ] **PROMPT-120** `P1` Provide understandable error or warning states when the input exceeds supported length or attachments are not processed.
- [ ] **PROMPT-121** `P1` Keep streaming content and intermediate drafts distinguishable from final verified actions or completed results.
- [ ] **PROMPT-122** `P1` Validate output formatting for lists, code, tables, citations, JSON-derived UI, and unexpected model responses.
- [ ] **PROMPT-123** `P1` Render generated markup safely and avoid allowing responses to inject executable HTML or scripts.
- [ ] **PROMPT-124** `P1` Confirm high-impact action previews and confirmation steps cannot be bypassed through prompt wording.
- [ ] **PROMPT-125** `P1` Ensure user-specific draft content and history are isolated across account switches, sessions, and browser storage.
- [ ] **PROMPT-126** `P1` Do not display internal prompt instructions, model credentials, or confidential debugging metadata in the client.
- [ ] **PROMPT-127** `P1` Test screen-reader announcements, keyboard interaction, and focus behavior for streaming answers and clarifications.
- [ ] **PROMPT-128** `P1` Check how UI behaves if a prompt revision changes tone, length, response structure, or allowed requests.
- [ ] **PROMPT-129** `P1` Validate that frontend feature flags map to approved server-side prompt versions and support safe rollback.
- [ ] **PROMPT-130** `P1` Collect appropriately consented feedback with prompt revision context without logging sensitive full user input unnecessarily.
- [ ] **PROMPT-131** `P1` Test user journeys with prompt-triggered refusals, model errors, timeouts, and tool failures on representative devices.
- [ ] **PROMPT-132** `P1` Confirm post-release UI monitoring can identify prompt-version-specific regressions and harmful user experiences.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#09_prompt_engineering_and_versioning), not prerequisites or evidence of PASS.

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
