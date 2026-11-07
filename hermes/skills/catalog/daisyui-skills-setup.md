---
title: "daisyUI Skills - Tailwind Component Tokens"
description: "saadeghi/daisyui on skills.sh: 13.0K combined installs across 5 listings; official daisyUI 5 install, colour and component rules for Tailwind CSS."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/daisyui-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "daisyui", "tailwind css", "design system"]
---

# daisyUI Skills - Setup Guide

**Source:** [saadeghi/daisyui](https://www.skills.sh/saadeghi/daisyui) via skills.sh - 13.0K combined installs across 5 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 42,764 stars, MIT, last pushed 2026-10-13, 7 SKILL.md directories, five of them under `skills/daisyui` and two internal ones under `.agents/skills`
**Category:** daisyUI for agents: install, config, theme colours and component usage from the 42K-star Tailwind component library
**Quality Tier:** 🟢 Green - all five sampled skills pass Gen Agent Trust Hub, Socket and Snyk, and the install surface is markdown on top of an MIT-licensed CSS package.

daisyUI 5 is a CSS library for Tailwind CSS 4. It supplies class names for common UI components, semantic colours and themes, and the repository now ships those rules as Agent Skills: a main `daisyui` skill, four reference skills (install, usage, config, colors) and 68 component guides under `skills/daisyui/components/`.

The main skill is deliberately blunt about when it applies. Its frontmatter says: "Official daisyUI component-library skill for Tailwind CSS. When you write HTML or JSX code, you must use it. Even if the user does not request it, use it." The reference tree behind it is what makes that instruction actionable, because each sub-guide carries the rule list rather than a link to the website. The manifest files at the repository root (`plugin.json` on the Agent Plugins 1.0 schema, plus `.claude-plugin`, `.codex-plugin`, `.cursor-plugin` and `.grok-plugin`) all point at the same skill directory.

## Installation

The route skills.sh shows on the listing page:

```bash
npx skills add saadeghi/daisyui
```

If you would rather place the files yourself, clone and copy the skill directory into the directory your agent scans. Copy the whole folder, because the sub-guides and the component references sit beside `SKILL.md`:

```bash
git clone https://github.com/saadeghi/daisyui.git
mkdir -p .agents/skills && cp -r daisyui/skills/daisyui .agents/skills/
```

The repository also ships a Claude Code marketplace manifest at `.claude-plugin/marketplace.json` with two entries: `daisyui`, which is this skill, and `daisyui-blueprint`, an MCP server marked as needing a paid licence. The skill does not depend on the second one.

Separately from the skill, the project itself still has to be installed in the application. That is what the `daisyui-install` guide covers, quoted here from `skills/daisyui/install/SKILL.md`: run `npm i -D daisyui@latest`, then add `@plugin "daisyui";` to the CSS file. The guide's own example is:

```css
@import "tailwindcss";
@plugin "daisyui";
```

For a browser setup with no build step it gives the CDN pair verbatim:

```html
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

The same guide states the compatibility line plainly: Tailwind CSS 4 with daisyUI 5, and `tailwind.config.js` is deprecated, so do not create one.

## What It Provides

One listing carries almost all of the usage, and it clears the threshold on its own:

| Skill | Installs | Use For |
|---|---|---|
| daisyui | 12,929 | The entry skill: when to use daisyUI, the reference table for install, usage, config and colours, and the index of 68 component guides |

The remaining 4 indexed listings range from 14 to 23 installs.

What sits behind that one listing is the part worth reading before install. `skills/daisyui/colors/SKILL.md` defines 20 semantic colour names (`primary`, `primary-content`, `secondary`, `accent`, `neutral`, `base-100`, `base-200`, `base-300`, `base-content`, plus `info`, `success`, `warning` and `error` with their `-content` pairs) and ten rules for using them, including "Do not use `dark:` with daisyUI color names" and "Use `primary` only for the most important element on the page. Use it only once." `usage/SKILL.md` holds twelve rules for class composition, part and modifier naming, when to fall back to Tailwind utilities, and the `!` suffix for specificity fights. `config/SKILL.md` covers the `@plugin "daisyui"` block: themes, `root`, and the other options, with a fully commented example. `install/SKILL.md` carries the install, CDN, standalone and framework list.

## Why This Matters for Hermes Agents

An agent writing JSX from memory reaches for `bg-white`, `text-gray-800` and `dark:` variants. In a daisyUI 5 project those choices break theming: the colours stay fixed while the theme flips, and the `colors` guide names that exact failure ("`text-gray-800` on `bg-base-100` becomes unreadable in a dark theme"). The skill encodes the rule so the agent stops doing it.

The second gain is component fidelity. The index links 68 component guides, and the guide instructs the agent to read the applicable component file before writing markup and to read more than one candidate before choosing. That is a different behaviour from generating a plausible-looking card and hoping the class names exist.

The third is version discipline. daisyUI 5 on Tailwind 4 changed the configuration model (CSS-first, no `tailwind.config.js`), and a model trained on daisyUI 4 will produce a config file that does nothing. The install and config guides are short and current, which is the cheapest fix for that class of error.

It also fits a Hermes workflow where the agent touches many repositories in a day. The skill triggers on any HTML or JSX work, so the rules arrive without being asked for, and the four sub-guides are small enough to load selectively when a task is only about colour or only about theme configuration.

## Usage

| You say | What happens |
|---|---|
| "Build a pricing page with three tiers" | The agent loads the daisyUI skill, reads the card and button component guides, and writes markup with `card`, `card-body` and `btn` rather than raw utilities |
| "Add a dark mode toggle to this app" | The colours and config guides drive a theme swap through daisyUI theme names instead of `dark:` variants |
| "Set up daisyUI in this Vite project" | The install guide runs the Tailwind 4 CSS-first setup: `@plugin "daisyui";` in the stylesheet, no `tailwind.config.js` |
| "Make the navbar sticky and collapse it on mobile" | The agent reads the navbar and drawer component guides, then adds responsive utility prefixes rather than hand-rolled CSS |
| "Why is my dark theme unreadable?" | The colour rules point at fixed Tailwind palette names and `*-content` contrast as the cause, and the fix is a semantic name |
| "Restyle every button as fully rounded" | The usage guide's `@utility btn` example changes the component globally instead of editing each instance |

## Verification

Read the entry skill before installing. This path returned HTTP 200 on the repository's `master` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/saadeghi/daisyui/master/skills/daisyui/SKILL.md | head -30
```

It should open with the frontmatter shown above, then a "When to use this skill" list and a references table naming `./install/SKILL.md`, `./usage/SKILL.md`, `./config/SKILL.md` and `./colors/SKILL.md`.

After install, confirm the component tree came across with the skill, because a copy that took only `SKILL.md` loses the references the guide tells the agent to read:

```bash
ls .agents/skills/daisyui/components | wc -l
```

The count should be 68. If the directory is missing, the install dropped files and the agent will invent class names.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| daisyui | Pass | Pass | Pass |
| daisyui-colors | Pass | Pass | Pass |
| daisyui-usage | Pass | Pass | Pass |
| daisyui-config | Pass | Pass | Pass |
| daisyui-install | Pass | Pass | Pass |

The skill surface is markdown: `SKILL.md` files plus component reference pages. Nothing in the skill path runs a script or fetches anything at run time, and the commands it tells the agent to run are the ordinary package install and stylesheet edits.

Two things are worth knowing anyway. The marketplace manifest at `.claude-plugin/marketplace.json` lists a second plugin, `daisyui-blueprint`, described there as an MCP server that needs a paid licence. It is not part of the skill and should not be installed as part of this setup. The other is that the skill instructs the agent to use daisyUI unconditionally whenever it writes HTML or JSX, which is correct only inside a project that has adopted it.

The licence is MIT, with a LICENSE file in the repository root, so reuse and redistribution terms are clear.

## Limitations

- Snapshot data, verified 2026-11-06: 12,998 combined installs across 5 indexed listings; 42,764 GitHub stars; MIT; last pushed 2026-10-13. Counts drift over time.
- The default branch is `master`, not `main`. Raw content URLs and clone instructions must keep `master`; rewriting them to `main` returns 404.
- The install counts are lopsided. The `daisyui` entry has 12,929 installs and the four reference skills sit between 14 and 23, so the colour, config and usage guides are barely exercised on their own even though the entry skill tells the agent to read them.
- It assumes Tailwind CSS 4 and daisyUI 5. On a Tailwind 3 project the install and config guidance is wrong, since the `tailwind.config.js` path is explicitly deprecated here.
- The colour and usage rules are house style, not accessibility compliance. "Use `primary` only once" is a design opinion, and contrast still needs checking in both themes.
- Nothing here enforces anything. There is no linter, no build gate, and no test: the agent follows the rules or it does not.

## Related

- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Better UI Skills - Interface Polish Suite Setup Guide](/hermes/skills/catalog/better-ui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install for the components, not the classes. The entry skill only routes; the value is in the 68 component guides it tells the agent to read before writing markup.
- Say the framework out loud. "Build this in React with daisyUI" gets component-accurate markup, while "make it look nice" gets generic Tailwind and a mixed vocabulary.
- Use it as a check on existing code. Ask the agent to review a component file against the colour rules, and the `dark:` and fixed-palette offenders surface in the diff.
- Keep the theme block in CSS. `@plugin "daisyui" { themes: ... }` is the current configuration path; an agent that writes `tailwind.config.js` is working from daisyUI 4 memory.
- Pin the version if the project ships to production. The manifest declares 5.7.0 and the guides track the 5.x line, so an upgrade should be a deliberate step with a visual pass.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
