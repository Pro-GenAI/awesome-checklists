# 06 — AI Data Curation and Labeling Checklist

> Verify that datasets used for AI training, tuning, evaluation, or retrieval are lawfully and responsibly sourced, technically consistent, properly labeled, traceable to origin, and separated to avoid misleading evaluation. A large dataset or high annotator agreement alone does not establish correctness or representativeness.

> **Scope: AI-specific.** This file is one part of the 06_AI_Data_Curation_and_Labeling.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Dataset sourcing and rights

- [ ] **CUR-001** `P2` Define each dataset's intended model task, target population, owners, and permitted training, tuning, and evaluation uses.
- [ ] **CUR-002** `P2` Inventory each original data source, supplier, collection method, acquisition date, and source-of-truth location.
- [ ] **CUR-003** `P2` Record provenance at a level that can trace a released example back to its permitted source and transformation history.
- [ ] **CUR-004** `P1` Verify licensing and terms explicitly permit the contemplated machine-learning, derivative, redistribution, and commercial uses.
- [ ] **CUR-005** `P1` Review contractual restrictions on scraping, retention, transfer, benchmarking, sharing, and downstream model outputs where relevant.
- [ ] **CUR-006** `P1` Determine applicable lawful basis, notice, consent, and other privacy obligations with qualified reviewers before using personal data.
- [ ] **CUR-007** `P2` Document any sensitive or regulated attributes and limit access and processing to what the specific use case requires.
- [ ] **CUR-008** `P1` Assess the rights and consent associated with identifiable image, voice, video, location, and biometric data where applicable.
- [ ] **CUR-009** `P1` Distinguish publicly accessible content from content actually authorized for collection or model development.
- [ ] **CUR-010** `P2` Record geographic, age-group, language, and temporal coverage and compare it with the intended deployment audience.
- [ ] **CUR-011** `P2` Identify affected or underrepresented communities and include relevant domain stakeholders in source selection.
- [ ] **CUR-012** `P2` Define sampling inclusion and exclusion criteria before collecting or curating data where feasible.
- [ ] **CUR-013** `P1` Quantify selection bias risks from collection channels, demographics, opt-in patterns, and device or network access.
- [ ] **CUR-014** `P1` Inspect sources for known quality problems, unreliable labels, synthetic material, spam, and adversarial contamination.
- [ ] **CUR-015** `P2` Define required provenance and integrity checks for data received from vendors, annotators, and third-party datasets.
- [ ] **CUR-016** `P1` Validate external transfer, provider retention, geographic storage, and subprocessor arrangements before supplying data to labeling or model vendors.
- [ ] **CUR-017** `P2` Assign an owner for source corrections, takedowns, rights challenges, and consent withdrawals.
- [ ] **CUR-018** `P2` Define how an erasure or source revocation reaches raw datasets, label stores, caches, exports, and derived model-training artifacts where required.
- [ ] **CUR-019** `P1` Use documented collection minimization and an approved retention schedule rather than keeping all source data indefinitely.
- [ ] **CUR-020** `P1` Restrict access to original sensitive sources and prevent accidental disclosure via dataset cards, examples, or shared repositories.
- [ ] **CUR-021** `P2` Document known limitations, collection gaps, consent-related biases, and suitability restrictions in a maintained dataset description.
- [ ] **CUR-022** `P1` Approve source additions or major licensing, population, and purpose changes before adding them to released training or evaluation data.

## Data quality and preparation

- [ ] **CUR-023** `P2` Define a versioned data schema, expected types, nullability, valid ranges, and allowed categorical values for every relevant field.
- [ ] **CUR-024** `P1` Verify ingest completeness with record counts, source IDs, checksums, and expected update windows where available.
- [ ] **CUR-025** `P1` Detect invalid encodings, truncated documents, unreadable media, corrupted records, and parser exceptions before labeling.
- [ ] **CUR-026** `P1` Apply documented normalization of text, Unicode, timestamps, identifiers, units, and other format-dependent features.
- [ ] **CUR-027** `P2` Record preprocessing order and parameters so curated datasets can be rebuilt reproducibly.
- [ ] **CUR-028** `P1` Measure missingness, outliers, duplicates, distribution shape, and class balance for relevant features and labels.
- [ ] **CUR-029** `P1` Detect exact and near-duplicate examples across sources before training and split assignment.
- [ ] **CUR-030** `P1` Preserve meaningful signals while removing or flagging spam, mislabeled, harmful, or irrelevant records.
- [ ] **CUR-031** `P1` Review whether cleaning rules disproportionately exclude specific languages, dialects, accessibility cases, or population groups.
- [ ] **CUR-032** `P1` Verify transformations do not silently strip negation, qualifiers, dialect features, units, or context needed for correct labels.
- [ ] **CUR-033** `P2` Define special handling for low-resource languages, scripts, mixed-language text, code-switching, and non-Latin inputs as applicable.
- [ ] **CUR-034** `P1` Validate document and multimedia preprocessing preserves speaker, timing, coordinate, or page-reference metadata where important.
- [ ] **CUR-035** `P1` Screen for unnecessary credentials, personal identifiers, protected fields, and prohibited confidential source content.
- [ ] **CUR-036** `P2` Document redaction and pseudonymization methods and test that supposedly removed sensitive information cannot still be recovered trivially.
- [ ] **CUR-037** `P1` Assess the privacy and fidelity of synthetic or augmented examples rather than treating synthetic data as automatically anonymous.
- [ ] **CUR-038** `P1` Keep source, human-generated, model-generated, and augmented records distinguishable for bias and contamination analysis.
- [ ] **CUR-039** `P1` Test that data augmentation does not change intended semantics or replicate protected source records beyond permitted uses.
- [ ] **CUR-040** `P1` Check training, evaluation, and serving input feature schemas for mismatches and missing required values.
- [ ] **CUR-041** `P1` Compare representative curated data distributions with the expected deployment distribution, including relevant time and segment changes.
- [ ] **CUR-042** `P2` Track anomaly thresholds, false alarms, owner decisions, and exceptions for data-quality checks.
- [ ] **CUR-043** `P1` Test batch and incremental curation for deterministic or otherwise documented behavior across reruns.
- [ ] **CUR-044** `P1` Version scripts, dependencies, extraction settings, feature definitions, and transformation outputs alongside curated datasets.
- [ ] **CUR-045** `P1` Quarantine or reject records with material unresolvable errors instead of silently guessing their content or labels.
- [ ] **CUR-046** `P2` Maintain data-quality dashboards or reports with row counts, missing fields, drift, duplicates, and source-specific failure rates.

