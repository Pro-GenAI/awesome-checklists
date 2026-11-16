# 14 — AI Human Review and Escalation Checklist

> Ensure human involvement in AI-assisted decisions is meaningful, authorized, timely, and auditable. A review button, nominal human sign-off, or the ability to view model output does not establish independent oversight or prevent unauthorized downstream execution.

> **Scope: AI-specific.** This file is one part of the 14_AI_Human_Review_and_Escalation.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Human oversight design

- [ ] **HUMAN-001** `P2` Define which AI-assisted decisions, recommendations, content releases, and external actions require human review based on severity and user impact.
- [ ] **HUMAN-002** `P2` Assign accountable owners for oversight policy, day-to-day review operations, reviewer competence, and incident escalation.
- [ ] **HUMAN-003** `P1` Distinguish human-in-the-loop approval before an action, human-on-the-loop supervision, and post-decision review in the documented workflow.
- [ ] **HUMAN-004** `P2` Identify consequential decisions where a qualified person must retain effective authority rather than merely rubber-stamping model output.
- [ ] **HUMAN-005** `P2` Specify which decisions can be fully automated and record the rationale, permitted use, and any legally required safeguards.
- [ ] **HUMAN-006** `P2` Define independent reviewer authority to reject, amend, postpone, reverse, or stop an AI recommendation or proposed action.
- [ ] **HUMAN-007** `P1` Require reviewers to see the real decision context, input evidence, known limitations, and consequences appropriate to their permissions.
- [ ] **HUMAN-008** `P1` Present model confidence or scores only with tested calibration and explanations of what the metrics actually measure.
- [ ] **HUMAN-009** `P1` Provide a clear distinction between AI-generated suggestions, verified source facts, reviewer judgments, and completed external actions.
- [ ] **HUMAN-010** `P2` Identify the minimum domain, language, cultural, accessibility, and risk expertise needed for each review category.
- [ ] **HUMAN-011** `P1` Establish reviewer training on automation bias, erroneous AI explanations, uncertainty, prompt injection, and escalation duties.
- [ ] **HUMAN-012** `P2` Define separation of duties for creating a model output, reviewing it, and authorizing high-impact execution when justified by risk.
- [ ] **HUMAN-013** `P1` Provide sufficient review time and staffing so reviewers can exercise judgment instead of being forced into automatic approvals.
- [ ] **HUMAN-014** `P2` Specify when reviewers should consult a second specialist or independent source before making consequential decisions.
- [ ] **HUMAN-015** `P2` Document how impacted people can request explanation, correction, or meaningful human intervention where applicable.
- [ ] **HUMAN-016** `P1` Review privacy, employment, sectoral, and automated-decision requirements for the actual jurisdiction and use case with qualified counsel.
- [ ] **HUMAN-017** `P2` Define the extent of human discretion and confirm that organizational procedures do not undermine genuine ability to override the AI.
- [ ] **HUMAN-018** `P2` Identify tasks where reviewers need access to the original document, image, audio clip, transcript, or tool result rather than a model summary.
- [ ] **HUMAN-019** `P1` Require deterministic authorization checks for every action independently of a reviewer's click and the model's proposed reasoning.
- [ ] **HUMAN-020** `P2` Specify safe behavior if the reviewer lacks permission, relevant expertise, or enough evidence to decide.
- [ ] **HUMAN-021** `P1` Design accessible review surfaces with clear status, understandable controls, and explicit confirmation for irreversible decisions.
- [ ] **HUMAN-022** `P1` Reassess oversight roles and decision authority whenever models, workflows, tool scopes, user populations, or risk classifications change.

## Review queues and decision thresholds

