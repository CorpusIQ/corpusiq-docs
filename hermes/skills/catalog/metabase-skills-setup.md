---
title: "Metabase Skills - BI and Dashboard Agent Suite"
description: "metabase/metabase: 20.3K combined installs. Metabase's own agent skills for dashboards, MBQL queries, docs and Clojure or TypeScript review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/metabase-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "business intelligence", "metabase", "dashboards", "clojure"]
---

# Metabase Skills - Setup Guide

**Source:** [metabase/metabase](https://www.skills.sh/metabase/metabase) via skills.sh - 20.3K combined installs across 28 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [metabase/metabase](https://github.com/metabase/metabase) - 50,069 stars, license field NOASSERTION (the root carries `LICENSE.txt`, `LICENSE-AGPL.txt`, `LICENSE-EMBEDDING.txt` and `LICENSE-MCL.txt`), branch master, last pushed 2026-11-01; 30 `SKILL.md` directories in two roots, 24 under `.claude/skills/` (plus a `_shared/` folder of style references) and 6 under `resources/mcp/v2/skills/`

**Category:** Metabase analytics work for agents: dashboard layout, filters, SQL dialects and visualisation settings

**Quality Tier:** 🟡 Yellow - one sampled skill (`typescript-review`) carries a Snyk Warn, and the GitHub license field reads NOASSERTION across four separate license files at the repository root

Metabase is the open source business intelligence and embedded analytics tool, and its monorepo carries two skill families written for two different jobs. The 24 skills under `.claude/skills/` govern work on the Metabase codebase itself: Clojure and ClojureScript authoring and review, TypeScript authoring and review, documentation writing and review, Cypress end to end tests, serdes YAML round trips, application database migrations, Malli schemas, frontend module boundaries and product analytics events. The six skills under `resources/mcp/v2/skills/` cover the other direction: they teach an agent the op grammars behind the Metabase MCP server's write tools, so a request like "add a filter to this dashboard" lands as a valid `add_parameter` and `wire_parameter` pair rather than a plausible-looking guess.

That split is the interesting part of this pack. The install counts describe the repository's contributor skills: 23 of the 28 listings map to a directory under `.claude/skills/`, and the other five (`metabase-data-app-*`) have no directory in the current tree. None of the six `resources/mcp/v2/skills/` names appears in the index at all. So the numbers rank the build-side skills, and the MCP-side skills, which are the ones a profile working on dashboards and queries would actually load, arrive without a count attached.

## Installation

The root README is the product README: a Cloud trial pitch, a feature list and screenshots, with no skills install documentation at all. The two pages that do document a skills CLI install point somewhere else: `docs/installation-and-operation/metabase-cli.md` and `docs/ai/agent-driven-development.md` both install the `metabase-cli` skill from the separate `metabase/agent-skills` repository, with `npx skills add metabase/agent-skills --skill metabase-cli -a claude-code` or the `metabase/mb-cli` Claude Code plugin. That route installs none of the 30 directories in this pack. The only in-repo routing guide is `AGENTS.md`, which points contributors at the `.claude/skills/` entries by path for work done inside the monorepo, so the CLI route is not documented for these skills and the durable install is a directory copy of both skill roots:

```bash
git clone --depth 1 https://github.com/metabase/metabase.git /tmp/metabase
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r /tmp/metabase/.claude/skills/. ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/metabase/resources/mcp/v2/skills/. ~/.hermes/profiles/corpusiq/skills/
```

The first copy brings 24 skill directories plus `_shared/`, and that folder has to travel with them: the skills pull it in by relative path, so `typescript-write` opens `@./../_shared/typescript-commands.md` and `@./../_shared/react-redux-patterns.md`, `clojure-write` opens the Clojure style guide and command references, and `docs-review` opens `metabase-style-guide.md`. Copying a single skill directory out of that layout silently loses its rules. The second copy adds the six MCP v2 skills (`dashboard-filters`, `dashboard-layout`, `documents`, `native-parameters`, `query-dialect`, `visualization-settings`), and no name collides between the two roots.

Two practical caveats come with the copy. Several of the development skills drive tooling that lives in the monorepo rather than in the skill: `clojure-eval` expects `clj-nrepl-eval` against a running nREPL, `app-db-migrations`, `backend-module-conventions` and `name-module-cycle` all reference `./bin/test-agent`, and the Cypress skills assume the repo's `e2e/` layout. Those commands belong to a Metabase checkout, so treat the skills as guidance for work in a clone, not as a self-contained toolchain. The MCP v2 skills describe the op grammars of the `dashboard_write`, `question_write`, `document_write` and `execute_query` tools, so they are actionable where a Metabase MCP v2 server is connected, and useful as reference material even where it is not.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| typescript-review | 2,304 | Reviewing TypeScript and JavaScript diffs and PRs against Metabase coding standards, style violations and code quality issues, with the shared style references loaded alongside. |
| typescript-write | 2,123 | Writing or modifying TypeScript and JavaScript, including tests and test helpers, before editing any TS, TSX, JS or JSX file in the frontend. |
| docs-write | 2,095 | Writing documentation in Metabase's conversational, user-focused style when creating or editing markdown and MDX files under `docs/`. |
| docs-review | 2,026 | Reviewing documentation diffs, files and PRs against the Metabase style guide, which the skill loads from `_shared/metabase-style-guide.md`. |
| clojure-write | 2,023 | REPL-driven Clojure and ClojureScript development: the coding conventions, workflow and command references to load before writing or refactoring backend code. |
| clojure-review | 2,013 | Reviewing Clojure and ClojureScript changes for Metabase coding standards, style violations and code quality issues. |
| analytics-events | 1,987 | Adding product analytics events that track user interactions in the Metabase frontend. |
| add-malli-schemas | 1,974 | Adding Malli schemas to API endpoints with the repo's patterns for validation timing and error handling. |
| metabase-data-app-semantic-layer | 816 | Data app work over the semantic layer: this listing has no matching directory in the current tree, and `docs/data-apps/build.md` documents the app route over published tables, metrics and the app's own collection. |
| metabase-data-app-actions | 814 | Data app writes through actions: no matching directory in the current tree; `docs/data-apps/build.md` states an app can write only through table actions or SQL actions in its own collection. |
| metabase-data-app-setup | 804 | Setting up a data app: no matching directory in the current tree; `docs/data-apps/build.md` lists the Metabase CLI (`mb`), Remote Sync, Node 22.12 and a Pro or Enterprise plan as requirements. |
| metabase-data-app-routing | 800 | Data app pages and routes: no matching directory in the current tree, and no page under `docs/data-apps/` covers routing; the docs mention that admins open a built app at `/apps/<slug>`. |
| metabase-data-app-migrate | 158 | Migrating data apps: no matching directory in the current tree, and no page under `docs/data-apps/` covers migration. |

The remaining 15 indexed listings range from 3 to 94 installs.

## Why This Matters for Hermes Agents

The MCP v2 skills answer a failure mode that ordinary prompt engineering does not touch. A model can write a dashboard request that looks right and fails at the API boundary: a parameter wired to the wrong target field, a card placed outside the 24-column grid, a native SQL question whose template tag kind is wrong, an MBQL query built on table names instead of numeric ids. Each of the six skills documents one of those grammars, with the trigger phrases written in, and `query-dialect` explicitly says to read it before authoring any non-trivial query or after a shape or unknown-id rejection.

The development skills matter for a different reason: Metabase is a 50,069-star Clojure codebase with strong in-house conventions, and the skills encode them as review gates rather than suggestions. `clojure-write` and `clojure-review` split authoring from review, `typescript-write` and `typescript-review` do the same for the frontend, and `docs-write` and `docs-review` do it again for documentation. The pairing is deliberate: the write skill carries the workflow and the review skill carries the checklist, so an agent that both edits and reviews its own work gets two different rule sets.

The `_shared/` folder is the piece that makes the set coherent. Style guides, command references and convention documents live once and are imported by whichever skill needs them, so a profile that copies one directory loses the exact rules that directory assumes. Keep the layout intact and the review skills behave like a house style guide; break it and they degrade into generic advice.

## Usage

| You say | What happens |
|---|---|
| "Add a filter on plan type to this dashboard" | `dashboard-filters` picks the `add_parameter` type and value source, then wires it with the `target_field` or `target_tag` grammar instead of a raw target. |
| "Build a dashboard from these six cards, with a KPI row at the top" | `dashboard-layout` works inside the 24-column grid, chooses per-display default sizes and the KPI-row pattern, and gives every card a tab. |
| "Aggregate orders by month and compare to last year" | `query-dialect` shapes the MBQL clause sequence, filters and breakouts, and uses multi-stage queries for the year-over-year comparison. |
| "Make this card a bar chart with currency formatting" | `visualization-settings` sets `display` for the data shape and writes `visualization_settings`, including the column-name rule and the `column_settings` JSON-string-key trap. |
| "Why does my SQL card return no rows when I pass a value" | `native-parameters` walks the template tag kinds, tells a field filter from a raw variable, and checks the `[[ ]]` optional blocks and widget types. |
| "Review this Clojure PR before I merge it" | `clojure-review` checks the diff against Metabase style and quality rules, with the Clojure style guide pulled in from `_shared/`. |
| "Export these dashboards, edit the YAML, import them back" | `serdes-workflow` runs the export, validate and import round trip, and `serdes-yaml-edit` handles the portable references inside the YAML. |

## Verification

The raw path for `dashboard-layout` returned HTTP 200 on branch master when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} dashboard-layout\n" \
  https://raw.githubusercontent.com/metabase/metabase/master/resources/mcp/v2/skills/dashboard-layout/SKILL.md
