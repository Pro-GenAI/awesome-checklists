# 03 — AI Evaluation and Governance Checklist

> Review whether a proposed AI use is appropriate, its risks are understood, the system has credible evaluation evidence, human oversight is operational, and organizational accountability is maintained across its lifecycle. This cross-cutting checklist complements detailed model, RAG, agent, red-team, data, and monitoring templates in their respective AI domain checklists.

> **Scope: AI-specific.** This file is one part of the 03_AI_Evaluation_and_Governance.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## AI use-case and risk definition

- [ ] **AIG-001** `P2` Describe the intended AI-assisted task, user groups, operating context, and expected benefit in terms that can be evaluated.
- [ ] **AIG-002** `P1` Determine whether a non-AI solution could achieve the same user outcome with lower risk or operational complexity.
- [ ] **AIG-003** `P2` Identify the AI system owner, business sponsor, model/application operator, and accountable release approver.
- [ ] **AIG-004** `P2` Maintain an inventory of in-scope AI models, providers, versions, datasets, prompts, retrieval sources, tools, and deployment locations.
- [ ] **AIG-005** `P1` Classify the system by potential impact and likelihood of harm using a documented, project-appropriate risk methodology.
- [ ] **AIG-006** `P2` Identify affected people, bystanders, downstream recipients, and vulnerable populations who may bear different risks.
- [ ] **AIG-007** `P2` Map foreseeable normal use, misuse, out-of-scope use, and high-consequence failure scenarios across the full user journey.
- [ ] **AIG-008** `P2` Record whether AI outputs inform or determine decisions in health, employment, education, finance, safety, legal, or other consequential contexts.
- [ ] **AIG-009** `P1` Assess potential physical, psychological, economic, reputational, privacy, security, and societal impacts relevant to the deployment.
- [ ] **AIG-010** `P2` Identify discrimination or disparate-impact risks across relevant groups and contexts using lawful, appropriate data and methods.
- [ ] **AIG-011** `P2` Define unacceptable uses, prohibited outcomes, and risk tolerance before design or release approval.
- [ ] **AIG-012** `P1` Assess whether the system should use generation, classification, retrieval, prediction, ranking, or deterministic rules for each task.
- [ ] **AIG-013** `P2` Map the trust boundaries between user content, retrieved data, model instructions, tool results, APIs, and privileged operations.
- [ ] **AIG-014** `P2` Identify data sensitivity, provenance, intellectual-property restrictions, and permitted processing purposes before using external AI services.
- [ ] **AIG-015** `P1` Review model-provider geography, data handling, subprocessor, and retention terms against the intended data flows.
- [ ] **AIG-016** `P2` Document AI capability limitations, missing knowledge, uncertainty, and circumstances requiring abstention or escalation.
- [ ] **AIG-017** `P1` Evaluate how users may over-rely on seemingly authoritative outputs, including automation bias and misunderstood confidence.
- [ ] **AIG-018** `P2` Identify the jurisdictions, deployment roles, and AI-specific legal or contractual requirements that require qualified review.
- [ ] **AIG-019** `P1` Assess EU AI Act applicability and changing phased deadlines for any relevant EU-market use case using current official guidance.
- [ ] **AIG-020** `P2` Record the risk classification, assumptions, material open issues, and the decision whether this AI use case is justified.
- [ ] **AIG-021** `P2` Define clear boundaries for any external actions, financial commitments, messages, or changes the AI system may initiate.
- [ ] **AIG-022** `P1` Reassess risk assumptions when the model, audience, context, connected tools, or policy requirements materially change.

## Evaluation approach

