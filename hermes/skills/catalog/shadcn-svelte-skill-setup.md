---
title: "shadcn-svelte Skill - Svelte UI Components for Agents"
description: "huntabyte/shadcn-svelte on skills.sh: 7,148 combined installs in 1 indexed listing; the Svelte component CLI workflow with enforced composition rules."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shadcn-svelte-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "svelte", "ui components", "shadcn"]
---

# shadcn-svelte Skill - Setup Guide

**Source:** [huntabyte/shadcn-svelte](https://www.skills.sh/huntabyte/shadcn-svelte) via skills.sh - 7,148 combined installs in 1 indexed listing; first seen 2026-11-08 (Nov 8 2026 morning sweep, first documentation)
**GitHub:** 9,247 stars, MIT, last pushed 2026-11-03, a single SKILL.md at skills/shadcn-svelte with four rule files, four workflow references and an agents manifest beside it
**Category:** Svelte UI for agents: shadcn-svelte component copy-in, Tailwind styling and accessible Svelte 5 patterns
**Quality Tier:** 🟢 Recommended - MIT licence, 9,247 stars on the project, Pass on all three scanners, and a skill narrow enough to be reviewed in one sitting.

This is a documentation repository that happens to ship a skill. shadcn-svelte is the community Svelte port of shadcn/ui: components are not a package dependency, they are source files copied into your project by a CLI. That distribution model is why the skill can exist at all, because the thing an agent gets wrong is never the import of a component, it is the composition, the styling conventions and the alias resolution around it.

`skills/shadcn-svelte/SKILL.md` is 247 lines and reads like a house style guide rather than a tutorial. It opens by declaring that everything runs through the project's own package runner, then moves through import shape, five principle rules, five groups of critical rules with links to per-topic files, a key-patterns code block, a component selection table, and a workflow. The critical rules are the substance: `class` for layout and never for overriding component colors, no `space-x-*` or `space-y-*`, `size-*` when width equals height, no manual `dark:` overrides, `cn()` for conditional classes, no manual `z-index` on overlays.

The last group is the one that changes agent output most. Use components, not custom markup: callouts are `Alert`, empty states are `Empty`, toasts come from `svelte-sonner`, separators are `Separator`, loading placeholders are `Skeleton`, status is `Badge`. An agent that has read this file stops hand-rolling a styled `div` for a callout, which is the single most common way shadcn projects drift away from the design system.

## Installation

The skill installs through the Skills CLI, which is the index the listing comes from:

```bash
npx skills add huntabyte/shadcn-svelte
```

One honest note about the source: the repository README is the project README for the CLI and the docs site, and it carries no skill-specific install line. The skill directory at `skills/shadcn-svelte/` is what the Skills CLI indexes. If the CLI prompt asks for an agent, pick yours; the payload is plain markdown.

Once installed, the commands the SKILL.md teaches are the shadcn-svelte CLI's own, run through the project's package manager. It allows exactly three runners, `npx shadcn-svelte@latest`, `pnpm dlx shadcn-svelte@latest` and `bunx --bun shadcn-svelte@latest`, and says to substitute the one the project uses:

```bash
# initialize in an existing Svelte project
npx shadcn-svelte@latest init

# initialize from a preset string built on the docs site
npx shadcn-svelte@latest init --preset <code>

# browse components interactively, or add by name, or add everything
npx shadcn-svelte@latest add
npx shadcn-svelte@latest add button card dialog
npx shadcn-svelte@latest add --all

# refresh components already installed
npx shadcn-svelte@latest update button
npx shadcn-svelte@latest update --all --yes

# registry authors only
npx shadcn-svelte@latest registry build
```

For a design system built from a `DESIGN.md`, the skill's own sequence is `npx sv create <app>` to scaffold SvelteKit, then `init --preset <code>`, then `add --all --yes` in a new app or only the missing components in an existing one.

## What It Provides

One indexed listing carries the whole skill, and the pack's threshold is zero, so it appears below:

| Skill | Installs | Use For |
|---|---|---|
| shadcn-svelte | 7,148 | Component add, update and debug workflow for Svelte projects: alias-aware imports, composition rules, Tailwind conventions and accessibility requirements |

No rows fall below the threshold of 0, so there is no tail. The install count is the entire adoption signal for the skill, though the repository behind it is one of the larger Svelte projects on GitHub.

What the skill actually carries is a rulebook with teeth. Each critical-rule heading links to a file with incorrect and correct code pairs: `rules/styling.md`, `rules/forms.md`, `rules/composition.md` and `rules/icons.md`. Four workflow references sit beside them: `cli.md` for commands and flags, `customization.md` for theming and CSS variables, and `design-system.md` plus `design-system-page.md` for the DESIGN.md route. There is also an `evals` directory and a `scripts/showcase-coverage.mjs` check used by the design-system workflow.

Several rules exist because the failure is specific and recurring. Dialog, Sheet and Drawer always need a `Title`, with `class="sr-only"` when it should be visually hidden, because the component is unusable with a screen reader otherwise. `Avatar` always needs a `Fallback`. `Button` has no `isPending` or `isLoading` prop, so a loading button is a `Spinner` inside a `Button` with `data-icon` on the spinner. Tabs triggers live inside `Tabs.List`. Items live inside their Group.

Import shape is spelled out because agents guess it wrong: multi-part components are namespace imports such as `import * as Dialog from "$lib/components/ui/dialog"`, while single-component barrels are named imports such as `import { Button } from "$lib/components/ui/button"` and never `Button.Root`. Aliases come from `components.json`, not from a hardcoded `$lib` path.

## Why This Matters for Hermes Agents

Svelte 5 changed enough syntax that a model trained across React and older Svelte will produce code that compiles and still looks wrong: props scattered where snippets belong, `space-y-4` where the design system expects `flex flex-col gap-4`, a raw `bg-blue-500` where a semantic token exists. None of those errors fail a build, which is exactly the class of mistake an agent ships without noticing.

The second reason is that shadcn-svelte components are source, not dependencies. An agent working in one of these projects is editing files the project owns, so the way it composes them becomes permanent. A skill that pins composition rules prevents a codebase from slowly accumulating three different card layouts.

For Hermes, the practical use is the component-docs habit the skill pushes: open `https://shadcn-svelte.com/docs/components/<name>.md` before writing or fixing a component, because the markdown variant of the docs page is directly readable by a fetch tool. That turns a guess about an API into a read, and it is cheaper than a failed build.

The tool permission line is also a small model of restraint. The skill declares `allowed-tools` as three Bash patterns, all of them the shadcn-svelte CLI behind a package runner, and `user-invocable: false`, so it loads automatically on component work rather than being called by name. If your harness honours that frontmatter, the skill cannot reach for anything else.

## Usage

| You say | What happens |
|---|---|
| "Add a data table page to this Svelte app" | Reads `components.json`, lists the ui directory, adds only the missing parts, then verifies composition |
| "Why does this dialog have no accessible name" | Points at the missing `Dialog.Title` rule rather than patching the symptom |
| "Make this form look right" | Rewrites the layout as `Field.FieldGroup` with `Field.Field`, not a `div` with `space-y-*` |
| "Build a dashboard shell" | Composes Sidebar, Card, Chart and Table instead of writing new markup |
| "Apply this DESIGN.md" | Follows the design-system workflow: scaffold, init with a preset, add all, map tokens, build the page, verify in a browser |
| "Update the button component" | Uses `update`, then reviews with `git diff`, and never runs `add --overwrite` without approval |
| "Add this component from a registry URL" | Confirms the registry first, then fixes hardcoded imports to match the project aliases |

The update path carries an explicit warning worth repeating: never use `--overwrite` on `add` without the user's approval when it would destroy intentional edits, because the project's copies are the source of truth once they have been customized.

## Verification

Read the skill before installing it. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/huntabyte/shadcn-svelte/main/skills/shadcn-svelte/SKILL.md | head -40
```

It should open with frontmatter naming `shadcn-svelte`, `user-invocable: false`, and an `allowed-tools` line listing exactly `npx`, `pnpm dlx` and `bunx --bun` runs of the CLI. The first body line is the `# shadcn-svelte` heading, followed by a blockquote telling the agent to run every CLI command through the project's own package runner.

After install, confirm the skill resolved and that the project is a shadcn-svelte project at all, because that is what the skill's trigger keys on:

```bash
ls ~/.claude/skills/shadcn-svelte/SKILL.md
cat components.json
```

The first should exist. The second should print a config with `aliases`, `tailwind`, `style` and `iconLibrary`; if it does not exist, the project has not been initialised and `npx shadcn-svelte@latest init` comes first.

A cheap behavioural check: ask for a settings page and read the diff. If it contains `space-y-*`, a raw `bg-blue-500`, a `div` standing in for `Alert`, or a `Button` with an `isLoading` prop, the skill did not load. If it contains `flex flex-col gap-*`, semantic tokens and `Field.FieldGroup`, it did.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08). Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shadcn-svelte | Pass | Pass | Pass |

