---
title: "Prisma Next Skills - Typed Database Access Setup"
description: "prisma/prisma-next: 23.9K combined installs. Agent skills for Prisma Next contracts, migrations, query lanes, runtime wiring and Supabase RLS."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/prisma-next-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "prisma", "database", "migrations", "typescript"]
---

# Prisma Next Skills - Setup Guide

**Source:** [prisma/prisma-next](https://www.skills.sh/prisma/prisma-next) via skills.sh - 23.9K combined installs across 40 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [prisma/prisma-next](https://github.com/prisma/prisma-next) - 411 stars, Apache-2.0 License, branch main, last pushed 2026-08-25; 31 `SKILL.md` files across two trees, `skills/<name>/SKILL.md` for 13 product skills (11 in the routed cluster, plus `skills/upgrade/` and `skills/extension-author/`) and `skills-contrib/<name>/SKILL.md` for 18 contributor workflow skills, with `skills/journey-tests/` holding 16 worked walkthroughs and `drive/` holding project-context memory for Drive skills whose canonical bodies live outside this tree

**Category:** Database schema, migrations and typed query access for agents

**Quality Tier:** 🟡 Beta - 1 sampled Warn verdict(s), the Snyk Warn on draft-release-notes; Apache-2.0, typed Postgres, SQLite and Mongo access from contract authoring through migration review

Prisma is the company behind Prisma ORM, and `prisma/prisma-next` is where it developed Prisma Next, the early-access data layer that became Prisma ORM v8. The root README is now a single archive notice: the repository is read-only, development continues in `prisma/prisma`, the `@prisma-next/*` and `prisma-next` npm packages are deprecated, and new projects install `prisma` instead. What the archive still holds intact is the agent layer: 31 `SKILL.md` files, 13 product skills under `skills/` and 18 contributor workflow skills under `skills-contrib/`.

The product cluster is a routed suite rather than a pile of prompts. `prisma-next` catches vague requests and routes them; `prisma-next-quickstart` handles adoption on a greenfield project or an existing database; `prisma-next-contract` edits the data contract; `prisma-next-migrations` and `prisma-next-migration-review` split authoring from deploy review; `prisma-next-queries`, `prisma-next-runtime` and `prisma-next-build` cover the query lanes, the `db.ts` wiring and the Vite plugin; `prisma-next-debug` reads the structured error envelope; `prisma-next-supabase` covers RLS and role binding; `prisma-next-feedback` hands a question to the team. Every file follows the same shape - mental-model headline, When to Use and When Not to Use, Key Concepts, Workflow, Common Pitfalls, What Prisma Next doesn't do yet, Reference Files, Checklist - and the skills README explains why that last section matters: Prisma Next is `0.x`, so each skill names the features the framework does not implement, gives the workaround, and routes the request to `prisma-next-feedback`, which gives the agent something concrete to say instead of confabulating a plausible API call against a method that does not exist.

## Installation

The root README carries no skills-install path, because it is an archive notice; the install commands live in `skills/README.md` in the same tree. That file's preferred route is the project initializer, which installs the cluster for you in the current working directory:

```bash
mkdir my-app && cd my-app
pnpm dlx prisma-next init
```

Standalone, into an existing project or a runtime added after `init`, `--all` installs every skill in the cluster for every agent runtime the CLI detects, without prompting per skill or per agent:

```bash
pnpm dlx skills add prisma/prisma-next#v<your-prisma-next-version> --all
```

To bind the cluster to one runtime instead, the README swaps `--all` for `--skill '*' -a <agent>`, naming `claude-code`, `cursor` and `codex` as examples:

```bash
pnpm dlx skills add prisma/prisma-next#v<your-prisma-next-version> --skill '*' -a codex
```

Two statements in that README decide the Hermes route. The install is always project-level, because the cluster's surface tracks the project's `@prisma-next/*` version and a host-wide install would have to pick a single version for every project on the host. The git ref is meant to match the runtime, so a project on Prisma Next `0.8.0` installs from `prisma/prisma-next#v0.8.0`. Neither rule blocks a profile-level copy, but it does make the copy a snapshot: take `skills/<name>/` from a clone of the ref your project pins and place it at `~/.hermes/profiles/corpusiq/skills/<name>/`, one directory per skill, and re-copy when the project's `@prisma-next/*` version moves.

Copy the directory and not the markdown alone. The two upgrade skills ship real codemods, 10 per-transition directories each (`upgrades/0.7-to-0.8` through `upgrades/0.16-to-0.17`) holding `.ts` and `.mjs` transforms, and the three review-phase contributor skills ship `scripts/` with `.mjs` validators plus a `package.json`, two of them with `agents/` as well.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prisma-next | 2,098 | Router for vague Prisma Next prompts: asks what you are trying to do, hands off to the specific sibling skill, answers what Prisma Next is and comparison questions such as Prisma Next versus Drizzle, and carries an explicit do-not-use list for prompts that already name a workflow. |
| prisma-next-migrations | 2,085 | Migration authoring: choosing `db update` versus `migration plan`, replacing the framework's placeholder sentinels in the rendered `migration.ts` with `dataTransform` closures, and recovering from MIGRATION.HASH_MISMATCH or an unfilled PN-MIG-2001 placeholder. |
| prisma-next-queries | 2,071 | Writing Postgres, SQLite and Mongo queries: lane selection between `db.orm.<Model>` plus `db.sql.<table>` and the Mongo `db.query.from(...)` pipeline builder, filters, projections, sorting, pagination, `.include(...)` eager loads, transactions and aggregates. |
| prisma-next-migration-review | 2,055 | Answering what migrations will run on merge or deploy: rendering the migration graph, resolving concurrent and diamond-convergence conflicts, MIGRATION.DIVERGED and missing-marker errors, and environment refs for CI. |
| prisma-next-debug | 2,055 | Reading a structured error envelope (code, domain, severity, why, fix, meta) and routing to recovery for hash mismatches, row and time budgets, planner conflicts, schema drift, and scripts that will not exit because the pool was never closed. |
| prisma-next-runtime | 2,054 | Wiring `db.ts`: the `postgres<Contract>(...)`, `sqlite<Contract>(...)` and `mongo<Contract>(...)` factories, middleware composition for telemetry, lints and budgets, DATABASE_URL handling, per-environment branching, and disposal through `db.close`, `db.end` or `await using`. |
| prisma-next-build | 2,051 | Build-system and dev-server integration: the Vite plugin for contract emit on save and HMR, while Next.js, Webpack, esbuild, Rollup and Turbopack are named as gaps rather than fabricated. |
| prisma-next-contract | 2,049 | Editing the data contract: models, fields, relations, indexes, enums, value objects, namespaces, cross-contract foreign keys, polymorphic types, extension namespaces such as pgvector, `prisma-next.config.ts` wiring and `prisma-next contract emit`. |
| prisma-next-quickstart | 2,045 | Adoption: greenfield `prisma-next init`, brownfield `contract infer` plus `db sign`, the connect-write-read first arc, and the day-to-day command set before routing onward to a specialist skill. |
| prisma-next-feedback | 2,033 | Turning a gap or a bug into a tracked artifact: filing a GitHub issue for a bug or feature request, and routing Q&A, design feedback and direct-team questions, extension authors included, to the Prisma Discord. |
| prisma-next-upgrade | 1,379 | Upgrading Prisma Next in an application: bumping every `@prisma-next/*` dependency, applying the per-transition code translation, validating with the project's own typecheck and tests, and committing one minor step at a time. |
| prisma-next-extension-upgrade | 1,226 | The same loop for an extension package: extension SPI churn across middleware lifecycle, codec and framework-component surfaces, exact pin verification through `prisma-next-check-pins`, and per-step commits. |
| prisma-next-supabase | 678 | Supabase projects: the `@prisma-next/extension-supabase` pack, cross-space foreign keys to `supabase:auth.AuthUser`, RLS policy authoring against `auth.uid()`, role binding with `asUser` / `asAnon` / `asServiceRole`, and JWT validation through `jwksUrl` or a legacy HS256 secret. |

The remaining 27 indexed listings range from 1 to 2 installs.

## Why This Matters for Hermes Agents

A database skill that stops at "run the migration command" leaves the decisions, the ordering and the recovery path to the model, and migrations are the one part of a schema change that is expensive to get wrong. This cluster splits the job: authoring, deploy review and error recovery are three separate skills with three separate descriptions, so an agent routes to one of them instead of improvising the whole pipeline from a single prompt.

The per-transition upgrade instructions are the most reusable machinery in the repository. Each of the two upgrade skills carries 10 directories of codemods keyed by version range, which turns "bump `@prisma-next/*` to the next minor" from a model improvisation into a scripted step, a typecheck, a test run and a commit per minor.

The `What Prisma Next doesn't do yet` section is the reason this suite is safe to hand to a cron or a subagent. Capability gaps are named in the file the agent loads, with the workaround and a route to `prisma-next-feedback`, so an agent asked for Studio, lifecycle callbacks, `EXPLAIN`, prepared statements, `db.batch()` or a Next.js plugin reports the gap instead of emitting code for an API that was never built.

The structured error envelope is the second guardrail. `prisma-next-debug` treats errors as `code`, `domain`, `severity`, `why`, `fix` and `meta`, and maps the code families (PN-RUN, PN-MIG, PN-CLI, PN-SCHEMA, plus budget and planner codes) to specific recovery, which is the difference between an agent that reports a hash mismatch and one that re-runs a destructive command hoping for a different result.

## Usage

| You say | What happens |
|---|---|
| "I just scaffolded a Prisma Next app, what now?" | `prisma-next` routes to `prisma-next-quickstart`, which walks the connect-write-read first arc and names the next command rather than dumping the CLI reference. |
| "What migrations will run when this merges?" | `prisma-next-migration-review` renders the migration graph, names what would apply, and flags MIGRATION.NO_MARKER or diamond convergence before the change reaches staging. |
| "My migration keeps failing with MIGRATION.HASH_MISMATCH" | `prisma-next-migrations` explains the sentinel pattern, replaces the placeholder with a `dataTransform` closure in the rendered `migration.ts`, and re-runs `db verify` to confirm the hash. |
| "Add a polymorphic relation and a pgvector column to the contract" | `prisma-next-contract` writes the attributes and the extension namespace call, wires `prisma-next.config.ts`, and runs `prisma-next contract emit` so the type surface updates. |
| "Why does my aggregate come back null?" | `prisma-next-queries` applies the lane rules and the typing notes: `count` is a `number` while sum, avg, min and max are `number` or null, and ranges use chained `.where()` rather than `.between()`. |
| "Our RLS policy leaks rows for anonymous requests" | `prisma-next-supabase` authors the `policy_select` / `@@rls` predicate against `auth.uid()`, binds the request through `asAnon()`, and checks the JWT path, `jwksUrl` for current projects or `jwtSecret` for legacy HS256. |
| "This script will not exit after the queries finish" | `prisma-next-debug` and `prisma-next-runtime` trace the open handle through `db.close`, `db.end`, `pool.end`, `[Symbol.asyncDispose]` and `await using`, then confirm the envelope code rather than killing the process. |

## Verification

All three raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} readme\n" \
  https://raw.githubusercontent.com/prisma/prisma-next/main/skills/README.md
