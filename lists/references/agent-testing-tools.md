# Optional AI Agent test scenarios and tools

This reference covers [AI agent controls](../AI/11_AI_Agents_and_Tool_Orchestration.md) and [backend API checks](../backend/17_AI_Agents_and_Tool_Orchestration.md). Third-party tools are **optional**, not prerequisites, vendor endorsements or audit evidence.

## Check-specific tests

| IDs | Evidence-focused test case | PASS condition |
| --- | --- | --- |
| `AGENT-020` | Inspect a versioned risk-acceptance record for an enabled autonomous workflow and reproduce cited staging scenarios or measurements | Each applicable harm, cost, latency, availability, and operator-burden criterion has a stated acceptance threshold or decision rule and linked evidence; an undocumented assessment is not PASS |
| `AGENT-092` | Give a prospective approver mock approval decisions involving model overconfidence, unverified explanations, and hidden tool side effects | A predeclared scoring threshold is met and recorded before approval privileges are granted; a training-attendance record alone is not PASS |
| `AGENT-042` | A low-privilege actor requests a high-privilege tool action via model response or untrusted content | Trusted enforcement layer denies the request; model refusal is not sufficient |
| `AGENT-046` | Execute permitted and denied synthetic tool actions; query audit records by correlation ID | Every required actor/action/target/policy/outcome field is present and protected content redacted; missing any requirement is not PASS |
| `AGENT-075` / `AGENT-100` | Change tool identity, run or argument digest after approval; replay through backend API | Runtime approval binding AND separate API validation reject forged or stale requests; share evidence but assess separate surfaces |
| `AGENT-102` | Simulate timeout and retry of an externally acting tool | Authoritative state demonstrates no unintended duplicate external side effect |
| `AGENT-083` | Deny a destructive queued tool action | No protected side effect executes without the requisite independent authorization |
| `AGENT-109` | Make a denied call containing synthetic credentials | Traces can be correlated without leaking credentials or protected payloads |
| `AGENT-090` | Trigger an emergency stop with queued children and an in-flight tool | Queued tasks stop; irreversible in-flight effects and compensation paths are documented and tested |

These are suggested verification designs, not completed tests or an assertion that the library itself has been independently validated. Define acceptable thresholds for the target system before testing. Record versioned direct evidence, environment, actor, expected and actual result, owner and exceptions per ID. The same artifact may support several controls, but a PASS requires a separately justified acceptance assertion for each. For `AGENT-046`, all mandatory schema fields and the redaction rule are part of **one record-schema outcome**.

## Tool-call validation matrix (AGENT-026/137–141)

The former multi-facet `AGENT-026` has been split into separate assertions. Run each negative fixture against the **server-side tool dispatcher**, not just model-output wording, and retain denial outcome and execution traces for the target revision. These are suggested tests, not completed test results.

| Stable ID | One negative fixture | Expected evidence for PASS |
| --- | --- | --- |
| `AGENT-026` | Name an unregistered or disabled tool | Dispatcher rejects the name without executing another tool |
| `AGENT-137` | Send a string where the trusted schema requires an integer | Invalid argument is rejected before invocation |
| `AGENT-138` | Omit a required field | Dispatch is rejected with no tool side effect |
| `AGENT-139` | Provide an out-of-range value or invalid enum | Constraint enforcement rejects the value |
| `AGENT-140` | Use an identifier with an invalid format or forbidden namespace | Trusted validation rejects the identifier; **access authorization is tested separately by AGENT-027** |
| `AGENT-141` | Supply a payload over the configured byte/structure limit | Oversized request is rejected before invoking the tool |

An existing tool integration may combine validation in one library call, but **each ID requires its own observed behavior**. Record N/A only when the tool has no corresponding argument surface and explain why. Malformed-model output alone is not evidence the server enforces the rule.
## Tool selection is not a control

Use the project's existing test harness first: backend integration tests, synthetic API calls, event fixtures and independent authorization mocks. [pytest](https://docs.pytest.org/en/stable/), [Vitest](https://vitest.dev/), [Jest](https://jestjs.io/), [LangGraph testing](https://docs.langchain.com/oss/python/langgraph/test), [promptfoo](https://www.promptfoo.dev/docs/intro/) and [OpenTelemetry](https://opentelemetry.io/docs/) are potential aids **only where relevant and already compatible with the target stack**. Running `python -m pytest -q` or `npx vitest run` alone proves none of these checks without specific assertions and observed effects. Model output does not prove access-control enforcement.

Review external publishers, exact revisions, licenses, dependency permissions, network/secrets access, data retention and sandbox isolation before installing an agent skill or scanner. Do not give third-party tools production privileges by default. See [shared review method](review-method.md).

**Protocol compatibility:** [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/index) is the current stable spec as of 2026-11-15; clients/SDKs may still negotiate 2025-11-25. Record the **actual negotiated revision** when testing authentication, session semantics or tool discovery.
