---
title: "Nuxt Skills - Vue, Nuxt and NuxtHub Agent Setup"
description: "onmax/nuxt-skills: 69.8K combined installs across 35 listings. Vue, Nuxt, Nuxt UI and NuxtHub skills that keep agent code on current framework APIs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/onmax-nuxt-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "nuxt", "vue"]
---

# Nuxt Skills - Setup Guide

**Source:** [onmax/nuxt-skills](https://www.skills.sh/onmax/nuxt-skills) via skills.sh - 69.8K combined installs across 35 indexed listings; first seen Jan 19, 2026 for the Nuxt and Vue listings, Jan 20, 2026 for vueuse and Jan 28, 2026 for pnpm
**GitHub:** [onmax/nuxt-skills](https://github.com/onmax/nuxt-skills) (724 stars; no LICENSE file in the repo, so GitHub reports no license while README.md and plugin.json both state MIT; pushed 2026-10-26; 26 `skills/<name>/SKILL.md` directories beside `plugin.json`, `mcp.json`, `ecosystem-skills.json`, `.claude-plugin/` and `.codex-plugin/`)
**Category:** Frontend / Vue and Nuxt Framework
**Quality Tier:** 🟡 Beta - clean auditor verdicts and weekly CI maintenance behind 69.8K installs, but the repo ships no LICENSE file, nine indexed listings no longer exist in the tree, and the core nuxt skill is written against a Nuxt 5 release candidate

The Nuxt ecosystem moves faster than any model's training cutoff. Nuxt 5 moved server code to Nitro v3, made routing case-sensitive and typed, and switched the bundler to Vite 8 with Rolldown; Vue 3.5 rewrote reactivity internals; Nuxt UI v4 rebuilt on Reka UI plus Tailwind CSS. This repository is one maintainer's attempt to keep an agent current across that whole surface: 26 SKILL.md directories covering the framework, the module authoring path, NuxtHub storage, Content, Studio, SEO, UI and the tooling around them.

The collection is a mix of hand-written skills and vendored ones. Seven come from antfu/skills (nuxt, vite, vitest, pinia, unocss, vue, nitro), four from vuejs-ai/skills (the vue-best-practices family), one from vueuse/skills, with the rest written in-repo. Vendor revisions are pinned in `ecosystem-skills.lock.json`, and `ecosystem-skills.json` names the upstream repositories and selected paths, so a given install is reproducible rather than floating on upstream HEAD.

## Installation

```bash
# Interactive picker, auto-detects installed agents
npx skills add onmax/nuxt-skills

# Global (user-wide) instead of per project
npx skills add onmax/nuxt-skills -g

# Skip the picker and install every skill in the repo
npx skills add onmax/nuxt-skills -y
```

```bash
# Claude Code marketplace route, one plugin for all skills
/plugin marketplace add onmax/nuxt-skills
/plugin install nuxt-skills@nuxt-skills
```

```bash
# Codex plugin marketplace route
codex plugin marketplace add onmax/nuxt-skills
codex plugin add nuxt-skills@nuxt-skills
```

The only prerequisite is Node.js for `npx`; no API key, runtime or build step is needed. Two MCP endpoints are optional companions: `mcp.json` registers the Nuxt MCP server at `https://nuxt.com/mcp`, and the nuxt-ui skill documents how to add the Nuxt UI MCP server at `https://ui.nuxt.com/mcp` for component API lookups. The README also notes that VueUse maintains its own current skill, so install `vueuse/skills` directly instead of relying on the generated copy here.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nuxt | 8,550 | Nuxt 5 app work: the `app/` srcDir layout, nuxt.config.ts and app.config.ts, typed routing, useFetch and useAsyncData, Nitro v3 server routes, modules, deployment |
| vue | 7,944 | Vue 3.5 Composition API: script setup macros, reactivity, watchers, lifecycle hooks, Transition and Teleport; rules favour TypeScript and shallowRef |
| reka-ui | 7,370 | Reka UI v2.11 (formerly Radix Vue) headless primitives: component APIs, asChild composition, controlled and uncontrolled state, virtualization, WAI-ARIA patterns |
| nuxt-ui | 7,010 | @nuxt/ui v4: 125+ Tailwind-based components, brand theming, forms, dashboards and docs layouts, plus wiring for the Nuxt UI MCP server |
| vitest | 3,124 | Vitest 5 config, mocking, coverage, test filtering and fixtures on the Vite transform pipeline |
| nuxt-seo | 3,094 | Nuxt SEO module: site config, robots and sitemap, dynamic OG images, schema.org JSON-LD, breadcrumbs and canonical URLs |
| vueuse | 3,058 | VueUse 14.x composables: check for an existing utility before writing a custom composable (no directory in the current tree) |
| nuxt-content | 2,816 | @nuxt/content: content.config.ts collections, queryCollection, Markdown and MDC rendering, hooks, custom sources, Content v2 migration |
| nuxt-modules | 2,743 | Authoring Nuxt modules: defineNuxtModule, Kit utilities, hooks, E2E testing, npm release and CI workflows |
| vite | 2,429 | Vite 8.3 (Rolldown plus Oxc): config, plugin API, SSR, library builds and the Vite 8 migration path |
| motion | 2,334 | Motion Vue (motion-v 1.x): declarative animations, gestures, scroll-linked effects, layout transitions, spring physics (no directory in the current tree) |
| nuxthub | 2,167 | NuxtHub v0.10.8: Drizzle ORM on SQLite, PostgreSQL or MySQL, KV, blob and cache bindings, migrations, Cloudflare and Vercel deployment |
| document-writer | 2,067 | Blog posts and documentation pages written to the style of the official Nuxt sites (no directory in the current tree) |
| nuxt-better-auth | 1,998 | @nuxtjs/better-auth: install and env config, client and server auth APIs, route protection, session refresh, Better Auth plugins |
| ts-library | 1,986 | TypeScript library authoring: package.json exports for dual CJS and ESM, tsconfig, tsdown and unbuild, type-safe API design, release CI (no directory in the current tree) |
| pnpm | 1,868 | pnpm installs, workspace catalogs, dependency overrides, patching third-party packages, CI setup, supply chain hardening (no directory in the current tree) |
| nuxt-studio | 1,571 | Self-hosted Nuxt Studio editor for Nuxt Content: installation, editor customization, OAuth, media, drafts, Git publishing, production deploy |

The remaining 18 indexed listings range from 144 to 1,270 installs: tsdown 1,270, tresjs 1,203, writing-web-documentation 965, phaser-best-practices 879, nuxt-i18n 589, vue-best-practices 279, vueuse-functions 272, nitro 257, pinia 246, vue-testing-best-practices 233, vue-debug-guides 231, vue-router-best-practices 221, comark 201, nuxt-users 184, arkenv 181, unocss 169, regle 167 and t3-code-continue-thread 144. Four of those (tsdown, tresjs, writing-web-documentation, phaser-best-practices) are also absent from the current tree, and the last group is the ecosystem tail: Pinia, UnoCSS, i18n, Nitro, a Vue testing and debugging set, a changelog tool and a validation library.

## Why This Matters for Hermes Agents

The failure mode this suite targets is confident, stale framework knowledge. An agent that writes a Nuxt 4 server route from memory will import auto-imported server utilities that Nuxt 5 no longer exposes by default, put a page in a root-level `pages/` folder when the default srcDir is now `app/`, and assume case-insensitive routing. The nuxt skill states all three changes directly, along with the Nitro v3 and Vite 8 shift and the Node 22.19 or 24.11 floor, so the correction arrives before the first file is written instead of after a failed build.

The second gain is scoping. Each skill is a router: it tells the agent which reference file to open for which task and explicitly says not to load them all. `nuxt-content` hands off non-content packages to the nuxt, nuxt-studio or nuxt-ui skills; `nuxthub` hands off server patterns to nuxt. For a Hermes session with a fixed context budget, that is a working progressive-disclosure design rather than one 40K-token blob, and it maps cleanly onto how skill activation already works here.

The third is coverage of the awkward middle layer. Module authoring, TypeScript library packaging and pnpm workspace plumbing are the tasks where agents produce plausible but wrong config. The nuxt-modules, ts-library and pnpm skills carry the actual defineNuxtModule signatures, exports maps and catalog syntax, which is cheaper to read than to reconstruct from error messages.

Finally, freshness is automated rather than promised. Three GitHub Actions workflows run weekly and biweekly: reka-ui docs are regenerated from upstream every Monday, ecosystem skills are re-bundled from their pinned source repos every Monday, and a maintenance job reviews upstream changelogs on the 1st and 15th and opens PRs when APIs move. The vendored revisions in `ecosystem-skills.lock.json` make each of those rebuilds traceable.

## Usage

| You say | What happens |
|---|---|
| "Add a server route that reads from NuxtHub KV" | Loads nuxthub for the `hub:kv` binding and wrangler config, and nuxt for the Nitro v3 handler style, then writes both against the installed version |
| "Why does this component fetch twice on navigation?" | Opens the vue skill for watch and watchEffect semantics plus the nuxt data-fetching reference for useAsyncData keys and caching |
| "Build a Nuxt module that registers a runtime composable" | Uses nuxt-modules for defineNuxtModule, Kit utilities and addPlugin patterns, then the playground test loop |
| "Set up a content collection with a typed query" | Loads nuxt-content for content.config.ts schema and queryCollection, without pulling in Studio or UI guidance |
| "Theme Nuxt UI to match our brand colours" | Works through the nuxt-ui theming and Tailwind CSS variable guidance, and points at the Nuxt UI MCP server for exact prop surfaces |
| "Add dynamic OG images and a sitemap" | Loads the nuxt-seo references for og-image and crawlability, then applies site config once for both |
| "This pnpm workspace override is not applying" | Uses the pnpm skill for catalog and override syntax and explains the resolution order before any edit |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -Ei "nuxt|vue"
```

Read the load-bearing skills before installing. All six URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/README.md
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/skills/nuxt/SKILL.md
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/skills/vue/SKILL.md
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/skills/nuxt-ui/SKILL.md
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/skills/reka-ui/SKILL.md
curl -sL https://raw.githubusercontent.com/onmax/nuxt-skills/main/skills/nuxthub/SKILL.md
```

The version statements are the fastest way to see if a skill matches your project:

```bash
grep -m1 "Based on\|generated at\|Current version" \
  ~/.claude/skills/nuxt/SKILL.md ~/.claude/skills/vite/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nuxt | Pass | Pass | Pass |
| vue | Pass | Pass | Pass |
| nuxt-ui | Pass | Pass | Pass |
| pnpm | Pass | Pass | Pass |

No sampled verdict reports malware, prompt injection or data exfiltration, and the SKILL.md files carry no `allowed-tools` frontmatter, so they cannot widen an agent's tool surface by themselves. The write actions are in the instructions, not in bundled code. Several skills tell the agent to run package installs (`npx nuxi module add hub`, `npm install nuxt-users` with drivers, `pnpm add`), which reach the npm registry and modify package.json and lockfiles. The nuxt-ui skill asks the agent to add an MCP server entry to `.cursor/mcp.json` or via `claude mcp add`, and the repo's own `mcp.json` points at the remote Nuxt MCP server at `https://nuxt.com/mcp`, so component answers can arrive over the network rather than from the pinned text. The repo also ships `sync-skills.sh`, which rsyncs `skills/` into `~/.claude/skills` and `~/.codex/skills` and runs `rm -rf` on directories it previously recorded in its own `.nuxt-skills-managed` manifest; it skips symlinked targets, but it is a delete-capable script and should be read before running. No skill ships code that reads or transmits credentials. What they do document is app-level secret handling you supply yourself: nuxthub environment bindings, nuxt-better-auth and nuxt-users OAuth client IDs and secrets, nuxt-studio Git and auth tokens, and arkenv environment validation.

## Limitations

- There is no LICENSE file in the repository. GitHub therefore reports no license, while README.md and plugin.json both say MIT. Treat the MIT claim as the publisher's stated intent and get written confirmation before redistributing the content or bundling it into a product.
- The install index outruns the tree: 35 indexed listings against 26 SKILL.md directories. vueuse, motion, document-writer, ts-library and pnpm still carry install counts and render content on skills.sh but have no directory at `main`, and four below-threshold listings (tsdown, tresjs, writing-web-documentation, phaser-best-practices) are in the same state. Installs of those names resolve from the index snapshot, not from files you can audit in the repo.
- The nuxt skill is generated against Nuxt 5 (`5.0.0-0`), dated 2026-09-25. On a Nuxt 4 project, read its directory layout and auto-import notes before applying them, because `app/` as srcDir and the loss of default server-utility auto-imports are Nuxt 5 behaviours.
- Version pins are per skill and uneven: vite is written for 8.3.1, vitest for 5.0.1, reka-ui for 2.11.0, nuxthub for 0.10.8, while vue-best-practices is a vendored rule set that follows its upstream repo. A skill can lag the release you actually have installed.
- Two skills depend on remote MCP servers for authoritative answers (nuxt.com/mcp and ui.nuxt.com/mcp), so their advice is only as current as that endpoint and is unavailable in an air-gapped session.
- Snapshot data, verified Oct 26, 2026: 69,820 combined installs across 35 indexed listings; 724 GitHub stars; no LICENSE file (README and plugin.json state MIT); last pushed 2026-10-26. Counts drift over time.

## Related

- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup) - the upstream source for four of this repo's vendored skills, if you want the rule sets without the Nuxt wrapper.
- [Anthony Fu Skills - Vue, Vite and TS Tooling Setup](/hermes/skills/catalog/antfu-skills-setup) - upstream for nuxt, vite, vitest, vue, pinia, unocss and nitro; install it directly when you want those without the ecosystem bundle.
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup) - offlines the Tailwind reference that the nuxt-ui theming guidance assumes.
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup) - interface quality skills that pair with framework-correct code from this suite.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with `-y` only when you want all 26 skills resident. The interactive picker is the better default, because nuxt, vue, nuxt-ui and nuxthub cover most sessions and each extra skill spends context on discovery.
- Ask the agent to quote the version line from the skill it is using ("based on Vite 8.3.1", "NuxtHub v0.10.8"). It is the quickest way to catch a skill that predates your lockfile.
- For component questions, let the agent hit the Nuxt UI MCP server instead of the bundled text. The skill itself routes there for exact props and slots, and the local copy is a summary.
- Keep the vendored skills on the repo's schedule. Re-running `npx skills add onmax/nuxt-skills` picks up the Monday re-bundles; editing your local copies by hand will be overwritten by the next sync.
- If you only work in Vue and not Nuxt, install `vuejs-ai/skills` and `antfu/skills` directly. This bundle's value is the Nuxt-specific layer on top, and the underlying rule sets are maintained upstream.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
