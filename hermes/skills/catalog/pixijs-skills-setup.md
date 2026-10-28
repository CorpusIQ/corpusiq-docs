---
title: "PixiJS Skills - 2D WebGL and WebGPU Rendering Suite Setup"
description: "Official PixiJS v8 suite: 151.7K combined installs. Application, scene graph, sprites, text, filters, shaders, and v7 migration for 2D web rendering."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pixijs-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "pixijs", "2d rendering", "webgpu"]
---

# PixiJS Skills - Setup Guide

**Source:** [pixijs/pixijs-skills](https://www.skills.sh/pixijs/pixijs-skills) via skills.sh - 151.7K combined installs across 26 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [pixijs/pixijs-skills](https://github.com/pixijs/pixijs-skills) - 358 stars, MIT, branch main, 26 skill directories under `skills/`, each one `SKILL.md` plus an optional `references/` folder, for 65 markdown files and roughly 856 KB of content in the clone

**Category:** 2D rendering and web game graphics with WebGL, WebGPU and Canvas

**Quality Tier:** 🟡 Beta - maintained under the official PixiJS organization, 358 GitHub stars, 26 indexed listings matching 26 skill directories one for one, MIT licensed, six skills sampled by three auditors with one Snyk warning

PixiJS is a 2D rendering library for WebGL, WebGPU and Canvas, and this repository is its own answer to the question of what an AI agent should write when asked to build with it. It is version-scoped to the v8 line. The skills cover the whole surface an agent actually touches: creating and configuring an `Application`, the scene graph, sprites, graphics, text, filters, custom shaders, assets, events, math, colour, the ticker, accessibility, non-browser environments, performance work, and the v7 to v8 migration that most real projects are still in the middle of.

The shape is one router plus 25 specialists. `pixijs` is the entry point: it holds a table that maps a task to the skill that owns it, and it tells the agent to load exactly one of them rather than reasoning from memory. Long material is pushed into `references/` folders, so `pixijs-assets` carries 12 reference files, `pixijs-scene-core-concepts` carries 7, and `pixijs-scene-text`, `pixijs-scene-mesh` and `pixijs-scene-sprite` carry 5, 5 and 4. The repository's sync commit names `pixijs/pixijs@v8.22.0` as its source, so the API detail tracks a specific upstream release rather than drifting free.

## Installation

The README leads with the skills CLI, which installs from the repository into the agent's skill directory:

```bash
npx skills add https://github.com/pixijs/pixijs-skills
```

Claude Code users add the repository as a plugin marketplace, with the slash command the README gives, run inside a session:

```text
/plugin marketplace add pixijs/pixijs-skills
```

Cursor has no marketplace step in the README. It points at Settings, then Rules, then Add Rule, then Remote Rule (Github), with the repository as the value. Both client paths read the same tree, since the repository ships a `.claude-plugin/marketplace.json` manifest and a `.cursor-plugin/` directory alongside it.

For Hermes and every other agent that reads a skill directory directly, the tree is the install source. Each directory under `skills/` is a self-contained skill, so a shallow clone and a copy of the directories you want is equivalent to a CLI install of those skills:

```bash
git clone --depth 1 https://github.com/pixijs/pixijs-skills.git
cp -R pixijs-skills/skills/pixijs ~/.hermes/profiles/corpusiq/skills/
cp -R pixijs-skills/skills/pixijs-scene-graphics ~/.hermes/profiles/corpusiq/skills/
```

Copy `pixijs` even if you only want one or two specialists. It is the router, it is the skill the install index ranks first, and without it the agent has no map from a request to the right directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pixijs | 6,929 | Entry point and router: load it first for any v8 task and it names the specialist that owns the job, with a `references/index.md` holding every skill's long description and trigger list. |
| pixijs-application | 6,096 | Creating and configuring an `Application`: `app.init()` options, `app.stage`, renderer and canvas access, the resize and ticker plugins, `app.destroy()`. |
| pixijs-performance | 6,079 | Profiling FPS, draw calls and GPU memory: destroy patterns, `GCSystem`, `TextureGCSystem`, object pooling, batching rules, `BitmapText` for dynamic text, culling, resolution and antialias tradeoffs. |
| pixijs-core-concepts | 6,033 | How a frame is rendered: the systems-and-pipes renderer, the render loop, choosing WebGL, WebGPU or Canvas, rendering into a `RenderTexture`, and context or device loss. |
| pixijs-scene-graphics | 6,031 | Vector drawing: shape-then-fill methods, path building, fill, stroke and cut, holes, gradients, patterns, shared `GraphicsContext`, SVG import and export. |
| pixijs-assets | 6,004 | Loading resources: `Assets.init`, `Assets.load`, bundles, manifests, background loading, caching, spritesheets, web and bitmap fonts, video, GIFs, compressed textures. |
| pixijs-scene-sprite | 5,974 | Drawing images: `Sprite` with anchor, tint and texture, `AnimatedSprite` for frame animation, `NineSliceSprite` for resizable panels, `TilingSprite` for scrolling backgrounds. |
| pixijs-events | 5,973 | Pointer, mouse, touch and wheel input: `eventMode` values, `FederatedEvent`, propagation and capture, `hitArea`, cursor handling, drag patterns. |
| pixijs-scene-container | 5,949 | Grouping and transforming: `Container` options, child management, local and world transforms, bounds, `zIndex` sorting. |
| pixijs-math | 5,926 | Coordinates and geometry: `Point`, `Matrix`, `Rectangle`, `Polygon`, hit tests, `toGlobal` and `toLocal`, plus the `pixi.js/math-extras` vector and intersection helpers. |
| pixijs-scene-core-concepts | 5,907 | The scene graph as a whole: leaf versus container, transforms, render order, culling, render groups, `RenderLayer`, masking. |
| pixijs-scene-text | 5,876 | Text rendering: `Text` for styled labels, `BitmapText` for cheap per-frame updates, `HTMLText`, `SplitText`, `TextStyle` and tag styles. |
| pixijs-ticker | 5,873 | Per-frame logic: `Ticker.add` and `addOnce`, `deltaTime` against `deltaMS`, `UPDATE_PRIORITY` ordering, frame rate caps, the on-render hook. |
| pixijs-filters | 5,858 | The effects pipeline: built-in filters, custom `Filter.from` with GLSL or WGSL, `filterArea`, and the `pixi-filters` package. |
| pixijs-scene-particle-container | 5,855 | Thousands of lightweight sprites: `ParticleContainer` with `Particle` instances, `dynamicProperties`, `boundsArea`. |
| pixijs-custom-rendering | 5,801 | Custom shaders, uniforms and batchers: `Shader.from`, `GlProgram` and `GpuProgram`, uniform groups and UBO mode, 3D and array textures, storage textures, render bundles, custom pipes. |
| pixijs-create | 5,786 | Scaffolding: `npm create pixi.js@latest` and its yarn, pnpm and bun forms, the vite and react templates, adding PixiJS to an existing project, `tsconfig` for TypeScript 5, 6 or 7. |
| pixijs-color | 5,785 | The `Color` class: hex, CSS name, RGB and HSL input, conversion methods, premultiply, the shared singleton. |
| pixijs-blend-modes | 5,769 | Compositing: standard modes such as add, multiply, screen and erase, and the advanced set behind `pixi.js/advanced-blend-modes`. |
| pixijs-scene-dom-container | 5,737 | Overlaying HTML on the canvas: `DOMContainer` with an element, anchor and scene-graph-driven CSS transforms, and the `pixi.js/dom` import. |
| pixijs-scene-mesh | 5,723 | Custom geometry: `Mesh` with `MeshGeometry`, `MeshSimple` for per-frame vertex animation, `MeshPlane`, `MeshRope`, `PerspectiveMesh`. |
| pixijs-environments | 5,661 | Running outside a standard browser: Web Workers, `OffscreenCanvas`, Node and server rendering, strict CSP contexts through `DOMAdapter` and `pixi.js/unsafe-eval`. |
| pixijs-scene-gif | 5,638 | Animated GIFs: the `pixi.js/gif` import, `GifSource` from `Assets.load`, `GifSprite` playback, autoplay and loop settings, callbacks, clone and destroy. |
| pixijs-accessibility | 5,568 | Screen reader and keyboard navigation: `AccessibilitySystem` options, the shadow DOM overlay, tab activation and mouse deactivation behaviour. |
| pixijs-migration-v8 | 5,372 | Upgrading from v7: async `app.init`, the single `pixi.js` package replacing `@pixi/*`, the shape-then-fill Graphics API, `BaseTexture` removal, the shader rework. |

The remaining 1 indexed listing is pixijs-html-source (4,532 installs), experimental HTML-in-Canvas textures through `HTMLSource` and `ElementImageSource`.

## Why This Matters for Hermes Agents

Rendering libraries are where an agent's memory of an API costs the most time. A v8 session that writes `beginFill` and `endFill`, imports from `@pixi/*`, or calls `new Application({ width: 800 })` produces code that fails at the first line executed, and the failure reads like a build problem rather than a version problem. `pixijs-migration-v8` exists for exactly that class of mistake, and it names the deltas instead of describing them in general terms.

The router is the second gain. A single skill holds the map from intent to directory, so an agent asked to "make the sprites drift" lands on `pixijs-ticker` for the frame loop and `pixijs-events` only if input is involved, instead of loading the whole suite into context. That matters on a Hermes profile that already carries a large skill library, where every extra thousand tokens is paid on every turn.

The third gain is specificity on the parts that are easy to get subtly wrong. Filter areas, culling configuration, `destroy` patterns and texture GC are all described as procedures with the option names attached, and `pixijs-performance` states which of them actually move FPS. An agent working from general knowledge writes plausible optimisations; this suite writes the ones the maintainers benchmarked.

There is also a documented escape hatch worth knowing. When no sub-skill matches a request, `pixijs` instructs the agent to fetch `https://pixijs.download/release/docs/llms.txt`, the generated index of the full API, and follow the matching page. That keeps the suite honest about its own coverage instead of letting the agent improvise the gaps.

## Usage

| You say | What happens |
|---|---|
| "Set up a PixiJS canvas in this Vite app" | The router picks pixijs-application, which walks `new Application()` plus `await app.init()` with the resize and autoDensity options, appends the canvas, and wires the resize plugin. |
| "Add a sprite that follows the pointer" | pixijs-events sets `eventMode` on the sprite, uses the federated pointer events for the move, and pixijs-ticker or the same handler applies the position with `deltaTime` scaling. |
| "Draw a rounded button with a gradient and a hover state" | pixijs-scene-graphics builds the shape with the shape-then-fill calls, applies a gradient fill, and pixijs-events adds the hit area and cursor change. |
| "The frame rate drops when the particle count goes up" | pixijs-performance works the batching and culling checklist, moves the sprites into a ParticleContainer where the properties allow it, and reports which change it expects to matter. |
| "We are on v7 and the upgrade broke our graphics code" | pixijs-migration-v8 maps each broken call to its v8 replacement, starting with async init and the shape-then-fill API, and flags the removed `@pixi/*` imports. |
| "This has to run in a Web Worker" | pixijs-environments sets up the worker adapter and OffscreenCanvas handoff, and names the features that do not survive the move. |
| "Make the game readable by a screen reader" | pixijs-accessibility wires `AccessibilitySystem`, sets accessible titles and tab order, and explains the shadow DOM overlay and the mobile activation caveat. |

## Verification

Probe the paths before you copy them. Every URL below returned 200 on branch main when this guide was written:

```bash
for p in skills/pixijs/SKILL.md \
         skills/pixijs-application/SKILL.md \
         skills/pixijs-performance/SKILL.md \
         skills/pixijs/references/index.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/pixijs/pixijs-skills/main/$p"
done
```

Read the router before installing anything else, because it is the file that tells an agent which of the other 25 to open:

- https://raw.githubusercontent.com/pixijs/pixijs-skills/main/skills/pixijs/SKILL.md
- https://raw.githubusercontent.com/pixijs/pixijs-skills/main/skills/pixijs/references/index.md

After a copy install, each skill is one directory with its own `SKILL.md`. Confirm what actually landed, since a partial copy is silent:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c '^pixijs'
head -4 ~/.hermes/profiles/corpusiq/skills/pixijs/SKILL.md
```

The count should match the number of directories you copied, and the `head` output should show the frontmatter name `pixijs`, which is also the name the install index uses. A different name means you are reading a stale copy.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pixijs | Pass | Pass | Warn |
| pixijs-application | Pass | Pass | Pass |
| pixijs-performance | Pass | Pass | Pass |
| pixijs-core-concepts | Pass | Pass | Pass |
| pixijs-scene-graphics | Pass | Pass | Pass |
| pixijs-assets | Pass | Pass | Pass |

The install surface is text only. The repository has no `package.json` at the root and no shell scripts, so adding the skills runs nothing and resolves no dependency; what lands in the skill directory is markdown. The Snyk warning on `pixijs` carries the code W011, and the sampled set is six of 26 listings, so the 17 passes above say nothing about the other 20. Treat the table as a starting point and open the individual security page for any skill you intend to keep installed.

Two run-time behaviours are worth flagging even though neither is a verdict failure. `pixijs` instructs the agent to fetch `https://pixijs.download/release/docs/llms.txt` when no sub-skill matches, which is an outbound read of a documentation site and should be allowed or blocked deliberately in a restricted environment. `pixijs-create` instructs the agent to run `npm create pixi.js@latest`, which writes a new project directory and installs dependencies, so a scaffolding request reaches the package registry even though the skills themselves do not.

The suite handles no credentials, no tokens and no remote state. Nothing in it deploys, publishes, deletes or bills. The realistic risk is a wrong-but-plausible render loop shipped into a game, not a compromised install.

## Limitations

- Snapshot data, verified 2026-10-28: 151,735 combined installs across 26 indexed listings; 358 GitHub stars; MIT; last pushed 2026-10-01. Counts drift over time.
- The suite is v8 only. There is one migration skill for reading v7 code and no v7 reference set, so an agent asked to maintain a v7 project has to translate backwards, and the migration skill is written in one direction.
- `pixijs-html-source` depends on experimental browser APIs (the HTML-in-Canvas specification) and is the only listing under 5,000 installs. Expect it to be unusable outside a recent Chromium build and to change shape upstream.
- API detail tracks the sync commit's upstream tag (`pixijs/pixijs@v8.22.0`, pushed 2026-10-01), which is a point in time rather than a live link. A skill can describe a release that is behind the installed package, and the router's documentation fallback is the intended remedy.
- The documented install paths are the skills CLI, the Claude Code plugin marketplace and Cursor remote rules. There is no per-skill install command for other agents, so on Hermes the copy route is the only one available, and it brings no plugin commands or hooks with it.
- 26 indexed listings line up exactly with 26 directories, so the index maps cleanly to the tree here. The combined figure is the sum of per-listing installs, not a count of distinct projects or users.

## Related

- [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup)
- [Three.js Game Skills - 3D Game Development Suite Setup](/hermes/skills/catalog/threejs-game-skills-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `pixijs` plus the two or three specialists you actually need. The router is small, it carries the map, and the specialists are the files that hold the API detail you do not want an agent inventing.
- Name the version when you ask. Saying "PixiJS v8" in the request keeps the agent inside these skills; saying "PixiJS" alone invites v7 patterns that the migration skill then has to undo.
- For anything where the answer is not in the router table, tell the agent to fetch the documentation index the router names. That one URL is a cheaper correction than a wrong shader.
- Ask for the destroy and cleanup path in the same request as the feature. `pixijs-performance` has the patterns, but an agent that has already moved on will not volunteer them.
- When a filter or blend mode looks wrong on WebGPU but fine on WebGL, check the skill's environment notes before rewriting the shader. Several behaviours differ by renderer, and the fix is usually a mode choice rather than shader code.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