## Labeling and adjudication

- [ ] **CUR-047** `P2` Define the annotation unit and clear label taxonomy, including mutually exclusive, multi-label, hierarchical, or span-based cases.
- [ ] **CUR-048** `P1` Write task-specific guidelines with positive and negative examples, boundary cases, and consistent decision criteria.
- [ ] **CUR-049** `P1` Include explicit labels or procedures for uncertainty, ambiguity, insufficient evidence, and genuinely unlabelable examples.
- [ ] **CUR-050** `P2` Describe how annotators should treat mixed-language, dialectal, culturally dependent, and domain-specific input.
- [ ] **CUR-051** `P2` Specify how annotators should handle subjective labels, value judgments, and disputed or context-sensitive categories.
- [ ] **CUR-052** `P1` Validate labeling UI and instructions with representative annotators before scaling collection.
- [ ] **CUR-053** `P1` Recruit or qualify annotators with language, domain, cultural, and accessibility expertise appropriate to the task.
- [ ] **CUR-054** `P1` Provide paid or otherwise approved training, calibration, and feedback consistent with applicable labor and contractual rules.
- [ ] **CUR-055** `P1` Restrict annotator access to only the data needed, and train workers on sensitive-data handling and reporting.
- [ ] **CUR-056** `P1` Design ergonomic, accessible labeling tools and safe support procedures for exposure to potentially distressing content.
- [ ] **CUR-057** `P2` Specify task assignment, randomization, overlap, and independence rules to reduce systematic annotator bias.
- [ ] **CUR-058** `P1` Create expert-reviewed gold or calibration items where the task permits an objectively defensible reference.
- [ ] **CUR-059** `P1` Measure intra-annotator and inter-annotator consistency using a metric appropriate to label type and chance agreement.
- [ ] **CUR-060** `P1` Review agreement by label, source, language, demographic proxy where lawful, and difficulty instead of relying on one global score.
- [ ] **CUR-061** `P1` Investigate low agreement as a possible ambiguity or guideline defect rather than always blaming annotators.
- [ ] **CUR-062** `P2` Define escalation and independent adjudication for disagreements, rare cases, and high-impact labels.
- [ ] **CUR-063** `P2` Record adjudication decisions and rationale so confusing guideline cases can be clarified.
- [ ] **CUR-064** `P1` Version annotation guidelines and document whether a guideline change requires affected labels to be reworked.
- [ ] **CUR-065** `P2` Track labeling corrections, revisions, annotator identifiers or permitted pseudonyms, timestamps, and approval state.
- [ ] **CUR-066** `P1` Use targeted double review, audit sampling, or expert review for high-impact and low-confidence labels.
- [ ] **CUR-067** `P1` Evaluate pre-labels and model-assisted annotation for anchoring bias, automation bias, and compounding model errors.
- [ ] **CUR-068** `P1` Check that annotators can correct or reject machine suggestions rather than being forced to approve them.
- [ ] **CUR-069** `P1` Monitor labeling throughput and error rates without trading away the quality necessary for the stated use.
- [ ] **CUR-070** `P1` Verify labeled exports preserve sample IDs, label definitions, geometry/span references, adjudication status, and provenance.

## Splits, leakage, and provenance

