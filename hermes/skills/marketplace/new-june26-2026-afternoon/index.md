---
title: New June 26, 2026 (Afternoon) — Agenthood 14-Agent Team + Letta AI 24-Skill Harness
description: 38 newly catalogued skills — Agenthood's full AI engineering team (14 specialized agent roles) and Letta Code's complete 24-skill agent harness. Multi-agent architecture, memory systems, and self-improving agent infrastructure.
---

# New Skills Discovered — June 26, 2026 (Afternoon Sweep)

**Sources:** [skills.sh](https://skills.sh) — [fworks-tech/agenthood](https://skills.sh/fworks-tech/agenthood), [letta-ai/letta-code](https://skills.sh/letta-ai/letta-code)
**Total new catalogued:** 38 skills | **Combined repos:** 2
**Date:** June 26, 2026

Two major additions fill gaps in our agent-infrastructure and multi-agent categories: Agenthood provides a complete AI engineering team as skills.sh-compatible Markdown files, and Letta Code's full 24-skill harness (previously only 1 skill documented) brings stateful agent memory, MCP conversion, and self-improving infrastructure.

---

## Skills Discovered

### 1. Agenthood — 14-Agent AI Engineering Team (fworks-tech/agenthood)

Agenthood packages 14 specialized AI agent roles as individual skills.sh-compatible SKILL.md files. Each agent is a self-contained role with responsibilities, standards, and communication patterns. Drop them into any agent runtime — Claude Code, Copilot, Hermes Agent, or the standalone TypeScript CLI.

**GitHub:** [fworks-tech/agenthood](https://github.com/fworks-tech/agenthood) · **npm:** `agenthood` (v3.0.0) · **License:** MIT

| Agent | Skill | Role |
|---|---|---|
| 🏗️ | **the-architect** | System design, ADRs, technical decisions |
| 🔒 | **the-auditor** | Security scanning, vulnerability assessment, dependency audit |
| 🐛 | **the-debugger** | Error triage, root cause analysis |
| 🚪 | **the-doorman** | Validation, branch protection, CI health checks |
| 🌐 | **the-envoy** | Cross-provider translation, convention validation |
| 📦 | **the-herald** | Releases, versioning, changelog generation |
| 📝 | **the-librarian** | Documentation, API references, knowledge management |
| 🔮 | **the-oracle** | Institutional knowledge, authoring templates |
| 🔍 | **the-reviewer** | Code review, standards enforcement |
| ✍️ | **the-scribe** | Commits, PR descriptions, changelogs |
| 👁️ | **the-sentinel** | Integrity monitoring, cross-member contradiction detection |
| 🧭 | **the-steward** | Context economy, provider cache strategies |
| 🧪 | **the-tester** | TDD, coverage analysis, edge case generation |
| ⚖️ | **the-warden** | Code health, complexity enforcement |

**Why this matters for Hermes:** Agenthood is a blueprint for multi-agent architecture. These 14 roles define clear boundaries, communication patterns, and escalation paths. Hermes agents can adopt individual roles (e.g., the-reviewer for PR workflows) or compose them into agent teams. The skills.sh compatibility means direct installation via `npx skills add`.

---

### 2. Letta Code — 24-Skill Stateful Agent Harness (letta-ai/letta-code)

Letta Code is a stateful agent harness built by the creators of MemGPT. Agents have persistent memory, identity, and learn over time through rewriting their own memory, skills, and prompts. Previously only 1 skill was catalogued — this update documents the full 24-skill suite.

**GitHub:** [letta-ai/letta-code](https://github.com/letta-ai/letta-code) · **npm:** `@letta-ai/letta-code` · **Built on:** MemGPT research

| Skill | Category | Description |
|---|---|---|
| **initializing-memory** | Memory | Set up agent memory blocks, identity, and personality |
| **syncing-memory-filesystem** | Memory | Git-backed memory sync (MemFS) across machines |
| **finding-agents** | Discovery | Search and discover existing agents in a workspace |
| **migrating-memory** | Memory | Migrate memory between agent runtimes and formats |
| **creating-skills** | Skills | Author new skills for agents programmatically |
| **acquiring-skills** | Skills | Discover and install skills from Hermes, ClawHub, GitHub |
| **messaging-agents** | Communication | Inter-agent messaging and channel management |
| **adding-models** | Configuration | Add and configure new LLM model backends |
| **working-in-parallel** | Orchestration | Dispatch and coordinate parallel agent workstreams |
| **searching-messages** | Search | Full-text search across all agent conversations |
| **defragmenting-memory** | Memory | Optimize and compact agent memory over time |
| **migrating from codex and claude code** | Migration | Migrate agents and workflows from other runtimes |
| **converting-mcps-to-skills** | MCP | Convert MCP servers into portable agent skills |
| **dispatching-coding-agents** | Orchestration | Spawn and manage coding sub-agents |
| **scheduling-tasks** | Scheduling | Cron jobs, heartbeats, and scheduled agent work |
| **customizing-commands** | Configuration | Add custom slash commands to the agent harness |
| **Context Doctor** | Diagnostics | Audit and repair agent context/memory quality |
| **customizing-statusline** | UI | Customize the agent terminal status display |
| **creating-extensions** | Extensions | Build harness extensions and plugins |
| **modifying-the-harness** | Core | Modify the agent harness itself for custom behavior |
| Plus 4 additional skills for channels, hooks, permissions, and secrets management | | |

**Why this matters for Hermes:** Letta Code is the closest architectural cousin to Hermes Agent — both are stateful agent harnesses with memory, skills, and multi-agent orchestration. Skills like `converting-mcps-to-skills`, `defragmenting-memory`, and `dispatching-coding-agents` are directly applicable to Hermes workflows. The `acquiring-skills` skill installs from Hermes, ClawHub, and GitHub — creating a two-way skill ecosystem bridge.

---

## Installation

```bash
# === Agenthood (14-agent team) ===
npx skills add fworks-tech/agenthood

# Or install individual agents:
npx skills add fworks-tech/agenthood --skill the-reviewer
npx skills add fworks-tech/agenthood --skill the-architect
npx skills add fworks-tech/agenthood --skill the-auditor

# === Letta Code Agent Harness (24 skills) ===
npm install -g @letta-ai/letta-code
letta skills install https://github.com/letta-ai/letta-code
```

---

## Impact Assessment

**Agenthood** fills the multi-agent architecture gap in our marketplace. With 14 clearly-defined roles, it provides a reference implementation for Hermes agent teams. The skills.sh compatibility means Hermes agents can directly load individual roles (e.g., the-reviewer for PR review workflows, the-auditor for security scanning).

**Letta Code** completes our documentation of one of the most sophisticated agent harnesses in the ecosystem. The memory architecture (MemFS with git backing, memory defragmentation), MCP-to-skills conversion pipeline, and self-improving agent loops are patterns Hermes can learn from. The bidirectional skill bridge (`acquiring-skills` installs from Hermes) creates ecosystem interoperability.

---

*← [June 26 Morning Update](/hermes/skills/marketplace/new-june26-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
