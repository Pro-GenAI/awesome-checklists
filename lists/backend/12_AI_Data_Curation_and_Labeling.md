# 12 — AI Data Curation and Labeling Checklist

> Verify that datasets used for AI training, tuning, evaluation, or retrieval are lawfully and responsibly sourced, technically consistent, properly labeled, traceable to origin, and separated to avoid misleading evaluation. A large dataset or high annotator agreement alone does not establish correctness or representativeness.

> **Scope: Backend / API-specific.** This file is one part of the 12_AI_Data_Curation_and_Labeling.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **CUR-093** `P1` Authenticate and authorize dataset ingestion, upload, annotation, adjudication, export, and deletion endpoints.
- [ ] **CUR-094** `P0` Enforce source, project, annotator role, record, and tenant isolation on every dataset and label API.
- [ ] **CUR-095** `P1` Validate file types, encodings, MIME claims, schema constraints, sizes, and submitted label payloads before persistence.
- [ ] **CUR-096** `P1` Reject unsupported or malicious files and prevent execution of untrusted content during parsing or previews.
- [ ] **CUR-097** `P1` Use stable source-record IDs and idempotent import requests to prevent accidental duplicate data from retries.
- [ ] **CUR-098** `P1` Preserve raw source and derived data identifiers, metadata, and provenance when transferring records across services.
- [ ] **CUR-099** `P1` Ensure API contracts distinguish unannotated, draft, submitted, reviewed, adjudicated, rejected, and withdrawn labels.
- [ ] **CUR-100** `P1` Validate annotation version and optimistic concurrency to prevent reviewers silently overwriting each other's decisions.
- [ ] **CUR-101** `P1` Apply role-based approval for guideline changes, label taxonomy updates, and data release publication.
- [ ] **CUR-102** `P1` Test bulk exports for correct split membership, approved schema versions, source restrictions, and permitted consumers.
- [ ] **CUR-103** `P1` Redact or restrict sensitive annotations, protected data, and annotator identifiers in responses, logs, and telemetry.
- [ ] **CUR-104** `P1` Ensure scoped service accounts and expiring credentials are used for labeling vendors and automated data pipelines as appropriate.
- [ ] **CUR-105** `P1` Expose ingestion, labeling, deduplication, and validation failures through actionable status or error contracts.
- [ ] **CUR-106** `P1` Rate-limit and bound bulk ingest, media processing, auto-labeling, and export operations to protect service availability.
- [ ] **CUR-107** `P1` Validate source deletion, access revocation, and correction APIs against indexed, cached, and downstream data copies.
- [ ] **CUR-108** `P1` Prevent client-supplied fields from marking unreviewed machine-generated labels as human-adjudicated ground truth.
- [ ] **CUR-109** `P1` Make dataset version, schema version, transformation version, and labeling-guideline revision available to authorized clients.
- [ ] **CUR-110** `P1` Test webhook and task-queue retries for duplicate annotations, source update ordering, and finalization correctness.
- [ ] **CUR-111** `P1` Verify API audit trails support reconstructing a release without storing unnecessary personal or distressing raw content.
- [ ] **CUR-112** `P1` Run production-equivalent contract tests for annotation status, privacy controls, invalid inputs, and export integrity.

## Release gate

- [ ] The dataset's intended use, source inventories, stewardship, relevant licensing and privacy rights, and prohibited uses have been reviewed by accountable owners.
- [ ] Collection scope, sensitive fields, retention, vendor processing, deletion or withdrawal mechanisms, and access restrictions are approved for the actual use case.
- [ ] Data-quality checks cover critical schema fields, record counts, duplicates, corrupt examples, preprocessing integrity, and relevant population/language representation.
- [ ] Human or machine-assisted labeling follows versioned guidelines, with measured agreement or quality review and resolved high-impact ambiguities where labels are used.
- [ ] Training, validation, test, and holdout split rules have been reviewed for entity, temporal, near-duplicate, and synthetic/augmentation leakage that could invalidate evaluation.
- [ ] Dataset and label versions have reconstructable provenance, controlled changes, accessible documentation of limitations, and verified export integrity.
- [ ] Relevant API and frontend workflows protect annotator and source data, preserve review states, and prevent unauthorized releases or overwritten labels.
- [ ] Severe unresolved rights, privacy, contamination, bias, or label-integrity risks have been remediated or explicitly dispositioned by qualified human approvers before dataset use.

**Domain-specific approval rule:** Block dataset-release sign-off when collection/use rights are unknown for material records, restricted personal data is exposed, severe unresolved labeling defects undermine the target task, evaluation data leaks into training, or required source deletion cannot be honored within accepted controls. No dataset documentation or quality score guarantees freedom from bias, lawful use in every jurisdiction, or a reliable downstream model.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#12_ai_data_curation_and_labeling), not prerequisites or verification evidence.

## Trusted references and scope

These primary and authoritative resources support practical dataset-quality, labeling, provenance, and risk review. Some technical examples are vendor-specific and do not establish universal legal obligations or independent certification.

- [Google PAIR — Data Collection + Evaluation](https://pair.withgoogle.com/guidebook-v2/chapter/data-collection/) — responsible data sourcing, representation, labeling workflows, and dataset evaluation.
- [Hugging Face — Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) — dataset composition, use restrictions, licenses, languages, bias, and metadata.
- [TensorFlow Data Validation — Guide](https://www.tensorflow.org/tfx/guide/tfdv) — schema validation, data anomalies, training-serving skew, and drift.
- [TensorFlow Data Validation — Get Started](https://www.tensorflow.org/tfx/data_validation/get_started) — example-level and aggregate validation, distributions, and typed schema checks.
- [HumanSignal Label Studio — Labeling](https://docs.humansignal.com/guide/labeling) — annotation instructions, labeling interfaces, overlapping work, and machine suggestions.
- [HumanSignal Label Studio — Annotation Quality](https://docs.humansignal.com/guide/quality) — review workflows, agreement analysis, annotator calibration, and corrections; some features are enterprise-specific.
- [HumanSignal Label Studio — Task Agreement](https://docs.humansignal.com/guide/stats.html) — consensus, pairwise agreement, and suitable comparison for complex labels; vendor-specific.
- [W3C — PROV Overview](https://www.w3.org/TR/prov-overview/) — recording source and transformation provenance for trustworthy derived datasets.
- [MLCommons — Croissant Dataset Format](https://github.com/mlcommons/croissant) — interoperable dataset/resource metadata, semantic structure, and responsible ML description.
- [UK ICO — AI Security and Data Minimisation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-should-we-assess-security-and-data-minimisation-in-ai/) — UK privacy and minimization obligations for AI development where applicable.
- [NIST — AI Risk Management Framework Playbook](https://airc.nist.gov/airmf-resources/playbook/) — risk-based documentation, fairness, representativeness, and management of AI data limitations.
- [Hugging Face — Dataset Card Creation Guide](https://huggingface.co/docs/hub/en/datasets-cards) — documentation conventions and metadata fields for released datasets.

**Applicability:** Hugging Face dataset cards and MLCommons Croissant are useful documentation/metadata conventions, not mandatory formats for every dataset. TensorFlow Data Validation illustrates schema, skew, and drift techniques; equivalent tools are acceptable. HumanSignal Label Studio agreement and quality features can be edition-specific. W3C PROV describes interoperable lineage, not proof of permission to collect data. UK ICO guidance concerns applicable UK data-protection law; evaluate other markets separately. Human labels may be subjective and disagreement can reveal genuine task ambiguity.

**Source review date:** 2026-11-12.
