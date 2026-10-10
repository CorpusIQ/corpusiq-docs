---
title: "Three.js Game Skills - 3D Game Development Suite Setup"
description: "Setup guide for majidmanzarpour/threejs-game-skills - 24.0K combined installs. 9 Three.js skills covering game UI, graphics, and gameplay systems."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/threejs-game-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "three.js", "browser games", "game development"]
---

# Three.js Game Skills - Setup Guide

**Source:** [majidmanzarpour/threejs-game-skills](https://www.skills.sh/majidmanzarpour/threejs-game-skills) via skills.sh - 24.0K combined installs across 9 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) (2,465 stars, MIT; pushed 2026-09-28; skill folders under `skills/`, each self-contained with `SKILL.md` plus references, scripts, and assets)
**Category:** Game Development / Three.js
**Quality Tier:** 🟡 Beta - 2,465-star MIT suite; active Sep 2026; all sampled verdicts Pass

Three.js Game Skills is a nine-skill suite by Majid Manzarpour for building playable, polished Three.js browser games with Codex or Claude Code. One shared pack serves both runners: a director skill routes gameplay, graphics, UI, asset generation, audio, debugging, and release verification so users do not have to pick specialist skills manually.

The suite ships runtime materials, not just instructions. The gameplay skill bundles a Vite + TypeScript + Three.js scaffold with deterministic test hooks and a seeded RNG, and the QA skill includes Playwright templates for smoke tests, visual-regression baselines, and bot playtests. The core skills need no paid API keys; optional Tripo, Gemini, and ElevenLabs keys unlock generated 3D models, images, and audio, with procedural fallbacks when keys are missing.

---

## Installation

```bash
# Install all nine skills for Codex
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex -g -y

# Install all nine skills for Claude Code
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a claude-code -g -y
```

From a cloned checkout, the local installer offers the same targets: `./install.sh --codex`, `./install.sh --claude`, or `./install.sh --all` (add `--force` to overwrite same-named skills; it never removes unrelated skills unless `--prune-managed` is passed).

Where the skills land once installed:

- Claude Code reads skills from `~/.claude/skills` and routes from each `SKILL.md` description; invoke the director with `/threejs-game-director`, or just name it in a prompt.
- Codex discovers global skills in `~/.agents/skills`; each skill's `agents/openai.yaml` supplies a `$skill-name` kickoff prompt. Avoid installing duplicate copies in both root locations.

Optional API keys are only needed for generated assets and go in your shell profile:

```bash
export TRIPO_API_KEY="..."      # threejs-3d-generator (3D models)
export GEMINI_API_KEY="..."     # threejs-image-generator (images)
export ELEVENLABS_API_KEY="..." # threejs-audio-generator (audio)
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| threejs-3d-generator | 2,970 | Tripo API text/image/multiview to 3D: game-ready GLB/FBX models, texturing, rigging, animation |
| threejs-gameplay-systems | 2,810 | Playable loop, mechanics, architecture, input, camera, physics, scoring, and game feel |
| threejs-game-ui-designer | 2,777 | HUDs, menus, overlays, responsive layout, safe areas, icons, touch controls, text fit |
| threejs-aaa-graphics-builder | 2,718 | Premium visuals: models, materials, lighting, VFX, world detail, and render polish |
| threejs-game-director | 2,607 | Main entrypoint: scope, quality bar, specialist routing, continuity, evidence |
| threejs-debug-profiler | 2,590 | Black screens, runtime errors, loading issues, mobile bugs, and performance profiling |
| threejs-qa-release | 2,559 | Production builds, browser and canvas verification, screenshots, mobile checks, release risk |
| threejs-audio-generator | 2,482 | ElevenLabs SFX, music, ambience, voice/TTS, and Three.js audio integration |
| threejs-image-generator | 2,457 | Gemini-generated concept art, textures, skies, icons, logos, and GUI art |

All 9 indexed listings cleared the 500-install table bar and appear above.

## Why This Matters for Hermes Agents

This suite treats verification as a first-class part of game building. Its expected-evidence list includes production builds, real input, screenshots, canvas pixel metrics, supported viewports, and bot playtests, and the director skill keeps a run manifest so the agent can prove what it checked. For agent builders, it is a strong example of a router-plus-specialists pattern: the director preserves scope and art direction while delegating independent work when the runner supports it. It also degrades cleanly: without paid keys or with delegation unavailable, the skills fall back to procedural assets and direct work rather than failing. Everything is packaged inside the skill folders (scaffold, scripts, references), so there is no separate build system to maintain before the agent can start.

## Usage

| You say | What happens |
|---|---|
| Build a premium futuristic tower defense game from scratch | threejs-game-director routes gameplay, graphics, UI, assets, and QA through the full production pass |
| The screenshots look basic, make them premium | threejs-aaa-graphics-builder targets models, materials, lighting, and VFX with a measured visual scorecard |
| The HUD overlaps on mobile screens | threejs-game-ui-designer fixes safe areas, text fit, and touch targets across viewports |
| The game shows a black screen after load | threejs-debug-profiler isolates the runtime or rendering failure |
| Get this game release-ready | threejs-qa-release runs the production build, browser checks, and a release risk report |
| Add a hero spaceship model to the game | threejs-3d-generator produces a game-ready GLB from a prompt when Tripo credentials are available |
| Add hit sounds and an ambience loop | threejs-audio-generator generates SFX and ambience through ElevenLabs and wires them into the game |

## Verification

Confirm the skills landed, then check whether the credential probe sees your optional keys:

```bash
# List installed skills
npx skills list | grep threejs

# Confirm skill files are in place (Claude Code path)
ls ~/.claude/skills/ | grep threejs

# Check which asset-generation keys the director can see (prints SET/MISSING, never key values)
bash ~/.claude/skills/threejs-game-director/scripts/probe_asset_credentials.sh
```

Review the exact instructions before installing: fetch a skill directly, for example `https://raw.githubusercontent.com/majidmanzarpour/threejs-game-skills/main/skills/threejs-3d-generator/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| threejs-3d-generator | Pass | Pass | Pass |
| threejs-gameplay-systems | Pass | Pass | Pass |
| threejs-game-ui-designer | Pass | Pass | Pass |

## Limitations

- Verdicts cover three sampled skills only; the rest of the suite is unaudited here, so re-check each skill's security page on skills.sh before production use.
- Optional paid keys (Tripo, Gemini, ElevenLabs) are needed for generated 3D, image, and audio assets; the core skills run without them using procedural and local assets.
- Provider calls run from local agent tooling, not the browser; never commit API keys or place them in browser-side game code.
- Delegation, background tools, and steering depend on the host runner; installing the skills does not enable API features or change model settings.
- The local installer is a bash script (`install.sh`); on Windows prefer the `npx skills add` path plus the README's PowerShell environment-variable instructions.
- Young suite tracked as Beta (2,465 stars; last pushed 2026-09-28); expect layout churn between releases, and pin a revision when vendoring. MIT license.

- Snapshot data, verified Oct 10, 2026: 23,970 combined installs across 9 indexed listings; 2,465 GitHub stars; MIT; last pushed 2026-09-28. Counts drift over time.

## Related

- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup) - 2D browser game development alternative to the Three.js stack
- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup) - engine-based game building with Godot 4
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup) - motion craft that pairs with the graphics and gameplay skills
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every broad request with threejs-game-director; it pulls in the specialists automatically, so naming each one is unnecessary.
- Missing keys are not blockers: when credentials are absent the director continues with procedural and local assets and reports the limitation.
- Set keys via your shell profile and re-run the credential probe before asset-heavy sessions; the probe sources common profiles the agent process may not inherit.
- For a small fix (a HUD tweak, one bug), skip the full pass: the suite scales verification to the change, so a small fix stays small.
- If the installed `skills` CLI does not support the codex or claude-code targets, install from a cloned checkout with `./install.sh --all`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
