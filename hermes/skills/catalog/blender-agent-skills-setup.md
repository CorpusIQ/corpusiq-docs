---
title: "Blender Agent Skills - 3D Production Workflows"
description: "el4cteo/blender-skills: 12.2K combined installs across 28 listings, professional Blender 5.3 modeling, rigging, animation and export workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/blender-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "blender", "3d", "game assets"]
---

# Blender Agent Skills - Setup Guide

**Source:** [el4cteo/blender-skills](https://www.skills.sh/el4cteo/blender-skills) via skills.sh - 12.2K combined installs across 28 indexed listings; first seen Nov 14, 2026
**GitHub:** 1,087 stars, MIT license, `main` branch, last pushed 2026-11-13, 28 `SKILL.md` files in `skills/<name>/` folders
**Category:** 3D content creation skills for Blender agents
**Quality Tier:** 🟢 Green - all six sampled verdicts pass, MIT license, and 28 in-tree skills.

Blender Agent Skills packages 28 professional Blender workflows as Agent Skills for Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot and Cursor. The skills cover the full 3D pipeline - modeling, UVs, texturing, baking, rigging, animation, clothing, hair, environments, stylized looks, optimization, export, rendering, video, weather, simulation and QA - built for Blender 5.2 LTS+ (verified on 5.3).

Every script is tested in a real Blender, and the README recommends updating to Blender 5.3.0 for the best experience: every skill is verified on it, and it adds KTX2 web export, the compositor effects stack and Gaussian splats. The repo tracks 190 files with 28 `SKILL.md` entries; the twelve most-installed skills appear in the table below.

## Installation

Install the Claude Code plugin:

```text
/plugin marketplace add EL4CTEO/blender-skills
/plugin install blender-agent-skills@blender-agent-skills
```

For any other agent, clone the repo and run the bundled installer:

```bash
git clone https://github.com/EL4CTEO/blender-skills
./blender-skills/install/install.sh          # macOS / Linux
```

The installer also ships `install.ps1` for Windows. It defaults to `~/.claude/skills` and `~/.agents/skills`; the latter is read by Codex, OpenCode, Gemini CLI, Copilot and Cursor. Options include `--agent claude|codex|opencode|gemini|copilot|cursor|all` and `--project DIR` for a single project. Requirements: Blender 5.2 LTS or newer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| blender-core | 739 | Foundation for Blender tasks - runs bpy via MCP or headless CLI and enforces 5.x API rules. |
| blender-character-rigging | 604 | Character rigging with Rigify fit/generate, bone naming and DEF/MCH/control layers. |
| blender-animation | 596 | Animation with slotted actions, the channelbag API, Python keyframing and F-curves. |
| blender-asset-qa | 589 | Review gate for meshes and assets; detects z-fighting, floating parts and bad weights. |
| blender-export-pipelines | 524 | Export with verified presets for Roblox and Unity (FBX, glTF, cages, R15). |
| blender-game-optimization | 505 | Optimize assets for real-time engines with triangle, material and bone budgets. |
| blender-pbr-materials | 501 | Physically based materials with metal/roughness rules and Principled BSDF inputs. |
| blender-hardsurface-modeling | 482 | Hard-surface and prop modeling with blockout-to-detail flow and modifier stacks. |
| blender-lighting-lookdev | 471 | Lighting, cameras and look-dev with studio 3-point lighting and HDRI environments. |
| blender-texture-baking | 467 | Bake texture maps in Cycles - high-to-low normals, AO, curvature and ID maps. |
| blender-retopology-uv | 464 | Retopology and UVs with auto retopo, deformation edge flow and seam placement. |
| blender-rendering | 453 | Render with Cycles, EEVEE and Workbench - quality presets, GPU setup and denoising. |

The remaining 16 indexed listings range from 254 to 441 installs.

## Why This Matters for Hermes Agents

Blender Agent Skills treats 3D production as a pipeline with named stages - modeling, UVs, texturing, baking, rigging, animation and export - rather than a grab bag of Blender prompts. Each stage is a dedicated skill, so an agent can route a task to the right workflow and produce a game-ready asset instead of an edit pile with no provenance.

The built-in QA gate is the second point. blender-asset-qa is a mandatory review gate for any mesh or asset an agent creates or edits, catching z-fighting, floating parts and bad weights before export - exactly the guardrail agents need when they generate geometry unattended.

The engine-agnostic export coverage matters for builders shipping to multiple platforms: the export skill carries verified presets for Roblox, Unity and other targets, and the optimization skill enforces per-platform triangle, material and bone budgets. Finally, every script is tested in a real Blender, which reduces the chance an agent emits bpy calls that fail at runtime.

## Usage

| You say | What happens |
|---|---|
| "Make a game-ready crate for Unreal" | Runs hardsurface-modeling, texture-baking and export-pipelines for a baked, exported asset. |
| "Rig this character and export a walk cycle to Unity" | Runs character-rigging with Rigify, then animation and export-pipelines. |
| "Check this model for z-fighting and floating parts" | Runs blender-asset-qa over the mesh and returns the review findings. |
| "Make this street a rainy night with puddles" | Runs blender-weather-fx and blender-time-of-day for rain, puddles and mood lighting. |
| "Give my character a shirt and hair cards" | Runs blender-clothing and blender-hair-grooming, then retargets the animation. |
| "Optimize this model for a mobile game" | Runs blender-game-optimization against triangle, texture and bone budgets. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/el4cteo/blender-skills/main/skills/blender-core/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/el4cteo/blender-skills/main/skills/blender-character-rigging/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/el4cteo/blender-skills/main/skills/blender-animation/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on the `main` branch.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| blender-core | Pass | Pass | Pass |
| blender-character-rigging | Pass | Pass | Pass |
| blender-animation | Pass | Pass | Pass |
| blender-asset-qa | Pass | Pass | Pass |
| blender-export-pipelines | Pass | Pass | Pass |
| blender-game-optimization | Pass | Pass | Pass |

All six sampled skills pass all three auditors. The sample covers only 6 of the 28 indexed listings, so it says little about the remaining 22.

## Limitations

- Snapshot data, verified 2026-11-14: 12,176 combined installs across 28 indexed listings; 1,087 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- The README documents no `npx skills` install command; it documents a Claude Code plugin and a clone-and-run installer instead.
- All six sampled verdicts pass, but the sample covers only 6 of 28 listings; the rest publish no verdict on skills.sh.
- This is not a prompt-only pack. The repo ships 190 tracked files including install scripts and assets, and the skill-level verdicts do not cover those artifacts.
- The skills are built for Blender 5.2 LTS+ (verified on 5.3); older Blender installs may not support every skill.

## Related

- [CC Blender Skill - 3D Production for Agents](/hermes/skills/catalog/cc-blender-skill-setup)
- [SpriteCook Skills - Pixel Art and Game Assets](/hermes/skills/catalog/spritecook-skills-setup)
- [Claude Design Skillstack - 3D & Animation Setup](/hermes/skills/catalog/claudedesignskills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with blender-core to learn the routing and API rules before adopting the full pipeline.
- Run blender-asset-qa on every asset before export; it is the mandatory review gate.
- Keep a Blender MCP server running so agents drive your open Blender instead of spawning headless instances.
- Use the installer's `--agent` and `--project` flags to scope skills to a single agent or project.
- Update to Blender 5.3.0 for KTX2 web export, the compositor effects stack and Gaussian splats.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