- [ ] **HUMAN-023** `P2` Inventory all review-triggering conditions, including risk severity, low confidence, policy flags, disagreement, and requested user appeals.
- [ ] **HUMAN-024** `P2` Define separate handling for routine validation, high-impact actions, incident triage, safety escalation, and regulatory or customer disputes.
- [ ] **HUMAN-025** `P2` Document task-appropriate thresholds for automatic approval, manual review, abstention, and hard blocking before production use.
- [ ] **HUMAN-026** `P1` Confirm numerical scores used for routing are calibrated, versioned, and meaningful for the reviewed task.
- [ ] **HUMAN-027** `P2` Define mandatory human review conditions that cannot be waived by an aggregate model score or low queue volume.
- [ ] **HUMAN-028** `P2` Specify what happens when classification, routing, or risk-scoring components fail or return malformed results.
- [ ] **HUMAN-029** `P1` Prioritize review queues by potential harm, urgency, case age, and any applicable service or legal deadlines.
- [ ] **HUMAN-030** `P1` Monitor queue volume, age, backlog, processing time, escalation rate, and cases that exceed agreed service levels.
- [ ] **HUMAN-031** `P1` Forecast capacity under expected peak demand and major policy, model, or provider changes.
- [ ] **HUMAN-032** `P1` Prevent queue overload from silently approving or dropping high-impact cases; use defined safe degradation or pauses.
- [ ] **HUMAN-033** `P1` Ensure work distribution respects reviewer expertise, working hours, availability, language, and conflicts of interest.
- [ ] **HUMAN-034** `P1` Use clear ownership and atomic claim/lease behavior to prevent two reviewers from making conflicting decisions on one case.
- [ ] **HUMAN-035** `P2` Define expiration and reassignment rules for stalled, abandoned, duplicate, or unclaimed review tasks.
- [ ] **HUMAN-036** `P1` Handle requests with missing source evidence or incomplete model outputs through clarification or safe rejection rather than a forced binary verdict.
- [ ] **HUMAN-037** `P1` Distinguish recommendation confidence from probability of actual harm and avoid conflating them in risk routing.
- [ ] **HUMAN-038** `P1` Test thresholds with representative benign cases to measure false alarms and avoid unnecessary obstruction of legitimate users.
- [ ] **HUMAN-039** `P1` Test threshold sensitivity with high-impact adverse cases and measure failures that incorrectly bypass review.
- [ ] **HUMAN-040** `P1` Measure queue and approval outcomes by relevant language, task category, access level, and justified population segment where lawful.
- [ ] **HUMAN-041** `P1` Review whether reviewer workload or incentive structures create systematic pressure toward approval.
- [ ] **HUMAN-042** `P2` Record threshold owners, revisions, supporting evaluations, exception criteria, and effective dates.
- [ ] **HUMAN-043** `P1` Use named backup reviewers and escalation chains to cover absence, holidays, incident surges, and specialist unavailability.
- [ ] **HUMAN-044** `P1` Provide a way to escalate an individual case immediately regardless of its model-assigned risk score.
- [ ] **HUMAN-045** `P1` Test dynamic reassignment, queue replay, partial outages, and resumed sessions for lost or duplicated review requests.
- [ ] **HUMAN-046** `P1` Reassess automated routing and review thresholds after material evaluation regressions, incident findings, or distribution shifts.

## Escalation and overrides

