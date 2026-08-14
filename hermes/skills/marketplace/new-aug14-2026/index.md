---
title: New Skills — August 14, 2026
description: "skills.sh sweep — 2 new publisher clusters with setup guides: Chrome DevTools MCP skills (chromedevtools/chrome-devtools-mcp, 8.5K installs) and Oh My Hermes suite (witt3rd/oh-my-hermes, 9 skills, ~800 installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug14-2026/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill marketplace", "skills.sh"]
sweep_id: aug-14-2026
new_publishers: 2
new_skills: 11
guides_drafted: 2
---

# New Skills — August 14, 2026

**Source:** [skills.sh](https://skills.sh) REST API multi-query sweep
**Date:** August 14, 2026
**Result:** 2 new publisher clusters · 11 skills · 2 setup guides

Routine daily sweep across 11 queries (core Hermes repos, broad terms, ecosystem repos: gbrain, honcho, devtools-skills, antigravity-awesome-skills, opendirectory, mercury-agent-skills). Cross-referenced 807 unique skills against the existing `hermes/skills/` tree. Two undocumented clusters with substantive Hermes value were found and guided.

---

## New Publisher Clusters (2) — With Setup Guides

### 1. Chrome DevTools MCP Skills — `chromedevtools/chrome-devtools-mcp` (8.5K installs)

Google's official Chrome DevTools skills. The biggest single gap found this sweep: the MCP server was indexed in the MCP catalog, but neither skill had a setup guide.

| Skill | Installs | Description |
|---|---|---|
| `chrome-devtools` | 5,934 | Chrome DevTools via MCP — debugging, troubleshooting, browser automation, performance traces, network inspection |
| `chrome-devtools-cli` | 2,572 | Browser automation from shell scripts via the `chrome-devtools` CLI |

Both work with any MCP-capable agent including Hermes (native MCP client). The repo is Google's official chrome-devtools-mcp (100K+ stars upstream ecosystem).

**Setup guide:** [Chrome DevTools MCP Skills Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/)

### 2. Oh My Hermes (OMH) Suite — `witt3rd/oh-my-hermes` (255⭐, ~800 installs)

Hermes-native multi-agent orchestration: consensus planning (Planner → Architect → Critic), Socratic requirements interviews, parallel research with citation verification, and evidence-verified execution. Rebuilt natively for Hermes primitives — installed via `hermes skills tap`, not npx.

| Skill | Installs | Description |
|---|---|---|
| `omh-autopilot` | 96 | End-to-end pipeline: interview → plan → execute → QA → verify |
| `omh-deep-research` | 95 | Parallel web research — subagents → synthesis → cite-verify |
| `omh-ralplan` | 93 | Planner + Architect + Critic → consensus implementation plan |
| `omh-deep-interview` | 92 | Socratic requirements interview, coverage tracking |
| `omh-ralph` / `omh-ralph-driver` | 91 / 90 | Verified execution — evidence required per task |
| `omh-ralph-task` | 90 | Single-task executor discipline, sibling isolation |
| `omh-triage` / `omh-triage-driver` | 89 | Multi-role consensus backlog triage (v0.1) |

Directly complements CorpusIQ's multi-agent stack (blueprint orchestration, supervisor-agent waves).

**Setup guide:** [Oh My Hermes (OMH) Suite Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup/)

---

## Evaluated and Skipped This Sweep

| Skill / Cluster | Installs | Reason Skipped |
|---|---|---|
| `agy-delegate` (amelnagdy/delegate-skills) | 1,371 | Requires Google Antigravity CLI (`agy`) — not Hermes-native |
| `react-devtools` (callstack/agent-device) | 1,319 | CLI command inside a Codex-targeted device tool, not a Hermes skill |
| `bambu-labs` (earthtojake/text-to-cad) | 4,892 | 3D-printer handoff domain — outside Hermes operations scope |
| `lynx-devtool` (lynx-community/skills) | 3,390 | Lynx mobile framework specific |
| `workflow-creator` (nicepkg/ai-workflow) | 337 | Claude Code / Cursor targeted |
| `design-lab` (0xdesign/design-plugin) | 1,280 | Claude plugin marketplace, no Hermes path |
| `font-awesome` (membranedev/application-skills) | 116 | Antigravity platform bot |
| `antigravity-*` (sickn33/agentic-awesome-skills) | 256–861 | Antigravity-specific naming; remaining generic skills from this catalog already covered |
| `azure-devtest-labs` (microsoftdocs/agent-skills) | 101 | Azure DevOps Labs platform specific |

---

## Installation

```bash
# Chrome DevTools MCP skills
npx skills add chromedevtools/chrome-devtools-mcp

# Oh My Hermes suite (native Hermes install)
hermes skills tap add witt3rd/oh-my-hermes
hermes skills install omh-deep-research omh-ralplan omh-ralplan-driver omh-deep-interview omh-ralph omh-ralph-driver omh-ralph-task omh-triage omh-triage-driver omh-autopilot
```

## Notable

- **Chrome DevTools MCP** is the standout: official Google skills, agent-agnostic MCP transport, and a large documentation gap (indexed as an MCP server but never given a skill setup guide).
- **OMH suite** is the most substantial Hermes-native multi-agent orchestration suite since the blueprint-orchestration methodology — consensus planning and verified execution align directly with CorpusIQ's multi-agent operations.
