---
title: "AI Labs Claude Skills - 27 Skill Business Suite Setup"
description: "ailabs-393/ai-labs-claude-skills: 42.1K combined installs across 27 skills for travel, finance, research writing, pitch decks, SEO and Office docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ailabs-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "business operations", "document generation"]
---

# AI Labs Claude Skills - Setup Guide

**Source:** [ailabs-393/ai-labs-claude-skills](https://www.skills.sh/ailabs-393/ai-labs-claude-skills) via skills.sh - 42.1K combined installs across 27 indexed listings
**GitHub:** [ailabs-393/ai-labs-claude-skills](https://github.com/ailabs-393/ai-labs-claude-skills) (458 stars; MIT at repo level; last push 2025-11-11; layout `packages/skills/<name>/SKILL.md` for 23 skills plus a nested `packages/skills/document-skills/<name>/SKILL.md` for docx, pdf, pptx and xlsx, all mirrored into a committed `dist/skills/` build copy; 24 generated `index.js` entrypoints, none implemented)
**Category:** Business Operations / Generalist Productivity
**Quality Tier:** 🟡 Trusted - a broad, script-backed business suite with 42,078 installs where all 27 indexed listings resolve to a real skill directory, MIT at repo level and clean Trust Hub and Socket verdicts on four sampled skills, held below Production by a last push eleven months before this snapshot, no CI beyond a funding file, generated placeholder `index.js` entrypoints, and four bundled document skills that carry Anthropic's own proprietary terms instead of the repo license

AI Labs (publisher `ailabs-393`) ships one of the larger generalist skill collections on skills.sh: 27 skills that cover trip planning, personal finance, sales reporting, investor decks, SEO audits, fiction continuity, Docker and CI/CD scaffolding, and the four Anthropic document skills. It is not a narrow toolkit. It is a small business-operations department written as markdown workflows, with Python scripts behind the ones that touch files.

The shape is consistent across the suite. Each skill directory holds a `SKILL.md` that opens with a short interview or clarification step (preferences, constraints, style), then a numbered workflow, then calls into `scripts/` for anything deterministic. Skills that need memory persist JSON under `~/.claude/`. That consistency is why the suite installs well and why it is worth reading before installing: the same front-loaded-question pattern explains most of its behaviour, and the same `dist/` mirror explains why a naive file count double-counts it.

## Installation

```bash
# The whole suite, 27 skills in one install
npx skills add ailabs-393/ai-labs-claude-skills
```

```bash
# The published npm package, Node >= 18 (README badge)
npm i ai-labs-claude-skills
```

The README's own build path, if you work from a clone of the repo rather than the npm package:

```bash
npm install
npm run build
npm run gen:pkg
npm run gen:index
```

`npm install` triggers the `postinstall` hook, which runs `install-skills.mjs` and copies `dist/skills` into `<your project>/.claude/skills`. Several skills call Python, so install their dependencies first: `pip install -r packages/skills/data-analyst/requirements.txt` covers pandas, numpy, scikit-learn, plotly, dash and dash-bootstrap-components; the document and deck skills need `python-pptx`, `pypdf`, `lxml` and `defusedxml`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| travel-planner | 4,079 | Trip planning with a stored preference profile: day-by-day itinerary, budget breakdown, packing list and cultural notes generated as JSON from `plan_generator.py` |
| research-paper-writer | 3,271 | IEEE and ACM structured academic papers: section scaffolding, citation handling and scholarly phrasing for a stated topic and length |
| personal-assistant | 2,705 | Task, schedule and habit tracking against a persistent JSON profile in `~/.claude/personal_assistant`, with retention rules for stale context |
| finance-manager | 2,482 | Transaction extraction from PDF or CSV, spending analysis, savings rate, and an HTML financial report with charts |
| business-analytics-reporter | 2,221 | CSV sales and revenue analysis that names weak areas, interprets the statistics and writes improvement strategies |
| script-writer | 1,894 | YouTube scripts from a stored style profile: hooks, retention structure, tone and length for a given topic |
| nutritional-specialist | 1,865 | Meal plans, recipes and dietary advice filtered through stored allergies, restrictions and goals |
| pitch-deck | 1,711 | Ten-slide investor or sales deck written as a real .pptx through `create_pitch_deck.py` |
| startup-validator | 1,562 | Market, competitor and problem-solution validation, backed by the agent's own web research |
| codebase-documenter | 1,513 | README, architecture, API and code-comment documentation for an existing codebase, with beginner-first templates |
| social-media-generator | 1,487 | Per-platform posts for X, Instagram, LinkedIn and Facebook, written into an organised folder with meaningful filenames |
| storyboard-manager | 1,423 | Fiction continuity: character development, plot structure, timeline tracking and consistency checks over a storyboard folder |
| business-document-generator | 1,403 | Proposals, business plans and annual budgets filled from bundled PDF templates via `generate_document.py` |
| csv-data-visualizer | 1,331 | Plotly charts, statistical data profiling and multi-plot dashboards for a CSV file |
| seo-optimizer | 1,276 | HTML and CSS SEO audit: meta tags, headings, schema markup, plus sitemap generation from a site directory |
| data-analyst | 1,173 | Missing-value detection and statistical imputation, then a Plotly Dash dashboard over the cleaned data |
| docker-containerization | 1,125 | Dockerfile and compose generation for Next.js and Node, with `docker-build.sh`, `docker-run.sh`, `docker-push.sh` and `docker-cleanup.sh` |
| brand-analyzer | 1,106 | Brand archetype and identity analysis that outputs a written brand guidelines document |

The remaining 9 indexed listings range from 890 to 987 installs: resume-manager (987, one-page PDF resumes built from a stored experience database), tech-debt-analyzer (985, code smell and dependency reports), cicd-pipeline-generator (980, GitHub Actions, GitLab CI and CircleCI configs), frontend-enhancer (968, Next.js styling, palettes and layout patterns), docx (922), pptx (914), pdf (903) and xlsx (890), which are the four Anthropic document skills carried in the nested `document-skills` folder, and test-specialist (902, unit, integration and end-to-end test authoring for JavaScript and TypeScript).

## Why This Matters for Hermes Agents

Most of this suite is work a Hermes session already attempts ad hoc: a sales CSV turned into findings, a deck outline turned into slides, a site audited for meta tags, a repo documented. What the skills add is a fixed question order and a fixed output shape. The front matter of each `SKILL.md` states when to invoke, then the workflow states what to ask before writing anything. Loading one gives a session a specification instead of a blank page, which is the difference between a plausible report and a repeatable one.

The second gain is the deterministic half. `finance-manager` ships `extract_pdf_data.py`, `analyze_finances.py` and `generate_report.py`; `csv-data-visualizer` ships `data_profile.py`, `visualize_csv.py` and `create_dashboard.py`; `pitch-deck` and `business-document-generator` emit real `.pptx` and `.pdf` files. Those scripts make no network calls (no `requests`, `urllib` or `curl` anywhere in the bundled Python, shell or JS), so an agent can run them in a sandbox and check the artifact before showing it to anyone.

The third is the memory pattern. Five of the skills front-load an interview and write the answers to JSON under `~/.claude/`: travel-planner and personal-assistant as per-skill directories, nutritional-specialist, resume-manager and script-writer as single files. Later runs read them back instead of re-asking. On a Hermes host that path belongs to a different tool, so you either repoint `DB_DIR` in the script or accept a stray directory, but the pattern itself is worth copying: collect preferences once, keep them small, expire what is stale. `personal-assistant` even ships explicit retention rules for discarding old context.

Finally, read it as a catalogue of prompts rather than as an SDK. Every npm `index.js` in `packages/skills` is a generated stub that logs the skill name and returns its input untouched, so nothing here runs through the package entrypoint. The value is `SKILL.md` plus `scripts/`, and the four document skills are Anthropic's own work redistributed under Anthropic terms, not original AI Labs content.

## Usage

| You say | What happens |
|---|---|
| "Plan ten days in Japan for two, mid budget, no seafood" | travel-planner collects or loads preferences, writes a day-by-day itinerary with a budget split and packing list through `plan_generator.py` |
| "Where is my money going this quarter" | finance-manager extracts transactions from the statement PDF or CSV, computes category totals and savings rate, then writes an HTML report with charts |
| "Turn this sales export into a board update" | business-analytics-reporter runs `analyze_business_data.py`, names the weak segments and drafts strategies tied to the numbers |
| "Build me an investor deck for this idea" | startup-validator pressure-tests the market first, then pitch-deck writes the ten slides to a .pptx |
| "Write the README for this repo" | codebase-documenter walks the tree, then produces a getting-started guide, architecture notes and API reference from its templates |
| "Audit our marketing site for SEO" | seo-optimizer checks meta tags, heading order, schema and sitemaps with `seo_analyzer.py` and `generate_sitemap.py`, then lists fixes |
| "Containerise this Next.js app" | docker-containerization writes a multi-stage Dockerfile and compose file, plus the build, run and push scripts |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "travel-planner|finance-manager|pitch-deck"
```

Read a skill before trusting it. Note the filename case: this repo has no `README.md`, the file is `ReadMe.md`, so a lowercase probe returns 404. Every URL below returned 200 when checked with `curl` on Oct 26, 2026, and `.../main/README.md` returned 404 on the same date:

```bash
B=https://raw.githubusercontent.com/ailabs-393/ai-labs-claude-skills/main
curl -sL $B/ReadMe.md
curl -sL $B/LICENSE
curl -sL $B/packages/skills/travel-planner/SKILL.md
curl -sL $B/packages/skills/finance-manager/SKILL.md
curl -sL $B/packages/skills/seo-optimizer/SKILL.md
curl -sL $B/packages/skills/document-skills/docx/SKILL.md
curl -sL $B/install-skills.mjs
```

Prove the Python side imports before a task depends on it:

```bash
python3 -c "import pandas, numpy, plotly, dash; print('viz ok')"
python3 -c "import pptx, pypdf; print('docs ok')"
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| travel-planner | Pass | Pass | Warn |
| research-paper-writer | Pass | Pass | Pass |
| finance-manager | Pass | Pass | Pass |
| seo-optimizer | Pass | Pass | Pass |

The single non-Pass verdict is informative rather than alarming. Snyk's audit of travel-planner on Sep 15, 2026 rates it MEDIUM with one finding, W011 third-party content exposure at 0.10: the workflow runs web searches for destination information, so the agent ingests untrusted external pages. No sampled skill carries a malware, injection or exfiltration finding.

Read the write surface before installing, because none of it is declared. No `SKILL.md` in the repo carries an `allowed-tools` or permissions block, so whatever the host agent can do, these skills can do. Concretely: the memory skills create directories and JSON files under `~/.claude/`; `plan_generator.py`, `generate_report.py` and the document scripts write output files wherever you point them; `docker-push.sh` runs `docker push` against whatever registry it is given, which publishes an image; and `install-skills.mjs` copies `dist/skills` into `<project>/.claude/skills` and then, 1.5 seconds later, recursively deletes its own package folder inside `node_modules`. Network access is not in the bundled code, it is in the instructions: travel-planner and startup-validator both tell the agent to search the web. Treat any skill that asks the agent to browse as untrusted-input handling, and keep the memory databases out of any directory you sync or publish.

## Limitations

- The repo is a snapshot, not a maintained product. `package.json` sits at 2.0.0 and the last commit is 2025-11-11, eleven months before this sweep. `.github` holds only `FUNDING.yml`, and although `package.json` declares `npm test -ws`, the only test file in the tree is one pytest for the bundled pdf skill's bounding-box helper.
- The root readme is `ReadMe.md`, not `README.md`. Any tooling or guide that probes the lowercase path gets a 404, and so does `raw.githubusercontent.com/.../main/README.md`.
- The tree carries 54 `SKILL.md` files for 27 skills: `packages/skills` holds 27 and the committed `dist/skills` build copy holds the same 27 again. A raw file count therefore doubles the suite. The four document skills also sit one level deeper, under `packages/skills/document-skills/`, while skills.sh indexes them as flat ids (docx, pdf, pptx, xlsx).
- License is mixed, not uniformly MIT. The repo `LICENSE` and root `package.json` say MIT, but `document-skills/{docx,pdf,pptx,xlsx}/SKILL.md` each declare `license: Proprietary. LICENSE.txt has complete terms`, and each bundled `LICENSE.txt` reads `(c) 2025 Anthropic, PBC. All rights reserved` with use governed by your Anthropic agreement. Redistributing or shipping those four under an MIT assumption is a licensing error.
- The npm package is a delivery vehicle, not a library. All 24 `index.js` entrypoints are the stub that `generate-index-files.js` writes: they log the skill name and return the input unchanged. Do not plan integrations against them.
- Persistence paths are hardcoded to `Path.home() / ".claude" / <skill>` in `assistant_db.py`, `travel_db.py`, `script_db.py` and `resume_db.py`, so on a Hermes host the data lands outside the Hermes profile and survives uninstall.
- Only one of the four sampled skills carries a non-Pass verdict: travel-planner has the Snyk Warn for browsing, while research-paper-writer, finance-manager and seo-optimizer are Pass on all three scanners. The other 23 listings were not sampled, and startup-validator also instructs the agent to browse without a published audit of its own.
- The same publisher ships `ailabs-393/design-md-planner` as a separate source with 32 installs. It is not part of this repo and is excluded from the 42,078.
- Snapshot data, verified Oct 26, 2026: 42,078 combined installs across 27 indexed listings; 458 GitHub stars; MIT at repo level with the four document skills under Anthropic proprietary terms; last pushed 2025-11-11. Counts drift over time.

## Related

- [Alireza Rezvani Claude Skills - 341 Engineering & Marketing Skills Setup](/hermes/skills/catalog/alirezarezvani-claude-skills-setup) - the same one-publisher-many-skills shape at a much larger roster.
- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup) - the aggregate-catalog route to the same breadth, if you would rather pick skills individually.
- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup) - Anthropic-published skills, useful context for the four document skills bundled here under Anthropic terms.
- [ResumeSkills - AI-Powered Resume Optimization Setup](/hermes/skills/catalog/resumeskills-setup) - a dedicated resume suite if resume-manager here is the only part you need.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole suite once, then delete the directories you will never invoke. 27 skills loading their descriptions into context costs more than the four or five you actually use, and what the CLI installs is plain folders, so dropping the rest is just a delete.
- Repoint `DB_DIR` at your agent's own state directory before first use of travel-planner, personal-assistant, script-writer or resume-manager. Otherwise the profile JSON accumulates under `~/.claude/` and is invisible to every later session.
- Treat `postinstall` as a write you did not ask for. It copies into `<project>/.claude/skills` and then removes its own `node_modules` folder; run `npm i ai-labs-claude-skills --ignore-scripts` if you only want the files.
- For anything that produces a file (deck, report, resume, document), run the Python script directly and open the artifact. The agent's summary of a .pptx is not evidence that the .pptx exists or looks right.
- Check the docx, pdf, pptx and xlsx licences separately before shipping output built with them. The repo says MIT, those four say Anthropic proprietary, and the second one governs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
