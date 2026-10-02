---
title: Unity AI Skills - Official 29-Skill Game Dev Suite
description: "Unity-Technologies/skills - 29 first-party Agent Skills for Unity workflows: project bootstrap, package management, builds, UI, graphics, multiplayer, monetization. 56.8K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/unity-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "unity", "game development", "csharp", "3d"]
---

# Unity AI Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/unity-technologies/skills) (29 skills, ~56.8K combined installs)
**GitHub:** [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills) (823⭐, 42 forks, C#, pushed Sep 10, 2026 - actively maintained; no LICENSE file present)
**Category:** Game Development / Unity
**First Seen:** Jun 8, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟢 Production (all three skills.sh audits Pass on the flagship skill)

Unity's official agent skill collection - 29 reusable skills that turn an agent into a Unity operator. Bootstrap version-controlled projects, drive the Unity CLI, manage UPM packages programmatically, run builds, and implement graphics, UI, multiplayer, and monetization features. The README states compatibility with Claude Code, GitHub Copilot, Cursor, Cline, and 50+ other agents - agent-agnostic Agent Skills format installable anywhere.

---

## Installation

```bash
npx skills add Unity-Technologies/skills
```

For Hermes Agent, copy skill folders from a clone:

```bash
git clone https://github.com/Unity-Technologies/skills.git
cp -r skills/skills/* ~/.hermes/skills/
```

## Skill Roster (top 15 of 29)

| Skill | Installs | What It Does |
|---|---|---|
| `unity-cli` | 4.4K | Unity CLI control - bootstrap projects, install editors, manage projects, run builds, check auth |
| `unity-package-management` | 3.6K | Add/remove/upgrade/discover UPM packages programmatically (headless/CI via PackageManager Client API) |
| `new-unity-project` | 3.1K | Guided flow from idea to running version-controlled project - delegates to the skills below |
| `build-live-game` | 2.9K | Build and operate a live game |
| `ui-ugui` | 2.8K | uGUI UI construction |
| `levelplay-unity-integration` | 2.8K | LevelPlay ad-mediation SDK integration |
| `implement-in-app-purchases` | 2.7K | IAP implementation for monetization |
| `ui-uitk` | 2.7K | UI Toolkit workflows |
| `ui` | 2.6K | General UI work |
| `urp-postprocessing` | 2.4K | URP post-processing setup |
| `optimize-text-mesh-pro` | 2.4K | TextMeshPro performance work |
| `sprite-editor` | 2.3K | 2D sprite workflows |
| `shader-graph-create-custom-node` | 2.3K | Custom shader graph nodes |
| `validate-urp-render-graph-renderer-feature` | 2.3K | URP render-graph feature validation |
| `optimize-audio` | 2.3K | Audio optimization |

Remaining 14 cover localization, web optimization, AI navigation, multiplayer services, Vivox voice chat, sprite atlases, tilemaps, 2D pixel-perfect setup, BIRP-to-URP migration, and more.

## Quick Start

1. Install the suite (no API keys - Unity Editor + CLI do the work)
2. Ask for a project - "create a new 2D mobile game project with ads and IAP" - `new-unity-project` gathers concept, platforms, and monetization, then delegates setup to the specific skills
3. `unity-cli` drives the Editor from the terminal: `unity status`, `unity command editor_play`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Monetization intelligence** | `levelplay-unity-integration` + `implement-in-app-purchases` encode Unity's canonical ad-mediation and IAP patterns - reference architecture for e-commerce and app-monetization client work |
| **Game-dev client support** | CorpusIQ operators building games or gamified apps get a complete agent-driven Unity workflow |
| **Visual/3D work** | URP, shader graph, and UI skills cover graphics pipelines for any 3D product work |

## Limitations / Verification

- **No LICENSE file:** the repo ships no LICENSE file (verified Sep 11, 2026). Content is freely readable, but license terms are unstated - flag for legal before redistribution.
- **Unity Editor required:** most skills operate a locally installed Unity Editor and CLI; headless/CI use needs a Unity license.
- **C#-centric:** skills assume Unity's ecosystem - not general-purpose agent skills.

```bash
# Verify skill installed
ls ~/.hermes/skills/unity-cli/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Three Agent Bridge Setup](/hermes/skills/catalog/three-agent-bridge-setup)
- [Cline Skills - Official Cline 43-Skill Collection Setup](/hermes/skills/catalog/cline-skills-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
