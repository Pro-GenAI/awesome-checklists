# 13 — AI Model and Dataset Cards Checklist

> Verify that model and dataset documentation accurately communicates intended use, capabilities, limitations, provenance, evaluation evidence, risks, and change history. A card is a living disclosure and engineering record—not proof of regulatory compliance, model safety, lawful data rights, or benchmark reproducibility.

> **Scope: Backend / API-specific.** This file is one part of the 13_AI_Model_and_Dataset_Cards.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **CARDS-091** `P1` Associate every served model or dataset API identifier with the correct approved card revision and underlying artifact.
- [ ] **CARDS-092** `P1` Provide authorized clients a stable way to discover the current card or supported metadata endpoint where appropriate.
- [ ] **CARDS-093** `P1` Validate model-card and dataset-card metadata against the platform's relevant schema before publishing.
- [ ] **CARDS-094** `P1` Return actual model revision or deployment identifiers when needed for audit without disclosing protected internal details.
- [ ] **CARDS-095** `P1` Ensure card claims about available features, supported modalities, and usage restrictions match the live API contract.
- [ ] **CARDS-096** `P1` Test card/documentation links for inactive, retired, renamed, and replaced model or dataset versions.
- [ ] **CARDS-097** `P1` Enforce authentication and tenant permissions before serving restricted provenance, evaluation, or dataset details.
- [ ] **CARDS-098** `P1` Prevent public metadata endpoints from exposing proprietary prompts, secrets, private source records, or hidden evaluation labels.
- [ ] **CARDS-099** `P1` Check that model aliases and routing changes do not silently display an obsolete card for the newly deployed model.
- [ ] **CARDS-100** `P1` Version and test metadata response schemas for consumers of cards, dataset manifests, and lineage information.
- [ ] **CARDS-101** `P2` Publish machine-readable license and language fields accurately where the supported format provides them.
- [ ] **CARDS-102** `P1` Verify dataset record counts, split names, checksum metadata, and supported file types against approved exports.
- [ ] **CARDS-103** `P1` Separate evaluated model quality metrics from live-service availability and capability promises in API metadata.
- [ ] **CARDS-104** `P1` Check API caching, content negotiation, and invalidation when a card is revised or withdrawn.
- [ ] **CARDS-105** `P1` Ensure model or dataset deletion and access revocation affect card links, cached metadata, and downloadable artifacts as required.
- [ ] **CARDS-106** `P1` Log safe card revision and publication events with authorized actor and traceable artifact IDs.
- [ ] **CARDS-107** `P1` Test API behavior when card references, license metadata, or required provenance are missing or invalid.
- [ ] **CARDS-108** `P1` Validate outbound references to external model or dataset publishers rather than trusting unverified caller-supplied URLs.
- [ ] **CARDS-109** `P2` Include documentation consistency checks in CI or a controlled release workflow for material model and dataset changes.
- [ ] **CARDS-110** `P1` Confirm the production release includes approved card links or equivalent information for affected API consumers.

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

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#13_ai_model_and_dataset_cards), not prerequisites or verification evidence.

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
