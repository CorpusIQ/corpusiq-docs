---
title: "Nonlooped Roblox Suite - Production Luau Skills Setup"
description: "nonlooped/roblox-suite - 12.6K combined installs: production-grade Roblox Luau skills for VFX, animation, networking, and monetization."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nonlooped-roblox-suite-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "roblox", "luau", "game development"]
---

# Nonlooped Roblox Suite - Setup Guide

**Source:** [nonlooped/roblox-suite](https://www.skills.sh/nonlooped/roblox-suite) via skills.sh - 12.6K combined installs across 28 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [nonlooped/roblox-suite](https://github.com/nonlooped/roblox-suite) - 37 stars, MIT license, last pushed Nov 20, 2026, main branch; 16 skill folders at the repo root, each with SKILL.md plus references/ and scripts/.
**Category:** Game Development (Roblox / Luau)
**Quality Tier:** 🟠 Orange - 15 sampled skills all pass the Gen Agent Trust Hub and Socket, but Snyk flags roblox-teleport with a Fail and four others with a Warn.

nonlooped/roblox-suite is a production-grade, opinionated skill set for AI agents and developers writing Roblox Luau. Its 28 indexed listings span API selection, server authority, persistence, gameplay, presentation, and Studio workflows, backed by 16 skill folders at the repo root, each with a SKILL.md entry point plus references/ and scripts/. Every skill links to the official Roblox documentation used to review it, and the shipped Lua scripts are examples with maturity labels that the README says to adapt and test before production use.

Against the three Roblox guides already in the catalog, this repository distinguishes itself in two ways it documents itself: every skill links to the official documentation used to review it, and the repo publishes a paired evaluation (evals/) with the prompts, outputs, and limits of comparing a baseline agent against the suite. A top-level roblox skill routes broad tasks to 15 specialists covering VFX, animation, user interfaces, MCP, testing, core services, monetization, networking, datastores, audio, Rojo, NPCs, physics, teleport, and Open Cloud.

## Installation

Install the suite from your project root and follow the installer prompts:

```bash
npx skills add nonlooped/roblox-suite
```

To install a single skill, pass --skill:

```bash
npx skills add nonlooped/roblox-suite --skill roblox-datastores
```

Manage the installation with:

```bash
npx skills list
npx skills update
npx skills remove roblox-datastores   # remove one skill
npx skills remove --all               # remove all installed skills
```

Use --agent to target a specific agent and --global for a global installation. If your agent cannot find the skills, run npx skills list to check the installation scope and agent target, then restart the agent to reload its skill files.

## What It Provides

skills.sh publishes per-skill install counts across the 28 indexed listings. The 8 most-installed skills are listed below; the remaining 20 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| roblox-vfx | 1,924 | build or optimize particles, beams, trails, and highlights, from emitter shapes to flipbooks and distance culling |
| roblox-animation | 1,239 | build or debug character animations, IK poses, animation-marker events, and UI or object tweens |
| roblox-user-interfaces | 745 | build or debug HUDs, menus, and world-space interfaces, including GUI containers and responsive layouts |
| roblox | 697 | route Luau tasks to specialist skills for architecture decisions and multi-system work |
| roblox-mcp | 697 | connect an AI client to Roblox Studio through MCP, including setup and playtesting |
| roblox-testing | 689 | test, debug, or profile experiences with Studio debugging, TestEZ, and the Script Profiler |
| roblox-core | 675 | choose Roblox services, script locations, and execution contexts for Luau types and serialization |
| roblox-gamepasses | 674 | implement game passes, developer products, subscriptions, and Robux transfers with server-side fulfillment |

The remaining 20 indexed listings range from 1 to 672 installs.

## Why This Matters for Hermes Agents

Roblox Luau changes fast, and a coding agent left to its training data will suggest deprecated APIs such as Humanoid:LoadAnimation or reach for SetAsync where concurrent writes can overwrite player data. This suite describes the modern alternatives, their constraints, and the official source for each, so a Hermes agent gets accurate guidance instead of stale patterns. The roblox router plus 15 specialists lets an agent load only the guidance relevant to the current task instead of a wall of advice. For a builder running Hermes agents on Roblox projects, the reusable Lua scripts (rate limiters, safe datastores, teleport helpers) are starting points with maturity labels, and the paired evaluation is evidence of what the suite does and does not improve. The main caveat is the Snyk Fail on roblox-teleport, noted below.

## Usage

| You say | What happens |
|---|---|
| Add a particle explosion to my game | Uses roblox-vfx to pick emitter shapes, flipbooks, and burst timing |
| Make this NPC patrol and chase | Uses roblox-npcs for PathfindingService, patrol, and chase logic |
| Save player progress safely | Uses roblox-datastores for concurrent writes, session locking, and quotas |
| Connect my agent to Roblox Studio | Uses roblox-mcp for connection setup and playtesting |
| Why does this remote let cheaters through | Uses roblox-networking for input validation, rate limiting, and exploit defenses |
| Set up Rojo sync for this place | Uses roblox-rojo for CLI and plugin setup, live sync, and syncback |
| Build a pass that grants items | Uses roblox-gamepasses for purchase prompts and server-side fulfillment |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/nonlooped/roblox-suite/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/nonlooped/roblox-suite/main/roblox/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skill's SKILL.md and references/ before relying on it, and re-check the security pages on skills.sh for the verdicts below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| roblox-vfx | Pass | Pass | Pass |
| roblox-animation | Pass | Pass | Pass |
| roblox-user-interfaces | Pass | Pass | Pass |
| roblox | Pass | Pass | Pass |
| roblox-mcp | Pass | Pass | Warn |
| roblox-testing | Pass | Pass | Warn |
| roblox-core | Pass | Pass | Pass |
| roblox-gamepasses | Pass | Pass | Warn |
| roblox-networking | Pass | Pass | Pass |
| roblox-datastores | Pass | Pass | Warn |
| roblox-audio | Pass | Pass | Pass |
| roblox-rojo | Pass | Pass | Pass |
| roblox-npcs | Pass | Pass | Pass |
| roblox-physics | Pass | Pass | Pass |
| roblox-teleport | Pass | Pass | Fail |

All 15 sampled listings pass the Gen Agent Trust Hub and Socket; Snyk returns one Fail (roblox-teleport), four Warn, and ten Pass.

## Limitations

- Snapshot data, verified Nov 25, 2026: 12,560 combined installs across 28 indexed listings; 37 GitHub stars; MIT; last pushed Nov 20, 2026. Counts drift over time.
- The 28 indexed listings map to 16 in-tree skill folders; the other 12 listings are a Release entry (6 installs) and 11 one-install listings under longer descriptive names, such as roblox-visual-effects-and-particles.
- Snyk marks roblox-teleport with a Fail and roblox-mcp, roblox-testing, roblox-gamepasses, and roblox-datastores with Warn; review those pages before production use.
- The shipped Lua scripts are examples with maturity labels, not turnkey production code; adapt and test them first.
- The paired evaluation is a single July 2026 run against one baseline model; treat it as a point-in-time signal, not ongoing coverage.

## Related

[Roblox Agent Skills - Production Roblox Skill Suite](/hermes/skills/catalog/roblox-agent-skills-setup) | [Roblox Brain - Roblox Studio Development Skills Setup](/hermes/skills/catalog/roblox-brain-setup) | [Roblox Game Dev Skills - Claude Code Suite Setup](/hermes/skills/catalog/roblox-game-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start broad tasks at the roblox router skill; it dispatches to the right specialist instead of loading the whole suite.
- Run npx skills update before reporting stale guidance, and restart your agent so it reloads the skill files.
- Use --global for skills you want across every Roblox project and --agent to pin a specific agent target.
- Treat the scripts/ files as starting points: they carry maturity labels and need testing before production.
- Re-check the roblox-teleport security page on skills.sh before relying on teleport guidance, given the Snyk Fail.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