curl -sL -o /dev/null -w "%{http_code} migration-review\n" \
  https://raw.githubusercontent.com/prisma/prisma-next/main/skills/prisma-next-migration-review/SKILL.md
curl -sL -o /dev/null -w "%{http_code} upgrade\n" \
  https://raw.githubusercontent.com/prisma/prisma-next/main/skills/upgrade/prisma-next-upgrade/SKILL.md
```

Expect `200` three times. The README URL is worth fetching first because it holds the install route, the version-pinning rule and the cluster table in one file. The second URL shows the flat layout, and the third shows the nested one: the two upgrade skills live under `skills/upgrade/` and `skills/extension-author/` rather than directly under `skills/`, which is the layout quirk most likely to break a loop that assumes `skills/<name>/SKILL.md`.

After the copy lands in the profile, confirm the frontmatter and the shape of the directory:

```bash
head -6 ~/.hermes/profiles/corpusiq/skills/prisma-next-migrations/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/prisma-next-upgrade/upgrades | head -3
```

A good copy shows `name:` and `description:` in the frontmatter, and the upgrade skill still has its `upgrades/` tree with the per-transition directories. A missing `upgrades/` directory means the copy flattened the skill to markdown, which leaves the agent describing codemods it cannot run. The frontmatter description is the routing contract, so read it before installing: it is what the runtime matches against, and on this repository the descriptions are deliberately long, listing trigger phrases and error codes.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prisma-next | Pass | Pass | Pass |
| prisma-next-migrations | Pass | Pass | Pass |
| prisma-next-queries | Pass | Pass | Pass |
| prisma-next-migration-review | Pass | Pass | Pass |
| draft-release-notes | Pass | Pass | Warn |

No FAIL verdict appears in the sampled five. The single Warn is a Snyk verdict on `draft-release-notes`, a contributor workflow skill under `skills-contrib/` that authors the committed release-notes file for a stable release from the merged PRs since the previous tag, so it sits outside the 11-skill product cluster an application would install. That skill is prose-driven and ships no script at all, which makes the Warn worth reading rather than assuming: the pack records the verdict and not the finding behind it, so open that Snyk entry on skills.sh before pulling the contributor tree.

The read-only nature of the repository is the larger fact to weigh. `prisma/prisma-next` is archived, so a skill copied from it does not receive fixes, and the install ref `#v<your-prisma-next-version>` resolves against a frozen history. The two upgrade skills are the part to review line by line, because they instruct an agent to run bundled `.ts` and `.mjs` transforms over your working tree; the review-phase contributor skills similarly ship `.mjs` scripts that read and write review artifacts. Everything else in the tree is markdown.

