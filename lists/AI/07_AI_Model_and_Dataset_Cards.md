# 07 — AI Model and Dataset Cards Checklist

> Verify that model and dataset documentation accurately communicates intended use, capabilities, limitations, provenance, evaluation evidence, risks, and change history. A card is a living disclosure and engineering record—not proof of regulatory compliance, model safety, lawful data rights, or benchmark reproducibility.

> **Scope: AI-specific.** This file is one part of the 07_AI_Model_and_Dataset_Cards.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Intended uses and limitations

- [ ] **CARDS-001** `P2` Describe each model and dataset in plain language, including its purpose, scope, owner, current status, and version.
- [ ] **CARDS-002** `P2` Identify intended direct users, downstream integrators, affected individuals, and the expected operating environment.
- [ ] **CARDS-003** `P1` Distinguish supported tasks from adjacent tasks that have not been evaluated or approved.
- [ ] **CARDS-004** `P1` State out-of-scope uses, prohibited uses, and predictable misuse scenarios with actionable examples.
- [ ] **CARDS-005** `P2` Identify high-impact domains and circumstances where independent human review or stronger controls are necessary.
- [ ] **CARDS-006** `P2` Describe supported languages, scripts, modalities, regions, input sizes, and interface constraints using actual tested coverage.
- [ ] **CARDS-007** `P2` Record known task-specific limitations such as stale knowledge, hallucinations, missing classes, and weak long-context behavior where relevant.
- [ ] **CARDS-008** `P1` Explain assumptions about input quality, data distributions, prompt structure, context sources, and required external services.
- [ ] **CARDS-009** `P1` State confidence or uncertainty limits without portraying uncalibrated scores as reliable probabilities.
- [ ] **CARDS-010** `P2` Document how outputs can affect people who are not direct users, including groups with limited opportunity to contest errors.
- [ ] **CARDS-011** `P2` Describe reasonably foreseeable safety, security, privacy, and discrimination risks relevant to the documented deployment.
- [ ] **CARDS-012** `P1` Explain mitigations, fallback procedures, and circumstances when users must abstain, escalate, or verify independently.
- [ ] **CARDS-013** `P1` Distinguish model capabilities from safeguards imposed by the surrounding application, access controls, and human workflow.
- [ ] **CARDS-014** `P2` List supported deployment environments, resource constraints, inference dependencies, and known incompatibilities.
- [ ] **CARDS-015** `P2` Document any restrictions arising from licenses, provider terms, consent, data processing, or applicable market requirements.
- [ ] **CARDS-016** `P1` Clarify whether the card covers a base model, fine-tuned variant, quantized checkpoint, hosted snapshot, or complete AI system.
- [ ] **CARDS-017** `P1` Provide examples of appropriate inputs and expected behavior without including confidential or disallowed personal data.
- [ ] **CARDS-018** `P1` State important conditions where publicly reported benchmark scores may not generalize to production workloads.
- [ ] **CARDS-019** `P1` Explain the potential for performance changes due to model-provider updates, retrieval freshness, tools, or user population drift.
- [ ] **CARDS-020** `P2` Identify who can approve exceptions and where users or integrators can report errors or suspected harmful behavior.
- [ ] **CARDS-021** `P1` Separate evidence-based statements, provider assertions, assumptions, and unknown information in the card.
- [ ] **CARDS-022** `P1` Review whether the intended-use guidance is comprehensible to non-expert stakeholders and accurately limits implied guarantees.

## Data and training provenance

