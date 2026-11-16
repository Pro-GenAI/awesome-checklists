# Website redesign SEO — URL migration map template

> **Optional project-specific planning worksheet, not a numbered checklist or an assurance of search rankings.** Copy this table into your own project document or spreadsheet. Keep private customer metrics and access credentials out of this shared repository. Adapt it only when pages or URLs actually change. The testable requirements are maintained in the linked numbered checklists; this file supplies an example table, not a second review gate.

**Based on:** [Google Search Central — Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes). **Reviewed:** 2026-11-13. Relevant checklist controls: [`SEO-032`, `SEO-048`, `SEO-010`, `SEO-012`, `SEO-029`](../13_SEO.md), and [`LAUNCH-117`, `LAUNCH-130`](../20_Release_and_LaunchReadiness.md).

## Checklist coverage

The following existing checklist controls own the verifiable acceptance criteria. This worksheet does not add checklist IDs or replace project-specific test evidence.

| Worksheet stage | Primary controls |
| --- | --- |
| Baseline, old-to-new URL decisions, owners and monitoring | [SEO-032](../13_SEO.md) |
| Redirects, removals, final URLs, canonicals, sitemaps and redirect retention | [SEO-048](../13_SEO.md), [SEO-010/012](../13_SEO.md) |
| Correct Search Console ownership, supported Change of Address cases and diagnostics | [SEO-029/032](../13_SEO.md) |
| Production/staging rules, critical user journeys and launch sign-off | [SEO-086](../13_SEO.md), [LAUNCH-117/130](../20_Release_and_LaunchReadiness.md) |

## Before launch: document the baseline and mapping

Record the migration owner, release/environment, planned launch window, redirects owner, URL inventory source, important canonical/indexed pages, primary search landing pages, Search Console access and baseline query/click/conversion date range. Record whether content has meaningfully changed, not just the URL.

| Old URL (example) | New URL / decision | Expected response at old URL | Content equivalence / rationale | Priority & verification evidence |
| --- | --- | --- | --- | --- |
| `https://example.test/services/design` | `https://example.test/web-design` | `301`/`308` permanent redirect | Same service; new slug | High; inspect actual response and final canonical |
| `https://example.test/about` | Keep same URL | `200` | Unchanged canonical route | Test production page, no redirect necessary |
| `https://example.test/legacy-offer` | Retire with no replacement | `404` or `410` | No genuinely equivalent destination | Check removed page is omitted from sitemap; do not redirect to an irrelevant homepage |

Use **example-only domains** above. For real migrations, record every important discoverable URL and identify 1:1 or many-to-one mappings only where destination intent and content actually match. A spreadsheet can add columns for source HTTP status, destination HTTP status, canonical URL, robots/noindex status, redirect hops, content owner, inbound-link/referral importance, assigned tester, date, and retest outcome.

## During launch: verify actual behavior

- Validate old URLs with real HTTP requests: correct permanent redirects for actual moves, no broken targets or loops, no irrelevant redirects, and appropriate `404`/`410` for permanently removed content.
- Inspect destination HTTP status, canonical tags, metadata, rendered content and production `robots.txt`/`noindex` state. A protected staging site must not be relied on for production indexing rules.
- Update contextual internal links, public profile links and XML sitemaps to final canonical destinations. Avoid chains by linking directly to the final destination.
- For eligible **domain or subdomain** moves, verify old/new Google Search Console properties and assess the Change of Address tool; path-only changes, HTTP-to-HTTPS changes, and www/non-www changes on the same domain do not require that tool.
- Verify migration and new-site capacity, accessibility and user journeys before declaring release readiness.

## After launch: keep monitoring and ownership

- Compare dated Search Console click/impression, indexing and coverage diagnostics with the approved baseline; monitor old and new URL server logs and analytics. Allow for temporary ranking fluctuation; do not promise unchanged ranking positions.
- Keep permanent migration redirects **generally at least one year** and longer when practical, especially while external visitors and backlinks still reach old URLs. Schedule an owner and review date before removing any redirect.
- Triage unexpected 404s, soft-404s, incorrect canonicals, redirect chains, blocked pages, stale sitemaps, broken critical flows and unexplained traffic losses; track evidence and remediation in your project issue tracker.
- If no URLs changed during the redesign, record this explicitly and verify content, metadata, canonical/indexing rules and performance without creating unnecessary redirects.

**Not an SEO loophole:** Purchasing aged domains just to inherit historical rankings is a separate, potentially manipulative practice; see [questionable tactics](https://github.com/Pro-GenAI/checklists-2/blob/main/seo-aeo-geo-tricks.md). This worksheet is for **legitimate content/site continuity**, not expired-domain ranking schemes.