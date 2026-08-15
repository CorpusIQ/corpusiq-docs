---
title: CMUX Skills — Agent Terminal Multiplexer Setup
description: "manaflow-ai/cmux — 22 skills at 76.3K installs for the cmux macOS window/workspace/pane/surface multiplexer (26.1K GitHub stars): browser panels, testing, dev workflow, backend, customization, diagnostics, and keyboard shortcuts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cmux-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "terminal", "multiplexer"]
---

# CMUX Skills — Setup Guide

**Source:** [manaflow-ai/cmux](https://skills.sh/manaflow-ai/cmux)
**GitHub:** [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) (26.1K stars)
**Skills:** 22 skills · 76.3K total installs
**Category:** Terminal Multiplexing & Agent Workspaces
**First Seen:** February 4, 2026 (catalogued August 15, 2026 sweep)
**Quality Tier:** 🟢 Production (all three security audits pass)

cmux is a macOS multiplexer that organizes agent sessions into a topology of windows, workspaces, panes, and surfaces, where a surface can be a terminal or a browser panel. The 22-skill cluster documents operating it end to end: browser panels, testing, dev workflow, backend, customization, diagnostics, keyboard shortcuts, and release/billing internals. The core skill defines the topology explicitly: window → workspace → pane → surface.

---

## Installation

```bash
npx skills add manaflow-ai/cmux
```

Individual skills:

```bash
npx skills add manaflow-ai/cmux --skill cmux-browser
npx skills add manaflow-ai/cmux --skill cmux-testing
```

## Prerequisites

| Requirement | Details |
|---|---|
| **macOS** | cmux is a macOS window/workspace multiplexer |
| **cmux installed** | The skills operate the cmux application |
| **Node.js + npx** | For the installer |

## What It Provides

| Skill | Installs | Notes |
|---|---|---|
| cmux | 7.0K | Core topology and routing (window/workspace/pane/surface) |
| cmux-browser | 6.4K | Browser panels inside cmux |
| cmux-markdown | 5.6K | Markdown rendering in panes |
| cmux-settings | 4.8K | Configuration |
| cmux-workspace | 4.6K | Workspace management |
| cmux-customization | 4.6K | Appearance and layout |
| cmux-diagnostics | 4.5K | Troubleshooting |
| cmux-keyboard-shortcuts | 4.2K | Shortcut reference |
| cmux-testing | 3.0K | Testing workflows |
| cmux-architecture | 3.0K | Internals |
| cmux-dev-workflow | 3.0K | Development loop |
| cmux-debugging / cmux-backend / cmux-billing / cmux-release | 2.9K / 2.9K / 1.7K / 2.9K | Debugging, backend, billing, release process |
| cmux-ghostty / cmux-custom-sidebar / cmux-socket-policy / cmux-shared-behavior / cmux-localization | 2.9K each | Terminal integration, UI, sockets, shared behavior, i18n |

## Quick Start

1. `npx skills add manaflow-ai/cmux`
2. Ask: "create a workspace with a terminal pane and a browser surface side by side"
3. Use `cmux-keyboard-shortcuts` for the shortcut reference during a session

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent workstation layout** | Window/workspace/pane/surface topology for running research alongside browser inspection |
| **Browser panels** | cmux-browser as a lightweight alternative to separate browser windows during agent work |
| **Dev workflow reference** | cmux-dev-workflow and cmux-testing patterns for structured agent development loops |
| **Multi-surface monitoring** | Side-by-side terminal + browser panels for cron debugging sessions |

## Limitations / Verification

- macOS only — no Linux or Windows surface
- Value requires running cmux itself; the skill cluster documents the tool

```bash
npx skills add manaflow-ai/cmux --skill cmux   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [NuShell Pro — Structured Shell Scripting Setup](/hermes/skills/catalog/nushell-pro-setup/) — shell workflows

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
