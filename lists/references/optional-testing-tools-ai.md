# Optional testing tools — AI checklists

**Editorial relocation: 2026-11-15.** These previously embedded tool suggestions are preserved for topical discoverability, but none is required, endorsed, independently security-validated, or proof of a successful review. Prefer existing target stack tests and human-verified evidence under the actual checklist IDs. Do not grant external agent skills or test frameworks production secrets or permission to execute target-controlled code without OS isolation. For agent-specific adversarial cases, see [agent-testing-tools.md](agent-testing-tools.md) and the [shared review method](review-method.md).

## 01_Requirements_and_Planning

Source: [lists/AI/01_Requirements_and_Planning.md](../AI/01_Requirements_and_Planning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** acceptance criteria, negative scenarios, and scope changes; include model and dataset behaviors where applicable.
- **Cross-stack:** [Cucumber](https://cucumber.io/docs/guides/overview/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest-bdd](https://pytest-bdd.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 02_LegalIssues

Source: [lists/AI/02_LegalIssues.md](../AI/02_LegalIssues.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** consent, retention, access, export, deletion, and policy-enforcement behavior (legal interpretation remains manual); include model and dataset behaviors where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 03_AI_Evaluation_and_Governance

Source: [lists/AI/03_AI_Evaluation_and_Governance.md](../AI/03_AI_Evaluation_and_Governance.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** AI policy thresholds, task/safety slices, escalation, and traceable evaluations; include model and dataset behaviors where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 05_AI_Model_Selection_and_Benchmarking

Source: [lists/AI/05_AI_Model_Selection_and_Benchmarking.md](../AI/05_AI_Model_Selection_and_Benchmarking.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** candidate models with identical datasets, metrics, latency, and safety thresholds; include model and dataset behaviors where applicable.
- **Cross-stack:** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) + [MLPerf](https://mlcommons.org/benchmarks/inference/).
- **Python:** [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/index) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 06_AI_Data_Curation_and_Labeling

Source: [lists/AI/06_AI_Data_Curation_and_Labeling.md](../AI/06_AI_Data_Curation_and_Labeling.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** data lineage, nulls, duplicates, labeling agreement, PII, and train/test leakage; include model and dataset behaviors where applicable.
- **Cross-stack:** [Great Expectations](https://docs.greatexpectations.io/) + [DVC](https://dvc.org/doc).
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 07_AI_Model_and_Dataset_Cards

Source: [lists/AI/07_AI_Model_and_Dataset_Cards.md](../AI/07_AI_Model_and_Dataset_Cards.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** required metadata, model/dataset versions, limitations, and documentation links; include model and dataset behaviors where applicable.
- **Cross-stack:** [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) + [lychee](https://github.com/lycheeverse/lychee).
- **Python:** [check-jsonschema](https://check-jsonschema.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Ajv](https://ajv.js.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 08_AI_FineTuning_and_Training

Source: [lists/AI/08_AI_FineTuning_and_Training.md](../AI/08_AI_FineTuning_and_Training.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** reproducible runs, training splits, checkpoints, and post-training quality; include model and dataset behaviors where applicable.
- **Cross-stack:** [MLflow](https://mlflow.org/docs/latest/) + [DVC](https://dvc.org/doc).
- **Python:** [Transformers Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 09_Prompt_Engineering_and_Versioning

Source: [lists/AI/09_Prompt_Engineering_and_Versioning.md](../AI/09_Prompt_Engineering_and_Versioning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** prompt versions, formatting, instructions, refusals, and injection resistance; include model and dataset behaviors where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 10_RAG_and_Knowledge_Bases

Source: [lists/AI/10_RAG_and_Knowledge_Bases.md](../AI/10_RAG_and_Knowledge_Bases.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** retrieval relevance, groundedness, citations, freshness, and document access; include model and dataset behaviors where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [Ragas](https://docs.ragas.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 12_AI_Inference_and_Serving

Source: [lists/AI/12_AI_Inference_and_Serving.md](../AI/12_AI_Inference_and_Serving.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** concurrency, latency, streaming, load, failover, and response contracts; include model and dataset behaviors where applicable.
- **Cross-stack:** [k6](https://grafana.com/docs/k6/latest/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [Locust](https://docs.locust.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [autocannon](https://github.com/mcollina/autocannon) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Artillery](https://www.artillery.io/docs) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 13_Multimodal_AI_Quality

Source: [lists/AI/13_Multimodal_AI_Quality.md](../AI/13_Multimodal_AI_Quality.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** image/audio/video fixtures, timing, captioning, invalid media, and accessibility; include model and dataset behaviors where applicable.
- **Cross-stack:** [FFmpeg](https://ffmpeg.org/) + [Playwright](https://playwright.dev/).
- **Python:** [Pillow](https://pillow.readthedocs.io/) + [librosa](https://librosa.org/doc/latest/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 14_AI_Human_Review_and_Escalation

Source: [lists/AI/14_AI_Human_Review_and_Escalation.md](../AI/14_AI_Human_Review_and_Escalation.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** review queues, approval boundaries, appeals, escalations, and audit trails; include model and dataset behaviors where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 15_AI_Evaluation_and_Regression

Source: [lists/AI/15_AI_Evaluation_and_Regression.md](../AI/15_AI_Evaluation_and_Regression.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** held-out cases, severe failures, judge calibration, and CI quality thresholds; include model and dataset behaviors where applicable.
- **Cross-stack:** [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [DeepEval](https://docs.confident-ai.com/) + [Ragas](https://docs.ragas.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 16_AI_Red_Teaming_and_Guardrails

Source: [lists/AI/16_AI_Red_Teaming_and_Guardrails.md](../AI/16_AI_Red_Teaming_and_Guardrails.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** injection, jailbreak, exfiltration, unsafe tools, and guardrail bypass; include model and dataset behaviors where applicable.
- **Cross-stack:** [garak](https://github.com/NVIDIA/garak) + [promptfoo](https://www.promptfoo.dev/docs/intro/).
- **Python:** [garak](https://github.com/NVIDIA/garak) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [promptfoo](https://www.promptfoo.dev/docs/intro/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 17_MLOps_and_Model_Lifecycle

Source: [lists/AI/17_MLOps_and_Model_Lifecycle.md](../AI/17_MLOps_and_Model_Lifecycle.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** lineage, promotion gates, artifacts, deployment, and rollback; include model and dataset behaviors where applicable.
- **Cross-stack:** [DVC](https://dvc.org/doc) + [MLflow](https://mlflow.org/docs/latest/).
- **Python:** [Evidently](https://docs.evidentlyai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 18_AI_Monitoring_and_Drift

Source: [lists/AI/18_AI_Monitoring_and_Drift.md](../AI/18_AI_Monitoring_and_Drift.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** drift thresholds, sampling, alert routing, and inference telemetry; include model and dataset behaviors where applicable.
- **Cross-stack:** [Prometheus promtool](https://prometheus.io/docs/prometheus/latest/command-line/promtool/) + [Grafana](https://grafana.com/docs/grafana/latest/).
- **Python:** [Evidently](https://docs.evidentlyai.com/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 19_Cost_and_FinOps

Source: [lists/AI/19_Cost_and_FinOps.md](../AI/19_Cost_and_FinOps.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** usage tagging, budget alerts, cost estimates, and anomaly scenarios; include model and dataset behaviors where applicable.
- **Cross-stack:** [Infracost](https://www.infracost.io/docs/).
- **Python:** [Cloud Custodian](https://cloudcustodian.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 20_Analytics_and_ProductMetrics

Source: [lists/AI/20_Analytics_and_ProductMetrics.md](../AI/20_Analytics_and_ProductMetrics.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** event naming, consent, schemas, experiments, and reporting integrity; include model and dataset behaviors where applicable.
- **Cross-stack:** [GA4 DebugView](https://support.google.com/analytics/answer/7201382).
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 21_GEO_and_AEO

Source: [lists/AI/21_GEO_and_AEO.md](../AI/21_GEO_and_AEO.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** machine-readable answers, structured data, citation links, and content consistency (not rankings); include model and dataset behaviors where applicable.
- **Cross-stack:** [Schema.org Validator](https://validator.schema.org/) + [lychee](https://github.com/lycheeverse/lychee).
- **Python:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [schema-dts](https://github.com/google/schema-dts) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 22_Release_and_LaunchReadiness

Source: [lists/AI/22_Release_and_LaunchReadiness.md](../AI/22_Release_and_LaunchReadiness.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** release smoke suites, security gates, rollback, and post-deploy verification; include model and dataset behaviors where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Trivy](https://trivy.dev/latest/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.
