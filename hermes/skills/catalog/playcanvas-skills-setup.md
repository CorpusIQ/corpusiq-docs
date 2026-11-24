---
title: "PlayCanvas Skills - 3D Web Engine Setup"
description: "playcanvas/skills - 6.5K combined installs: 18 skills for PlayCanvas web engine app building, GLB workflow and rendering."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/playcanvas-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "playcanvas", "webgl", "game engine"]
---

# PlayCanvas Skills - 3D Web Engine Setup

**Source:** [playcanvas/skills](https://www.skills.sh/playcanvas/skills) via skills.sh - 6.5K combined installs across 18 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [playcanvas/skills](https://github.com/playcanvas/skills) - 43 stars, MIT, main branch, last pushed Nov 18, 2026; one SKILL.md per skill under plugins/playcanvas/skills/, with marketplace manifests for Claude Code, Cursor and Codex alongside.
**Category:** 3D Web Development and Game Engines
**Quality Tier:** 🟡 Yellow - inspect-glb carries one Warn cell (Snyk); the other 17 sampled skills pass all three checks.

PlayCanvas Skills is the official collection from the PlayCanvas team for coding agents working against the PlayCanvas web engine. The 18 skills install through the Agent Skills installer and also ship as native plugins for Claude Code, Codex and Cursor, so the same skill files reach every supported agent. Each skill owns one stage of a PlayCanvas app: GLB inspection, scene assembly, lighting, effects, animation, build structure, draw-call reduction and pixel-level verification.

The collection is deliberately portable. The skills read the project to resolve whether the active surface is the direct Engine API, @playcanvas/react or @playcanvas/web-components, then load only the reference that matches, which keeps startup context at roughly 700 tokens for the whole set. The repo ships Markdown, JSON and images only, with no scripts, hooks or MCP servers, so installation carries no runtime to audit.

## Installation

Add the skills with the Agent Skills installer:

```bash
npx skills add playcanvas/skills
```

Use --all to install every skill into all detected agents, or -g for a user-level install. Start a new conversation after installing so the agent discovers the new skill metadata.

For a native plugin install instead of Agent Skills, add this repository as a marketplace:

```bash
claude plugin marketplace add playcanvas/skills
claude plugin install playcanvas@playcanvas
```

```bash
codex plugin marketplace add playcanvas/skills
codex plugin add playcanvas@playcanvas
```

For Cursor, load the plugin from a checkout with cursor-agent --plugin-dir plugins/playcanvas, or link plugins/playcanvas into ~/.cursor/plugins/local/playcanvas for a persistent install.

Choose one route per agent: installing both Agent Skills and a native plugin, or the Claude plugin from two marketplaces, exposes duplicate skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| inspect-glb | 427 | reading GLB clips, joints, hierarchy and compression before loading a model |
| build-app | 420 | structuring a Direct Engine, React or Web Components application |
| apply-conventions | 418 | applying Engine conventions for transforms, cameras, lights and materials |
| find-examples | 417 | finding and adapting the official example that matches the installed version |
| light-scene | 416 | lighting, environment, shadows, tone mapping and post-processing |
| assemble-scene | 416 | composing entity hierarchies from models, colliders, rigid bodies and scripts |
| configure-animation | 415 | clip playback, blending, state graphs and retargeting |
| add-effects | 415 | choosing particles, shader chunks, runtime meshes or post-processing |
| calibrate-model | 414 | recording scale, grounding and pivot offsets for repeated models |
| reuse-scripts | 413 | reusing the scripts and helpers the installed Engine already ships |
| reduce-draw-calls | 391 | cutting draw calls with lifecycle, batching and instancing |
| verify-pixels | 390 | proving a rendering change is pixel-identical or bounded |
| override-shader-chunks | 386 | custom StandardMaterial shading through chunk overrides |
| bake-lighting | 386 | baking static lighting, shadows and ambient occlusion into lightmaps |
| load-assets | 243 | loading glTF models and textures with Draco and Basis/KTX2 compression |
| inspect-runtime | 243 | reading live app state through the Engine devtools hook |
| manage-game-state | 170 | managing game state |
| build-hud | 170 | building a heads-up display |

All 18 indexed listings clear the 150-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

An agent that writes PlayCanvas code from general knowledge tends to reach for legacy APIs, guess model scale and orientation, and ship a page that renders nothing or renders at the wrong speed. This collection closes those gaps with a sequence that mirrors how a senior engine programmer works: inspect the GLB before placing it, calibrate its scale once, assemble the scene with one semantic root per object, then verify the result in the running app instead of trusting a clean build.

The surface detection is the highest-leverage part. The same skills serve three different authoring surfaces, direct Engine, React and Web Components, and they resolve which one a project uses from imports and markup before loading any reference. For an operator running a product site, inspect-glb and load-assets decide whether a model blocks the main thread while it decodes, and verify-pixels provides the regression evidence that most 3D teams skip.

The collection ends every workflow with evidence: reduce-draw-calls for CPU-bound scenes, bake-lighting for static cost, and verify-pixels for the no-visual-change guarantee. Two listings, manage-game-state and build-hud, carry install counts but no SKILL.md in the current tree, so treat those two as index-only entries.

## Usage

| You say | What happens |
|---|---|
| Build a product viewer for these GLB files | Uses inspect-glb, calibrate-model and assemble-scene in order |
| The scene renders but runs slow | Uses reduce-draw-calls to measure and cut draw calls |
| Add bloom without washing out the scene | Uses add-effects to pick the right post-processing route |
| The model loads at the wrong size | Uses calibrate-model for scale and grounding offsets |
| Make the animation play and blend correctly | Uses configure-animation for clips, blending and state |
| Prove my shader change changed nothing | Uses verify-pixels for a deterministic capture comparison |
| Bake the static shadows to save frame time | Uses bake-lighting to precompute lighting into lightmaps |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/playcanvas/skills/main/README.md | head -40
```

Confirm the GLB inspection skill body is present before model work:

```bash
curl -sL https://raw.githubusercontent.com/playcanvas/skills/main/plugins/playcanvas/skills/inspect-glb/SKILL.md | head -30
```

Confirm the app structure skill body is present before building:

```bash
curl -sL https://raw.githubusercontent.com/playcanvas/skills/main/plugins/playcanvas/skills/build-app/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| inspect-glb | Pass | Pass | Warn |
| build-app | Pass | Pass | Pass |
| apply-conventions | Pass | Pass | Pass |
| find-examples | Pass | Pass | Pass |
| light-scene | Pass | Pass | Pass |
| assemble-scene | Pass | Pass | Pass |
| configure-animation | Pass | Pass | Pass |
| add-effects | Pass | Pass | Pass |
| calibrate-model | Pass | Pass | Pass |
| reuse-scripts | Pass | Pass | Pass |
| reduce-draw-calls | Pass | Pass | Pass |
| verify-pixels | Pass | Pass | Pass |
| override-shader-chunks | Pass | Pass | Pass |
| bake-lighting | Pass | Pass | Pass |
| load-assets | Pass | Pass | Pass |
| inspect-runtime | Pass | Pass | Pass |
| manage-game-state | Pass | Pass | Pass |
| build-hud | Pass | Pass | Pass |

The single Warn cell sits on inspect-glb (Snyk). Every other sampled skill passes Gen Agent Trust Hub, Socket and Snyk.

## Limitations

- Snapshot data, verified Nov 23, 2026: 6,550 combined installs across 18 indexed listings; 43 GitHub stars; MIT licence; last pushed Nov 18, 2026. Counts drift over time.
- Two listings, manage-game-state and build-hud, carry install counts but have no SKILL.md in the current tree and no in-repo description, so their Use For cells stay at name level.
- The skills target Engine application workflows and do not automate the PlayCanvas Editor, create or publish Editor projects, or manage cloud services.
- A few skills run commands on the local machine: inspect-glb reads GLB JSON with Node, inspect-runtime injects a devtools hook snippet, and find-examples reads official examples via gh api when they are not installed locally.
- The plugin ships Markdown, JSON and images only, but it collects and sends no user data, which the README states explicitly.
- Installing both Agent Skills and a native plugin for the same agent exposes duplicate skills, so pick one route.

## Related

- [Three.js Skills - 3D Graphics Toolkit for Agents](/hermes/skills/catalog/threejs-skills-setup)
- [Three.js Skills (Cesartevisual) - 3D Web Suite Setup](/hermes/skills/catalog/threejs-cesartevisual-setup)
- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time when fixing a specific bug; inspect-glb plus calibrate-model covers most model-placement incidents without the full set.
- Ask for the GLB inspection before any placement code, so scale, grounding and compression are decided before geometry is written.
- Keep verify-pixels next to every shader or lighting change: it is the only reliable way to prove a rendering edit changed nothing.
- For @playcanvas/react or web-components projects, let the skills resolve the surface from imports rather than forcing the direct Engine path.
- If a skill name appears twice after install, you have both Agent Skills and a native plugin for one agent; remove one route.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
