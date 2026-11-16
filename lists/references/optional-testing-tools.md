# Optional testing tools — central index

These resources consolidate previously repeated tool and command examples from numbered checklists. **They are optional leads, not approval, certification, required scanners, or evidence that a check has passed.** A reviewer must choose tools applicable to the actual stack, verify provenance and versions, use appropriately isolated test environments, and save observed results under the relevant stable ID.

- [Shared scope — 13 file-specific tool collections](optional-testing-tools-shared.md)
- [Frontend scope — 19 file-specific tool collections](optional-testing-tools-frontend.md)
- [Backend scope — 33 file-specific tool collections](optional-testing-tools-backend.md)
- [AI scope — 20 file-specific tool collections](optional-testing-tools-ai.md)
- [Security — cross-scope scanners, restrictions and third-party agent cautions](security-testing-tools.md)
- [AI Agents — ID-specific adversarial scenarios and optional tools](agent-testing-tools.md)

The **85 generic blocks** were moved without modifying any checklist IDs or acceptance criteria. Each original file links directly to its own matching catalog heading. The remaining six numbered Security and Agent files already use separate, more focused testing references.

## Handling results

A command's exit status is not an audit decision. For each checklist ID, record test scope, asset/commit, environment, versioned configuration, test assertions, direct evidence, human reviewer, and PASS/FAIL/UNKNOWN/N/A decision. Do not execute downloaded tools or target-controlled code with production credentials or without authorization and OS-enforced isolation when necessary.

See the [shared review method](review-method.md), [authorship/validation disclosure](../../AUTHORSHIP.md) and [source freshness policy](source-freshness-policy.md). The original source reference citations remain in each numbered checklist, with its source-review date now at the end of the file.