- [ ] **HUMAN-047** `P2` Define severity levels and routing contacts for safety, privacy, security, operational, legal, and domain-specific escalation.
- [ ] **HUMAN-048** `P2` Document when first-line reviewers must refer a case to an independent specialist or authorized higher-level decision maker.
- [ ] **HUMAN-049** `P1` Give reviewers an explicit ability to reject an AI recommendation and record a corrected outcome or required human action.
- [ ] **HUMAN-050** `P1` Test that a rejection prevents execution of the corresponding pending tool call or action, including through nested agents.
- [ ] **HUMAN-051** `P1` Bind every approval to the authenticated reviewer, actual run, target tool, normalized parameters, and specific proposed action.
- [ ] **HUMAN-052** `P1` Expire approvals and require renewed review when material parameters, target resources, permissions, or the action itself change.
- [ ] **HUMAN-053** `P1` Reject altered, forged, stale, duplicated, or replayed decisions and do not trust client-supplied serialized approval state.
- [ ] **HUMAN-054** `P1` Recheck the reviewer's authority and the original user's current permissions immediately before execution.
- [ ] **HUMAN-055** `P1` Prohibit broad standing approvals for high-impact actions unless an independently approved and narrowly scoped exception policy explicitly permits them.
- [ ] **HUMAN-056** `P1` Assess whether resumed execution after a handoff changes the approval scope or introduces additional unreviewed operations.
- [ ] **HUMAN-057** `P1` Require additional confirmation or dual control for irreversible or high-risk actions when the task or applicable rules call for it.
- [ ] **HUMAN-058** `P1` Design a safe route when reviewers are unavailable, approval service fails, or risk classification is uncertain.
- [ ] **HUMAN-059** `P1` Allow reviewers and affected users to cancel a pending action and verify cancellation propagates to queued work.
- [ ] **HUMAN-060** `P2` Document which external side effects can be reversed, compensated, or only mitigated after approval.
- [ ] **HUMAN-061** `P1` Use operation identifiers, authoritative status checks, and duplicate safeguards when approved actions resume after crashes or retries.
- [ ] **HUMAN-062** `P1` Distinguish approval of a tool call from evidence that the tool actually completed its external side effect.
- [ ] **HUMAN-063** `P1` Provide an emergency halt or suspension capability for confirmed AI harm or unauthorized activity.
- [ ] **HUMAN-064** `P1` Test overrides, appeals, and emergency stops during an active model rollout, provider outage, or degraded monitoring.
- [ ] **HUMAN-065** `P2` Define a transparent review/appeal process for contested outcomes with accessible submission and case-status tracking where appropriate.
- [ ] **HUMAN-066** `P1` Ensure legal or contractual notification and redress obligations are evaluated for incidents and significant automated decisions.
- [ ] **HUMAN-067** `P2` Record reasoned override decisions without requiring reviewers to endorse unsupported model explanations.
- [ ] **HUMAN-068** `P1` Escalate repeated low-quality decisions, model disagreement, unsafe tool proposals, and queue anomalies to responsible model and risk owners.

## Auditability and reviewer quality

