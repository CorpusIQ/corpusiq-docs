---
title: "shadcn Skill - shadcn/ui Component Workflows Setup"
description: "Setup guide for the official shadcn skill from shadcn-ui/ui: project context, component docs, registry search, and always-on UI rules for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shadcn-ui-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "shadcn", "ui components", "frontend"]
---

# shadcn Skill - Setup Guide

**Source:** [shadcn-ui/ui](https://www.skills.sh/shadcn-ui/ui/shadcn) via skills.sh - 93.9K installs (first seen Mar 6, 2026)
**GitHub:** [shadcn-ui/ui](https://github.com/shadcn-ui/ui) (125,283 stars, MIT license; very active - pushed Oct 8, 2026; skill file `skills/shadcn/SKILL.md`, ~19.4 KB)
**Category:** Frontend / UI Components
**Quality Tier:** 🟢 Production - official shadcn publisher, MIT, actively developed

The official shadcn skill for AI coding agents, published by the shadcn/ui team in their own repository. It manages shadcn components and projects: adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. The skill injects live project context, fetches component docs before code is written, and enforces always-on rules with Incorrect/Correct code pairs in linked reference files, so agents build with documented shadcn patterns instead of inventing UI.

---

## Installation

```bash
# Owner/repo shorthand
npx skills add shadcn-ui/ui --skill shadcn

# Full GitHub URL
npx skills add https://github.com/shadcn-ui/ui --skill shadcn
```

The skill is agent-facing (`user-invocable: false`): it activates from project context rather than as a slash command. It has no MCP server or external dependencies; the commands it runs are the shadcn CLI executed through the project's own package runner (`npx shadcn@latest`, `pnpm dlx shadcn@latest`, or `bunx --bun shadcn@latest`).

## What It Provides

| Capability | How |
|---|---|
| Project context injection | `npx shadcn@latest info --json` reads the project config (aliases, framework, base, icon library, Tailwind version, resolved paths, package manager, preset) and the installed component list before work starts |
| Component docs and examples | `npx shadcn@latest docs <component>` returns documentation, example, and API reference URLs; the skill fetches them before creating, fixing, debugging, or using a component |
| Registry search | `npx shadcn@latest search` across configured registries, `view` for items not yet installed, and `add owner/repo/item` for community items (`@magicui`, `@tailark`, and more) |
| Presets and templates | Named presets (`nova`, `vega`, `maia`, `lyra`, `mira`, `luma`) and base62 preset codes; templates `next`, `vite`, `start`, `react-router`, `astro`, `laravel`; monorepo scaffolding |
| Enforced UI rules | Always-on rules with Incorrect/Correct pairs in linked files: no `space-x`/`space-y` (use `flex` with `gap-*`), `size-*` for equal dimensions, semantic color tokens, `cn()` for conditional classes, `FieldGroup`/`Field` forms |
| Safe component updates | `--dry-run` and `--diff` previews for merges that preserve local changes; `--view` to inspect items before installing; `--overwrite` requires explicit approval |
| Chat UI primitives | `MessageScroller`, `Message`, `Bubble`, `Attachment`, and `Marker` composition for chat interfaces, with streaming follow and jump-to-latest built in |
| Component selection map | A need-to-component matrix: Button variants, form inputs, overlays (Dialog, Sheet, Drawer), feedback (Alert, Skeleton, Spinner), charts, navigation, menus, empty states |

## Why This Matters for Hermes Agents

Frontend work on React and Next.js codebases is a core Hermes agent task, and shadcn/ui is a widely used React component layer. This skill keeps agents on documented shadcn patterns and semantic tokens instead of inventing UI: it injects the project's real aliases, framework, base, and icon library, then enforces them in generated code, so components drop into the existing design system rather than fighting it. It also fires on any project with a `components.json` file, so it activates without extra prompting whenever a Hermes agent opens a shadcn-based repo.

## Usage

| You say | What happens |
|---|---|
| "Add the shadcn table component to this project" | Checks installed components, fetches docs, adds via the project's package runner |
| "Create an app with --preset base-nova" | Scaffolds a new project from a named preset with the right template and package manager |
| "Run shadcn init in this repo" | Initializes an existing project via the CLI, writing config and CSS variables |
| "Switch this project to --preset a2r6bw" | Decodes the code, asks overwrite / partial / merge / skip, then applies |
| "Find a login block in the shadcn registry" | Searches configured registries before writing any custom markup |
| "Update the button component but keep my local changes" | Uses `--dry-run` and `--diff` to merge upstream changes safely |

The skill also activates on its own triggers: any mention of shadcn/ui, component registries, presets, `shadcn init`, "create an app with --preset", or any project containing a `components.json` file. It is agent-facing, so there is no slash command to learn.

## Verification

```bash
# Confirm the skill is installed
npx skills list | grep shadcn

# Hermes users: confirm it is registered as a skill
hermes skills list | grep shadcn

# Functional check inside a shadcn project (commands the skill itself runs)
npx shadcn@latest info --json    # project config plus installed components
npx shadcn@latest docs button    # documentation and example URLs
```

## Security

skills.sh verdicts for the shadcn skill (verified Oct 8, 2026):

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shadcn | Pass | Warn | Pass |

**Known caution:** the skills.sh page warns that this skill contains shell command directives (a `!` prefix that executes system commands and injects the output). Here the injected commands are the project's package-runner invocations of the shadcn CLI (`npx shadcn@latest`, `pnpm dlx shadcn@latest`, `bunx --bun shadcn@latest`), the most notable being `info --json` for project context. They read project state rather than modify it, but reviewers should treat the skill as executing local CLI commands: review the commands and run it in repositories you trust.

## Related

- [Jezweb Skills - 96-Skill Web Dev & Design Suite Setup](/hermes/skills/catalog/jezweb-skills-setup) - includes shadcn/ui coverage among 96 web development and design skills
- [Meng To Skills Setup Guide for Hermes Agents](/hermes/skills/catalog/mengto-skills-setup) - frontend, motion, and visual design skills from the Design+Code founder
- [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/hermes/skills/catalog/podo-design-agent-skills-setup) - curated design-skill catalog covering UI craft, motion, Figma, and accessibility

## Pro Tips

1. **Match the project's package runner.** The skill requires `npx shadcn@latest`, `pnpm dlx shadcn@latest`, or `bunx --bun shadcn@latest` based on the `packageManager` field from project context; matching it keeps commands consistent with the project setup.
2. **Docs before code.** For every component you create, fix, debug, or use, run `npx shadcn@latest docs <component>` and fetch the returned URLs first; the skill's workflow is built to work from real API docs instead of guessing.
3. **Check before you add.** `info --json` lists installed components, and the skill guards both directions: do not import components that have not been added, and do not re-add ones already installed.
4. **Update with `--dry-run` and `--diff`.** Smart merges preserve local changes, a blind `--overwrite` needs explicit approval, and fetching raw component files from GitHub by hand is ruled out by the skill.
5. **Review what a community registry added.** After adding items from third-party registries (for example `@magicui`), read the new files: rewrite hardcoded import paths to the project's `ui` alias and swap icons to the project's `iconLibrary`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
