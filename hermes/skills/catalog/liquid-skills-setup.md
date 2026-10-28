---
title: "Liquid Skills - Shopify Theme Standards and A11y Setup"
description: "Benjamin Sehl's Shopify Liquid skills: 9.4K combined installs across 3 skills for Liquid syntax, theme CSS/JS standards, and WCAG 2.2 a11y patterns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/liquid-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "shopify", "liquid", "accessibility"]
---

# Liquid Skills - Shopify Theme Setup Guide

**Source:** [benjaminsehl/liquid-skills](https://www.skills.sh/benjaminsehl/liquid-skills) via skills.sh - 9.4K combined installs across 3 indexed listings; verified 2026-10-27 (Oct 27 sweep)

**GitHub:** [benjaminsehl/liquid-skills](https://github.com/benjaminsehl/liquid-skills) - 121 stars, no LICENSE file at the repo root, branch main, 3 skill directories under `skills/` each holding a `SKILL.md` plus a `references/` folder, and a Claude Code marketplace manifest at `.claude-plugin/marketplace.json`; the clone's head commit is dated 2026-07-16

**Category:** Shopify theme development (Liquid)

**Quality Tier:** 🟡 Beta - single maintainer, 121 stars, three skills, no license file; the patterns are specific and current, but the repo ships no scripts, no tests and no security review

This is a deliberately small suite: three skills for Shopify Liquid theme development, split by scope rather than by product. `shopify-liquid-themes` covers the language and the theme file architecture, `liquid-theme-standards` covers CSS, JavaScript and HTML conventions inside theme files, and `liquid-theme-a11y` covers WCAG 2.2 patterns for commerce components. The README states that all three work with any Shopify Liquid theme, and the marketplace manifest wraps them into a single plugin named `shopify-theme-skills` whose owner block lists a shopify.com address, which reads as first-hand theme knowledge rather than a generic skill dump.

Together the three index at 9,404 combined installs across 3 indexed listings, and the SKILL.md files total 1,177 lines with the long-form detail pushed into fourteen reference files that the agent opens only when a task needs them. That shape matters here: Liquid is a language where a plausible-looking edit fails at render time, so the value is in the written constraints, not in tooling.

## Installation

The README documents one command, installing the plugin as a whole:

```bash
claude skill install --plugin shopify-theme-skills benjaminsehl/liquid-skills
```

The repository also carries a Claude Code marketplace manifest, so the standard two-step plugin path has what it needs: the marketplace name is `shopify-liquid-theme-skills`, the plugin is `shopify-theme-skills`, `strict` is false, and the plugin lists the three skill directories in `skills/`. Confirm your CLI's syntax against the manifest before relying on it:

```bash
claude plugin marketplace add benjaminsehl/liquid-skills
claude plugin install shopify-theme-skills@shopify-liquid-theme-skills
```

For any other agent, including Hermes, the skills.sh CLI is the generic path:

```bash
npx skills add benjaminsehl/liquid-skills
```

If you would rather vendor them, the pack's own install block clones the repo and copies the directory you need into your agent's skills folder. Each skill is self contained, so a copy has to bring `references/` with it:

```bash
git clone --depth 1 https://github.com/benjaminsehl/liquid-skills.git
mkdir -p ~/.hermes/skills
cp -R liquid-skills/skills/shopify-liquid-themes ~/.hermes/skills/
cp -R liquid-skills/skills/liquid-theme-standards ~/.hermes/skills/
cp -R liquid-skills/skills/liquid-theme-a11y ~/.hermes/skills/
```

There is no MCP server, no CLI, no hook and no configuration step. After install the agent reads the skill text and edits theme files with the file tools it already has.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| shopify-liquid-themes | 3,672 | Writing sections, blocks and snippets with correct schema JSON: the 33 setting types, `visible_if` conditions, LiquidDoc headers, `t` translation keys, and the 152 filter, 30 tag and 137 object lookup tables in `references/`. |
| liquid-theme-standards | 2,901 | CSS, JS and HTML rules for theme files: BEM inside `{% stylesheet %}` (which does not process Liquid), design tokens as custom properties, Web Components with no external dependencies, defensive CSS, and logical properties for RTL. |
| liquid-theme-a11y | 2,831 | WCAG 2.2 patterns for commerce components: product cards, carousels, cart drawers, filters, price display, modals and tabs, plus a decision table that picks a native element before reaching for ARIA. |

All 3 indexed listings clear the 2,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Liquid is small but hostile to improvisation. There are no parentheses in conditions and no ternary operator, `for` loops cap at 50 iterations, `contains` only works on strings, snippets cannot see outer-scope variables, and `{% stylesheet %}` does not interpolate Liquid even though it sits inside a `.liquid` file. An agent writing from memory produces something that looks right and renders wrong, and `shopify-liquid-themes` exists to remove exactly those guesses: it carries the eight critical gotchas as a checklist and a full example per construct.

The standards skill is what keeps agent output from forking a theme. It fixes BEM at a single element level, caps specificity at `0 4 0` with `0 1 0` as the target, bans IDs as selectors and `!important`, requires design tokens over hardcoded values, keeps JavaScript dependency free, and pushes logical properties so RTL locales do not need a second stylesheet. Applied consistently, an agent's edits read like the rest of the theme instead of like a patch.

Accessibility is where commerce themes actually lose customers, and it is the part agents most often fake. `liquid-theme-a11y` starts from a decision table that maps each component to a native element and an ARIA pattern: `<details>` for expandable content, `<dialog>` for modals and cart drawers, `[popover]` for tooltips, real `<form>` and `<fieldset>` for filters. Native first means most of the audit findings never get written.

The context economics are also good. Three SKILL.md files at 1,177 lines total, with the bulk of the detail in references such as `objects-tier2.md` (69 objects of property lists) that are read only when a task reaches that depth. For a Hermes agent running unattended on a theme task, that means a short, stable instruction surface and no runtime dependencies to break.

Finally, the three skills compose the way theme work actually arrives: a request like "add a featured collection section that is keyboard accessible" crosses the schema skill, the standards skill and the a11y skill in one turn, and because all three describe the same `sections/`, `blocks/`, `snippets/` layout they do not contradict each other.

## Usage

| You say | What happens |
|---|---|
| "Add a featured collection section with a heading, product limit and background color setting" | shopify-liquid-themes writes the section with a correct `{% schema %}`, picks setting types from the 33-type table, applies `visible_if` where settings depend on each other, and respects the 50-iteration loop cap. |
| "Why does my `{% stylesheet %}` block ignore `section.settings.bg_color`" | liquid-theme-standards explains that stylesheet tags do not process Liquid, then rewrites the dynamic value as an inline custom property on the element or moves it into a `{% style %}` block. |
| "Make the cart drawer keyboard accessible" | liquid-theme-a11y switches the drawer to `<dialog>`, adds focus trapping, restores focus to the trigger on close, and announces the cart count change in a live region. |
| "Clean up these product cards, the classes are a mess" | liquid-theme-standards rewrites to single-level BEM, replaces hardcoded colors and spacing with tokens, removes `!important`, and brings specificity back to `0 1 0`. |
| "Screen readers read our sale price wrong" | liquid-theme-a11y applies the price display pattern so compare-at and current price are labelled with context instead of being read as two bare numbers. |
| "Move all the hardcoded English strings into translations" | shopify-liquid-themes replaces literals with the `t` filter, adds interpolation where names are involved, and writes the keys into `locales/en.default.json` using the documented key naming. |
| "The carousel autoplays even with reduced motion on" | liquid-theme-a11y applies the animation and motion rules, and liquid-theme-standards wires the `prefers-reduced-motion` branch in the component's CSS. |

## Verification

Confirm all three skill files are reachable on main before installing. Every URL below returned 200 on 2026-10-27:

```bash
for p in skills/shopify-liquid-themes/SKILL.md \
         skills/liquid-theme-standards/SKILL.md \
         skills/liquid-theme-a11y/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/$p"
done
```

Read the manifest and the README directly if you are installing through Claude Code, since the plugin name and marketplace name have to match:

- https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/.claude-plugin/marketplace.json
- https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/README.md

The three SKILL.md files are worth skimming before you hand an agent write access to a theme, because each one tells the agent to create or edit files:

- https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/skills/shopify-liquid-themes/SKILL.md
- https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/skills/liquid-theme-standards/SKILL.md
- https://raw.githubusercontent.com/benjaminsehl/liquid-skills/main/skills/liquid-theme-a11y/SKILL.md

After install, the skills directory should hold one folder per skill, each with its reference files intact:

```bash
ls ~/.hermes/skills | grep -E "shopify-liquid-themes|liquid-theme-standards|liquid-theme-a11y"
ls ~/.hermes/skills/liquid-theme-a11y/references
```

The second listing should show `component-patterns.md` and `focus-and-keyboard.md`. If the folder exists but `references/` is empty, the copy skipped a level and the skill will fall back to guessing.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shopify-liquid-themes | Not checked | Not checked | Not checked |
| liquid-theme-standards | Not checked | Not checked | Not checked |
| liquid-theme-a11y | Not checked | Not checked | Not checked |

The real risk here is file writes, not code execution. All three skills instruct the agent to create or edit theme source: `sections/`, `blocks/`, `snippets/`, `layout/`, `templates/`, `config/settings_schema.json`, `locales/*.json` and `assets/`. Their frontmatter carries only `name` and `description`, with no allowed-tools or permission field, so the skills do not narrow what the host agent may touch. The blast radius is exactly the file access you granted it, which argues for running them in a repository checkout on a branch rather than against a published theme.

There is no credential surface. A grep across the clone finds no Shopify CLI invocation, no `theme push`, no Admin API token, no OAuth flow and no telemetry. The only network calls in the bundled examples are storefront endpoints such as `fetch('/cart/add.js')` inside Web Component samples. That is code destined for a shopper's browser, so review it as front-end code that will run against a live cart, not as a local script.

Note what the skills assume about a live store: a theme checked out on disk, and no deploy step at all. Nothing in the three files defines how an edit reaches production, so your own tooling makes that decision. The components they touch sit on the commerce path, specifically cart drawer, price display, product filters and forms, which is why a development theme and a preview of the cart flow should come before publishing anything generated here.

One licensing point belongs in this section too: the repository has no LICENSE file, so there is no grant to redistribute or vendor the text into a theme you ship.

## Limitations

- Snapshot data, verified 2026-10-27: 9,404 combined installs across 3 indexed listings; 121 GitHub stars; no LICENSE file at the repository root; branch main. Counts drift over time.
- Breadth is narrow: exactly 3 skills, all aimed at Shopify theme developers working in `.liquid` and theme assets. There is nothing here on app development, Hydrogen, the Admin API, Shopify Functions or theme deployment, so the suite is a supplement to a Shopify development skill set, not a replacement.
- No LICENSE file: the repo root holds only `README.md`, `.gitignore`, `.claude-plugin/` and `skills/`. Absent a license, default copyright applies, so do not vendor these files into a distributed theme or republish them without the author's permission.
- The README drifts from the tree. It reports 318, 420 and 448 lines for the three SKILL.md files; the clone has 314, 429 and 434. Its one-line `claude skill install --plugin ...` command also does not match the standard marketplace and install commands, so check the manifest for the real plugin name.
- Verdicts from the three auditors were not sampled this fire, so the Security table is all Not checked and should be re-read on skills.sh before production use.
- Guidance, not tooling: no scripts, no tests and no automated accessibility scan ship with the repo. The WCAG patterns are applied by hand, which means an axe or Lighthouse pass is still needed to catch what a pattern checklist cannot.
- One maintainer, last commit 2026-07-16. Treat the content as a snapshot of current Liquid practice rather than a maintained product.

## Related

- [Shopify Development - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/shopify-development-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)

## Pro Tips

- Install all three. They are split by scope, not by product, and a single section request usually needs the schema skill and the standards skill in the same turn.
- Send the agent to `references/` on purpose. `objects-tier2.md` is 69 objects of property lists and will dominate context for a task that only needs `product.title`.
- Name the theme paths explicitly. The skills assume `sections/`, `blocks/`, `snippets/` and `layout/` at the repo root, and they will create files there if the layout is different.
- Ask for the a11y skill before review, not after. Its decision table picks `<details>`, `<dialog>` and `[popover]` over custom ARIA, which removes most findings before an audit sees them.
- Run theme work on a branch against a development theme, then preview the cart drawer and price display. Those are the components most likely to break in a way that only shows up with a filled cart.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