- [ ] **HUMAN-069** `P1` Log a stable case identifier, input version, model/prompt/policy version, review task, actor, and relevant event timestamps.
- [ ] **HUMAN-070** `P2` Record the proposal, decision category, approving or rejecting role, rationale, and actual execution outcome at an appropriate level of detail.
- [ ] **HUMAN-071** `P1` Keep required audit records in controlled storage protected against unauthorized editing and deletion.
- [ ] **HUMAN-072** `P1` Ensure logging and review exports minimize personal information, model secrets, and sensitive source materials.
- [ ] **HUMAN-073** `P1` Restrict review histories and appeal records by user, tenant, case, and reviewer authorization.
- [ ] **HUMAN-074** `P2` Define audit retention, access, deletion, legal hold, and geographic processing requirements by applicable policy and law.
- [ ] **HUMAN-075** `P1` Version review policies, threshold rules, reviewer instructions, and decision rubrics for reproducible incident analysis.
- [ ] **HUMAN-076** `P1` Check that logs distinguish model-generated recommendations from human judgments and confirmed tool effects.
- [ ] **HUMAN-077** `P1` Test reconstructing a disputed case from approved evidence without relying on undocumented ephemeral client state.
- [ ] **HUMAN-078** `P1` Measure reviewer error, disagreement, override frequency, false approvals, and false rejections on representative sampled cases.
- [ ] **HUMAN-079** `P1` Calibrate reviewers with qualified example cases and objective or appropriately adjudicated reference judgments.
- [ ] **HUMAN-080** `P1` Review cases with unusual decision speed, repeated approvals, conflicting outcomes, or unexpectedly low escalation rates.
- [ ] **HUMAN-081** `P1` Assess differences in outcomes across reviewer teams, language groups, and justified user segments with privacy and sample-size safeguards.
- [ ] **HUMAN-082** `P1` Provide a second review or structured adjudication process for high-severity disagreements and possible reviewer conflicts.
- [ ] **HUMAN-083** `P1` Use quality findings to improve guidelines, workload, tooling, and training rather than hiding exceptions in aggregate rates.
- [ ] **HUMAN-084** `P2` Track recurring escalations and user appeals to identify AI failure patterns that deserve model or workflow remediation.
- [ ] **HUMAN-085** `P1` Review access logs for unusual bulk case browsing, unauthorized exports, or attempts to manipulate approval records.
- [ ] **HUMAN-086** `P1` Test that monitoring alarms and incident workflows still function when a review service, queue, or audit sink is unavailable.
- [ ] **HUMAN-087** `P2` Define independent audits or spot checks proportionate to the harm and regulatory exposure of the application.
- [ ] **HUMAN-088** `P2` Record reviewer training completion, delegated authority, and requalification after significant policy or tooling changes.
- [ ] **HUMAN-089** `P1` Make approval and review reporting understandable to qualified internal oversight staff without disclosing restricted records.
- [ ] **HUMAN-090** `P2` Document corrective actions with owners, deadlines, retraining or policy changes, and subsequent retest evidence.
- [ ] **HUMAN-091** `P1` Review whether humans have enough time, context, and organizational authority to exercise meaningful independent judgment.
- [ ] **HUMAN-092** `P1` Reassess quality and fairness when the model, client interface, evidence sources, user population, or review team changes.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **HUMAN-113** `P1` Clearly label AI-proposed actions, pending human decisions, and confirmed completed outcomes in the review interface.
- [ ] **HUMAN-114** `P1` Show reviewers the relevant action, target, side effects, affected data, and supporting evidence before requesting approval.
- [ ] **HUMAN-115** `P1` Provide obvious approve, reject, request-changes, escalate, and cancel controls according to reviewer permissions.
- [ ] **HUMAN-116** `P1` Do not preselect acceptance for high-impact actions or obscure the safer rejection or escalation path.
- [ ] **HUMAN-117** `P1` Display explicit warnings for irreversible, high-value, privacy-sensitive, or externally visible actions.
- [ ] **HUMAN-118** `P1` Keep approval confirmation bound to the displayed action parameters and warn users when these change.
- [ ] **HUMAN-119** `P1` Show review status, current owner, escalation state, and case age without exposing another user's protected information.
- [ ] **HUMAN-120** `P1` Make queues sortable or filterable by urgency, task type, status, and assigned reviewer as authorized.
- [ ] **HUMAN-121** `P1` Ensure screen-reader labels, focus order, keyboard shortcuts, and status announcements support critical reviewer decisions.
- [ ] **HUMAN-122** `P1` Test localization and understandable language for safety, legal, and high-impact review instructions where relevant.
- [ ] **HUMAN-123** `P1` Show missing evidence, conflicting data, uncertain outputs, or unavailable source material rather than implying verified facts.
- [ ] **HUMAN-124** `P1` Provide enough source context for reviewers to inspect original evidence where their permissions allow.
- [ ] **HUMAN-125** `P1` Prevent AI-generated markup, external snippets, and reviewer comments from executing scripts in the review UI.
- [ ] **HUMAN-126** `P1` Protect against duplicate clicks, browser tab races, network disconnects, stale case views, and unintended repeat approval.
- [ ] **HUMAN-127** `P1` Show clear feedback when a decision is denied, expired, superseded, or rejected by current authorization rules.
- [ ] **HUMAN-128** `P1` Offer affected users an accessible appeal, correction, or human-contact mechanism where supported or legally required.
- [ ] **HUMAN-129** `P1` Communicate review and escalation progress without promising completion time or outcome the system cannot guarantee.
- [ ] **HUMAN-130** `P1` Let reviewers report suspicious model behavior, possible prompt injection, or conflicting instructions directly from the case.
- [ ] **HUMAN-131** `P1` Keep sensitive cases, annotations, decision histories, and personally identifying details out of nonessential client analytics.
- [ ] **HUMAN-132** `P1` Test the complete review-and-escalation experience on supported browsers, mobile devices, and assistive technologies.

## Release gate

- [ ] Documented decision categories identify which AI outcomes require human intervention, specialist review, dual control, or immediate suspension according to impact and applicable law.
- [ ] Qualified reviewers have real access to the necessary evidence, time, training, authority, and accessible controls to approve, reject, change, escalate, or stop a decision.
- [ ] Review queues, prioritization, assignment, decision thresholds, staffing, expirations, and safe backlog/outage behavior have been tested under representative workload.
- [ ] Approval, denial, and override controls are bound to authenticated, authorized reviewers and the exact action parameters; stale, replayed, forged, and changed requests cannot execute.
- [ ] Significant decisions, reviewer disagreements, appeals, overrides, completed actions, and incident escalation are traceable with appropriate privacy, integrity, and retention safeguards.
- [ ] Human-review effectiveness and potential automation bias have been evaluated with representative benign, ambiguous, and high-impact cases, including false approvals and unjustified rejections.
- [ ] API and frontend pathways accurately distinguish proposals from confirmed effects and handle waiting, denial, timeout, failed resume, cancellation, and correction accessibly.
- [ ] A named risk owner has reviewed residual limitations, complaint/redress obligations where applicable, response runbooks, emergency halt mechanisms, and the exact release configuration.

