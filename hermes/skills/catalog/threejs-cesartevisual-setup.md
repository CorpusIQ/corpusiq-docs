---
title: "Three.js Skills (Cesartevisual) - 3D Web Suite Setup"
description: "cesartevisual/threejs-skills - 18.6K combined installs: 24 Three.js skills for scenes, shaders, R3F, WebGPU, physics and 3D delivery."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/threejs-cesartevisual-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "three.js", "webgl", "3d web"]
---

# Three.js Skills (Cesartevisual) - 3D Web Suite Setup

**Source:** [cesartevisual/threejs-skills](https://www.skills.sh/cesartevisual/threejs-skills) via skills.sh - 18.6K combined installs across 24 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [cesartevisual/threejs-skills](https://github.com/cesartevisual/threejs-skills) - 28 stars, MIT, main branch, last pushed Sep 10, 2026; one SKILL.md per skill under skills/, with reference files kept alongside each skill.
**Category:** 3D Web Development and WebGL
**Quality Tier:** 🟢 Green - every one of the 20 sampled skills passes Gen Agent Trust Hub, Socket and Snyk with no Warn or Fail cells.

Three.js Skills is a community-maintained collection that gives a coding agent working 3D knowledge for the browser. The collection is independent of the Three.js maintainers and uses the Agent Skills format, so the files install into Claude Code, Cursor, Codex and other supported agents. Each of its 24 skills owns one part of the work an agent needs to finish a 3D feature: scene hierarchy, lighting, materials, shaders, animation, physics, asset loading, interaction, testing and delivery.

The shape of the collection is the useful part. A single umbrella skill plans a complete 3D web experience, and 23 focused skills each cover one failure mode that an agent working from general knowledge tends to get wrong, such as a black canvas, a flickering material after a colour-space change, a shadow map that is tuned for the wrong scene scale, or a glTF model that blocks the main thread while it decodes.

## Installation

Install the whole collection in your web project:

```bash
npx skills add cesartevisual/threejs-skills
```

Choose the skills and the agent when prompted. To target an agent or one skill directly:

```bash
npx skills add cesartevisual/threejs-skills --agent claude-code
npx skills add cesartevisual/threejs-skills --skill threejs-r3f
npx skills add cesartevisual/threejs-skills --global
```

Clone and install from a sibling directory:

```bash
git clone https://github.com/cesartevisual/threejs-skills.git ../threejs-skills
npx skills add ../threejs-skills
```

Without the CLI, copy folders from skills/ into the project skill directory and keep each SKILL.md with the references it links. Claude Code reads .claude/skills/, Cursor reads .cursor/skills/ or .agents/skills/, and Codex reads .agents/skills/.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| threejs-r3f | 956 | building or fixing React Three Fiber scenes, Drei helpers and Suspense loading |
| threejs-performance | 956 | profiling frame time, GPU load, asset memory and resource leaks |
| threejs-web | 899 | planning a full 3D web experience or picking focused skills for one |
| threejs-animation | 880 | animation clips, skeletal motion, transitions and scroll timelines |
| threejs-lighting | 810 | environment maps, direct lights, baked light and tuned shadows |
| threejs-shaders | 802 | GLSL shaders, custom material effects, uniforms and deformation |
| threejs-assets | 800 | loading, validating, compressing and caching glTF models and textures |
| threejs-testing | 799 | browser checks, visual fixtures, lifecycle tests and device evidence |
| threejs-interaction | 795 | pointer picking, orbit controls, dragging and selection |
| threejs-scene | 782 | scene hierarchy, camera framing, coordinate transforms and renderer lifecycles |
| threejs-materials | 781 | PBR materials, texture mapping, transparency and colour-management fixes |
| threejs-debugging | 768 | black canvases, missing meshes, wrong colours, flicker, picking bugs and context loss |
| threejs-particles | 762 | particle systems, point clouds and large repeated datasets |
| threejs-postprocessing | 758 | bloom, antialiasing, ambient occlusion and render-target composition |
| threejs-accessibility | 749 | keyboard use, assistive technology, reduced motion and non-3D fallbacks |
| threejs-geometry | 747 | BufferGeometry, procedural meshes, instancing and geometry attributes |
| threejs-product-viewer | 727 | product viewers with material variants, hotspots and image export |
| threejs-physics | 713 | Rapier or another physics engine, colliders and fixed timesteps |
| threejs-html | 699 | responsive HTML and framework integration, scroll sections and overlays |
| threejs-spatial-data | 690 | BIM, IFC, GIS, CAD, measurement and large-coordinate datasets |
| threejs-webgpu | 683 | rendering through the WebGPU backend instead of WebGL |
| threejs-deployment | 683 | shipping a 3D site, including asset hosting and load strategy |
| threejs-audio | 683 | positional and scene-driven audio inside a 3D experience |
| threejs-xr | 675 | immersive and XR presentation modes |

All 24 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

An agent asked to build a 3D web page starts from partial knowledge and produces a scene that renders nothing, a camera pointed at empty space, or a model that loads after the user has scrolled past it. The collection closes exactly those gaps. threejs-debugging is the highest-leverage file for a builder because a black canvas, a flickering surface and a mesh that never appears are the three symptoms that consume the most time and give the weakest error messages. threejs-scene and threejs-lighting decide whether the first render works at all, and the shader, postprocessing and physics skills cover the parts where a single wrong uniform or an uncontrolled timestep produces motion that runs at different speeds on different machines.

The suite is also organized the way an agent reads work in stages: plan with threejs-web, build with the scene, lighting, material and geometry skills, test with threejs-testing, and ship with threejs-deployment. For an operator running a product site, threejs-product-viewer and threejs-performance decide whether a 3D product page helps conversion or just adds three seconds of load time, and threejs-accessibility answers the question that most 3D projects skip until an audit: what does this page do when the visitor cannot use a pointer or has reduced motion enabled.

## Usage

| You say | What happens |
|---|---|
| Build a 3D hero section for our landing page | Uses threejs-web to plan the scene, then scene, lighting and performance skills |
| My canvas is black and there are no errors | Uses threejs-debugging to walk the likely causes in order |
| The model loads but the page freezes | Uses threejs-assets to move decoding and release work off the critical path |
| Make the product spin only when it is hovered | Uses threejs-interaction with orbit and picking guidance |
| Add bloom without washing out the scene | Uses threejs-postprocessing to compose render targets correctly |
| The scene runs at different speeds on two laptops | Uses threejs-animation and threejs-physics for frame-independent motion and fixed timesteps |
| Can we show this in a headset | Uses threejs-xr and threejs-webgpu to plan the immersive path |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/cesartevisual/threejs-skills/main/README.md | head -40
```

Confirm the React Three Fiber skill body is present before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/cesartevisual/threejs-skills/main/skills/threejs-r3f/SKILL.md | head -30
```

Confirm the performance skill body is present before profiling work:

```bash
curl -sL https://raw.githubusercontent.com/cesartevisual/threejs-skills/main/skills/threejs-performance/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| threejs-r3f | Pass | Pass | Pass |
| threejs-performance | Pass | Pass | Pass |
| threejs-web | Pass | Pass | Pass |
| threejs-animation | Pass | Pass | Pass |
| threejs-lighting | Pass | Pass | Pass |
| threejs-shaders | Pass | Pass | Pass |
| threejs-assets | Pass | Pass | Pass |
| threejs-testing | Pass | Pass | Pass |
| threejs-interaction | Pass | Pass | Pass |
| threejs-scene | Pass | Pass | Pass |
| threejs-materials | Pass | Pass | Pass |
| threejs-debugging | Pass | Pass | Pass |
| threejs-particles | Pass | Pass | Pass |
| threejs-postprocessing | Pass | Pass | Pass |
| threejs-accessibility | Pass | Pass | Pass |
| threejs-geometry | Pass | Pass | Pass |
| threejs-product-viewer | Pass | Pass | Pass |
| threejs-physics | Pass | Pass | Pass |
| threejs-html | Pass | Pass | Pass |
| threejs-spatial-data | Pass | Pass | Pass |

The four listings outside the sample, threejs-webgpu, threejs-deployment, threejs-audio and threejs-xr, carry no verdict cells in this sample, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 18,597 combined installs across 24 indexed listings; 28 GitHub stars; MIT licence; last pushed Sep 10, 2026. Counts drift over time.
- The collection is independent of the Three.js maintainers and is not an official package; the README states this plainly.
- The install band is narrow by design: every skill sits between 675 and 956 installs, because the collection is installed as a set and no single file dominates usage.
- Four of the 24 listings were outside the verdict sample and carry no security cells in this guide.
- Separately, skill names in the tree are plain directory names under skills/, so an agent that guesses a path outside that layout will read nothing.

## Related

- [Three.js Skills - 3D Graphics Toolkit for Agents](/hermes/skills/catalog/threejs-skills-setup)
- [R3F Skills - React Three Fiber for Agents](/hermes/skills/catalog/r3f-skills-setup)
- [Blender Skills - MCP Production Pipeline](/hermes/skills/catalog/blender-skills-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time when you are fixing a specific bug; threejs-debugging plus threejs-performance covers most production incidents without loading the full set.
- Ask for the scene plan before the code. threejs-web forces the camera, scale and asset budget decision before any geometry is written.
- Keep threejs-testing next to threejs-animation: deterministic visual fixtures are the only reliable way to catch a regression in motion.
- Check colour management before blaming lighting when materials look washed out; the materials skill names the colour-space settings that usually cause it.
- If a page must work without JavaScript-driven 3D, pair this collection with the accessibility skill and decide the fallback before the first mockup.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
