---
title: "Turborepo Skill - Monorepo Build System Setup"
description: "vercel/turborepo: 87.6K combined installs. The official Turborepo skill for turbo.json pipelines, caching, Remote Cache, filters and CI workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/turborepo-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "turborepo", "monorepo", "vercel", "build"]
---

# Turborepo Skill - Setup Guide

**Source:** [vercel/turborepo](https://www.skills.sh/vercel/turborepo) via skills.sh - 87.6K combined installs across 1 indexed listing; first documented 2026-11-03 (nightly sweep)

**GitHub:** [vercel/turborepo](https://github.com/vercel/turborepo) - 31,299 stars, MIT, branch main, last pushed 2026-11-02; one skill directory at `skills/turborepo/` holding a single 26-line `SKILL.md`, in a repository whose build engine is Rust (`Cargo.toml`, `crates/`) and whose published CLI is the `turbo` npm package

**Category:** Monorepo build system: task pipelines, caching, Remote Cache, filtering, environment variables and CI, documented for agents inside the repository it governs

**Quality Tier:** 🟢 Green - the single sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE file

This is the skill Vercel ships inside its own monorepo, and its README opens with a sentence that reframes the product: "Turborepo is the build system for coding agents." The skill takes that literally. It is 26 lines long, it contains no turbo.json example, and it does not attempt to teach the pipeline syntax. Instead it tells the agent that the complete documentation ships inside the installed `turbo` package and gives it the path to read.

That omission is the design. Turborepo's task graph, cache inputs and flag surface change between releases, and a skill that reproduced the documentation would be wrong at some version. By pointing the agent at `node_modules/turbo/docs/README.md` and telling it to read the bundled copy for the installed version, the skill stays correct by staying empty. It also tells the agent not to trust it: "Do not rely on this skill for framework guidance. Always read the bundled docs, which match the installed version exactly."

The repository behind it is a real monorepo with a Rust core. Turborepo's engine compiles to a native binary, the npm package is a wrapper around it, and `packages/turbo` carries `copy-docs.js` and `docs-index.md`, with `docs` listed in the package `files` field and `prepack` running the copy. That is the mechanism the skill depends on, and it is why the workflow it prescribes works at all: the index the agent reads is the one assembled at publish time for that exact version.

## Installation

The skill installs through skills.sh by repository and skill name, which is how the single indexed listing is published:

```bash
npx skills add vercel/turborepo --skill turborepo
```

For a Hermes profile, the manual route is a sparse clone plus a copy. The whole skill is one directory with one file:

```bash
git clone --depth 1 https://github.com/vercel/turborepo.git /tmp/turborepo
cp -r /tmp/turborepo/skills/turborepo ~/.hermes/profiles/corpusiq/skills/
```

The skill only becomes useful once `turbo` is installed in the project the agent is working on, because the documentation it reads lives there:

```bash
npm install turbo --save-dev
ls node_modules/turbo/docs/README.md
```

For a global install rather than a project dependency, `npm install -g turbo` also works, but the docs lookup path in the skill assumes the project layout and resolves the package location when it does not find it there. On a non-flat `node_modules` layout, a pnpm workspace for example, the skill's first instruction is to resolve the real path:

```bash
node -p "require.resolve('turbo/package.json')"
```

Read `docs/README.md` relative to whatever that prints. The skill also covers the case where `turbo` is absent: inspect the repository's package manager and existing version constraints before adding it, rather than pinning the newest release into a workspace that is deliberately behind.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| turborepo | 87,555 | Configuring and troubleshooting Turborepo repositories: turbo.json, task pipelines, caching, Remote Cache, the turbo CLI, filtering, environment variables, package boundaries, monorepo structure and CI workflows. |

No indexed listings fall below the threshold; the single listing appears above.

The 26 lines do four things, and each one is worth knowing before you rely on it. First, it routes: the agent reads `node_modules/turbo/docs/README.md` and uses that task index to choose the smallest relevant page. Second, it scopes: read the page before changing Turborepo configuration, package scripts or CI workflows, which is the opposite of guessing at a cache key. Third, it handles the workspace resolution problem above. Fourth, it defers: if `turbo` is not installed, inspect the repository before adding it, then read the bundled docs rather than guidance written for a different release.

The skill's own description lists the trigger surface, and it is broader than the file: `turbo.json`, task pipelines, caching, Remote Cache, the `turbo` CLI, filtering, environment variables, package boundaries, monorepo structure and CI workflows. That description is what the router matches on, which is why a skill this small still gets selected for a question about `--filter` syntax.

## Why This Matters for Hermes Agents

A monorepo is where an agent's confidence does the most damage. Change one `turbo.json` field and the cache can silently stop hitting, or start hitting when it should not, and the symptom shows up as a stale build an hour later rather than as an error. A skill that recites the config format cannot tell you what your installed version accepts. One that forces a read of the version-matched docs can.

The self-limiting shape is the more transferable lesson. Most published skills are written to be complete, and completeness is what makes them expire. This one is written to expire gracefully: it holds routing logic and one version-resolution trick, and every factual claim about Turborepo lives in the package the user actually installed. If Vercel changes the cache inputs next quarter, this skill is still correct, because it never made a claim it would have to retract.

For Hermes agents specifically, the bundled docs are also a context win. `node_modules/turbo/docs/` is a task index over many short pages, so the agent can pull the one page about `--filter` or `outputs` instead of a 200-line skill that covers everything and buries the answer. On a repository that sells itself on build speed, teaching the agent to read the smallest relevant page is the same discipline applied to context.

## Usage

| You say | What happens |
|---|---|
| "Why is my turbo build not hitting the cache?" | The skill sends the agent to the bundled cache documentation, then to the config page for the installed version, so inputs, outputs and env declarations are checked against this release rather than a remembered one. |
| "Add a build pipeline for the new package" | It reads the task pipeline docs from `node_modules/turbo/docs/`, then edits `turbo.json` with the `dependsOn` and `outputs` keys that release supports. |
| "Set up Remote Cache for the team" | It follows the Remote Cache page, which covers authentication and the token plumbing, instead of inventing a workflow from memory. |
| "Run the tests only for packages affected by this change" | It reads the filtering page and uses `--filter` against the changed packages, with the syntax of the installed CLI. |
| "Our CI passes locally but fails in the pipeline" | It works through env variables, cache divergence and task ordering using the CI and environment documentation bundled with the package. |
| "Is turbo even installed here?" | It runs `node -p "require.resolve('turbo/package.json')"`, and if that fails, inspects the package manager and version constraints before proposing an install. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/vercel/turborepo/main/skills/turborepo/SKILL.md
```

The skill is short enough to read in full, which is the fastest verification there is:

```bash
git clone --depth 1 https://github.com/vercel/turborepo.git /tmp/turborepo
wc -l /tmp/turborepo/skills/turborepo/SKILL.md
head -4 /tmp/turborepo/skills/turborepo/SKILL.md
```

That should print 26 lines, with `name: turborepo` and the pipeline-and-cache description on the first two. The claim that matters is the one about the bundled docs, and it is easy to check in the published package:

```bash
TURBO_PKG=$(node -p "require.resolve('turbo/package.json')")
ls "$(dirname "$TURBO_PKG")/docs/README.md"
```

If that `ls` fails, the installed `turbo` predates the docs bundling and the skill's central instruction will not resolve. In that case upgrade `turbo` rather than installing the skill into a repository that cannot satisfy it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| turborepo | Pass | Pass | Pass |

One listing, three passes, and an MIT licence, which is about as simple as this section gets. The skill is 26 lines of Markdown that instructs an agent to read files inside `node_modules` and, in one branch, to consider installing a package.

That branch is the only thing to watch. The skill tells the agent to inspect the repository's package manager and existing version constraints before adding `turbo`, which is the right instruction but still an instruction to install software. In a Hermes profile with broad tool access, an agent that reads "add turbo" as permission to install the latest release can move a pinned monorepo forward without meaning to. Keep dependency changes behind the same review you would give a human's pull request.

Reading files inside `node_modules` carries no execution risk, and the docs are static Markdown. The repository's own disclosure route is worth noting for completeness: Vercel asks that vulnerabilities go to `security@vercel.com` rather than a public issue, and points at `security.vercel.com`.

## Limitations

- Snapshot data, verified 2026-11-03: 87,555 combined installs across 1 indexed listing; 31,299 GitHub stars; MIT; last pushed 2026-11-02. Counts drift over time.
- There is exactly one listing, so the 87.6K figure is that one skill's count rather than a suite total. There is no narrower variant to fall back on if the router misses the trigger.
- The skill is a router to documentation, not documentation. It contains no turbo.json example, no flag reference and no cache key guidance; without the bundled docs it is close to useless.
- It depends on a package feature. The `docs` directory only exists in `turbo` releases that ship it, so an older install on the machine breaks the central instruction.
- Nothing here is Turborepo-specific in the framework sense. The skill says so itself: do not rely on it for framework guidance, read the bundled docs instead.
- It is written for the monorepo it lives in. A workspace with unusual layout or a package manager that hoists differently may need the `require.resolve` step before anything else works.

## Related

- [Nx AI Agents Config - Monorepo Agent Skills Setup](/hermes/skills/catalog/nx-ai-agents-config-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Gemini CLI Skills - Repository Workspace Pack](/hermes/skills/catalog/gemini-cli-skills-setup)
- [Fallow Skills - Codebase Intelligence for TS and JS Setup](/hermes/skills/catalog/fallow-rs-fallow-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `turbo` in the project before installing the skill. The skill's whole value is a path into `node_modules/turbo/docs/`, and without the package there is nothing at that path.
- Ask for the smallest relevant page rather than "the Turborepo docs". The bundled `README.md` is a task index, and reading one page keeps the context budget for the actual change.
- Resolve the package before reading when the workspace is pnpm or otherwise non-flat. `node -p "require.resolve('turbo/package.json')"` is the one line that makes the rest work.
- Never hand-edit a cache key from memory. Cache inputs and `outputs` are version-sensitive, and a wrong `outputs` glob is the classic cause of a build that passes locally and fails in CI.
- Treat a suggested `turbo` install as a dependency change, not a fix. The skill's own instruction is to check existing constraints first, and that instruction is there for a reason.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
