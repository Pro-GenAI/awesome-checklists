# 17 — MLOps and Model Lifecycle Checklist

> Verify that AI/ML experiments, data, models, approvals, deployment configurations, and retirement decisions are traceable and managed across the system lifecycle. Registry entries and passing offline tests are inputs to a release decision, not proof of safe real-world operation.

> **Scope: AI-specific.** This file is one part of the 17_MLOps_and_Model_Lifecycle.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Experiments and reproducibility

- [ ] **MLOPS-001** `P2` Define the model's intended task, business owner, supported use, and measurable performance and risk thresholds before starting experiments.
- [ ] **MLOPS-002** `P1` Keep training, evaluation, and pipeline code under reviewed version control with traceable change history.
- [ ] **MLOPS-003** `P2` Record the exact source revision, training entry point, execution pipeline, and runtime environment for each consequential experiment.
- [ ] **MLOPS-004** `P1` Version data snapshots, sample-selection rules, feature transformations, labels, and split assignments consumed by each run.
- [ ] **MLOPS-005** `P1` Capture model architecture, base checkpoint, tuning method, optimizer, hyperparameters, and configuration for every promoted candidate.
- [ ] **MLOPS-006** `P2` Record random seeds, deterministic settings, accelerator/software libraries, and known sources of nondeterminism.
- [ ] **MLOPS-007** `P1` Preserve task metrics, validation results, severe failures, and statistical uncertainty alongside model outputs.
- [ ] **MLOPS-008** `P2` Record training and evaluation hardware type, runtime, utilization, costs, and resource limits for material experiments.
- [ ] **MLOPS-009** `P1` Use an experiment tracker or equivalent immutable run records so results can be compared and audited.
- [ ] **MLOPS-010** `P2` Assign globally unique run IDs and link child trials, hyperparameter searches, and resumed training jobs to their parents.
- [ ] **MLOPS-011** `P1` Validate input schema, missing fields, corrupted examples, class distributions, and data quality before training begins.
- [ ] **MLOPS-012** `P1` Check data-preparation and feature-pipeline tests with known-correct fixtures, including edge values and encoding.
- [ ] **MLOPS-013** `P1` Prevent training-to-validation contamination and evaluation leakage in snapshots, feature stores, prompts, and augmented data.
- [ ] **MLOPS-014** `P1` Test pipeline reproducibility by rerunning representative experiments against approved inputs and comparing expected tolerances.
- [ ] **MLOPS-015** `P1` Distinguish reproducible computation from statistically identical nondeterministic model outcomes.
- [ ] **MLOPS-016** `P2` Track preprocessing, tokenization, embedding, retrieval, and safety configurations that change model behavior where relevant.
- [ ] **MLOPS-017** `P1` Store experiment artifacts and logs with scoped access and retention; exclude production secrets and unnecessary protected training examples.
- [ ] **MLOPS-018** `P1` Validate checkpoint and artifact integrity before using resumed or transferred training outputs.
- [ ] **MLOPS-019** `P2` Define how failed, interrupted, partial, or canceled runs are classified and excluded from approval calculations.
- [ ] **MLOPS-020** `P1` Separate research experimentation resources and credentials from production training and inference systems.
- [ ] **MLOPS-021** `P2` Publish a clear comparison of candidate versus baseline quality, cost, reliability, fairness, and other risk-relevant metrics.
- [ ] **MLOPS-022** `P2` Document experiment owner, conclusions, data caveats, and go/no-go decision before a candidate is registered for release.

## Model registries and lineage

