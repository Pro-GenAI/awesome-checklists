# 08 — AI Fine-tuning and Training Checklist

> Verify that training or fine-tuning a model is justified, reproducible, permissioned, numerically stable, evaluated for unintended behavioral changes, and released under explicit control. Lower training loss or a successful provider job alone does not establish model quality, safety, data rights, or deployment readiness.

> **Scope: AI-specific.** This file is one part of the 08_AI_FineTuning_and_Training.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Training objectives and configuration

- [ ] **TRAIN-001** `P2` Define the intended task, affected users, observable improvement target, and reason training is preferable to prompting, retrieval, or workflow changes.
- [ ] **TRAIN-002** `P2` Identify the exact approved base model or checkpoint, revision, license, provider restrictions, and permitted fine-tuning or redistribution uses.
- [ ] **TRAIN-003** `P1` Choose full fine-tuning, supervised fine-tuning, adapter-based training, preference optimization, or another approach based on task evidence and resources.
- [ ] **TRAIN-004** `P2` Document explicit quality, safety, privacy, cost, latency, and deployment acceptance criteria before starting training.
- [ ] **TRAIN-005** `P1` Choose a non-tuned or current-production baseline and maintain comparable evaluation settings for the candidate.
- [ ] **TRAIN-006** `P2` Record the training objective, loss function, expected label semantics, and any reward or preference signals used.
- [ ] **TRAIN-007** `P2` Specify the trainable parameters, frozen modules, adapter targets, LoRA rank and scaling, or equivalent method settings when applicable.
- [ ] **TRAIN-008** `P1` Verify a parameter-efficient adapter is compatible with the precise base model, tokenizer, architecture, and inference runtime.
- [ ] **TRAIN-009** `P2` Document optimizer, learning-rate schedule, warm-up, regularization, weight decay, gradient accumulation, and clipping settings.
- [ ] **TRAIN-010** `P1` Set effective batch size, sequence length, padding, truncation, example packing, and sampling policies with explicit rationale.
- [ ] **TRAIN-011** `P1` Verify conversational training uses the correct role and chat templates for the target model and release.
- [ ] **TRAIN-012** `P1` Check that loss masking trains on intended assistant/completion tokens rather than inadvertently optimizing prompts or protected context.
- [ ] **TRAIN-013** `P2` Define how tool-call formats, special tokens, structured outputs, and end-of-turn markers are represented in training examples.
- [ ] **TRAIN-014** `P1` Set validation cadence, checkpoint selection criterion, early-stop policy, and maximum training steps or epochs.
- [ ] **TRAIN-015** `P2` Define numerical precision, quantization, distributed training, and accelerator-memory settings supported by the actual runtime.
- [ ] **TRAIN-016** `P1` Validate mixed-precision and quantized training with checks for NaNs, gradient underflow/overflow, and changed task quality.
- [ ] **TRAIN-017** `P1` Estimate compute, GPU memory, storage, checkpoint volume, run duration, and total training cost against approved limits.
- [ ] **TRAIN-018** `P2` Specify distributed worker configuration, sharding, accumulation, optimizer state, and any expected scaling bottlenecks.
- [ ] **TRAIN-019** `P1` Review training-job identities, network egress, secret handling, approved artifact destinations, and access to private datasets.
- [ ] **TRAIN-020** `P1` Plan training-risk mitigations for overfitting, catastrophic forgetting, reward hacking, and unexpected behavioral changes.
- [ ] **TRAIN-021** `P2` Assign responsible ML engineering, evaluation, data rights, security, and deployment approvers.
- [ ] **TRAIN-022** `P1` Version and freeze the approved training configuration, base artifact, and environment before starting a release-candidate run.

## Training data and splits

