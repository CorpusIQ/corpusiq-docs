---
title: "Anthony Fu Skills - Vue, Vite and TS Tooling Setup"
description: "Anthony Fu's skills: 375.7K combined installs. Twelve portable skills covering Vue, Nuxt, Vite, Vitest, pnpm, UnoCSS and his own setup conventions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/antfu-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "vue", "vite", "typescript"]
---

# Anthony Fu Skills - Setup Guide

**Source:** [antfu/skills](https://www.skills.sh/antfu/skills) via skills.sh - 375.7K combined installs across 21 indexed listings; new to this catalog in the Oct 24, 2026 evening sweep

**GitHub:** [antfu/skills](https://github.com/antfu/skills) - 6,008 stars, MIT, last pushed 2026-10-23, branch main, 12 skill directories under `skills/` plus git submodules that pin the official documentation each generated skill is built from

**Category:** Frontend Tooling / JavaScript and TypeScript

**Quality Tier:** 🟡 Beta - official repository from a Vue, Vite and Nuxt core maintainer with permissive licensing and clean auditor verdicts, but the README describes the collection as a proof of concept the author has not fully tested in practice

Anthony Fu maintains Vue, Vite, Nuxt, Vitest, UnoCSS and more, and this repository is his opinionated answer to a specific question: what should an agent know before it touches a project in that stack. The collection is larger than most personal skill sets because it is generated rather than hand written. Each skill is produced from the official documentation of the project it covers, then fine tuned, and the documentation source is pinned as a git submodule so the skill can be regenerated when upstream changes.

That design is the reason to install it rather than a competitor. The generated skills carry the actual APIs of Vue, Vite, Vitest, Nuxt, Pinia, pnpm, UnoCSS, VitePress and Nitro, and the hand maintained ones carry Anthony's own conventions on top: which toolchain he reaches for, how he publishes a library, how he opens a pull request, how he triages issues. An agent that has both the API surface and the house conventions produces code that a maintainer of those projects would not rewrite.

What the repository does not claim is maturity. The author says plainly that this is a proof of concept for generating skills from source documentation and keeping them in sync, that he has not fully tested how well the skills perform, and that feedback is welcome. Treat that as the honest state of the collection rather than a marketing caveat, and review the skill you depend on before you rely on it.

## Installation

Two paths, both from the README. The recommended one installs through the `@antfu/skills` package, which keeps the skills in sync with your package manager and also pulls in curated skills from other authors:

```bash
pnpm i -D skills-npm @antfu/skills
pnpx skills-npm setup
```

The direct path installs from this repository only, through the `skills` CLI:

```bash
npx skills add antfu/skills
```

To take every skill in the repository without prompts, and optionally globally:

```bash
npx skills add antfu/skills --skill='*'
npx skills add antfu/skills --skill='*' -g
```

Each directory under `skills/` is self contained, with a short `SKILL.md` and a `references/` folder the agent loads only when a task reaches it. Copying one directory into your agent's skills folder works the same way as the CLI install.

If you want your own version of this collection, the README documents the generator: fork the repository, run `pnpm install`, edit `meta.ts` with your projects and documentation sources, then `pnpm start cleanup`, `pnpm start init` and `pnpm start sync` before asking an agent to generate a skill per project.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| vitest | 43,245 | Writing tests, mocking, coverage configuration, test filtering and fixtures with the Vite powered test runner and its Jest compatible API. |
| vite | 39,531 | Build configuration in `vite.config.ts`, the plugin API, SSR, library mode and the Vite 8 Rolldown migration. |
| vue | 35,756 | Vue 3 Composition API work: `script setup` macros including `defineProps`, `defineEmits` and `defineModel`, the reactivity system and the built-in components. |
| nuxt | 24,092 | Full stack Nuxt: SSR and hybrid rendering, auto imports, file based routing, server routes, `useFetch` and middleware. |
| vue-best-practices | 23,362 | Vue best practice guidance; indexed listing with no directory under `skills/` in the current tree. |
| pnpm | 22,318 | Workspaces through `pnpm-workspace.yaml`, catalogs, patches, overrides, config dependencies and the global virtual store. |
| vueuse-functions | 21,418 | VueUse composable guidance; indexed listing with no directory under `skills/` in the current tree. |
| pinia | 19,701 | Defining Pinia stores and working with state, getters and actions, including store patterns outside a component. |
| web-design-guidelines | 19,341 | Web design guideline review; indexed listing with no directory under `skills/` in the current tree. |
| vue-router-best-practices | 18,763 | Vue Router best practice guidance; indexed listing with no directory under `skills/` in the current tree. |
| vue-testing-best-practices | 17,184 | Vue testing best practice guidance; indexed listing with no directory under `skills/` in the current tree. |
| antfu | 16,858 | Anthony Fu's opinionated tooling and conventions for JavaScript and TypeScript projects: ESLint and Prettier alternatives, monorepos, library publishing, project setup. |
| unocss | 16,024 | Configuring the atomic CSS engine, writing utility rules and shortcuts, and working with the Wind, Icons and Attributify presets. |
| tsdown | 13,966 | TypeScript library bundling guidance; indexed listing with no directory under `skills/` in the current tree. |
| slidev | 13,796 | Slide deck authoring guidance; indexed listing with no directory under `skills/` in the current tree. |
| turborepo | 13,333 | Monorepo task orchestration guidance; indexed listing with no directory under `skills/` in the current tree. |
| vitepress | 11,825 | Building documentation sites on Vite and Vue, configuring themes and writing Markdown that uses Vue components. |
| nitro | 2,617 | The framework agnostic server toolkit behind Nuxt: `nitro.config`, server routes and event handlers, route rules, caching, storage, tasks, websockets and deployment targets. |
| antfu-design | 2,130 | Building devtools style Vue 3 interfaces on `@antfu/design`: the UnoCSS preset, the semantic token vocabulary, the prefixed primitives and light and dark contrast rules. |

The remaining 2 indexed listings sit below the threshold: antfu-create-pr (465 installs) and antfu-issue-triage (24 installs). Both exist in the tree and both are agent workflow skills rather than stack documentation.

## Why This Matters for Hermes Agents

Framework knowledge is the cheapest thing to get wrong. An agent asked to add a route in Nuxt, mock a module in Vitest or configure a monorepo in pnpm produces plausible code from training data that is often one major version behind, and the failure shows up as a type error the user has to debug.

These skills invert that. Each one is regenerated from the documentation of the project it covers, so the API surface in the skill matches the version the documentation describes, and the per skill `references/` folders hold the long form detail. For a Hermes agent working across several repositories, that is the difference between advice and a checked procedure.

The hand maintained skills matter for a different reason. `antfu` encodes the author's setup conventions, which are opinionated in ways a model cannot infer: he uses pnpm with catalogs, ESLint through a shared config rather than a bespoke one, and a particular publishing shape for libraries. An agent that follows the convention produces a pull request that matches the repository it lands in.

The operational caveat is the one the author states: this is a proof of concept and the per skill quality has not been measured. Install it for the API coverage, keep the hand maintained conventions in an `AGENTS.md` if you want them always loaded, and review a skill before you depend on it in a release path.

## Usage

| You say | What happens |
|---|---|
| "Add a composable that tracks window width" | vue applies the Composition API and reactivity rules, and vueuse-functions (when installed) points at the existing composable instead of a new one. |
| "Write tests for this module" | vitest configures the runner, mocks, coverage and fixtures in the shape the project already uses. |
| "Why does my library build emit two copies of Vue" | vite covers library mode and externalisation, and names the Rolldown migration if the project is on Vite 8. |
| "Set up a new monorepo" | antfu applies the pnpm workspace conventions, and turborepo or pnpm catalogs handle task and dependency wiring. |
| "Add a server route in Nuxt" | nuxt writes the route under `server/` with the correct event handler and runtime config access. |
| "Migrate this site to VitePress" | vitepress scaffolds config, theme and Markdown with Vue components. |
| "Open a pull request for this branch" | antfu-create-pr writes a Conventional Commits title, an evidence based body and attaches before and after screenshots for UI changes. |

## Verification

Confirm the layout on main before installing. Every in-tree skill uses the same one:

```bash
for p in skills/vue/SKILL.md \
         skills/vite/SKILL.md \
         skills/vitest/SKILL.md \
         skills/antfu/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/antfu/skills/main/$p"
done
```

Read the two workflow skills before granting repository access, because both act on GitHub:

- https://raw.githubusercontent.com/antfu/skills/main/skills/antfu-create-pr/SKILL.md
- https://raw.githubusercontent.com/antfu/skills/main/skills/antfu-issue-triage/SKILL.md

After install, the skills should appear in your agent's skills directory, one folder per skill. A listing install first (`npx skills add antfu/skills --skill='*'` prompts before writing) shows what the index resolves. To check a specific skill's API coverage, read its `SKILL.md` and the files under its `references/` folder in the browser or with the raw URLs above.

## Security

skills.sh verdicts for sampled skills (verified October 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vue | Pass | Pass | Pass |
| vite | Pass | Pass | Pass |
| vitest | Pass | Pass | Pass |
| nuxt | Pass | Pass | Pass |
| pnpm | Pass | Pass | Pass |
| antfu | Pass | Pass | Pass |

All six sampled listings pass all three auditors, and they are the six that matter for the risk model: documentation skills that write code and run commands but hold no credentials and call no remote service. The two unsampled workflow skills are the ones that touch GitHub, so review `antfu-create-pr` and `antfu-issue-triage` yourself before enabling them in a repository with write access.

The install path runs `pnpx skills-npm setup` from the `@antfu/skills` package, which writes skill files into your project. That is the only step in this guide that changes files outside a source edit, so run it on a clean tree and read the diff.

## Limitations

- Snapshot data, verified October 24, 2026: 375,749 combined installs across 21 indexed listings; 6,008 GitHub stars; MIT; last pushed 2026-10-23. Counts drift over time.
- The install index outruns the tree: 21 indexed listings against 12 skill directories. Nine listings have no directory under the current `skills/` tree, which is why several rows above read as listing only. `antfu-design` ships from the separate `antfu/design` repository.
- The README calls the project a proof of concept and states the author has not fully tested how well the skills perform. The install counts measure distribution, not measured quality.
- The generated skills are only as current as their pinned documentation submodule. A project on a canary or release candidate version may be ahead of what the skill describes.
- Two skills act on GitHub (`antfu-create-pr`, `antfu-issue-triage`). Neither is in the table above because both are under the install threshold, and both need a scoped token if you enable them.
- This is one author's opinionated stack. If your project uses a different toolchain, the `antfu` conventions skill will produce advice that conflicts with your own.

## Related

- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

## Pro Tips

- Start with one skill, not all twelve. `npx skills add antfu/skills` prompts per skill, and a stack specific skill only pays for its context when the project uses that stack.
- Read the `references/` folder of the skill you install. The `SKILL.md` is the entry point and the version specific detail lives one level down.
- Pin the install in a lockfile where the CLI writes one, so a teammate gets the same skill content rather than whatever main holds that day.
- Check the submodule pin before trusting a generated skill on a new major version: the repository records the documentation commit each skill was built from.
- Keep the `antfu` conventions skill out of repositories that do not follow those conventions. It is intentionally opinionated and will fight a different house style.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
