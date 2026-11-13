---
title: "Make Platform Skills - Make.com Automation Setup"
description: "qfeius/make-platform-skills: 4.7K combined installs across 18 listings for Make.com app work - makecli, DSL YAML, UI, permissions and invoice OCR"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/make-platform-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "make.com", "low-code", "automation"]
---

# Make Platform Skills - Setup Guide

**Source:** [qfeius/make-platform-skills](https://www.skills.sh/qfeius/make-platform-skills) via skills.sh - 4.7K combined installs across 18 indexed listings; first seen Nov 11, 2026
**GitHub:** 0 stars, AGPL-3.0, `main` branch, last pushed 2026-11-11, 18 `SKILL.md` files under `skills/` against 18 indexed listings, 283 files in total
**Category:** Build and operate applications on the Make platform, from CLI and DSL to UI, permissions and release
**Quality Tier:** 🟡 Established - an 18-for-18 tree with working CLI and channel guidance, held back by zero stars, a single publisher and an AGPL licence.

This is not a collection of independent skills. It is one product's engineering standard, split into 18 files with an explicit routing table: a user question maps to a skill, and a task that crosses domains combines several with a stated division of labour. The README states which skill owns what and, just as usefully, which skill must not absorb another's rules.

The subject is the Make platform, and the skills cover the full build: `makecli` for platform resources and commands, `makedsl` for the DSL YAML that defines apps, entities, fields, relations and views, `makeui` for frontend layout in `apps/ui`, and the `make-app-*` family for the runtime concerns behind it (auth, service APIs, filtering, sorting, grouping, permissions, record actions, observability, trace IDs). `make-integration` handles invoice and receipt recognition, and `canvas-table-integration` and `make-ai-assistant` cover two out-of-house component packages.

The README is written in Chinese. That is worth knowing before you install: the skills themselves are runtime instructions, but the routing table, the channel documentation and the per-skill usage notes that make the pack usable all live in that README.

## Installation

The README documents two release channels, `main` for verified skills and `beta` for candidates, and gives both a makecli path and a direct npx path:

```bash
npx -y skills add https://github.com/qfeius/make-platform-skills/tree/main \
  --skill '*' --agent codex claude-code -y --global
```

```bash
# switch channel, then install what is missing
makecli settings set channel beta
makecli skills update
```

```bash
npx skills add qfeius/make-platform-skills --skill make-app-approval -g
```

`settings set` only records the choice; the content is replaced on the next install or update. To upgrade already-installed skills without changing channel, the README gives `npx skills update -g`. New skills added to the repo do not arrive through that path, so use `makecli skills update` or the `npx skills add` form when the pack grows.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| makecli | 338 | Driving Make from the CLI: create and deploy apps, diff and apply, inspect apps, entities, relations and records, configure token and server URL. |
| makedsl | 335 | Generating Make DSL YAML for apps, entities, fields, relations, views and options before anything is applied remotely. |
| make-integration | 332 | Invoice and receipt recognition: pulling amounts and tax identifiers out of taxi, train, hotel and restaurant vouchers. |
| makeui | 328 | Make App frontend work: app shell, list, create, edit and detail pages, drawers, workbench, bottom navigation and responsive layout. |
| make-app-auth | 327 | The unified login path: authenticated `/api/make/**` requests, 401 and 403 handling, logout and current identity context. |
| make-app-service | 324 | Service API contracts in `apps/service`: schema transfer, records, users, departments, lookup and file proxies. |
| make-app-runtime | 323 | Build and release contract: packaging, container entry points, service start failures, dist output and workspace layout. |
| make-app-filter | 319 | Record list filtering: keyword search compiled to `filter.expression`, advanced filters, AND/OR condition groups and filter presets. |
| canvas-table-integration | 311 | Consumer-side wiring of `@qfei-design/canvas-table`: columns from JSON meta, virtual loading, grouped tables and cell editing. |
| make-app-permission | 296 | Single-app permission chain: menu, route, button and field visibility, create fields and record level read, create, update and delete. |
| make-env-setup | 274 | Preparing the local Make environment: Node, package manager, git and makecli version checks plus login verification. |
| make-app-sort | 274 | Record list sorting: multi-field sort with priority, drag ordering, header sort linkage and saved sort presets. |
| make-app-group | 266 | Multi-level grouping: group conditions, drag grouping, group presets, group filtering and leaf pagination. |
| make-app-actions | 257 | Record actions: single edit and delete, checkbox selection, batch edit, row level write pre-checks and selection safety. |
| make-ai-assistant | 240 | Integrating `@qfei-design/make-ai-assistant`: multi-session chat, SSE streaming, file and image upload, history and feedback. |

The remaining 3 indexed listings range from 4 to 119 installs (make-app-observability 119, make-app-approval 82, and one malformed index entry at 4).

## Why This Matters for Hermes Agents

Most skill packs are a bag of options. This one is a set of contracts, and that changes what an agent can be trusted to do with it. The README's routing table states priority rules: an explicitly named skill wins, otherwise the question keywords choose, and when a task spans domains the main skill owns the rules while the others only carry a hand-off note.

For anyone building an internal app on a low-code platform, the hard parts are the ones nobody demoes: who can see which field, what happens on a 401 mid-session, which trace ID ties a UI error to a gateway log, what the release contract says about the service entry point. Those are exactly the skills in the `make-app-*` family, and each one is written as a boundary rather than a tutorial.

The channel design is also unusually disciplined for a skill repo. Candidates land on `beta`, get exercised by real agent tasks, then merge to `main`, and the same `[settings] channel` switches both the CLI and the skill set. That is a working answer to the problem every skill pack eventually hits: how do you ship a change to instructions that an agent follows literally.

The caveat is scope. These skills teach the Make platform's conventions and package APIs, not a general method. The value is high inside that platform and close to zero outside it.

## Usage

| You say | What happens |
|---|---|
| "Set up the Make development environment on this machine" | Runs `make-env-setup`, checks Node, package manager, git and makecli versions, then verifies the login. |
| "Model a customer object with these fields and a relation to orders" | Runs `makedsl` for the DSL YAML, then `makecli` to apply and deploy. |
| "Build the list page for this object" | Runs `makeui` with `canvas-table-integration` and `make-app-actions`, giving a table on desktop and cards on mobile. |
| "Add advanced filtering with AND/OR groups on this list" | Runs `make-app-filter` to compile the conditions and wire the panel, with `make-app-permission` for field level access. |
| "Lock the salary field so only HR can read it" | Runs `make-app-permission` for the field and route permissions, with `make-app-service` enforcing the same result server side. |
| "The service container will not start after deploy" | Runs `make-app-runtime` against the packaging and entry point contract and reports what is missing. |
| "Read the totals off this stack of taxi and hotel receipts" | Runs `make-integration` and returns the recognised amount and tax identifiers per document. |

## Verification

The tree is `skills/<name>/SKILL.md` on `main`. Both probes returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/qfeius/make-platform-skills/main/skills/makecli/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/qfeius/make-platform-skills/main/skills/makedsl/SKILL.md
```

After a global install, confirm 18 directories under the skills target. Check the channel too: `makecli skills list` reports the target channel and branch, so a beta install that was meant to be stable shows up there rather than in a failing task.

Read `make-env-setup` before running any other skill. Several of the others assume a verified makecli login and a pinned Node baseline, and they fail in confusing ways when either is missing.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| makecli | Pass | Pass | Warn |
| makedsl | Pass | Pass | Pass |
| make-integration | Pass | Warn | Pass |
| makeui | Warn | Pass | Pass |

The other 14 indexed listings carry no published verdicts. The two warnings are worth reading rather than dismissing: `makecli` deploys to a live platform, so any credential it holds can change real applications, and `makeui` generates frontend code across a large surface where a wrong instruction becomes shipped UI. This pack also ships 283 files, so it carries more executable helpers than a pure instruction set.

## Limitations

- Snapshot data, verified 2026-11-13: 4,749 combined installs across 18 indexed listings; 0 GitHub stars; AGPL-3.0; last pushed 2026-11-11. Counts drift over time.
- No stars and a single publisher. There is no outside review, no issue history to read and no second maintainer to catch a bad instruction.
- AGPL-3.0 is a copyleft licence. Read it against your internal redistribution and hosted-service policy before shipping anything derived from these skills.
- One index entry is named `skills/makeui`, which is a path fragment rather than a skill directory. It carries 4 installs and no content, so ignore it when counting the pack.
- The README describes each skill's role in Chinese, and the per-skill usage notes that make the routing table usable have no English counterpart in the repository.
- Several skills are written against `@qfei-design` packages (canvas-table, make-app-actions, make-app-mobile, make-ai-assistant) that must be installed in the app itself. The skill covers the integration contract, not the package.
- The whole pack is Make-specific. The routing discipline transfers to other automation platforms; the commands, DSL and component APIs do not.

## Related

- [Ziniao Skills - ERP and Store Automation Setup](/hermes/skills/catalog/ziniao-open-skills-setup)
- [firecrawl-workflows - Growth & Research Automation Setup](/hermes/skills/catalog/firecrawl-workflows-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `make-env-setup` and run it first. Every other skill in the pack assumes the toolchain and login it establishes.
- Stay on `main` unless you are actively testing the pack. A beta skill that changes behaviour under an agent is harder to debug than one that is simply absent.
- Give the agent the routing table's keywords, not the skill names. The README is built so that a task description selects the right skill, and forcing a skill by name skips the boundary rules.
- When a task crosses more than two skills, ask for the plan before the code. These contracts interact on purpose, and a page built without the permission skill has to be rebuilt rather than patched.
- Keep `makecli` credentials out of the agent's context. Let the CLI hold the token and have the agent call commands, rather than pasting a token into a prompt.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
