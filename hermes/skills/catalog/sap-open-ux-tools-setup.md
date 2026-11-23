---
title: "Open UX Tools - SAP Fiori Agent Skills Setup"
description: "sap/open-ux-tools: SAP Fiori development skills covering app development, charts, filters and testing - 5.6K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sap-open-ux-tools-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "sap fiori", "ui5", "cap"]
---

# Open UX Tools - SAP Fiori Agent Skills Setup

**Source:** [sap/open-ux-tools](https://www.skills.sh/sap/open-ux-tools) via skills.sh - 5.6K combined installs across 15 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [sap/open-ux-tools](https://github.com/sap/open-ux-tools) - 161 stars, Apache-2.0 license, main branch, last pushed Nov 23, 2026; skills live in two places: four under .agents/skills/<name>/SKILL.md and nine under plugins-coding-agents/fiori/skills/<name>/SKILL.md, with a Claude Code marketplace file at plugins-coding-agents/fiori/.claude-plugin/marketplace.json.
**Category:** SAP Fiori and UI5 Development
**Quality Tier:** 🟠 Orange - 1 Fail cell and 1 Warn cell across the 15-skill sample: Snyk Fails on odata-vocabularies-sync and Snyk Warns on sap-fiori-text-and-id.

Open UX Tools is SAP's monorepo of open source modules for building SAP Fiori applications, maintained by the same team behind SAP Fiori tools and driven by the SAP community. The repository publishes its modules to npm under the @sap-ux scope and, for coding agents, ships a set of skills alongside an MCP server for SAP Fiori development.

The agent skills split across two directories: nine Fiori skills under plugins-coding-agents/fiori/skills/ (app development, charts, visual filters, the @sap-ux/create CLI, the ESLint plugin, OPA5 testing, tree tables, building blocks and text-and-id) plus four tooling skills under .agents/skills/ (adp-controller-extension, eslint-rule-development, odata-vocabularies-sync and create-skill-sap-fiori-tools). The skills are distributed through a Claude Code plugin marketplace file and a GitHub Awesome Copilot plugin.json, not through the product README.

## Installation

Install the Fiori skills plugin in Claude Code from its marketplace file:

```bash
claude plugin marketplace add https://raw.githubusercontent.com/SAP/open-ux-tools/main/plugins-coding-agents/fiori/.claude-plugin/marketplace.json
claude plugin install sap-ux-fiori-tools
```

In GitHub Copilot, install the same plugin through the Copilot CLI:

```bash
copilot plugin install sap-ux-fiori-tools@awesome-copilot
```

The four tooling skills under .agents/skills/ are not part of the Fiori plugin and have no installer in the product README, which documents the monorepo's pnpm development flow (pnpm install, pnpm build, pnpm test) instead. The plugin README notes that once the plugin is listed in the Claude Code public marketplace, install simplifies to claude plugin install sap-ux-fiori-tools.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sap-fiori-add-visual-filter | 711 | adding chart-based visual filters to a Fiori Elements filter bar or value help (CAP or ABAP RAP) |
| sap-fiori-app-development | 710 | building Fiori Elements apps, List Reports, Object Pages and Worklists on CAP or OData |
| sap-fiori-analytical-chart | 699 | adding an analytical chart (chart plus table hybrid) to a List Report with aggregated data |
| sap-fiori-create-cli | 695 | invoking the @sap-ux/create CLI to generate, add, convert or update SAP Fiori projects |
| sap-fiori-eslint-plugin | 691 | configuring, migrating and running ESLint with @sap-ux/eslint-plugin-fiori-tools |
| sap-fiori-opa5-test-development | 660 | writing, fixing and reviewing OPA5 integration tests for Fiori Elements (V2 and V4) |
| odata-vocabularies-sync | 475 | syncing the odata-vocabularies package to the latest published vocabulary resources |
| eslint-rule-development | 357 | developing a new ESLint rule for @sap-ux/eslint-plugin-fiori-tools end to end |
| sap-fiori-tree-table | 345 | configuring a hierarchical tree table for parent-child recursive hierarchies |
| create-skill-sap-fiori-tools | 126 | authoring, reviewing or refactoring a skill for the SAP Fiori Tools ecosystem |
| adp-controller-extension | 87 | extending Fiori adaptation project controllers with custom logic and UI changes |

The remaining 4 indexed listings range from 2 to 18 installs.

## Why This Matters for Hermes Agents

A coding agent asked to modify a SAP Fiori Elements app will reach for generic React or UI5 advice and miss the Fiori-specific patterns: the @sap-ux/create CLI commands, the fiori-tools ESLint rules, the OPA5 test libraries for OData V2 and V4, and the building-block workflow that goes through the Fiori MCP server. These skills encode that knowledge, and they are written by the same SAP team that builds the tooling, so the guidance matches the actual tool versions. The highest-value skills are sap-fiori-app-development for correct app structure, sap-fiori-create-cli for the generator commands, and sap-fiori-opa5-test-development for tests that actually exercise a Fiori app. The four tooling skills under .agents/skills/ cover the ecosystem maintenance side - authoring skills, writing ESLint rules and syncing OData vocabularies - which matters if you maintain tooling rather than just apps. For operators, the plugin distribution path means the skills update with the plugin rather than drifting from a manual copy.

## Usage

| You say | What happens |
|---|---|
| Add a chart-based filter to this List Report | Runs sap-fiori-add-visual-filter to add a visual filter to the filter bar |
| Scaffold a new Fiori project | Runs sap-fiori-create-cli to invoke the @sap-ux/create generator commands |
| Run ESLint on my Fiori app | Runs sap-fiori-eslint-plugin to configure, migrate or run the fiori-tools rules |
| Write OPA5 tests for this Fiori Elements app | Runs sap-fiori-opa5-test-development for V2 or V4 test libraries |
| Add a tree table to show a hierarchy | Runs sap-fiori-tree-table to configure a recursive parent-child table |
| Hide the technical key, show the business ID | Runs sap-fiori-text-and-id to swap GUIDs for business text |
| Extend the controller in my adaptation project | Runs adp-controller-extension to add custom logic and UI changes |

## Verification

Confirm the Fiori plugin marketplace file resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/SAP/open-ux-tools/main/plugins-coding-agents/fiori/.claude-plugin/marketplace.json
```

Spot-check a Fiori skill and a tooling skill to confirm the two-directory layout:

```bash
curl -sL https://raw.githubusercontent.com/SAP/open-ux-tools/main/plugins-coding-agents/fiori/skills/sap-fiori-app-development/SKILL.md | head -30
```

```bash
curl -sL https://raw.githubusercontent.com/SAP/open-ux-tools/main/.agents/skills/adp-controller-extension/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sap-fiori-add-visual-filter | Pass | Pass | Pass |
| sap-fiori-app-development | Pass | Pass | Pass |
| sap-fiori-analytical-chart | Pass | Pass | Pass |
| sap-fiori-create-cli | Pass | Pass | Pass |
| sap-fiori-eslint-plugin | Pass | Pass | Pass |
| sap-fiori-opa5-test-development | Pass | Pass | Pass |
| odata-vocabularies-sync | Pass | Pass | Fail |
| eslint-rule-development | Pass | Pass | Pass |
| sap-fiori-tree-table | Pass | Pass | Pass |
| create-skill-sap-fiori-tools | Pass | Pass | Pass |
| adp-controller-extension | Pass | Pass | Pass |
| sap-fiori-text-and-id | Pass | Pass | Warn |
| sap-fiori-building-blocks | Pass | Pass | Pass |
| add-visual-filter | Pass | Pass | Pass |
| sap-fiori | Pass | Pass | Pass |

The 15-skill sample is nearly clean - the only non-Pass cells are a Snyk Fail on odata-vocabularies-sync and a Snyk Warn on sap-fiori-text-and-id - and all 15 indexed listings carry a published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,591 combined installs across 15 indexed listings; 161 GitHub stars; Apache-2.0 license; last pushed Nov 23, 2026. Counts drift over time.
- The index and tree do not fully line up: add-visual-filter (3 installs) and sap-fiori (2 installs) have no matching skill directory in the current tree, and the Fiori plugin README lists seven skills while its plugin.json bundles eight.
- The product README documents the monorepo's pnpm development flow, not a skills installer, so install commands come from the plugin README at plugins-coding-agents/fiori/README.md.
- The four tooling skills under .agents/skills/ are not included in the Fiori plugin marketplace file and have no documented installer in the fetched sources.
- The repository requires Node 18+ (the AGENTS.md sets 20+ for the monorepo), and the skills pair with the @sap-ux/fiori-mcp-server.
- This is one of several SAP skill sources; sap/ai-skills-library and secondsky/sap-skills are separate repositories and not the same set of skills.

## Related

- [SAP AI Skills Library - Enterprise Agent Skills Setup](/hermes/skills/catalog/sap-ai-skills-library-setup)
- [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup)
- [Frontend Design Skills - UI Composition and UX Review](/hermes/skills/catalog/hueyexe-frontend-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install through the plugin marketplace so the skills stay in sync with the tooling versions, rather than copying files by hand.
- Start with sap-fiori-app-development to get app structure right, then pull sap-fiori-create-cli for the generator commands.
- Read the odata-vocabularies-sync body before relying on it; its Snyk Fail cell is a reason to review the skill first.
- For Fiori Elements apps, use the V4 test library (sap.fe.test) for OData V4 and fioriElementsTestLibrary for V2 when writing OPA5 tests.
- If you contribute skills to the ecosystem, follow the create-skill-sap-fiori-tools conventions, including the sap-fiori-<feature> naming rule.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