- [ ] **AIG-023** `P2` Define measurable task success criteria and unacceptable failures before selecting an evaluation dataset or model.
- [ ] **AIG-024** `P1` Select evaluation metrics appropriate to the use case, including task quality, accuracy, recall, consistency, abstention, and error severity where relevant.
- [ ] **AIG-025** `P0` Set explicit acceptance thresholds, review rules, and responsible approvers for high-impact outcomes.
- [ ] **AIG-026** `P1` Establish a deterministic or human-workflow baseline where feasible to show the added value of the AI system.
- [ ] **AIG-027** `P1` Create representative test cases covering routine, ambiguous, long-tail, multilingual, and high-impact scenarios in the target population.
- [ ] **AIG-028** `P1` Include realistic user goals and full workflow context rather than evaluating only isolated model text outputs.
- [ ] **AIG-029** `P1` Include clearly defined negative tests for prohibited behaviors, unsupported requests, and out-of-scope questions.
- [ ] **AIG-030** `P1` Evaluate factual accuracy and unsupported assertions against trusted references when factual outputs are expected.
- [ ] **AIG-031** `P1` Assess whether the system states uncertainty, asks for missing context, and abstains or escalates appropriately.
- [ ] **AIG-032** `P1` Evaluate whether model outputs include unsafe instructions, privacy leaks, harmful stereotyping, or discriminatory outcomes relevant to the context.
- [ ] **AIG-033** `P1` Test prompt injection, malicious retrieved content, untrusted tool output, and attempted instruction or permission escalation at system boundaries.
- [ ] **AIG-034** `P1` Test whether tool-use authorization and external side effects remain controlled under adversarial and ambiguous inputs.
- [ ] **AIG-035** `P1` Measure false positives and false negatives separately where errors have materially different costs.
- [ ] **AIG-036** `P1` Evaluate performance by justified subgroups, languages, devices, and operating environments while avoiding unlawful or unreliable inference.
- [ ] **AIG-037** `P1` Separate development, tuning, validation, and final held-out evaluation data to reduce contamination and overfitting.
- [ ] **AIG-038** `P2` Track test set provenance, allowed use, version, sampling limitations, and changes to expected outcomes.
- [ ] **AIG-039** `P1` Use appropriate human evaluation rubrics, reviewer qualification, and adjudication of disagreements where automated scores are insufficient.
- [ ] **AIG-040** `P1` Validate that model-based judges or automated evaluators align with competent human assessments before relying on their scores.
- [ ] **AIG-041** `P1` Check evaluator bias, judge position sensitivity, scoring drift, and failure to identify harmful outputs where applicable.
- [ ] **AIG-042** `P1` Report confidence intervals, sample sizes, uncertainty, and critical-error counts when interpreting quantitative results.
- [ ] **AIG-043** `P1` Run repeat evaluations under controlled settings to characterize nondeterminism and meaningful output variability.
- [ ] **AIG-044** `P2` Record model, prompt, retrieval, tool, guardrail, dataset, and configuration versions for every acceptance result.
- [ ] **AIG-045** `P1` Evaluate changes against a trusted baseline and flag regressions in safety, fairness, task quality, and user-impacting behavior.
- [ ] **AIG-046** `P2` Document limitations of benchmarks and offline datasets, including where they may not predict real-world outcomes.
- [ ] **AIG-047** `P1` Include staged or shadow evaluation with controlled real-world signals when risk and data permissions permit.
- [ ] **AIG-048** `P1` Ensure serious failures have clear owner, severity, remediation action, and retest requirements before sign-off.

## Human oversight and accountability

- [ ] **AIG-049** `P2` Assign responsibility for AI policy, deployment approval, operational oversight, user complaints, and model-incident escalation.
- [ ] **AIG-050** `P2` Define which decisions AI may support, which require human approval, and which must remain fully human-controlled.
- [ ] **AIG-051** `P2` Identify high-impact or irreversible actions and require an appropriately authorized human checkpoint before execution.
- [ ] **AIG-052** `P1` Ensure reviewers have enough context, source material, and system limitations to make independent decisions.
- [ ] **AIG-053** `P1` Give authorized humans practical means to pause, override, reject, correct, or disable unsafe AI behavior.
- [ ] **AIG-054** `P1` Test that escalation to a human actually reaches a responsible person within an appropriate service window.
- [ ] **AIG-055** `P2` Define who can approve exceptional AI uses, accept residual risks, and revoke earlier approval.
- [ ] **AIG-056** `P1` Train reviewers on automation bias, hallucinations, limitations, relevant safety risks, and appropriate verification methods.
- [ ] **AIG-057** `P1` Set workload and escalation limits that make genuine human review feasible rather than purely nominal.
- [ ] **AIG-058** `P1` Distinguish recommendations, drafts, and automated decisions in internal workflows and customer interactions.
- [ ] **AIG-059** `P2` Define a clear process for users to report harmful, incorrect, or discriminatory AI outputs and request follow-up.
- [ ] **AIG-060** `P1` Provide a route for contesting or seeking human review of consequential AI-supported outcomes where appropriate or legally required.
- [ ] **AIG-061** `P2` Document when users and affected parties must be informed they are interacting with an AI system or receiving AI-generated content.
- [ ] **AIG-062** `P1` Ensure user-facing disclosures accurately describe capabilities, limits, available human assistance, and relevant data handling.
- [ ] **AIG-063** `P2` Define the criteria and authorized process for suspending AI features after a serious incident or evidence of emerging harm.
- [ ] **AIG-064** `P1` Keep incident records including affected scope, causal hypotheses, temporary mitigations, user notifications, and corrective actions.
- [ ] **AIG-065** `P1` Review anonymized or appropriately protected user feedback and incident trends for previously unrecognized harms.
- [ ] **AIG-066** `P1` Ensure accountability for AI-generated external communications, transactions, or changes remains with a named human or organization.
- [ ] **AIG-067** `P1` Test handoff, appeal, and emergency-disablement paths rather than relying on policy documents alone.
- [ ] **AIG-068** `P1` Review oversight and escalation arrangements after staffing, supplier, or critical workflow changes.