```

Expect `200`. After the copies land, confirm both roots arrived and that the shared folder survived beside the skills:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{dashboard-layout,query-dialect,typescript-write,clojure-eval}/ | wc -l
ls ~/.hermes/profiles/corpusiq/skills/_shared | head -4
head -5 ~/.hermes/profiles/corpusiq/skills/dashboard-layout/SKILL.md
```

The count should print 4, the shared listing should show `clojure-style-guide.md`, `cypress-conventions.md`, `development-workflow.md` and `metabase-style-guide.md`, and the header should show `name: dashboard-layout`.

## Security

One of the five sampled skills carries a Snyk warn, which is what makes this pack Yellow despite clean Gen Agent Trust Hub and Socket verdicts across the sample.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| typescript-review | Pass | Pass | Warn |
| add-malli-schemas | Pass | Pass | Pass |
| e2e-test | Pass | Pass | Pass |
| serdes-yaml-edit | Pass | Pass | Pass |
| app-db-migrations | Pass | Pass | Pass |

The skill payload itself is markdown. There is no package to install, no build step and no postinstall hook in the skills, so the reviewable surface is prose plus relative links into `_shared/`. The warns sit on a large commercial codebase rather than on a script, and the plausible reading is that a review skill over a monorepo this size trips heuristics without naming a specific finding.

