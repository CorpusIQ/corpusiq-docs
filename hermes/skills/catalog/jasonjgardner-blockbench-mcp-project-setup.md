---
title: "Blockbench MCP Skills - 3D Production Setup"
description: "jasonjgardner/blockbench-mcp-project - 11.4K combined installs: Blockbench MCP skills for modeling, texturing, animation, and PBR materials."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jasonjgardner-blockbench-mcp-project-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "3d modeling", "blockbench", "mcp"]
---

# Blockbench MCP Skills - Setup Guide

**Source:** [jasonjgardner/blockbench-mcp-project](https://www.skills.sh/jasonjgardner/blockbench-mcp-project) via skills.sh - 11.4K combined installs across 15 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [jasonjgardner/blockbench-mcp-project](https://github.com/jasonjgardner/blockbench-mcp-project) - 30 stars, Apache-2.0 license, last pushed Sep 26, 2026, main branch; 15 skill folders under skills/<name>/SKILL.md plus a 9-skill mirror under .claude/skills/.
**Category:** 3D Modeling and Game Asset Authoring (Blockbench MCP)
**Quality Tier:** 🟠 Orange - 15 sampled skills: eleven pass all three checks, three carry a Snyk Warn, and one carries a Gen Agent Trust Hub Fail.

jasonjgardner/blockbench-mcp-project is an example project that shows how to set up the Blockbench MCP server for agent use. Every skill here drives the Blockbench MCP plugin, so the skills only do anything when the desktop Blockbench application is running with that plugin installed and its MCP endpoint reachable. The repository itself is a sample harness for that plugin, not the plugin.

The 15 indexed listings cover 3D modeling, texturing, animation, PBR materials, Hytale and Minecraft-specific workflows, and AI texture generation. Fourteen listings have a matching skills/<name>/SKILL.md in the current tree; blockbench-plugins carries installs but no matching directory, while the tree instead ships blockbench-development, which skills.sh does not index.

## Installation

The desktop Blockbench application must be running in the background first. The README pins the MCP port to 3000 and the endpoint to bb-mcp (the plugin defaults, changeable in the plugin settings).

The repository is a Claude Code plugin; installing it registers the desktop and headless MCP servers, every skill in skills/, and the reviewer agent in agents/:

```bash
claude plugin marketplace add jasonjgardner/blockbench-mcp-project
claude plugin install blockbench-mcp@blockbench-mcp-project --scope user
```

Individual skills install with the generic skills CLI, one per command:

```bash
npx skills add https://github.com/jasonjgardner/blockbench-mcp-project --skill blockbench-use
npx skills add https://github.com/jasonjgardner/blockbench-mcp-project --skill blockbench-modeling
```

To add only the desktop MCP server without the plugin:

```bash
claude mcp add blockbench npx mcp-remote http://localhost:3000/bb-mcp
```

## What It Provides

skills.sh publishes per-skill install counts for all 15 indexed listings. The 8 most-installed skills are listed below; the remaining 7 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| blockbench-modeling | 1,559 | build and edit 3D models with cubes, meshes, spheres, and cylinders; edit vertices, extrude faces, and group models |
| blockbench-texturing | 1,417 | paint textures and manage UVs with brushes, layers, fills, gradients, and shapes |
| blockbench-animation | 1,368 | create animations with keyframes, bone rigs, and animation curves |
| blockbench-mcp-overview | 1,315 | tour of the Blockbench MCP server tools, resources, and prompts for new projects |
| blockbench-use | 1,135 | mandatory orchestrator loaded before Blockbench MCP calls; routes to sub-skills and enforces pre-flight checks and exports |
| blockbench-pbr-materials | 986 | author PBR materials for Minecraft Bedrock RTX with normal, height, and MER maps and texture_set.json |
| blockbench-hytale | 946 | Hytale-specific models and animations with attachments, shading modes, quads, and visibility keyframes |
| blockbench-plugins | 753 | Blockbench plugin authoring; listing has no matching directory in the current tree |

The remaining 7 indexed listings range from 227 to 310 installs.

## Why This Matters for Hermes Agents

These skills turn a blocky 3D authoring tool into something an agent can drive programmatically, which matters if a Hermes agent has to produce game-ready assets (Minecraft, Hytale, or generic low-poly models) as part of a task. The blockbench-use skill is the key piece of discipline: it is a mandatory orchestrator that every Blockbench MCP call routes through, enforcing pre-flight checks, checkpoints, and exports instead of letting an agent fire raw MCP calls at a half-configured scene. The modeling, texturing, animation, and PBR skills then encode the actual workflows, and blockbench-mcp-overview gives the agent a map of the whole tool, resource, and prompt surface before it starts. The caveat is that everything here is gated on the Blockbench MCP plugin, so an agent cannot do useful work without a running desktop Blockbench instance behind it.

## Usage

| You say | What happens |
|---|---|
| Model a low-poly character from cubes | Uses blockbench-modeling to build cube and mesh geometry and edit vertices and groups |
| Paint a texture for this model | Uses blockbench-texturing for brushes, layers, fills, and UV mapping |
| Animate a walk cycle | Uses blockbench-animation to add keyframes and bone rigs |
| Set up PBR materials for Bedrock RTX | Uses blockbench-pbr-materials for normal, height, and MER maps and texture_set.json |
| Where do I start with Blockbench MCP | Uses blockbench-mcp-overview for the tool, resource, and prompt tour |
| Run any Blockbench MCP operation | Uses blockbench-use as the orchestrator that routes to the right sub-skill |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/jasonjgardner/blockbench-mcp-project/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/jasonjgardner/blockbench-mcp-project/main/skills/blockbench-use/SKILL.md | head -40
```

Both URLs return 200. After installing, confirm the Blockbench desktop application is running with the MCP plugin active before relying on any skill, and review each skills/<name>/SKILL.md before use.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| blockbench-modeling | Pass | Pass | Pass |
| blockbench-texturing | Pass | Pass | Pass |
| blockbench-animation | Pass | Pass | Pass |
| blockbench-mcp-overview | Pass | Pass | Pass |
| blockbench-use | Pass | Pass | Pass |
| blockbench-pbr-materials | Fail | Pass | Pass |
| blockbench-hytale | Pass | Pass | Warn |
| blockbench-plugins | Pass | Pass | Pass |
| blockbench-gpt-image-textures | Pass | Pass | Pass |
| blockbench-new-model | Pass | Pass | Warn |
| blockbench-flipbook-textures | Pass | Pass | Warn |
| blockbench-vanilla-textures | Pass | Pass | Pass |
| blockbench-particles | Pass | Pass | Pass |
| blockbench-albedo-to-pbr | Pass | Pass | Pass |
| blockbench-substance | Pass | Pass | Pass |

All 15 listings were sampled; eleven pass all three checks, three carry a Snyk Warn (blockbench-hytale, blockbench-new-model, blockbench-flipbook-textures), and one carries a Gen Agent Trust Hub Fail (blockbench-pbr-materials).

## Limitations

- Snapshot data, verified Nov 25, 2026: 11,450 combined installs across 15 indexed listings; 30 GitHub stars; Apache-2.0 license; last pushed Sep 26, 2026. Counts drift over time.
- Every skill depends on the Blockbench MCP plugin running inside a desktop Blockbench instance; the repository is an example harness for that plugin, not the plugin itself.
- Index-vs-tree drift: blockbench-plugins carries 753 installs but has no matching directory in the current tree, while blockbench-development exists in the tree but is not indexed.
- The README install list names one skill blockbench-albedo-to-normal, while the indexed listing is blockbench-albedo-to-pbr; confirm the current name before scripting installs.
- One listing carries a Gen Agent Trust Hub Fail and three carry a Snyk Warn; review those security pages before production use.

## Related

[Blender Agent Skills - 3D Production Workflows](/hermes/skills/catalog/blender-agent-skills-setup) | [CC Blender Skill - 3D Production for Agents](/hermes/skills/catalog/cc-blender-skill-setup) | [Text to CAD Skills - 3D Model and URDF Setup](/hermes/skills/catalog/text-to-cad-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep the desktop Blockbench application running with the MCP port on 3000 and the bb-mcp endpoint before any agent starts driving the skills.
- Load blockbench-use first; it is the orchestrator that routes to the right sub-skill and enforces pre-flight checks, checkpoints, and exports.
- Add only the desktop server with `claude mcp add blockbench npx mcp-remote http://localhost:3000/bb-mcp` if you want the skills without the full plugin.
- For Minecraft Bedrock RTX work, pair blockbench-pbr-materials with blockbench-albedo-to-pbr and blockbench-vanilla-textures.
- Install individual skills with `npx skills add https://github.com/jasonjgardner/blockbench-mcp-project --skill <name>` rather than pulling the whole repository.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
