# Licensing and reuse

<!-- SPDX-License-Identifier: CC0-1.0 -->

This repository intentionally uses **CC0 1.0 for original checklist and editorial material** and **MIT for original executable code and automation**. The goal is to make commercial and internal reuse straightforward without imposing a share-alike or noncommercial requirement. This guide explains scope; the actual license texts are [LICENSE](../LICENSE) and [LICENSE-CODE](../LICENSE-CODE).

**Rights qualification:** A license applies only to material for which Pro-GenAI or its contributors hold the necessary rights to grant it. The following path guide is **not** a claim that third-party excerpts, linked standards, protected marks, or all historical contributions have been cleared. If a file includes a separately credited or uncleared component, that component keeps its own rights.

## File-level scope

| Content or path | Intended license for original contributions | Notes |
| --- | --- | --- |
| `lists/**/*.md`, `lists/references/*.json` | **CC0-1.0** | Checklist criteria, editorial selections, original reference summaries and generated catalogs; external standards remain their owners' works. |
| `docs/**/*.md`, `docs/checklists/catalog.json` | **CC0-1.0** | Original written guidance, drop-in templates and editorial metadata, excluding separate third-party material. |
| `README.md`, `AGENTS.md`, `.github/pull_request_template.md` | **CC0-1.0** | Original explanatory and contributor guidance. |
| `skills/awesome-checklists/SKILL.md`, `skills/awesome-checklists/references/*.md` | **CC0-1.0** | Original human-/agent-readable instructions and documentation; executable scripts are MIT. |
| `scripts/*.py`, `skills/awesome-checklists/scripts/*.py`, `skills/awesome-checklists/tests/*.py` | **MIT** | Executable scripts, automation, and tests. |
| `docs/website/*.py`, `docs/website/build.sh`, `docs/website/assets/site.js`, `docs/website/assets/site.css` | **MIT** | Website code and styling. |
| `.github/workflows/*`, `.pre-commit-config.yaml`, other original build/automation configuration | **MIT** | Maintainer-authored automation/configuration; third-party actions and dependencies retain their terms. |
| `docs/website/assets/*.svg`, third-party marks, quoted excerpts, external links | **Not automatically covered** | Original branding and visual marks are not being placed under CC0 by this guide; inspect notices and obtain permission where necessary. Linking or showing a badge does not relicense it. |
| `LICENSE`, `LICENSE-CODE` | **License texts** | Interpret and retain their original terms. |

For mixed files, **the identified content or code component determines the applicable terms**, not the file extension alone. Independently attributed third-party material overrides any folder-wide summary. The documentation can include short example commands; substantial standalone executable source files follow MIT. When uncertain, ask via an issue before redistribution.

## SPDX identifiers

Where safe for the syntax, original executable files carry `SPDX-License-Identifier: MIT` in a comment, and selected original Markdown templates carry `SPDX-License-Identifier: CC0-1.0` in an HTML comment. A missing in-file tag does not replace the scope table or the actual license files. Do not add an SPDX claim to an imported file, an uncleared excerpt, or a brand asset without confirming rights.

## Reuse and attribution

- **Checklist text under CC0:** Use and adapt, including inside proprietary commercial products, without an attribution obligation under CC0. A waiver or fallback license applies only to the rights its grantor controls.
- **MIT software:** Use, modify and redistribute commercially, including in proprietary systems; include the MIT copyright and permission notice in copies or substantial portions of the software.
- **Credit is welcome, not required for CC0 content:** Consider `Uses [awesome-checklists](https://github.com/Pro-GenAI/awesome-checklists) by Pro-GenAI` with a link. This is distinct from the optional **Reviewed with awesome-checklists** badge, which should be displayed only after an actual documented review; neither indicates certification, approval, or endorsement.
- **No automatic rights to trademarks, patents, or third-party materials:** Do not imply partnership, approval, or that external standards are sublicensed by this project.

## Contribution and historical-rights checks

Contributors should consult [CONTRIBUTING.md](CONTRIBUTING.md) and disclose the origin, permissions and intended license of original or adapted material. Contributions are **not copyright assignments**: the contributor retains whatever copyright they hold while making an authorized contribution under the applicable repository license. If the rights are unclear, link to the upstream standard or paraphrase independently instead of importing restricted text.

Maintainers must not presume that a historical or third-party contribution becomes CC0 just because it appears in `lists/` or `docs/`. Before asserting or changing coverage, identify the author/source, the contributor's authority, the applicable terms, any required attribution, and the reviewed location. Keep the record in the issue/PR or a provenance note; seek permission, remove disputed content, or exclude it pending review. See [AUTHORSHIP.md](AUTHORSHIP.md) for the existing provenance limitations.

This guidance summarizes intended licensing for reuse and is not a substitute for the license texts or legal review of a specific third-party work.
