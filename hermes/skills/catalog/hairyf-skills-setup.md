---
title: "Hairyf Skills - Vue, Nuxt and Tooling Collection"
description: "hairyf/skills: 25.7K combined installs. Eighty generated agent skills for Vue, Nuxt, Vite, React, testing and build tooling, plus starters."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hairyf-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "vue", "nuxt", "vite", "tooling"]
---

# Hairyf Skills - Setup Guide

**Source:** [hairyf/skills](https://www.skills.sh/hairyf/skills) via skills.sh - 25.7K combined installs across 80 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [hairyf/skills](https://github.com/hairyf/skills) - 26 stars, MIT (`LICENSE.md`, copyright Hairyf), branch main, last pushed 2026-10-14; 80 skill directories under `skills/`, one `SKILL.md` each plus a `references/` folder of topic files, 1,966 Markdown files and about 11 MB in total, with upstream documentation cloned as git submodules under `sources/`

**Category:** Framework and tooling knowledge for agents across Vue, Nuxt, Vite, React, testing and bundling, plus scaffolding starters and a small media and Minecraft wing

**Quality Tier:** 🟢 Green - all nine sampled verdicts across three listings pass on Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT licence file

Hairy's Skills is a fork of `antfu/skills`, maintained by Hairyf, and the README is honest about what it is: a curated collection of Agent Skills built on Anthony Fu's collection and extended with skills reflecting Hairyf's own preferences and projects. It doubles as a proof of concept for generating skills from source documentation and keeping them in sync. `meta.ts` maps upstream repositories such as react.dev, vuejs/docs, nuxt/nuxt, tailwindcss.com and motiondivision/motion to output skill names, `.gitmodules` clones those repositories into `sources/`, and the generated output is committed under `skills/`.

The tree holds 80 skill directories and 1,966 Markdown files. Coverage runs from Vue, Nuxt, Vite, UnoCSS, Pinia and Vitest through React and Next.js to Tailwind CSS, Motion and Anime.js, then out to Tauri, Electron, Flutter and React Native, OpenAPI 2.0 and 3.2, and a set of `arch-*` starter templates. A handful have nothing to do with front-end work: `imagine`, `sonic` and `vision` for media generation, and a Minecraft group covering mods, models, textures and shader work. The README's own warning belongs up front rather than in a footnote: "I haven't fully tested how well the skills perform in practice".

## Installation

The README gives two commands, both through the skills CLI:

```bash
# the whole collection
pnpx skills add hairyf/skills

# the whole collection, installed globally
pnpx skills add hairyf/skills --all -g
```

Install one skill at a time instead when you are wiring this into a working profile. Eighty skills mean eighty trigger descriptions competing for the same requests:

```bash
npx skills add hairyf/skills --skill nuxt
npx skills add hairyf/skills --skill vue-best-practices
```

The manual route is a clone plus a copy, because every skill is self-contained under `skills/`:

```bash
git clone --depth 1 https://github.com/hairyf/skills.git /tmp/hairyf-skills
ls -d /tmp/hairyf-skills/skills/*/ | wc -l
cp -r /tmp/hairyf-skills/skills/nuxt ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole directory, not only `SKILL.md`. The generated skills are index pages: the `nuxt` skill opens with a topic table and routes each row to one of 18 reference files, from `core-directory-structure.md` to `best-practices-ssr.md`. Adding `--recurse-submodules` matters only if you plan to regenerate rather than install, since `sources/` holds the upstream documentation checkouts.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tailwindcss | 3,884 | Utility-first styling: responsive layouts, theme variables and design systems. |
| hairy-utils | 1,258 | Working with the @hairy/utils core utility package. |
| motion | 1,148 | Animations, gestures, layout transitions and scroll effects with Motion for JS, React and Vue. |
| openapi-specification-v3.2 | 906 | Authoring and validating OpenAPI 3.2 documents, including JSON Schema 2020-12. |
| next | 858 | Next.js App Router, Server Components, caching and Server Actions. |
| react-use | 848 | Picking hooks for sensors, UI, animation, side effects and state. |
| vitest | 786 | Writing tests, mocking, coverage configuration and test filtering. |
| valtio | 784 | Proxy-based reactive state for React and vanilla JavaScript. |
| openapi-specification-v2 | 779 | Writing or validating Swagger 2.0 specs and generating clients and docs. |
| valtio-define | 753 | Working with the valtio-define helper package. |
| hairy-react-lib | 752 | Using the @hairy/react-lib hooks and components. |
| unjs | 732 | h3, nitro, ofetch, unstorage and other universal JavaScript builds. |
| overlastic | 678 | Working with the Overlastic library. |
| hairy | 657 | Hairyf's opinionated defaults for TypeScript, ESLint, pnpm and Vitest. |
| undocs | 630 | Documentation sites built with Nuxt Content and Nuxt UI. |
| writing-humanizer-zh | 627 | Removing AI-writing tells from Simplified Chinese copy. |
| tsdown | 619 | Bundling TypeScript libraries with Rolldown and emitting type declarations. |
| arch-tsdown-monorepo | 611 | Scaffolding a pnpm monorepo with tsdown per package and trusted publishing. |
| tauri | 415 | Tauri apps: Rust backend, WebView frontend, IPC, security and plugins. |
| react-native-reusables | 377 | shadcn-style components for React Native with NativeWind or Uniwind. |

The remaining 60 indexed listings range from 2 to 374 installs.

The generated skills share one shape: frontmatter with `name`, a trigger-heavy `description`, and `metadata` recording author, version and source repository, followed by a table of topics that points into `references/`. That is why the collection can be large without being expensive, because an agent loads one `SKILL.md` of a few hundred lines and follows only the reference links its task needs. The hand-maintained skills listed in the README (`hairy`, `antfu`, `github-workflow`, `create-skill-from-repo`, `dsh-plugin-creator`, the two OpenAPI specs and the media skills) are prose rather than generated, so they read differently: fewer reference tables, more direct instruction.

## Why This Matters for Hermes Agents

The context budget is the whole argument for this format. Nearly 2,000 Markdown files would be impossible to carry into a session; as skills they cost one description each until a request matches, and the README makes that point itself when it contrasts skills with an AGENTS.md that loads everything upfront.

Generated skills carry provenance. The `nuxt` skill states that it is based on Nuxt 3.x and was generated on 2026-01-28, with metadata naming the upstream repository. An agent that knows which framework generation it is reading is less likely to suggest an API that was removed two majors ago, and a stale skill is visible as stale rather than merely wrong.

The `arch-*` skills are the part with no equivalent in a documentation set. They are opinions about how to scaffold a Nuxt app, a tsdown library, a CLI, a monorepo, a VSCode extension or a browser extension, which is exactly the kind of decision an agent makes badly by default and a reviewer then pays for.

The risk is overlap. Eighty skills mean many near-duplicate triggers across the Vue and React ecosystems, and the router, not the model, decides which one loads. Installing all of them into one profile is how an agent ends up reading the React skill for a Vue request.

## Usage

| You say | What happens |
|---|---|
| "Set up linting and formatting for this new TypeScript library" | `hairy` or `antfu` applies the opinionated defaults: pnpm, @antfu/eslint-config, Vitest, strict TypeScript. |
| "Scaffold a lightweight Vue SPA" | `arch-nuxt-lite` lays out the Vitesse Lite stack: Vite, Vue 3, file-based routing, UnoCSS and VueUse. |
| "Write tests for this composable" | `vitest` covers config, mocking, coverage and test filtering in a Vite project. |
| "Publish this package as ESM with type declarations" | `tsdown` bundles with Rolldown and emits declarations, with the `arch-tsdown` starter for layout. |
| "Build a Nuxt module with runtime code and types" | `arch-nuxt-module-builder` scaffolds with @nuxt/module-builder. |
| "Move this React Native app from NativeWind to Uniwind" | `migrate-nativewind-to-uniwind` handles package removal, config migration, Tailwind 4 and theme conversion. |
| "Make this Chinese post sound less like a model wrote it" | `writing-humanizer-zh` rewrites Simplified Chinese copy against a catalogue of AI-writing patterns. |

## Verification

The raw paths below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/hairyf/skills/main/skills/tailwindcss/SKILL.md

curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/hairyf/skills/main/skills/nuxt/SKILL.md
```

Then count what a clone actually delivers, and inspect one generated skill:

```bash
git clone --depth 1 https://github.com/hairyf/skills.git /tmp/hairyf-skills
ls -d /tmp/hairyf-skills/skills/*/ | wc -l
find /tmp/hairyf-skills/skills -name SKILL.md | wc -l
ls /tmp/hairyf-skills/skills/nuxt/references | wc -l
head -8 /tmp/hairyf-skills/skills/nuxt/SKILL.md
```

The counts should print 80, 80 and 18. `head` should show `name: nuxt`, the description with its trigger phrases, and `metadata` naming Anthony Fu as author with a version stamp. If a skill directory holds only `SKILL.md` and no `references/`, the copy came from a partial checkout and the skill will answer from headings alone.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tailwindcss | Pass | Pass | Pass |
| hairy-utils | Pass | Pass | Pass |
| motion | Pass | Pass | Pass |

The three sampled listings are documentation only, and most of the tree is Markdown, but the repository as a whole is not inert. `skills/vision/scripts/vision.js` is a Node CLI that sends images to an OpenAI-compatible vision model, `skills/sonic/scripts/install/woosh.sh` and `mmaudio.sh` install local audio tooling, `skills/minecraft-texture/scripts/mc_texture.py` post-processes images into block textures, and `skills/create-skill/scripts` can initialise and package new skills. None of that runs until a skill is invoked, but installing all 80 copies all of it into the profile, and the green tier reflects three sampled listings rather than an audit of every script.

The content is also third-hand in places: many skills are generated from upstream documentation repositories cloned as submodules, and the README credits further sources such as vercel-labs/agent-skills, blader/humanizer and uni-stack/uniwind. Check the upstream terms before redistributing a generated skill, and treat `sonic` and `vision` as network clients that need keys rather than as pure knowledge.

## Limitations

- Snapshot data, verified 2026-11-03: 25,708 combined installs across 80 indexed listings; 26 GitHub stars; MIT via `LICENSE.md`; last pushed 2026-10-14. Counts drift over time.
- Install counts and repository attention disagree sharply: 25.7K installs against 26 stars. Distribution comes through skills.sh, so treat stars as a weak signal here.
- The README calls the collection a proof of concept and says the author has not fully tested how well the skills perform in practice. Read a skill before you rely on it.
- Generated skills are only as current as the commit they were generated from. The `nuxt` skill is based on Nuxt 3.x as of 2026-01-28, and nothing in the install path refreshes it.
- Several skills are Chinese-first (`uniapp`, `uniapp-x`, `writing-styles-juejin`, `writing-humanizer-zh`) and produce or expect Chinese-language output.
- The 60 listings below 377 installs include most of the specialised material (Minecraft, Electron, Flutter, the smaller arch starters), so the table above is the popular half rather than the interesting half.

## Related

- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup)
- [Anthony Fu Skills - Vue, Vite and TS Tooling Setup](/hermes/skills/catalog/antfu-skills-setup)
- [Nuxt Skills - Vue, Nuxt and NuxtHub Agent Setup](/hermes/skills/catalog/onmax-nuxt-skills-setup)
- [Vue Ecosystem Skills - Version-Aware Vue Context](/hermes/skills/catalog/vue-ecosystem-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the framework skill plus its `arch-*` starter, not the whole collection. Two or three skills cover a normal Vue or Nuxt project.
- Check `references/` before trusting a generated skill. A directory with four reference files is a summary; one with eighteen is close to the upstream docs.
- Read the `metadata.source` and generation date when a framework ships a major version, and regenerate rather than patch by hand.
- The fork is a working template for the same trick in another ecosystem: `meta.ts` lists source repositories, and the README documents `nr start init`, `sync` and `cleanup` as the maintenance loop.
- Prefer the hand-maintained skills for conventions (`hairy`, `antfu`, `github-workflow`) and the generated ones for API surface, because the two are maintained in different ways.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