- [ ] **CARDS-023** `P2` Identify model developer, provider, distributor, architecture family, checkpoint, release date, and accountable maintainer.
- [ ] **CARDS-024** `P2` Record base-model identity and lineage for adapters, merges, distillation, fine-tuning, quantization, or post-training variants.
- [ ] **CARDS-025** `P1` Link approved training, validation, and evaluation datasets to exact versioned manifests or immutable references where available.
- [ ] **CARDS-026** `P1` Summarize training data sources, collection periods, geographic and language coverage, and intended representativeness.
- [ ] **CARDS-027** `P2` Document major source omissions, selection biases, exclusions, and known gaps in corpus coverage.
- [ ] **CARDS-028** `P1` State dataset creators, stewards, publishers, acquisition channels, and the purpose for which data was collected.
- [ ] **CARDS-029** `P2` Identify source license terms and relevant restrictions on access, redistribution, commercial use, training, and derived artifacts.
- [ ] **CARDS-030** `P2` Record applicable notice, consent, contractual, and privacy reviews for identifiable or sensitive source data.
- [ ] **CARDS-031** `P2` Document whether and how personal, protected, copyrighted, or proprietary content is filtered or handled in source material.
- [ ] **CARDS-032** `P2` Describe annotation approach, label schema, annotator or expert qualifications, and adjudication methods where applicable.
- [ ] **CARDS-033** `P1` Report significant data-cleaning, deduplication, filtering, augmentation, and synthetic-generation steps.
- [ ] **CARDS-034** `P2` Track transformation code revisions, extraction tools, feature schemas, tokenizers, and relevant preprocessing versions.
- [ ] **CARDS-035** `P1` Explain training and validation split strategies and potential overlap or contamination limits.
- [ ] **CARDS-036** `P1` Link model training runs to architecture, important hyperparameters, training regime, compute settings, and reproducibility artifacts.
- [ ] **CARDS-037** `P2` Record when training details are unavailable for third-party closed models instead of inferring undisclosed facts.
- [ ] **CARDS-038** `P2` Document who verified supplied source or vendor claims and which provenance elements remain unconfirmed.
- [ ] **CARDS-039** `P2` Track origin of multimodal inputs, such as images, audio, video, and sensor data, where relevant to permissions and bias.
- [ ] **CARDS-040** `P2` Describe expected handling of withdrawn, corrected, expired, or disputed source data and its downstream derivatives.
- [ ] **CARDS-041** `P2` Publish data volume, modality distribution, label balance, and other useful composition statistics at a suitably safe aggregation level.
- [ ] **CARDS-042** `P2` Maintain traceable identifiers between model-card data claims, dataset-card entries, manifests, and underlying approved evidence.
- [ ] **CARDS-043** `P1` Verify published data examples and metadata do not expose protected records, hidden labels, or nonpublic evaluation cases.
- [ ] **CARDS-044** `P1` Explain differences between data that was used for training, retrieval at runtime, preference tuning, and evaluation.
- [ ] **CARDS-045** `P2` Describe data retention and restricted access to raw corpora, generated labels, model artifacts, and dataset exports.
- [ ] **CARDS-046** `P2` Document remaining provenance or licensing uncertainty as a material limitation with an owner and review status.

## Evaluation and fairness disclosure

- [ ] **CARDS-047** `P2` Specify each evaluation's task, metric definition, scoring direction, acceptance threshold, and tested model or dataset version.
- [ ] **CARDS-048** `P2` Describe benchmark dataset names, versions, sample sizes, sampling method, and permitted use.
- [ ] **CARDS-049** `P2` Document evaluation prompts, relevant system configuration, decoding settings, tools, retrieval sources, and test conditions.
- [ ] **CARDS-050** `P1` Distinguish model-only scores from end-to-end application results and from provider-reported benchmark claims.
- [ ] **CARDS-051** `P1` Show baseline or comparator scores where available so results can be interpreted in context.
- [ ] **CARDS-052** `P1` Report meaningful uncertainty, repeatability, confidence intervals, or limitations for variable and small-sample results.
- [ ] **CARDS-053** `P1` Disclose important severe errors and failure modes even if the average score meets an acceptance threshold.
- [ ] **CARDS-054** `P2` Describe subgroup performance or relevant differences across languages, cohorts, locations, and accessibility contexts when lawfully and validly evaluated.
- [ ] **CARDS-055** `P1` State when subgroup measurements were not performed or are unreliable due to limited sample sizes or inadequate labels.
- [ ] **CARDS-056** `P1` Report the rationale and limitations for collecting or inferring any sensitive attributes used in fairness analysis.
- [ ] **CARDS-057** `P1` Explain harmful-output, refusal, overblocking, privacy, prompt-injection, or tool-authorization tests appropriate to the actual capabilities.
- [ ] **CARDS-058** `P2` Document robustness results for malformed, ambiguous, rare, out-of-distribution, and adversarial examples where tested.
- [ ] **CARDS-059** `P2` Describe false-positive, false-negative, calibration, or abstention performance when those distinctions affect real-world risk.
- [ ] **CARDS-060** `P1` Include known dataset annotation uncertainties, class imbalance, missingness, and potential evaluation contamination.
- [ ] **CARDS-061** `P1` Assess whether data and metrics represent the deployed population rather than relying only on public leaderboard rankings.
- [ ] **CARDS-062** `P2` Record latency, memory, throughput, energy or cost observations only with relevant hardware and serving conditions.
- [ ] **CARDS-063** `P1` Explain how evaluation results differ across deployment variants, regions, provider snapshots, or quantized configurations.
- [ ] **CARDS-064** `P1` Label qualitative human-assessment findings with rubric, reviewer process, and potential evaluator bias.
- [ ] **CARDS-065** `P1` Link findings to authorized, versioned reports without exposing restricted test prompts or personal data.
- [ ] **CARDS-066** `P1` State mitigation status, accepted residual risk, and planned additional evaluation for unresolved limitations.
- [ ] **CARDS-067** `P1` Require review by responsible risk or domain specialists when the documented model affects consequential decisions.
- [ ] **CARDS-068** `P1` Update the disclosed evidence after material regressions or verified incidents rather than leaving contradicted claims in place.

