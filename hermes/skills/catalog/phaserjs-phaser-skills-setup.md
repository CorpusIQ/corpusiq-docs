---
title: "Phaser Skills - HTML5 Game Development Suite"
description: "phaserjs/phaser on skills.sh: 26.3K combined installs across 28 listings; 28 skills covering the Phaser 4 API, scenes to physics to tilemaps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/phaserjs-phaser-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "phaser", "html5"]
---

# Phaser Skills - Setup Guide

**Source:** [phaserjs/phaser](https://www.skills.sh/phaserjs/phaser) via skills.sh - 26.3K combined installs across 28 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 40,649 stars, MIT licence, last pushed 2026-08-21, 28 directories at skills/<name>/SKILL.md
**Category:** HTML5 game development for agents: Phaser 4 scenes, rendering, input, physics, audio, tilemaps and migration
**Quality Tier:** 🟢 Production - every sampled audit Pass; MIT; 40,649 stars.

Phaser is a 2D HTML5 game framework maintained by Phaser Studio Inc, and the framework repository now ships its own agent skills: 28 directories under `skills/`, one per subsystem of the Phaser 4 API. Each holds a SKILL.md with a name, a description that ends in trigger terms, the source paths it summarises and links to sibling skills.

The set tracks the v4 renderer rewrite rather than the older pipeline model. Filters, RenderNodes, GPU sprite and tilemap layers and the reworked tint system each have their own entry, and `v3-to-v4-migration` maps the breaking changes for anyone bringing an existing project forward.

## Installation

The skills.sh listing installs the whole set with one command:

```bash
npx skills add phaserjs/phaser
```

The framework itself comes from npm, per the repository README:

```bash
npm install phaser
```

```js
import Phaser from 'phaser';
```

The README's scaffold app is the fastest way to get a project the skills can talk about:

```bash
npm create @phaserjs/game@latest
```

There is no plugin or marketplace manifest in the repository, so the skills.sh CLI is the install route, and a manual copy of `skills/*/SKILL.md` into your agent's skill directory does the same job.

## What It Provides

All 28 indexed listings are above the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| game-setup-and-config | 1,305 | Creating a Phaser.Game instance and GameConfig: renderer choice, canvas placement, pixel art, FPS and boot sequence |
| sprites-and-images | 1,195 | Sprite and Image factory methods, texture and frame selection, scale, tint, origin, depth and component mixins |
| animations | 1,143 | Spritesheets, atlases, AnimationManager, play and chain control, frame callbacks and animation events |
| tilemaps | 1,049 | Tiled JSON maps, tilemap layers, tile collision, dynamic tiles and tilemap camera culling |
| scenes | 1,037 | Scene lifecycle methods, transitions, parallel scenes, sleeping, pausing, restarting and SceneManager traffic |
| input-keyboard-mouse-touch | 1,034 | Keyboard keys, pointer and touch handling, drag and drop, hit areas, interactive objects and gamepads |
| v4-new-features | 1,030 | What Phaser 4 adds: Filters, RenderNodes, Gradient, Noise, GPU sprite and tilemap layers and the new tint system |
| audio-and-sound | 1,018 | Loading and playing audio, music and volume control, spatial audio, Web Audio and the SoundManager |
| scale-and-responsive | 993 | ScaleManager modes (FIT, RESIZE, EXPAND, ENVELOP), auto-centring, fullscreen and browser resize |
| loading-assets | 980 | Loader plugin for images, spritesheets, atlases, audio, JSON, tilemaps and bitmap fonts, plus load progress |
| tweens | 974 | Property tweens, chains, easing functions, stagger, yoyo, repeat, callbacks and the TweenManager |
| cameras | 951 | Camera shake, fade, flash, pan and zoom, follow behaviour, scroll, bounds, viewports and minimaps |
| particles | 940 | ParticleEmitter, emission and death zones, particle properties, textures, gravity wells and movement |
| physics-arcade | 925 | Arcade Physics: velocity, acceleration, gravity, collisions, overlap, world bounds and static bodies |
| graphics-and-shapes | 888 | The Graphics object for lines, rectangles, circles, arcs, polygons, gradients and generated textures |
| text-and-bitmaptext | 887 | Text and BitmapText, web fonts, styling, word wrap, alignment, padding and dynamic content |
| geometry-and-math | 861 | Vectors, rectangles, circles, triangles, polygons, angles, distance, interpolation and snapping |
| groups-and-containers | 854 | Groups, object pooling, batch operations and nested transforms inside Containers |
| time-and-timers | 853 | TimerEvent, delayed calls, looping timers, the Clock plugin and time scaling |
| game-object-components | 853 | Shared component mixins: Transform, Alpha, Tint, Origin, Depth, Flip, Mask, GetBounds and Lighting |
| events-system | 840 | EventEmitter, scene and game events, custom events and event-driven communication |
| filters-and-postfx | 838 | Bloom, blur, glow, colour matrix, barrel distortion, displacement, custom shaders and the filter pipeline |
| render-textures | 831 | RenderTexture and DynamicTexture, drawing objects to textures, snapshots, stamps and offscreen rendering |
| physics-matter | 812 | Matter.js rigid bodies, constraints, composite bodies, sensors and collision filtering |
| data-manager | 811 | DataManager key-value data on game objects, data change events and custom game state |
| actions-and-utilities | 810 | Alignment, grid layout, batch actions and set operations across groups of game objects |
| curves-and-paths | 807 | Splines, bezier curves, lines, ellipses, path followers and mathematical curve types |
| v3-to-v4-migration | 770 | Phaser 3 to 4 migration: pipelines to render nodes, FX and masks to filters, tint changes and API differences |

No indexed listings fall below the threshold; all 28 appear above.

## Why This Matters for Hermes Agents

Game requests fail in a specific way: the loop runs, the canvas renders, and the result is wrong in a way no stack trace reports. These skills give an agent the actual API surface for scenes, physics, input and cameras, which removes most of the confident-but-nonexistent method names that canvas work attracts.

The skills ship inside the framework repository, so they are versioned with the code they describe. Text about Phaser 4 render nodes is not advice about Phaser 3 pipelines, and the split between `v4-new-features` and `v3-to-v4-migration` makes that boundary explicit rather than leaving the agent to infer it from a changelog.

Each description ends in trigger terms, so routing is keyword driven: `tween`, `Tilemap`, `ScaleManager` and `this.add.sprite` each resolve to one skill instead of pulling the whole pack into context. That matters when a session is already long and a single question about camera fade should not cost 28 files.

The reference detail is what makes the pack usable for tool work. Every skill names the source files it summarises, such as `src/core/Game.js` and `src/scale/const/`, so an agent can escalate from the summary to the real implementation when the summary runs out.

## Usage

| You say | What happens |
|---|---|
| "start a new Phaser 4 game" | game-setup-and-config settles renderer, canvas, scaling and FPS before any scene code is written |
| "my sprite renders but the tint is wrong" | sprites-and-images covers tint and frame state, and game-object-components explains the mixin behind it |
| "load this Tiled map and block the walls" | tilemaps covers Tiled JSON loading, layer setup and per-tile collision |
| "move the player with arcade physics" | physics-arcade sets velocity, gravity, colliders and world bounds |
| "port our Phaser 3 build to v4" | v3-to-v4-migration maps pipelines to render nodes and FX to filters, with the breaking changes listed |
| "burst particles when the player dies" | particles configures an emitter with emission zones, textures and particle properties |
| "the canvas is cut off on phones" | scale-and-responsive picks a ScaleManager mode and handles browser resize |

## Verification

Fetch one skill file and confirm the frontmatter matches the listing. The path below is `skills/game-setup-and-config/SKILL.md` on branch master, and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/phaserjs/phaser/master/skills/game-setup-and-config/SKILL.md | head -5
```

A response opening with `name: game-setup-and-config` and a quoted description confirms the tree still matches what skills.sh indexed. Then confirm the directory count:

```bash
curl -s "https://api.github.com/repos/phaserjs/phaser/contents/skills" | grep -c '"type": "dir"'
```

That returns 28. After the install, run this from the directory your agent loads skills from to confirm the copies landed:

```bash
ls -d */ | grep -E "^(game-setup-and-config|scenes|tilemaps)$"
```

Three matching directory names is the expected result.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| game-setup-and-config | Pass | Pass | Pass |
| sprites-and-images | Pass | Pass | Pass |
| animations | Pass | Pass | Pass |
| graphics-and-shapes | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 26,289 combined installs across 28 indexed listings; 40,649 GitHub stars; MIT licence; last pushed 2026-08-21. Counts drift over time.
- The skills document Phaser 4. A project still on Phaser 3 should start with v3-to-v4-migration or the v3 documentation, because the subsystem text describes the node renderer.
- Four of the 28 listings were sampled for security verdicts. The other 24 have no verdict recorded on this page, so review the individual skill files before use in a production build.
- The skills live inside the framework repository. Cloning it to read them pulls the full source tree and its history, not a small standalone skill pack.
- `phaser.js` is 8.23 MB because roughly 84 percent of it is inline JSDoc; the minified build is 1.29 MB, or 345 KB gzipped. Plan build sizes around the minified file.
- There is no plugin or marketplace manifest, so updates are a re-run of the skills.sh install rather than a versioned package upgrade.

## Related

- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup)
- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [Roblox Brain - Roblox Studio Development Skills Setup](/hermes/skills/catalog/roblox-brain-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read v4-new-features once before starting. Filters, RenderNodes, GPU layers and the tint change appear again in almost every other skill.
- Load two skills per question at most. The descriptions are deliberately narrow, and stacking five of them dilutes the trigger match that made routing work.
- Ask for the source path when a summary is thin. Each skill names the files it covers, so the agent can read `src/` directly instead of paraphrasing.
- Keep renderer, scale mode and FPS decisions in one place. game-setup-and-config owns them, and scattering them across scenes is what breaks responsive builds later.
- Scaffold with `npm create @phaserjs/game@latest` first, then install the skills into that project, so the template and the skill text agree on version.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
