---
title: "Astro Skills - Island Architecture for Agents"
description: "astrolicious/agent-skills on skills.sh: 19.0K combined installs across 1 listing; Astro components, config, adapters and deployment checks for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/astrolicious-astro-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "astro", "static site", "frontend"]
---

# Astro Skills - Setup Guide

**Source:** [astrolicious/agent-skills](https://www.skills.sh/astrolicious/agent-skills) via skills.sh - 19.0K combined installs across 1 indexed listing; first seen 2026-11-07 (Nov 7 2026 morning sweep)
**GitHub:** 13 stars, no license file at the repository root, branch `main`, last pushed 2026-03-20, one skill directory at `skills/astro/SKILL.md`
**Category:** Astro work for agents: island architecture, content collections, view transitions and static deployment checks
**Quality Tier:** 🟡 Yellow - all three scanners pass, but the repository carries no LICENSE file, has 13 stars, and ships a single 140-line `SKILL.md` with no reference tree behind it.

The astrolicious repository is the narrowest possible distribution of a framework skill: one directory, one `SKILL.md`, and a README that is nothing but a credits list. The skill's frontmatter declares `name: astro`, `license: MIT`, `authors: "Astro Team"` and `version: "0.0.1"`, and its description covers components, pages, SSR adapters, content collections, static deployment, project structure and CLI commands.

That is a lot of surface for 140 lines, and the body is honest about it. The first line after the title is an instruction to always consult [docs.astro.build](https://docs.astro.build) for code examples and the latest API, and the file then gives the agent a compact reference: CLI commands, the canonical project structure, the core config options with an `astro.config.ts` example, two worked component examples, a deployment checklist built around adapters, and links onward.

## Installation

The skills.sh listing documents a single command for this repository:

```bash
npx skills add astrolicious/agent-skills
```

If you would rather place the file yourself, the repository is one directory, so a manual install is a clone plus a copy into the directory your agent scans:

```bash
git clone https://github.com/astrolicious/agent-skills.git
mkdir -p .agents/skills && cp -r agent-skills/skills/astro .agents/skills/
```

There is nothing else to install. The skill has no scripts, no dependencies and no manifest files at the repository root, and the README does not document any plugin or marketplace route, so the `npx skills` path or a manual copy are the only two options the repository supports.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| astro | 18,959 | The Astro framework skill: CLI commands, project structure, config, adapters and a deploy checklist |

No indexed listings fall below the threshold.

The install count is concentrated in a single listing, so the useful question is what that one file contains. It opens with a quick reference that pins the CLI commands an agent will otherwise guess at: `npx astro dev`, `npx astro build`, `npx astro check`, `npx astro add` and `npx astro sync`, plus the note that `astro sync` has to be re-run after adding or changing plugins. It then lists the config file names the CLI looks for (`astro.config.js`, `.mjs`, `.cjs`, `.ts`) and the `--config` flag for a custom path.

The project structure section marks `src/pages` as required and the rest as convention, which is the distinction a model usually flattens. The config section covers `site` as the deployed URL used for sitemaps and canonical URLs, and shows a minimal `defineConfig` example. The adapters section carries a one-line `npx astro add <name> --yes` for Node, Cloudflare, Netlify and Vercel, and the deployment workflow ends with a step that is easy to skip: verify the build output directory exists and is non-empty before deploying.

## Why This Matters for Hermes Agents

An agent asked to touch an Astro project usually has three failure modes, and this skill addresses each one. The first is inventing structure. Astro is convention-driven (`src/pages` is required, `src/components` is not), and a model that has never seen the repository will scaffold directories that the router ignores. The skill states the required-versus-convention split in one line.

The second is config drift. Astro reads four different config file extensions and a `--config` override, and the `site` value drives sitemaps and canonical URLs. Getting `site` wrong produces a site that builds cleanly and then publishes the wrong canonicals, which is the kind of bug that only shows up in search data weeks later.

The third is the deploy step. The workflow in the skill is ordered: add the adapter, run `astro check` to catch type and configuration errors, run `astro build`, confirm `dist/` is non-empty, then deploy. An agent that jumps from `astro add` straight to a deploy command tends to ship an empty artifact.

The skill also tells the agent to treat `docs.astro.build` as the source of truth rather than its own memory, which is the correct posture for a framework that ships breaking changes on a regular cadence. For Hermes workflows that touch many repositories, a 140-line file that arrives with the framework's own vocabulary is cheaper than a long research pass per task.

## Usage

| You say | What happens |
|---|---|
| "Add a landing page to this Astro site" | The agent writes `src/pages/index.astro` with a frontmatter block, matching the page example rather than inventing a route config |
| "Make this component reusable across pages" | The agent creates `src/components/Card.astro`, reads props from `Astro.props`, and imports it where needed |
| "Switch this project to on-demand rendering on Cloudflare" | The agent runs `npx astro add cloudflare --yes`, then `astro check`, then `astro build`, and confirms the output directory before deploying |
| "Why are my canonical URLs wrong?" | The agent checks the `site` field in the Astro config, since that value drives sitemap and canonical generation |
| "My build broke after I added an integration" | The agent re-runs `npx astro sync` to regenerate TypeScript types, which the skill flags as required after plugin changes |
| "Review this Astro project structure" | The agent compares the tree against the documented layout and flags anything outside `src/pages`, `src/components`, `src/layouts`, `src/styles` and `public` |

## Verification

Read the skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/astrolicious/agent-skills/main/skills/astro/SKILL.md | head -30
```

It should open with the frontmatter (`name: astro`, `authors: "Astro Team"`, `version: "0.0.1"`, `license: MIT`), then the line pointing at docs.astro.build, then a "Quick Reference" block with the CLI commands.

After install, confirm the file landed in the directory your agent scans, adjusting the path if your setup differs:

```bash
ls .agents/skills/astro/SKILL.md
```

The install is complete when that file exists and starts with the same frontmatter. There are no supporting references to check, which is also why a partial copy cannot lose anything.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| astro | Pass | Pass | Pass |

The skill surface is a single markdown file. Nothing in it executes, nothing is fetched at run time, and every command it hands the agent is a standard `npx astro` invocation against the local project. That is the whole reason the scanners pass.

Two licensing facts are worth separating. The repository has no LICENSE file at its root, so GitHub reports no license, while the `SKILL.md` frontmatter claims `license: MIT`. Treat the MIT claim as a declaration inside the file rather than a repository-level grant, and read it before redistributing the text.

## Limitations

- Snapshot data, verified 2026-11-07: 18,959 combined installs across 1 indexed listing; 13 GitHub stars; no license file; last pushed 2026-03-20. Counts drift over time.
- No LICENSE file exists at the repository root. The MIT claim lives only in the skill frontmatter, so the redistribution terms are weaker than a normal MIT repository.
- The file is 140 lines including its frontmatter, and it covers CLI, structure, config and adapters. Content collections, islands and view transitions appear in the frontmatter trigger list but have no sections in the file, so the agent still has to fall back to the docs for those topics.
- Last push was 2026-03-20, so anything Astro added after that date is absent. The skill itself instructs the agent to consult docs.astro.build, which is the mitigation.
- One file, one maintainer account, 13 stars, no CI and no tests. The `version: "0.0.1"` in the frontmatter is the only version signal, and there are no tags or releases to pin against.
- No install instructions exist in the repository README, which is a credits list only. The command above comes from the skills.sh listing page for this repository.

## Related

- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Netlify Agent Skills - Serverless Deployment for Hermes Setup](/hermes/skills/catalog/netlify-agent-skills-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Say the framework and the host out loud. "Deploy this Astro site to Netlify" gets the adapter plus the check and build steps, while "make it deployable" gets a guess.
- Keep the deploy checklist. The step that verifies `dist/` is non-empty before deploying catches the most common empty-artifact failure.
- Treat the skill as a router to the docs. It names the right pages, and the agent reading docs.astro.build for the current API is the behaviour the file asks for.
- Ask for a structure review first on unfamiliar repositories. Comparing the tree against the documented layout is cheap and surfaces misplaced pages before anyone writes code.
- Pin your Astro major version in prose when you delegate. The skill tracks the current CLI shape and does not carry per-version migration notes.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