## Documentation and revision history

- [ ] **CARDS-069** `P1` Store the canonical card in a discoverable repository, registry, or documentation system with a named maintenance owner.
- [ ] **CARDS-070** `P1` Bind each released card to an immutable model or dataset version rather than an untracked latest alias.
- [ ] **CARDS-071** `P1` Include creation, last-review, publication, effective, and supersession dates as relevant.
- [ ] **CARDS-072** `P1` State the audience and decide which content is public versus access-restricted by policy and contractual rights.
- [ ] **CARDS-073** `P1` Use a maintained card structure that separates overview, intended use, data, evaluation, risks, limitations, and contact channels.
- [ ] **CARDS-074** `P1` Populate required metadata such as language, license, task type, base model, or dataset references when the publishing platform supports them.
- [ ] **CARDS-075** `P1` Validate machine-readable metadata schema and links before publication, including YAML or JSON-LD syntax where applicable.
- [ ] **CARDS-076** `P2` Record the document source, reviewer, approval status, and exact release build to which the card applies.
- [ ] **CARDS-077** `P1` Keep technical claims aligned with evaluated configurations, recorded deployment versions, and reproducible experiment manifests.
- [ ] **CARDS-078** `P2` Define a change log showing what changed, why, who reviewed it, and when the new version became effective.
- [ ] **CARDS-079** `P1` Review cards after changes to model weights, tuning, data sources, collection rules, labels, supported uses, or policies.
- [ ] **CARDS-080** `P1` Add incident-driven warnings or revised limitations without waiting for a full model retrain where immediate disclosure is appropriate.
- [ ] **CARDS-081** `P1` Ensure changes to dataset versions and documentation propagate to linked model cards and published downstream records.
- [ ] **CARDS-082** `P1` Mark retired, withdrawn, deprecated, or replaced models and datasets clearly while preserving authorized archival history.
- [ ] **CARDS-083** `P2` Publish migration guidance or updated links when a model, endpoint, dataset, or evaluation protocol is superseded.
- [ ] **CARDS-084** `P1` Check accessibility, readable tables, descriptive links, and relevant localization for documentation used by external audiences.
- [ ] **CARDS-085** `P1` Verify that public download cards and discovery listings do not imply licenses, capabilities, or safety approvals not actually established.
- [ ] **CARDS-086** `P2` Document an intake process for correction requests, misuse reports, reproducibility questions, and provenance disputes.
- [ ] **CARDS-087** `P1` Provide appropriate limitations or unknown-status notation rather than silently omitting unavailable evidence.
- [ ] **CARDS-088** `P1` Retain previous approved card versions so reviewers can reconstruct what users were told at earlier release dates.
- [ ] **CARDS-089** `P2` Define a periodic review cadence proportionate to model change frequency, use-case risk, and data freshness.
- [ ] **CARDS-090** `P1` Have a qualified owner review the release-ready card for factual consistency, privacy, security, and lawful publication.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **CARDS-111** `P1` Make model and dataset descriptions easy to find from the relevant product feature, documentation page, or download surface.
- [ ] **CARDS-112** `P1` Explain intended and out-of-scope uses in accessible language without making unproven safety or accuracy guarantees.
- [ ] **CARDS-113** `P1` Show meaningful limitations and supported-language or modality restrictions near consequential user decisions.
- [ ] **CARDS-114** `P1` Make clear whether a claim describes the underlying model, an external provider, or the complete application workflow.
- [ ] **CARDS-115** `P1` Present evaluation metric names, baselines, sample sizes, and known limitations in a way non-experts can interpret.
- [ ] **CARDS-116** `P1` Distinguish tested behavior from forecasts, marketing statements, and pending research outcomes.
- [ ] **CARDS-117** `P1` Display correct model version, card revision, and update date when users compare or rely on model information.
- [ ] **CARDS-118** `P1` Provide a clear path to license, usage conditions, dataset provenance, and appropriate privacy notices.
- [ ] **CARDS-119** `P1` Ensure cards, citations, metadata badges, and documents remain keyboard accessible and screen-reader understandable.
- [ ] **CARDS-120** `P1` Test long technical tables, code examples, mixed scripts, and responsive layouts on supported devices.
- [ ] **CARDS-121** `P1` Do not expose hidden examples, confidential data, or protected subgroup counts in public card previews or downloadable reports.
- [ ] **CARDS-122** `P1` Show missing, withdrawn, outdated, or unavailable documentation as such rather than silently substituting a different model card.
- [ ] **CARDS-123** `P1` Ensure external card and paper links have descriptive labels and expected destinations.
- [ ] **CARDS-124** `P1` Provide a correction or error-reporting contact for misleading, outdated, or harmful model documentation.
- [ ] **CARDS-125** `P1` Use consistent terminology and qualified localization for critical limitations or legal notices where applicable.
- [ ] **CARDS-126** `P1` Keep user-visible examples aligned with the production model and do not publish examples that reveal real secrets or private histories.
- [ ] **CARDS-127** `P1` Label claims sourced from third-party model cards when the application has not independently verified them.
- [ ] **CARDS-128** `P1` Test frontend updates when a staged rollout changes model aliases, supported capabilities, or access permissions.
- [ ] **CARDS-129** `P1` Verify downloadable cards are clearly dated, versioned, and available only to permitted audiences.
- [ ] **CARDS-130** `P1` Confirm user research or review shows the card communicates meaningful risks without overwhelming the intended audience.

