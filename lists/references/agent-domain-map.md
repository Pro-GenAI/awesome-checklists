# AI Agent domain — verified ID and section map

**Checked against source:** 2026-11-15. The `AGENT` domain contains **141 unique contiguous IDs** across **two different scope files**, not one giant file. The 22 IDs between `AGENT-094` and `AGENT-117` are not deleted or unassigned.

| Owner file | Covered IDs | Required sections | Count |
| --- | --- | --- | ---: |
| [AI / Agents and Tool Orchestration](../AI/11_AI_Agents_and_Tool_Orchestration.md) | `AGENT-001`–`AGENT-094`, `AGENT-117`–`AGENT-136` (frontend), `AGENT-137`–`AGENT-141` (tool-input validation) | Goals/workflow, tools and permissions, handoffs, human approvals, **Frontend Checks** | 119 |
| [Backend / Agents and Tool Orchestration](../backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks) | `AGENT-095`–`AGENT-116` | **API Checks** | 22 |

`API Checks` is deliberately a backend-specific section. It would be confusing to insert a duplicate empty heading into the AI-specific file. The two files cross-link to the owning section instead.

## Automated maintenance contract

The authoritative [agent-domain-contract.json](agent-domain-contract.json) defines all ranges, owners, mandatory sections and cross-scope links. Run:

```bash
python3 skills/awesome-checklists/scripts/validate_domain_structure.py
```

This checks domain-wide contiguous IDs, exact owner ranges, no hidden duplicate AGENT IDs in other numbered checklists, required headings, target existence and local section anchors. Run it through the source linter locally; GitHub Actions is disabled and does not execute on pushes or pull requests. Failures indicate a structure/ownership error, **not a missing check in one file merely because its neighboring ID lives in another scope**.

## AGENT-026 split — independent evidence

**2026-11-15:** AGENT-026 now checks only trusted tool identity. AGENT-137 tests argument types; AGENT-138 required fields; AGENT-139 bounds/enum rules; AGENT-140 identifier format/namespace rules; AGENT-141 payload-size caps. [Tool-schema test matrix](agent-testing-tools.md#tool-call-validation-matrix-agent-026137141) documents independent accept/reject evidence. Any PASS under the former multi-facet AGENT-026 wording is historical and must be re-assessed. Authorization remains separately enforced under AGENT-027/042; identifier *format* validation is not proof of per-object access authorization.

## AGENT-043 atomicity clarification

`AGENT-043` now concerns operation-specific permissions only. Approval policy and actual human approval enforcement are already separately testable under `AGENT-073`, `AGENT-075`–`AGENT-078`, and `AGENT-083`; **no duplicate ID is needed**. Earlier results for the compound wording cannot be grandfathered as full PASS for these controls.

## Which check is a control, a verification test or a scoped counterpart?

Refer to [agent-control overlap and evidence map](overlap-review.md). `AGENT-075` specifies approval-binding enforcement; backend `AGENT-100` checks an additional API attack surface. The same trace can be linked by two independently justified assertions. For audit logging, `AGENT-046` is one **event-schema criterion**, not an arbitrary bundle of separately passed fields: missing any mandatory field or redaction requirement means no PASS. See [targeted agent test scenarios](agent-testing-tools.md).

## Review scope

Use `python3 skills/awesome-checklists/scripts/generate_review.py --scope AI --size 25 --output agent-ai-starter.md` for a bounded AI-scope starting set, or use `--scope backend --domain AGENT --size 25` only when enough eligible IDs exist (**currently 22 backend AGENT IDs, so a 25-check domain-only command must be rejected rather than fabricate controls**). For backend API agent-only review use the 22 existing controls directly; the generator's minimum is 25, which is why it must not silently pad a 22-check collection.

The map does not certify any system's runtime authorization, idempotency, MCP compliance or release readiness. Every actual product review begins UNKNOWN and requires evidence.
