---
title: "R3F Skills - React Three Fiber for Agents"
description: "enzed/r3f-skills: 23.5K installs across 11 listings; focused React Three Fiber guidance from fundamentals to physics, shaders and postprocessing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/r3f-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "react three fiber", "threejs", "webgl"]
---

# R3F Skills - Setup Guide

**Source:** [enzed/r3f-skills](https://www.skills.sh/enzed/r3f-skills) via skills.sh - 23.5K combined installs across 11 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 133 stars, no LICENSE file (the README License section states MIT), last pushed 2026-08-31, 11 directories at skills/<name>/SKILL.md
**Category:** 3D on the web for agents: React Three Fiber scenes, materials, lighting, physics and performance budgets
**Quality Tier:** 🟡 Yellow: no LICENSE file at the repo root even though the README states MIT, and the guidance is pinned to a dependency review from 2026-08-31

This is a narrow, deliberate pack: eleven skills, one per concern in a React Three Fiber scene, from canvas setup and typed JSX through geometry, materials, lighting, textures, loaders, animation, shaders, postprocessing, interaction and Rapier physics. There is no router skill and no catch-all, so the agent picks a single file per problem.

Each skill keeps three things in `SKILL.md`: the decisions that change the output, the pitfalls that break it, and one checked example. Longer optional recipes sit in that skill's `references/` directory and are meant to be loaded only when relevant, which keeps the entry files small.

## Installation

The README documents one install command:

```bash
npx skills add EnzeD/r3f-skills
```

The skills CLI lets you choose skills and target agents, so a single concern can be installed on its own. For a manual install, the README says to copy the individual skill folders into your agent's skills directory, including their `references/` subfolders:

```bash
git clone https://github.com/enzed/r3f-skills && cp -R r3f-skills/skills/r3f-fundamentals ~/.claude/skills/
```

Repository development dependencies are explicitly not needed to use the skills; they matter only if you want to run the repo's own validation suite.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| r3f-interaction | 3,363 | Pointer events, dragging, picking and controls |
| r3f-fundamentals | 2,232 | Canvas, typed JSX, hooks, renderer choice and ownership |
| r3f-animation | 2,140 | Delta-based motion, demand rendering and clip playback |
| r3f-postprocessing | 2,055 | Composer, selective bloom, depth and output color |
| r3f-materials | 2,035 | PBR, transparency, transmission and material cost |
| r3f-geometry | 2,032 | Geometry, buffers, instancing, points and lines |
| r3f-shaders | 2,029 | GLSL, uniforms, deformation and optional TSL |
| r3f-lighting | 1,974 | Direct lights, environments and shadows |
| r3f-physics | 1,905 | Rapier bodies, colliders, simulation steps and joints |
| r3f-loaders | 1,895 | Assets, Suspense, decoders, caching and clones |
| r3f-textures | 1,819 | Color spaces, UVs, sampling and render targets |

No indexed listings fall below the threshold; all 11 listings appear above.

## Why This Matters for Hermes Agents

React Three Fiber guidance rots quickly. Fiber 8 and Fiber 9 have different APIs, drei and three move on their own cadence, and a model trained on older material will confidently write code that no longer mounts. This pack is written against a stated version set and tells the agent to inspect the consuming project's versions before choosing an API.

The compatibility table is the useful part for a Hermes agent: React 19.2.8, `@react-three/fiber` 9.7.0, `@react-three/drei` 10.7.8, `three` 0.185.1 (r185), `@react-three/rapier` 2.2.0, `@react-three/postprocessing` 3.1.1 and `postprocessing` 6.39.4, reviewed 2026-08-31. That gives the agent a baseline to diff your `package.json` against instead of guessing.

The one-skill-per-concern layout also fits how agents work. A lighting question loads r3f-lighting, not a 2000-line framework guide, and the expensive optional recipes stay in references until they are needed.

The boundaries are stated rather than implied. Fiber 8 with React 18 is treated as a separate legacy pairing that the fixtures do not test, Fiber 10 alpha APIs are excluded, and the WebGPU and TSL material is optional and not covered by the browser smoke suite.

## Usage

| You say | What happens |
|---|---|
| "set up a Canvas with typed JSX" | r3f-fundamentals covers renderer choice, hooks and ownership rules |
| "lights are washing out the materials" | r3f-lighting works through direct lights, environments and shadows |
| "the glass material looks flat" | r3f-materials covers PBR, transparency, transmission and material cost |
| "1000 boxes are killing the frame rate" | r3f-geometry moves the scene to instancing and buffer reuse |
| "the model pops in and out" | r3f-loaders covers Suspense boundaries, decoders, caching and clones |
| "my raycaster picks the wrong mesh" | r3f-interaction covers pointer events, dragging and picking |
| "the bloom is blowing out the whole scene" | r3f-postprocessing covers composer passes and selective bloom |
| "the character should fall onto the floor" | r3f-physics covers Rapier bodies, colliders and simulation steps |

## Verification

Fetch one raw skill file to confirm the tree matches what skills.sh indexed. The path is skills/r3f-fundamentals/SKILL.md on branch main, and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/enzed/r3f-skills/main/skills/r3f-fundamentals/SKILL.md | head -30
```

A response with frontmatter and a "decisions, pitfalls, one example" structure confirms the file is live. Then compare the pinned versions against your own project before the agent writes code:

```bash
npm ls three @react-three/fiber @react-three/drei --depth=0
```

If your numbers differ from the fixture table in the README, say so in the prompt so the agent works from your versions rather than the pinned ones.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| r3f-interaction | Pass | Pass | Pass |
| r3f-animation | Pass | Pass | Pass |
| r3f-geometry | Pass | Pass | Pass |
| r3f-physics | Pass | Pass | Pass |
| r3f-textures | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 4, 2026: 23,479 combined installs across 11 indexed listings; 133 GitHub stars; no LICENSE file; last pushed 2026-08-31. Counts drift over time.
- No LICENSE file exists at the repo root, while the README License section states MIT. Treat the terms as unresolved until the file appears.
- Last pushed 2026-08-31, the oldest snapshot in this batch, so treat API guidance as version-pinned rather than current. Re-check the compatibility table before relying on it.
- The fixtures do not test Fiber 8 with React 18, and Fiber 10 alpha APIs are excluded, so the skills are not a reference for either stack.
- WebGPU and TSL recipes are optional and type-checked only; the browser smoke suite targets WebGL and does not certify WebGPU.
- The repo has no GitHub description, so the skills.sh listing is the main external metadata source for the pack.

## Related

- [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup)
- [Three.js Game Skills - 3D Game Development Suite Setup](/hermes/skills/catalog/threejs-game-skills-setup)
- [Three Agent Bridge Setup](/hermes/skills/catalog/three-agent-bridge-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- State your Fiber, three and drei versions in the prompt. The skills tell the agent to check, but naming them saves a round trip and removes the guess.
- Install only the concerns you need when working on an existing scene; each skill is independently installable and the references folder is where the weight sits.
- Load references deliberately. The entry file is three sections; the recipes behind it are long and only pay off for the specific problem they cover.
- Ask for the checked example first, then adapt it. The examples are the part that gets validated against the fixture versions.
- Read the pitfalls section before debugging. Most R3F failures in generated code trace back to a listed pitfall rather than a novel bug.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