The licence question deserves more attention than the verdicts. The GitHub license field reports NOASSERTION because the repository mixes four licenses: the `LICENSE.txt` says source outside the top-level `enterprise` directory is AGPL, `LICENSE-AGPL.txt` carries the GNU Affero GPL v3 text, `LICENSE-MCL.txt` puts the `enterprise` directory and Enterprise Edition features under the Metabase Commercial License, and `LICENSE-EMBEDDING.txt` is a separate agreement for `app-embed.js`. Copying skill prose into a profile is low risk; copying code out of the repository is not, and the AGPL and commercial terms travel with that code.

Anything an agent runs from these skills reaches outside the markdown. `clojure-eval` talks to a live nREPL, the Cypress skills drive a browser against a running instance, and the migration and module skills shell out to `./bin/test-agent`. Point them at a development instance with disposable data, keep database credentials in the environment rather than in a prompt, and treat a Metabase session cookie or API key as a secret the agent never prints.

## Limitations

- Snapshot data, verified 2026-10-31: 20,284 combined installs across 28 indexed listings; 50,069 GitHub stars; license field NOASSERTION with AGPL, commercial and app-embed license files at the root; last pushed 2026-11-01. Counts drift over time.
- The pushed date reads 2026-11-01 because GitHub timestamps are UTC (`2026-11-01T01:25:55Z`), which is the evening of 2026-10-31 in US Mountain time. Treat the sweep date and the push date as the same day.
- Index and tree disagree in both directions. The five `metabase-data-app-*` listings carry installs but have no `SKILL.md` directory in the current tree, and none of the six `resources/mcp/v2/skills/` names appears in the index, so the MCP-facing skills ship without install counts.
- `metabase-ui-component-from-figma` is the third kind of gap: a real directory in `.claude/skills/` with no indexed listing, so it arrives with the copy and never shows in the numbers above.
- Most of the development skills are repo-scoped. `clojure-eval`, the Cypress pair, `app-db-migrations`, `backend-module-conventions` and `name-module-cycle` all assume a Metabase checkout with its nREPL, `./bin/test-agent` and `e2e/` layout, so outside a clone they are review guidance rather than runnable workflow.
- Install counts are not a ranking of usefulness. The top eight rows are codebase-wide authoring and review skills, while the six skills that describe the MCP tool grammars carry no count at all.

## Related

- [Upstash Skills - Serverless Backend Setup](/hermes/skills/catalog/upstash-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy `.claude/skills/.` rather than individual skill directories. The `@./../_shared/` imports are relative, and a skill moved out of that layout loads no style guide at all.
- Install the six MCP v2 skills even if no Metabase MCP server is connected yet. `query-dialect` and `native-parameters` read as a specification of the tool surface, which is cheaper than discovering the clause shapes by rejection.
- Read `dashboard-layout` before the first dashboard request, not after. The every-card-needs-a-tab rule and the 24-column grid are the two constraints that produce the "squished into half the width" failure the skill names.
- Confirm which of the two families you are editing. `.claude/skills/` skills describe changing the Metabase codebase; `resources/mcp/v2/skills/` skills describe driving a Metabase instance. Pointing a contributor at the MCP skills wastes a load.
- Check the five `metabase-data-app-*` listings against the tree before linking to them in any workflow. They have counts, but no skill file to run.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