The skill is prose plus reference markdown plus one small Node script, `scripts/showcase-coverage.mjs`, used to check that every component in a design system has a showcase. Nothing in the reasoning path executes.

The blast radius is the CLI, not the skill. `add` and `update` write files into the user's project and can overwrite customized components, which is why the skill gates `--overwrite` behind explicit approval and recommends `git diff` after every update. Adding from a third-party registry URL is the other sharp edge, since that pulls source from a host neither shadcn-svelte nor the skill controls; the skill requires confirming the URL before running `add`, and requires fixing hardcoded imports afterwards so a foreign item does not leak a path convention into your project.

Licence status is clean: MIT, published under `LICENSE.md` in the repository root, and the README states it in the same breath. The repository is not archived. One honest caveat: the 9,247 stars describe the shadcn-svelte project, not the skill, so a Pass verdict here says nothing about the wider trust surface of the CLI you will actually run.

## Limitations

- Snapshot data, verified 2026-11-08: 7,148 combined installs in 1 indexed listing, 9,247 GitHub stars, MIT, last pushed 2026-11-03. Counts drift.
- One listing against one skill directory, so there is no drift to report between index and repository in this snapshot. That is a thin signal rather than a strong one.
- Star count is the project's. The skill is a recent addition to a monorepo that also holds the CLI, the docs site and the registry, so the repository's popularity is not evidence about the skill's quality.
- The skill ships inside the documentation repository, which means it can fall behind the CLI at `packages/cli` between releases. There is no version pin linking the SKILL.md to a CLI version, so a rule can be correct for one release and stale for the next.
- It assumes a Svelte project with Tailwind and a `components.json`. In a fresh directory nothing it says applies until `init` has run, and in a React project none of it applies at all.
- The relative links inside SKILL.md (`./rules/styling.md`, `./cli.md`) only resolve when the whole skill directory is installed. Copying just `SKILL.md` into a prompt loses every rule file.
- The repository README documents no skill install path, so the Skills CLI command is the index's, not the maintainer's documentation. I verified the SKILL.md URL directly and did not run the installer.

## Related

- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup)
- [Svelte AI Tools - Official Svelte and SvelteKit Setup](/hermes/skills/catalog/svelte-ai-tools-setup)

## Pro Tips

- Run `add` with no arguments first in an unfamiliar project. It prints the interactive component list, which is a faster inventory than reading the docs index and cheaper than adding something twice.
- Read the four rule files, not just SKILL.md. The summary lines name the rule; the rule files carry the incorrect and correct pairs, and the pairs are what an agent pattern-matches against.
- Let `components.json` decide the imports. Hardcoding `$lib/components/ui` works in the default template and breaks in every project that moved `aliases.ui`, which is why the skill calls it out twice.
- Use `update` with a clean tree. Committing first makes the merge visible in `git diff`, and a customized component that conflicts is a decision you want to see rather than a file that silently took the registry version.
- Fetch the markdown docs page instead of the HTML one. `shadcn-svelte.com/docs/components/<name>.md` returns the component doc as readable text, which is a single request rather than a scrape.
- The design-system route is the highest-leverage use. Mapping a `DESIGN.md` onto CSS variables once, then adding every component against those tokens, beats styling pages component by component later.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