- [ ] **TRAIN-023** `P1` Confirm training and preference data have approved provenance, licensing, consent, and permitted model-development uses.
- [ ] **TRAIN-024** `P1` Link each training run to immutable or versioned datasets, source manifests, transformation code, and labeling guidelines.
- [ ] **TRAIN-025** `P1` Check training records against required schemas, field types, role formats, media metadata, and sample-size constraints.
- [ ] **TRAIN-026** `P1` Verify target labels, assistant completions, selected/rejected preference pairs, and scoring rubrics match the chosen objective.
- [ ] **TRAIN-027** `P1` Ensure preference datasets preserve the same prompt context for chosen and rejected outputs where the method requires it.
- [ ] **TRAIN-028** `P1` Detect missing responses, inconsistent roles, malformed conversations, corrupted media, and invalid token sequences before training.
- [ ] **TRAIN-029** `P1` Validate examples retain relevant task context and that truncation does not delete necessary answers or safety qualifiers.
- [ ] **TRAIN-030** `P1` Measure token-length distributions, language and task frequencies, label balance, and outlier examples before scheduling runs.
- [ ] **TRAIN-031** `P1` Prevent training, validation, and held-out evaluation overlap across near-duplicates, translations, source documents, users, and synthetic variants.
- [ ] **TRAIN-032** `P1` Use group-based or temporal splits when related records would make random row splits misleading.
- [ ] **TRAIN-033** `P1` Protect the final release-evaluation holdout from data selection, prompt tuning, hyperparameter search, and training feedback.
- [ ] **TRAIN-034** `P1` Check that known benchmark questions or private grading answers have not leaked into fine-tuning examples.
- [ ] **TRAIN-035** `P1` Review sample weighting, class rebalance, filtering, and oversampling for unintended distribution or fairness effects.
- [ ] **TRAIN-036** `P1` Audit model-generated synthetic training examples for factual errors, unsafe content, memorization, and copied private records.
- [ ] **TRAIN-037** `P1` Check the quality and consistency of human labels and adjudicate ambiguous or high-impact cases before training.
- [ ] **TRAIN-038** `P1` Verify inclusion of task-relevant refusals, clarifications, boundary cases, and policy-consistent behavior where appropriate.
- [ ] **TRAIN-039** `P1` Review model behavior risks introduced by demonstrations containing unsafe instructions, privileged tool calls, or untrusted document text.
- [ ] **TRAIN-040** `P1` Measure potential overrepresentation of narrow sources, annotator preferences, dialects, or demographic proxies where lawful and relevant.
- [ ] **TRAIN-041** `P1` Apply necessary minimization or redaction to personal data, credentials, confidential business records, and protected identifiers.
- [ ] **TRAIN-042** `P2` Define how source deletion, license withdrawal, or consent changes are propagated to future training runs and affected model artifacts.
- [ ] **TRAIN-043** `P1` Keep private datasets and golden evaluations access-controlled; prevent accidental publication to experiment dashboards or model hubs.
- [ ] **TRAIN-044** `P2` Document augmentation, example packing, shuffling, sampling seeds, and preprocessing version so the training input can be reconstructed.
- [ ] **TRAIN-045** `P1` Validate tokenization, attention masks, loss masks, and data collators on a small known-correct fixture before large training.
- [ ] **TRAIN-046** `P2` Record excluded records, their exclusion reasons, unresolved data quality issues, and any accepted representation limitations.

## Checkpoints and reproducibility

