---
title: New Skills — July 14, 2026 (Update)
description: 4 additional OpenClaw/Hermes ecosystem skills discovered July 14, 2026 — wiki-history-ingest (2,744 installs), vps-server-management, and 2 agent plugin skills.
---

# New Skills Discovery — July 14, 2026 (Update)

**Date:** July 14, 2026
**Method:** Extended skills.sh API sweep (15 queries across broader ecosystem terms — hermes+deployment, hermes+security, hermes+mcp, openclaw+integration, clawpilot, davidondrej/skills, etc.)
**Results:** 4 genuinely new Hermes/OpenClaw-relevant skills not in any prior sweep or catalog

---

## Summary

| # | Skill | Installs | Publisher | Category |
|---|-------|----------|-----------|----------|
| 1 | wiki-history-ingest | 2,744 | ar9av/obsidian-wiki | Agent History / Knowledge Management |
| 2 | vps-server-management | 26 | davidondrej/skills | Infrastructure / DevOps |
| 3 | create-plugin | 24 | richfrem/agent-plugins-skills | Agent Plugin Development |
| 4 | task-agent | 24 | richfrem/agent-plugins-skills | Agent Task Management |

---

## Skill Details

### 1. wiki-history-ingest — Unified History Ingest Router (2,744 installs)

**Publisher:** [ar9av/obsidian-wiki](https://skills.sh/ar9av/obsidian-wiki)
**Installs:** 2,744
**Category:** Agent History / Knowledge Management

Unified entrypoint for ingesting agent conversation history into an Obsidian wiki vault. Routes to specialized history ingest skills for Claude, Copilot, Codex, **Hermes**, **OpenClaw**, and Pi. Dispatches based on explicit subcommand or auto-detection from source paths (`~/.hermes`, `~/.openclaw`, etc.).

```bash
npx skills add ar9av/obsidian-wiki --skill wiki-history-ingest
```

**Full setup guide:** [wiki-history-ingest →](/hermes/skills/catalog/wiki-history-ingest-setup/)

### 2. vps-server-management — Agent Server Operations (26 installs)

**Publisher:** [davidondrej/skills](https://skills.sh/davidondrej/skills) (2,510 ★)
**Installs:** 26
**Category:** Infrastructure / DevOps

Manage VPS servers and the AI agents running on them — SSH, deploy, monitor, restart. Explicitly references **Hermes Agent** (Discord gateway deployment) in its server inventory. Part of the `skills/ops-and-setup/` category in davidondrej's 40-skill agent toolkit.

```bash
npx skills add davidondrej/skills --skill vps-server-management
```

**Full setup guide:** [vps-server-management →](/hermes/skills/catalog/vps-server-management-setup/)

### 3. create-plugin — Agent Plugin Scaffolding (24 installs)

**Publisher:** [richfrem/agent-plugins-skills](https://skills.sh/richfrem/agent-plugins-skills) (4 ★)
**Installs:** 24
**Category:** Agent Plugin Development

Scaffold new plugins for agent frameworks. Part of the agent-plugins-skills toolkit for building reusable agent components across Claude Code, Codex, and other agent platforms.

```bash
npx skills add richfrem/agent-plugins-skills --skill create-plugin
```

### 4. task-agent — Agent Task Runner (24 installs)

**Publisher:** [richfrem/agent-plugins-skills](https://skills.sh/richfrem/agent-plugins-skills) (4 ★)
**Installs:** 24
**Category:** Agent Task Management

Execute and manage agent tasks with structured workflows. Part of the agent-plugins-skills ecosystem for cross-platform agent task execution.

```bash
npx skills add richfrem/agent-plugins-skills --skill task-agent
```

---

## Skipped Skills

- **openclaw-log-report** (junlincobo/openclaw-log-report, 88 installs) — 0 stars, no description, last updated April 2026. Low quality signal.
- **haiqing-self-improving-agent** (skills.volces.com, 41 installs) — Not accessible on GitHub; skills.volces.com is a custom registry. Unable to verify content or relevance.
- **crypto-price** (evgyur/crypto-price, 66 installs) — Clawdbot crypto lookup. 2 stars. Marginal Hermes relevance.
- **check-integration** (nowledge-co/community, 275 installs) — Could not locate SKILL.md in repo. The nowledge-co repo has Hermes (`nowledge-mem-hermes`) and OpenClaw (`nowledge-mem-openclaw-plugin`) directories — worth a dedicated sweep.

---

## Cross-Reference Notes

This update sweep ran after the [July 14 morning sweep](/hermes/skills/marketplace/new-july14-2026/) (2 skills). Extended queries across 15 broader ecosystem terms surfaced 4 additional skills, primarily from repos adjacent to the standard hermes/openclaw/clawdbot query set.

**Key repos discovered for future sweeps:**
- **ar9av/obsidian-wiki** — 37+ skills in `.skills/` directory. Only 3 previously catalogued (hermes-history-ingest, openclaw-history-ingest, wiki-history-ingest). The remaining 34+ skills (wiki-dashboard, wiki-lint, wiki-query, cross-linker, etc.) should be evaluated in a dedicated sweep.
- **davidondrej/skills** (2,510 ★) — 40 skills across 5 categories. Only 2 previously catalogued (distribute-skill-to-all-agents, browser-harness). 38 skills remain uncatalogued — many are agent infrastructure skills relevant to Hermes operations.
- **nowledge-co/community** (131 ★) — Has dedicated `nowledge-mem-hermes` and `nowledge-mem-openclaw-plugin` directories. Memory plugin for Hermes agents.

Previous sweep: [July 14, 2026](/hermes/skills/marketplace/new-july14-2026/)

---

*Part of the Hermes Skills Library — curated by CorpusIQ. [View all skills](/hermes/skills/marketplace/)*
