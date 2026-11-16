# Contributing and maintaining checklists

The repository is **public**. Readers can clone, inspect and install its skill without GitHub credentials for public access, subject to GitHub rate limits.

**Review-first contribution policy:** Prefer pull requests for substantive changes and qualified review for risk-sensitive edits. The legacy source-lint and website-build workflows remain disabled. The new `quality-gates.yml` validates curated README conventions and lifecycle catalog integrity on pull requests; `link-health.yml` checks curated links on a weekly schedule. Also run and record appropriate local verification commands before merging. Authorized maintainers may commit directly to `main`, but a direct push is not independent peer validation. External contributions are welcome.

## Authorship and validation policy

Read [AUTHORSHIP.md](AUTHORSHIP.md) before adding or changing review criteria. Publicly disclose AI-assisted candidates and missing provenance where known; **do not** claim every checklist item was independently inspected or tested. Record the authoritative source (including standard version/exact clause, if appropriate), drafting/assistance origin, person/role and date of any *actual* human editorial review, and any outstanding gaps. If human or domain-expert validation is incomplete, state that explicitly.

A machine-generated priority tier or proposed framework mapping cannot certify compliance. The [control-level starter crosswalk](../lists/references/control-crosswalk.md) records confirmed *identifiers* but proposed partial mappings that need human scoping and evidence.

## Change rules

1. Choose the correct scope file, preserve each stable check ID and existing numbered filename, and write independently verifiable checks. New scope files take the next unused folder prefix; retired prefixes are not reused. See [ID history](../lists/references/id-history.md).
2. For new security checks, allocate an unused `SEC-` ID, update [security-id-registry.json](../lists/references/security-id-registry.json), and record the change in [CHANGELOG.md](CHANGELOG.md).
3. Add `P0`, `P1` or `P2` as a **contextual starting tier**, not a legal certification or permanent global severity. Core 50 priorities are curated; remaining labels are provisional.
4. Keep release gates, source references and evidence criteria current. Do not put credentials, customer data, live test results or third-party agent-skill installation instructions into numbered checklists.
5. For suspected compound checks, run the read-only `audit_compound_checks.py`. Split only when distinct outcomes need independent evidence; document ID succession and changes to meaning.
6. Update the relevant README, [optional framework crosswalk](../lists/references/compliance-crosswalk.md) and [AI framework watch](../lists/references/ai-source-watch.md) when the underlying source or regulatory scope materially changes.

## Agent domain maintenance and source currency

The AGENT domain is split across the AI and backend scope files. If changing an AGENT ID, its placement, or a required section/link, update [agent-domain-contract.json](../lists/references/agent-domain-contract.json) and [agent-domain-map.md](../lists/references/agent-domain-map.md) as appropriate. Do **not** insert a duplicate empty `API Checks` heading into the AI file. Verify all 141 IDs across both files, not sequentiality inside each file. Review the [control/test distinctions](../lists/references/overlap-review.md) and preserve IDs for different enforcement surfaces.

The stable MCP spec as of 2026-11-15 is [2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/index), but a specific SDK/server may still implement/negotiate an older release. Document the **actually implemented version** and the date of source review, rather than presenting dated references as timeless or assuming newer behavior applies to older runtimes.

## Source pinning and freshness

Review reports must record both the exact checklist-source SHA and the target project revision. A local unversioned directory is not immutable provenance. Follow the [source freshness policy](../lists/references/source-freshness-policy.md) and [generated inventory](../lists/references/inventory.json); changing a review date without evaluating relevant sources is not acceptable.

## Section and anchor integrity

Keep exactly one `## Release gate` and one `## Trusted references and scope` in every numbered source file; place the release gate first, followed by trusted references and a source-review date **as the last nonblank line**. Move any optional tool examples to the [central catalog index](../lists/references/optional-testing-tools.md), linking each checklist to its relevant scope-specific section; do not put external references or tool headings after the source date. When adding links such as `[API Checks](../lists/backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks)`, verify that the destination file and *heading anchor* exist. The offline repository linter now checks both. External link probes remain advisory because network and access restrictions can produce false failure signals.

## Local verification before submitting changes

From the repository root:

```bash
python3 skills/awesome-checklists/scripts/lint_repository.py
python3 skills/awesome-checklists/scripts/generate_inventory.py --check
python3 skills/awesome-checklists/scripts/generate_id_prefixes.py --check
python3 skills/awesome-checklists/scripts/check_source_freshness.py --max-age-days 180
python3 skills/awesome-checklists/scripts/validate_domain_structure.py
python3 skills/awesome-checklists/scripts/validate_release_metadata.py --verify-pin-ancestry  # full clone with fetched main
python3 -m unittest discover -s skills/awesome-checklists/tests -v
python3 skills/awesome-checklists/scripts/export_checklists.py --only-core --output /tmp/core-checklists.json
python3 skills/awesome-checklists/scripts/audit_compound_checks.py --output /tmp/compound-candidates.json
python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --size 50 --output /tmp/scoped-review.md
```

The historical [source lint](../.github/workflows/checklist-lint.yml.disabled) and [website build](../.github/workflows/website.yml.disabled) workflows remain disabled. New [curation quality gates](../.github/workflows/quality-gates.yml) and [curated-link health checks](../.github/workflows/link-health.yml) are active workflows; their results do not constitute independent expert review. Run the commands above locally and save the output; external-link audits require explicit local invocation. A passing local test is not certification, independent expert approval, or field validation.

**Website CI stays disabled** in `.github/workflows/website.yml.disabled`. Run `bash docs/website/build.sh` and `python docs/website/check_site.py` manually when changing published site behavior.

## Curated GenAI lifecycle entries and drop-in template changes

Prefer a small number of maintained, directly actionable entries over link volume. A proposed resource must explain **what production failure it prevents**, **when to use it**, its owner/source, and evidence that it is maintained. Exclude bare link dumps, self-promotion without implementation detail, duplicated generic web-dev lists, archived or abandoned sources, and unverifiable compliance claims. Use consistent category tags such as `[PR Template]`, `[Eval Benchmark]`, `[Security Audit]` or `[Runtime Guardrail]`.

The five [drop-in templates](../checklists/README.md) are shortlist views of stable IDs, not new canonical checklist IDs. Edit Markdown and [catalog.json](../checklists/catalog.json) together, keep review status UNKNOWN until evidence is provided, and run:

```bash
python3 scripts/validate_lifecycle_catalog.py
npx --yes awesome-lint docs/AWESOME.md
pre-commit run --all-files  # if pre-commit is installed
```

The Awesome linter checks the compact `AWESOME.md` curated index rather than applying single-list formatting rules to the extensive reference-library README. Its GitHub metadata rules also require the `awesome` and `awesome-list` repository topics, which must be added by a repository administrator. Code and repository automation remain MIT; the proposed CC0 text license requires maintainer rights review before merger.