## Release gate

- [ ] The released model and/or dataset has an identifiable owner, exact artifact version and approved current card with intended uses, out-of-scope uses and supported constraints.
- [ ] Source, training and dataset provenance, relevant licensing or rights restrictions, transformations and open lineage gaps are documented without exposing protected records.
- [ ] The card presents version-matched evaluation evidence, tested populations or modalities, material performance differences and known severe failure cases or uncertainty.
- [ ] Meaningful safety, privacy, bias, accessibility and downstream misuse limitations have responsible mitigation or escalation guidance proportionate to risk.
- [ ] Published metadata, references, model identifiers and dataset links have passed schema, access-control, consistency and link checks where relevant.
- [ ] API and frontend surfaces expose appropriate, version-matched documentation, and correctly handle restricted, withdrawn or superseded cards.
- [ ] The maintenance owner, change-triggered review, correction intake, revision history, publication controls and responsible reviewers are in place.
- [ ] Significant missing rights, contradictory or misleading capability claims, unsupported high-impact uses or unresolved disclosure risks are blocked or formally dispositioned by qualified approvers.

**Domain-specific approval rule:** Block documentation approval if material claims cannot be reconciled to the actual model or dataset, a critical known limitation is concealed, a public card exposes protected information, or rights and usage restrictions remain unreviewed for the intended release. Publication does not certify a model, validate every provider claim or grant dataset-use rights.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#07_ai_model_and_dataset_cards), not prerequisites or evidence of PASS.

## Trusted references and scope

The following primary specifications, publishing guides and responsible-AI references support practical model and dataset documentation. Use the parts applicable to the artifact and publication platform.

- [Hugging Face — Model Cards](https://huggingface.co/docs/hub/en/model-cards) — required contextual information, intended use, limitations, training and evaluation metadata.
- [Hugging Face — Annotated Model Card](https://huggingface.co/docs/hub/en/model-card-annotated) — structured model card template, cross-functional responsibilities, bias and risk documentation.
- [Hugging Face — Model Release Checklist](https://huggingface.co/docs/hub/model-release-checklist) — model release readiness, versioned artifacts and documented metadata.
- [Hugging Face — Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) — dataset composition, language, license, intended use, and machine-readable metadata.
- [Hugging Face — Model Card Publishing Guide](https://huggingface.co/docs/huggingface_hub/en/guides/model-cards) — versioned metadata editing, publishing and review workflows on Hugging Face Hub.
- [MLCommons — Croissant Format](https://docs.mlcommons.org/croissant/) — interoperable dataset metadata, resources, record structure, and ML semantics.
- [MLCommons — Croissant 1.1 Announcement](https://mlcommons.org/2026/02/croissant-1-1-standard/) — updated machine-readable provenance and governance metadata; adoption is optional.
- [W3C — PROV Overview](https://www.w3.org/TR/prov-overview/) — interoperable representation of source, agent and transformation provenance.
- [NIST AI RMF Playbook — Map](https://airc.nist.gov/airmf-resources/playbook/map/) — intended context, documented system limits, assumptions and foreseeable impacts.
- [NIST AI RMF Playbook — Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) — quality, fairness, reliability and risk-measurement evidence and limitations.
- [Microsoft — Responsible AI Transparency Note](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/document-intelligence/transparency-note) — clear distinctions among the model, people, deployment context, supported uses and limitations.
- [TensorFlow — Model Card Toolkit](https://github.com/tensorflow/model-card-toolkit) — model-card generation from training and evaluation metadata, with implementation-specific support.

**Applicability:** Hugging Face model and dataset card metadata conventions apply when using that platform; an equivalent internal registry and documentation process can be appropriate for restricted artifacts. MLCommons Croissant 1.1 provides an optional machine-readable dataset metadata specification, including provenance, rather than a universal requirement. W3C PROV documents lineage structures but does not establish that training data was lawfully obtained. NIST AI RMF is voluntary guidance. Model Card Toolkit and vendor transparency notes are implementation examples, not evidence that an individual model is complete, unbiased, safe or certified. Never infer undisclosed third-party training details; document the uncertainty.

**Source review date:** 2026-11-12.
