---
title: "Vinext - Next.js on Vite Migration Skill Setup"
description: "cloudflare/vinext - 10.3K combined installs: Cloudflare's agent skill for migrating Next.js apps to vinext, its Vite-based Next.js runtime."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cloudflare-vinext-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "vinext", "nextjs", "vite", "cloudflare"]
---

# Vinext - Setup Guide

**Source:** [cloudflare/vinext](https://www.skills.sh/cloudflare/vinext) via skills.sh - 10.3K combined installs across 1 indexed listing; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [cloudflare/vinext](https://github.com/cloudflare/vinext) - 9,414 stars, MIT license, last pushed Nov 27, 2026, main branch; the indexed skill lives at .agents/skills/migrate-to-vinext/SKILL.md.
**Category:** Next.js Tooling (Vite Migration)
**Quality Tier:** 🟢 Green - the single listing is sampled and passes all three checks.

This is Cloudflare's vinext repository, the Vite plugin that reimplements the Next.js API surface so existing Next.js apps can run on Vite, with Cloudflare Workers as the primary deployment target. skills.sh indexes exactly one skill here, migrate-to-vinext, and the full 10,295 combined installs attach to that single listing. The skill sits at .agents/skills/migrate-to-vinext/SKILL.md with three reference files alongside it: compatibility.md, config-examples.md, and troubleshooting.md.

The skill is a phase-by-phase migration playbook: it verifies the project is Next.js, runs vinext check for a scored compatibility report, then walks through vinext init (automated migration) with manual package replacement and Vite config generation as a fallback, and finishes with deployment setup for Cloudflare Workers or other platforms via Nitro. The default branch is main, and the repo also carries two further in-tree skills (fix and triage) that skills.sh does not index.

## Installation

The README documents the skills CLI as the optional agent-assisted path. Install the skill, then open your Next.js project and ask it to migrate:

```bash
npx skills add cloudflare/vinext
```

```
migrate this project to vinext
```

The skill works with Claude Code, OpenCode, Cursor, Codex, and other AI coding tools. The migration itself runs through vinext's own CLI rather than through the skill:

```bash
npx vinext init
```

For a new project instead of a migration, scaffold with create-vinext-app:

```bash
pnpm create vinext-app@latest my-app
```

## What It Provides

skills.sh publishes a per-skill install count for the single indexed listing.

| Skill | Installs | Use For |
|---|---|---|
| migrate-to-vinext | 10,295 | Migrating Next.js projects to vinext: compatibility scanning, package replacement, Vite config generation, ESM conversion, and deployment setup (Cloudflare Workers natively, other platforms via Nitro) |

No indexed listings fall below the 1,000-install threshold.

## Why This Matters for Hermes Agents

vinext is one of the most visible bets on running Next.js outside Vercel, and the migration skill is a maintained, phase-by-phase playbook rather than a loose set of tips. An agent that migrates a Next.js app by hand risks missing the non-obvious steps: ESM conversion, renaming CJS config files, wiring Cloudflare cache adapters, and leaving the existing Next.js setup intact. The skill encodes all of them, including the flags agents and CI must pass to vinext init when no interactive prompt is available. Its three reference files let the agent load only the compatibility matrix, config examples, or troubleshooting notes it needs for the current step. The trade-off is that the skill is opinionated about Cloudflare: it recommends the native @vinext/cloudflare deploy path and treats Nitro as the secondary route, so an agent should keep that bias in mind for non-Cloudflare targets. And because vinext itself is under active development, the skill's guidance tracks a fast-moving tool and should be re-checked against the current repo before large migrations.

## Usage

| You say | What happens |
|---|---|
| Migrate this project to vinext | Verifies it is a Next.js project, then runs compatibility scanning, installs packages, generates a Vite config, and starts the dev server, flagging anything needing manual attention |
| Check whether my Next.js app works on vinext | Runs vinext check to produce a scored compatibility report before any changes |
| Migrate but keep Next.js working too | Runs the non-destructive vinext init flow, leaving next.config, tsconfig, and source files untouched |
| Set up Cloudflare Workers deployment | Asks for the deployment target and cache choices, then configures cloudflare.config.ts, bindings, and the deploy workflow |
| Deploy this to Vercel or Netlify | Adds the Nitro plugin and sets the matching NITRO_PRESET for the target platform |
| Convert my configs to ESM | Adds "type": "module" and renames CJS config files to .cjs to avoid ESM conflicts |

## Verification

Confirm the skill body and its references resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/cloudflare/vinext/main/.agents/skills/migrate-to-vinext/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/cloudflare/vinext/main/.agents/skills/migrate-to-vinext/references/compatibility.md | head -40
curl -sL https://raw.githubusercontent.com/cloudflare/vinext/main/README.md | head -40
```

All three URLs return 200. After installing, review the SKILL.md and its reference files before relying on it.

## Security

skills.sh verdicts for the sampled skill (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| migrate-to-vinext | Pass | Pass | Pass |

Across the 1 sampled skill there are 3 Pass, 0 Warn, and 0 Fail cells; the single listing passes all three checks.

## Limitations

- Snapshot data, verified Nov 26, 2026: 10,295 combined installs across 1 indexed listing; 9,414 GitHub stars; MIT license; last pushed Nov 27, 2026. Counts drift over time.
- vinext is under active development; the README says it is not yet a drop-in replacement for every application, with known gaps in newer App Router features, so evaluate it against your own app before adopting.
- skills.sh indexes only migrate-to-vinext; the repo tree also carries fix and triage skills under .agents/skills/ that carry no indexed install count.
- The skill covers roughly 94% of the Next.js 16 API surface, and intentionally excludes Vercel-specific features, AMP, legacy next export, Turbopack/webpack config, next/jest, and create-next-app scaffolding.
- The default branch is main, and every raw URL in this guide uses main.

## Related

[Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup), [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup), [Astro Skills - Contributor and PR Workflows Setup](/hermes/skills/catalog/astro-setup), [Anthony Fu Skills - Vue, Vite and TS Tooling Setup](/hermes/skills/catalog/antfu-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run vinext check before migrating; the skill flags critical incompatibilities early and tells you to stop if they exist.
- Prefer vinext init for a direct, repeatable migration, and keep the agent skill for investigating compatibility issues and guiding the migration.
- Pass --platform plus --cdn-cache, --data-cache, and --image-optimization when running vinext init from an agent or CI session; init errors out without them when there is no interactive prompt.
- Leave next.config.js in place; vinext reads it for redirects, rewrites, headers, basePath, i18n, and env config.
- For Cloudflare bindings, use import { env } from "cloudflare:workers" rather than getPlatformProxy() or custom worker entries.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
