---
title: "Dembrandt Skills - Design System Judgment for Agents"
description: "dembrandt/dembrandt-skills on skills.sh: 38.3K combined installs across 45 listings; UX and design-system rules your agent reads before touching a UI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dembrandt-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "design system", "ux review", "accessibility"]
---

# Dembrandt Skills - Setup Guide

**Source:** [dembrandt/dembrandt-skills](https://www.skills.sh/dembrandt/dembrandt-skills) via skills.sh - 38.3K combined installs across 45 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 184 stars, MIT (LICENSE in the repo root), last pushed 2026-11-01, 45 SKILL.md directories at skills/<name>/SKILL.md
**Category:** Design-system judgment for agents: component families, colour tokens, elevation, forms and information architecture
**Quality Tier:** 🟡 Review - a tightly maintained suite (45 skills, 45 directories, every listing indexed, last pushed 2026-11-01) where extract-design carries a Snyk Warn and two skills depend on an external Dembrandt engine.

The README states the premise directly: the agent writes the component in seconds and does not know the modal should have been a drawer, or that the grey it picked fails contrast. These 45 skills carry that judgment as rules, one file per decision area, from colour derivation and type scales through form validation, tab navigation, overlay hierarchy, app shells and WCAG 2.2 review.

The structure is unusually even. Every one of the 45 indexed listings has a matching `skills/<name>/SKILL.md` directory in the tree, the install counts sit in a narrow band (280 to 1,076), and the README groups the same files into seven reading families: brand and visual identity, design tokens and scales, layout and structure, components and interaction, UX principles, technical foundation, and a pipeline group.

Two skills have a dependency worth knowing before install. `extract-design` and `generate-ui-from-brand` read tokens off a live site and need the Dembrandt engine, which the README describes as a free open-source CLI and MCP server that turns a website into design tokens and enforces them in CI. The other 43 work on the install alone.

## Installation

The README's quick start is one command:

```bash
npx skills add dembrandt/dembrandt-skills --all
```

The README notes that skills load only when a prompt needs them, so `--all` costs nothing, and that `--global` installs for every project. Installs are copies, so later changes arrive through:

```bash
npx skills update
```

On Claude Code the plugin route is shorter, because it carries the skills and registers the dembrandt MCP server in one go. The `npx` line goes in a terminal; the `/plugin` lines are typed inside Claude Code:

```
/plugin marketplace add dembrandt/dembrandt-skills
/plugin install dembrandt@dembrandt
```

The plugin does not fetch the browser the extraction needs, so run this once before the first extraction:

```bash
npx dembrandt install-browser
```

If you are wiring the engine by hand instead, the README's MCP entry is:

```json
{
  "mcpServers": {
    "dembrandt": {
      "command": "npx",
      "args": ["-y", "dembrandt", "mcp"]
    }
  }
}
```

The engine needs Node.js 18 or newer, and Dembrandt drives its own Chromium, which is not bundled.

## What It Provides

Twenty listings clear the 944-install threshold, and they read as the spine of a design review: usability criteria, performance, theming, density, form craft, brand language, information architecture, motion and accessibility.

| Skill | Installs | Use For |
|---|---|---|
| nielsen-usability-heuristics | 1,076 | The ten usability heuristics as review criteria for audits, interaction flows and error messages |
| performance-and-web-vitals | 1,058 | Lighthouse audits and Core Web Vitals: LCP, CLS, INP, images, fonts and render-blocking resources |
| color-mode-and-theme | 1,007 | Light, dark or both, and when a theme selector earns its place in the product |
| ui-density | 997 | Matching information density to platform and user type, including desktop products adapted for mobile |
| form-design | 996 | Helper text, placeholders, validation and submit behaviour for forms and data entry |
| semantic-html-and-seo | 979 | Semantic HTML5, SEO basics, alt text, progressive enhancement and SPA concerns |
| brand-visual-language | 979 | Shape language across type, radius and icons for design systems and visual consistency review |
| information-architecture | 969 | Naming, navigation, a UI that mirrors the data model, confirms for irreversible changes |
| motion-and-storytelling | 968 | Animation principles and cinematic technique applied to transitions, scroll motion and onboarding |
| algorithmic-color-palette | 965 | Deriving a full palette from one or two brand colours: state variants, tinted greys, semantic colours |
| modular-scale-typography | 962 | Ratio-based type scales where every size relates to the others, including minimum sizes |
| user-flows-and-guided-paths | 960 | Multi-step paths and wizards: onboarding, checkout and setup sequences |
| wcag-accessibility | 956 | WCAG 2.2 AA as required by the European Accessibility Act: contrast, keyboard access, ARIA |
| responsive-paradigms | 955 | Mobile, tablet and desktop treated as separate paradigms rather than one layout scaled down |
| gestalt-ui-organisation | 954 | Grouping related controls by proximity, similarity and common region |
| visual-emphasis-and-hierarchy | 953 | Size, colour, weight and position for primary actions, CTA groups, cards and dashboards |
| button-states | 951 | Rest, hover, active, focus, disabled and loading states derived from the base colour |
| component-family-consistency | 950 | Shared radius, colour logic, shadow, border and spacing across buttons, inputs, badges and pills |
| loading-states-and-perceived-performance | 949 | Spinners, skeletons and staggered reveals that manage perceived wait |
| micro-interactions | 944 | Small purposeful animation: toggles, animated icons, success moments, loaders |

The remaining 25 indexed listings range from 280 to 943 installs. That tail holds the extraction pipeline and the specialist layout decisions: `generate-ui-from-brand` (943), `extract-design` (937), `status-colors-and-errors` (937), `data-display-and-selection` (935), `elevation-and-depth` (932), `sticky-and-fixed-elements` (930), `notifications-and-recovery` (928), `scroll-areas` (921), down through `app-shell` (407), `sizing-units` (340), `clone-website` (320), `surface-separation` (283) and `marketing-vs-product-system` (280).

## Why This Matters for Hermes Agents

Agents are good at producing a screen that renders and bad at producing one that belongs. The failure is rarely a broken component; it is a modal where the flow wanted a drawer, three button families that look like three products, or a grey that fails contrast at 15px. This suite is a set of rules aimed at exactly that gap, written as decisions rather than inspiration.

The coverage is decision-shaped. `button-states` is about six states derived from one base colour. `component-family-consistency` is about shared radius, colour logic, shadow and spacing across a family. `information-architecture` is about naming and confirms for irreversible changes. An agent can apply each of those to a diff without needing taste, which is the property that makes a skill reliable.

The suite also covers the parts of a review an agent tends to skip: `wcag-accessibility` anchors to WCAG 2.2 AA and the European Accessibility Act, `performance-and-web-vitals` works from Lighthouse and Core Web Vitals, and `semantic-html-and-seo` covers alt text and progressive enhancement. Those are checkable claims, so an agent citing the skill can be held to them.

There is a real orchestrator, not only a pile of rules. The `dembrandt` skill (897 installs, in the tail) is described in the README as a six-stage pipeline across brand, tokens, layout, components, polish and an accessibility gate, and the README says a broad request like "review this screen" routes there. Ask narrowly and one skill loads; ask broadly and the pipeline runs.

The caveat is that two skills need infrastructure. `extract-design` and `generate-ui-from-brand` read a live site through the Dembrandt engine, so on a machine without Node and the bundled Chromium they will not do what the description promises. Installing all 45 and assuming all 45 work is the mistake this suite invites.

For a Hermes agent working in a frontend repository, the practical value is a review vocabulary. Instead of "make it look better", the agent gets named checks with named failure modes, which is the difference between a review that changes a diff and one that produces adjectives.

## Usage

| You say | What happens |
|---|---|
| "I have one brand colour, build me a full UI palette" | algorithmic-color-palette derives states and brand-tinted greys from the one value |
| "My font sizes feel random, set up a type scale" | modular-scale-typography builds a ratio scale and sets minimum sizes |
| "Review this interface for usability issues" | nielsen-usability-heuristics runs the ten heuristics, or the dembrandt skill runs the full pipeline on a broad request |
| "Our buttons, inputs and badges look like three different products" | component-family-consistency reconciles radius, colour logic, shadow and spacing |
| "Design a multi-step onboarding flow for a B2B tool" | user-flows-and-guided-paths covers wizards, purchase flows and onboarding sequences |
| "Does this pass WCAG 2.2 AA?" | wcag-accessibility checks contrast, keyboard access and ARIA against the standard |
| "Extract the design system from stripe.com" | extract-design reads tokens through the Dembrandt engine, which must be installed first |

## Verification

Check a skill's own text before you install the set. Both probes below returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/dembrandt/dembrandt-skills/main/skills/nielsen-usability-heuristics/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/dembrandt/dembrandt-skills/main/skills/form-design/SKILL.md | head -20
```

The first opens with a description that scopes the skill to auditing an interface, designing interaction flows, writing error messages or reviewing usability. The second scopes to helper text, placeholders, validation and submit behaviour. Both are short frontmatter blocks, so you can read the trigger conditions in seconds and decide whether the skill will fire on your task.

After `npx skills add`, confirm what landed in your agent's skills directory and check the one-time browser fetch the two extraction skills depend on:

```bash
ls ~/.claude/skills | wc -l
npx dembrandt install-browser
```

The README says 43 of the 45 skills work on the install alone and that only `extract-design` and `generate-ui-from-brand` need the engine, so a directory count near 45 with a working `npx dembrandt` is the expected state. If you took the Claude Code plugin route, the dembrandt MCP server is registered by the plugin and the browser still has to be fetched with `npx dembrandt install-browser`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nielsen-usability-heuristics | Pass | Pass | Pass |
| user-flows-and-guided-paths | Pass | Pass | Pass |
| extract-design | Pass | Pass | Warn |
| operational-expert-tool-ui | Pass | Pass | Pass |
| marketing-vs-product-system | Pass | Pass | Pass |

`extract-design` is the one flag, and it is also one of the two skills that runs external infrastructure: it drives a headless browser at a URL you give it and reads the computed styles back. A Warn there is worth reading rather than dismissing, because the skill is not just markdown advice, it is a pipeline that reaches the network.

The engine is a separate trust decision. `npx dembrandt` pulls a package at run time, `npx dembrandt install-browser` fetches a Chromium build, and the MCP server registers a tool surface your agent can call. Pin versions and read what the MCP exposes before pointing it at a production site.

The skills themselves are instructional text with no scripts in the skill directories, which keeps the install surface small. The risk with a judgment suite is different from the risk with an execution suite: the instructions shape what an agent changes in your codebase, so a rule that is wrong for your product becomes a wrong edit.

The repository is MIT with a LICENSE file in the root, so redistribution of the skill text is settled. The engine at `dembrandt/dembrandt` is a different repository with its own licence, and the README calls it free and open source without naming terms.

## Limitations

- Snapshot data, verified 2026-11-06: 38,341 combined installs across 45 indexed listings; 184 GitHub stars; MIT; last pushed 2026-11-01. Counts drift over time.
- Two of the 45 skills are not self-contained. `extract-design` and `generate-ui-from-brand` require the Dembrandt CLI or MCP server, Node.js 18 or newer, and a Chromium the CLI downloads itself.
- Installs are copies, not links. The README says to run `npx skills update` to pick up later changes, so a set installed months ago can be several revisions behind without any signal.
- The install counts sit in a narrow band (280 to 1,076) across all 45 listings. Volume here is close to uniform, so the ranking is a weak signal about which skill is best developed.
- This is a judgment suite, not a linter. Nothing in the 45 skills enforces a token, fails a build or blocks a merge; the rules only apply when the agent reads the file and chooses to follow it.
- The extraction path observes a live site. Whether you may extract another company's design tokens is a legal and ethical question the README does not address, and `clone-website` reproduces a page 1:1 by measurement.

## Related

- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all 45, read two. The set is cheap to install because skills load on demand, but a review is only as good as the rule file the agent actually opens; start with `button-states` and `form-design`.
- Ask broadly when you want the pipeline. The README says a request like "review this screen" routes to the `dembrandt` orchestrator, which runs brand, tokens, layout, components, polish and an accessibility gate in sequence.
- Set up the engine before the first extraction, not during it. `npx dembrandt install-browser` is a separate step from both install routes and is the most common reason `extract-design` appears broken.
- Pair it with a measurement skill. These rules name what to check; `performance-and-web-vitals` and `wcag-accessibility` supply the numbers that decide whether the check passed.
- Use `marketing-vs-product-system` when a product grows a second surface. It is the file that separates intentional divergence between a marketing site and an app from drift.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
