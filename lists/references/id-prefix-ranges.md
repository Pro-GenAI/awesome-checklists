# Stable ID prefix ranges and ownership

**Generated from source on 2026-11-15.** The [machine-readable prefix register](id-prefix-ranges.json) lists **35 prefixes, 4,215 distinct IDs**, their exact occupied numeric intervals, and every numbered checklist file that owns IDs under each prefix. It is generated from **all four scopes** and checked on every direct `main` push; this avoids treating apparent gaps inside one file as deleted controls.

For example:

| Prefix | Full observed range | Scope/ownership explanation |
| --- | --- | --- |
| `SEC` | `SEC-001`–`SEC-121` | 121 controls across shared, frontend, backend and AI Security; [history](id-history.md) and [live registry](security-id-registry.json) |
| `AGENT` | `AGENT-001`–`AGENT-141` | General/frontend controls in AI file, with `AGENT-095`–`AGENT-116` in backend [API Checks](../backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks); [cross-file contract](agent-domain-contract.json) |
| `A11Y` | `A11Y-001`–`A11Y-112` | 112 checks distributed across relevant scope files |
| `APID` | `APID-001`–`APID-120` | 120 API domain checks across relevant scopes |
| `TST` | `TST-001`–`TST-084` | 84 testing checks across relevant scopes |

All 35 prefixes are contiguous **across their combined owning files**. The source generator now **rejects missing numeric IDs and prefixes that do not begin at `-001`, even if someone tries to regenerate the JSON register**. Gaps inside a single file remain legitimate when another scope owns those IDs. Retirements require an explicitly reviewed retirement policy and history record before loosening this invariant; do not silently remove, renumber or reuse IDs. **Continuity is a structural fact, not proof of semantic completeness or independent expert review.**

Run from the repository root:

```bash
python3 skills/awesome-checklists/scripts/generate_id_prefixes.py --check
```

To intentionally change a prefix or move an ID, regenerate the JSON, update the appropriate ID history and CHANGELOG, and verify the source inventory. CI refuses unnoticed range/count/file-owner drift. The static [inventory manifest](inventory.json) separately checks totals by scope, and the [source freshness policy](source-freshness-policy.md) flags dated references.
