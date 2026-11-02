---
title: "Awesome GameDev Skills - 77 Game Engine Agent Suite"
description: "gamedev-skills/awesome-gamedev-agent-skills: 581.3K combined installs. Seventy-seven game-dev skills and a router for twelve engines, Godot to Roblox."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-gamedev-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "godot", "unity", "game engines"]
---

# Awesome GameDev Skills - Setup Guide

**Source:** [gamedev-skills/awesome-gamedev-agent-skills](https://www.skills.sh/gamedev-skills/awesome-gamedev-agent-skills) via skills.sh - 581.3K combined installs across 78 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) - 6,525 stars, Apache-2.0 with `LICENSE` and `NOTICE` in the root, branch main, last pushed 2026-10-28; 78 `SKILL.md` folders: 77 skills under `skills/<group>/<name>/` plus the dispatcher at `router/SKILL.md`

**Category:** Game development for agents: Godot, Unity, Unreal, Phaser, shaders, level design and publishing

**Quality Tier:** 🟢 Green - 6,525 stars under Apache-2.0, a validator and a regression suite in the repo, and all five sampled listings pass all three audits

The suite is maintained by Abhishek Barali and it puts 77 skills plus a router behind one install, grouped into nine categories. The engine groups carry Godot 4.7 (16 skills), Unity 6.3 LTS 6000.3 (8), Unreal Engine 5.8 (6), the web trio of Phaser 4.2, PixiJS 8.22 and three.js r186 (6), and a long tail of Ebitengine v2.10.5, Bevy 0.20, pygame-ce 2.5.8, Love2D 11.5, Defold 1.14.0 and Roblox (13). The remaining groups cut across engines: 15 disciplines from game feel to save systems, 9 genre templates, and 4 workflow skills for jams, prototyping, Steam and itch.

The router is what makes the size usable. On each request it fingerprints the project from its files, a `project.godot` for Godot and a `*.uproject` for Unreal among them, reads the task out of the request, and names the smallest set of skills to read before acting, engine basics first and then the concept and any genre glue. Engine choice is exclusive and the other three groups are additive, so a request to add a double jump to a Godot player loads `godot-2d-movement` and `platformer` and nothing else. Every skill is written from primary engine documentation, pinned to a stated release, and checked by `scripts/validate-skills.py`, which is covered by its own regression tests in `tests/`.

## Installation

The README's one command installs the router and all 77 skills into the agent it detects. It needs Node.js 22.20 or later:

```bash
npx skills add gamedev-skills/awesome-gamedev-agent-skills
```

Add `--list` to preview the skill list without installing, `-g` to install for every project, or `-a <agent>` to target one tool (`-a cursor`, `-a claude-code`, `-a gemini-cli`). A subset is installed by repeating `--skill`:

```bash
npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill godot-tilemap --skill platformer
```

The repository is also a Claude Code plugin marketplace, so the same files install through Claude's own commands. The `gamedev` plugin is everything; each category is its own plugin if you want less:

```bash
claude plugin marketplace add gamedev-skills/awesome-gamedev-agent-skills
claude plugin install router@awesome-gamedev-agent-skills
claude plugin install godot@awesome-gamedev-agent-skills
```

Swap `godot` for `unity`, `unreal`, `ebitengine`, `web-engines` or `other-engines`, and add `disciplines`, `genres` or `workflows` as needed. Install `router` either way, because the engine bundles do not carry it.

The manual route is a directory copy, which is the one to use for a Hermes profile since Hermes appears in none of the compatibility tables:

```bash
git clone --depth 1 https://github.com/gamedev-skills/awesome-gamedev-agent-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R awesome-gamedev-agent-skills/router ~/.hermes/profiles/corpusiq/skills/router
cp -R awesome-gamedev-agent-skills/skills/godot/godot-tilemap ~/.hermes/profiles/corpusiq/skills/
```

The skill folder itself is the unit: `skills/<category>/<name>/`, where `<name>` equals the skill's `name` field, and `references/`, `scripts/` and `assets/` inside it travel with it. `docs/INSTALLATION.md` has the per-agent paths for Claude Code, Codex, Cursor, Windsurf, Cline, Kiro and Oh My Pi.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| game-feel | 12,047 | Juice that makes actions land: screen shake, hit-stop and freeze frames, tweened and eased motion, squash and stretch, knockback, and layered audio-visual feedback, written as engine-neutral techniques that pair with the detected engine's tween, particle and camera APIs. |
| game-ui-ux | 11,878 | Cross-engine HUD and menu work: anchors, resolution scaling, safe areas and focus navigation. |
| level-design | 9,803 | Whitebox and blockout structure, tile and grid layout, pacing. |
| performance-optimization | 9,406 | Profile first, then fix: frame budget, CPU and GPU triage, draw calls, pooling, garbage collection, asset budgets. |
| audio-design | 9,358 | Buses and mixing, adaptive music, SFX, ducking. |
| game-ai | 9,322 | NPC decision-making: finite state machines, behavior trees, steering, pathfinding. |
| save-systems | 9,307 | Serialize and restore game state: formats, slots, versioning, autosave. |
| camera-systems | 9,285 | 2D follow, deadzone and look-ahead with bounds; 3D orbit and first-person; a screen-shake hook for game-feel. |
| procedural-gen | 9,039 | Noise, RNG and seeds, plus grid, dungeon and terrain generation. |
| input-systems | 8,968 | Input architecture: action mapping, rebinding, multi-device, buffering. |
| physics-tuning | 8,814 | Making physics feel right: fixed timestep, mass and drag, continuous collision detection, stability, collision layers. |
| create-game-assets | 8,791 | Art direction and a production pipeline for cohesive sprites, tiles, textures, icons, UI art and 3D assets: lock a visual target, build families, normalize the output, check it inside the game. |
| shader-programming | 8,772 | Cross-engine shader concepts: vertex and fragment stages, UVs, common effects. |
| dialogue-systems | 8,581 | Branching dialogue and narrative: nodes, conditions, variables, with Yarn and Ink. |
| godot-ui-control | 8,522 | Godot `Control` nodes: anchors, containers, themes, focus navigation. |
| router | 8,478 | The dispatcher. Fingerprints the project to exactly one engine, classifies the task, and names the minimal skills to read before writing code. Start here when unsure. |
| godot-animation | 8,424 | `AnimationPlayer`, `AnimationTree` and `Tween`. |
| godot-gdscript | 8,264 | The GDScript language: typing, lifecycle, `@export`, signals, idioms. |
| godot-shaders | 8,254 | The Godot shading language: 2D `canvas_item` and 3D `spatial` shaders. |
| godot-nodes-scenes | 8,213 | The scene tree and node composition: reusable scenes, instancing `PackedScene` at runtime, autoload singletons, and the "node not found" and freed-node errors that follow a wrong split. |

The remaining 58 indexed listings range from 1,046 to 8,200 installs. That tail runs from rpg, godot-physics and prototype-fast just under the line down to roblox-simulator-economy at 1,046, and it holds the genre templates (platformer, roguelike, tower-defense, card-game, visual-novel, survival-crafting, puzzle, fps-shooter), the whole Unity and Unreal engine groups, the web and other-engine groups, and the four workflow skills.

## Why This Matters for Hermes Agents

Game code is the place where an agent's confident guessing costs the most, because the failure is not a wrong answer in chat but a scene that will not open. Engine APIs move between releases: `get_gravity()` and `move_and_slide()` in a Godot 4.7 controller are not the Godot 3 spellings, `CharacterBody2D` replaced `KinematicBody2D`, and Unity's built-in input differs from the Input System package in almost every call. This pack removes the guess by handing the agent a playbook written against a named release, so the first draft it writes is closer to the engine's current idioms than to whatever the model memorised.

The router solves the context problem that a 77-skill pack creates. Loading the whole suite would bury the request in irrelevant engine material; loading one engine skill per request means the agent reads a few thousand tokens of exactly the right thing, and re-routes when the task pivots from the player controller to the save system. That is the same shape as Hermes's own skill routing: a small always-on dispatcher, with the detail in files read on demand.

The discipline and genre layers are the part that generalises beyond games. A skill like `save-systems` or `performance-optimization` states the decision criteria, not just the API, and the genre templates deliberately compose rather than re-teach primitives, which keeps an agent from producing five overlapping explanations of a jump. The assets workflow goes further: it locks a visual target first and normalises every generated family against it, which is the discipline an agent needs before it is allowed to generate a hundred sprites.

Finally the repository is checkable. Skills are validated by a script, that script has regression tests, engine baselines are documented in `docs/VERSION-SUPPORT.md` and re-checked on a dated pass, and the layout is plain Markdown with no build step. An operator can audit what the agent will read before it reads it.

## Usage

| You say | What happens |
|---|---|
| "Add a double jump to my Godot player" | Detects Godot from `project.godot`, loads `godot-2d-movement` for the controller and `platformer` for jump feel, and skips the other 75 skills. |
| "Make an inventory for my Unity RPG" | Loads `unity-scriptableobjects` for the data architecture, `rpg` for the stats and inventory model, and `save-systems` for persistence. |
| "Build a 2D puzzle in Go with Ebitengine" | Loads `ebitengine-game` for the update and draw contract and `puzzle` for board state, rule resolution and undo. |
| "Procedural dungeon roguelike in Godot" | Loads `godot-tilemap`, `procedural-gen` and `roguelike` together: tiling, seeded generation, and grid movement with permadeath and field of view. |
| "Make a cohesive pixel-art player, enemies and tiles" | Loads `create-game-assets` plus the detected engine's importer, locks a visual target, builds the asset families, normalizes the output deterministically and checks the result inside the game. |
| "How should I design save slots?" | Loads `save-systems` alone and answers on formats, slot layout, versioning and autosave rather than on engine APIs. |
| "Publish my game on itch with butler" | Loads `itch-publish` for the project page, channels and `butler` uploads. |

## Verification

Probe the raw files before installing anything. These four paths returned 200 on branch main on 2026-11-02:

```bash
for p in router skills/disciplines/game-feel skills/godot/godot-nodes-scenes skills/workflows/steam-publish; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/gamedev-skills/awesome-gamedev-agent-skills/main/$p/SKILL.md"
done
```

After a clone, count the skills instead of trusting a listing. The tree holds 78 `SKILL.md` files, 77 skills plus the router:

```bash
git clone --depth 1 https://github.com/gamedev-skills/awesome-gamedev-agent-skills.git /tmp/gamedev-skills
find /tmp/gamedev-skills -name SKILL.md -not -path "*/.git/*" | wc -l
head -6 /tmp/gamedev-skills/router/SKILL.md
```

The count should print 78, and the second command should show the router's folded `name:` and `description:` frontmatter, which is what the agent routes on. To confirm the copy landed in a Hermes profile:

```bash
ls ~/.hermes/profiles/corpusiq/skills | wc -l
head -3 ~/.hermes/profiles/corpusiq/skills/router/SKILL.md
```

The repository's own validator is the last check, and the README runs it on every contribution:

```bash
cd /tmp/gamedev-skills && python3 scripts/validate-skills.py
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| game-feel | Pass | Pass | Pass |
| godot-nodes-scenes | Pass | Pass | Pass |
| steam-publish | Pass | Pass | Pass |
| pixijs-rendering | Pass | Pass | Pass |
| roblox-simulator-economy | Pass | Pass | Pass |

All five sampled listings pass all three auditors, with no Warn or Fail to report, and the sample spans a discipline, a Godot engine skill, a publishing workflow, a web engine skill and a Roblox skill. The pack is Apache-2.0 with the `NOTICE` file kept in the root, and the directories that ship code are the ones to read: seven skills carry a `scripts/` folder with nine Python helpers (`check_godot_project.py`, `check_unity_project.py`, `check_defold_project.py`, `check_ebitengine.py`, `check_steam_build.py`, `new_game.py`, `package_macos_app.py`, `asset_report.py`, `build_preview_sheet.py`), and `roblox-simulator-economy` carries Luau balance and economy-math modules. They are project checks and generators run by hand, not hooks, so nothing executes when the files are installed.

The real surface is elsewhere: these skills tell an agent to run engine toolchains on a real project. `godot-export` and `unity-build-pipeline` drive build steps, `steam-publish` walks Steamworks onboarding and downloads the SDK, and `itch-publish` runs `butler`. Grant those commands per project, from a directory you are willing to have rebuilt, and keep the Steam and itch credentials out of the repository, because the skills have no sandbox of their own.

## Limitations

- Snapshot data, verified 2026-11-02: 581,262 combined installs across 78 indexed listings; 6,525 GitHub stars; Apache-2.0; last pushed 2026-10-28. Counts drift over time.
- The table carries the 20 listings at or above 8,213 installs. The other 58 range from 1,046 to 8,200 and are summarised in one line, so the table reads as the popular subset rather than the whole suite.
- Every listing has a folder in the current tree, 78 of 78, so there is no index-to-tree drift to work around. The router is one of those 78 and is not a game-development skill in its own right.
- Engine baselines are pinned to named releases: Godot 4.7, Unity 6.3 LTS 6000.3, Unreal Engine 5.8, Ebitengine v2.10.5 on Go 1.25+, Phaser 4.2, PixiJS 8.22, three.js r186, Bevy 0.20, pygame-ce 2.5.8, Love2D 11.5 and Defold 1.14.0. `docs/VERSION-SUPPORT.md` calls these baselines for new projects, not upgrade targets, so a project on an older release needs the differences checked before the code is pasted in.
- The security sample is 5 of 78 listings. The other 73 are unaudited by that sample, including every Unity and Unreal skill.
- The skills CLI path needs Node.js 22.20 or later, and the validator is a separate Python entry point. Neither Hermes nor any generic agent runtime is named in the compatibility tables, so a Hermes install is a directory copy that you keep updated yourself.

## Related

- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)
- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the router with whatever else you install. The engine bundles do not carry it, and without it the agent picks skills by name recognition, which is exactly the guessing the suite exists to remove.
- When the wrong skill loads, read `router/references/routing-table.md` and `router/references/engine-detection.md` before editing anything. Detection is file-based, so a missing `project.godot` or an unusual folder layout explains most misroutes.
- Install one engine bundle plus `disciplines` rather than all 78 if you work in a single engine. The suite is designed so the categories compose, and leaving the other engines out keeps context for the work you actually do.
- Run `python3 scripts/validate-skills.py` after any local edit to a `SKILL.md`, and read `tests/test_validate_skills.py` if you are changing the rules rather than the content.
- Read `docs/VERSION-SUPPORT.md` before writing code into an older project. The baselines there are dated and engine-specific, and they tell you which release each skill was reviewed against.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
