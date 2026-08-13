---
title: OpenTUI — Setup Guide for Hermes Agents
description: Build terminal user interfaces with Core, React, or Solid APIs — 52.8K+ installs
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/opentui-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# OpenTUI — Setup Guide

**Source:** [msmps/opentui-skill](https://github.com/msmps/opentui-skill) (Community)
**Skill:** `opentui` · **Installs:** 52,800+ · **Category:** Development & Tools
**Platform:** Linux, macOS, Windows

OpenTUI is a consolidated skill for building terminal user interfaces (TUIs) with the OpenTUI framework. It supports Core, React, and Solid APIs for components, layout, keyboard/keymap handling, animations, and testing. Perfect for Hermes agents that need to create terminal-based dashboards, monitors, or interactive CLI tools.

## Installation

```bash
npx skills add msmps/opentui-skill@opentui
```

## What It Does

OpenTUI provides a complete TUI development workflow:
- **Framework selection** — Choose Core, React, or Solid based on project needs
- **Component library** — Pre-built TUI components (tables, forms, charts, etc.)
- **Layout system** — Flexible terminal layout management
- **Keyboard handling** — Keymap configuration and input management
- **Animation support** — Terminal animations and transitions
- **Testing utilities** — TUI-specific test helpers

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Node.js | v18+ (for React/Solid APIs) |
| Bun | Recommended for `create-tui` scaffolding |
| Terminal | Any modern terminal emulator with Unicode support |

## Critical Rules

When using OpenTUI with Hermes agents:

1. **Use `create-tui` for new projects** — See framework `REFERENCE.md` quick starts
2. **`create-tui` options must come before arguments** — `bunx create-tui -t react my-app` works, `bunx create-tui my-app -t react` does NOT
3. **Never call `process.exit()` directly** — Use `renderer.destroy()` instead
4. **Text styling requires nested tags in React/Solid** — Use modifier elements, not props

## Usage with Hermes

The skill loads detailed reference files based on your framework choice:

```
# Hermes automatically loads the right references when TUI tasks are detected
"Build a terminal dashboard showing real-time system metrics"
"Create an interactive CLI form for user input"
"Add keyboard shortcuts to my terminal app"
```

### Framework Decision Tree

| Requirement | Recommended Framework |
|-------------|----------------------|
| Simple, fast TUI | Core API |
| Complex state management | React API |
| Reactive data flows | Solid API |

## Reference File Structure

Framework references follow a 5-file pattern:
- `REFERENCE.md` — Main framework reference
- `components/` — Component-specific docs
- `layout/` — Layout system docs
- `keyboard/` — Input handling
- `testing/` — Test patterns

Cross-cutting concepts (animation, keymaps) are single-file guides.

## Related Skills

- [CLI Anything Harnesses Setup](/docs/hermes/skills/catalog/cli-anything-harnesses-setup/) — CLI tool wrappers
- [Browser Harness Setup](/docs/hermes/skills/catalog/browser-harness-setup/) — Browser automation
- [Terminal Skills Setup](/docs/hermes/skills/catalog/terminal-skills-setup/) — General terminal operations

## Source

- **skills.sh:** [msmps/opentui-skill@opentui](https://skills.sh/msmps/opentui-skill)
- **GitHub:** [github.com/msmps/opentui-skill](https://github.com/msmps/opentui-skill)
