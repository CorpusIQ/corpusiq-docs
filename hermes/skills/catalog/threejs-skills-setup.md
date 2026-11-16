---
title: "Three.js Skills - 3D Graphics Toolkit for Agents"
description: "full-stack-skills/threejs-skills - 9.2K combined installs across 22 indexed listings: 18 Three.js skills for scenes, camera, lights and materials."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/threejs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "threejs", "webgl", "3d"]
---

# Three.js Skills - Setup Guide

**Source:** [full-stack-skills/threejs-skills](https://www.skills.sh/full-stack-skills/threejs-skills) via skills.sh - 9.2K combined installs across 22 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 12 stars, Apache-2.0 license, `main` branch, last pushed 2026-10-03, `SKILL.md` files under `skills/<name>/SKILL.md`
**Category:** 3D graphics - Three.js scenes, materials, rendering and animation
**Quality Tier:** 🟢 Green - all 12 sampled skills pass the Gen Agent Trust Hub, Socket and Snyk.

Three.js Skills is a curated collection of agent skills for building 3D web applications, part of the Full Stack Skills ecosystem maintained by PartMe.AI. The repository documents 18 Three.js skills, each a self-contained SKILL.md that an agent loads on demand to recall API surface, workflow and reference material instead of hallucinating three.js calls.

Skills are organized by subsystem, scenes, camera, lights, materials, geometries, animation, renderers, loaders, texturing and post-processing, and they cross-reference each other so an agent is pointed to the right skill for the task. The same repository also ships four OpenSpec workflow skills under `.agents/skills/` for spec-driven change management.

## Installation

```bash
# install all skills
npx skills add full-stack-skills/threejs-skills

# or install a specific skill
npx skills add full-stack-skills/threejs-skills --skill <skill-name>
```

Manual install for Claude Code:

```bash
git clone https://github.com/full-stack-skills/threejs-skills.git
cp -r threejs-skills/skills/* .claude/skills/
```

Skills are compatible with Claude Code, Codex, Cursor, OpenCode, Gemini CLI, GitHub Copilot, Windsurf and 70+ other agents.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| threejs-animation | 500 | Keyframe animation with AnimationMixer, clips and actions; mixing, crossfading, loop modes and procedural rigs. |
| threejs-materials | 494 | Classic materials from MeshStandard to ShaderMaterial; PBR maps, transparency, depth and GLSL. |
| threejs-camera | 487 | Perspective, orthographic, cube, array and stereo cameras; projection matrices, FOV and environment maps. |
| threejs-scenes | 485 | Scene root, fog and background configuration for the world container. |
| threejs-renderers | 485 | WebGLRenderer and WebGPURenderer, canvas sizing, tone mapping, color space and render targets. |
| threejs-lights | 484 | Ambient, hemisphere, directional, point, spot and area lights plus shadows, probes and IES. |
| threejs-postprocessing | 473 | EffectComposer and stock passes such as UnrealBloom, SSAO, SSR, Bokeh and Outline. |
| threejs-loaders | 471 | Asset I/O via LoadingManager, GLTFLoader with Draco and KTX2, plus exporters. |
| threejs-geometries | 471 | BufferGeometry, typed attributes, instancing, primitives and addon geometries such as Text and Decal. |
| threejs-controls | 468 | Orbit, Fly, FirstPerson, Trackball, Drag, PointerLock and Transform controls for navigation and gizmos. |
| threejs-textures | 466 | GPU texture objects, sampling, mipmaps, anisotropy and PMREM environment prefiltering. |
| threejs-objects | 466 | Object3D hierarchy, Mesh, SkinnedMesh, LOD, Points, Sprite, Raycaster and Layers masks. |
| threejs-dev-setup | 459 | Project scaffolding with npm, Vite/Webpack, import maps and TypeScript, plus addon import path fixes. |

The remaining 9 indexed listings range from 195 to 448 installs.

## Why This Matters for Hermes Agents

Three.js has a large, versioned API, and an agent working from memory mixes up class names, addon import paths and WebGL versus WebGPU idioms. Each skill here is a self-contained reference for one subsystem, holding the exact classes, parameters and cross-references, so the agent recalls the real API instead of inventing it.

The cross-referencing is the key design: materials points to node-tsl for shader graphs, loaders points to textures for runtime parameters, and renderers points to postprocessing for composer chains. That routing keeps an agent on the correct path when a task spans several subsystems.

dev-setup is the most practical entry point, covering npm, Vite/Webpack, import maps and the common module-not-found failures, which is where most three.js agent work first goes wrong.

For a Hermes agent the value is a stable, vendor-maintained knowledge base for a fast-moving library, plus OpenSpec workflow skills for turning feature work into proposals and archived changes.

## Usage

| You say | What happens |
|---|---|
| "Add bloom and SSAO to my scene" | threejs-postprocessing recalls the EffectComposer chain and the UnrealBloom and SSAO passes. |
| "Load a GLB model with Draco compression" | threejs-loaders provides GLTFLoader with DRACOLoader and KTX2Loader setup. |
| "Set up a WebGPU renderer with the right tone mapping" | threejs-renderers covers WebGPURenderer, color space and tone mapping configuration. |
| "Give the camera orbit controls with damping" | threejs-controls recalls OrbitControls, damping and animation-loop integration. |
| "Create a procedural terrain from a plane geometry" | threejs-geometries covers BufferGeometry, attributes and instancing. |
| "Scaffold a new three.js project with Vite and TypeScript" | threejs-dev-setup provides the bundler and import-map guidance. |
| "Fix a module-not-found for OrbitControls" | threejs-dev-setup points to the correct three/addons/ import path. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/full-stack-skills/threejs-skills/main/skills/threejs-scenes/SKILL.md | head -20
npx skills add full-stack-skills/threejs-skills
```

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| threejs-animation | Pass | Pass | Pass |
| threejs-materials | Pass | Pass | Pass |
| threejs-camera | Pass | Pass | Pass |
| threejs-scenes | Pass | Pass | Pass |
| threejs-renderers | Pass | Pass | Pass |
| threejs-lights | Pass | Pass | Pass |
| threejs-postprocessing | Pass | Pass | Pass |
| threejs-loaders | Pass | Pass | Pass |
| threejs-geometries | Pass | Pass | Pass |
| threejs-controls | Pass | Pass | Pass |
| threejs-textures | Pass | Pass | Pass |
| threejs-objects | Pass | Pass | Pass |

All 12 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 9,207 combined installs across 22 indexed listings; 12 GitHub stars; Apache-2.0; last pushed 2026-10-03. Counts drift over time.
- The README documents 18 Three.js skills, while skills.sh indexes 22 listings; the four openspec-* skills (openspec-propose, openspec-explore, openspec-archive-change, openspec-apply-change) are OpenSpec workflow skills shipped alongside the Three.js set under `.agents/skills/`.
- Five README-listed skills (threejs-math, threejs-helpers, threejs-webxr, threejs-node-tsl, threejs-audio) sit under 450 installs and are summarized in the table tail rather than described in detail.
- The repository has 12 GitHub stars at snapshot, so it carries less community vetting than larger suites.
- Documentation is available in English and simplified Chinese (README.zh-CN.md); the primary reference is the English README.

## Related

- [Three.js Agent Skills](/hermes/skills/catalog/threejs-agent-skills-setup)
- [Three.js Game Skills](/hermes/skills/catalog/threejs-game-skills-setup)
- [WebGL Animation Skills](/hermes/skills/catalog/iart-webgl-animation-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install specific skills with `--skill <name>` when you only need a few subsystems; the full pack is 18 skills.
- Let the cross-references route you: when a task spans subsystems, follow the "see threejs-X" pointers in each SKILL.md.
- For shader-graph work pick threejs-node-tsl, and for classic GLSL use threejs-materials; do not mix both for the same authoring path.
- Keep the agent's three.js version aligned with the docs referenced by dev-setup to avoid stale import paths.
- Use the openspec-* skills for spec-driven change management when the Three.js work needs formal proposals and archives.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
