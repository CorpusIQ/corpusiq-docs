---
title: "Blender Skills - MCP Production Pipeline"
description: "arjun988/blender-skills - 50.7K combined installs across 93 indexed listings: 94 Blender skills for an MCP-powered 3D production pipeline."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/blender-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "blender", "3d", "mcp"]
---

# Blender Skills - Setup Guide

**Source:** [arjun988/blender-skills](https://www.skills.sh/arjun988/blender-skills) via skills.sh - 50.7K combined installs across 93 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 3,835 stars, MIT license, `main` branch, last pushed 2026-11-06, `SKILL.md` files under `.claude/skills/<name>/` with a mirrored copy under `.cursor/skills/<name>/`
**Category:** 3D content creation - Blender modeling, rigging, texturing and engine export
**Quality Tier:** 🟢 Green - all 12 sampled skills pass the Gen Agent Trust Hub, Socket and Snyk.

Blender Skills turns Cursor, Claude Code, Kiro and Codex into a senior technical art team for Blender. The repository ships 94 specialist skills covering the full production pipeline, from blockout and modeling through rigging, texturing, lighting, simulation and engine export, plus art direction packs for specific styles, moods, worlds and gameplay genres.

Every skill executes directly inside a running Blender instance through Blender MCP rather than narrating UI steps, and the blender-director skill orchestrates the others by routing a request through the right specialist chain. The `.cursor/skills/` directory is a synced mirror of `.claude/skills/`, so the same pack serves all four clients.

## Installation

Claude Code:

```bash
git clone https://github.com/arjun988/blender-skills.git
cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/
```

Cursor (Windows PowerShell):

```powershell
git clone https://github.com/arjun988/blender-skills.git
Copy-Item -Recurse -Force "blender-skills\.claude\skills\*" ".cursor\skills\"
```

Kiro and Codex:

```bash
# Kiro: copy skill folders into the Kiro skills directory, then restart Kiro
cp -r blender-skills/.claude/skills/* /path/to/kiro/skills/

# Codex: mount or copy skills into the Codex skills path
cp -r blender-skills/.claude/skills/* /path/to/codex/skills/
```

The skills execute through Blender MCP. Set up the connection in four steps: install uv, install the BlenderMCP addon in Blender, open the BlenderMCP sidebar panel and connect, then restart the agent. Cursor reads `.cursor/mcp.json`; Claude Code reads `.mcp.json`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rigging | 729 | Production rigging with armatures, IK/FK, constraints, weight painting and drivers. |
| blender-modeler | 718 | Core Blender modeling for Edit Mode, modifiers, collections, precision modeling and scene organization. |
| character-artist | 715 | AAA character modeling: anatomy, stylization, facial topology, clothing, hair and animation-ready meshes. |
| asset-optimization | 698 | Validates and optimizes assets for polycount, topology, UV efficiency, material count, naming and game-ready performance. |
| materials | 696 | PBR and stylized materials for metal, wood, concrete, fabric, glass, dirt and procedural shaders. |
| environment-artist | 687 | AAA environment art for modular kits, buildings, terrain, vegetation, architecture and scene composition. |
| uv-workflow | 655 | UV unwrapping for seam placement, packing, texel density, UDIM, lightmap UVs and modular layouts. |
| export-pipeline | 655 | Production export to FBX, GLTF, OBJ, USD and Alembic with scale, pivot, rotation, normals, materials, animation and collision verification. |
| qa-review | 654 | Production QA gate using viewport screenshots, validation checklists, naming audits and ship/no-ship verdicts. |
| retopology | 652 | Retopology for animation-ready, low-poly, quad-dominant meshes with clean edge loops and polygon flow. |
| lowpoly-style | 652 | Low-poly art direction inspired by PS1/PS2 and modern lo-fi horror games for readable silhouettes and strong atmosphere. |
| animation | 652 | Game-ready animation including walk/run/idle cycles, combat, mechanical animation, constraints, Graph Editor and NLA workflows. |

The remaining 81 indexed listings range from 483 to 649 installs.

## Why This Matters for Hermes Agents

Agents are usually weak at production 3D because the work spans many specialized disciplines and a single wrong setting, like a flipped normal or a mis-scaled export, ruins the result downstream. Blender Skills splits that expertise into 94 narrow roles and chains them through a director skill, so the agent applies the right specialist to each stage instead of one general model.

The Blender MCP integration is what makes the skills useful rather than instructional: the agent operates the running Blender instance directly, so what it produces is a real .blend change, not a list of menu steps.

The validation discipline matters for delivery. asset-optimization and qa-review gate every asset on polycount, topology, naming and game-readiness before export, which catches the silent failures that agents typically let through.

For a Hermes agent this is a ready-made technical-art pipeline: an orchestrated, MCP-driven suite that covers blockout through engine export for Unreal, Unity and Godot.

## Usage

| You say | What happens |
|---|---|
| "Build a game-ready sci-fi rifle for Unreal Engine" | blender-director routes through hard-surface, uv-workflow, materials, asset-optimization and export-pipeline. |
| "Retopologize this creature sculpt for game animation" | retopology rebuilds the mesh, then uv-workflow, texture-workflow and rigging prepare it for animation. |
| "Match this reference image of an industrial spaceship" | The agent analyzes the photo, camera-matches, then builds geometry, materials and lighting with a screenshot comparison loop. |
| "Validate this asset before export" | asset-optimization and qa-review check polycount, topology and naming, then run a ship/no-ship gate. |
| "Make a modular horror corridor kit" | blender-director chains horror-style, environment-artist and lighting for the atmosphere. |
| "Rig this character for animation" | rigging builds the armature with IK/FK, constraints and weight painting, then hands off to animation. |
| "Export this scene to Godot" | export-pipeline produces the file with scale, pivot, normals and collision verified. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/arjun988/blender-skills/main/.claude/skills/rigging/SKILL.md | head -20
git clone https://github.com/arjun988/blender-skills.git
ls blender-skills/.claude/skills/
```

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rigging | Pass | Pass | Pass |
| blender-modeler | Pass | Pass | Pass |
| character-artist | Pass | Pass | Pass |
| asset-optimization | Pass | Pass | Pass |
| materials | Pass | Pass | Pass |
| environment-artist | Pass | Pass | Pass |
| uv-workflow | Pass | Pass | Pass |
| export-pipeline | Pass | Pass | Pass |
| qa-review | Pass | Pass | Pass |
| retopology | Pass | Pass | Pass |
| lowpoly-style | Pass | Pass | Pass |
| animation | Pass | Pass | Pass |

All 12 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 50,725 combined installs across 93 indexed listings; 3,835 GitHub stars; MIT; last pushed 2026-11-06. Counts drift over time.
- The skills.sh marketplace listing is under review by Anthropic, so install directly from GitHub until it is published.
- Skills only act inside Blender when Blender MCP is connected; without the addon and a running Blender instance they describe steps instead of executing them.
- The README and tree carry 94 skills including the blender-director orchestrator, but skills.sh indexes 93 listings; blender-director is not an indexed listing.
- Install copies skill folders into `.claude/skills/` or `.cursor/skills/` rather than a managed package, so updates mean re-copying the folders.
- The Cursor snippet targets Windows PowerShell; macOS and Linux Cursor users copy the same folders with shell commands.

## Related

- [Blender Agent Skills](/hermes/skills/catalog/blender-agent-skills-setup)
- [Unreal Engine Skills](/hermes/skills/catalog/unreal-engine-skills-setup)
- [Unity AI Skills](/hermes/skills/catalog/unity-ai-skills-setup)
- [CC Godot](/hermes/skills/catalog/cc-godot-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let blender-director route requests instead of invoking specialist skills directly; it chains the right pipeline for the asset type.
- Attach a reference image and ask for a match; the agent camera-matches, builds, then screenshot-compares in a loop.
- Run asset-optimization and qa-review as the final gate before any engine export.
- Keep a running Blender instance with the BlenderMCP addon connected, or skills fall back to narrating UI steps.
- Read SKILLS_GUIDE.md for the subtype coverage map, decision trees and workflow combinations.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
