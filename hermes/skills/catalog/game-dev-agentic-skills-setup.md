---
title: "Game Dev Agentic Skills - Godot and Bevy Suite"
description: "thedivergentai/game-dev-agentic-skills: 41.7K combined installs. 184 LGPL-3.0 game dev skills for Godot 4.7+ and Bevy 0.20, one path at a time."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/game-dev-agentic-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "godot", "bevy", "gamedev"]
---

# Game Dev Agentic Skills - Setup Guide

**Source:** [thedivergentai/game-dev-agentic-skills](https://www.skills.sh/thedivergentai/game-dev-agentic-skills) via skills.sh - 41.7K combined installs across 100 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [thedivergentai/game-dev-agentic-skills](https://github.com/thedivergentai/game-dev-agentic-skills) - 924 stars, LGPL-3.0, branch main, last pushed 2026-10-16; 184 skill directories under `skills/`, each with a `SKILL.md` and most with a `references/` or `scripts/` folder beside it, plus a `skills_index.json` that lists the same 184 entries

**Category:** Game development knowledge for agents: Godot 4.7+ domain skills, genre blueprints, and a Bevy 0.20 parity track

**Quality Tier:** 🟢 Green - all three sampled listings pass every auditor (Gen Agent Trust Hub, Socket and Snyk) and the repository ships an LGPL-3.0 LICENSE file

Game Dev Agentic Skills is published by Divergent AI and described in its own README as an agent library for Godot 4.7+ and Bevy 0.20+. The organising idea is long term memory for game work: each skill holds the concentrated part of an engine topic that a base model does not reliably know, written for an agent that is about to make a design or implementation choice rather than for a human reading a tutorial.

The suite is large and deliberately hierarchical. Godot work starts at `godot-master`, which orchestrates the domain skills through architectural workflows, anti-pattern catalogues and performance budgets. Bevy work starts at `bevy-master` on the same pattern, with dedicated parity skills. Around the two hubs sit domain skills (`godot-2d-physics`, `godot-ui-theming`, `godot-save-load-systems`), genre blueprints (`godot-genre-roguelike`, `godot-genre-metroidvania`, the 27 blueprint set the publisher advertises), and persona skills that the publisher names Analyst, Auditor and Builder.

## Installation

The README opens with a warning that shapes the whole install: choose one path, because installing every skill at once floods the agent with metadata for 184 skills and produces what the author calls a Context Storm. The documented entry points are the two engine hubs:

```bash
npx skills add thedivergentai/Game-Dev-Agentic-Skills/skills/godot-master
npx skills add thedivergentai/Game-Dev-Agentic-Skills/skills/bevy-master
```

A single domain skill is the narrower option, and the README recommends it whenever you already know which skill owns the work:

```bash
npx skills add thedivergentai/Game-Dev-Agentic-Skills/skills/godot-characterbody-2d
npx skills add thedivergentai/Game-Dev-Agentic-Skills/skills/godot-inventory-system
```

The installation rubric adds the flags and the verification step. `-g` installs globally into the shared store at `~/.agents/skills/`, `-a` names the client, and `-y` skips the prompt:

```bash
npx skills add thedivergentai/Game-Dev-Agentic-Skills/skills/godot-master -g -a claude-code -y
npx skills list -g -a claude-code
```

Restart the host agent afterwards, because most clients read skill directories once at session start. The README also documents a clone route for agents that read files directly: query `skills_index.json`, then read `skills/<name>/SKILL.md`. For a Hermes profile that is the simplest path, since the profile reads its own skills directory:

```bash
git clone --depth 1 https://github.com/thedivergentai/game-dev-agentic-skills.git /tmp/gdas
cp -r /tmp/gdas/skills/godot-master ~/.hermes/profiles/corpusiq/skills/
```

Do not use the `--all` flag on this repository. The README marks it an instant no, and the reason is mechanical: 184 skills of metadata is more than most routing layers can hold, and the useful part of the suite is one hub plus the handful of domain skills a project actually needs.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| godot-master | 5,109 | The Godot 4.7+ orchestrator: starting a project, designing architecture, building entity and component systems, debugging physics or performance, choosing between 2D and 3D, planning multiplayer, optimizing draw calls, porting platforms, migrating 4.6 to 4.7. |
| godot-shaders-basics | 707 | Shader work past the first tutorial: batch-safe hitflash, alpha scissor foliage and dissolve, screen space post effects, depth reconstruction, triplanar mapping, instance uniforms. |
| godot-2d-animation | 690 | 2D animation with AnimatedSprite2D and skeletal cutout rigs: sprite frame animation, procedural squash and stretch, bone hierarchies, frame perfect timing. |
| godot-ui-theming | 634 | Theme resources, StyleBoxes, custom fonts and theme overrides: consistent UI styling, theme inheritance, dynamic theme switching, dark mode, font variations. |
| godot-gdscript-mastery | 632 | GDScript landmines: static typing opcodes, signal up and call down, unique names and onready lifecycle, Callable bind and unbind, await sequences, typed collections, safe Dictionary iteration. |
| godot-particles | 626 | GPU particle systems with GPUParticles2D and GPUParticles3D: explosions, magic effects, weather, trails, gradients, sub-emitters, custom particle shaders. |
| godot-save-load-systems | 624 | Save and load systems: JSON or binary serialization, the PERSIST group pattern, versioning and migration, player progress, settings, error recovery. |
| godot-testing-patterns | 609 | GdUnit4 decisions: unit versus scene versus CI gates, headless runners, snapshot tests, mocked networks, validating signals and physics without assert catalogues. |
| godot-characterbody-2d | 547 | CharacterBody2D work: platformer movement with coyote time and jump buffering, top-down and tank controls, one-way platforms, state machines for players, NPCs and enemies. |
| godot-camera-systems | 547 | 2D and 3D cameras: smooth following, trauma based shake, deadzones and drag for platformers, look-ahead prediction, camera transitions. |
| godot-3d-world-building | 546 | 3D level design with GridMap and MeshLibrary, CSG geometry, occlusion, runtime GridMap builders. Routes sky, fog and Environment recipes to godot-3d-lighting. |
| godot-signal-architecture | 543 | Signal driven architecture: typed signals, signal chains, one-shot connections, AutoLoad event buses, decoupling nodes. |
| godot-input-handling | 531 | InputMap actions, InputEvent processing, controller support, rebinding, deadzones, input buffering, gamepad and accessibility features. |
| godot-ui-containers | 529 | Responsive layouts with Container nodes: size flags, anchors, split containers, virtual list pooling, stretch shrink previews, dynamic layouts. |
| godot-project-foundations | 529 | Project organization: feature based folders, naming conventions, snake_case files, PascalCase nodes, scene unique names, gitignore practice. |
| godot-composition | 528 | The composition pattern for gameplay entities: player controllers, NPCs, enemies, weapons and hitboxes built as Has-A relationships. |
| godot-2d-physics | 523 | 2D physics: collision layers and masks, Area2D triggers, raycasting, PhysicsDirectSpaceState2D queries, line of sight, manual physics queries. |
| godot-resource-data-patterns | 522 | Data oriented design with Resource and RefCounted classes: item databases, character stats, typed arrays, serialization, nested resources, caching. |
| godot-combat-system | 517 | Combat systems: hitbox and hurtbox architecture, damage data, health components, combat state machines, combos, cooldowns, damage popups. |
| godot-state-machine-advanced | 514 | Hierarchical finite state machines and pushdown automata: state stacks, sub-states, transition validation, context passing for layered AI behavior. |
| godot-procedural-generation | 514 | Procedural content: dungeons, terrain, loot and levels through FastNoiseLite, random walks, BSP trees, wave function collapse and seeded randomization. |

The remaining 79 indexed listings range from 125 to 512 installs.

The threshold cuts through the middle of the suite rather than the bottom. Above it sit the hub, the systems skills that most projects touch, and the foundational genre-adjacent pieces; below it sit the genre blueprints (`godot-genre-roguelike` at 399, `godot-genre-rts` at 279), the platform skills (`godot-platform-mobile` at 453, `godot-platform-console` at 287), the migration skills (`godot-adapt-2d-to-3d` at 265, `godot-adapt-mobile-to-desktop` at 254), and the three personas (`godot-auditor` at 228, `godot-analyst` at 165, `godot-builder` at 180). Those are the ones to install by name when a project needs them, since each is a single `SKILL.md` under `skills/`.

## Why This Matters for Hermes Agents

Game engines are a domain where a general model is confidently wrong in expensive ways. Godot 4.7 brought AreaLight3D, HDR output and a new Asset Store, and an agent writing from older training data produces code that looks plausible and fails at import. The density of these skills is aimed at exactly that gap: the README's phrase is knowledge delta, the distance between what a base model already knows and what a senior engine developer knows from shipping.

The hierarchy is the part worth copying into other domains. A single hub skill carries the architecture, the anti-pattern list and the performance budget, and it routes into domain skills for specifics. That keeps the always-resident context small while leaving depth one read away, which is the same trade a Hermes skill library makes when it splits a large `SKILL.md` into references.

Some of the skills are unusually concrete for a prompt library. `godot-agent-vision` gives an agent eyes on the editor: a cross platform screenshot CLI that writes budgeted WebP, plus a rubric of roughly 237 micro-receptors covering hierarchy, contrast, typography, affordance, spacing, color and motion, used to score what the agent just rendered. `godot-monte-carlo-balancer` builds a Rust and rayon simulation lab that extracts live game data, simulates playstyles from AFK to pro, and emits win rate and economy verdicts with confidence intervals. Both turn a subjective judgement into a measurement, which is the only kind of judgement an agent can report honestly.

## Usage

| You say | What happens |
|---|---|
| "Start a new Godot 4.7 project with a sane folder layout" | `godot-master` takes the architecture path and applies the naming and structure rules from `godot-project-foundations`, then routes gameplay work to domain skills. |
| "My platformer character feels floaty" | `godot-characterbody-2d` supplies coyote time, jump buffering and variable jump height patterns, plus the state machine shape the movement needs. |
| "Why is this scene dropping frames when the particles fire?" | `godot-master` covers performance budgets and profiling, and hands particle specific work to `godot-particles` for emission and sub-emitter settings. |
| "Add save files that survive a version update" | `godot-save-load-systems` provides serialization, the PERSIST group pattern, versioning and a migration path. |
| "Write the collision and trigger logic for a boss arena" | `godot-2d-physics` covers layers, masks, Area2D triggers and direct space state queries; `godot-combat-system` adds hitbox and hurtbox structure. |
| "Is the UI readable and does it look like a template?" | `godot-agent-vision` captures the viewport and scores it against the taste rubric, so the verdict names contrast, spacing and hierarchy rather than saying it looks off. |
| "This level is unfair after the mid game" | `godot-monte-carlo-balancer` simulates playstyles against real game data and reports win rates with confidence intervals before any tuning. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/thedivergentai/Game-Dev-Agentic-Skills/main/skills/godot-master/SKILL.md
```

After a clone, confirm the tree and the index agree and that the hub skill really is the orchestrator:

```bash
git clone --depth 1 https://github.com/thedivergentai/game-dev-agentic-skills.git /tmp/gdas
ls -d /tmp/gdas/skills/*/ | wc -l
python3 -c "import json;print(len(json.load(open('/tmp/gdas/skills_index.json'))))"
head -4 /tmp/gdas/skills/godot-master/SKILL.md
```

Both counts should print 184. The `head` output should show `name: godot-master` and a description that names itself the primary entry point for Godot development tasks, with the Godot 4.7 keyword list. Then check that an installed copy kept its references and scripts:

```bash
ls ~/.hermes/profiles/corpusiq/skills/godot-master
ls ~/.hermes/profiles/corpusiq/skills/godot-master/references | head -5
```

`godot-master` ships a `references/` directory and a `scripts/` directory beside `SKILL.md`. A copy that lands only the Markdown file loses the evidence the hub cites, which is the usual reason a hub skill reads as vague after installation.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| godot-master | Pass | Pass | Pass |
| godot-shaders-basics | Pass | Pass | Pass |
| godot-2d-animation | Pass | Pass | Pass |

Every sampled listing passes all three auditors, which is the cleanest result of the packs reviewed for this catalogue. That verdict covers skill text, not the engine work an agent does with it: the instructing files describe Godot APIs, and the agent applies them to your project.

The repository is not Markdown only. `godot-master` and other skills ship `scripts/` directories, `godot-agent-vision` documents a host screenshot CLI, `godot-monte-carlo-balancer` describes a Rust simulation binary, and the repository has a top level `scripts/generate_star_history.py`. Those run only when an agent or a human invokes them, but they do run processes on your machine, so read a skill's scripts before granting a project shell access. The version 0.1.1 release notes also describe a license gate: asset bytes are copied only when you pass a real licence note and `--allow-assets`, which is the right default for a suite that can pull third party art.

The licence itself deserves a read. The project is LGPL-3.0 over the skill library, and the README explains the intent directly: improvements to the library stay open, while games you build with the skills can be commercial and closed source. If you plan to fork or vendored-copy skills into a product, that distinction decides what you owe back.

## Limitations

- Snapshot data, verified 2026-11-03: 41,716 combined installs across 100 indexed listings; 924 GitHub stars; LGPL-3.0; last pushed 2026-10-16. Counts drift over time.
- skills.sh indexes 100 listings while the repository ships 184 skill directories. The 79 listings below the 514 install threshold, and the 84 skills with no indexed listing at all, only exist for you as files in the cloned tree.
- Two indexed rows, `godot-mcp-scene-builder` at 134 and `godot-mcp-setup` at 125, carry Bevy 2D sprite animation descriptions that do not match their names. Treat their metadata as a publishing error and read `SKILL.md` before relying on either.
- The suite is large enough to damage an agent that installs it wholesale. The README forbids `--all` for this reason, and `godot-master` alone is described as dense at roughly 15k tokens, so one hub plus a few domain skills is the workable shape.
- The library targets Godot 4.7+ and Bevy 0.20+. Code written against 4.5 or earlier will not line up with the API guidance, and the migration skills cover the hop forward rather than backward compatibility.
- LGPL-3.0 is copyleft over the skill library. Using the skills to build and ship a closed source game is explicitly allowed; modifying and redistributing the library carries obligations.

## Related

- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup)
- [OpenUI Skill - Generative UI Setup](/hermes/skills/catalog/openui-setup)
- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [PixiJS Skills - 2D WebGL and WebGPU Rendering Suite Setup](/hermes/skills/catalog/pixijs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `godot-master` and stop there until a task actually needs more. It routes to domain skills by name, and the routing works when the target skill is not installed as a clear gap rather than a silent wrong answer.
- Read the anti-pattern catalogue in the hub before accepting generated code. Most Godot agent failures are patterns the catalogue already names, from typed array slop to duplicated materials breaking batching.
- Pair `godot-agent-vision` with any UI work. A rubric score is a checkable claim, and it stops the agent from declaring a layout finished because the code compiled.
- Keep one engine per project context. The README is explicit that Godot work starts at `godot-master` and Bevy work at `bevy-master`, with no product wide master, so a mixed session blurs the API surface.
- Check the licence gate before letting an agent pull assets. The 0.1.1 notes make a real licence note a precondition for copying asset bytes, and skipping it is how a prototype acquires provenance debt.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