## Model and policy governance

- [ ] **AIG-069** `P2` Maintain an AI system register identifying owners, use case, model/provider versions, deployment context, risk class, and approval state.
- [ ] **AIG-070** `P2` Define a documented AI governance policy covering acceptable use, prohibited uses, data handling, human oversight, and incident response.
- [ ] **AIG-071** `P2` Assign review responsibilities across product, engineering, security, privacy, legal, domain experts, and affected-user representatives as warranted.
- [ ] **AIG-072** `P1` Keep decisions and risk treatments traceable to owners, review dates, evidence, and residual-risk acceptance.
- [ ] **AIG-073** `P2` Document the provenance, licensing, allowed purposes, and known restrictions of models and third-party AI components.
- [ ] **AIG-074** `P1` Review supplier contracts, usage policies, data-processing terms, audit rights, retention, and model-change notification practices.
- [ ] **AIG-075** `P2` Maintain model or system documentation describing intended uses, capabilities, evaluation results, known limitations, and warnings.
- [ ] **AIG-076** `P2` Identify training, fine-tuning, retrieval, or feedback data that could introduce bias, sensitive information, or intellectual-property risk.
- [ ] **AIG-077** `P2` Define controls to prevent unauthorized training or secondary use of customer data by internal systems or suppliers where prohibited.
- [ ] **AIG-078** `P2` Document prompt, system policy, retrieval configuration, guardrail, tool permissions, and model changes through version-controlled review.
- [ ] **AIG-079** `P1` Set a change classification that distinguishes low-risk prompt/content edits from significant model, capability, autonomy, and data-use changes.
- [ ] **AIG-080** `P1` Require renewed evaluation and authorization before material changes to intended purpose, model, tool authority, or deployment audience.
- [ ] **AIG-081** `P2` Define operational monitors for unexpected outputs, misuse, policy violations, user complaints, cost, and model-quality degradation.
- [ ] **AIG-082** `P1` Establish a controlled incident response for AI-specific failures, including containment, investigation, remediation, and notification owners.
- [ ] **AIG-083** `P2` Document how AI features can be rolled back, disabled, or routed to a safe alternative without corrupting user work.
- [ ] **AIG-084** `P1` Set retention and restricted access for evaluations, prompts, model inputs/outputs, incident records, and audit artifacts.
- [ ] **AIG-085** `P1` Reassess regulatory applicability and required documentation against the law and effective dates relevant to the deployment.
- [ ] **AIG-086** `P1` Distinguish voluntary NIST/OECD guidance and ISO management-system practices from mandatory laws and contract clauses.
- [ ] **AIG-087** `P1` Require a qualified compliance review before asserting conformity, certification, or legal approval for the system.
- [ ] **AIG-088** `P2` Define supplier-exit, model-replacement, and data-deletion plans for critical third-party AI dependencies.
- [ ] **AIG-089** `P2` Assign periodic policy review, independent challenge, and management reporting proportional to risk.
- [ ] **AIG-090** `P2` Record the justification for accepting residual harm risks and the conditions that require reconsidering approval.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **AIG-111** `P1` Tell users when they are interacting with an AI system or viewing AI-generated outputs where appropriate or required.
- [ ] **AIG-112** `P1` Explain the AI feature's intended use, major limitations, and the kinds of decisions that still require human verification.
- [ ] **AIG-113** `P1` Distinguish AI-generated suggestions from verified source material, user-authored content, and completed system actions.
- [ ] **AIG-114** `P1` Present citations, retrieved evidence, and confidence indicators accurately, without implying proof that a cited source supports an unsupported claim.
- [ ] **AIG-115** `P1` Provide clear feedback when the system lacks information, declines a request, or cannot reliably complete a task.
- [ ] **AIG-116** `P1` Make important prompts, generated content, and pending changes reviewable before committing irreversible actions.
- [ ] **AIG-117** `P1` Provide clear confirmation of what tool actions were actually executed and how users can undo or contest them.
- [ ] **AIG-118** `P1` Offer a practical way to edit, reject, regenerate, correct, or report AI-generated outputs as the workflow permits.
- [ ] **AIG-119** `P1` Provide an accessible path to a qualified human or non-AI alternative for high-impact or failed interactions when warranted.
- [ ] **AIG-120** `P1` Explain the handling and retention of user-entered information, uploads, and feedback as required by applicable policy.
- [ ] **AIG-121** `P1` Avoid interface language that overstates model reliability, expertise, consciousness, authority, or guaranteed correctness.
- [ ] **AIG-122** `P1` Display important data-privacy, sensitive-information, and unsafe-use warnings at the point users may submit relevant content.
- [ ] **AIG-123** `P1` Ensure safety interventions, refusals, and escalation messages are comprehensible with keyboard and assistive technology.
- [ ] **AIG-124** `P1` Design clear loading, streaming, timeout, cancellation, and partial-result behavior without implying unfinished content is final.
- [ ] **AIG-125** `P1` Prevent accidental repeated purchases, submissions, or privileged tool actions from duplicate clicks and retries.
- [ ] **AIG-126** `P1` Label generated or modified images, audio, and video where the product's applicable disclosure obligations require it.
- [ ] **AIG-127** `P1` Test the user experience when results contain misleading claims, discriminatory language, personal data, or prohibited content.
- [ ] **AIG-128** `P1` Ensure feedback and appeal controls preserve enough context for authorized review without exposing another user's information.
- [ ] **AIG-129** `P1` Use user research to assess automation bias and whether people understand when AI output should not be trusted.
- [ ] **AIG-130** `P1` Confirm frontend release flags, model versions, content notices, and human-review paths match approved production policy.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#03_ai_evaluation_and_governance), not prerequisites or evidence of PASS.

