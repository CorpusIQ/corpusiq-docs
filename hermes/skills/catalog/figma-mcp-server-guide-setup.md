---
title: Figma MCP Server Guide — Design-to-Code Workflows for Hermes Agents
description: Figma's official MCP server guide skills — implement designs, use Figma, generate designs/libraries, code connect. 23K+ combined installs across 6 skills for design-to-code automation.
---

# Figma MCP Server Guide — Setup Guide

**Source:** [figma/mcp-server-guide](https://skills.sh/figma/mcp-server-guide) (23K+ combined installs)
**GitHub:** [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) (1,809 ⭐)
**Category:** Design / Development
**Quality Tier:** 🟢 Production

Figma's official MCP server guide skills — the bridge between design and code. These skills teach Hermes agents how to read Figma designs, generate code implementations, create component libraries, and connect design systems to production code. Essential for any agent workflow that involves design-to-code translation or design system management.

---

## Installation

```bash
# Core design-to-code skills (highest installs)
npx skills add figma/mcp-server-guide --skill implement-design
npx skills add figma/mcp-server-guide --skill figma-use
npx skills add figma/mcp-server-guide --skill figma-generate-design

# Component library & code connect
npx skills add figma/mcp-server-guide --skill figma-generate-library
npx skills add figma/mcp-server-guide --skill figma-code-connect

# File management
npx skills add figma/mcp-server-guide --skill figma-create-new-file
npx skills add figma/mcp-server-guide --skill figma-create-design-system-rules
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **implement-design** | 6.0K | Translate Figma designs into production code — layout, components, styling |
| **figma-use** | 5.5K | General Figma MCP server usage — reading designs, extracting assets, inspecting properties |
| **figma-generate-design** | 4.0K | Generate new Figma designs from prompts or specifications |
| **figma-generate-library** | 2.7K | Create reusable Figma component libraries with consistent design tokens |
| **figma-create-new-file** | 2.3K | Programmatically create new Figma files with specific configurations |
| **figma-code-connect** | 2.2K | Connect Figma components to production code — design system synchronization |
| **figma-create-design-system-rules** | 1.7K | Define and enforce design system rules — tokens, spacing, typography, colors |

---

## 🔑 Standout Features

### Design-to-Code Pipeline (implement-design)
The most-installed Figma skill at 6K. Agents can read Figma designs programmatically and generate accurate code implementations — React components, CSS layouts, Tailwind classes — directly from design files. This closes the design-development gap that traditionally requires manual translation.

### Code Connect (figma-code-connect)
Two-way synchronization between Figma components and production code. When code changes, the design system updates. When designs change, code references update. This is the holy grail of design system management — automated, bidirectional, always in sync.

### Design System Rules (figma-create-design-system-rules)
Define tokens, spacing scales, typography hierarchies, and color palettes as enforceable rules. Agents can validate designs against these rules, ensuring consistency across all generated UI.

---

## Hermes Agent Use Cases

- **Landing Page Generation**: Read a Figma design and generate the full HTML/CSS/React implementation
- **UI Component Building**: Extract component specs from Figma and build matching React/Vue/Svelte components
- **Design System Automation**: Maintain design-to-code consistency through automated code connect synchronization
- **Rapid Prototyping**: Generate Figma designs from text descriptions, then implement them in code
- **Design QA**: Validate that implemented UIs match Figma designs pixel-perfect

---

## Discovery Method

Publisher sweep via `npx skills find "design" --owner "figma"`. Figma was not previously catalogued in any sweep. Confirmed 7 skills across the mcp-server-guide repo. The implement-design skill at 6K installs is the most-installed design-to-code skill on skills.sh.

---

## Notes

- **implement-design** (6K) is the highest-install design-to-code skill — direct bridge between Figma and production code
- **figma-code-connect** enables bidirectional design-code sync, a capability no other skills.sh publisher offers
- These skills complement CorpusIQ's media/content generation pipeline for rapid landing page and UI creation
- The MCP server approach means Hermes agents can interact with Figma programmatically without browser automation
