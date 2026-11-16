# Authorship, AI assistance and validation

**Public disclosure (2026-11-15).** This library is a **maintainer-curated collection of review prompts**, not a vendor-neutral certification, audited security baseline, or a set of requirements independently examined one by one. The repository contains checklists based on cited public references, editorial integration, and maintenance changes. **AI-assisted drafting and transformations have been used for portions of the 2026-11-15 changes** (including generated priority suggestions, documentation and helper code) under maintainer direction. The repository **does not possess a complete, per-ID historical ledger** of whether each of the 4,215 checks was written by a human, proposed by a model, externally sourced or independently reviewed. Accordingly, no global claim of full human expert validation is made.

## What has and has not been validated

- **Mechanically verifiable:** Local scripts check numbered file counts, IDs, unchecked source templates, formatting, local links and metadata. The two legacy source-lint and website workflows remain disabled. New curation CI checks template parity, source integrity and Awesome list conventions; CI does not replace expert review. Passing them does not establish security, legal or AI correctness.
- **Curated versus provisional:** The 50-item starter has individually curated context-sensitive P0/P1/P2 labels. The other 4,165 tiers are **provisional, deterministic text-based suggestions**, not manually adjudicated risk severity.
- **Sources and examples:** Linked references document the origin of *topics* and related technical guidance; a citation is **not** confirmation that every sentence was verbatim derived, fully covered or independently verified. The [standards starter mapping](lists/references/control-crosswalk.md) has confirmed external identifiers but **proposed partial alignments**; the [source-coverage ledger](lists/references/source-coverage-audit.md) and [AI source watch](lists/references/ai-source-watch.md) have stated scope limitations.
- **Human assessment:** The project owner/reviewer must test each applicable check on an actual target, record evidence, decide applicability and exceptions, and authorize release. There is no claim that these project reviews, external user trials or independent professional certifications have occurred for the entire library.
- **Direct commits:** Maintainers may commit to `main` without a PR; record local validation evidence and the commit SHA. Automated tests do not imply human peer review.

## Procedure for future additions and substantive edits

1. **Record origin.** For each proposed addition or major rewrite, note the source (original project evidence, standard and edition, public URL, maintainer knowledge, or AI-assisted suggestion), publication/review dates and any third-party licensing limits. Do not copy protected normative text wholesale.
2. **Validate independently.** A competent human reviewer should compare the candidate wording against the actual authoritative publication, supported technology and threat model. For live standards, verify the exact version and external ID; for legal duties, enlist a qualified jurisdiction-specific reviewer. If this has not happened, mark validation status **unreviewed** rather than implying approval.
3. **Make one outcome testable.** Each stable ID should have an observable pass condition and evidence example, not a list of unrelated tests. Use the [compound-check audit](skills/awesome-checklists/scripts/audit_compound_checks.py) to identify wording for editorial review; the audit's flags are only suggestions.
4. **Preserve identity and provenance.** Do not delete or repurpose IDs silently. Use [ID history](lists/references/id-history.md), [CHANGELOG.md](CHANGELOG.md) and the source metadata when checks move or split. Keep the Core 50 JSON text synchronized.
5. **Run tests before publishing.** Run local inventory lint, unit tests and scoped-review generator tests (see [CONTRIBUTING.md](CONTRIBUTING.md)). The legacy disabled workflows do not run; the new curation workflow runs a subset of mechanical checks on PRs and main pushes. Record actual results; mechanical checks are not subject-matter validation.
6. **Disclose remaining uncertainty.** Review documentation should state exactly what was tested, what was only inspected, which controls were inherited from prior work, and which IDs remain unvalidated. Do not mark **UNKNOWN** as PASS. In audited contexts, a separate qualified independent review is necessary.

## Suggested human-review record

| Field | Example of acceptable entry |
| --- | --- |
| Checklist ID and revision | Current stable ID, Git commit |
| Drafting provenance | Maintainer-authored / public-source adaptation / AI-assisted candidate / **unknown** |
| Primary source | URL, standard/version, section, retrieval date or project-specific test |
| Human technical reviewer | Identified person/role and date, or **not reviewed** |
| Verification | Actual test and evidence, or **not tested** |
| Status | Draft / needs human review / source checked / validated for a specific use case |
| Limitations | Scope, exclusions, unresolved conflicts, jurisdictions or version conditions |

The absence of an entry does **not** imply the check has been reviewed. A project team's completed review is separate from the library maintainer's editorial check.