- [ ] **TRAIN-047** `P2` Assign stable run identifiers linking code revision, data version, base weights, training configuration, and execution environment.
- [ ] **TRAIN-048** `P2` Record library versions, container image digests, accelerator models, driver/runtime versions, and distributed-training topology.
- [ ] **TRAIN-049** `P1` Set and capture random seeds and determinism controls supported by the framework while documenting limits across devices and releases.
- [ ] **TRAIN-050** `P1` Test that a small training run can be repeated within realistic numerical and statistical tolerances.
- [ ] **TRAIN-051** `P1` Configure loss, validation metrics, learning rate, gradient norms, memory usage, and throughput logging at useful intervals.
- [ ] **TRAIN-052** `P1` Detect NaN or infinite loss, diverging gradients, unstable reward metrics, and unexpected learning-rate schedule changes.
- [ ] **TRAIN-053** `P1` Monitor train-versus-validation divergence and define investigation criteria for overfitting or data contamination.
- [ ] **TRAIN-054** `P1` Validate automatic mixed precision, gradient scaling where applicable, and numerical stability for the selected hardware.
- [ ] **TRAIN-055** `P1` Choose checkpoint cadence based on data loss tolerance, expected preemption, storage cost, and recovery time.
- [ ] **TRAIN-056** `P1` Persist the necessary model or adapter weights, optimizer state, scheduler state, step counters, and random-number states for exact supported resumption.
- [ ] **TRAIN-057** `P1` Distinguish inference-only weight exports from resumable training checkpoints in names and metadata.
- [ ] **TRAIN-058** `P1` Test interruption and resume from a representative checkpoint and compare resulting run behavior with expected tolerances.
- [ ] **TRAIN-059** `P1` Verify partial, corrupted, or incomplete checkpoints cannot be promoted or silently selected for resumption.
- [ ] **TRAIN-060** `P1` Validate distributed sharded checkpoint restore with the selected training topology and supported framework version.
- [ ] **TRAIN-061** `P1` Test checkpoint restore when storage, rank count, node placement, or topology changes if that recovery mode is supported.
- [ ] **TRAIN-062** `P1` Check model/adaptor save and load compatibility with its exact base revision and required special-token configuration.
- [ ] **TRAIN-063** `P2` Record model artifact checksums or cryptographic digests and protect training outputs against unauthorized overwrites.
- [ ] **TRAIN-064** `P1` Restrict access to checkpoints because weights, optimizer state, and metadata may contain sensitive information.
- [ ] **TRAIN-065** `P1` Ensure training artifact storage, retention, and deletion satisfy applicable data policy and contractual constraints.
- [ ] **TRAIN-066** `P1` Test job timeouts, worker loss, transient network failures, and storage quota exhaustion with safe resource cleanup.
- [ ] **TRAIN-067** `P1` Prevent duplicate training jobs or repeated scheduled runs from silently replacing reviewed artifacts or exhausting compute budgets.
- [ ] **TRAIN-068** `P1` Keep traceable history of experiment failures, restart reasons, configuration changes, and checkpoint selection rationale.
- [ ] **TRAIN-069** `P2` Document the final candidate's exact artifact, adapter composition, source run, and evaluation checkpoint identifier.
- [ ] **TRAIN-070** `P1` Verify the archived training recipe can regenerate a functionally comparable candidate under its documented constraints.

## Post-training evaluation and deployment

