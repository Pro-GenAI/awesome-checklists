# Source review freshness policy

**As of 2026-11-15:** Source-review metadata is tracked per numbered checklist as `**Source review date:** YYYY-MM-DD.` This is the date a maintainer last evaluated the listed sources; **it does not guarantee that every link is reachable, that standards still apply, or that each check has been independently validated**.

A source review older than **180 days** is flagged as stale. Check the version and status of material primary sources, current effective dates for statutes/regulations, affected ID-to-standard mappings, and compatibility with the deployed platform/SDK. When changes affect a check, update the check, [ID history](id-history.md), [CHANGELOG](../../docs/CHANGELOG.md), and related crosswalks. Only advance the source-review date after rechecking relevant sources; changing a timestamp alone is not an audit.

**Automated check:**

```bash
python3 skills/awesome-checklists/scripts/check_source_freshness.py --max-age-days 180
python3 skills/awesome-checklists/scripts/check_source_freshness.py --max-age-days 180 --fail-stale
```

The first command fails on missing/invalid/future dates and prints warnings for stale files; the second also fails for any stale file. Both GitHub Actions workflows are disabled; run nonblocking age checks locally and `--fail-stale` for explicit strict reviews. Individual dated sources can evolve faster than 180 days; this is a **maximum age trigger**, not permission to ignore critical security or regulatory changes. Human maintainers should reassess high-risk source changes whenever notified.

Network-accessible external links are probed only in a scheduled/manual **advisory** audit. Because a fixed first-N sample misses most links, the audit now rotates its bounded 120-URL window **weekly across the sorted set of links**; an explicit `--external-offset` reproduces any window locally. HTTP 404/410 is reported as possibly broken only after a **GET confirms** a HEAD failure; 401/403/429 and network failures remain inconclusive. Manual local audits list the sampled URLs and probe them with bounded concurrency; save their output because the disabled workflow cannot upload GitHub Actions artifacts. A reviewer must inspect suspected 404/410 cases before changing links. The audit is nonblocking, and rotating coverage is **not** evidence every current source is reachable or applicable. Do not claim live source validation from an offline CI pass.
