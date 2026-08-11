---
title: Debugging Hermes TUI Commands — Skill Setup Guide
description: Install and configure debugging-hermes-tui-commands, the official Hermes Agent skill for troubleshooting TUI slash command issues — 76 installs.
---

# Debugging Hermes TUI Slash Commands — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/debugging-hermes-tui-commands) (76 installs)
**Category:** Development / Debugging
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent TUI (Ink/TypeScript frontend)

Diagnose and fix Hermes TUI slash command issues across the three-layer architecture: Python command registry, `tui_gateway` JSON-RPC bridge, and Ink/TypeScript frontend. Essential for Hermes developers and power users debugging command autocomplete, registration, or TUI-CLI inconsistency.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Command autocomplete debugging** | Diagnose why commands don't appear in TUI autocomplete |
| **Layer desync detection** | Identify when Python registry ≠ gateway ≠ frontend |
| **TUI-CLI inconsistency** | Fix commands that work in CLI but not TUI |
| **Config persistence** | Debug commands that persist config but don't apply live |
| **New command registration** | Walkthrough for adding commands to all three layers |

---

## Architecture Overview

Hermes slash commands span three layers:

```
┌─────────────────────────────┐
│  Ink/TypeScript Frontend    │  ← What you see (autocomplete, rendering)
├─────────────────────────────┤
│  tui_gateway JSON-RPC       │  ← Bridge between Python ↔ TypeScript
├─────────────────────────────┤
│  Python Command Registry    │  ← Backend command definitions
└─────────────────────────────┘
```

A bug in any single layer can cause commands to fail silently.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill debugging-hermes-tui-commands
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/development/debugging-hermes-tui-commands ~/.hermes/skills/
```

---

## When to Use

| Symptom | Likely Layer | Action |
|---------|-------------|--------|
| Command missing from autocomplete | Frontend or Gateway | Check `tui_gateway` command list |
| Works in CLI, not TUI | Gateway bridge | Verify JSON-RPC method registration |
| Config saves but TUI stale | Frontend | Check frontend config reload logic |
| Command registered but no-op | Python registry | Verify command handler binding |
| Adding new command | All three | Follow the three-layer registration |

---

## Common Debugging Commands

```bash
# Check registered Python commands
hermes commands list

# Restart TUI gateway
hermes gateway restart

# Check TUI frontend for loaded commands
# (In TUI, type / and observe autocomplete)

# Verify JSON-RPC bridge is healthy
curl -s http://localhost:$(hermes gateway port)/health
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ (TUI-enabled) |
| Node.js | 18+ (for Ink/TypeScript frontend) |
| Terminal | TUI-capable (iTerm2, Kitty, WezTerm, Windows Terminal) |

---

## Verification

After install, test by diagnosing a known command:

```
Hermes, why doesn't /my-custom-command show up in the TUI autocomplete?
```

The agent should walk through the three-layer diagnostic: Python registry → gateway → frontend.

---

## Pitfalls

- **TUI-only skill:** Does not apply to CLI-only Hermes deployments. The three-layer architecture is TUI-specific.
- **Requires TUI access:** You need a running Hermes TUI to verify fixes. Cannot diagnose purely from CLI.
- **Gateway restart needed:** Many fixes require `hermes gateway restart` to take effect. The skill will guide this but won't auto-restart.

---

**Installed via:** `npx skills add nousresearch/hermes-agent --skill debugging-hermes-tui-commands`
