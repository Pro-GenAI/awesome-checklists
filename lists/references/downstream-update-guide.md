# Keeping project reviews aligned with upstream checklist changes

A project review is evidence about **one project revision against one checklist-source revision**. Source templates stay unchecked. Neither copied Markdown nor a newer upstream export should silently overwrite prior PASS/FAIL/UNKNOWN/N/A decisions.

## Save a source snapshot when you start

Run from a checkout of awesome-checklists, and store these generated files in the project's review records:

    python3 skills/awesome-checklists/scripts/export_checklists.py --source-commit "$(git rev-parse HEAD)" --output checklist-baseline.json --review-template project-review.json

Record the reviewed **project SHA separately** from the checklist-source SHA. Keep evidence, reviewer identity, exceptions and sign-off alongside the project review. The template begins at UNKNOWN; a generated tier never establishes a PASS.

## Compare when you update the source

After checking out a newer upstream revision, export the same scope and compare:

    python3 skills/awesome-checklists/scripts/export_checklists.py --source-commit "$(git rev-parse HEAD)" --output checklist-current.json
    python3 skills/awesome-checklists/scripts/compare_checklist_exports.py --before checklist-baseline.json --after checklist-current.json --output checklist-delta.md
    python3 skills/awesome-checklists/scripts/compare_checklist_exports.py --before checklist-baseline.json --after checklist-current.json --format json --output checklist-delta.json --fail-on-review-needed

The last command returns **exit status 2** for an actionable change, **0** if no new review is needed, and **1** on malformed/incompatible input or I/O errors. A section-only move is reported but does not by itself invalidate evidence. Export scopes must match (all or the same individual scope). The comparison ignores line-number shifts but checks IDs, criterion text, priority, scope owner, source file and section.

## Reconcile without erasing history

- **New IDs:** assess applicability, assign an owner and obtain evidence; default to UNKNOWN.
- **Reworded or re-tiered IDs:** reassess against the current release. An earlier PASS does not automatically transfer; tiers are contextual triage, not externally audited severity.
- **Moved IDs:** check whether new scope ownership changes applicability or the evidence needed.
- **Removed IDs:** retain the historic result and source SHA, consult the [ID history](id-history.md) and [changelog](../../docs/CHANGELOG.md), and do not silently remap or reuse the ID.
- **Unchanged IDs:** preserve historical results; reconsider expiring evidence, environment changes and new threat models before a new release decision.

For a bounded first pass use [Core 50](core-50.md), a [25-check scope starter](minimum-viable-by-scope.md), or a [25–100-check profile](scoped-review-generator.md). A **full risk-based audit** may need many more checks, independent security verification, and applicable external requirements; there is no universal sufficient minimum.

**Limitations:** Save baseline JSON at review time. Older source revisions may require the exporter from that revision; a current exporter may fail against an older inventory. The diff tool does not validate the controls themselves, infer new legal obligations, execute tests, or authorize a release.
