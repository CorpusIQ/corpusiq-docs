---
title: "Roblox Game Dev Skills - Claude Code Suite Setup"
description: "ashexplained/roblox-skills: 7.8K combined installs across 40 listings; 40 Claude Code skills for Roblox game development from ideas to live ops."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/roblox-game-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "roblox", "game development", "luau"]
---

# Roblox Game Dev Skills - Setup Guide

**Source:** [ashexplained/roblox-skills](https://www.skills.sh/ashexplained/roblox-skills) via skills.sh - 7.8K combined installs across 40 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 63 stars, MIT license, `main` branch, last pushed 2026-07-01. Each of the 40 skills is a top level directory holding one SKILL.md, with setup-roblox-skills also carrying tracker and triage configuration files.
**Category:** Roblox game development for Claude Code agents
**Quality Tier:** 🟡 Yellow - 58 Pass and 2 Warn across the 60 sampled verdict cells; MIT licence.

This is the AshExplained suite of 40 Claude Code skills for Roblox game development. It spans the full game development lifecycle, from game ideas and Luau architecture through combat systems, UX, economy, monetization, security, QA, publishing, and live ops. A companion vertical-slice workflow turns a concept into a PRD, splits the PRD into playtestable slices, and moves each slice through a triage state machine so the agent never tries to build a whole game in one broken pass.

A different publisher, sentinelcore, owns a separate seven-skill Roblox suite also indexed in this catalog; see the Related section for that page. This guide covers the larger AshExplained collection only.

## Installation

Clone the repository into your Claude Code skills directory. For a single game project:

```bash
git clone https://github.com/AshExplained/roblox-skills.git .claude/skills/roblox-skills
```

For user-level skills available in every project:

```bash
git clone https://github.com/AshExplained/roblox-skills.git ~/.claude/skills/roblox-skills
```

On Windows PowerShell:

```bash
git clone https://github.com/AshExplained/roblox-skills.git "$env:USERPROFILE\.claude\skills\roblox-skills"
```

Each subfolder holds one SKILL.md, and Claude Code discovers them automatically once they are installed. Installing only makes the skills available; the README requires one more step.

Run setup-roblox-skills once per game project:

```
setup-roblox-skills
```

This step injects a routing block into the project's CLAUDE.md containing the lifecycle map, every skill's purpose and trigger words, and next-skill routing. Because that block lives in CLAUDE.md, Claude reads it at the start of every session and knows which skill to reach for. Skipping it still loads the skills, but without the lifecycle context that keeps the agent building in vertical slices.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| roblox-world-level-design | 270 | Design worlds, levels, hubs, zones, biomes, obbies, arenas, and exploration spaces with spatial layout, player flow, spawns, and text free guidance. |
| roblox-game-ux | 245 | Design and critique game UX, HUDs, menus, onboarding, mobile controls, and progression surfaces so an experience feels clear and retention aware. |
| roblox-asset-pipeline | 236 | Plan and execute asset workflows for Creator Store search, generated meshes and materials, thumbnails, icons, and asset performance budgets. |
| roblox-playtest-qa | 235 | Playtest experiences through Studio MCP with attention to first session fun, mobile UX, console errors, progression, and exploit sensitive flows. |
| roblox-ui-implementation | 228 | Implement Studio UI such as ScreenGui, HUDs, menus, touch controls, buttons, and shop panels, then verify the result through Studio MCP. |
| roblox-mobile-playtest | 222 | Playtest and QA for mobile and tablet, covering device simulator checks, touch controls, safe areas, thumb zones, and text readability. |
| roblox-combat-systems | 219 | Design, implement, and review combat systems for melee, ranged, abilities, hit detection, status effects, and exploit resistant remotes. |
| roblox-animation-audio-feedback | 217 | Improve game feel through animation, audio, VFX, reward juice, movement feel, combat feedback, and UI transitions without hurting mobile performance. |
| roblox-game-ideas | 207 | Generate or evaluate game ideas using retention, social, monetization, mobile first, and first session best practices. |
| roblox-performance-optimization | 204 | Analyze and optimize scene and script performance for mobile frame rate, memory, instance count, rendering cost, streaming, and leaks. |
| roblox-creator-store-security-audit | 202 | Audit Creator Store, Toolbox, and other imported assets for malicious or risky scripts before inserting or trusting them. |
| roblox-economy-balancing | 200 | Balance economies and progression math with currency sources and sinks, pricing, reward curves, and inflation control without pay to win pressure. |
| roblox-security-economy | 198 | Build and review security sensitive economy systems with anti dupe logic, RemoteEvent validation, server authority, and receipt handling. |
| roblox-debugging-bugfix | 198 | Debug and fix bugs through Studio MCP with repro steps, console errors, script search and edit, and post fix verification. |
| roblox-genre-patterns | 195 | Apply genre specific design patterns for simulator, tycoon, obby, RPG, tower defense, survival, horror, and racing planning from idea to live ops. |
| roblox-game-development-lifecycle | 194 | Orchestrate the full game development lifecycle as the umbrella entrypoint that routes broad requests to the right specialist skill by phase. |
| roblox-luau-architecture | 192 | Design, inspect, and refactor Luau architecture for module boundaries, client server flow, remotes, and script placement. |
| roblox-studio-workflow | 190 | Use Roblox Studio MCP safely to connect, inspect a place, edit scripts and instances, insert assets, and playtest. |
| roblox-policy-compliance | 190 | Review platform policy and compliance risk for Community Standards, advertising rules, gacha odds disclosure, age labels, IP, and privacy. |

The remaining 21 indexed listings range from 158 to 189 installs.

## Why This Matters for Hermes Agents

A general purpose model writing Roblox code reproduces the tutorial defaults it has seen most often, and several of those defaults are wrong for the platform: economy state trusted to the client, DataStore writes with no retry, a RemoteEvent handler that accepts whatever the client sends, a UI laid out in fixed offsets that breaks on phones. None of these fail at compile time. They fail in front of players, with an executor, or when a save is lost.

This suite turns those platform rules into playbooks an agent reads before it writes. The security skills encode server authority and anti-dupe checks; the economy skills carry fair monetization without pay-to-win; the performance and mobile skills keep the experience playable on phones, which is where most Roblox players are.

The vertical-slice workflow is the part that changes behaviour the most. Instead of generating an entire game in one pass, the agent goes concept to PRD to issues to triage, then builds one small slice through client, server, remotes, data, and UI before moving on. Luau code and instances live in the Roblox cloud experience and are edited through Studio MCP, so Git tracks planning artifacts only.

## Usage

| You say | What happens |
|---|---|
| "Give me 3 mobile first Roblox simulator ideas with fair monetization" | Loads roblox-game-ideas to generate and score concepts for retention, social, and monetization fit. |
| "Design a server authoritative currency system that resists dupes" | Loads roblox-security-economy for anti dupe logic, RemoteEvent validation, and server authority. |
| "Review this Creator Store model before I insert it" | Loads roblox-creator-store-security-audit to scan the asset for malicious or risky scripts. |
| "Take this concept from idea to launch" | Loads roblox-game-development-lifecycle, which routes the work to the right specialist skill by phase. |
| "Set up this game project for Claude" | Runs setup-roblox-skills to inject the lifecycle routing block into CLAUDE.md. |
| "Break my PRD into playtestable slices" | Loads roblox-to-issues to split the PRD into small vertical slices that can each be verified in Studio. |

## Verification

Probe a skill on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/ashexplained/roblox-skills/main/roblox-world-level-design/SKILL.md | head -12
```

The file should open with `name: roblox-world-level-design` and a description about world and level design. After cloning, confirm the required setup skill is present:

```bash
git clone https://github.com/AshExplained/roblox-skills.git .claude/skills/roblox-skills
ls .claude/skills/roblox-skills/setup-roblox-skills/SKILL.md
```

Then run the setup step and check that CLAUDE.md carries the routing block:

```
setup-roblox-skills
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| roblox-world-level-design | Pass | Pass | Pass |
| roblox-game-ux | Pass | Pass | Pass |
| roblox-asset-pipeline | Pass | Pass | Pass |
| roblox-playtest-qa | Pass | Pass | Pass |
| roblox-ui-implementation | Pass | Pass | Pass |
| roblox-mobile-playtest | Pass | Pass | Pass |
| roblox-combat-systems | Pass | Pass | Pass |
| roblox-animation-audio-feedback | Pass | Pass | Pass |
| roblox-game-ideas | Pass | Pass | Pass |
| roblox-performance-optimization | Pass | Pass | Pass |
| roblox-creator-store-security-audit | Pass | Pass | Warn |
| roblox-economy-balancing | Pass | Pass | Pass |
| roblox-security-economy | Pass | Pass | Warn |
| roblox-debugging-bugfix | Pass | Pass | Pass |
| roblox-genre-patterns | Pass | Pass | Pass |
| roblox-game-development-lifecycle | Pass | Pass | Pass |
| roblox-luau-architecture | Pass | Pass | Pass |
| roblox-studio-workflow | Pass | Pass | Pass |
| roblox-policy-compliance | Pass | Pass | Pass |
| roblox-retention-monetization | Pass | Pass | Pass |

The sample covers 20 of the 40 indexed listings; the only two Warn cells are Snyk flags on roblox-creator-store-security-audit and roblox-security-economy. The repository holds markdown only, with no scripts or hooks that run when a skill loads.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,791 combined installs across 40 indexed listings; 63 GitHub stars; MIT; last pushed 2026-07-01. Counts drift over time.
- The skills are written for Claude Code and the Roblox Studio MCP; an agent without a Studio MCP connection can read the playbooks but cannot run the inspect, edit, and playtest steps.
- The README requires running setup-roblox-skills once per project; skipping it leaves the routing block out of CLAUDE.md, so the skills load without lifecycle context.
- Luau code and instances live in the Roblox cloud experience and are never committed to Git; the repository holds planning artifacts only.
- The last push is 2026-07-01, so specific dashboard paths and Creator Hub steps in some skills may need checking against current Roblox Studio.
- Install counts are flat across the suite; the top skill carries 270 installs and the rest trail off to the 158 to 189 tail.

## Related

- [Roblox Skills - Game Systems for Agents Setup](/hermes/skills/catalog/roblox-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run setup-roblox-skills before asking for any game work; the CLAUDE.md routing block is what keeps the agent building in vertical slices.
- Load one skill per task. A broad "build me a game" request hits the umbrella router first, then hands off to the right specialist.
- Read roblox-security-economy before roblox-creator-store-security-audit on anything that touches currency or imports assets.
- Keep the Studio MCP connected; most build, QA, and bugfix skills verify their work through it.
- For a new concept, go roblox-to-prd then roblox-to-issues then roblox-triage, and playtest each slice before the next.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