- [ ] **MLOPS-023** `P1` Use a controlled registry or equivalent artifact catalog for every model or externally hosted snapshot approved for production.
- [ ] **MLOPS-024** `P2` Assign immutable model version identifiers and maintain the exact artifact digest or provider revision where available.
- [ ] **MLOPS-025** `P2` Track model provider, license, original base model, adapter or fine-tune, framework, and intended serving runtime.
- [ ] **MLOPS-026** `P1` Link each registered model version to the experiment or training job that produced it.
- [ ] **MLOPS-027** `P2` Record provenance for training, validation, and evaluation datasets and the transformations used to create them.
- [ ] **MLOPS-028** `P1` Link each model to its evaluation suite, task scores, severe failures, risk decisions, and approval evidence.
- [ ] **MLOPS-029** `P1` Store relevant model-card documentation, intended uses, constraints, and known limitations alongside the registry entry.
- [ ] **MLOPS-030** `P2` Define registry ownership and role-based permission for publishing, reviewing, promoting, archiving, and deleting versions.
- [ ] **MLOPS-031** `P1` Prevent unreviewed models or model aliases from being promoted by users without authorization.
- [ ] **MLOPS-032** `P1` Verify that aliases or deployment pointers resolve to an approved immutable version at release time.
- [ ] **MLOPS-033** `P1` Audit alias reassignment and registry edits with actor, timestamp, prior target, new target, and change reason.
- [ ] **MLOPS-034** `P1` Check compatibility between model artifact format, serialization library, inference framework, runtime, and required hardware.
- [ ] **MLOPS-035** `P1` Scan serialized artifacts and dependencies for unsafe deserialization paths or untrusted executable content before loading.
- [ ] **MLOPS-036** `P1` Use signed provenance, hashes, or equivalent integrity controls for models and supporting build artifacts where warranted.
- [ ] **MLOPS-037** `P1` Make feature schemas, tokenizer versions, prompt templates, output contracts, and serving configuration discoverable from the model version.
- [ ] **MLOPS-038** `P1` Link feature store snapshots and materialized feature definitions to the registered model where that architecture is used.
- [ ] **MLOPS-039** `P2` Track deployment location, endpoint version, traffic share, and active consumers for every released model.
- [ ] **MLOPS-040** `P1` Keep release-critical prior model versions and compatible dependencies available for the agreed rollback window.
- [ ] **MLOPS-041** `P2` Define data, artifact, registry, and audit retention separately, including required privacy and intellectual-property controls.
- [ ] **MLOPS-042** `P1` Propagate correction or deletion requirements to copies, caches, re-exported artifacts, and downstream uses when applicable.
- [ ] **MLOPS-043** `P1` Validate registry lookup, model download, and dependency resolution in a production-equivalent environment before promotion.
- [ ] **MLOPS-044** `P1` Reconcile registry metadata with actual deployed model revisions rather than assuming metadata proves runtime state.

## Promotion, deployment, and rollback

