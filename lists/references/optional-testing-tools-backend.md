# Optional testing tools — backend checklists

**Editorial relocation: 2026-11-15.** These examples were previously appended after source-review dates in numbered backend checklists and are collected here for per-file discovery. None is a mandatory scanner, endorsed installation, proof of compliance, or approval to exercise third-party systems. Choose tools against the deployed stack and *Test focus*, pin versions, and retain actual authorized tests and evidence for the stable IDs. Use isolated non-production fixtures and respect data/secrets access. Backend Security and AI Agent tooling have separate [security](security-testing-tools.md) and [agent](agent-testing-tools.md) guides; also see the [shared review method](review-method.md).

## 01_Requirements_and_Planning

Source: [lists/backend/01_Requirements_and_Planning.md](../backend/01_Requirements_and_Planning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** acceptance criteria, negative scenarios, and scope changes; include API and service behavior where applicable.
- **Cross-stack:** [Cucumber](https://cucumber.io/docs/guides/overview/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest-bdd](https://pytest-bdd.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 02_LegalIssues

Source: [lists/backend/02_LegalIssues.md](../backend/02_LegalIssues.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** consent, retention, access, export, deletion, and policy-enforcement behavior (legal interpretation remains manual); include API and service behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 03_Architecture_and_CodeQuality

Source: [lists/backend/03_Architecture_and_CodeQuality.md](../backend/03_Architecture_and_CodeQuality.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** dependency boundaries, code quality, interface contracts, and architectural regression; include API and service behavior where applicable.
- **Cross-stack:** [Semgrep](https://semgrep.dev/docs/) + [dependency-cruiser](https://github.com/sverweij/dependency-cruiser).
- **Python:** [Ruff](https://docs.astral.sh/ruff/) + [mypy](https://mypy.readthedocs.io/en/stable/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeScript tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html) + [ESLint](https://eslint.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [ESLint](https://eslint.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 04_UI_UX_and_Usability

Source: [lists/backend/04_UI_UX_and_Usability.md](../backend/04_UI_UX_and_Usability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** navigation, responsive layouts, form errors, visual states, and user flows; include API and service behavior where applicable.
- **Cross-stack:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) + [Storybook](https://storybook.js.org/).
- **Python:** [Playwright](https://playwright.dev/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Storybook](https://storybook.js.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Storybook](https://storybook.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 05_Accessibility

Source: [lists/backend/05_Accessibility.md](../backend/05_Accessibility.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** keyboard navigation, focus order, accessible names, contrast, and assistive-tech flows; include API and service behavior where applicable.
- **Cross-stack:** [axe DevTools](https://www.deque.com/axe/devtools/) + [WAVE](https://wave.webaim.org/).
- **Python:** [Playwright](https://playwright.dev/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 06_Internationalization_and_Localization

Source: [lists/backend/06_Internationalization_and_Localization.md](../backend/06_Internationalization_and_Localization.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** plural rules, locale formatting, missing strings, RTL, and long-text layouts; include API and service behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/).
- **Python:** [Babel](https://babel.pocoo.org/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [FormatJS](https://formatjs.github.io/docs/getting-started/installation) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [i18next](https://www.i18next.com/) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 07_API_Design_and_Integrations

Source: [lists/backend/07_API_Design_and_Integrations.md](../backend/07_API_Design_and_Integrations.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** API schemas, auth, errors, compatibility, and dependency failures; include API and service behavior where applicable.
- **Cross-stack:** [Redocly CLI](https://redocly.com/docs/cli/) + [Pact](https://docs.pact.io/).
- **Python:** [Schemathesis](https://schemathesis.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Supertest](https://github.com/ladjs/supertest) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Dredd](https://dredd.org/en/latest/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Submission workflow tests:** Run [Playwright](https://playwright.dev/) or equivalent browser tests for submit/redirect/refresh/back behavior and verify authoritative mutation counts and idempotency.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 08_Data_and_DatabaseManagement

Source: [lists/backend/08_Data_and_DatabaseManagement.md](../backend/08_Data_and_DatabaseManagement.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** migrations, constraints, permissions, data integrity, rollback, and concurrent writes; include API and service behavior where applicable.
- **Cross-stack:** [pgTAP](https://pgtap.org/) + [Testcontainers](https://testcontainers.com/).
- **Python:** [testcontainers-python](https://testcontainers-python.readthedocs.io/) + [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 10_AI_Evaluation_and_Governance

Source: [lists/backend/10_AI_Evaluation_and_Governance.md](../backend/10_AI_Evaluation_and_Governance.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** AI policy thresholds, task/safety slices, escalation, and traceable evaluations; include API and service behavior where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 11_AI_Model_Selection_and_Benchmarking

Source: [lists/backend/11_AI_Model_Selection_and_Benchmarking.md](../backend/11_AI_Model_Selection_and_Benchmarking.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** candidate models with identical datasets, metrics, latency, and safety thresholds; include API and service behavior where applicable.
- **Cross-stack:** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) + [MLPerf](https://mlcommons.org/benchmarks/inference/).
- **Python:** [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/index) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 12_AI_Data_Curation_and_Labeling

Source: [lists/backend/12_AI_Data_Curation_and_Labeling.md](../backend/12_AI_Data_Curation_and_Labeling.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** data lineage, nulls, duplicates, labeling agreement, PII, and train/test leakage; include API and service behavior where applicable.
- **Cross-stack:** [Great Expectations](https://docs.greatexpectations.io/) + [DVC](https://dvc.org/doc).
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 13_AI_Model_and_Dataset_Cards

Source: [lists/backend/13_AI_Model_and_Dataset_Cards.md](../backend/13_AI_Model_and_Dataset_Cards.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** required metadata, model/dataset versions, limitations, and documentation links; include API and service behavior where applicable.
- **Cross-stack:** [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) + [lychee](https://github.com/lycheeverse/lychee).
- **Python:** [check-jsonschema](https://check-jsonschema.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Ajv](https://ajv.js.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 14_AI_FineTuning_and_Training

Source: [lists/backend/14_AI_FineTuning_and_Training.md](../backend/14_AI_FineTuning_and_Training.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** reproducible runs, training splits, checkpoints, and post-training quality; include API and service behavior where applicable.
- **Cross-stack:** [MLflow](https://mlflow.org/docs/latest/) + [DVC](https://dvc.org/doc).
- **Python:** [Transformers Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 15_Prompt_Engineering_and_Versioning

Source: [lists/backend/15_Prompt_Engineering_and_Versioning.md](../backend/15_Prompt_Engineering_and_Versioning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** prompt versions, formatting, instructions, refusals, and injection resistance; include API and service behavior where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 16_RAG_and_Knowledge_Bases

Source: [lists/backend/16_RAG_and_Knowledge_Bases.md](../backend/16_RAG_and_Knowledge_Bases.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** retrieval relevance, groundedness, citations, freshness, and document access; include API and service behavior where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [Ragas](https://docs.ragas.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 18_AI_Inference_and_Serving

Source: [lists/backend/18_AI_Inference_and_Serving.md](../backend/18_AI_Inference_and_Serving.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** concurrency, latency, streaming, load, failover, and response contracts; include API and service behavior where applicable.
- **Cross-stack:** [k6](https://grafana.com/docs/k6/latest/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [Locust](https://docs.locust.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [autocannon](https://github.com/mcollina/autocannon) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Artillery](https://www.artillery.io/docs) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 19_Multimodal_AI_Quality

Source: [lists/backend/19_Multimodal_AI_Quality.md](../backend/19_Multimodal_AI_Quality.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** image/audio/video fixtures, timing, captioning, invalid media, and accessibility; include API and service behavior where applicable.
- **Cross-stack:** [FFmpeg](https://ffmpeg.org/) + [Playwright](https://playwright.dev/).
- **Python:** [Pillow](https://pillow.readthedocs.io/) + [librosa](https://librosa.org/doc/latest/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 20_AI_Human_Review_and_Escalation

Source: [lists/backend/20_AI_Human_Review_and_Escalation.md](../backend/20_AI_Human_Review_and_Escalation.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** review queues, approval boundaries, appeals, escalations, and audit trails; include API and service behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 21_AI_Evaluation_and_Regression

Source: [lists/backend/21_AI_Evaluation_and_Regression.md](../backend/21_AI_Evaluation_and_Regression.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** held-out cases, severe failures, judge calibration, and CI quality thresholds; include API and service behavior where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [Ragas](https://docs.ragas.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 22_AI_Red_Teaming_and_Guardrails

Source: [lists/backend/22_AI_Red_Teaming_and_Guardrails.md](../backend/22_AI_Red_Teaming_and_Guardrails.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** injection, jailbreak, exfiltration, unsafe tools, and guardrail bypass; include API and service behavior where applicable.
- **Cross-stack:** [garak](https://github.com/NVIDIA/garak) + [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [garak](https://github.com/NVIDIA/garak) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 23_MLOps_and_Model_Lifecycle

Source: [lists/backend/23_MLOps_and_Model_Lifecycle.md](../backend/23_MLOps_and_Model_Lifecycle.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** lineage, promotion gates, artifacts, deployment, and rollback; include API and service behavior where applicable.
- **Cross-stack:** [DVC](https://dvc.org/doc) + [MLflow](https://mlflow.org/docs/latest/).
- **Python:** [Evidently](https://docs.evidentlyai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 24_AI_Monitoring_and_Drift

Source: [lists/backend/24_AI_Monitoring_and_Drift.md](../backend/24_AI_Monitoring_and_Drift.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** drift thresholds, sampling, alert routing, and inference telemetry; include API and service behavior where applicable.
- **Cross-stack:** [Prometheus promtool](https://prometheus.io/docs/prometheus/latest/command-line/promtool/) + [Grafana](https://grafana.com/docs/grafana/latest/).
- **Python:** [Evidently](https://docs.evidentlyai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 25_Documentation_and_DeveloperExperience

Source: [lists/backend/25_Documentation_and_DeveloperExperience.md](../backend/25_Documentation_and_DeveloperExperience.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** links, snippets, onboarding setup, and API documentation examples; include API and service behavior where applicable.
- **Cross-stack:** [lychee](https://github.com/lycheeverse/lychee) + [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2).
- **Python:** [doctest](https://docs.python.org/3/library/doctest.html) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeDoc](https://typedoc.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [JSDoc](https://jsdoc.app/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 26_Testing

Source: [lists/backend/26_Testing.md](../backend/26_Testing.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** unit/integration, API contract, end-to-end, and regression test runs; include API and service behavior where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Pact](https://docs.pact.io/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/) + [coverage.py](https://coverage.readthedocs.io/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/) + [Playwright](https://playwright.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/) + [Playwright](https://playwright.dev/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 27_Performance_and_Scalability

Source: [lists/backend/27_Performance_and_Scalability.md](../backend/27_Performance_and_Scalability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** throughput, latency percentiles, browser responsiveness, and resource budgets; include API and service behavior where applicable.
- **Cross-stack:** [k6](https://grafana.com/docs/k6/latest/) + [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).
- **Python:** [Locust](https://docs.locust.io/) + [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [autocannon](https://github.com/mcollina/autocannon) + [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 28_SEO

Source: [lists/backend/28_SEO.md](../backend/28_SEO.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** crawlability, robots/canonical, rendered metadata, and structured data; include API and service behavior where applicable.
- **Cross-stack:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) + [Rich Results Test](https://search.google.com/test/rich-results).
- **Python:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [schema-dts](https://github.com/google/schema-dts) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 29_GEO_and_AEO

Source: [lists/backend/29_GEO_and_AEO.md](../backend/29_GEO_and_AEO.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** machine-readable answers, structured data, citation links, and content consistency (not rankings); include API and service behavior where applicable.
- **Cross-stack:** [Schema.org Validator](https://validator.schema.org/) + [lychee](https://github.com/lycheeverse/lychee).
- **Python:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [schema-dts](https://github.com/google/schema-dts) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Optional owned-site AI-fetch diagnostic:** A case-insensitive log search for `OAI-SearchBot|ChatGPT-User|Claude-SearchBot|Claude-User|PerplexityBot|Perplexity-User` can identify **candidate** requests only. It mixes automated search crawlers with user-triggered fetchers, can match spoofed strings, misses unidentified traffic and says nothing by itself about citations. Where supported, cross-check provider-published IP lists/verified bot metadata and include edge-blocked requests, HTTP status codes, route grouping, time windows and log retention gaps. See **GEO-081** and general privacy-safe logging under **OBS-018/019**.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 30_DevOps_and_CI_CD

Source: [lists/backend/30_DevOps_and_CI_CD.md](../backend/30_DevOps_and_CI_CD.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** pipeline definitions, IaC policy, build artifacts, and deploy smoke checks; include API and service behavior where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Checkov](https://www.checkov.io/) + [Trivy](https://trivy.dev/latest/).
- **Python:** [pytest-testinfra](https://testinfra.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 31_Reliability_and_DisasterRecovery

Source: [lists/backend/31_Reliability_and_DisasterRecovery.md](../backend/31_Reliability_and_DisasterRecovery.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** network/service failure injection, retries, restore, and recovery objectives; include API and service behavior where applicable.
- **Cross-stack:** [Toxiproxy](https://github.com/Shopify/toxiproxy) + [k6](https://grafana.com/docs/k6/latest/).
- **Python:** [testcontainers-python](https://testcontainers-python.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 32_Monitoring_and_Observability

Source: [lists/backend/32_Monitoring_and_Observability.md](../backend/32_Monitoring_and_Observability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** trace propagation, metrics/logs, alert conditions, and SLO visibility; include API and service behavior where applicable.
- **Cross-stack:** [Prometheus promtool](https://prometheus.io/docs/prometheus/latest/command-line/promtool/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [OpenTelemetry](https://opentelemetry.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 33_Analytics_and_ProductMetrics

Source: [lists/backend/33_Analytics_and_ProductMetrics.md](../backend/33_Analytics_and_ProductMetrics.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** event naming, consent, schemas, experiments, and reporting integrity; include API and service behavior where applicable.
- **Cross-stack:** [GA4 DebugView](https://support.google.com/analytics/answer/7201382).
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 34_Cost_and_FinOps

Source: [lists/backend/34_Cost_and_FinOps.md](../backend/34_Cost_and_FinOps.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** usage tagging, budget alerts, cost estimates, and anomaly scenarios; include API and service behavior where applicable.
- **Cross-stack:** [Infracost](https://www.infracost.io/docs/).
- **Python:** [Cloud Custodian](https://cloudcustodian.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 35_Release_and_LaunchReadiness

Source: [lists/backend/35_Release_and_LaunchReadiness.md](../backend/35_Release_and_LaunchReadiness.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** release smoke suites, security gates, rollback, and post-deploy verification; include API and service behavior where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Trivy](https://trivy.dev/latest/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.
