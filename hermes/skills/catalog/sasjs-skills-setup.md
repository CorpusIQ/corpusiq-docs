---
title: "SASjs Skills - SAS and Analytics Pipeline Setup"
description: "sasjs/skills on skills.sh: 9.3K combined installs across 8 listings; SAS language, core macros, CLI, adapter and server skills for SASjs projects."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sasjs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "sas", "analytics", "cli"]
---

# SASjs Skills - Setup Guide

**Source:** [sasjs/skills](https://www.skills.sh/sasjs/skills) via skills.sh - 9.3K combined installs across 8 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 3 stars, MIT licence, last pushed 2026-11-03, 8 skill directories at the repository root
**Category:** SAS language and SASjs toolchain for agents: pure SAS, core macros, CLI, adapter, framework, lint, server and package management
**Quality Tier:** 🟡 Beta - Snyk Warn on sasjs-server; MIT; 3 stars.

SAS is still the substrate under a large share of regulated analytics, and its tooling has a documentation problem for agents: the language reference, the SASjs CLI, the macro library and the server wrapper are four different knowledge domains that a general model blurs together. This repository ships eight skills, one per domain, so an agent loads the one that matches the question instead of a summary of all of them.

The split is deliberate. `sas` covers the language only, DATA step, PROC SQL, macro language, formats and ODS, and states explicitly that it contains no SASjs framework content. The rest cover the ecosystem: `sasjs-core` for the `@sasjs/core` macro library and its coding standards, `sasjs-cli` for create, compile, build, deploy, run and test workflows, `sasjs-framework` for full application structure and `sasjsconfig.json`, `sasjs-adapter` for calling SAS services from TypeScript or JavaScript, `sasjs-server` for the NodeJS wrapper around the SAS binary, `sasjs-lint` for the `.sasjslint` rule set, and `sas-packages` for the SAS Packages Framework and the SASPAC archive.

## Installation

The README installs the whole collection:

```bash
npx skills add sasjs/skills
```

Individual skills install by appending `@<skill-name>`, and there is a preview command that generates a prompt for one skill without installing it:

```bash
npx skills add sasjs/skills@sasjs-core
npx skills use sasjs/skills@sas
```

The README also documents the housekeeping commands:

```bash
npx skills list
npx skills update
npx skills remove sasjs-core
```

The skills are agent-agnostic, each one a folder with a `SKILL.md`. The installer writes them to the standard `.agents/skills/` directory, which VS Code Copilot auto-discovers, and the README suggests committing that folder so a whole team picks the skills up. Copilot also checks `.github/skills/` if you prefer that location.

## What It Provides

Eight listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| sas | 1,253 | Pure SAS language work: DATA step, PROC SQL, macro language, formats, ODS and common procedures, with no SASjs framework content |
| sasjs-server | 1,249 | Installing, configuring and running @sasjs/server, with desktop and server modes, SAS/JS/Python/R runtimes, env vars, LDAP auth and the REST API |
| sasjs-core | 1,248 | Working in a sasjs/core style repo: the prefixed macro families (mf_, mp_, mm, ms_, mv_), picking an existing macro over reinventing one, and the build, lint and doxygen conventions |
| sasjs-cli | 1,246 | Using @sasjs/cli to create, compile, build, deploy, run and test projects against SAS 9, Viya and SASjs server targets |
| sasjs-framework | 1,245 | Building full SASjs applications: project layout, sasjsconfig.json, services, jobs and macros folders, multi-target configuration and streaming frontends |
| sasjs-adapter | 1,245 | Frontend and Node integration with @sasjs/adapter: the request call and response shape, auth per server type, file upload and session management |
| sas-packages | 969 | Installing, loading and unloading SAS packages with the SAS Packages Framework and SASPAC, including fileref rules and version pinning |
| sasjs-lint | 812 | Linting and formatting SAS with @sasjs/lint: .sasjslint rules, macro-declaration rules, banned strings, severity levels and exit codes |

No indexed listings fall below the threshold; all 8 appear above.

## Why This Matters for Hermes Agents

SAS code fails in ways that look correct. A missing `%local` leaks a macro variable into a wider scope, a hardcoded fileref collides with another process, a macro call terminated with a semicolon emits a stray statement. These are exactly the conventions `sasjs-core` states as mandatory rules: one macro per file with a matching filename, parentheses on `%macro` definitions, no semicolon on macro calls, every macro variable declared `%local`, unique filerefs through `mf_getuniquefileref`, and a Doxygen header on every file.

The `sas` skill keeps the language separate for a reason. An agent asked a PROC SQL question should not be reasoning about `sasjsconfig.json`, and a skill that mixes both produces answers that are half framework and half language. Scoping it to pure SAS means the trigger is precise and the content is dense.

The ecosystem skills then cover the delivery path. `sasjs-cli` handles the compile, build, deploy and test cycle against three different target types, `sasjs-framework` covers the project contract, and `sasjs-adapter` covers the browser and Node side. For a team running SAS behind a web front end, that is the whole chain an agent needs before it can change anything safely.

`sasjs-lint` is the quiet win. A linter with a documented rule set and exit codes gives an agent a pass or fail signal, which is far more useful than asking it to judge SAS style by eye.

## Usage

| You say | What happens |
|---|---|
| "Why does this DATA step lose the last record in each BY group" | sas reads the language reference and checks the first. and last. indicators in the DATA step |
| "Write a PROC SQL join that works on Viya" | sas produces idiomatic SAS with the appropriate SQL dialect and no framework content |
| "Add a macro to our sasjs/core repo" | sasjs-core applies the coding standards and the correct macro prefix and header |
| "Compile just this file and deploy to the Viya target" | sasjs-cli runs the single-file compile then the deploy for that target |
| "Set up a new SASjs app with two targets" | sasjs-framework scaffolds the project structure and sasjsconfig.json |
| "Call our SAS service from the React front end" | sasjs-adapter shows the request call, response shape and session handling |
| "Lint the SAS folder and fail the build on errors" | sasjs-lint runs the configured rules and returns the documented exit code |
| "Install the sasjscore package into this session" | sas-packages walks the SPF install and load sequence with the fileref rules |

## Verification

Read the language skill before installing, since its description is the trigger:

```bash
curl -fsSL https://raw.githubusercontent.com/sasjs/skills/main/sas/SKILL.md | head -6
```

It should open with `name: sas`, a description naming the DATA step, PROC SQL and macro language, and an MIT licence line. The other skill directories sit at the repository root rather than under `skills/`, so the same pattern works for any of them:

```bash
curl -fsSL https://raw.githubusercontent.com/sasjs/skills/main/sasjs-core/SKILL.md | head -4
```

After installing, check the directory the README says the installer targets:

```bash
ls .agents/skills | grep -E 'sas|sasjs'
```

Eight directories should appear. Confirm the installer's view of what it owns:

```bash
npx skills list
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sas | Pass | Pass | Pass |
| sasjs-server | Pass | Pass | Warn |
| sasjs-framework | Pass | Pass | Pass |

`sasjs-server` carries the only Warn in the sample, and it is the skill that deals with environment variables, LDAP authentication and a REST API in front of a SAS binary. Read that one before letting an agent change server configuration, and keep credentials in the environment rather than in `sasjsconfig.json`.

## Limitations

- Snapshot data, verified 2026-11-05: 9,267 combined installs across 8 indexed listings; 3 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- The repository is young and small at 3 stars, though it is actively pushed. Treat these skills as a well-scoped draft rather than battle-tested guidance.
- Six of the eight listings sit within eight installs of each other, which reads like a single sweep snapshot rather than independent adoption. Do not read the ranking as a quality signal.
- The skills are instruction sets. Nothing here installs SAS, the SASjs CLI or a server target, and most workflows assume access to SAS 9, Viya or a SASjs server.
- `sasjs-server` carries a Snyk Warn, and configuring it involves env vars, LDAP auth and runtime selection. Review changes to a running server by hand.
- Skill directories live at the repository root, not under a `skills/` folder, so any tooling that assumes the common `skills/<name>/SKILL.md` layout needs adjusting.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup)
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per skill on a large repo. `npx skills add sasjs/skills@sasjs-cli` keeps the descriptions that compete for attention down to the ones the project actually uses.
- Preview before installing with `npx skills use sasjs/skills@sas`. It generates the prompt without writing a directory, which is enough to judge whether a skill covers your question.
- Name the skill explicitly in Copilot Auto mode. The README's own tip is that "using the sasjs-cli skill, deploy this to my Viya target" works regardless of which model handles the turn.
- Commit `.agents/skills/` so the team shares one copy. Skills that live only in a home directory drift per developer.
- Read `sasjs-core` before writing macros. Its standards are mandatory in that repo, and a macro without `%local` declarations or a unique fileref is the most common review rejection.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
