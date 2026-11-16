# 14 — AI Fine-tuning and Training Checklist

> Verify that training or fine-tuning a model is justified, reproducible, permissioned, numerically stable, evaluated for unintended behavioral changes, and released under explicit control. Lower training loss or a successful provider job alone does not establish model quality, safety, data rights, or deployment readiness.

> **Scope: Backend / API-specific.** This file is one part of the 14_AI_FineTuning_and_Training.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **TRAIN-093** `P1` Authenticate and authorize training-job creation, dataset association, model promotion, checkpoint retrieval, and cancellation endpoints.
- [ ] **TRAIN-094** `P1` Use separate scoped roles for launching experiments, accessing protected data, reviewing models, and promoting production releases.
- [ ] **TRAIN-095** `P1` Validate base-model IDs, fine-tuning methods, data references, hyperparameters, and job configurations against approved server-side allowlists.
- [ ] **TRAIN-096** `P1` Prevent untrusted API requests from selecting arbitrary files, URLs, model packages, or executable training code.
- [ ] **TRAIN-097** `P1` Enforce per-user, per-tenant, and per-project compute quotas, concurrent-job ceilings, and total cost limits.
- [ ] **TRAIN-098** `P1` Verify data-processing region, provider training use, retention, and external transfer restrictions for hosted training APIs.
- [ ] **TRAIN-099** `P1` Ensure uploaded training data and evaluation fixtures are accessible only to authorized training and grading services.
- [ ] **TRAIN-100** `P1` Do not include private examples, provider credentials, or protected model artifacts in default job logs or diagnostic responses.
- [ ] **TRAIN-101** `P1` Return stable run, dataset, checkpoint, and artifact identifiers with documented version and authorization semantics.
- [ ] **TRAIN-102** `P1` Expose distinct states for queued, validating, training, evaluating, failed, canceled, completed, and approved jobs.
- [ ] **TRAIN-103** `P1` Validate API behavior for malformed training examples, missing splits, unsupported methods, and over-limit datasets.
- [ ] **TRAIN-104** `P1` Test cancellation and retries so terminated or duplicated jobs do not silently incur runaway compute or promote stale artifacts.
- [ ] **TRAIN-105** `P1` Use authenticated and replay-resistant callbacks or event delivery for training completion and promotion events.
- [ ] **TRAIN-106** `P1` Verify that fine-tuned inference endpoints load the exact approved base/checkpoint/adapter combination.
- [ ] **TRAIN-107** `P1` Test structured inference outputs and safety controls after the tuned model is introduced through API routing.
- [ ] **TRAIN-108** `P1` Require independent model-evaluation and risk gates before update of production model aliases or endpoint deployments.
- [ ] **TRAIN-109** `P1` Protect checkpoint download, model export, and adapter merge operations with artifact-integrity and permission checks.
- [ ] **TRAIN-110** `P2` Maintain safe correlation from training jobs to evaluation reports, deployed inference routes, and incident records.
- [ ] **TRAIN-111** `P1` Test provider errors, quota exhaustion, model deprecation, and incompatible checkpoint formats for predictable recovery behavior.
- [ ] **TRAIN-112** `P1` Include training-to-serving compatibility, data privacy, and fallback contract tests in the release workflow.

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

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#14_ai_finetuning_and_training), not prerequisites or verification evidence.

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