## Limitations

- Snapshot data, verified 2026-10-30: 23,921 combined installs across 40 indexed listings; 411 GitHub stars; Apache-2.0; last pushed 2026-08-25. Counts drift over time.
- The repository is archived and read-only. Prisma Next development continues in `prisma/prisma` under the name Prisma ORM v8, the `@prisma-next/*` and `prisma-next` npm packages are deprecated, and the README points new projects at `npm install prisma` plus `npm create prisma@latest`. The skills describe the `@prisma-next/*` surface, which is the pre-v8 surface, so a project already on Prisma ORM v8 should read these files as history rather than as guidance.
- The install index outruns the tree. skills.sh carries 40 listings against 31 `SKILL.md` files, and the 10 `drive-*` listings (`drive-create-plan`, `drive-code-review`, `drive-agent-personas` and the rest, 1 install each) have no `SKILL.md` in this repository: `drive/README.md` places their canonical bodies at `.agents/skills/drive-*/SKILL.md`, a path this tree does not contain. The `record-gotchas` listing maps to a `skills-contrib/record-gotcha/` directory, and `skills-contrib/psl-ast-layers/` exists in the tree with no listing.
- There is no global install path. The skills README states the install is always project-level, because the cluster's surface tracks the project's `@prisma-next/*` version, so a Hermes profile copy is a pinned snapshot that has to be refreshed when the project's version moves.
- Prisma Next is early access `0.x`. Each skill's `What Prisma Next doesn't do yet` section names unbuilt features (model validations, lifecycle callbacks, Studio, runtime-apply migrations, `EXPLAIN`, prepared statements, `db.batch()`, multi-database routing, the Next.js plugin), which is honest but means a request can end at a named gap rather than working code.
- Install counts do not rank these skills. The top ten listings sit between 2,033 and 2,098 installs, which is publication noise, and the tail sits at 1 or 2. Judge a skill by its `SKILL.md` and its workflow, not by the number beside it.

## Related

- [prisma Skills](/hermes/skills/catalog/prisma)
- [supabase Skills](/hermes/skills/catalog/supabase)
- [Vinta Django AI Plugins - Django and Celery Setup](/hermes/skills/catalog/vintasoftware-django-ai-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the cluster, not one skill. The router plus the specialists is the design: `prisma-next` decides which sibling answers, and a lone specialist leaves the agent with no route for anything outside its lane.
- Match the git ref to the pinned runtime version. The README's rule is `#v<your-prisma-next-version>`, because the skills reference commands, exit codes and capability claims that track the installed `@prisma-next/*` version.
- Copy directories with `cp -r` or `rsync` and never `cp *.md`. Two skills carry codemod trees and three carry `scripts/`, and a markdown-only copy produces an agent that promises a transform it cannot execute.
- Read `prisma-next-debug` before you need it. Its error-code families (PN-RUN, PN-MIG, PN-CLI, PN-SCHEMA, budget and planner codes) are the vocabulary every other skill assumes, and pasting a code into a session routes faster than describing the symptom.
- Treat the archived status as part of the install decision. Pin the copy in your own repository or profile notes with the ref it came from, since no upstream fix will arrive for a skill taken from this tree.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
