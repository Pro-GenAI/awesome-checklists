# Awesome Checklists Website

This directory contains the **website generator, styles, scripts, images, and build/deployment documentation** for a responsive, searchable **static HTML website** generated from the repository's Markdown checklists. No JavaScript framework, database, or hosted build service is needed.

**`docs/website/` is website source code, not a checklist folder.** The **91 numbered checklist templates** live in `../../lists/` and its `frontend/`, `backend/`, and `AI/` subfolders; the repository root holds `README.md` and `AGENTS.md`, with other guides in `docs/`. The migration worksheet lives under `lists/frontend/references/` and the source-coverage audit under `lists/references/`. These unnumbered files appear as **Resources** in the site, separate from numbered checklist counts. Files under `docs/website/` are website code, assets, and site-specific documentation, not checklist criteria.

## Build

From the repository root:

```bash
bash docs/website/build.sh
```

The command creates a local Python virtual environment, installs the one small Markdown-renderer dependency, discovers **all checklist Markdown and root guides outside `docs/website/`, `skills/`, and hidden/build directories**, and writes the complete site to `docs/website/dist/`.

## Preview locally

First build the site with `bash docs/website/build.sh` from the repository root. Then **run any one** of these alternatives from the repository root (do not run them all at once; each uses port 8000):

**Python 3 (standard library, no extra server dependency):**

```bash
python3 -m http.server 8000 --directory docs/website/dist
```

**Node.js (via `npx`; downloads `http-server` if necessary):**

```bash
npx --yes http-server docs/website/dist -p 8000 -a 127.0.0.1
```

**Ruby (standard-library HTTP server):**

```bash
ruby -run -e httpd docs/website/dist -p 8000
```

**PHP (built-in web server):**

```bash
php -S 127.0.0.1:8000 -t docs/website/dist
```

Open **http://127.0.0.1:8000/** in your browser. The commands serve the generated `docs/website/dist/` site; they do **not** rebuild it. Re-run `bash docs/website/build.sh` after changing source Markdown, website assets, or generator code.

To specify your real public URL (important for canonical URLs, sitemap, robots.txt, and llms.txt):

```bash
SITE_URL="https://your-domain.example/" bash docs/website/build.sh
```

The default is `https://awesome-checklists.pro-genai.com/`, configured for the production Cloudflare Pages custom domain. **Change `SITE_URL` if you deploy elsewhere**; the default is a build setting, not a claim that the site is already published.

For a preconfigured environment, install `pip install -r docs/website/requirements.txt` and run `WEBSITE_NO_VENV=1 bash docs/website/build.sh`.

## What gets generated

- `index.html` from root `README.md`
- A matching `.html` page for **every other published source Markdown file**. Checklist sources move under `lists/`, but published HTML retains its pre-move URLs (e.g., `AI/10_RAG_and_Knowledge_Bases.html`), preserving existing inbound links. Unnumbered root and `lists/**/references/` files appear as searchable **Resources**, not as checklists; existing resource page URLs are preserved.
- Landing pages for the `lists/frontend/`, `lists/backend/`, and `lists/AI/` collections
- Reader resources including `docs/CHANGELOG.md`, `docs/AUTHORSHIP.md`, `lists/references/optional-testing-tools.md`, `lists/references/id-prefix-ranges.md`, `lists/references/source-freshness-policy.md`, `lists/references/security-surface-coverage.md`, `lists/references/agent-domain-map.md`, `lists/references/agent-testing-tools.md`, `lists/references/minimum-viable-by-scope.md`, `lists/references/scoped-review-generator.md`, `lists/references/control-crosswalk.md`, `lists/references/core-50.md`, [shared review method](../../lists/references/review-method.md), [optional compliance crosswalk](../../lists/references/compliance-crosswalk.md), the worked review and overlap analysis. The machine-readable `lists/references/core-50.json` lives in the source repository; generate the full **4,215-check** JSON catalog locally using `python3 skills/awesome-checklists/scripts/export_checklists.py --output checklists.json`. Core 50 priorities are curated; remaining tiers are preliminary text-rule-derived triage.
- A client-side searchable index (`search-index.json`) and assets (`assets/`)
- A navy-and-green checkmark favicon in `assets/favicon.svg` linked from every generated page, plus a homepage hero banner in `assets/awesome-checklists-banner.svg` (also used in the root README), and a portable, readable **440 × 44 px** `assets/reviewed-with-awesome-checklists.svg` project badge with a prominent review checkmark, plus a public, larger-style Shields.io README snippet documented in the [root README](../../README.md#display-the-reviewed-with-awesome-checklists-badge). Displaying the badge is a project-maintainer self-declaration, **not independent certification**.
- Per-page titles, descriptions, canonical and Open Graph tags, breadcrumbs, and Schema.org structured data
- Search-engine discovery files (`sitemap.xml`, `robots.txt`)
- A generated root `llms.txt` listing all checklists; its introductory text is maintained in `docs/website/llms.txt`

Links from Markdown files to other Markdown files are rewritten to their corresponding HTML pages. Anchors and external URLs are preserved. New Markdown files are picked up on the **next build** without manually editing navigation.

Generated HTML is excluded from Git; `docs/website/dist/` is a deployable output artifact. Files under `docs/website/` are builder source and files under `skills/` are installable agent instructions; neither directory is indexed as checklist pages.

## Deployment

Cloudflare Pages deploys the `main` branch to https://awesome-checklists.pro-genai.com/ using `SITE_URL=https://awesome-checklists.pro-genai.com/ bash docs/website/build.sh` and the `docs/website/dist` output directory. Both GitHub Actions workflows are disabled as `.github/workflows/website.yml.disabled` and `.github/workflows/checklist-lint.yml.disabled`; none run automatically. To validate locally, run `python3 -m unittest discover -s skills/awesome-checklists/tests -v`, `python3 skills/awesome-checklists/scripts/validate_inventory.py`, `bash docs/website/build.sh`, and `python3 docs/website/check_site.py` from the repository root. Re-enable CI only through a separate, intentional decision.

## Maintain

Update `docs/website/assets/site.css` or `docs/website/assets/site.js` for presentation. Update `docs/website/llms.txt` for the introductory, human-edited LLM index text; the list of checklists is generated automatically. Keep core review guidance and stable checklist IDs in sync with [AGENTS.md](../../AGENTS.md). This is a **reference library**, not an official compliance or certification service.
