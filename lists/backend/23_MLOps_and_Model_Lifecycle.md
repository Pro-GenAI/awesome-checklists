# 23 — MLOps and Model Lifecycle Checklist

> Verify that AI/ML experiments, data, models, approvals, deployment configurations, and retirement decisions are traceable and managed across the system lifecycle. Registry entries and passing offline tests are inputs to a release decision, not proof of safe real-world operation.

> **Scope: Backend / API-specific.** This file is one part of the 23_MLOps_and_Model_Lifecycle.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **MLOPS-091** `P1` Expose inference, model metadata, and lifecycle endpoints through authenticated APIs with purpose-scoped permissions.
- [ ] **MLOPS-092** `P1` Verify production API responses and diagnostic headers identify the serving model revision where appropriate without leaking sensitive configuration.
- [ ] **MLOPS-093** `P1` Reject consumer requests that try to bypass approved routing, model versions, or safety policies.
- [ ] **MLOPS-094** `P1` Validate request feature schemas, input lengths, modalities, context sizes, and output contract requirements before inference.
- [ ] **MLOPS-095** `P0` Test authentication, authorization, and tenant isolation when selecting models, viewing experiment results, or invoking private endpoints.
- [ ] **MLOPS-096** `P1` Protect registry and promotion APIs with separate rights from ordinary inference access.
- [ ] **MLOPS-097** `P1` Require authorized approvals, invariant checks, and audit trails for model promotion, alias changes, and deactivation calls.
- [ ] **MLOPS-098** `P1` Validate model package signatures, digests, and runtime compatibility before deploy operations accept artifacts.
- [ ] **MLOPS-099** `P1` Test mixed-version inference clients and legacy consumers during canary and rollback.
- [ ] **MLOPS-100** `P2` Define rate limits, budget ceilings, timeouts, bounded retries, and behavior under quota exhaustion.
- [ ] **MLOPS-101** `P1` Measure model-load errors, inference tail latency, memory pressure, throughput, and provider failure rates by release.
- [ ] **MLOPS-102** `P1` Check data and prediction schema compatibility between training features, feature stores, and online/batch inference.
- [ ] **MLOPS-103** `P1` Validate retraining job triggers, input data version, deduplication, and scheduling permissions.
- [ ] **MLOPS-104** `P1` Prevent user-supplied model identifiers or paths from causing unsafe artifact loading or untrusted code execution.
- [ ] **MLOPS-105** `P1` Protect model weights, prompts, customer features, and prediction payloads from unintended logs or unapproved data transfers.
- [ ] **MLOPS-106** `P1` Test fallback routing for unavailable providers, revoked versions, incompatible outputs, and policy updates.
- [ ] **MLOPS-107** `P1` Ensure telemetry provides safe experiment, registry, deployment, and inference correlation IDs.
- [ ] **MLOPS-108** `P1` Confirm canceled, failed, and partial training jobs cannot be mistaken for approved model packages.
- [ ] **MLOPS-109** `P1` Verify model-retirement APIs invalidate serving routes, caches, and dependent scheduled jobs as designed.
- [ ] **MLOPS-110** `P1` Run production-equivalent API contract tests against approved model promotion and rollback configurations.

## Release gate

- [ ] Critical model training and tuning runs are traceable to reviewed code, data, environment, configuration, evaluation, and identifiable accountable owners.
- [ ] The approved model artifact or provider snapshot has verifiable identity, provenance, integrity, permissioned registry metadata, and documented intended use and limitations.
- [ ] Quality, safety, privacy, performance, compatibility, and resource/cost thresholds have been evaluated against representative conditions and a known-good baseline.
- [ ] Authorized promotion gates validate the specific model and associated feature, schema, prompt, tool, and serving configurations; unapproved versions cannot be deployed.
- [ ] Production-equivalent deployment, staged rollout, mixed-version compatibility, endpoint health, and rollback or safe-disablement tests pass.
- [ ] Ongoing monitoring, incident escalation, user feedback, drift investigation, retraining approvals, and retention/decommissioning procedures have named owners.
- [ ] Relevant API and frontend behaviors remain safe and comprehensible across model changes, fallback, and retired capabilities.
- [ ] Residual material risks and unresolved failures are documented and approved by appropriately qualified humans for the exact release.

**Domain-specific approval rule:** Block sign-off when a production model cannot be traced to approved data and code, integrity or access controls permit unreviewed artifacts to be deployed, severe evaluation or privacy findings are unresolved, or rollback/emergency disablement is required but untested. Automatic retraining does not confer automatic deployment authorization.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#23_mlops_and_model_lifecycle), not prerequisites or verification evidence.

## Trusted references and scope

These primary specifications, project documentation, and authoritative risk-management resources support the lifecycle checks. They describe different architectures and are not interchangeable certification requirements.

- [Google Cloud Architecture Center — MLOps CI/CD/CT](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — automation, testing, metadata, continuous training, and serving lifecycle; emphasis on predictive ML.
- [MLflow — Experiment Tracking](https://mlflow.org/docs/latest/tracking/) — experiment run metadata, datasets, artifacts, metrics, parameters, and run comparison.
- [MLflow — Model Registry](https://mlflow.org/docs/latest/registry/) — model versioning, registry ownership, aliases, lineage, and approval metadata.
- [MLflow — Model Registry Workflows](https://mlflow.org/docs/latest/ml/model-registry/workflow/) — promotion workflows and migration away from deprecated fixed model stages.
- [Kubeflow Pipelines — ML Metadata](https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/) — pipeline executions, artifact lineage, metadata, and operational migration considerations.
- [Kubeflow Pipelines — ML Artifacts](https://www.kubeflow.org/docs/components/pipelines/user-guides/data-handling/artifacts/) — typed datasets, model artifacts, provenance, and pipeline artifact lifecycle.
- [TensorFlow Extended — ML Metadata](https://www.tensorflow.org/tfx/guide/mlmd) — tracking relationships among data, training runs, model artifacts, and software dependencies.
- [Amazon SageMaker AI — Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) — model package approvals, lineage, metadata, and controlled deployment.
- [Amazon SageMaker AI — Pipelines Overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html) — processing, training, evaluation, condition gates, and model registration workflows.
- [NIST AI RMF Playbook — Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) — human risk decisions, continual monitoring, recovery, vendor oversight, and decommissioning.
- [SLSA v1.2 — Provenance](https://slsa.dev/spec/v1.2/provenance) — verifiable artifact build/source provenance relevant to model packaging and serving supply chains.
- [OpenTelemetry — Generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — model, operation, token, and response observability with sensitivity safeguards.

**Applicability:** Google Cloud's MLOps architecture article principally covers predictive machine learning; generative AI may use provider-managed models rather than locally trained artifacts. MLflow fixed Staging/Production/Archived model stages are deprecated in favor of model aliases, tags, and suitable environment access control; a mutable alias must never replace an immutable release identity. Kubeflow, TensorFlow ML Metadata, and SageMaker capabilities depend on the deployed version and provider configuration. SLSA is supply-chain provenance guidance, not proof of permission to use training data. OpenTelemetry's GenAI conventions and implementation support may evolve; avoid logging protected prompt or response content without an approved policy. NIST AI RMF is voluntary and not a certification.

**Source review date:** 2026-11-12.
