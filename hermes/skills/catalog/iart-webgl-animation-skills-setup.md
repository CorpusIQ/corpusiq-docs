---
title: "WebGL Animation Skills - Three.js and Shaders"
description: "iart-ai/webgl-animation-skills on skills.sh: 5.3K combined installs; Three.js, GLSL fragment shader and GPU particle skills for web 3D motion."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iart-webgl-animation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "webgl", "three.js", "glsl"]
---

# WebGL Animation Skills - Setup Guide

**Source:** [iart-ai/webgl-animation-skills](https://www.skills.sh/iart-ai/webgl-animation-skills) via skills.sh - 5.3K combined installs across 3 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 51 stars, MIT licence, last pushed 2026-06-22, three SKILL.md directories under skills/, with a Claude Code plugin manifest in .claude-plugin
**Category:** WebGL for agents: Three.js animation, GLSL fragment shaders and GPU particle systems with render troubleshooting
**Quality Tier:** 🟢 Verified - all three sampled skills pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE.

This is a three-skill pack for real-time 3D on the web, positioned deliberately off the 2D and Lottie path: shaders, Three.js scenes and particle systems. Each skill is a working guide rather than a prompt, opening with skeleton code the agent is expected to adapt, and each carries a `references/` file for the detail that would otherwise bloat the skill.

The split is by rendering layer. `shader-glsl` handles the fragment stage, one shader per pixel: gradients, noise and fbm, SDF shapes, domain warping, image transitions, and wiring a `ShaderMaterial` with uniforms. `threejs-animation` handles the scene: render loops, camera moves, GLTF `AnimationMixer` playback and crossfades, instancing, scroll-linked 3D, React Three Fiber and GPU disposal. `particle-system` handles the emergent layer: confetti, snow, smoke and sparks, flow fields and curl noise, connected-dot networks, and GPU `Points` shaders.

## Installation

The README's install line:

```bash
npx skills add iart-ai/webgl-animation-skills
```

Or as a Claude Code plugin marketplace:

```bash
/plugin marketplace add iart-ai/webgl-animation-skills
```

then `/plugin install webgl-animation-skills`. The manifest that makes the second route work lives at `.claude-plugin/marketplace.json` in the repository.

The README states the skills run in Claude Code, Cursor, Codex and 40 or more agents. It gives no per-agent flag syntax, so for anything other than Claude Code use the skills CLI and let it detect the harness.

The skills activate on request rather than on setup. The README lists the triggers as: asking for a fragment shader, a `ShaderMaterial` or a generative GPU background; animating a Three.js or R3F scene, blending GLTF clips, or chasing a WebGL memory leak; and asking for a particle, confetti, flow-field or constellation effect.

## What It Provides

All three indexed listings clear the 500-install threshold, and the install counts are close enough that the split is even rather than one dominant skill.

| Skill | Installs | Use For |
|---|---|---|
| shader-glsl | 1,798 | GLSL fragment shaders: gradients, noise and fbm, SDFs, domain warping, image transitions, Three.js ShaderMaterial uniforms, post-processing |
| particle-system | 1,746 | Particle motion: confetti, snow, smoke and sparks, flow fields, curl noise, connected-dot networks, GPU Points shaders, emitters with forces |
| threejs-animation | 1,735 | Three.js and R3F motion: scenes, camera moves, GLTF clip playback and crossfades, InstancedMesh, scroll-linked 3D, leak-free GPU disposal |

All three indexed listings clear the 500-install threshold and appear in the table above; there is no tail.

## Why This Matters for Hermes Agents

WebGL is the category where generated code most often looks right and performs wrong. An agent can produce a scene that renders and still burns a laptop battery, because the frame-rate dependent animation, the uncapped device pixel ratio and the geometry never disposed on unmount are all invisible in a screenshot.

The skills address that directly. The Three.js guide sets `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))` in its opening skeleton, advances rotation by delta time rather than per frame, and ships a `references/resource-disposal.md` file specifically for the leak. That is unusual detail for a prompt-sized skill, and it is the difference between a demo and something you can leave running.

Shaders are the opposite problem: an agent that has never written GLSL will invent syntax that a compiler rejects, or produce something that compiles and looks like mud. The shader skill opens with a working fragment skeleton, normalisation and aspect correction, and the Inigo Quilez cosine palette, which is the fastest route to a good-looking animated gradient.

Particles are where the performance budget actually breaks. The skill's own guidance is explicit: 2D canvas for hundreds, GPU `Points` for thousands. Handing an agent that rule before it writes a per-particle DOM loop is cheaper than discovering the frame drop after deploy.

The three skills also compose, which is the reason to install the pack rather than one file. A hero section is a Three.js scene, a shader background and a particle layer, and the boundaries between them (uniforms, disposal, frame budget) are exactly where a single general-purpose skill gives vague advice.

## Usage

| You say | What happens |
|---|---|
| "Animated aurora gradient background in WebGL" | shader-glsl writes the fragment shader with a cosine palette and wires it to Three.js as a ShaderMaterial |
| "Crossfade idle to walk on this GLTF model" | threejs-animation sets up the AnimationMixer, the clips and the crossfade timing in R3F or plain Three.js |
| "Confetti burst when this form submits" | particle-system integrates per-particle forces and runs the burst on the canvas path sized for hundreds |
| "Constellation background that stays fast with 2,000 dots" | particle-system uses the spatial-grid connected-dot approach and GPU points |
| "This scene leaks GPU memory on unmount" | threejs-animation walks the disposal checklist in references/resource-disposal.md |
| "Image transition with a glitch effect" | shader-glsl builds a transition shader with displacement or RGB split |
| "Camera should follow scroll on this page" | threejs-animation links the camera to scroll position with a lerped or damped follow |

## Verification

Review the three skills before installing. These paths returned HTTP 200 on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/iart-ai/webgl-animation-skills/main/skills/shader-glsl/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/iart-ai/webgl-animation-skills/main/skills/threejs-animation/SKILL.md | head -5
```

The first should open with `name: shader-glsl`, a description listing fragment shaders, gradients, transitions and ShaderMaterial wiring, and `version: 0.1.0`. The second should open with `name: threejs-animation`, a description naming GLTF clips, InstancedMesh, R3F and disposal, then the same version line.

Then confirm the install and the reference files:

```bash
ls .claude/skills/shader-glsl .claude/skills/particle-system .claude/skills/threejs-animation
ls .claude/skills/threejs-animation/references
```

Each skill directory in the repository holds a SKILL.md and a README.md; the check that matters is that the SKILL.md arrived. The last command should list `r3f-and-perf.md` and `resource-disposal.md`; the other two skills carry `glsl-cookbook.md` and `particle-recipes.md` respectively. If a directory is missing, re-run the README install:

```bash
npx skills add iart-ai/webgl-animation-skills
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shader-glsl | Pass | Pass | Pass |
| particle-system | Pass | Pass | Pass |
| threejs-animation | Pass | Pass | Pass |

These are markdown guides with no scripts, no installer and no dependency additions; the install surface is text your agent reads. The security-relevant risk is the usual one for instruction files: a skill that tells an agent to follow a guide is a skill an agent will follow, including the code snippets.

The code the skills recommend is what reaches your application. That means Three.js and R3F dependencies you add yourself, shaders compiled on the GPU, and a render loop that runs on your users' machines. Review the dispose and DPR guidance as production requirements rather than optimisations, since both are about what the page does to a real device.

The repository also ships a `scripts/` directory, which its README describes as a verify-loop toolkit the agent calls rather than hand-rolls: `seek-shot.sh` screenshots a page's frozen `?t=N` moments, `contact-sheet.sh` tiles frames side by side, and `probe-mp4.sh` reads back an encoded file's resolution, codec, fps and duration. Those are local shell scripts operating on output your machine already produced, so review them as you would any script in a repository you are about to let an agent run.

## Limitations

- Snapshot data, verified 2026-11-06: 5,279 combined installs across 3 indexed listings; 51 GitHub stars; MIT; last pushed 2026-06-22. Counts drift over time.
- Small repository, three skills, one publisher (iart-ai). The install counts are healthy, but the star count is modest and the only third-party signal in this snapshot is the set of skills.sh verdicts above.
- The skills are version 0.1.0. Treat them as an early surface: APIs they document (Three.js, R3F and the WebGL extensions they use) move, and no commit after 2026-06-22 has adjusted for that.
- This pack is one of a 14-repository collection from the same publisher, and each pack installs separately. Installing this one does not bring in the 2D, Lottie, or video packs.
- Nothing here renders or tests output. The guidance is about writing code that performs; whether the result looks right is still a human review, and the repository demonstrates its output with a showcase GIF and the verify scripts rather than a test suite.
- The skills assume a Three.js or R3F project already exists or that you want one created. They are not a framework and do not scaffold an application.

## Related

- [IART Web Animation Skills - GSAP and SVG Suite](/hermes/skills/catalog/iart-web-animation-skills-setup)
- [Three.js Game Skills - 3D Game Development Suite Setup](/hermes/skills/catalog/threejs-game-skills-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the layer, not the effect. "Write a fragment shader for this" routes to shader-glsl, "make these particles swirl" routes to particle-system, and a request for "a cool 3D background" makes the agent guess.
- Read `references/resource-disposal.md` before shipping anything that mounts and unmounts. Geometry, material and texture disposal is the failure that only shows up after navigation, in production.
- Cap the pixel ratio in every scene. The skills do it in their skeletons because retina displays otherwise render four times the pixels for no visible gain.
- Pair a shader with a scene rather than nesting them. Uniform updates belong in the render loop, and an agent that inlines shader code into a component usually gets the update order wrong.
- Use the example prompts from the README as activation tests. If "build a connected-dot constellation background that stays fast with 2000 particles" does not pull in particle-system, the install did not land where the harness reads it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
