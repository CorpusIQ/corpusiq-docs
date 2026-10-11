---
title: "Delegate Skills - CLI Agent Fleet Orchestration Setup"
description: "Setup guide for amElnagdy/delegate-skills - 65.9K combined installs. Delegate coding tasks to per-CLI lanes: Codex, Claude, OpenCode, Cursor, and more."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amelnagdy-delegate-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent orchestration", "cli delegation", "coding agents"]
---

# Delegate Skills - Setup Guide

**Source:** [amElnagdy/delegate-skills](https://www.skills.sh/amElnagdy/delegate-skills) via skills.sh - 65.9K combined installs across 18 indexed listings; first seen Aug 14, 2026 (single-row skip); re-qualified Oct 10, 2026 (zero-catalog audit)
**GitHub:** [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) (2,355 stars, MIT license; pushed Oct 7, 2026; `skills/<name>/SKILL.md` layout)
**Category:** Multi-Agent Orchestration / CLI Delegation
**Quality Tier:** 🟡 Beta - 2,355-star MIT suite; active (pushed Oct 7, 2026; relay smoke CI); all sampled verdicts Pass

Delegate Skills, published by independent developer amElnagdy, turns your orchestrating agent into a dispatcher for the coding CLIs already installed on your machine. The organizing idea is a fleet of lanes: `delegate-setup` discovers the implementer CLIs it can find, proposes lanes like `feature`, `tests`, and `ui`, and writes the configuration only after you approve. From there you dispatch a brief to a lane or straight to one implementer, review the diff, and land the commit yourself. The suite spans 18 indexed skills, 17 implementer skills plus the setup skill, and has drawn 65.9K combined installs.

The delegation loop is review-first by design. Each `*-delegate` skill bundles a small `relay.mjs` script (Node built-ins only, no dependencies, no network calls of its own) that launches the implementer CLI, waits for completion, and writes a structured `result.json` with status, touched files, and a session id where the CLI exposes one. No relay ever commits; committing belongs to the reviewer, and each skill states its implementer's autonomy limits in that CLI's own terms.

---

## Installation

Prerequisites: Node 18+ and `git`, plus the target implementer CLI installed and authenticated as you would use it at a terminal. `delegate-setup` needs no implementer CLI; it discovers whichever are installed.

```bash
# Browse the full roster first
npx skills add amElnagdy/delegate-skills --list

# Install everything, or pick individual skills
npx skills add amElnagdy/delegate-skills
npx skills add amElnagdy/delegate-skills --skill delegate-setup
npx skills add amElnagdy/delegate-skills --skill codex-delegate
```

Pin an installation to an existing release tag as `@vMAJOR.MINOR.PATCH`; the skills CLI installs by git ref, not by the version in `SKILL.md`. You can also scope an install to one agent or make it global:

```bash
npx skills add amElnagdy/delegate-skills --skill codex-delegate --agent claude-code
npx skills add amElnagdy/delegate-skills --global
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| codex-delegate | 6,926 | Dispatch OpenAI Codex in workspace-write sandbox mode, resumable by session id |
| opencode-delegate | 5,896 | OpenCode build agent for implementation, plan agent for read-only runs |
| claude-delegate | 5,428 | Claude Code with acceptEdits and an explicit tool surface, resumable |
| agy-delegate | 5,255 | Google Antigravity under its own permission modes, plan mode for read-only |
| delegate-setup | 5,134 | Discover installed CLIs and write an approved fleet of lanes; never dispatches work |
| kimi-delegate | 3,931 | Kimi Code in auto permission mode with session resume |
| grok-delegate | 3,793 | Grok Build with workspace-scoped writes and a best-effort read-only tripwire |
| cursor-delegate | 3,563 | Cursor Agent with --force writes or plan-mode read-only runs |
| pi-delegate | 3,140 | Pi with full local tools; read-only runs limited to read, grep, find, ls |
| qoder-delegate | 2,915 | Qoder CLI in auto permission mode, plan mode for read-only |
| vibe-delegate | 2,834 | Mistral Vibe with accept-edits by default, plan-only read-only runs |
| cline-delegate | 2,646 | Cline in act mode with auto-approve, or a relay-enforced plan mode |
| copilot-delegate | 2,606 | GitHub Copilot CLI with allow-all-tools opt-in, headless auto-deny otherwise |
| aider-delegate | 2,552 | Aider with commits force-disabled, dry-run read-only mode, and resume support |
| zcode-delegate | 2,454 | Z.AI ZCode in yolo or plan mode, resolved from the desktop app bundle |
| warp-delegate | 2,369 | Warp Agent CLI through the oz headless agent, conversation resume by id |
| commandcode-delegate | 2,291 | Command Code with --yolo as the only headless write state |
| omp-delegate | 2,214 | Oh My Pi with --yolo approval mode and read-only read, grep, glob runs |

All 18 indexed listings clear the 2,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Delegation is one of the cheapest ways to scale an agent's throughput without scaling its context. Hermes agents already orchestrate tools and subagents, and this suite adds a portable layer that hands bounded coding work to first-class CLI implementers, each with its own strengths, cost profile, and trust level. Because every relay speaks one contract (`delegate-relay.result.v1`), the review pipeline stays the same when you swap Codex for Claude Code or route a mechanical refactor to a local model through Aider. The loop maps cleanly onto agent safety practice too: dispatch, poll, inspect the diff, re-run your own gates, and only then commit. And since the relays are dependency-free Node scripts, the whole layer is auditable before you trust it with a working tree.

## Usage

| You say | What happens |
|---|---|
| "Create a fleet for feature, tests, and UI work" | delegate-setup discovers installed implementer CLIs and proposes lane config for your approval |
| "Have Codex implement the refactor in services/billing/, then review and commit it" | codex-delegate dispatches the brief through its relay and returns a diff for review |
| "Implement the billing workflow with OpenCode in the feature lane" | opencode-delegate runs through the named lane with that lane's dials |
| "Run this queue of migration tasks through Codex while I review each one" | codex-delegate processes the queue task by task, each returning a structured result.json |
| "Fix the parser in a separate Claude Code session" | claude-delegate spins a fresh session from a self-contained brief, resumable by id |
| "Do a read-only planning pass before touching anything" | any *-delegate skill can run its implementer in a read-only or plan mode first |
| "Land this once it looks right" | you commit after review; no relay ever commits |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i delegate

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -i delegate

# Review the codex-delegate skill from GitHub before installing
curl -sL https://raw.githubusercontent.com/amElnagdy/delegate-skills/master/skills/codex-delegate/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| codex-delegate | Pass | Pass | Pass |
| claude-delegate | Pass | Pass | Pass |
| delegate-setup | Pass | Pass | Warn |
| opencode-delegate | Pass | Pass | Pass |

## Limitations

- The suite is a relay layer, not a sandbox: several implementers ship no CLI-enforced read-only mode, and what a run touches outside the target path may not be contained.
- Each implementer CLI has to be installed, authenticated, and kept current on its own; the skills do not bundle or manage them.
- Listings sit between 2,214 and 6,926 installs and the family was only sized on Oct 10, 2026 (re-qualified in a zero-catalog audit after a single-row first sighting), so the combined figure is young.
- Single-maintainer project: MIT licensed, 2,355 stars, active as of Oct 7, 2026 with a relay smoke CI.
- Snapshot data, verified Oct 10, 2026: 65,947 combined installs across 18 indexed listings; 2,355 GitHub stars; MIT; last pushed Oct 7, 2026. Counts drift over time.

## Related

- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup) - the vendor suite for Codex, one of the delegate lanes
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup) - Anthropic's agentic coding skill patterns
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup) - templates for writing your own delegation skills
- [Delegate Skills - Background Agent Delegation](/hermes/skills/catalog/delegate-skills-setup) - an earlier, different project that shares this name (isolated worktree workers, June 2026)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Give every dispatch a self-contained brief; the implementer starts a fresh session with none of your orchestrator's chat history.
- Start with read-only or plan runs to calibrate an implementer's behavior before granting write access.
- Use lanes for repeated work (feature, tests, ui) and direct dispatch for one-offs with explicit flags.
- Re-run the project's own gates while reviewing; the diff and touched-files report are review aids, not guarantees.
- Pin installs to a release tag (`@vMAJOR.MINOR.PATCH`) for reproducible setups across a team.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
