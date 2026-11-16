---
title: "Roblox Agent Skills - Production Roblox Skill Suite"
description: "el4cteo/roblox-skills - 25.5K combined installs across 23 indexed listings: current, secure Roblox and Luau skills for AI agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/roblox-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "roblox", "luau", "game development"]
---

# Roblox Agent Skills - Setup Guide

**Source:** [el4cteo/roblox-skills](https://www.skills.sh/el4cteo/roblox-skills) via skills.sh - 25.5K combined installs across 23 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 118 stars, MIT license, `main` branch, last pushed 2026-11-03, `SKILL.md` files under `skills/<name>/`
**Category:** Roblox game development - architecture, live-ops, security and monetization
**Quality Tier:** 🟡 Yellow - one sampled skill (roblox-studio-mcp) carries a Snyk Warn; the rest pass all three scanners.

el4cteo/roblox-skills is a third, independent Roblox skill publisher in the catalog, separate from tabooharmony/roblox-brain and sentinelcore/roblox-skills, and it is not a mirror of either. This suite emphasizes production systems such as analytics and live-ops, architecture, data stores, monetization, networking and security on top of the core Luau, world-building and testing skills.

The skills keep agent-written Roblox code current, secure and correct, checked against the Roblox API reference (Studio 0.743, October 2026). CI type-checks every Luau example in strict mode and flags deprecated APIs on a weekly run, and agents see only a short description per skill (about 150 tokens), loading the full skill on demand.

## Installation

Claude Code:

```text
/plugin marketplace add EL4CTEO/roblox-skills
/plugin install roblox-skills@roblox-skills
```

Any other agent (needs Node.js):

```bash
npx skills add EL4CTEO/roblox-skills
npx skills add EL4CTEO/roblox-skills -a cursor -a windsurf -y
```

Without Node.js:

```bash
git clone https://github.com/EL4CTEO/roblox-skills.git && cd roblox-skills
./scripts/install.sh --project /path/to/game
./scripts/install.sh --agent windsurf --global
```

`docs/agents.md` lists every agent id and folder. Add `--link` to symlink the skills so `git pull` updates them. For Roblox Studio Assistant, download `roblox-assistant-skills.zip` from the latest release and add it via Assistant Settings > Skills > Add.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| roblox-world-building | 1,247 | Building worlds with code: parts, materials, Lighting, day/night, Terrain, CSG destruction, particles and beams. |
| roblox-testing | 1,182 | Testing Roblox code with Jest Lua, TestEZ, Studio runs, Studio MCP and CI via Open Cloud Luau Execution. |
| roblox-ui | 1,155 | Responsive cross-platform UI: ScreenGui, safe areas, Scale vs Offset, layout, StyleSheets, RichText and touch navigation. |
| roblox-luau | 1,150 | Modern type-safe Luau: strict mode, the new type solver, generics, the task library and OOP patterns. |
| roblox-game-systems | 1,146 | Recipes for server-authoritative systems: currency, XP/levels, rounds, combat, inventory, shops and daily rewards. |
| roblox-characters-animation | 1,146 | Characters and animation: Humanoid states, health and damage, Animator/AnimationTrack, tweens and tools. |
| roblox-security | 1,132 | Anti-exploit design: never trust the client, validate remote arguments, rate limiting and economy trade safety. |
| roblox-code-review | 1,130 | Reviewing Roblox/Luau for exploits, data loss, memory leaks, performance and deprecated APIs. |
| roblox-performance | 1,124 | Performance diagnosis: MicroProfiler, Script Profiler, memory leaks and Parallel Luau with Actors. |
| roblox-studio-mcp | 1,114 | Driving Roblox Studio from an agent via the Studio MCP server: inspect the DataModel, edit scripts, playtest. |
| roblox-architecture | 1,114 | Project structure and the client/server model: replication, where code and assets belong, lifecycle. |
| roblox-data-stores | 1,112 | Persistence: DataStoreService, ProfileStore session locking, leaderboards, MemoryStore queues and messaging. |
| roblox-networking | 1,086 | Client-server communication: RemoteEvent/Function, serialization, server validation and bandwidth. |
| roblox-audio | 1,082 | Sound and music: the Audio API, Sound/SoundGroup, 2D vs 3D audio, voice routing and text-to-speech. |
| roblox-analytics-liveops | 1,072 | Analytics and live ops: AnalyticsService events, A/B experiments, badges, timed events and season passes. |
| roblox-teleport-matchmaking | 1,070 | Multi-place and multi-server games: TeleportAsync, lobbies, parties, queues and matchmaking. |
| roblox-input | 1,069 | Player input and cameras: Input Action System, UserInputService, ContextActionService and custom cameras. |
| roblox-npc-ai | 1,066 | NPCs and enemy AI: PathfindingService, state machines, perception, line of sight and pooling. |
| roblox-physics | 1,063 | Physics and spatial queries: raycasts, collision groups, assemblies, mover constraints and vehicles. |
| roblox-monetization | 1,061 | Robux monetization: developer products, passes, subscriptions, rewarded ads and refunds. |
| roblox-tooling | 1,055 | Professional toolchain: Rojo, Rokit, Wally/pesde, luau-lsp, StyLua, selene, roblox-ts and CI. |
| roblox-text-chat | 1,049 | Chat and text safety: TextChatService, TextService filtering, commands and privacy checks. |
| roblox-open-cloud | 1,048 | Open Cloud REST APIs and HttpService: API keys/OAuth, external data stores, publishing and webhooks. |

No indexed listings fall below 1,000 installs; all 23 appear above.

## Why This Matters for Hermes Agents

Roblox code decays fast: the platform deprecates APIs every release, and agent-written code that leans on stale patterns such as `wait()`, `BodyVelocity` and legacy `Chat` breaks or opens exploits. This suite bakes that maintenance into the skill set - the README commits to checking every example against the current API reference, and CI type-checks each Luau snippet in strict mode, so an agent working from these skills gets current patterns instead of inherited blog snippets.

The production-system coverage is what sets it apart for builders. Skills for analytics and live-ops, data stores, monetization, networking and architecture mean an agent can do more than write scripts: it can reason about server authority, player data, economy safety and cross-server teleportation in the same session.

The studio-mcp skill closes the loop: the agent can drive an open Studio place, run Luau in edit, server and client contexts, playtest, read output and capture screenshots, so verification is not a human round-trip.

## Usage

| You say | What happens |
|---|---|
| "Where should this script live?" | roblox-architecture explains ServerScriptService vs ReplicatedStorage and the client/server replication model. |
| "Save player data safely" | roblox-data-stores applies DataStoreService with retries and ProfileStore session locking. |
| "Why is my game lagging?" | roblox-performance walks MicroProfiler and Script Profiler to find memory or replication cost. |
| "Audit this script for exploits" | roblox-security and roblox-code-review check remote validation and deprecated APIs. |
| "Add matchmaking to my game" | roblox-teleport-matchmaking covers TeleportAsync, lobbies, parties and queues. |
| "Let the agent playtest in Studio" | roblox-studio-mcp connects the agent to the built-in Studio MCP server. |

## Verification

Check the skill before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/el4cteo/roblox-skills/main/skills/roblox-architecture/SKILL.md | head -30
```

Skills live under `skills/<name>/` in the repo. Confirm the path exists in the current tree before installing a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| roblox-world-building | Pass | Pass | Pass |
| roblox-testing | Pass | Pass | Pass |
| roblox-ui | Pass | Pass | Pass |
| roblox-luau | Pass | Pass | Pass |
| roblox-game-systems | Pass | Pass | Pass |
| roblox-characters-animation | Pass | Pass | Pass |
| roblox-security | Pass | Pass | Pass |
| roblox-code-review | Pass | Pass | Pass |
| roblox-performance | Pass | Pass | Pass |
| roblox-studio-mcp | Pass | Pass | Warn |
| roblox-architecture | Pass | Pass | Pass |
| roblox-data-stores | Pass | Pass | Pass |

roblox-studio-mcp carries the only Warn in the sample (Snyk); it drives Roblox Studio, so review what it does before enabling it unsupervised.

## Limitations

- Snapshot data, verified Nov 16, 2026: 25,473 combined installs across 23 indexed listings; 118 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- roblox-studio-mcp carries the only scanner Warn in the sample (Snyk); treat it as normal and re-check its skills.sh security page before production.
- This is a third, independent Roblox publisher alongside tabooharmony/roblox-brain and sentinelcore/roblox-skills; it is not a mirror of those suites and emphasizes analytics, live-ops and architecture instead.
- Skill descriptions are short by design (about 150 tokens each); load the full SKILL.md on demand for the details.
- The project is not affiliated with Roblox Corporation (per the README).

## Related

- [Roblox Brain](/hermes/skills/catalog/roblox-brain-setup)
- [Roblox Skills](/hermes/skills/catalog/roblox-skills-setup)
- [Unity AI Skills](/hermes/skills/catalog/unity-ai-skills-setup)
- [Unreal Engine Skills](/hermes/skills/catalog/unreal-engine-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load the full SKILL.md on demand; the short descriptions are intentional so agent context stays lean.
- Connect the agent to Studio's built-in MCP server (roblox-studio-mcp) so it can playtest and verify changes.
- Run roblox-code-review before launch to catch deprecated APIs and exploits with its severity-ranked checklist.
- Prefer server-authoritative designs; roblox-security spells out why the client can never be trusted.
- Symlink skills with `--link` at install so `git pull` keeps them updated.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
