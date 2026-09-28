---
title: Hermes Agent v0.21.0 The Pantheon Release
description: Hermes Agent v0.21.0 (v2026.8.31) - The Pantheon Release. Bot Mode society of agents, cron memory and continuity, live subagent steering, MCP command center, desktop browser driving, 6 new providers.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.0/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.21.0 (v2026.8.31)

**Release Date:** August 31, 2026
**Since v0.20.0:** ~5,800 commits · ~2,475 merged PRs · ~5,680 files changed · ~2,100 issues closed · 760+ contributors

> The Pantheon Release. v0.20.0 made Hermes the herald. In v0.21.0 the gods assemble: a society of named agents that talk to each other like a team, cron jobs that remember between runs, subagents you can steer mid-flight, an MCP command center, and an agent that drives the desktop's own browser. This release also fully documents the v0.20.1 through v0.20.6 infrastructure patch windows.

---

## Highlights

- **Bot Mode, built into the desktop app** - every agent profile gets a name, a deterministic avatar face, and a place in a shared roster. Create group chats where multiple bots and you talk in one room, @-mention any bot from the composer, and give rooms names and pictures. Multi-agent now looks like a chat app full of coworkers.
- **`hermes peer` - bot-to-bot DMs** - any Hermes agent can message any other by handle, across profiles and gateways, from the CLI or from inside a conversation.
- **Cron jobs that remember** - scheduled jobs load and update persistent memory like any other agent. `continuity=true` carries each run's output into the next run, so scheduled agents learn between ticks.
- **Steer your subagents while they run** - `delegate_task` gained live orchestration: list running children, steer one mid-flight with a course correction, or stop it early and keep the partial results.
- **The MCP command center** - MCP servers and the catalog merged into one coherent desktop page with drag-in import, background health checks that nudge re-auth before a tool fails, and one-click connects.
- **A CLI power wave** - Ctrl+P fuzzy command palette, `/model` picker that filters as you type, `/status` showing reasoning mode, pending approvals, and context usage.
- **The agent drives the desktop's browser** - Hermes now navigates, clicks, and reads the in-app browser directly instead of only observing it.
- **Six new providers** - Meta Model API (Muse Spark) as a built-in provider, alongside CommandCode, Tencent TokenPlan, Nebius Token Factory, Ramp Router, and Actual Cloud.
- **Security hardening** - protected agent-instruction files (AGENTS.md, skills, memory stores) now always require write approval, so a prompt-injected agent cannot quietly rewrite its own rules.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.8.3...v2026.8.31](https://github.com/NousResearch/hermes-agent/compare/v2026.8.3...v2026.8.31)

---

*← [v0.20.1 - Patch Release](/docs/hermes/changelog/v0.20.1) | [v0.21.1 - Patch Release](/docs/hermes/changelog/v0.21.1) →*

*↑ [Changelog Home](/docs/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
