# Optional testing tools — shared checklists

**Editorial relocation: 2026-11-15.** These optional testing-tool examples were formerly appended after source-review dates in shared numbered checklists. They are leads, **not** verified scanner recommendations, security guarantees, required tooling, permissions to run target-controlled code, or evidence that any control passed. Select the tool, version, test fixture and sandbox based on the actual project and the per-file **Test focus**. See the [shared review method](review-method.md).

## 01_Requirements_and_Planning

Source: [lists/01_Requirements_and_Planning.md](../01_Requirements_and_Planning.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** acceptance criteria, negative scenarios, and scope changes; include shared/cross-team controls where applicable.
- **Cross-stack:** [Cucumber](https://cucumber.io/docs/guides/overview/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest-bdd](https://pytest-bdd.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Cucumber.js](https://github.com/cucumber/cucumber-js) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 02_LegalIssues

Source: [lists/02_LegalIssues.md](../02_LegalIssues.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** consent, retention, access, export, deletion, and policy-enforcement behavior (legal interpretation remains manual); include shared/cross-team controls where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Optional prelaunch issue-spotting tool:** [Stef Builds Scan](https://stefbuilds.com/scan); supporting user-supplied [Instagram reel](https://www.instagram.com/reels/DfnqAxaMdjG/). The tool and reel were submitted as **legal-risk prevention sources**, but their content could not be extracted; evaluate actual functionality before relying on any result. Map concrete findings to existing `LEG-004/011/013/014/018/021/074` and relevant `SEC`/`LAUNCH` IDs, as applicable.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 03_Architecture_and_CodeQuality

Source: [lists/03_Architecture_and_CodeQuality.md](../03_Architecture_and_CodeQuality.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** dependency boundaries, code quality, interface contracts, and architectural regression; include shared/cross-team controls where applicable.
- **Cross-stack:** [Semgrep](https://semgrep.dev/docs/) + [dependency-cruiser](https://github.com/sverweij/dependency-cruiser).
- **Python:** [Ruff](https://docs.astral.sh/ruff/) + [mypy](https://mypy.readthedocs.io/en/stable/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeScript tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html) + [ESLint](https://eslint.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [ESLint](https://eslint.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 04_Internationalization_and_Localization

Source: [lists/04_Internationalization_and_Localization.md](../04_Internationalization_and_Localization.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** plural rules, locale formatting, missing strings, RTL, and long-text layouts; include shared/cross-team controls where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/).
- **Python:** [Babel](https://babel.pocoo.org/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [FormatJS](https://formatjs.github.io/docs/getting-started/installation) + [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [i18next](https://www.i18next.com/) + [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 06_Cost_and_FinOps

Source: [lists/06_Cost_and_FinOps.md](../06_Cost_and_FinOps.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** usage tagging, budget alerts, cost estimates, and anomaly scenarios; include shared/cross-team controls where applicable.
- **Cross-stack:** [Infracost](https://www.infracost.io/docs/).
- **Python:** [Cloud Custodian](https://cloudcustodian.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 07_Documentation_and_DeveloperExperience

Source: [lists/07_Documentation_and_DeveloperExperience.md](../07_Documentation_and_DeveloperExperience.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** links, snippets, onboarding setup, and API documentation examples; include shared/cross-team controls where applicable.
- **Cross-stack:** [lychee](https://github.com/lycheeverse/lychee) + [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2).
- **Python:** [doctest](https://docs.python.org/3/library/doctest.html) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [TypeDoc](https://typedoc.org/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [JSDoc](https://jsdoc.app/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **README-specific verification:** [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) and [lychee](https://github.com/lycheeverse/lychee) can check formatting and links; also perform an independently observed clean-environment first-use walkthrough, which tools alone cannot validate.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 08_Testing

Source: [lists/08_Testing.md](../08_Testing.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** unit/integration, API contract, end-to-end, and regression test runs; include shared/cross-team controls where applicable.
- **Cross-stack:** [Playwright](https://playwright.dev/) + [Pact](https://docs.pact.io/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/) + [coverage.py](https://coverage.readthedocs.io/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Vitest](https://vitest.dev/) + [Playwright](https://playwright.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Jest](https://jestjs.io/) + [Playwright](https://playwright.dev/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 09_Performance_and_Scalability

Source: [lists/09_Performance_and_Scalability.md](../09_Performance_and_Scalability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** throughput, latency percentiles, browser responsiveness, and resource budgets; include shared/cross-team controls where applicable.
- **Cross-stack:** [k6](https://grafana.com/docs/k6/latest/) + [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).
- **Python:** [Locust](https://docs.locust.io/) + [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [autocannon](https://github.com/mcollina/autocannon) + [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 10_Reliability_and_DisasterRecovery

Source: [lists/10_Reliability_and_DisasterRecovery.md](../10_Reliability_and_DisasterRecovery.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** network/service failure injection, retries, restore, and recovery objectives; include shared/cross-team controls where applicable.
- **Cross-stack:** [Toxiproxy](https://github.com/Shopify/toxiproxy) + [k6](https://grafana.com/docs/k6/latest/).
- **Python:** [testcontainers-python](https://testcontainers-python.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 11_DevOps_and_CI_CD

Source: [lists/11_DevOps_and_CI_CD.md](../11_DevOps_and_CI_CD.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** pipeline definitions, IaC policy, build artifacts, and deploy smoke checks; include shared/cross-team controls where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Checkov](https://www.checkov.io/) + [Trivy](https://trivy.dev/latest/).
- **Python:** [pytest-testinfra](https://testinfra.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Testcontainers](https://testcontainers.com/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Testcontainers](https://testcontainers.com/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 12_Monitoring_and_Observability

Source: [lists/12_Monitoring_and_Observability.md](../12_Monitoring_and_Observability.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** trace propagation, metrics/logs, alert conditions, and SLO visibility; include shared/cross-team controls where applicable.
- **Cross-stack:** [Prometheus promtool](https://prometheus.io/docs/prometheus/latest/command-line/promtool/) + [OpenTelemetry](https://opentelemetry.io/docs/).
- **Python:** [OpenTelemetry](https://opentelemetry.io/docs/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [OpenTelemetry](https://opentelemetry.io/docs/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 13_Analytics_and_ProductMetrics

Source: [lists/13_Analytics_and_ProductMetrics.md](../13_Analytics_and_ProductMetrics.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** event naming, consent, schemas, experiments, and reporting integrity; include shared/cross-team controls where applicable.
- **Cross-stack:** [GA4 DebugView](https://support.google.com/analytics/answer/7201382).
- **Python:** [Pandera](https://pandera.readthedocs.io/) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Zod](https://zod.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Ajv](https://ajv.js.org/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

---

## 14_Release_and_LaunchReadiness

Source: [lists/14_Release_and_LaunchReadiness.md](../14_Release_and_LaunchReadiness.md)

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** release smoke suites, security gates, rollback, and post-deploy verification; include shared/cross-team controls where applicable.
- **Cross-stack:** [actionlint](https://github.com/rhysd/actionlint) + [Trivy](https://trivy.dev/latest/) + [Playwright](https://playwright.dev/).
- **Python:** [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [Playwright](https://playwright.dev/) + [Vitest](https://vitest.dev/); for Vitest-based suites, run `npx vitest run` (or `npx playwright test` for E2E).
- **JavaScript:** [Playwright](https://playwright.dev/) + [Jest](https://jestjs.io/); for Jest-based suites, run `npx jest --ci` (or `npx playwright test` for E2E).
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.
