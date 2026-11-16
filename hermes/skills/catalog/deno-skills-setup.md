---
title: "Deno Skills - Official Deno Development Suite"
description: "denoland/skills: 2.8K combined installs across 8 listings, official Deno skills for permissions, Deploy, Fresh frontends, sandboxes and Node migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/deno-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "deno", "typescript", "javascript"]
---

# Deno Skills - Setup Guide

**Source:** [denoland/skills](https://www.skills.sh/denoland/skills) via skills.sh - 2.8K combined installs across 8 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 103 stars, MIT license, `main` branch, last pushed 2026-07-29, five `SKILL.md` files under `skills/`
**Category:** TypeScript and JavaScript runtime development
**Quality Tier:** 🟢 Green - both sampled skills pass all three auditors.

Deno's official skill collection targets Deno 2.9 and later, and its main job is to stop agents from writing Node habits into Deno code. The central claim in the repository is worth repeating because it decides how an agent should behave: `deno install` reads `package.json`, `deno add express` installs from npm, `node_modules` and `node:` built-ins work, so migrating to Deno is not a rewrite.

Version 2 of the collection consolidated three overlapping skills into one. `deno-guidance`, `deno-expert` and `deno-project-templates` were merged into `deno`, because their content overlapped and scaffolding is now `deno init`. The install index still carries the old names, which is the drift to keep in mind when picking what to install.

## Installation

Install the whole collection, or a single skill:

```bash
npx skills add denoland/skills
npx skills add denoland/skills --skill deno
```

For Claude Code there is also a plugin path:

```text
/plugin marketplace add denoland/skills
/plugin install deno-skills@denoland-skills
```

Manual installation is supported by copying directories into `~/.claude/skills/` or a project's `.claude/skills/`, which is the documented fallback when an agent host has no installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| deno-expert | 544 | Older name for the consolidated Deno skill; install `deno` instead. |
| deno-frontend | 421 | Fresh framework, Preact components and Tailwind CSS in Deno. |
| deno-deploy | 392 | Deployment workflows for Deno Deploy. |
| deno-guidance | 381 | Older name for the consolidated Deno skill; install `deno` instead. |
| deno | 368 | Core skill: dependency management, permissions, `deno.json`, the built-in toolchain and publishing. |
| deno-sandbox | 367 | Safe code execution with `@deno/sandbox`. |
| deno-project-templates | 224 | Older name, superseded by `deno init` and the consolidated skill. |
| migrate-to-deno | 124 | Moving a Node, npm, Yarn, pnpm or Bun project to Deno. |

All 8 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Permissions are the thing Deno does differently, and they are the thing a model trained on Node gets wrong. The skills push scoped grants such as `--allow-net=example.com` over blanket `-A`, which matters most when an agent is writing code that will run unattended.

The second trap is migration advice. An agent that treats Deno as a foreign runtime will propose rewriting a Node project from scratch; the repository's own guidance says the opposite and explains why. That reframing is hard to get from generic training data and cheap to get from a skill.

The consolidation is a good example of what healthy skill maintenance looks like. Rather than shipping four overlapping skills and letting an agent choose at random, the maintainers merged them into one `deno` skill and documented the change, so the guidance an agent loads is unambiguous. The cost is index drift, which the Limitations section covers.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a Deno HTTP server" | Uses the core skill for `deno.json`, the standard library and the current serve API. |
| "Move this Express app to Deno" | Uses `migrate-to-deno` and keeps the npm imports instead of rewriting the app. |
| "Deploy this to Deno Deploy" | Uses the deployment skill for the project and configuration steps. |
| "Run this untrusted snippet" | Uses the sandbox skill with `@deno/sandbox` rather than `-A` on the host. |
| "Add a Fresh route with a Preact island" | Uses the frontend skill for Fresh conventions and component structure. |
| "Why does deno test fail to find my imports" | Checks the permissions, import map and `deno.json` configuration the core skill documents. |

## Verification

Check the skill files and the target Deno version before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/denoland/skills/main/skills/deno/SKILL.md | head -20
deno --version
npx skills add denoland/skills --list
```

The skills target Deno 2.9 and later, so an older runtime is the first thing to rule out when guidance does not match behaviour.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| deno | Pass | Pass | Pass |
| deno-deploy | Pass | Pass | Pass |

The collection is first-party Deno content: Markdown skills plus plugin manifests, with permission guidance that reduces risk rather than adding capabilities.

## Limitations

- Snapshot data, verified 2026-11-14: 2,821 combined installs across 8 indexed listings; 103 GitHub stars; MIT; last pushed 2026-07-29. Counts drift over time.
- The install index outruns the tree: 8 listings against 5 `SKILL.md` files, because `deno-guidance`, `deno-expert` and `deno-project-templates` were merged into `deno` and only survive as listing names.
- The last push predates this snapshot by more than three months, so guidance tracks Deno 2.9 rather than the newest release.
- Five skills is a small surface: there is no React, Next.js or database skill here, and those come from other collections.
- Deno Deploy commands and configuration are the area most likely to change between releases, so re-check the deploy skill after upgrading.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `deno` rather than the merged names; the old three still resolve in the index but carry no separate content.
- Ask the agent to state the Deno version before it writes configuration, since the skills target 2.9 and later.
- Prefer scoped permissions in generated code, and treat a blanket `-A` in agent output as a defect to review.
- For migrations, keep `package.json` and npm imports: the documented path is incremental, not a rewrite.
- Use the sandbox skill whenever the agent has to run code it did not write.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
