---
title: "Claude Design Skillstack - 3D & Animation Setup"
description: "Setup guide for freshtechbro/claudedesignskills - 60.8K combined installs. A 3D/WebGL, animation, and modern web design skillstack for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claudedesignskills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "webgl", "animation", "web design"]
---

# Claude Design Skillstack - Setup Guide

**Source:** [freshtechbro/claudedesignskills](https://www.skills.sh/freshtechbro/claudedesignskills) via skills.sh - 60.8K combined installs across 23 indexed listings; first seen Oct 10, 2026 (evening sweep)
**GitHub:** [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) (1,021 stars, MIT; pushed Nov 20, 2025; `.claude/skills/<name>/SKILL.md` layout)
**Category:** 3D / WebGL / Animation / Web Design
**Quality Tier:** 🟢 Production - 1,021-star MIT skillstack; 23 listings, 60.8K combined; all sampled verdicts Pass; last pushed Nov 2025

freshtechbro's Claude Design Skillstack is a design agency in a repo: a Claude Code plugin marketplace covering 3D/WebGL, animation, scroll effects, and modern web design. The README counts 27 plugins (22 individual skills plus 5 category bundles), 50+ slash commands, and 27+ specialized agents, with coverage that spans Three.js, GSAP, React Three Fiber, Framer Motion, and Babylon.js through to Blender, Spline, Rive, and Substance 3D pipelines. Each skill is a standard Claude skill package (SKILL.md plus references, scripts, and assets), and skills.sh indexes 23 listings with 60.8K combined installs, every one above 1,993.

Two organizational details matter when installing. First, the five bundles (core-3d-animation, extended-3d-scroll, animation-components, authoring-motion, meta-skills) group the individual skills by workflow, which is usually the right granularity. Second, the repository was last pushed Nov 20, 2025 - roughly 11 months before this snapshot - so treat version compatibility for fast-moving libraries like Three.js and the React ecosystem as something to verify per project.

---

## Installation

Add the marketplace to Claude Code, then install individual plugins or complete bundles:

```bash
# Add marketplace
/plugin marketplace add freshtechbro/claudedesignskills

# Install individual plugins
/plugin install threejs-webgl
/plugin install gsap-scrolltrigger
/plugin install react-three-fiber

# Or install complete bundles
/plugin install core-3d-animation        # 5 skills: Three.js, GSAP, R3F, Motion, Babylon
/plugin install extended-3d-scroll       # 6 skills: A-Frame, Vanta, PlayCanvas, PixiJS, Locomotive, Barba
/plugin install animation-components     # 5 skills: React Spring, Magic UI, AOS, Anime.js, Lottie
/plugin install authoring-motion         # 4 skills: Blender, Spline, Rive, Substance 3D
/plugin install meta-skills              # 2 skills: Integration patterns, Modern design
```

Individual skills can also be uploaded to claude.ai (Skills settings, then Upload skill) from the `.claude/skills/` zips, or the repo can be cloned for local customization; each skill auto-activates when the agent detects a relevant task.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| motion-framer | 5,190 | Framer Motion animation work: 11 generator types, React motion patterns |
| threejs-webgl | 4,176 | Three.js scenes and WebGL boilerplate via setup_scene.py, PBR material patterns |
| react-three-fiber | 3,289 | Declarative React Three Fiber components from 12 generator types |
| blender-web-pipeline | 3,054 | Blender to web asset pipeline for models and scenes |
| web3d-integration-patterns | 2,852 | Integration patterns for combining 3D libraries inside web app architectures |
| modern-web-design | 2,681 | Modern web design practice for current browser capabilities |
| lottie-animations | 2,659 | Lottie vector motion for product and marketing UI |
| animated-component-libraries | 2,626 | Drop-in animated component libraries for React interfaces |
| gsap-scrolltrigger | 2,578 | GSAP scroll timelines via generate_animation.py and timeline_builder.py |
| spline-interactive | 2,555 | Spline scenes brought into production pages |
| animejs | 2,506 | Anime.js micro-animations and timeline choreography |
| lightweight-3d-effects | 2,380 | Lightweight 3D page effects without full WebGL overhead |
| rive-interactive | 2,366 | Stateful interactive motion for product interfaces |
| locomotive-scroll | 2,339 | Smooth scrolling and parallax behavior |
| pixijs-2d | 2,312 | Fast 2D canvas rendering for games and interactive graphics |
| babylonjs-engine | 2,296 | Babylon.js scenes: 8 scene types and 13 mesh shapes via generators |
| react-spring-physics | 2,227 | Physics-based React motion for natural interactions |
| scroll-reveal-libraries | 2,216 | Viewport-triggered entrance and reveal animations |
| substance-3d-texturing | 2,171 | PBR texturing workflows for production 3D assets |
| barba-js | 2,152 | Page transitions between views |
| aframe-webxr | 2,114 | Browser VR and AR scenes with A-Frame |
| playcanvas-engine | 2,106 | Browser games and interactive 3D with the PlayCanvas engine |
| skill-creator | 1,993 | Skill authoring: init_skill.py, quick_validate.py, package_skill.py |

Every indexed listing clears the 1,500-install threshold, so the table above covers the full skills.sh index for this repo.

## Why This Matters for Hermes Agents

Agents write web UI constantly, and the difference between passable and polished is almost always motion and 3D craft: springs that feel physical, scroll choreography that stays in sync, shaders that do not tank the frame budget. This skillstack encodes that craft as loadable skills - patterns, boilerplate generators, and integration guides for the exact libraries design engineers reach for. The plugin packaging matters for multi-agent setups: bundles install a whole workflow area at once, and the slash commands give an agent deterministic entry points instead of freehand component writing. Because everything is MIT and plain SKILL.md, teams can vendor, trim, or fork the parts they need. The generator scripts (50+ across the repo) cut the most tedious part of 3D work: scene, component, and animation boilerplate. The caveat is upkeep: with the repo about 11 months stale, pair the skill patterns with current library docs when versions diverge. For Hermes-style agents, this is a broad, well-organized reference layer for any task involving WebGL, animation, or scroll behavior.

## Usage

| You say | What happens |
|---|---|
| "Create a Three.js scene with PBR materials" | threejs-webgl activates with setup_scene.py boilerplate and material patterns |
| "Add GSAP scroll animations to this page" | gsap-scrolltrigger builds timelines via generate_animation.py and timeline_builder.py |
| "Build a React Three Fiber component with physics" | react-three-fiber generates from its 12 component types |
| "Give this hero a lightweight 3D background" | lightweight-3d-effects or pixijs-2d picks the right weight class for the effect |
| "Animate this list with spring physics" | react-spring-physics applies physical motion patterns |
| "Prepare this Blender model for the web" | blender-web-pipeline handles the 3D asset pipeline and export |
| "Package a new skill for our team" | skill-creator runs init_skill.py, quick_validate.py, and package_skill.py |

## Verification

```bash
# In Claude Code, confirm the marketplace and installed plugins
/plugin

# Repo clone: count the skill directories and packages
ls -d .claude/skills/*/ | wc -l

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/freshtechbro/claudedesignskills/main/.claude/skills/motion-framer/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| motion-framer | Pass | Pass | Pass |
| react-three-fiber | Pass | Pass | Pass |
| threejs | - | - | - |

Two of the three sampled skills are clean across all three engines; threejs is unrated. Coverage is 2 of the 23 skills, so extend checks to any skill you plan to run unattended.

## Limitations

- Staleness: last pushed Nov 20, 2025, roughly 11 months before this snapshot; verify API compatibility for fast-moving libraries (Three.js, GSAP, React ecosystem) before production use.
- Verdict coverage is 2 of 23 skills; the rest are unsampled.
- Community footprint is light for the install count: 1,021 GitHub stars for a 23-skill set.
- Depth varies by skill: some are pattern libraries, others ship generator scripts and packaged assets; audit per skill.
- The packaging targets Claude Code (plugin marketplace and claude.ai uploads); other agents consume the SKILL.md files directly.
- Snapshot data, verified Oct 10, 2026: 60,838 combined installs across 23 indexed listings; 1,021 GitHub stars; MIT; last pushed Nov 20, 2025. Counts drift over time.

## Related

- [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup) - the single-library counterpart for the flagship skill
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup) - deeper GSAP coverage than the bundled skill
- [Motion Design Skill - LottieFiles Animation Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup) - Lottie-focused motion work
- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup) - programmatic video when motion work graduates to video
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install bundles, not singles, when starting: core-3d-animation is the highest-leverage first pick.
- The foundation skills (threejs-webgl, gsap-scrolltrigger, motion-framer) anchor most integrations; learn those first.
- Lean on the generator scripts before writing boilerplate: setup_scene.py, component_generator.py, and timeline_builder.py cover the common cases.
- Skills are compatible with claude.ai upload (SKILL.md at zip root) if you prefer library-style management over the marketplace.
- Because the repo pre-dates recent library releases, diff the patterns against current docs when a project uses bleeding-edge versions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
