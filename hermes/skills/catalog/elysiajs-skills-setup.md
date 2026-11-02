---
title: "ElysiaJS Skill - Bun Web Framework Setup"
description: "elysiajs/skills: 14.5K combined installs. One Elysia v2 skill for Bun backends: routing, validation, plugins, Eden types and deployment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elysiajs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "elysiajs", "bun", "typescript", "api development"]
---

# ElysiaJS Skill - Setup Guide

**Source:** [elysiajs/skills](https://www.skills.sh/elysiajs/skills) via skills.sh - 14.5K combined installs across 1 indexed listing; first seen 2026-11-02 (morning sweep)

**GitHub:** [elysiajs/skills](https://github.com/elysiajs/skills) - 70 stars, no license file in the repository, branch main, last pushed 2026-10-19; 1 `SKILL.md` at `elysia/SKILL.md` with 23 reference pages in `elysia/references/` and a `metadata.json` manifest

**Category:** Bun-native API development for agents: Elysia routing, validation, plugins and Eden end-to-end types

**Quality Tier:** 🟡 Yellow - a clean audit and a well-indexed skill, but there is no license file, no README, and only 70 stars behind a framework still in beta

This is a single-skill repository published by the ElysiaJS organisation: three entries at the root, a `.gitignore`, a `.prettierrc` and an `elysia/` folder. There is no README, no build step and no test suite in the repository, because the repository is documentation and nothing else. The whole artifact is `elysia/SKILL.md` at 89 lines, 23 reference pages under `elysia/references/`, and a `metadata.json` that records the version, the organisation and the baseline the guidance was checked against.

The skill describes Elysia v2, the TypeScript framework built around Bun, and it is written to be read in slices rather than loaded whole. The `SKILL.md` opens with four instructions: inspect `package.json`, the lockfile, the runtime and the app structure and keep the project's existing versions; treat the guidance as 2.0.0-rc.0 or newer and refuse to upgrade a v1 project unless the user asks; read only the references the task needs; then check types and exercise the affected route including its rejection path. After that it states the rules that catch agents out, and closes with a minimal app plus a `bun:test` file that opens no port, and a task-to-reference index for the 23 pages.

## Installation

There is no README in this repository and therefore no documented install command. The generic skills.sh CLI path is the one to use, and it writes the skill into whichever agent it detects:

```bash
npx skills add elysiajs/skills
```

The manual route is the same copy it always is, with one detail worth knowing: the folder is named `elysia` while the skill's `name` field is `elysiajs`, so the directory on disk and the skill the runtime routes on do not share a spelling.

```bash
git clone --depth 1 https://github.com/elysiajs/skills.git /tmp/elysiajs-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills/elysia
cp -R /tmp/elysiajs-skills/elysia/. ~/.hermes/profiles/corpusiq/skills/elysia/
```

Copy the folder contents, not just `SKILL.md`. The 89-line skill links all 23 reference pages, so a copy without them leaves the agent holding rules with no detail behind them.

Nothing else has to be installed for the skill to load. To use what it describes you need a project on Elysia v2 with Bun, since the skill defaults new projects to Bun and `t` schemas, and `references/runtimes.md` covers Node, Deno, Workers and frontend integration for projects that are not on Bun. Node specifically needs `@elysia/node` and Node 22.18 or newer, which the skill states as a rule rather than an option.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| elysiajs | 14,474 | Building, debugging and migrating Elysia v2 backends: route options before the handler, keeping the inferred type when you chain or rebind, hook order around `.use()`, typed dependencies per plugin, `status()` and `problem()` for expected failures, `UnwrapSchema` and `UnwrapModels` for inferred types, `decorate` and `state` versus per-request `derive`, `schema: 'merge'` on guards, optional capabilities such as WebSockets, file MIME detection and the Node adapter, plus a `bun:test` route test that opens no port. |

No indexed listings fall below the threshold; the single listing above is the whole index.

The 23 references are the substance, and the skill's own index maps a task to a page: core API, lifecycle, composition and plugins, validation, errors, project structure, cookies, WebSockets, testing, Eden typed clients, OpenAPI, runtimes, deployment, observability, the official plugins (CORS, JWT, static files, cron, HTML, GraphQL), Drizzle, Prisma, Better Auth, the AI SDK, React Email, migration from v1, a pattern index, and versions. `metadata.json` adds the provenance record: version 2.0.0, organisation ElysiaJS, dated 17 Oct 2026, with the abstract "Elysia v2 backend guidance, checked against 2.0.0-beta.32".

## Why This Matters for Hermes Agents

Elysia's type system is the point of the framework and the thing an agent most easily breaks. The route type is inferred from the handler's return value, so reassigning `let app = new Elysia()` widens it and silently destroys Eden's end-to-end types; the same is true of pulling handlers out into loose functions. Those are not syntax errors, they are type regressions that surface three files later, and the skill states them as rules with the reason attached, which is what an agent needs to avoid reproducing the mistake it has seen in older training data.

The second class of failure is registration order. Elysia hooks fire in the order they are registered relative to routes and `.use()` calls, and `onRequest` is the documented exception. An agent that adds an auth hook after the routes will produce a server that looks correct and authenticates nothing on the routes already mounted. `references/lifecycle.md` is the page that explains it, and the skill's rule points there before the agent writes the hook.

Version drift is the third. Elysia v2 changed signatures from v1, and the ecosystem is mid-beta with independent plugin beta numbers, so a model working from v1 examples produces code that type-checks against the wrong major. The skill's first instruction is to read the manifest and lockfile and keep existing versions, which turns a silent upgrade into a decision, and `references/migration.md` exists to recognise the differences rather than to authorise an upgrade.

For a builder, that adds up to a skill that behaves like a careful colleague on a pre-1.0 framework: read the project first, keep the types, get the hook order right, test the rejection path. The last part is worth copying elsewhere. The minimal test in the skill calls `app.handle()` instead of listening on a port and asserts both the 200 and the 422, so the failure case is exercised in the same test as the success.

## Usage

| You say | What happens |
|---|---|
| "Add a GET route for /users/:id with a numeric param" | Writes the route with a `t.Object` params schema, keeps the handler inline so the return type stays inferred, and exports `typeof app` for Eden. |
| "My Eden client lost all its types after a refactor" | Traces the widening: a reassigned `let app`, a handler moved out of the chain, or a child instance that does not `.use()` its own providers. |
| "Add an auth hook to this API" | Registers the hook before the routes and before `.use(child)`, and explains that `onRequest` is the one hook that runs before routing. |
| "Validate the upload is a PNG" | Uses the validation reference for schema coercion and notes that file MIME validation needs a detector registered as an optional capability. |
| "Return a 404 instead of throwing" | Uses `status()` or `problem()` for an expected failure, because a returned value is part of the route's inferred type while a thrown error is not. |
| "Write a test for this route" | Writes a `bun:test` case that calls `app.handle()` with no port open and asserts the success status and the rejection status. |
| "We are on Elysia 1, should we upgrade?" | Reads the migration reference to recognise the differences and leaves the upgrade decision to you, since the skill explicitly refuses to treat migration notes as permission. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/elysiajs/skills/main/elysia/SKILL.md
```

After a clone, confirm that the references came with the skill. This is the check that matters, because a copy holding only `SKILL.md` looks installed and behaves badly:

```bash
git clone --depth 1 https://github.com/elysiajs/skills.git /tmp/elysiajs-skills
find /tmp/elysiajs-skills -name SKILL.md | wc -l
ls /tmp/elysiajs-skills/elysia/references | wc -l
head -4 /tmp/elysiajs-skills/elysia/SKILL.md
```

The first count should print 1, the second 23, and `head` should show `name: elysiajs` and the description the runtime routes on. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/elysia/references | wc -l
grep -c 'references/' ~/.hermes/profiles/corpusiq/skills/elysia/SKILL.md
```

The reference count should still be 23, and the grep should return a non-zero number of pointers, which confirms the skill can still reach its detail.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| elysiajs | Pass | Pass | Pass |

The one sampled listing passes all three auditors, with no Warn or Fail to report. The repository contains no executable code at all: `SKILL.md`, 23 Markdown references, a `metadata.json` and a `.prettierrc`. There is no install script, no hook, no dependency and nothing that runs when the skill is loaded.

The repository also has no license file, so there is no explicit grant to copy, republish or redistribute the text. The folder is public and indexed on skills.sh, but the skill text itself carries no license, which matters if you intend to mirror it rather than install it into a profile.

What the skill does change is the code the agent writes. It teaches a pre-1.0 framework whose packages are published as bets: `references/versions.md` warns that the review used a local checkout with uncommitted source changes, that the commit alone does not reproduce the reviewed tree, and that the listed package versions do not prove release availability or end-to-end compatibility. Treat every version it names as a claim to check against the registry before pinning production dependencies, and read the validation and error pages before letting an agent expose error detail, since the skill notes that explicit error details can remain public in production.

## Limitations

- Snapshot data, verified 2026-11-02: 14,474 combined installs across 1 indexed listing; 70 GitHub stars; no license file; last pushed 2026-10-19. Counts drift over time.
- No license file exists in the repository, so reuse of the skill text has no explicit grant even though it is publicly indexed.
- There is no README at all. The installation is the generic `npx skills add` path, and the only documentation is `SKILL.md` plus the 23 references, so there is nothing describing compatibility, support or who maintains it.
- The version story is internally inconsistent. `SKILL.md` says it describes 2.0.0-rc.0 or newer, while `metadata.json` and `references/versions.md` record a review on 2026-10-17 against a local checkout declaring 2.0.0-beta.32, with uncommitted source changes present. That review also states the commit alone does not reproduce the reviewed tree.
- The folder is `elysia/` while the skill name is `elysiajs`. A copy-by-folder-name install lands under a different name than the one the description advertises, which is worth knowing when you are debugging why a skill did not load.
- One skill and one maintainer surface at 70 stars. The skill is a guide to the framework's own documentation and says so, recommending `elysiajs.com/llms.txt` for v1 and `next.elysiajs.com/llms.txt` for v2 rather than presenting itself as the source of truth.

## Related

- [M. Collina Node Skills - Fastify & Node.js Agent Suite Setup](/hermes/skills/catalog/mcollina-node-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [NestJS Best Practices - 40-Rule Agent Skill Setup Guide](/hermes/skills/catalog/agent-nestjs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Point the agent at one reference page per task instead of hoping it reads all 23. The task-to-reference index at the end of `SKILL.md` is the map, and a request like "add WebSocket routes" should land on `references/websocket.md`, not on the core API page.
- Ask for the type check and the rejection-path test in the same breath. The skill's rule is to exercise the route including its rejection path, and in practice that means a 422 assertion next to the 200 in one `bun:test` case.
- When Eden loses its types, look for a widened instance before you look at the client. A reassigned `let app`, a handler lifted out of the chain, or a child that skipped `.use()` are the three causes the skill names.
- Pin the framework version in the project and leave it alone. `references/versions.md` says to prefer the installed release's source and tests over conflicting docs, which is the right tiebreak for a beta.
- Read `references/errors.md` before production. The distinction between a returned error and a thrown one decides what ends up in the route's inferred type and what can leak into a response.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
