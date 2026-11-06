---
title: "AI Design Skills - Landing Pages and Figma"
description: "elayadesign/ai-design-skills on skills.sh: 5.3K combined installs; landing page design and Figma design skills on one fixed visual system."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elayadesign-ai-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "design", "figma", "landing pages"]
---

# AI Design Skills - Setup Guide

**Source:** [elayadesign/ai-design-skills](https://www.skills.sh/elayadesign/ai-design-skills) via skills.sh - 5.3K combined installs across 3 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 14,497 stars, MIT licence, last pushed 2026-11-02, two SKILL.md directories under skills/
**Category:** Design execution for agents: landing pages from intake to visual system, and structured Figma files with variables
**Quality Tier:** 🟢 Verified - all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE.

This is a small, deliberately narrow design collection: two skills, each a self-contained folder, both built on one fixed visual system. `landing-page-design` covers building a page from nothing, from intake questions through page structure and conversion copy to a strict typographic and spacing system. `figma-designer` covers working inside Figma through the Figma MCP, with real variables, named text styles, auto layout and components rather than hand-placed shapes.

The values are the point, and both skills share them. Font sizes resolve to the Tailwind type scale rather than arbitrary pixels, spacing and corner radius come from tokens, and the Figma side adds a two-layer colour system (Core Colors, then Color System with light and dark modes), named text styles and button and state rules. A skill that names the number is the difference between an agent that produces a coherent page and one that produces a plausible page with 13px body text and four different corner radii.

## Installation

The README installs with the skills CLI and needs Node.js:

```bash
npx skills add elayadesign/ai-design-skills
```

It lists the skills in the repository and asks which ones to install and for which agents. The README's flags skip the prompts:

```bash
# one skill
npx skills add elayadesign/ai-design-skills --skill landing-page-design

# pick agents
npx skills add elayadesign/ai-design-skills -a claude-code -a cursor

# user-level instead of project-level
npx skills add elayadesign/ai-design-skills -g

# see what's available without installing
npx skills add elayadesign/ai-design-skills --list
```

Add `-y` to skip confirmations. Skills land in `.claude/skills/` for Claude Code and `.agents/skills/` for Cursor, Codex and other agents, and `npx skills update` pulls later changes.

The README also documents a manual route. For Claude Code it clones the repository and copies the skill folder:

```bash
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

For Cursor it writes the rules file directly:

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## What It Provides

Two listings clear the 500-install threshold, and they cover the two ends of the same job: deciding and building the page, then producing the design file.

| Skill | Installs | Use For |
|---|---|---|
| landing-page-design | 4,078 | Landing page build from intake to structure, conversion copy, SEO, and a strict type, spacing, radius, colour and motion system |
| figma-designer | 1,003 | Figma work with real variables, named text styles, auto layout, components with every state, and a Foundations frame bound to the tokens |

The remaining 1 indexed listing is design-to-motion (208 installs), which has no directory in the current `skills/` tree; the README documents only `landing-page-design` and `figma-designer`.

## Why This Matters for Hermes Agents

Design is the category where a capable agent's output is most obviously machine-made. The failure is rarely a broken layout; it is a page with five font sizes, inconsistent spacing, a gradient hero and copy that says nothing. Rules with explicit values remove most of that variance, because the agent is choosing from a scale rather than inventing a value.

The landing page skill is split into two halves that must run in order. Part A decides what the page says and how it is structured: the one primary action, the audience, objections, proof, then section and layout selection. Part B is the non-negotiable visual system. The skill says to work through A before touching B, which is the discipline an agent skips when asked for "a nice landing page" in one shot.

The intake is written for an agent rather than a human designer. It tells the agent to gather what is missing in one batch, and to make a reasonable assumption and state it in one line rather than stall the build when the user cannot answer. That is the correct trade for a conversational agent.

The Figma skill solves a different problem: file integrity. It requires listing existing variable collections, text styles and library components before creating anything, binds fills, strokes, radius, padding and gap to variables rather than typed numbers, and builds a Foundations frame whose samples update when a token changes. An agent that does this leaves a file a designer can maintain; an agent that does not leaves a mockup.

The scope rules are honest about conflict. The skill states that where a rule conflicts with a framework default, the skill wins, and where the user's explicit prompt conflicts with a rule, the user wins. That precedence is worth knowing before you install it, because it decides who is in charge when your instructions disagree with the file.

## Usage

| You say | What happens |
|---|---|
| "Build a landing page for this product" | The skill runs intake in one batch, fixes the single primary action, then selects structure before any styling |
| "Rewrite this hero copy for conversions" | Part A's copy rules apply: offer, audience, objection handling and one primary action |
| "Set up a design system in Figma" | figma-designer creates spacing and radius variables, the two colour layers and the text styles first |
| "Make a button component with all states" | The skill builds states from the token reference and binds fills to Color System tokens |
| "This page looks generic, what is wrong?" | The visual rules are checked as written requirements: type scale, spacing, radius, hero layout, icons, motion |
| "Design this page in Figma from this link" | figma-designer loads the Figma plugin rules, checks the file, then builds section by section |
| "Update the tokens across the file" | Editing a variable updates every bound sample in the Foundations frame, which is the check that binding worked |

## Verification

Review both skills before install. These paths returned HTTP 200 on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/landing-page-design/SKILL.md | head -4
curl -fsSL https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/figma-designer/SKILL.md | head -4
```

The first should open with `name: landing-page-design` and a description that names intake questions, page structure, conversion copywriting and the strict visual rules. The second should open with `name: figma-designer` and a description naming variables, text styles, auto layout, components and the Tailwind type and radius scale.

Then confirm the install landed where your harness reads it:

```bash
ls .claude/skills/landing-page-design .claude/skills/figma-designer
```

Each directory should hold a SKILL.md. If you installed user-level with `-g`, look under your home directory instead of the project. If nothing is there, run the README install again:

```bash
npx skills add elayadesign/ai-design-skills
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| landing-page-design | Pass | Pass | Pass |
| figma-designer | Pass | Pass | Pass |
| design-to-motion | Pass | Pass | Pass |

Both shipped skills are markdown rule sets. They do not ship executables or install dependencies, so the install surface is a text file an agent reads as instructions. That is also the risk that matters: instructions that tell an agent to follow a guide will be followed.

figma-designer is the one with reach into another system. It directs an agent through the Figma MCP to create and edit variables, text styles and components in a real file, and it expects the official `figma-use`, `figma-generate-design` and `figma-generate-library` skills to be present for the Plugin API rules. Point it at a scratch file for the first run, and check that the file you hand it is one you can restore from version history.

The Cursor manual route writes a rules file into `.cursor/rules` with `curl` from a raw URL. Pin it to a commit rather than a branch if you want reproducibility.

## Limitations

- Snapshot data, verified 2026-11-06: 5,289 combined installs across 3 indexed listings; 14,497 GitHub stars; MIT; last pushed 2026-11-02. Counts drift over time.
- The install index outruns the tree. `design-to-motion` (208 installs) has no directory under `skills/`, and the README documents only two skills, so there is nothing to read before install for that listing.
- figma-designer is not standalone. It explicitly layers on top of the official Figma skills and requires the Figma MCP to be connected; without both, the design rules have nothing to act on.
- The redesign path is not in this repository. Upgrading an existing site is a separate skill (`redesign-existing-projects`) in the elayadesign/redesign-skill repository, which the README links.
- These are rules, not a component library. There is no theme file, no starter template and no build step; the page is still built by your agent, and the quality depends on how closely it follows the values.
- The landing page rules were partly adapted from taste-skill by Leon Lin under MIT, which the SKILL.md states and whose licence text it embeds. Keep that notice with any copy you redistribute.
- The collection is described in its README as growing, with more skills to come. Treat the current two as the stable surface.

## Related

- [Figma MCP Server Guide - Design-to-Code Workflows](/hermes/skills/catalog/figma-mcp-server-guide-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)
- [claude-design - Setup Guide](/hermes/skills/catalog/claude-design-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the intake before asking for output. One batch of questions about offer, audience, objections, proof and traffic source produces a page that says something; skipping it produces a page that looks like every other one.
- Give the agent the token reference explicitly when working in Figma. The values live at the end of the SKILL.md, and an agent that skims the workflow without reading the tokens invents sizes.
- Ask for sections one at a time. The skill builds the hero first, then one section per step, and screenshots between steps; asking for the whole page at once is what produces a page with no hierarchy.
- Keep one typeface in the Figma file. The rules allow a second face only for code, data or numbers, and no weights above bold, which is the fastest constraint to break and the easiest to check.
- Use `--list` before installing if you are unsure which half you need. The two skills are independent, and a Figma-only task does not need the landing page rules loaded.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
