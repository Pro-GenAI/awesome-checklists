# Worked review example — awesome-checklists repository

This is an **actual but deliberately narrow source-inspection example**, not a product certification or completed release review. Evidence is tied to repository commit [`ab6718379ee114c57b58ba482883196b199e1d4d`](https://github.com/Pro-GenAI/awesome-checklists/commit/ab6718379ee114c57b58ba482883196b199e1d4d), inspected on **2026-11-15**. Some findings may change on later commits; the example intentionally retains the historical snapshot.

**Target:** the `awesome-checklists` repository's documentation, helper-test packaging and repository workflow configuration. **Reviewed:** root README, numbered testing/documentation checklists, listed tests, and the `.github/workflows/` directory. **Not reviewed:** the entire website runtime, all 91 checklists, deployed infrastructure, user data, or a test execution transcript. **Reviewer:** source-inspection example; **human sign-off:** not supplied. **Release decision:** pending.

| ID | Result | Direct evidence and assessment | Next action |
| --- | --- | --- | --- |
| [`DOC-002`](../07_Documentation_and_DeveloperExperience.md) | **PASS** (documentation-entry-point scope only) | The [README at the reviewed commit](https://github.com/Pro-GenAI/awesome-checklists/blob/ab6718379ee114c57b58ba482883196b199e1d4d/README.md) states the project purpose, scope, installation prerequisite and an issue link for help. This verifies the check's **documentation presence**, not whether a new reader successfully completes setup. | Recheck new-user comprehension separately under the relevant usability/onboarding controls. |
| [`TST-009`](../08_Testing.md) | **FAIL** (repository's code-helper release workflow) | [`.github/workflows/website.yml.disabled`](https://github.com/Pro-GenAI/awesome-checklists/blob/ab6718379ee114c57b58ba482883196b199e1d4d/.github/workflows/website.yml.disabled) is not an active GitHub Actions workflow, so the defined tests are not required to run on changes. This is an intentional repository choice, **not** an assertion that CI must be enabled. | Maintainer should document an equivalent manual test gate and retain evidence for release changes, or explicitly accept the residual risk. |
| [`TST-034`](../08_Testing.md) | **UNKNOWN** | The [unit-test source](https://github.com/Pro-GenAI/awesome-checklists/blob/ab6718379ee114c57b58ba482883196b199e1d4d/skills/awesome-checklists/tests/test_checklists.py) exists, but this source-inspection example has no independently verified test report or signed-off result tied to the reviewed release commit. Merely finding tests does not establish execution or passing results. | Run tests on the exact revision, record interpreter, environment, command, exit code, artifacts, and reviewer. |
| [`RAG-053`](../AI/10_RAG_and_Knowledge_Bases.md) | **N/A** | This review concerns a [Markdown checklist library](https://github.com/Pro-GenAI/awesome-checklists/blob/ab6718379ee114c57b58ba482883196b199e1d4d/README.md), not a deployed tenant-aware retrieval API. The RAG document-isolation criterion does not apply to the *reviewed repository functionality*. It **would** apply if reviewing a RAG product using these checklists. | Reevaluate applicability if a retrieval service is added to the reviewed system. |

These four statuses are **not a score**. A `PASS` requires direct, check-specific evidence; `FAIL` requires a demonstrated gap; `UNKNOWN` is not a pass; `N/A` requires a clear scope rationale. A different reviewer may find additional material findings in uninspected areas. No row self-approves a release.

## Recommended project record fields

Keep review records **outside** upstream checklist templates: `project`, `release_commit`, `review_date`, `reviewer`, `scope`, `checklist_id`, `result`, `evidence_urls`, `reproduction_or_test_command`, `environment`, `owner`, `remediation_due`, `exception_approver`, and `decision`. Never include passwords, production tokens or sensitive customer data in a public review record.

To create a machine-readable review skeleton for the curated starter set, run from the repository root:

```bash
python3 skills/awesome-checklists/scripts/export_checklists.py \
  --only-core --output core-catalog.json --review-template project-review.json \
  --source-commit "$(git rev-parse HEAD)"
```

The generated `project-review.json` has **all statuses UNKNOWN** until the actual project is evaluated. The starter selection is not sufficient for release approval on its own.