**Domain-specific approval rule:** Block release if human review is legally or risk-required but the reviewer cannot independently challenge or stop outcomes; if unapproved, altered, or replayed actions can execute; if high-impact cases can be silently auto-approved during overload; or if mandatory records and escalation routes are unavailable. Human oversight must be proportionate and effective, not merely ceremonial.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#14_ai_human_review_and_escalation), not prerequisites or evidence of PASS.

## Trusted references and scope

**2026 source update:** See the [AI source-currency watch](../references/ai-source-watch.md) for verified NIST/OWASP 2026 editions and the amended EU AI Act timeline. Use current official publications for applicability; source lists do not certify compliance.



The primary standards, laws, risk-management guidance, and implementation references below inform the checklist. Apply vendor features and legal requirements only where relevant to the particular application and deployment.

- [NIST AI RMF Playbook — Govern](https://airc.nist.gov/airmf-resources/playbook/govern/) — human-AI oversight roles, reviewer competence, accountability, and appeal/override processes.
- [NIST AI RMF Playbook — Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) — risk-based incident handling, escalation, mitigation, and continuing oversight.
- [EU AI Act (Regulation 2024/1689) — Article 14 and Article 26](https://eur-lex.europa.eu/eli/reg/2024/1689) — risk-proportionate human oversight and deployer responsibilities for applicable high-risk systems; check current application dates.
- [EU GDPR (Regulation 2016/679) — Article 22](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) — rules on significant solely automated decisions and relevant human intervention or contestation safeguards where applicable.
- [OpenAI Agents SDK — Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) — review interruptions, parameter-bound tool approval, sticky-decision scope, secure resume and replay prevention.
- [OpenAI Agents SDK — Run state](https://openai.github.io/openai-agents-python/ref/run_state/) — durable paused-run state, serialized context, restoration risks, and approval integrity.
- [Microsoft Agent Framework — Tool approval](https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval) — approval-required tools, sessions, standing approvals, and middleware scope.
- [Microsoft Agent Framework — Human-in-the-loop workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop) — workflow pause/resume, human decisions, and orchestration approval paths.
- [OWASP — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — high-impact action authorization, approval integrity, least privilege and incident handling.
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — accessible reviewer interfaces, input controls, focus, status messaging and navigation.
- [OECD — AI Principles](https://oecd.ai/en/ai-principles) — human-centred oversight, transparency, accountability, and risk management.
- [NIST AI RMF Playbook — Map](https://airc.nist.gov/airmf-resources/playbook/map/) — context and impact assessment that determines meaningful oversight requirements.

**Applicability:** The NIST AI RMF is voluntary. The EU AI Act includes Article 14 oversight design requirements and Article 26 deployer obligations for applicable high-risk AI systems; as reflected in the Commission's 2026 updates, relevant Annex III high-risk requirements generally apply from 2 December 2027 and Annex I product-integrated requirements from 2 August 2028. Verify the applicable category, role, exceptions, later amendments and effective date with qualified counsel rather than assuming present-day applicability. GDPR Article 22 applies in specific circumstances involving solely automated decisions with legal or similarly significant effects, including exceptions and safeguards; not every AI suggestion triggers that article. OpenAI Agents SDK and Microsoft Agent Framework approval facilities have different behavior for reused/standing approvals, nested agents, saved state, and resumed tool calls. Their native controls must be supplemented with trusted application authorization, concurrency controls, replay prevention, and recovery of external side effects. WCAG 2.2 requirements depend on the applicable conformance target and governing accessibility law.

**Source review date:** 2026-11-12; EU timeline confirmed against the Commission's 2026 guidance on 2026-11-15.
