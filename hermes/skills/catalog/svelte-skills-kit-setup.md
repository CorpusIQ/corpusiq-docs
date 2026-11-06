---
title: "Svelte Skills Kit - Runes, Data Flow and Deployment"
description: "spences10/svelte-skills-kit on skills.sh: 5.0K combined installs across 11 listings; Svelte 5 runes, SvelteKit data flow and deployment skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/svelte-skills-kit-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "svelte", "sveltekit", "frontend"]
---

# Svelte Skills Kit - Setup Guide

**Source:** [spences10/svelte-skills-kit](https://www.skills.sh/spences10/svelte-skills-kit) via skills.sh - 5.0K combined installs across 11 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 94 stars, no licence (no LICENSE file in the repository root), last pushed 2026-10-12, ten SKILL.md directories under plugins/svelte-skills/skills/ for eleven indexed listings, with marketplace manifests at .claude-plugin/ and plugins/
**Category:** SvelteKit for agents: runes, template directives, data flow, remote functions, styling and deployment
**Quality Tier:** 🟡 Review - no licence (no LICENSE file in the repository root, so no explicit grant to reuse or redistribute the skill text) and this repository is a plugin marketplace wrapper that republishes skills maintained in another repository.

This is a distribution repository rather than an original skill collection. The README opens by calling it a "Claude Code plugin marketplace wrapper for the Svelte skills from spences10/skills", and says the Svelte subset is packaged here for Claude Code users while the canonical, vendor-agnostic source is `spences10/skills`. That matters twice: the skills you install are copies synced from elsewhere, and the plugin format is Claude Code's, not a generic one.

The content itself is ten Svelte 5 and SvelteKit reference skills, each a short SKILL.md of 49 to 101 lines, most opening with a quick-start table and terse rules. They are written as lookups, not tutorials: `svelte-runes` answers which rune to reach for, `sveltekit-structure` covers file naming, nested layouts, error boundaries and hydration, `svelte-template-directives` covers `{@attach}` replacing `use:` actions. The repository also ships two plugins, `svelte-lsp` and `typescript-lsp`, that carry language-server configuration for Claude Code.

## Installation

The README's quick start adds the marketplace once, then installs the skill plugin:

```bash
/plugin marketplace add spences10/svelte-skills-kit
/plugin install svelte-skills
```

The same marketplace also carries the two language-server plugins. Each supplies configuration only, so install the server binaries first and check they resolve on `PATH`:

```bash
npm i -g svelte-language-server
which svelteserver
/plugin install svelte-lsp@svelte-skills-kit
```

The TypeScript plugin is the official configuration with `useSyntaxServer` set to `never`, which makes the first `goToDefinition` or `findReferences` wait for the project index instead of answering from the lightweight syntax server. Its README step installs the server, then disables the official plugin so two servers do not both handle `.ts` files:

```bash
npm i -g typescript-language-server typescript
/plugin install typescript-lsp@svelte-skills-kit
/plugin disable typescript-lsp@claude-plugins-official
```

If you are not using Claude Code plugins, the README points at the canonical repository with an explicit agent and skill name:

```bash
npx skills add spences10/skills --agent claude-code --skill svelte-runes
```

## What It Provides

Five listings clear the 500-install threshold. The three highest are the ones that shape how an agent writes Svelte 5 code: state, project structure, and components.

| Skill | Installs | Use For |
|---|---|---|
| svelte-runes | 1,100 | `$state`, `$derived`, `$effect`, `$props`, `$bindable`, plus migration from Svelte 4 patterns and the reactivity mistakes those runes prevent |
| sveltekit-structure | 1,095 | Routing, nested layouts, error handling, SSR, `svelte:boundary`, file naming, pending UI and hydration |
| svelte-components | 557 | Component patterns, headless libraries (Bits UI, Ark UI, Melt UI), form patterns and third-party integration |
| svelte-template-directives | 533 | `{@attach}`, `{@html}`, `{@render}`, `{@const}` and `{@debug}`, including `@attach` as the replacement for `use:` actions |
| sveltekit-data-flow | 504 | Load functions, form actions, `+page.server.ts` versus `+page.ts`, serialization, `fail()`, `redirect()`, `error()` and `invalidateAll()` |

The remaining 6 indexed listings range from 107 to 430 installs: sveltekit-remote-functions (430), svelte-deployment (249), ecosystem-guide (204), svelte-styling (132), layerchart-svelte5 (129) and svelte-layerchart (107). `layerchart-svelte5` has no directory of its own in the current tree; the in-tree LayerChart skill is `svelte-layerchart`.

## Why This Matters for Hermes Agents

Svelte 5 broke the mental model that most training data carries. Stores, `export let`, `$:` blocks and `use:` actions are all still findable in examples, and mixing them with runes produces code that compiles with warnings and behaves unpredictably. A skill that starts with "which rune" and states the Svelte 5 answer is a direct counter to that.

The structure skill covers the failure that is hardest to see in a diff. SvelteKit decides where code runs by filename, so an agent that puts a database call in `+page.ts` instead of `+page.server.ts` ships a bundle that leaks server code, and nothing in the editor complains. `sveltekit-structure` and `sveltekit-data-flow` both address that boundary explicitly.

The skills are also cheap to load. Each is around a hundred lines, most with a quick-start table at the top, so a Hermes agent can pull `svelte-runes` for a state question and `sveltekit-data-flow` for a form question without loading a framework manual into the context window.

The template-directives skill is the most current of the set: `{@attach}` arrived in Svelte 5.29 and most published Svelte code predates it. An agent that knows it replaces `use:` actions with something reactive, spreadable through components and able to return cleanup, produces code that matches the framework's direction rather than its history.

Finally, the language-server plugins are an operational win rather than a content one. Type errors in `.svelte` files and definition lookups are exactly the feedback an agent needs after an edit, and the README notes Claude Code has no official Svelte code-intelligence plugin.

## Usage

| You say | What happens |
|---|---|
| "Add a derived total to this component" | `svelte-runes` picks `$derived` over `$effect` and shows the dependency shape that keeps it reactive |
| "Move this database read out of the page component" | `sveltekit-data-flow` moves it into `+page.server.ts` and fixes the load signature |
| "Add a settings route with its own layout" | `sveltekit-structure` covers file naming, nested layouts and where error boundaries belong |
| "This form should not reload the page" | `sveltekit-data-flow` uses a form action with `fail()` and `invalidateAll()` instead of manual fetch wiring |
| "Replace this use: action" | `svelte-template-directives` rewrites it as `{@attach}`, including the cleanup return |
| "Style the child component from the parent" | `svelte-styling` covers `:global`, custom properties and the `style:` directive |
| "Build for Cloudflare Pages" | `svelte-deployment` covers adapters, Vite config, pnpm 10 prepare scripts and production builds |

## Verification

Read a skill before installing it. Both probes below were checked on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/spences10/svelte-skills-kit/main/plugins/svelte-skills/skills/svelte-runes/SKILL.md | head -6
curl -fsSL https://raw.githubusercontent.com/spences10/svelte-skills-kit/main/plugins/svelte-skills/skills/sveltekit-structure/SKILL.md | head -6
```

The first should open with `name: svelte-runes` and a one-line description covering reactive state, props, effects and migration. The second should open with `name: sveltekit-structure` and a description naming routing, layouts, error handling, SSR and `svelte:boundary`.

After the marketplace install, confirm the plugin is cached, since the README states that plugin files live at `~/.claude/plugins/cache/` rather than in the source tree:

```bash
ls ~/.claude/plugins/cache
```

The directory should contain the `svelte-skills` plugin. The README notes that source edits require a reinstall or a manual cache sync before they take effect.

If you installed through the canonical repository instead, check the skill where your CLI put it and read the description line: it should name the runes the skill covers, since that text is what the agent routes on.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| svelte-runes | Pass | Pass | Pass |
| svelte-components | Pass | Pass | Pass |
| sveltekit-remote-functions | Pass | Pass | Pass |
| svelte-styling | Pass | Pass | Pass |
| svelte-layerchart | Pass | Pass | Pass |

There is no LICENSE file in the repository root, so a passing scanner verdict says nothing about your right to redistribute the text. The repository is also a wrapper: the content originates in `spences10/skills`, and terms for that source are a separate question from the wrapper's own.

The real install surface is not the markdown. The two companion plugins drive language servers that the README installs globally with `npm i -g`, so `svelte-language-server` and `typescript-language-server` end up in a global prefix and execute inside your editor session. Pin or review those versions, and remember the TypeScript plugin deliberately changes an official plugin's initialisation options.

## Limitations

- Snapshot data, verified 2026-11-06: 5,040 combined installs across 11 indexed listings; 94 GitHub stars; no licence; last pushed 2026-10-12. Counts drift over time.
- No LICENSE file in the repository root. There is no explicit grant to copy, modify or redistribute the skill text, which matters more than usual here because the repository is a Claude Code plugin marketplace wrapper republishing Svelte skills maintained in spences10/skills.
- The install index outruns the tree by one. Eleven listings carry install counts but `plugins/svelte-skills/skills/` holds ten directories; `layerchart-svelte5` (129 installs) has no directory of its own, and `svelte-layerchart` is the LayerChart skill that ships.
- The packaged install path is Claude Code specific. It is a plugin marketplace with slash commands, the README's universal alternative lists `--agent claude-code`, `--agent pi` and `--agent opencode`, and Hermes is not among them, so a Hermes install has to go through the canonical repository and its CLI flags.
- Remote functions are experimental. The `sveltekit-remote-functions` skill states that remote functions are experimental in SvelteKit 2.58 and require enabling, so guidance there can change between releases.
- These are reference sheets, not generators. Nothing here scaffolds a project, and the material assumes Svelte 5; a codebase still on Svelte 4 needs the migration sections rather than the patterns.

## Related

- [Svelte AI Tools - Official Svelte and SvelteKit Setup](/hermes/skills/catalog/svelte-ai-tools-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `svelte-runes` before anything else. Most Svelte mistakes an agent makes are rune mistakes, and the rest of the pack assumes that vocabulary.
- Ask for the server file by name. "Put the load in `+page.server.ts`" is a stronger instruction than "load this data", because the filename is the security boundary.
- Keep `svelte-lsp` installed if you edit components in a loop. Type errors after an edit are the fastest feedback available and Claude Code has no official Svelte equivalent.
- Take the canonical repository when you need another agent target. The wrapper is convenient for Claude Code and a detour everywhere else.
- Read the sync script before contributing. This repository pulls from `spences10/skills` with `scripts/sync-from-skills.sh`, so an edit here can be overwritten by the next sync.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
