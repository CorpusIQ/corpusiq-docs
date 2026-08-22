---
title: "agentiko-hermes — Setup Guide - CorpusIQ Docs"
description: Hermes Agent features guide for the agentiko Telegram setup — cron, delegation, memory, automation, YOLO mode, dual-agent hunting, and slash commands.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentiko-hermes-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# agentiko-hermes — Setup Guide

**Source:** [uphiago/recon-skills](https://github.com/uphiago/recon-skills)
**Skill:** `agentiko-hermes`
**Installs:** 16

A comprehensive Hermes Agent features guide covering cron jobs, task delegation, persistent memory, automation workflows, YOLO mode configuration, dual-agent hunting patterns, and slash commands — specifically designed for the agentiko Telegram integration setup.

## Installation

```bash
npx skills add https://github.com/uphiago/recon-skills --skill agentiko-hermes
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v2.0+ |
| Telegram bot | Configured for agentiko integration |
| agentiko | Installed and configured on target system |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Cron job setup | "Set up a recurring job for X" | Guided cron configuration |
| Task delegation | "Delegate this task to a subagent" | Delegation workflow |
| Memory management | "Save this to persistent memory" | Memory storage guidance |
| YOLO mode | "Enable autonomous execution" | YOLO mode configuration |
| Dual-agent hunting | "Set up dual-agent workflow" | Multi-agent coordination |
| Slash commands | "/help" or "/commands" | Available slash command reference |

## CLI/Command Reference

The skill provides a reference guide. Key patterns documented:

- **Cron:** `hermes cron create --schedule "0 */6 * * *" --prompt "..."`
- **Delegation:** `delegate_task(goal="...", context="...")`
- **Memory:** `memory(action="add", target="memory", content="...")` 
- **YOLO mode:** Configuration for autonomous execution without confirmation gates
- **Slash commands:** `/reload-skills`, `/restart`, `/status`, `/help`

## CorpusIQ Use Cases

1. **Telegram agent operations** — Reference guide for CorpusIQ agents operating via Telegram Topic 2
2. **Cron management** — Best practices for multi-cron agent operations
3. **Delegation patterns** — Multi-agent workflows for parallel task execution
4. **Memory architecture** — Persistent memory patterns across CorpusIQ agent sessions
5. **New team onboarding** — Training reference for new Hermes agent operators

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Skill reference incomplete | Outdated skill version | Check for updates: `npx skills update` |
| Telegram integration fails | Bot token invalid | Verify bot token in agentiko config |
| Cron commands not working | Hermes version mismatch | Ensure Hermes v2.0+ |
| Delegation patterns differ | Custom Hermes config | Adapt patterns to your profile setup |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep agentiko-hermes
```

Test with a help prompt:
```
"What slash commands are available for Hermes Agent?"
```