- [ ] **MLOPS-045** `P2` Define development, evaluation, staging, production, and retirement states using explicit approval policy, not only a registry label.
- [ ] **MLOPS-046** `P1` Require a recorded qualified approver and current evaluation evidence for risk-defined model promotion.
- [ ] **MLOPS-047** `P1` Gate training and deployment pipelines on data-schema tests, reproducible artifacts, and model-quality and safety acceptance results.
- [ ] **MLOPS-048** `P1` Run model and pipeline integration tests against the actual feature, retrieval, tool, and inference dependencies.
- [ ] **MLOPS-049** `P1` Verify container images, packages, model files, configuration, and build provenance match approved release artifacts.
- [ ] **MLOPS-050** `P1` Check resource compatibility, model load time, memory headroom, accelerators, runtime versions, and warm-up behavior.
- [ ] **MLOPS-051** `P1` Test online, batch, streaming, and asynchronous inference paths supported by the selected deployment architecture.
- [ ] **MLOPS-052** `P2` Record model version, configuration, endpoint, feature flags, planned audience, and rollout window in a release manifest.
- [ ] **MLOPS-053** `P1` Use staged traffic, shadow inference, canary, or blue-green deployment where risk and architecture warrant it.
- [ ] **MLOPS-054** `P2` Define initial cohort, traffic promotion increments, observation periods, and stop criteria before rollout.
- [ ] **MLOPS-055** `P1` Test p95/p99 latency, errors, throughput, capacity, and unit cost under representative production-like load.
- [ ] **MLOPS-056** `P1` Verify output quality, refusal rates, drift indicators, and high-impact user outcomes against predeclared guardrails.
- [ ] **MLOPS-057** `P1` Confirm model and associated prompt, tokenizer, schema, feature, retrieval, and safety versions remain compatible while mixed versions serve traffic.
- [ ] **MLOPS-058** `P1` Check whether a rolled-back model can read data written by the new version and whether any migration is irreversible.
- [ ] **MLOPS-059** `P1` Test traffic rollback, registry-pointer reversal, feature disablement, or safe non-AI fallback in a controlled environment.
- [ ] **MLOPS-060** `P2` Define recovery options when models rely on mutable external providers or revisions that cannot be restored exactly.
- [ ] **MLOPS-061** `P1` Verify failed or partial deployments do not leave orphaned endpoints, duplicate jobs, unbounded cost, or stale traffic routing.
- [ ] **MLOPS-062** `P1` Use infrastructure-as-code or reproducible deployment configuration where applicable to avoid manual environment drift.
- [ ] **MLOPS-063** `P1` Limit production promotion rights and protect credentials, model artifacts, and high-impact environment settings.
- [ ] **MLOPS-064** `P1` Ensure rollout automation stops on failed health checks rather than silently expanding exposure.
- [ ] **MLOPS-065** `P2` Record release decisions and actual serving versions and compare them with the approved manifest after deployment.
- [ ] **MLOPS-066** `P2` Maintain model-specific on-call runbooks, alert routes, emergency disabling, and provider support contacts.
- [ ] **MLOPS-067** `P1` Verify downstream API clients and frontend experiences remain compatible across staged rollouts and rollback.
- [ ] **MLOPS-068** `P2` Define the stabilization period and accountable reviewer for final post-deployment acceptance.

## Retraining and lifecycle governance

