---
title: "Flue - Desktop Software Control for Agents Setup"
description: "sfkislev/flue - 31.1K combined installs: let agents control desktop apps like Photoshop, Premiere, and Blender from the shell without MCP servers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sfkislev-flue-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "desktop automation", "adobe", "blender"]
---

# Flue - Setup Guide

**Source:** [sfkislev/flue](https://www.skills.sh/sfkislev/flue) via skills.sh - 31.1K combined installs across 11 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [SFKislev/Flue](https://github.com/SFKislev/Flue) - 112 stars, MIT license, last pushed Oct 18, 2026, main branch; skills in skills/<name>/SKILL.md with app adapters in adapters/<app>_adapter/.
**Category:** Agent Tooling (Desktop App Control)
**Quality Tier:** 🟡 Yellow - all 11 listings sampled: two carry a Warning (Adobe on Snyk, Autodesk on Gen Agent Trust Hub) and nine pass all three checks; no Fails.

sfkislev/flue is Flue, a small bridge that lets coding agents drive desktop software directly from the shell with a single pip install and no MCP servers. The agent sends a script through a bridge command, the bridge runs it inside the app's own scripting runtime (COM, AppleScript, or a local endpoint), and the app returns JSON. The 11 indexed listings cover the core flue skill plus per-application skills for Adobe Creative Cloud, Blender, Houdini, Autodesk, and Figma.

Flue installs as a skill that surfaces a Python bridge, and `flue setup` detects installed agentic harnesses - Claude Code, Codex, Copilot, Cursor, OpenCode, Hermes, Gemini CLI, Antigravity CLI, Qwen CLI, Cline, and Kilo CLI - so each knows the bridge is available. Every application adapter ships its own AGENTS.md and APP.md describing the app-specific scripting surface, with Windows and macOS supported.

## Installation

```bash
pip install flue
flue setup
```

`flue setup` detects your agentic harnesses and registers the Flue skill with them. For first-run checks and app-specific prerequisites, see docs/setup.md. Some applications need a one-time bridge install beyond pip: a Blender addon, a Figma plugin import, a CEP bridge for Adobe apps, and a 3ds Max bridge, each handled by an install_*.ps1 script in the matching adapter directory.

## What It Provides

skills.sh publishes per-skill install counts for all 11 indexed listings. The 8 most-installed skills are listed below; the remaining 3 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| flue | 12,601 | Core Flue bridge: let agents control desktop apps from the shell with no MCP servers |
| Blender | 3,012 | Control Blender from the shell via a Python bridge to bpy |
| Photoshop | 2,239 | Control Adobe Photoshop from the shell via ExtendScript bridges |
| Illustrator | 2,176 | Control Adobe Illustrator from the shell via ExtendScript bridges |
| Adobe | 1,912 | Control Adobe desktop apps (Photoshop, Illustrator, Premiere, After Effects, InDesign, Audition) |
| Premiere | 1,904 | Control Adobe Premiere Pro from the shell via ExtendScript bridges |
| Houdini | 1,861 | Control SideFX Houdini from the shell via a Python bridge to hou |
| InDesign | 1,839 | Control Adobe InDesign from the shell via ExtendScript bridges |

The remaining 3 indexed listings range from 10 to 1,838 installs.

## Why This Matters for Hermes Agents

Flue replaces the fragile parts of desktop automation with a direct path into the scripting APIs each application already ships. Instead of MCP schemas, screenshots, or a computer-use harness, an agent sends a script through a small bridge command and gets JSON back. Hermes is a first-class target: `flue setup` registers the skill with Hermes alongside Claude Code, Codex, and the rest, so a Hermes agent can take a real task inside Photoshop, Blender, Unity, or Houdini without standing up or maintaining any server. For a builder who already pays for a scripting-capable model, that means lower maintenance than MCP servers and less fragility than pixel-driven control. The trade-off is coverage: Flue only reaches the apps that expose a scripting runtime, and some of those need a one-time plugin or addon install a human must perform.

## Usage

| You say | What happens |
|---|---|
| Add a blue cube to the Blender scene | Uses the Blender skill to drive bpy through the bridge |
| Create a retouch layer in Photoshop | Uses the Photoshop skill's ExtendScript examples |
| Set the selected stroke to black 1pt in Illustrator | Uses the Illustrator skill's ExtendScript examples |
| Build a scene in Unity | Uses the Unity skill to send JSON commands through the bridge |
| Check which apps Flue can drive | Flue reports the supported desktop apps and their bridges |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/SFKislev/Flue/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/SFKislev/Flue/main/skills/blender/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skill before relying on it, and re-check the security pages on skills.sh for the Warnings noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| flue | Pass | Pass | Pass |
| Blender | Pass | Pass | Pass |
| Photoshop | Pass | Pass | Pass |
| Illustrator | Pass | Pass | Pass |
| Adobe | Pass | Pass | Warn |
| Premiere | Pass | Pass | Pass |
| Houdini | Pass | Pass | Pass |
| InDesign | Pass | Pass | Pass |
| Autodesk | Warn | Pass | Pass |
| Audition | Pass | Pass | Pass |
| Figma | Pass | Pass | Pass |

All 11 listings were sampled: two carry a Warning (Adobe on Snyk, Autodesk on Gen Agent Trust Hub) and nine pass all three checks, with no Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 31,135 combined installs across 11 indexed listings; 112 GitHub stars; MIT license; last pushed Oct 18, 2026. Counts drift over time.
- The Figma listing trails the rest at 10 installs and needs a one-time plugin import in the desktop app.
- The bridge install scripts are PowerShell (install_*.ps1), which is Windows-first; macOS uses AppleScript and local HTTP bridges instead.
- Several applications need app-specific setup beyond `pip install` (Blender addon, Adobe CEP bridge, Unity package).
- Flue replaces the MCP-server approach, so a harness already wired for MCP schemas has to switch to bridge commands.

## Related

[Agent Desktop - Computer Use for Agents Setup](/hermes/skills/catalog/agent-desktop-setup) | [Agent Device - Mobile Device Control for Agents](/hermes/skills/catalog/agent-device-setup) | [Agent Browser - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/agent-browser-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `flue setup` after installing so every harness, including Hermes, registers the Flue skill.
- Point agents at docs/setup.md for first-run checks and app-specific prerequisites before their first task.
- Ask agents to surface any app-specific setup a human must do (plugin import, addon install) instead of failing silently.
- Keep the Figma desktop app open and import its one-time plugin before relying on the Figma skill.
- Prefer Flue over screenshots or computer-use control for any app that exposes a scripting API.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