- [ ] **TRAIN-071** `P1` Compare the trained candidate with the unchanged approved baseline on representative, held-out, task-specific evaluations.
- [ ] **TRAIN-072** `P1` Verify improvement in the intended target task is meaningful and not confined to the training examples.
- [ ] **TRAIN-073** `P1` Measure regressions on unrelated but important baseline capabilities to detect catastrophic forgetting.
- [ ] **TRAIN-074** `P1` Evaluate safety refusals, legitimate-request false blocks, unsupported assertions, and harmful outputs after tuning.
- [ ] **TRAIN-075** `P1` Test unauthorized tool use, prompt-injection susceptibility, private-data exposure, and policy compliance where relevant.
- [ ] **TRAIN-076** `P1` Assess structured output, tool-call argument validity, role semantics, and required response formats against production contracts.
- [ ] **TRAIN-077** `P1` Measure relevant language, cohort, dialect, and domain performance differences with adequate samples and permitted data use.
- [ ] **TRAIN-078** `P1` Test memorization or unintended reproduction of private training examples using controlled, authorized fixtures.
- [ ] **TRAIN-079** `P1` Report confidence intervals, repeatability limits, and severe failures rather than relying solely on one aggregate quality score.
- [ ] **TRAIN-080** `P1` Validate downstream RAG, agents, multimodal processing, and human-approval workflows when the fine-tuned model participates in them.
- [ ] **TRAIN-081** `P1` Benchmark serving latency, model/adapter load time, throughput, memory, and inference cost against approved budgets.
- [ ] **TRAIN-082** `P1` Test inference using the precise model weights, adapter, tokenizer, chat template, and quantization settings selected for deployment.
- [ ] **TRAIN-083** `P1` Ensure the release model card captures training origin, intended uses, dataset limits, evaluation evidence, and known safety restrictions.
- [ ] **TRAIN-084** `P1` Register the candidate with immutable artifact/version identifiers, traceable lineage, and an auditable approval status.
- [ ] **TRAIN-085** `P1` Require a qualified human to review critical quality, safety, privacy, and licensing findings before promotion.
- [ ] **TRAIN-086** `P1` Verify no automatic training job or model-registry alias can deploy an unreviewed checkpoint to production.
- [ ] **TRAIN-087** `P1` Stage rollout using controlled traffic or a testing environment appropriate to impact, with predeclared stop criteria.
- [ ] **TRAIN-088** `P1` Test compatibility with the current API response formats, stored conversations, client versions, and fallback models.
- [ ] **TRAIN-089** `P2` Maintain an approved previous version or safe non-AI fallback and test model/adapter rollback.
- [ ] **TRAIN-090** `P1` Monitor post-release task performance, safety blocks, token/cost changes, drift, and user complaints by model revision.
- [ ] **TRAIN-091** `P2` Define triggers for retuning, retraining, revocation, deprecation, or emergency disablement based on observed harm or poor quality.
- [ ] **TRAIN-092** `P2` Record release decision, risk acceptances, owners, deployment manifest, and post-launch review date.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **TRAIN-113** `P1` Clearly distinguish model-training controls and fine-tuning data uploads from ordinary inference features in the UI.
- [ ] **TRAIN-114** `P1` Explain who may upload data, start training, view evaluation results, export models, or approve deployment.
- [ ] **TRAIN-115** `P1` Show the training method, base-model revision, dataset, costs, and significant use restrictions before a privileged job starts.
- [ ] **TRAIN-116** `P1` Provide warnings for confidential data, rights restrictions, sensitive labels, and external processor transfers where relevant.
- [ ] **TRAIN-117** `P1` Display actual training states, elapsed progress, checkpoint/evaluation status, and failures without inventing successful completion.
- [ ] **TRAIN-118** `P1` Prevent misleading progress percentages when the underlying provider only supplies coarse asynchronous job states.
- [ ] **TRAIN-119** `P1` Provide accessible controls for start, pause if supported, cancel, retry, and inspect job errors.
- [ ] **TRAIN-120** `P1` Do not present generated or partially validated checkpoints as production-approved models.
- [ ] **TRAIN-121** `P1` Show baseline-versus-candidate evaluation results with meaningful metrics, sample limitations, and documented severe regressions.
- [ ] **TRAIN-122** `P1` Distinguish evaluation outcomes, risk approvals, staged deployments, and actual production model promotion.
- [ ] **TRAIN-123** `P1` Provide explicit confirmation and an authenticated approval path for production promotion or irreversible training-data deletion.
- [ ] **TRAIN-124** `P1` Test stale dashboards, duplicate clicks, disconnected sessions, and delayed job events against authoritative server state.
- [ ] **TRAIN-125** `P1` Restrict dataset examples, private evaluation prompts, model artifacts, and sensitive job logs by role and tenant.
- [ ] **TRAIN-126** `P1` Safely render training filenames, dataset descriptions, generated logs, error messages, and model-card content without script injection.
- [ ] **TRAIN-127** `P1` Ensure training and deployment progress, errors, and confirmation states are accessible via keyboard and screen readers.
- [ ] **TRAIN-128** `P1` Check responsive layouts, supported languages, and long experiment identifiers across relevant desktop and mobile screens.
- [ ] **TRAIN-129** `P1` Communicate model behavior changes, known limitations, and safe fallback to users affected by the newly tuned model.
- [ ] **TRAIN-130** `P1` Offer understandable recovery when training or model promotion fails, expires, or is canceled.
- [ ] **TRAIN-131** `P1` Collect user feedback on new-model output regressions with privacy-conscious version attribution.
- [ ] **TRAIN-132** `P1` Confirm model-switching interfaces show only approved model versions and do not expose administrative credentials or protected configuration.

## Release gate