## Trusted references and scope

**2026 source update:** See the [AI source-currency watch](../references/ai-source-watch.md) for verified NIST/OWASP 2026 editions and the amended EU AI Act timeline. Use current official publications for applicability; source lists do not certify compliance.



These are primary and authoritative sources for cross-cutting AI risk and governance decisions. Recommendations from non-binding frameworks are not universal legal duties, and management-system standards do not themselves certify a particular AI deployment.

- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — voluntary AI risk framework and lifecycle-level assessment; NIST states the 1.0 framework is being revised.
- [NIST — AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) — Govern, Map, Measure, Manage actions; voluntary guidance, not an exhaustive mandatory checklist.
- [NIST — Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — cross-sector generative-AI risk categories and suggested mitigations.
- [ISO — ISO/IEC 42001:2023 AI management systems](https://www.iso.org/standard/42001) — requirements and guidance for an organizational AI management system; full standard requires separate access.
- [ISO — ISO/IEC 23894:2023 AI risk management](https://www.iso.org/standard/77304.html) — contextual AI risk identification, evaluation, and treatment; full guidance requires separate access.
- [OECD — AI Principles](https://oecd.ai/en/ai-principles) — non-binding principles for human rights, fairness, transparency, safety, and accountability.
- [OWASP — GenAI LLM Top 10 (2026)](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — current OWASP 2026 risks covering model-integrated application security; detailed threat modeling belongs in the Security and Red Teaming checklists.
- [European Commission — EU AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — changing phased application dates and categories for EU applicability review.
- [EUR-Lex — Regulation (EU) 2024/1689 (consolidated)](https://eur-lex.europa.eu/eli/reg/2024/1689) — official consolidated legal text; consult qualified advisers about the current provisions and their application.
- [European Commission — Navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act) — provider, deployer, transparency, and phased-application guidance.
- [NIST — AI RMF Manage function](https://airc.nist.gov/airmf-resources/playbook/manage/) — risk acceptance, monitoring, mitigation, and go/no-go decisions.
- [W3C WAI — How to Make Your Presentations Accessible to All](https://www.w3.org/WAI/teach-advocate/accessible-presentations/) — illustrative accessible information and communication practices where relevant.

**Applicability:** NIST AI RMF 1.0 and its Playbook are voluntary and were under revision as of this source review. ISO/IEC 42001 and 23894 are published standards with full texts subject to license/access; these links identify their scope but are not a substitute for reading licensed requirements. The EU AI Act has phased, revised application dates as of 2026; distinguish providers, deployers, risk classes, markets, and effective dates with qualified legal counsel. OWASP GenAI LLM Top 10 2026 applies primarily to relevant LLM-integrated systems. Only implement controls proportionate to system risk and actual interfaces.

**Source review date:** 2026-11-12; official NIST/OWASP/EU timeline links rechecked 2026-11-15.
