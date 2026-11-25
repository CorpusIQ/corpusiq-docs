---
title: "Figma Console MCP Skills - Design Systems and A11y Setup"
description: "southleft/figma-console-mcp-skills - 3.4K combined installs: Figma design-systems skills for tokens, variables, WCAG lint and a11y audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/figma-console-mcp-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "figma", "design system", "accessibility"]
---

# Figma Console MCP Skills - Setup Guide

**Source:** [southleft/figma-console-mcp-skills](https://www.skills.sh/southleft/figma-console-mcp-skills) via skills.sh - 3.4K combined installs across 23 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [southleft/figma-console-mcp-skills](https://github.com/southleft/figma-console-mcp-skills) - 101 stars, MIT license, last pushed Aug 16, 2026; 23 skill directories live under skills/<name>/, each with a SKILL.md plus scripts/ and references/ files, though the README documents only 22 of them.
**Category:** Design Systems and Accessibility
**Quality Tier:** 🟡 Yellow - all 15 sampled skills pass Gen Agent Trust Hub and Socket; figma-comments, figma-scan-code-accessibility, figma-generate-component-doc and figma-annotations carry Warn cells on Snyk.

southleft/figma-console-mcp-skills repackages the most powerful capabilities of the Figma Console MCP as Markdown skills that run on the native Figma MCP server. Each skill is a self-contained folder with a SKILL.md playbook plus ready-to-paste scripts, so an agent handles design-systems work (token export and import, variable management, component-set analysis, WCAG linting, accessibility audits, version diffing, annotations, FigJam and Slides) without reinventing the Figma Plugin API each session.

Most skills run through use_figma; four REST skills (figma-version-history, figma-generate-changelog, figma-blame-node, figma-comments) reach data the Plugin API cannot and need a Figma personal access token, while one code-side skill (figma-scan-code-accessibility) runs axe-core over generated HTML with no Figma connection at all. The skills.sh index lists 23 listings at 3.4K combined installs; the README documents 22, with figma-extract-design-system present in the tree and index but absent from that list.

## Installation

The fastest path is npx:

```bash
npx skills add southleft/figma-console-mcp-skills
npx skills add southleft/figma-console-mcp-skills --list
npx skills add southleft/figma-console-mcp-skills --skill figma-export-tokens
```

Claude Code plugin:

```text
/plugin marketplace add southleft/figma-console-mcp-skills
/plugin install figma-console-mcp-skills@figma-console-mcp-skills
```

Terminal clone for Claude Code, Cursor and other agents:

```bash
git clone https://github.com/southleft/figma-console-mcp-skills.git
cd figma-console-mcp-skills
cp -R skills/* ~/.claude/skills/
```

Two prerequisites: connect Figma (a one-time OAuth login) and have the official figma-use skill available (it ships with the Figma integration). The four REST skills also need export FIGMA_TOKEN="figd_..." set in the shell.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| figma-lint-design | 175 | linting a node tree for WCAG 2.2 and design-system quality: contrast, target size, focus, hardcoded colors |
| figma-export-tokens | 175 | exporting Figma variables to DTCG, CSS, Tailwind, SCSS, TypeScript, JSON and other token formats |
| figma-design-system-inventory | 162 | one-call inventory of an entire design system: tokens, components, styles and visual specs |
| figma-audit-accessibility | 160 | per-component accessibility scorecard: state coverage, focus, target size, color-blind simulation |
| figma-check-design-parity | 156 | comparing a Figma node against a code spec for a 0-100 parity score and fix suggestions |
| figma-manage-variables | 152 | creating, updating, renaming, deleting and organizing Figma variables, collections and modes |
| figma-import-tokens | 152 | pushing design tokens from code into Figma as variables |
| figma-analyze-component-set | 149 | extracting a variant set as a state machine mapped to CSS pseudo-classes for code generation |
| figma-setup-design-tokens | 148 | bootstrapping a complete design-token system (collection, modes, variables) in one step |
| figma-comments | 148 | reading, posting, replying to and deleting Figma file comments via the REST API |
| figma-scan-code-accessibility | 147 | scanning generated HTML with axe-core for structural and semantic accessibility violations |
| figma-generate-component-doc | 147 | generating Markdown documentation for a component: anatomy, tokens, states, accessibility |
| figma-component-properties | 147 | adding, editing and deleting component properties and setting instance properties |
| figma-annotations | 147 | reading and writing designer annotations pinned to nodes |

The remaining 9 indexed listings range from 68 to 145 installs.

## Why This Matters for Hermes Agents

The native Figma MCP is general-purpose; the hard part is doing each design-systems job well and repeatably. These skills package that know-how as self-contained playbooks plus ready-to-paste scripts, so a Hermes agent working a Figma-to-code pipeline gets the correct Plugin API idiom on first use instead of discovering it per session. The token and variable skills are the anchor: they cover the full code-to-Figma and Figma-to-code round trip across DTCG, CSS, Tailwind, SCSS and TypeScript, which is the plumbing most design-tool integrations skip. The quality layer (lint, audit, parity, code scan) closes the loop from design to shipped code with WCAG 2.2 checks on both sides. Four skills need a personal access token because they reach version history and comments, which the Plugin API cannot; that split is clearly documented and easy to gate. Nothing here requires the Figma Console MCP server itself, so the collection is a lighter-weight alternative to standing up another MCP.

## Usage

| You say | What happens |
|---|---|
| Export my Figma variables to CSS | Uses figma-export-tokens to emit CSS custom properties (or Tailwind, SCSS, JSON) |
| Lint this frame for accessibility | Uses figma-lint-design for a WCAG 2.2 and design-system quality pass |
| Audit this component for a11y | Uses figma-audit-accessibility for a per-component accessibility scorecard |
| Does my code match the Figma? | Uses figma-check-design-parity to score the build against the design |
| Set up design tokens from scratch | Uses figma-setup-design-tokens to bootstrap a collection with light and dark modes |
| Document this component | Uses figma-generate-component-doc for Markdown anatomy, states and tokens |
| Scan this HTML for a11y issues | Uses figma-scan-code-accessibility to run axe-core over the markup |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/southleft/figma-console-mcp-skills/main/README.md | head -60
```

Confirm a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/southleft/figma-console-mcp-skills/main/skills/figma-lint-design/SKILL.md | head -30
```

Skills install to .agents/skills/ (npx) or ~/.claude/skills/ (manual copy); confirm the folders exist after install.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| figma-lint-design | Pass | Pass | Pass |
| figma-export-tokens | Pass | Pass | Pass |
| figma-design-system-inventory | Pass | Pass | Pass |
| figma-audit-accessibility | Pass | Pass | Pass |
| figma-check-design-parity | Pass | Pass | Pass |
| figma-manage-variables | Pass | Pass | Pass |
| figma-import-tokens | Pass | Pass | Pass |
| figma-analyze-component-set | Pass | Pass | Pass |
| figma-setup-design-tokens | Pass | Pass | Pass |
| figma-comments | Pass | Pass | Warn |
| figma-scan-code-accessibility | Pass | Pass | Warn |
| figma-generate-component-doc | Pass | Pass | Warn |
| figma-component-properties | Pass | Pass | Pass |
| figma-annotations | Pass | Pass | Warn |
| figma-deep-component | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,368 combined installs across 23 indexed listings; 101 GitHub stars; MIT license; last pushed Aug 16, 2026. Counts drift over time.
- The index and the README drift: figma-extract-design-system (68 installs) has a SKILL.md in the tree and an index listing but is absent from the README's 22-skill documentation.
- Four skills require a Figma personal access token (FIGMA_TOKEN) and a terminal-capable agent; they do not run in plain Claude Desktop or claude.ai chat.
- Skills read and write live design data, so review each script before running it against a production Figma file.
- skills.sh sampled 15 of the 23 listings for security verdicts; the other 8 have no sampled verdicts.

## Related

- [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup)
- [UI/UX Agent Skill System - Vendor-Neutral Skill Suite Setup](/hermes/skills/catalog/ui-ux-agent-skill-system-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run npx skills add southleft/figma-console-mcp-skills --list first to preview the collection before installing.
- Pair any Plugin-API skill with the official figma-use skill, which is the source of truth for the Figma Plugin API surface.
- Gate the four REST skills behind export FIGMA_TOKEN only when you actually need version history, changelogs, blame or comments.
- figma-extract-design-system is present in the tree even though the README omits it; its SKILL.md sits at skills/figma-extract-design-system/SKILL.md.
- Each skill is self-contained, so a single-folder upload or zip works with no broken links.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
