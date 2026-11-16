# Scoped review generator — 25 to 100 checks

The library has **4,215 unique stable IDs** but only a project-specific subset is appropriate for most first reviews. Use the offline [generate_review.py](../../skills/awesome-checklists/scripts/generate_review.py) to produce a review **in Markdown or JSON**, without copying the upstream checklists or requiring external APIs.

## Start here

From the repository root, with **Python 3.10+** (no third-party packages):

| Use case | Command |
| --- | --- |
| First-launch starter, 50 checks | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --size 50 --project "My app" --output review.md` |
| Internal tool, 25 checks | `python3 skills/awesome-checklists/scripts/generate_review.py --profile internal-tool --size 25 --output internal-review.md` |
| Regulated use case, 100 candidates | `python3 skills/awesome-checklists/scripts/generate_review.py --profile regulated --size 100 --output regulated-review.md` |
| AI/agent project only, 50 checks | `python3 skills/awesome-checklists/scripts/generate_review.py --scope AI --size 50 --output ai-review.md` |
| All four scopes, explicitly | `python3 skills/awesome-checklists/scripts/generate_review.py --scope shared --scope frontend --scope backend --scope AI --size 100 --output fullstack-ai.md` |
| Security-only, 25 checks | `python3 skills/awesome-checklists/scripts/generate_review.py --domain SEC --size 25 --output security-review.md` |
| JSON status template | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --size 50 --format json --output review.json` |
| Ensure a specific check | `python3 skills/awesome-checklists/scripts/generate_review.py --include-id SEC-111 --exclude-id SEC-007 --output review.md` |

**Selection safety:** The generator uses manually curated Core 50 tiers and profile-specific domain/keyword selection. It deliberately **does not score provisional P0/P1/P2 labels** as severity: those labels are heuristic and require a reviewer to set project risk. Profile keywords also express editorial defaults, not proven release readiness.

**The commands above are examples, not a prescribed minimum profile.** The default source scopes for each profile are shared/frontend/backend. **AI is intentionally opt-in** because non-AI projects should not automatically receive AI-specific checks. Use `--scope AI` or repeat `--scope` for all desired scopes; explicit scopes replace defaults. `--domain` filters by stable ID prefix, not filename. Only IDs already in the library can be forced in or excluded. If a restricted scope has fewer than the requested count, the script errors rather than silently substituting unrelated checks.

## Four smaller first-pass scope profiles

For an initial narrow review, generate a **25-check shortlist for each relevant scope** (shared, frontend, backend or AI) with the commands and limitations in [minimum-viable-by-scope.md](minimum-viable-by-scope.md). If reviewing an AI agent, see the [136-ID domain map](agent-domain-map.md): the backend API slice contains only 22 AGENT controls and is not padded to satisfy a 25-item count. The full scope and domain release gates must still be assessed where applicable.

## How checks are selected

Selection is deterministic and documented in the Python script. Each profile first includes a short, explicit set of existing ID anchors (when applicable), then scores candidates using **only curated Core 50 priority tiers** plus domain and keyword weights. Provisional `P0/P1/P2` labels remain visible in the output but contribute **zero points** to ranking. Weighted scope balancing prevents larger domains from monopolizing the shortlist. **This is a heuristic candidate selection, not a validated risk or compliance ranking.** A qualified reviewer must tailor the scope and reassess project-specific priority using real risks and evidence.

The output contains the actual source path, stable ID, criterion text, tier/basis, review owner and evidence fields (JSON), or an editable review table (Markdown). **All items begin `UNKNOWN`**, have no evidence and cannot be marked `PASS` without independent verification. Results contain a decision/exception register, reference to the source commit when validated, and a reminder to include other applicable release gates. The original source Markdown files are never modified.

## Pinning provenance

The generator now **automatically derives the full 40-character source SHA from a clean local Git checkout**, and uses that immutable revision in Markdown and JSON outputs. It refuses unversioned or modified tracked source trees. You may pass `--source-commit` to enforce an exact expected checkout SHA; it must match HEAD:

```bash
SHA=$(git rev-parse HEAD)
python3 skills/awesome-checklists/scripts/generate_review.py --source-commit "$SHA" --size 50 --output review.md
```

The helper rejects an unversioned or dirty tracked checkout, and any supplied SHA that differs from local HEAD, rather than claiming unverified content was a particular Git revision.

## Review procedure

1. Choose the relevant profile and explicit scopes. Exclude inapplicable surfaces rather than declaring them passed. Never assume this bounded selection satisfies regulatory standards.
2. Record exact project artifact and environment. For each ID, assign a reviewer, actual project severity, acceptance test and linked evidence.
3. Replace `UNKNOWN` with `PASS`, `FAIL` or `N/A` only after applicable evidence or a reasoned applicability determination. Document exceptions, owners and deadlines separately.
4. Add any missing architectural, jurisdictional or high-impact checks. See the [shared method](review-method.md) and [optional external control crosswalk](control-crosswalk.md). A standards mapping does not establish compliance.
5. A named authorized human records the release decision. A generated Markdown/JSON file is **never** a signed approval, security audit, AI safety guarantee or legal certification.

For a broader unfiltered catalog, use [export_checklists.py](../../skills/awesome-checklists/scripts/export_checklists.py); for the manually curated 50, see [Core 50](core-50.md).
