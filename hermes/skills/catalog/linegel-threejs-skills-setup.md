---
title: "Linegel Three.js Skills - WebGPU/TSL Suite Setup"
description: "linegel/threejs-complete-set-of-skill - 4.8K combined installs: Three.js WebGPU/TSL skills for procedural scenes, effects and visual validation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linegel-threejs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "three.js", "webgpu", "3d graphics"]
---

# Linegel Three.js Skills - Setup Guide

**Source:** [linegel/threejs-complete-set-of-skill](https://www.skills.sh/linegel/threejs-complete-set-of-skill) via skills.sh - 4.8K combined installs across 29 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [linegel/threejs-complete-set-of-skill](https://github.com/linegel/threejs-complete-set-of-skill) - 14 stars, ISC license, last pushed Sep 24, 2026, main branch; 27 installable skill directories under skills/<name>/SKILL.md plus a separate product-from-scratch skill under .claude/skills/ and experimental threejs-physics-integration notes.
**Category:** 3D Graphics (Three.js WebGPU/TSL)
**Quality Tier:** 🟡 Yellow - all 15 sampled skills pass the Gen Agent Trust Hub and Socket checks; two carry a Warn cell on Snyk and none carries a Fail.

linegel/threejs-complete-set-of-skill publishes installable agent skills for Three.js r185 WebGPU and TSL (Three Shading Language) work. The 27 installable skills cover procedural graphics (geometry, materials, buildings, vegetation, planets), rendering systems (cameras, shadows, bloom, exposure, image pipelines), motion and effects (particles, dynamic surfaces, space effects), and falsifiable visual validation. Every skill is model-invoked: its description names the real invocation branches, common decisions live in SKILL.md, and branch-only equations and API rules load through explicit context pointers.

The skills.sh index lists 29 listings at 4.8K combined installs. Two listings sit outside the installable set: product-from-scratch (144 installs) is a separate Claude skill under .claude/skills/, and threejs-physics-integration (2 installs) is experimental notes the README marks as not an installable skill. Full demos, labs, review material, and generated media under the top-level threejs-* directories stay repository-only.

## Installation

List the available skills, install all of them, or select one:

```bash
npx skills@latest add linegel/threejs-complete-set-of-skill --list
npx skills@latest add linegel/threejs-complete-set-of-skill --skill '*'
npx skills@latest add linegel/threejs-complete-set-of-skill --skill threejs-spectral-ocean
```

For a specific agent in non-interactive setup:

```bash
npx skills@latest add linegel/threejs-complete-set-of-skill --skill '*' -g -a codex -y
npx skills@latest add linegel/threejs-complete-set-of-skill --skill '*' -g -a claude-code -y
```

The installable product is the skills/ directory; runtimes without the skills CLI can copy the required skills/<name>/ directories into their local skills directory. For a request spanning several rendering systems, start with threejs-choose-skills; focused requests can invoke the owning skill directly. Validate the roster with npm run skills:check.

## What It Provides

skills.sh publishes per-skill descriptions for the 15 sampled listings, and every skill in the table below has one. Of the 29 indexed listings, 27 map to installable skills/<name>/ directories in the current tree; product-from-scratch lives under .claude/skills/ and threejs-physics-integration has no SKILL.md counterpart.

| Skill | Installs | Use For |
|---|---|---|
| threejs-visual-validation | 187 | validating WebGPU/TSL implementations against falsifiable visual, temporal, performance and lifecycle claims |
| threejs-procedural-geometry | 183 | compiling procedural geometry with indexed mesh writers, sweeps, batching and dynamic updates |
| threejs-procedural-materials | 179 | building coherent NodeMaterial PBR systems with UV, array, atlas or projected mapping |
| threejs-procedural-buildings-and-cities | 178 | compiling procedural buildings, cities and semantic site assemblies |
| threejs-particles-trails-and-effects | 177 | representation-first particles, trails and effects with GPU pools and HDR integration |
| threejs-choose-skills | 176 | routing multi-system WebGPU/TSL work to the smallest causal skill set |
| threejs-camera-controls-and-rigs | 175 | one-writer camera rigs, framing, control handoffs and large-world coordinates |
| threejs-object-sculptor | 174 | sculpting reference-image objects into procedural Three.js models |
| threejs-exposure-color-grading | 174 | metering and grading scene-linear WebGPU images with tone-map and LUT assignment |
| threejs-image-pipeline | 173 | coordinating WebGPU/TSL final-image graphs with shared signals and output ownership |
| threejs-sky-atmosphere-and-haze | 173 | building sky, atmosphere and haze with authored fog, scattering and aerial perspective |
| threejs-procedural-motion-systems | 173 | animating semantic state with deterministic WebGPU/TSL motion systems |

The remaining 17 indexed listings range from 2 to 172 installs.

## Why This Matters for Hermes Agents

This is one of the few Three.js collections written for the WebGPU and TSL pipeline rather than the older GLSL path. Each skill encodes a representation-first discipline: choose the workload and truth contract before writing GPU code, name units, owners, validity limits, resets, and failure signatures, and keep sequential actions in order with a checkable completion criterion per step. threejs-choose-skills routes a multi-system request to the smallest causal skill set, and threejs-visual-validation turns "it looks right" into falsifiable claims about visual, temporal, performance, and lifecycle correctness. The product boundary is unusually strict: only self-contained files under skills/<name>/ are installed, and the validator follows JavaScript and TypeScript imports, fetch and readFile calls, and HTML/SVG references to reject repository leakage. Read it for the procedural-graphics reference and for a model of how a skills repository should separate its installable product from demos and labs.

## Usage

| You say | What happens |
|---|---|
| Build an ocean at sunset with clouds and bloom | Uses threejs-choose-skills to route the request across the water, sky, bloom and exposure skills |
| Generate a procedural city block | Uses threejs-procedural-buildings-and-cities for massing, facades, batching and LOD |
| Make the camera fly through the scene | Uses threejs-camera-controls-and-rigs for framing, handoffs and resets |
| Why does this render look wrong? | Uses threejs-debugging to reproduce, localize and contain the failure |
| Add realistic particles and trails | Uses threejs-particles-trails-and-effects with GPU pools and HDR integration |
| Grade the exposure for this scene | Uses threejs-exposure-color-grading for metering, EV and tone-map assignment |
| Prove this scene hits 60 fps | Uses threejs-visual-validation to check performance and lifecycle claims |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/linegel/threejs-complete-set-of-skill/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/linegel/threejs-complete-set-of-skill/main/skills/threejs-visual-validation/SKILL.md | head -40
```

Both URLs return 200. After installing, run npm run skills:check to validate the roster, frontmatter, product boundary, and links, or run the copy-mode smoke installation the README documents to confirm the CLI installs all 27 skills.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| threejs-visual-validation | Pass | Pass | Pass |
| threejs-procedural-geometry | Pass | Pass | Warn |
| threejs-procedural-materials | Pass | Pass | Pass |
| threejs-procedural-buildings-and-cities | Pass | Pass | Pass |
| threejs-particles-trails-and-effects | Pass | Pass | Pass |
| threejs-choose-skills | Pass | Pass | Pass |
| threejs-camera-controls-and-rigs | Pass | Pass | Pass |
| threejs-object-sculptor | Pass | Pass | Pass |
| threejs-exposure-color-grading | Pass | Pass | Pass |
| threejs-image-pipeline | Pass | Pass | Pass |
| threejs-sky-atmosphere-and-haze | Pass | Pass | Pass |
| threejs-procedural-motion-systems | Pass | Pass | Pass |
| threejs-bloom | Pass | Pass | Pass |
| threejs-debugging | Pass | Pass | Warn |
| threejs-ambient-contact-shading | Pass | Pass | Pass |

Two sampled skills carry a Warn cell on Snyk (threejs-procedural-geometry and threejs-debugging); none carries a Fail. 15 of the 29 indexed listings were sampled; the rest were not.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,763 combined installs across 29 indexed listings; 14 GitHub stars; ISC license; last pushed Sep 24, 2026. Counts drift over time.
- The directory description mentions 25 expert skills while the README says 27 installable skills; the current tree ships 27 skill directories under skills/.
- The install index outruns the installable set: product-from-scratch (144 installs) is a separate Claude skill under .claude/skills/, and threejs-physics-integration (2 installs) is experimental notes the README marks as not an installable skill, with no SKILL.md of its own.
- The full repository (4579 files) includes demos, labs, review material and generated media that are not installed; only the skills/<name>/ directories form the installable product.
- Two of the 15 sampled skills carry a Warn cell on Snyk (threejs-procedural-geometry and threejs-debugging); none carries a Fail.
- The skills target Three.js r185 WebGPU/TSL specifically, so they assume the WebGPU renderer and the TSL shading language rather than the legacy GLSL path.

## Related

[Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup) | [Three.js Skills (Cesartevisual) - 3D Web Suite](/hermes/skills/catalog/threejs-cesartevisual-setup) | [PlayCanvas Skills - 3D Web Engine](/hermes/skills/catalog/playcanvas-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start multi-system requests with threejs-choose-skills, then let focused requests invoke the owning skill directly.
- Install everything with --skill '*' for a full environment, or --skill threejs-spectral-ocean to pull a single skill.
- Run npm run skills:check before trusting the roster; it validates frontmatter, the product boundary, links and licenses.
- Treat the top-level threejs-* demos and labs as reference material only; they are not part of the installed product.
- Use threejs-visual-validation last, after the owning skill has built the effect, to prove the visual and performance claims rather than eyeballing them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
