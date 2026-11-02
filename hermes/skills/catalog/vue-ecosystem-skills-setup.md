---
title: "Vue Ecosystem Skills - Version-Aware Vue Context"
description: "Vue ecosystem agent skills: 5.9K combined installs. 35 version-aware skills for Vue 3.6, Pinia, Vue Router, VueUse, Reka UI, Vuetify and TanStack."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vue-ecosystem-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "vue", "frontend", "pinia"]
---

# Vue Ecosystem Skills - Setup Guide

**Source:** [skilld-dev/vue-ecosystem-skills](https://www.skills.sh/skilld-dev/vue-ecosystem-skills) via skills.sh - 5.9K combined installs across 35 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [skilld-dev/vue-ecosystem-skills](https://github.com/skilld-dev/vue-ecosystem-skills) - 184 stars, MIT, branch main, last pushed 2026-10-10; 35 `SKILL.md` directories under `skills/`, one per indexed listing

**Category:** Version-aware Vue ecosystem reference for agents: Vue 3.5/3.6, Pinia, Vue Router, Reka UI and VueUse

**Quality Tier:** 🟢 Green - generated from published package sources by skilld, MIT licensed, 35 skill directories against 35 indexed listings, and all five sampled skills pass Gen Agent Trust Hub, Socket and Snyk

Harlan Wilton's skilld project generates this collection rather than hand-writing it. Each skill is rebuilt from the published npm package of one Vue library, using that package's docs, GitHub issues, discussions and changelog as sources, and each one is regenerated when the library ships a new release. The 35 skills cover the core (`vue`, `pinia`, `vue-router`, `vue-test-utils`, `unhead`), UI libraries (`quasar`, `vuetify`, `primevue`, `shadcn-vue`, `reka-ui`, `floating-ui-vue`, `vue-data-ui`, `unovis-vue`), data and state (`pinia-colada`, six TanStack adapters), forms (`vee-validate`, `formkit`), animation (`motion-v`, `vueuse-motion`) and tooling (`vue-i18n`, `vitepress`, `tresjs`, `slidev-cli`), plus the VueUse family split across core, shared, components, integrations, math and motion.

The pitch is version awareness, and the files back it up with numbers. Each `SKILL.md` names the package version it was built against in its H1 and cites file paths in the prepared package for its claims: `vue` 3.6.0-beta.17, `pinia` 4.0.3, `vue-router` 5.3.1, `@vueuse/core` 15.0.0, `vuetify` 4.0.1, `quasar` 2.33.1, `@tanstack/vue-table` 9.2.4, `reka-ui` 2.10.5. That matters because agents default to the Vue 2 or Pinia 2 patterns in their training data, and a cited baseline is checkable in a way that prose advice is not.

## Installation

Three routes are documented. The skilld CLI is the project's own:

```bash
npx skilld add skilld-dev/vue-ecosystem-skills
npx skilld add skilld-dev/vue-ecosystem-skills --skill pinia
npx skilld add skilld-dev/vue-ecosystem-skills --skill vue-test-utils
```

The second is the skills.sh CLI, which installs the same directories:

```bash
npx skills add skilld-dev/vue-ecosystem-skills
```

The third is the Claude Code plugin marketplace, which installs one plugin per library:

```text
/plugin marketplace add skilld-dev/vue-ecosystem-skills
/plugin install pinia@vue-ecosystem-skills
/plugin install vue-router@vue-ecosystem-skills
/plugin install reka-ui@vue-ecosystem-skills
```

The filter names are the short package names, not the directory names. `--skill vue` lands `skills/vue-skilld`, and `--skill formkit` lands `skills/formkit-core-skilld`. For Hermes, the copy route is the one that applies, since none of the three is written for Hermes:

```bash
git clone https://github.com/skilld-dev/vue-ecosystem-skills.git
cp -R vue-ecosystem-skills/skills/pinia-skilld ~/.hermes/profiles/corpusiq/skills/
```

Every skill directory holds only markdown, so a copy is self-contained. Copy the ones the project actually imports rather than all 35; the trigger phrases overlap heavily and an agent that loads `vue-skilld` for a `vuetify` question gets the wrong baseline.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| quasar-skilld | 691 | Building and debugging Quasar apps: Vite, Vitest, Storybook and UMD setup, Quasar CLI, Sass variable styling, and upgrades within Quasar v2 on a 2.33.1 baseline. |
| vue-i18n-skilld | 424 | Vue 3 internationalization: createI18n, useI18n, message syntax, pluralization, datetime and number formatting, lazy loading, and v10 to v12 migration. |
| vue-skilld | 420 | Work in `.vue` files against Vue 3.6: script setup, reactivity, Vapor Mode, SSR, and the API changes from 3.4 through 3.6.0-beta.17. |
| vuetify-skilld | 401 | Vuetify 4 Material components: createVuetify setup, components and labs, composables, theming, icons, locale and dates, SASS variables, treeshaking, and v3 to v4 migration. |
| pinia-skilld | 335 | Pinia stores: option and setup stores, state, getters, actions, subscriptions, plugins, SSR hydration, testing, and migration notes from v2 and v3 on a 4.0.3 baseline. |
| vue-router-skilld | 307 | Vue Router 5: typed routes, file-based routing, data loaders, and the `vite`, `auto-routes` and experimental entry points. |
| pinia-colada-skilld | 239 | Data fetching on Pinia with `@pinia/colada`: useQuery, useMutation, useInfiniteQuery, cache invalidation, optimistic updates, plugins and SSR. |
| vueuse-core-skilld | 217 | The `@vueuse/core` composables at v15: the current API surface, v14 to v15 migration rules, new composables such as useWebMCP and useLiveAnnouncer, and deprecations. |
| tanstack-vue-query-skilld | 217 | Async data with `@tanstack/vue-query` 5: query and mutation hooks, caching, and the query-core exports that pass through the adapter. |
| vee-validate-skilld | 186 | Vue form validation with vee-validate 4.15: useForm and defineField usage, schema patterns, typed schemas, and pitfalls since 4.9. |
| primevue-skilld | 183 | PrimeVue 5 components: setup with the PrimeUI license key, compound component usage, deprecated API replacements, and design token theming. |
| shadcn-vue-skilld | 173 | shadcn-vue work in Vue or Nuxt: init, add and migrate commands, components.json keys, registries, icon libraries, and the MCP server. |
| vueuse-components-skilld | 168 | Renderless `@vueuse/components`: 46 Use* and On* components plus 14 directives, with props, slot shapes, emits and directive binding syntax. |
| vue-test-utils-skilld | 167 | Component tests with `@vue/test-utils` 2.5.1: mount and shallowMount options, wrapper queries, findComponent, and migration from VTU v1. |
| vueuse-integrations-skilld | 145 | `@vueuse/integrations` wrappers for 12 libraries: useAxios, useSortable, useFocusTrap, useCookies, useIDBKeyval, useJwt, useQRCode and the rest. |
| motion-v-skilld | 145 | Motion for Vue 2.4.4: the motion component, AnimatePresence, variants, gestures, layout and scroll animation, motion values, and the Nuxt module. |
| reka-ui-skilld | 144 | Reka UI primitives: composing headless accessible components, version-specific API rules, and styling guidance for reka-ui 2.10.5. |
| tanstack-vue-table-skilld | 142 | TanStack Table v9 for Vue: useTable with explicit tableFeatures, reactive data, FlexRender, atom-based state, and the v8 to v9 breaking changes. |
| unhead-vue-skilld | 105 | Head management with `@unhead/vue` 3: useHead, useSeoMeta, useHeadSafe, useScript, and SSR or streaming SSR setup, and the reason not to install it under Nuxt. |
| vueuse-motion-skilld | 104 | Declarative animation with `@vueuse/motion` 3: the v-motion directive, Motion and MotionGroup components, useMotion and useSpring, and presets. |

The remaining 15 indexed listings range from 4 to 100 installs.

## Why This Matters for Hermes Agents

An agent writing Vue code without a skill produces the median of its training data, and the README makes the same point about this ecosystem: agents still struggle with Vue 3.5 APIs out of the box, while Vue 3.6, Pinia 4, Vue Router 5, VueUse 15 and Reka UI 2 are already shipping. Nine of the twenty busiest skills here pin one of those newer baselines in their H1, so a wrong answer is traceable to a stale skill rather than a mystery.

The citation style is the part that helps most in review. Statements come with package-relative paths such as `package.json:87-89` or `dist/index.d.ts:4-5`, which means a Hermes agent can open the installed package and check the claim instead of repeating documentation prose. That is the difference between advice and evidence when a dependency bump breaks a build.

Splitting VueUse into six skills is a context decision. `@vueuse/core`, `@vueuse/shared`, `@vueuse/components`, `@vueuse/integrations`, `@vueuse/motion` and the math package have different API surfaces and different baselines (core at 15.0.0, motion at 3.0.3), and loading one instead of a merged reference keeps the instructions specific and the token count lower.

The collection also carries its own maintenance tooling, which is a signal about freshness. `scripts/sync.mjs` regenerates the collection, `scripts/validate.mjs` and `scripts/naming.mjs` enforce structure and naming, and `.claude-plugin/marketplace.json` maps a plugin name to the skill directory behind it, which is the file the `/plugin install` route reads.

## Usage

| You say | What happens |
|---|---|
| "Add a Pinia store for the cart with SSR hydration" | pinia-skilld loads before the edit and uses the 4.x setup-store and hydration rules instead of the v2 patterns the model would default to. |
| "Our router guards stopped firing after the upgrade" | vue-router-skilld checks the v5 loader and typed route model, including which of the `vite`, `auto-routes` and experimental entry points apply. |
| "Wire a data table with server-side pagination" | tanstack-vue-table-skilld builds it on v9 useTable with explicit tableFeatures and FlexRender, and flags the v8 to v9 breaking changes on the way. |
| "Build a dialog that works with a screen reader" | reka-ui-skilld composes the headless primitives with the accessibility wiring already in place, rather than hand-rolled ARIA attributes. |
| "Format prices and dates for German and French users" | vue-i18n-skilld sets up number and datetime formatting against the locale message syntax and checks the pluralization rules for both. |
| "Write tests for this component's emitted events" | vue-test-utils-skilld uses 2.5.1 mount options and wrapper queries, and points at the VTU v1 differences that usually break a copied test. |
| "This code does not match the Vue 3.6 docs at all" | vue-skilld compares the code against the 3.6.0-beta.17 surface, including Vapor Mode and the 3.4 to 3.6 change list. |

## Verification

Probe the paths on the branch before installing anything. All three returned 200 when this guide was written:

```bash
for p in skills/vue-skilld/SKILL.md skills/pinia-skilld/SKILL.md skills/quasar-skilld/SKILL.md; do
  curl -s -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/skilld-dev/vue-ecosystem-skills/main/$p"
done
```

After an install, check that the directory names carry the `-skilld` suffix even though the filter names do not, and read the baseline version in the first heading:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c 'skilld$'
head -6 ~/.hermes/profiles/corpusiq/skills/pinia-skilld/SKILL.md
```

The count should match the number of skills you asked for, and the heading should read `pinia@4.0.3` rather than the version in the README comment. If the two disagree, the copy is stale.

One more check worth running on a real project: ask the agent where a claim came from. A correct answer cites a path in the installed package or a docs URL, which is how these skills are written. An answer with no citation is a sign the skill file did not load and the model answered from memory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| quasar-skilld | Pass | Pass | Pass |
| tanstack-vue-query-skilld | Pass | Pass | Pass |
| tanstack-vue-table-skilld | Pass | Pass | Pass |
| unovis-vue-skilld | Pass | Pass | Pass |
| unovis-ts-skilld | Pass | Pass | Pass |

The install surface is markdown. All 207 files under `skills/` are `.md` files, with no scripts, binaries or config inside any skill directory, so nothing in a skill runs on install or on load. The repository's `scripts/` directory (`sync.mjs`, `validate.mjs`, `naming.mjs`, plus their test files) is collection maintenance and is not installed with a skill. The root `package.json` defines `sync`, `sync:check`, `validate`, `lint` and `lint:fix` only, with no preinstall, postinstall or prepare lifecycle hook, so an `npx` install runs no repository code.

The risk that remains is instruction-level, and it is the same risk as any skill: these files tell an agent which API to prefer, which migration to follow and which patterns to avoid. A wrong instruction produces confident wrong code, and the version pinning means the instructions age. Read the `SKILL.md` for the library you are actually editing before you trust its advice on a project that sits on a different major version.

Two details are worth knowing before install. Some skills state environment limits that a project may not meet: `shadcn-vue` assumes Tailwind CSS 4, `quasar` and `vue-i18n` state Node 22 or newer, and `unhead` says not to install or configure it manually under Nuxt. And `primevue-skilld` documents setup with a PrimeUI license key, which is a commercial dependency rather than a credential you already hold.

No skill file carries a credential, and none of them executes anything itself; they are instructions. The supply chain to watch is npm, not the skills: every file describes a package you will install, and the versions named in the baselines are the ones the advice was verified against.

## Limitations

- Snapshot data, verified 2026-11-01: 5,930 combined installs across 35 indexed listings; 184 GitHub stars; MIT; last pushed 2026-10-10. Counts drift over time.
- The README's version comments lag the skill baselines, because each skill is rebuilt on release: it lists `pinia` at 3.0.4 against `pinia@4.0.3` in the skill, `vue` at 3.6.0-beta.6 against 3.6.0-beta.17, `vue-router` at 5.0.2 against 5.3.1, and `vueuse-core` at 14.2.1 against 15.0.0. Trust the `SKILL.md` heading, not the comment.
- Install names and directory names differ. The README carries 33 `--skill` names against 35 directories, with `formkit`, `motion-vue`, `tresjs` and `unhead` mapping to `formkit-core-skilld`, `motion-v-skilld`, `tresjs-core-skilld` and `unhead-vue-skilld`, while `slidev-cli-skilld` and `unovis-ts-skilld` have no install line in the README at all.
- The plugin manifest is narrower again. `.claude-plugin/marketplace.json` defines 32 plugins over 32 directories, so the marketplace route cannot reach `slidev-cli-skilld`, `unhead-vue-skilld` or `unovis-ts-skilld`; those three need the CLI or a directory copy.
- Nothing here targets Hermes. The documented routes are the skilld CLI, the skills.sh CLI and the Claude Code plugin marketplace, so the directory copy above is the supported path, and nothing updates it when skilld republishes.
- Several baselines are prereleases or brand new majors. The Vue skill is built on 3.6.0-beta.17, so its Vapor Mode guidance describes a beta, and Pinia 4, Vue Router 5, VueUse 15, Vuetify 4 and PrimeVue 5 advice will not apply to a project still on the previous major.

## Related

- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup)
- [Nuxt Skills - Vue, Nuxt and NuxtHub Agent Setup](/hermes/skills/catalog/onmax-nuxt-skills-setup)
- [web-quality-skills - Google-Grade Web Quality Audits](/hermes/skills/catalog/web-quality-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the two or three packages the repository actually imports. All 35 skills compete for the same trigger phrases, so a vague request for a component can pull in the wrong library's baseline.
- Add the README's relevance line to the agent file, verbatim: evaluate each installed skill against the current task, decide YES or NO, and invoke every YES skill before proceeding. Without it, a large collection sits unused because nothing tells the agent to consult one.
- Filter by the short package name the README uses, `--skill vue` or `--skill quasar`, then list what landed. The directory that arrives is `vue-skilld`, so the two names never match.
- Compare the `SKILL.md` heading against `package.json` before you trust migration advice. A skill built on `pinia@4.0.3` will describe v3 to v4 changes that do not exist in a project still on v2.
- Re-run the add command after a major upgrade rather than editing the copied file. skilld rebuilds each skill when its package releases, so a fresh install is the update path.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
