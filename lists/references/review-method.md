# Shared review method and priority rubric

This guide applies to **all 91 numbered checklists**. Source templates deliberately remain unchecked and are **not** evidence of project readiness, safety, legality, or certification. The checks guide a **risk-based, scoped review**, not a requirement to process the entire library.

## Getting a bounded project review

To avoid reviewing 4,215 items indiscriminately, use the [scoped review generator](scoped-review-generator.md) for 25–100 UNKNOWN-first candidates selected by startup, regulated or internal-tool profile, optional scope and ID filters. The selection does not prove minimum compliance or replace additional applicable release gates. For externally mapped references, consult the [verified-identifier, proposed-mapping crosswalk](control-crosswalk.md). See [authorship and validation disclosure](../../AUTHORSHIP.md) for limits on human and AI review claims.

The [four 25-check scope starters](minimum-viable-by-scope.md) are deliberately bounded and always begin UNKNOWN. To prevent copied project reviews drifting silently from upstream, save a pinned JSON source catalog and run the [downstream update comparison](downstream-update-guide.md) before transferring any earlier PASS to a new source revision. The [AGENT domain map](agent-domain-map.md) clarifies cross-file ID continuity; the [overlap review](overlap-review.md) distinguishes an independent control from an adversarial test or API-specific verification.

## Review record

In a project-specific record (not the upstream template), capture the project and release/build/commit; environment and affected users; architecture and applicable jurisdictions; reviewer and accountable approval owner; date; chosen checklists and excluded scopes; decisions and exceptions; evidence artifacts and their versions. A separate [evidence-linked worked example](example-review.md) demonstrates the distinction between verified, failed, unknown, and inapplicable items.

For every applicable check, record its **stable ID**, responsible owner, verification procedure, direct evidence (code/config reference, test report, trace, screenshot or approved document), test environment, observed outcome, severity, and remediation/retest or exception. Never paste secrets, private audit material or protected user data into public reports.

## Results and human decision

| Result | Required interpretation |
| --- | --- |
| `PASS` | The specific criterion was verified with direct, current evidence for the reviewed release and environment. |
| `FAIL` | Evidence demonstrates a relevant unmet criterion; track a remediation owner and deadline. |
| `UNKNOWN` | Not checked, insufficient evidence, ambiguous criterion, or inaccessible system; **not a pass**. |
| `N/A` | Explicit architecture/use-case/jurisdiction rationale shows the criterion does not apply; **not a pass**. |

Evaluate domain-wide release gates across **all relevant scope files**, not once per repeated gate. A reviewer never self-certifies a release. Authorized humans decide residual risk, exceptions and final release approval.

## Per-check starting tiers

The label beside each numbered checklist item is an **editable triage suggestion, not intrinsic severity**:

- **`P0` — critical candidate:** If applicable, a gap could warrant blocking or escalating release until mitigated or explicitly approved by accountable owners.
- **`P1` — recommended verification:** Common assurance requirement or material failure mode; assign an owner and review before a relevant release.
- **`P2` — contextual/optional review:** Supporting documentation, lifecycle or less immediately exploitable risk; escalate when the product's environment, user harm or regulation warrants it.

**Provenance:** The original [Core 50](core-50.md) had individually curated tier labels. The remaining checks were assigned provisional initial labels on **2026-11-15** using a deterministic text-based triage pass: explicit severe authority/data-exposure failure language tends toward P0, documentation/inventory wording tends toward P2, and the remainder defaults to P1. **These labels have not all received domain-expert/manual severity review.** A simple text rule cannot infer exploitability, legally required controls, threat likelihood, application risk, business impact, or whether a documentation control is essential. **Never assume a P2 control is safe to skip; never rely on tiers to satisfy a standard.** Always re-rate based on project risk and legal applicability.

Core 50 remains a suggested short first pass, **not a universal minimum**. Record actual project-specific severity separately from the source `P0/P1/P2` tier. A control can legitimately be an urgent blocker for a medical or payment product even when the source tier is P2.

## Meaning of "high-priority" in all release gates

Where a release gate says **high-priority**, the decision must follow a **documented project-specific** threat model, mandatory obligations, material findings and reviewer-assigned blockers. Curated Core 50 `P0`/`P1` tiers are review prompts; other priority labels are provisional text heuristics and do **not** automatically block or authorize release. Even a `P2` suggestion may represent a mandatory obligation. A materially exploitable issue or an `UNKNOWN` release-critical control requires evidence, mitigation, or a documented authorized and time-bound exception; do not mark UNKNOWN as PASS.

## Shared release sign-off

A domain's common sign-off requirements may be linked once across multiple scope files. The reviewer still needs evidence for **every applicable scope**, project-specific exceptions/owners, and a single documented approval decision. Do not delete differentiated domain-specific release criteria merely to reduce repeated wording. The Security scope files now link to the shared Security release gate.

## Use multiple scope slices without duplicating work

The domain IDs, not filename sequence numbers, are stable. For instance the `AGENT` domain includes general agent controls under `lists/AI/` and API-specific controls under `lists/backend/`. Select all relevant slices, reuse evidence between related but different controls when valid, and record distinct acceptance outcomes. Filename numbering only determines **within-folder recommended order** and stable IDs are not required to appear sequentially inside topical sections.

## Granularity and ID preservation

Prefer **one independently testable outcome per ID**. To surface possible remaining compound items across all scope files, run `python3 skills/awesome-checklists/scripts/audit_compound_checks.py --output compound-candidates.json` from the repository root. The output is **heuristic editorial backlog only** and does not itself justify splitting, renumbering, or claiming duplicate IDs. A check may include examples or conditions when these are necessary to define its single outcome, but do not mark an entire compound check `PASS` if any required facet is unverified. Record its status `FAIL` or `UNKNOWN` until required facets are independently verified. Split a compound control only after confirming independent acceptance evidence, assigning globally unused IDs, retaining old-ID meaning where feasible, mapping old-to-new IDs in the [changelog](../../CHANGELOG.md), and updating inventory counts and curated metadata.

## Third-party agents, frameworks, testing tools and references

The [central optional testing-tool index](optional-testing-tools.md) points to per-file Shared, Frontend, Backend and AI examples plus dedicated Security and Agent scenarios. Lists are **not prerequisites** or proof of test coverage; choose context-specific tests and independently examine actual evidence. The source review date belongs at the end of each numbered checklist's reference section, not before any optional vendor instructions.



Third-party links in source references or suggested testing tools are **leads**, not endorsements or permissions to execute. Before use, review the actual maintained revision, publisher and license, dependencies/supply chain, permissions, secrets exposure, network capabilities, sandbox prerequisites, data retention, platform compatibility, and permissions requested by the tool. Prefer minimal-privilege/offline tests. Do not grant a tool authority merely because it is popular or suggested in a checklist. The reusable checklists no longer repeat a vendor-specific AI-skill recommendation block.

## Compliance is an optional crosswalk

See the [framework crosswalk](compliance-crosswalk.md) and the [AI source-currency watch](ai-source-watch.md). It maps **topics** to potential external obligations for further analysis; it is not a substitute for actual legal requirements, ASVS control-level verification, a SOC 2 audit, or qualified professional review. Effective dates and jurisdictions are part of applicability.