- [ ] The training purpose, permitted base-model use, accountable owners, chosen method, expected improvement, and material privacy/licensing restrictions have been reviewed.
- [ ] Versioned datasets, preprocessing, labels and preference examples pass defined quality checks; evaluation holdouts are appropriately separated and contamination assessed.
- [ ] The exact training job has a reviewed configuration, identifiable base checkpoint, correct loss/format semantics, approved resource budgets, numerical stability evidence, and reproducible lineage.
- [ ] Candidate weights or adapters, checkpoints, and artifact metadata are integrity-checked; required resume and failure-recovery paths are tested for the training environment.
- [ ] Held-out task and baseline comparisons meet predeclared quality/safety criteria, with checks for catastrophic forgetting, memorization, behavior regression, and relevant cohort differences.
- [ ] API/inference and frontend compatibility have been evaluated for the exact tuned model, including schema validity, latency, costs, fallback, safety, and user-visible limitations as relevant.
- [ ] Registry, model card, deployment approval, staged rollout, monitoring, and rollback or emergency disablement are ready for the approved artifact version.
- [ ] No unaccepted high-severity privacy, data-rights, unsafe-content, or unauthorized-action failure remains; a qualified human has signed off on the specific release and accepted residual risks.

**Domain-specific approval rule:** Block model promotion when material training data lack permitted use, evaluation holdouts are compromised, the approved base/adapter artifact cannot be identified or restored, the candidate shows serious unmitigated behavior or safety regression, or deployment bypasses required authorization. A low training loss, efficient fine-tuning method, or model-card publication is not an independent release approval.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#08_ai_finetuning_and_training), not prerequisites or evidence of PASS.

## Trusted references and scope

The following primary maintainer documentation and authoritative guidance inform these training-related checks. Methods and configuration flags are conditional on the exact framework and release in use; they are not mandatory for every AI system.

- [Hugging Face TRL — Supervised Fine-Tuning Trainer](https://huggingface.co/docs/trl/sft_trainer) — conversational/prompt-completion data, masking, packing, and supervised training configuration.
- [Hugging Face TRL — Direct Preference Optimization Trainer](https://huggingface.co/docs/trl/dpo_trainer) — chosen/rejected preference pair formats, reference policies, and preference optimization.
- [Hugging Face PEFT — LoRA](https://huggingface.co/docs/peft/main/conceptual_guides/lora) — adapter-based parameter-efficient fine-tuning, base-model compatibility, and configuration.
- [Hugging Face Transformers — Trainer features](https://huggingface.co/docs/transformers/trainer_recipes) — checkpoints, resumable training, optimizer and random state, and interruptions.
- [Hugging Face Datasets — File Names and Splits](https://huggingface.co/docs/hub/datasets-file-names-and-splits) — separating and documenting training, validation, and test data.
- [Hugging Face — Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) — source rights, dataset description, known limitations, and versioned metadata.
- [Hugging Face — Model Cards](https://huggingface.co/docs/hub/en/model-cards) — model intended use, provenance, training and evaluation disclosures.
- [PyTorch — Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) — randomness controls and limits of reproducibility across framework/device versions.
- [PyTorch — Automatic Mixed Precision](https://docs.pytorch.org/docs/stable/amp.html) — mixed precision, gradient scaling where applicable, and numerical stability.
- [PyTorch — Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html) — sharded and distributed state saving, restoration, and topology requirements.
- [Amazon SageMaker AI — Training Output Artifacts](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html) — managed training artifact output and separation of final model from other job data.
- [Google Cloud Architecture Center — MLOps CI/CD/CT](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — reproducible pipelines, model evaluation, controlled release, and continuous training.
- [NIST AI RMF Playbook — Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) — trustworthiness evaluations, dataset splits, robustness, representativeness, and ongoing monitoring.

**Applicability:** Hugging Face TRL SFT and preference trainers vary across versions in chat-template support, loss masking, packing semantics, and trainer defaults; inspect actual deployed code and dataset format. LoRA/PEFT adapters depend on the exact base model and are not universally interchangeable. PyTorch documents that complete reproducibility cannot be guaranteed across releases and hardware even with identical random seeds. Restoring training exactly may require optimizer, scheduler and RNG states beyond model weights; distributed checkpoints have topology and compatibility constraints. Mixed precision benefits and numerical risks depend on hardware and dtype. AWS SageMaker output behavior applies only to that managed training platform; Google Cloud MLOps examples do not make its architecture universal. NIST AI RMF practices are voluntary guidance, not certification.

**Source review date:** 2026-11-12.
