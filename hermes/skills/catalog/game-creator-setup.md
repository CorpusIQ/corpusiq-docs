---
title: "Game Creator - Playable Intelligence Game Skills"
description: "playableintelligence/game-creator on skills.sh: 31.8K installs across 31 listings; 31 skills taking a 2D or 3D browser game from idea to Play.fun."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/game-creator-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "phaser", "threejs"]
---

# Game Creator - Setup Guide

**Source:** [playableintelligence/game-creator](https://www.skills.sh/playableintelligence/game-creator) via skills.sh - 31.8K combined installs across 31 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 355 stars, no LICENSE file (the README License section states MIT), last pushed 2026-11-03, 31 directories at skills/<name>/SKILL.md
**Category:** Game production for agents: ideation, core loop design, level and systems tuning, art direction and playtest loops
**Quality Tier:** 🟡 Yellow: game-3d-assets draws Socket and Snyk Warns, and the repo ships no LICENSE file even though the README states MIT

Game Creator is an opinionated Claude plugin that turns a prompt into a playable browser game on one of two engines: Phaser 3 for 2D and Three.js for 3D. Thirty-one skills divide the work between reference guidance (engine patterns, assets, audio, architecture), user-invocable commands (viral-game, make-game, improve-game, add-feature) and review passes.

The pipeline is the product. Every code-modifying step is followed by a QA subagent that runs build, headless runtime, gameplay, architecture and visual checks, with an autofix loop of up to three attempts. Games are scaffolded from one of two shipped templates rather than generated from scratch, and every game exposes `window.render_game_to_text()` so an agent can read state as JSON instead of interpreting pixels.

## Installation

The README documents one install line, with an agent flag for scoping:

```bash
npx skills add playableintelligence/game-creator
```

```bash
npx skills add playableintelligence/game-creator -a claude-code
```

The same pattern works for other targets the README names:

```bash
npx skills add playableintelligence/game-creator -a codex
```

```bash
npx skills add playableintelligence/game-creator -a cursor
```

The README states the pack works with 40 or more coding agents through `npx skills add`. When it is installed as a plugin, the commands are namespaced, for example `/game-creator:viral-game`, `/game-creator:make-game` and `/game-creator:add-assets`.

## What It Provides

Twenty of the 31 indexed listings meet the 898-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| game-designer | 2,015 | Visual polish: gradients, particles, screen shake, transitions and juice |
| game-assets | 1,624 | Pixel art sprites through renderPixelArt, renderSpriteSheet and a palette system |
| design-game | 1,474 | Audits an existing game's visuals and implements the polish pass |
| phaser | 1,419 | Phaser 3 scene patterns, arcade physics and high-DPI rendering |
| game-audio | 1,348 | Strudel.cc background music plus Web Audio sound effects |
| game-architecture | 1,237 | EventBus, GameState and Constants reference architecture |
| threejs-game | 1,134 | Three.js event-driven, modular game structure |
| game-3d-assets | 1,127 | Finds, downloads and integrates GLB and GLTF models into Three.js games |
| improve-game | 1,122 | Audits a game and implements the highest-impact fixes |
| game-qa | 1,120 | Playwright visual regression, gameplay, performance and accessibility testing |
| make-game | 1,108 | Multi-session workflow with milestones, ADRs and docs/STATE.md |
| add-audio | 1,038 | Adds music and sound effects to an existing game |
| add-assets | 1,027 | Replaces geometric shapes with pixel art sprites |
| add-feature | 1,007 | Adds a gameplay mechanic that follows the project architecture |
| review-game | 982 | Read-only review of architecture, performance and practice |
| qa-game | 967 | Writes Playwright QA tests for an existing game |
| add-3d-assets | 965 | Swaps primitive shapes for real GLB models in 3D games |
| meshyai | 935 | Generates, auto-rigs and animates 3D models through Meshy AI |
| game-deploy | 935 | Deploys to here.now by default, plus GitHub Pages, Vercel and itch.io |
| quick-game | 898 | Fast playable scaffold with no assets, audio, deploy or monetization |

The remaining 11 indexed listings range from 586 to 893 installs, covering monetization, promo recording, template cloning, world generation and multiplayer.

## Why This Matters for Hermes Agents

Agent-built games usually fail in the same place: the code compiles, nothing throws, and the game is unplayable. Game Creator answers that with a QA subagent after every step and an autofix loop, so a Hermes agent gets a failing signal from a headless browser rather than from a human playing the result.

The second transferable idea is the fixed architecture. Every game, 2D or 3D, uses an EventBus for cross-module traffic, a single GameState with `reset()`, and a Constants file for every magic number. An agent that knows the layout can add a feature without re-reading the whole codebase, and the architecture validator can flag drift mechanically.

`render_game_to_text()` is the pattern worth stealing for non-game work too. It exposes current state as a JSON string, which gives an agent a readable observation channel for a canvas app that has no DOM to inspect.

The pack is also honest about scope boundaries. add-assets is 2D only, add-3d-assets is 3D only, review-game makes no changes, and quick-game deliberately skips deploy and monetization, so routing between skills stays predictable.

Two cautions belong in the same breath. The QA path assumes Node, Vite and Playwright are available, and monetization means calling third-party services: Play.fun registration needs its MCP server, and the 3D asset skills reach paid APIs.

## Usage

| You say | What happens |
|---|---|
| "make a space invaders game" | viral-game scaffolds from the Phaser template, adds pixel art, polish, audio, then deploys and monetizes |
| "/game-creator:viral-game 2d my-game" | One-shot pipeline: scaffold, sprites, design, audio, promo video, deploy to here.now and Play.fun |
| "build a game from this tweet" | fetch-tweet pulls the post through the fxtwitter API, then viral-game builds from it |
| "/game-creator:make-game" | Multi-session project: idea, scaffold, phases with milestones, ADRs and a state file |
| "add chiptune music and sound effects" | add-audio writes Strudel.cc music patterns and Web Audio SFX |
| "replace the shapes with pixel art" | add-assets generates sprites through renderPixelArt and the palette system |
| "review my game architecture" | review-game produces a read-only architecture and performance review |
| "add Playwright tests to my game" | qa-game writes gameplay, visual regression and accessibility tests |

## Verification

Fetch one raw skill file to confirm the tree still matches what skills.sh indexed. The path below is skills/quick-game/SKILL.md on branch main, and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/playableintelligence/game-creator/main/skills/quick-game/SKILL.md | head -20
```

A response opening with `name: quick-game` and a description confirms the skill content is live. Then re-run the install for your agent and confirm the command set is registered:

```bash
npx skills add playableintelligence/game-creator -a claude-code
```

If the plugin form is what you installed, check that `/game-creator:quick-game` autocompletes in the agent before running the longer pipelines.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| game-designer | Pass | Pass | Pass |
| game-3d-assets | Pass | Warn | Warn |
| qa-game | Pass | Pass | Pass |
| use-template | Pass | Pass | Pass |
| retrodiffusion | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 4, 2026: 31,774 combined installs across 31 indexed listings; 355 GitHub stars; no LICENSE file; last pushed 2026-11-03. Counts drift over time.
- No LICENSE file exists at the repository root, while the README License section states MIT. Treat the terms as unresolved until the file lands.
- The README warns that games using `@strudel/web` for audio must carry an AGPL-3.0-compatible licence, and the tech stack table lists Strudel.cc as AGPL-3.0.
- game-3d-assets carries a Socket Warn and a Snyk Warn in the sampled set.
- The pipeline assumes Node, Vite 7 and Playwright are installed locally; the QA subagent runs headless Chromium.
- Monetization and 3D generation reach outside the repo: Play.fun registration needs its MCP server, worldlabs needs a WLT_API_KEY, and retrodiffusion is a paid API.

## Related

- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with quick-game when you want to see whether the toolchain works on your machine. It skips assets, audio, deploy and monetization, so failures are easy to attribute.
- Keep per-run cost down by using viral-game for a throwaway prototype and make-game for anything you intend to iterate on across sessions.
- Read the architecture validator output before editing by hand. The EventBus, GameState and Constants rules are what make the later add-feature runs cheap.
- Do the deploy step last and separately. game-deploy validates before and after publishing, which is easier to read when nothing else is running.
- Pin your own copy if you depend on a specific template. The repo moves fast, and both templates are copied, not generated, so drift changes your scaffold.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
