---
title: "Roblox Brain - Roblox Studio Development Skills Setup"
description: "Roblox Brain: 61.6K combined installs. TabooHarmony's MIT library teaches coding agents 29 Roblox Studio skills: Luau, gameplay, design and tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/roblox-brain-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "roblox studio", "luau", "game development"]
---

# Roblox Brain - Setup Guide

**Source:** [tabooharmony/roblox-brain](https://www.skills.sh/tabooharmony/roblox-brain) via skills.sh - 61.6K combined installs across 37 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [TabooHarmony/roblox-brain](https://github.com/TabooHarmony/roblox-brain) - 143 stars, MIT License (`LICENSE`), branch main, last commit 2026-10-14; skills-only tree with 29 skill directories in four libraries at `skills/core/`, `skills/gameplay/`, `skills/design/` and `skills/tools/`, each holding `SKILL.md` plus `references/full.md`, alongside `scripts/` (skill, API drift and source URL validators), `tests/` and `.github/workflows/ci.yml`

**Category:** Roblox Studio game development knowledge for coding agents, from Luau and server authority through UI, monetization and publishing

**Quality Tier:** 🟡 Beta - FAILS on roblox-testing (Gen Agent Trust Hub and Snyk) with the other five samples clean; MIT, 143 stars, 29 directories against 37 indexed listings

roblox-brain is a skills-only repository from the publisher TabooHarmony, aimed at the gap every general coding model has with Roblox: Luau instead of TypeScript, Studio and the DataModel instead of a filesystem, server authority instead of trust, and DataStore budgets instead of a database. Nothing here is a plugin, an npm package or a build system. It is markdown, 29 skill directories deep, written against Creator Hub documentation and reviewed on a release cadence that reached v2.3.1 on 2026-10-14.

The suite is organised into four installable libraries: core (10 skills covering Luau, architecture, networking, security, data and performance), gameplay (10 covering building, physics, NPCs, camera, input, GUI, effects, lighting, audio and localization), design (5 covering game design, player psychology, growth, analytics and monetization) and tools (4 covering Studio MCP, external tooling, Open Cloud and a publish checklist). Each skill follows progressive disclosure: a `SKILL.md` entry point capped under 3,000 characters with a quick reference, and a longer `references/full.md` the agent opens only when it needs examples and API detail. The release history is substantive rather than cosmetic, with 2.3.0 adding mobile-first GUI guidance, gamepad focus ownership, first-session onboarding traces and subscription receipts, and 2.3.1 correcting an engine limit that the architecture notes had wrong.

## Installation

The README documents the `skills` CLI as the primary route. All 29 skills:

```bash
npx skills add TabooHarmony/roblox-brain
```

One library at a time, which is the recommended split in the README's own skill-set table:

```bash
npx skills add TabooHarmony/roblox-brain/skills/core
# or: gameplay, design, tools
```

One named skill:

```bash
npx skills add TabooHarmony/roblox-brain --skill roblox-building
```

The README's manual route is a directory copy, and it is explicit that the copy has to include the reference file. Copying only `SKILL.md` leaves `references/full.md` behind, which is where the examples and API tables sit:

```bash
cp -r skills/gameplay/roblox-gui ~/.hermes/profiles/corpusiq/skills/
```

That last path is the repository's own manual form (its example targets `~/.claude/skills/`), pointed at a Hermes profile directory. The repository also states that `.codex/skills/` and `.cursor/skills/` work the same way, so any client with a documented skills directory can take a copied tree.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| roblox-building | 2,560 | Geometry, maps, props and generated assets, plus inspecting Toolbox assets before replacing them and verifying a build in Studio. |
| roblox-animation-vfx | 2,499 | Animations, particles, beams, trails, tweens, camera shake and effect composition, with readability and performance checks in play. |
| roblox-studio-mcp | 2,407 | Editing scripts and scenes through Studio MCP, routing calls to a specific Studio instance with `studio_id`, plus playtesting and screenshots. |
| roblox-lighting | 2,359 | Lighting, atmosphere, day/night cycles and post-processing, with `LightingStyle` and `PrioritizeLightingQuality` guidance. |
| roblox-gui | 2,339 | Menus, HUDs, shops and dialogs that hold up on phones, tablets, desktop and console, including layout, reflow and visual verification. |
| roblox-luau-patterns | 2,240 | Module boundaries, object lifecycles, signals, task scheduling, fallible calls, cleanup and metatable behaviour. |
| roblox-performance | 2,222 | Profiling and fixing low FPS, memory, network load and slow phones, including Parallel Luau, pooling, streaming and allocation costs. |
| roblox-architecture | 2,200 | Feature ownership, runtime location, dependencies, startup order and client/server authority, traced from input through remotes to saved state. |
| roblox-security | 2,161 | Anti-exploit audits: authority models, remote abuse, economy and purchase hardening, DataStore flows, bans and sandboxed scripts. |
| roblox-audio | 2,148 | Playback, spatial sound, music systems, sound effects, SoundGroups and dynamic audio effects. |
| roblox-npc-ai | 2,135 | NPCs, bots and enemies: pathfinding, state machines, line of sight, spawning and AI update loops. |
| roblox-luau-types | 2,120 | Type annotations, generics, narrowing, inference, strict mode, sealed tables and module type exports. |
| roblox-networking | 2,099 | RemoteEvents and RemoteFunctions: argument validation, rate limits, server authority, shared clocks and exploit resistance. |
| roblox-luau-core | 2,081 | Luau syntax, tables, control flow, string patterns, scope, closures and the traps hit by code ported from JavaScript or Python. |
| roblox-monetization | 2,071 | Game Passes, Developer Products, receipts, subscriptions, private servers and policy checks. |
| roblox-physics | 2,051 | Vehicles, ragdolls, projectiles, elevators, constraints, forces and network ownership, including line forces and IK controls. |
| roblox-data | 2,048 | Player persistence with DataStore and ProfileStore: schemas, migrations, retries, session ownership and data budgets. |
| roblox-publish-checklist | 2,015 | Change-scoped release gates, evidence capture, dashboard checks and rollback readiness before a publish. |
| roblox-tooling | 1,981 | Rojo, Wally, pesde, Selene, StyLua, Lune, Rokit, luau-lsp, package manifests and CI. |
| roblox-analytics | 1,976 | AnalyticsService events, economy tracking, funnels, first-session traces and event taxonomy under the documented limits. |
| roblox-camera | 1,957 | Camera types, CFrame math, screen raycasts, first and third person, shoulder views, cutscenes and screen shake. |
| roblox-cloud | 1,908 | Open Cloud REST APIs: API keys, OAuth 2.0, webhooks, scopes, token lifecycle and experience secrets. |
| roblox-input | 1,904 | Touch, gamepad, keyboard, mouse and motion input, on-screen action buttons, action binding and gamepad focus ownership. |
| roblox-server-data | 1,841 | OrderedDataStore leaderboards, MessagingService, MemoryStore, global state and cross-server coordination. |
| roblox-localization | 1,780 | Translation tables, locale handling, auto-translation, region detection and audience-specific text filtering. |
| roblox-growth-design | 1,743 | Discovery, positioning, retention, experiment design, LiveOps, thumbnail tests and launch packaging. |
| roblox-collaboration-mode | 1,544 | Sets initiative before any Roblox task: when to act, when to warn, and which decisions need the user. |
| roblox-game-design | 1,462 | Core loops, tutorials, level pacing, economy structure, game feel and curation. |
| roblox-player-psychology | 1,373 | First-minute psychology, reward schedules, streaks, pricing, RNG and pity systems, and community loops. |
| roblox-code-review | 669 | No in-tree skill. CHANGELOG 2.0.0 removed it as a standalone router and sends review work to the domain skill for the change. |

The remaining 7 indexed listings range from 145 to 484 installs.

## Why This Matters for Hermes Agents

A general model asked to write Roblox code fails in a specific and expensive way: it treats the client as trustworthy, writes DataStore calls without session ownership, and reaches for web idioms that Luau does not have. The core library exists to prevent that class of mistake before the first commit, which is cheaper than a code review after a launch.

The design of the suite assumes Hermes is not a monolith. Twenty-nine independently routed skills, with descriptions that trigger on fixing and auditing as well as writing, mean the agent loads `roblox-gui` for a mobile overlap and `roblox-networking` for a remote validation question, instead of dragging a single enormous Roblox document into every turn. The `when_to_use` field added in 2.3.0 exists for exactly that routing, with symptom phrases like "data not saving" and "UI overlaps on mobile".

The tools library is the part that touches the Agent itself rather than the game. `roblox-studio-mcp` covers driving Studio over MCP with per-instance routing, `roblox-tooling` covers the external chain from Rojo to CI, and `roblox-publish-checklist` converts a release into evidence-backed gates. For a Hermes setup that builds and ships Roblox experiences on a schedule, that combination is the difference between a build that is verified and one that is merely pushed.

The honest framing is that this is documentation, not automation. It will not stop an agent from writing unsafe code, and it cannot verify a place file. It raises the floor of what the agent knows before it writes.

## Usage

| You say | What happens |
|---|---|
| "Build a shop menu that works on phones" | The mobile-first GUI order from `roblox-gui` applies: smallest landscape phone first, safe-area containers, measured placement, then a check against the state combinations that cause overlaps. |
| "My saves are not persisting after a restart" | `roblox-data` covers session ownership, migrations and retries, and `roblox-server-data` picks up when the state has to cross servers. |
| "Players are duplicating currency" | `roblox-security` treats the client as compromised and hardens the purchase and economy path, with `roblox-networking` adding remote validation and rate limits. |
| "The game runs at 20 FPS on low-end phones" | `roblox-performance` profiles the hot path first, then applies pooling, streaming and allocation guidance rather than guessing at micro-optimizations. |
| "Add a game pass that grants once, even after a crash" | `roblox-monetization` requires a durable, idempotent grant before the receipt is acknowledged, and treats subscriptions and dynamic prices as separate paths. |
| "Wire up Rojo and run lint in CI" | `roblox-tooling` uses the project's existing package manager or Rokit, sets pins for Rojo and Selene, and covers realm conflicts and CI result checks. |
| "We are shipping tonight" | `roblox-publish-checklist` runs change-scoped release gates with evidence, dashboard checks and rollback readiness before the update goes out. |

## Verification

Confirm the raw entry point is reachable on main before you install, using paths from the repository tree. All four below returned 200 when this guide was written:

```bash
for p in skills/core/roblox-architecture skills/core/roblox-security \
         skills/tools/roblox-publish-checklist skills/gameplay/roblox-gui; do
  curl -s -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/TabooHarmony/roblox-brain/main/$p/SKILL.md"
done
```

That loop doubles as the drift check the Limitations section describes. Swap in an indexed name that has no directory, such as `skills/core/roblox-testing`, and the same URL returns 404, which is how you separate a live skill from a stale listing.

After installing, check that the reference file came along with the entry point, since the copy route is where installs silently lose detail:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/roblox-gui/
head -12 ~/.hermes/profiles/corpusiq/skills/roblox-gui/SKILL.md
```

A healthy copy shows `SKILL.md` and a `references/` directory holding `full.md`. The frontmatter should name the skill, carry a `description`, an optional `when_to_use`, a `last_reviewed` date and a non-empty `sources` list, which is the schema `AGENTS.md` documents and `scripts/validate_skills.py` enforces.

Review a `SKILL.md` before you install it: read the description and `when_to_use` to see what will trigger it, then skim the Quick Reference and open `references/full.md` for any claim about an engine limit or API signature. The repository ships its own validators (`scripts/validate_skills.py`, `scripts/verify_source_urls.py`, `scripts/verify_api_drift.py`), and running them from a clone needs only `pyyaml`, which is the single line in `requirements.txt`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

The one failure in the sample is roblox-testing, the lowest-installed listing in the pack, and it fails two independent auditors rather than one: Gen Agent Trust Hub and Snyk both return Fail, while Socket passes it. That row leads the table below.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| roblox-testing | Fail | Pass | Fail |
| roblox-building | Pass | Pass | Pass |
| roblox-animation-vfx | Pass | Pass | Pass |
| roblox-studio-mcp | Pass | Pass | Pass |
| roblox-lighting | Pass | Pass | Pass |
| roblox-gui | Pass | Pass | Warn |

The other five sampled skills pass Gen Agent Trust Hub and Socket; Snyk adds one warn, on `roblox-gui`, and no second failure.

What the failure means in practice. A skill in this repository is markdown: `SKILL.md` plus `references/full.md`, no executable payload, no installer, no postinstall script, so a Fail cannot be about code that runs at install time. Agents read skills as instructions, which makes instruction content the attack surface, and a dual Fail is the pattern scanners raise when a document contains commands, fetched URLs or text that reads like an override. This pack records verdicts only, not finding text, so read the roblox-testing page on skills.sh and the file itself before installing by name. The mitigating fact is mechanical: `roblox-testing` has no directory on main (the raw path returns 404) and sits below the install threshold at 145, so a full-repository or library install does not fetch it, while `npx skills add TabooHarmony/roblox-brain --skill roblox-testing` would.

For the rest of the suite the risk profile is low and the surface is your own Studio session. `roblox-studio-mcp` instructs an agent to drive Studio over MCP, which can edit scripts and scenes in a real place, and `roblox-cloud` covers Open Cloud API keys, OAuth and webhooks. Keep keys out of scripts (the 2.0.0 notes already push experience secrets through `HttpService:GetSecret`), and test MCP edits on a copy of the place rather than the live one.

## Limitations

- Snapshot data, verified 2026-10-29: 61,628 combined installs across 37 indexed listings; 143 GitHub stars; MIT License; last pushed 2026-10-14. Counts drift over time.
- The indexed count and the tree disagree by eight. skills.sh indexes 37 listings, the repository has 29 skill directories, and every one of the eight absent names returns 404 on main, including the sample that fails security. CHANGELOG 2.0.0 documents the removal of two of them as standalone skills (`roblox-code-review` and `roblox-ui-design`), so treat the listing as partly historical and install from the tree.
- All eight are index-only, and one of them, `roblox-code-review` at 669 installs, sits above the pack threshold, so this guide's table carries a row for a skill you cannot install. CHANGELOG 2.0.0 says its review job moved to the domain skill for the change rather than being carried over as a router.
- The entry points are capped under 3,000 characters by design, so the guidance an agent sees first is a quick reference. Anything that depends on the detail, from engine limits to API signatures, sits in `references/full.md` and is only loaded on demand. Copying `SKILL.md` alone silently halves the skill.
- Single publisher. 143 stars and one maintainer behind all 29 skills, so accuracy, review cadence and security response rest on that person rather than an organisation.
- Accuracy is pinned to Creator Hub documentation, and the release notes show the cost of that: 2.3.1 exists to correct a wrong `NumberValue` ceiling in the architecture notes. 24 of the 29 entry points carry `last_reviewed: 2026-10-14`, and the rest date from 2026-07-26 to 2026-10-02, so assume some engine claims trail the docs between releases and verify anything load-bearing against the source link in the frontmatter.

## Related

- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)
- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup)
- [Three.js Game Skills - 3D Game Development Suite Setup](/hermes/skills/catalog/threejs-game-skills-setup)
- [Layer Skills - AI Game Asset Creation Suite Setup](/hermes/skills/catalog/layerai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `roblox-collaboration-mode` first on any autonomous Roblox task. It sets the initiative level before domain work starts, which is what stops an agent from rewriting a networking layer you only asked it to read.
- Install one library at a time. Core alone covers most backend work, and a smaller installed set means fewer competing descriptions when the agent chooses a skill.
- Copy directories, not files. `references/full.md` is where the API tables live, and a `SKILL.md` on its own is a summary of a skill you did not really install.
- Run the raw URL check in Verification before trusting an install command with an indexed name. The index carries at least eight names with no directory behind them.
- Keep the publish checklist for anything that ships, and read its dashboard requirements before the release window rather than during it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
