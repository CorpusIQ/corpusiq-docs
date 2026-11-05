---
title: "Effect Skills - TypeScript Effect System Setup"
description: "effect-ts/skills on skills.sh: 9.2K combined installs across 2 listings; Effect TypeScript repo setup plus a bounded v3 to v4 upgrade workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/effect-ts-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "typescript", "effect", "migration"]
---

# Effect Skills - Setup Guide

**Source:** [effect-ts/skills](https://www.skills.sh/effect-ts/skills) via skills.sh - 9.2K combined installs across 2 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 114 stars, MIT licence, last pushed 2026-10-09, 2 SKILL.md directories under skills/
**Category:** TypeScript effect-system guidance for agents: repository setup conventions and a bounded Effect v3 to v4 migration
**Quality Tier:** 🟢 Production - every sampled audit Pass; MIT; 114 stars.

The Effect TypeScript library ships its own agent guidance inside the npm package, at `node_modules/effect/AGENTS.md`. This repository is the thin layer that points a coding agent at it: two skills, one that wires a repository up to the installed Effect version and one that drives a v3 to v4 upgrade.

The design choice is worth naming. Instead of copying Effect conventions into skill files that go stale as the library moves, `effect-ts` instructs the agent to read the guidance shipped with whichever version is actually installed and to search `node_modules/effect/src` for anything the guide does not cover. `effect-v3-to-v4` applies the same discipline to migration: replacements come from the generated `migration/v3-to-v4.md` reference in the Effect repo, not from the model's memory of the API.

## Installation

The README installs cross-agent through skills.sh, and the command installs both skills:

```bash
npx skills add Effect-TS/skills
```

The repository README spells the organization `Effect-TS` while the skills.sh listing is named `effect-ts/skills`. Run the command as the README writes it. There is no per-skill install flag documented for this repo, so a project that only needs the migration workflow still gets both directories.

The `effect-ts` skill expects Effect itself to be present. Its own SKILL.md starts with the install step, using whatever package manager the project already uses:

```bash
pnpm add effect@latest
```

In a monorepo it installs Effect as a root dev dependency so the source is reachable from `node_modules/effect/src`:

```bash
pnpm add -D effect@latest
```

Then add the block the skill asks for to `AGENTS.md` or `CLAUDE.md`: a short "Learning more about Effect" section telling the agent to read `node_modules/effect/AGENTS.md` completely before writing Effect code, follow the links in it, and search `node_modules/effect/src` for APIs it does not cover.

## What It Provides

Two listings, both above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| effect-ts | 8,457 | Setting up a repository that uses Effect: install step, monorepo dev dependency, and the agent instructions that point at the package's own AGENTS.md |
| effect-v3-to-v4 | 732 | Migrating a codebase from Effect v3 to v4, including every `@effect/*` package crossing the v3/v4 boundary |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

Effect's API surface is broad and has moved across major versions, which is exactly the shape of library a language model gets wrong quietly. A plausible-looking helper that was renamed or removed between majors type-checks as a red squiggle at best and as a runtime surprise at worst. `effect-ts` removes the guess by making the installed package the source of truth: the agent reads the guidance that shipped with the version in the lockfile, not a remembered one.

The migration skill is the more disciplined of the two. It works in a fixed order that matters: local shallow checkouts of the v4 and v3 branches, then reading the migration index, then migrating `package.json` before any type-check. That last ordering is the difference between a usable error list and a wall of unresolved imports from packages that v4 consolidated away.

It also constrains how the reference is read. Search the migration reference for the symbol, do not read the whole file, then escalate to the topic guides and finally to v4 or v3 source. Every rename is answered by upstream data.

And it refuses the easy exit. The skill's hard prohibition is that an error is never silenced instead of resolved, and its done condition is a clean type-check with tests reported honestly rather than treated as a gate. For an agent that likes to declare victory, that is the useful part.

## Usage

| You say | What happens |
|---|---|
| "Set this repo up to use Effect" | effect-ts adds the dependency, configures the monorepo dev dependency and writes the AGENTS.md block |
| "We just installed effect, check our agent instructions" | effect-ts verifies the pointer to node_modules/effect/AGENTS.md exists and is complete |
| "Why is this Effect code wrong for our version" | effect-ts reads the installed package's AGENTS.md and searches node_modules/effect/src |
| "Migrate this service from Effect v3 to v4" | effect-v3-to-v4 clones both branches, migrates package.json and starts the type-check loop |
| "Upgrade all our @effect packages across the v4 boundary" | effect-v3-to-v4 removes consolidated packages and aligns the rest on one v4 version |
| "This migration has 400 type errors, work through them" | effect-v3-to-v4 resolves each error through the migration reference, escalating to source when needed |
| "Is the migration done" | effect-v3-to-v4 reports type-check status and the honest test outcome |

## Verification

Read the skill file before installing, since the description is the trigger the agent matches:

```bash
curl -fsSL https://raw.githubusercontent.com/Effect-TS/skills/main/skills/effect-ts/SKILL.md | head -4
```

It should open with `name: effect-ts` and the single-line description about setting up a repository that uses Effect. Then confirm the one directory per skill landed:

```bash
ls ~/.claude/skills | grep -E 'effect-ts|effect-v3-to-v4'
```

Two directories should appear. For the setup skill to do anything useful, the package guidance it points at must exist:

```bash
ls node_modules/effect/AGENTS.md
```

For the migration skill, check that its working checkouts are where it expects them after the first run:

```bash
ls .repos/effect/migration/
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| effect-ts | Pass | Pass | Pass |
| effect-v3-to-v4 | Pass | Pass | Pass |

Both skills are markdown instruction files with no installer scripts of their own, and both verdict sets are clean. The migration skill does clone the Effect repository into the project and will edit `package.json` plus source files, so run it on a branch with a clean working tree and review the diff before merging.

## Limitations

- Snapshot data, verified 2026-11-05: 9,189 combined installs across 2 indexed listings; 114 GitHub stars; MIT; last pushed 2026-10-09. Counts drift over time.
- `effect-ts` is a 35-line skill that delegates almost everything to `node_modules/effect/AGENTS.md`. If the dependency is not installed, or the version predates that file, the skill has nothing to point at.
- `effect-v3-to-v4` carries `disable-model-invocation: true` in its frontmatter, so an agent will not pick it up from a passing mention. Ask for it by name.
- The migration path needs network and git at run time: two shallow clones plus a searchable migration reference. It is not an offline workflow.
- Install counts are lopsided, 8,457 against 732, so the setup skill has far more real-world exercise than the migration skill.
- No CHANGELOG or version matrix ships in the repo, so a v4 release that reorganizes the migration reference would need a skill update rather than a config change.

## Related

- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Mastra AI Skills - TypeScript Agent Framework Setup](/hermes/skills/catalog/mastra-ai-skills-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install Effect before the skill. The setup skill's first instruction is the dependency itself, and its second is the AGENTS.md pointer, so run them in that order instead of asking the agent to sort it out.
- Put the AGENTS.md block in the repository, not in a personal config. It is the one piece of this suite that every future session depends on.
- Commit before the migration. The skill edits `package.json` and source files in place, and a clean diff is the only sane review surface.
- Do the `package.json` change on its own. Aligning package versions before the first type-check turns thousands of unresolved imports into a list of real API errors.
- Do not accept a suppressed error as progress. The skill's own rule is that errors get resolved, not silenced with a cast or an ignore comment.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