- [ ] **CUR-071** `P2` Define training, validation, test, and any holdout or temporal split policy before tuning the model.
- [ ] **CUR-072** `P1` Partition by the appropriate independent unit, such as person, account, document, subject, device, or time window.
- [ ] **CUR-073** `P1` Prevent the same user, source document, event family, or near-duplicate content from leaking across independent splits.
- [ ] **CUR-074** `P1` Use group-based or time-based splits for correlated records when random row splits would inflate reported performance.
- [ ] **CUR-075** `P1` Keep a final holdout evaluation set separate from prompt tuning, labeling-rule adjustments, and model selection decisions.
- [ ] **CUR-076** `P1` Audit train/evaluation overlap after augmentation, translation, synthetic generation, and near-duplicate expansion.
- [ ] **CUR-077** `P2` Track contamination risks when benchmark questions, answers, or evaluation examples become available to model training.
- [ ] **CUR-078** `P1` Recheck splits for new data batches and changed entity identity rules rather than assuming historical partitions remain safe.
- [ ] **CUR-079** `P1` Assess whether each split contains enough critical classes, languages, scenarios, and relevant groups to evaluate the intended system.
- [ ] **CUR-080** `P2` Document when stratification or oversampling alters evaluation prevalence and report limitations when interpreting metrics.
- [ ] **CUR-081** `P2` Record dataset version, manifest, sample IDs, split membership, checksums, and relevant source snapshot identifiers.
- [ ] **CUR-082** `P1` Version labeling instructions, adjudication changes, schemas, and preprocessing code with their resulting dataset artifacts.
- [ ] **CUR-083** `P1` Ensure a model run can identify the exact dataset and transformation revisions used for training and evaluation.
- [ ] **CUR-084** `P2` Maintain end-to-end lineage from acquired source through cleaning, labeling, split assignment, and exported training records.
- [ ] **CUR-085** `P1` Control who can modify a frozen validation or holdout set, and audit authorized revisions to it.
- [ ] **CUR-086** `P1` Test export/import and storage integrity with checksums or equivalent consistency validation where appropriate.
- [ ] **CUR-087** `P2` Define how corrected labels propagate to downstream versions without silently changing prior benchmark results.
- [ ] **CUR-088** `P1` Remove withdrawn, revoked, or expired records from future dataset releases and assess whether prior model artifacts need remediation.
- [ ] **CUR-089** `P2` Publish a dataset card or equivalent description covering creation, composition, labels, intended use, licensing, limitations, and risks.
- [ ] **CUR-090** `P1` Report known gaps in data provenance, subgroup coverage, and uncertain ground truth as limitations rather than hiding them.
- [ ] **CUR-091** `P1` Establish a periodic review for dataset drift, obsolescence, label-taxonomy changes, and new source restrictions.
- [ ] **CUR-092** `P1` Require responsible owner approval and an auditable change record before publishing a training or evaluation dataset release.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **CUR-113** `P1` Display project labeling instructions, taxonomy definitions, and contextual examples adjacent to annotation controls.
- [ ] **CUR-114** `P1` Ensure annotators can identify ambiguous, unlabelable, or insufficient-context samples without fabricating a label.
- [ ] **CUR-115** `P1` Give annotators a way to report unsafe content, task defects, confusing instructions, and suspected bias.
- [ ] **CUR-116** `P1` Make assignment, draft, submission, review, rejection, and adjudication states visibly distinguishable.
- [ ] **CUR-117** `P1` Prevent accidental duplicate submissions and warn before overwriting or losing unsaved annotation work.
- [ ] **CUR-118** `P1` Provide accessible keyboard controls, meaningful focus behavior, labels, and status announcements for labeling tools.
- [ ] **CUR-119** `P1` Test supported screen readers, text scaling, high contrast, and non-pointer operation on critical annotation journeys.
- [ ] **CUR-120** `P1` Verify image, audio, video, and text annotation controls preserve correct coordinates, timing, spans, and selection under zoom.
- [ ] **CUR-121** `P1` Show source context, relevant dates, language, and evidence without exposing unrelated protected source data.
- [ ] **CUR-122** `P1` Support the scripts, locale formatting, Unicode input, and right-to-left behavior required by labeling audiences.
- [ ] **CUR-123** `P1` Allow reviewers to compare independent annotations and resolve disagreements without misrepresenting machine suggestions as ground truth.
- [ ] **CUR-124** `P1` Clearly label machine-preannotated content and require explicit human acceptance where the review policy requires it.
- [ ] **CUR-125** `P1` Prevent machine-suggested labels from biasing independent blind reviews where independence is part of the study design.
- [ ] **CUR-126** `P1` Restrict personal-data previews, exports, and image downloads to authorized annotators and reviewers.
- [ ] **CUR-127** `P1` Ensure annotation text, media metadata, and user-supplied source content are safely rendered without active-script injection.
- [ ] **CUR-128** `P1` Display accurate remaining task count, progress, review outcome, and actionable explanations of rejected submissions.
- [ ] **CUR-129** `P1` Test interrupted sessions, temporary offline states, and retry/resume so annotations are not silently lost or duplicated.
- [ ] **CUR-130** `P1` Make annotation and adjudication histories reviewable by authorized staff with appropriate privacy protections.
- [ ] **CUR-131** `P1` Provide accessible interfaces for searching records by status, label class, source, and audit issue as permitted.
- [ ] **CUR-132** `P1` Verify production labeling UI matches the approved taxonomy, guideline version, API schema, and data-access policy.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#06_ai_data_curation_and_labeling), not prerequisites or evidence of PASS.

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