- [ ] **MLOPS-069** `P2` Assign lifecycle owners for model quality, data pipeline integrity, serving operations, regulatory review, and eventual decommissioning.
- [ ] **MLOPS-070** `P2` Define retraining triggers based on observed drift, performance degradation, data changes, scheduled refresh, or business requirements.
- [ ] **MLOPS-071** `P1` Distinguish label delay and data-availability lag from true concept or model-performance drift before triggering retraining.
- [ ] **MLOPS-072** `P1` Keep retraining data selection, rights, consent, retention, and sensitive-data handling subject to current approved policies.
- [ ] **MLOPS-073** `P2` Define whether retraining is automatic, manually approved, or prohibited for specific high-impact model categories.
- [ ] **MLOPS-074** `P1` Ensure a retraining run does not automatically replace a production model without the required evaluation and promotion gate.
- [ ] **MLOPS-075** `P1` Monitor incoming training data schema, source quality, class balance, distribution shift, and possible poisoning.
- [ ] **MLOPS-076** `P1` Repeat necessary subgroup, safety, task, regression, and robustness evaluations for each new candidate.
- [ ] **MLOPS-077** `P1` Compare retrained models against a known-good baseline using representative held-out and post-deployment cases.
- [ ] **MLOPS-078** `P2` Record new data, label, algorithm, provider, and tuning changes so improvements and regressions are attributable.
- [ ] **MLOPS-079** `P1` Test pipeline retries, interruption recovery, parallel training, and duplicate-trigger prevention to avoid uncontrolled costs.
- [ ] **MLOPS-080** `P2` Maintain appropriate retraining compute quotas, budget alerts, and workload priority controls.
- [ ] **MLOPS-081** `P1` Capture model predictions or authorized outcome signals needed for monitoring without retaining unnecessary protected content.
- [ ] **MLOPS-082** `P2` Define monitoring metrics and escalation for input changes, output anomalies, severe failures, and business outcome degradation.
- [ ] **MLOPS-083** `P2` Document incident workflows for unexpected bias, hallucination, leakage, unsafe agent behavior, or inappropriate autonomous actions.
- [ ] **MLOPS-084** `P1` Retain a tested ability to quarantine a candidate, roll back a release, or disable a model after emerging harm.
- [ ] **MLOPS-085** `P1` Review third-party model/provider deprecations, license changes, pricing changes, and data-processing policy updates.
- [ ] **MLOPS-086** `P2` Define how feedback and user complaints become sanitized, versioned training or evaluation records after review.
- [ ] **MLOPS-087** `P1` Update model cards, release notes, risk evaluations, and user disclosures after material changes.
- [ ] **MLOPS-088** `P1` Periodically audit registry ownership, obsolete artifacts, inactive endpoints, access rights, and deployment costs.
- [ ] **MLOPS-089** `P2` Define retirement triggers including unsupported use, expired rights, unmitigated risk, or declining operational value.
- [ ] **MLOPS-090** `P1` Decommission models with a plan for endpoint shutdown, dependent clients, data retention, deletion, and required audit records.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **MLOPS-111** `P1` Confirm the interface accurately communicates AI capability, known limits, and changes in behavior resulting from a model release.
- [ ] **MLOPS-112** `P1` Test essential user journeys on the candidate and approved baseline model with the same UI and authorized data.
- [ ] **MLOPS-113** `P1` Verify frontend feature flags select only the server-approved model routing and cannot grant privileged model access.
- [ ] **MLOPS-114** `P1` Show meaningful loading, timeout, refusal, fallback, and error states when a new model behaves differently.
- [ ] **MLOPS-115** `P1` Confirm model changes do not break structured UI cards, generated markup, citations, or downstream field validation.
- [ ] **MLOPS-116** `P1` Validate streaming partial responses, cancellations, and retry states across staged model deployments.
- [ ] **MLOPS-117** `P1` Test accessibility of dynamic model outputs, status announcements, keyboard navigation, and error feedback.
- [ ] **MLOPS-118** `P1` Include supported languages, scripts, devices, and assistive technologies in release-specific UI tests.
- [ ] **MLOPS-119** `P1` Explain to users when tasks are unavailable because an incompatible or retired model capability was disabled.
- [ ] **MLOPS-120** `P1` Ensure consequential tool actions still require appropriate user confirmation after model replacement.
- [ ] **MLOPS-121** `P1` Check privacy notices and user consent text match the actual deployed model/provider data handling.
- [ ] **MLOPS-122** `P1` Test a safe fallback experience for disabled AI features, provider outages, and rollback.
- [ ] **MLOPS-123** `P1` Prevent cached conversations and generated artifacts from exposing prior users' protected content after account changes.
- [ ] **MLOPS-124** `P1` Verify model-specific references, disclosures, and help content are updated when a release changes supported features.
- [ ] **MLOPS-125** `P1` Check perceived latency and user-task completion time when model response length or inference speed changes.
- [ ] **MLOPS-126** `P1` Confirm UI telemetry can associate errors and approved user feedback with the model release without logging unnecessary private prompts.
- [ ] **MLOPS-127** `P1` Make it possible to report harmful or wrong outputs with traceable, privacy-safe incident identifiers.
- [ ] **MLOPS-128** `P1` Check old browser tabs, cached bundles, and mobile clients against the new model's response schemas.
- [ ] **MLOPS-129** `P1` Verify that frontend experiments or cohort routing do not misattribute model outputs or show incorrect completion status.
- [ ] **MLOPS-130** `P1` Validate rollback does not strand unfinished workflows, saved drafts, or user-visible external actions.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#17_mlops_and_model_lifecycle), not prerequisites or evidence of PASS.

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
