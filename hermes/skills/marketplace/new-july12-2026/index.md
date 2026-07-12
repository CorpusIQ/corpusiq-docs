---
title: New Skills Discovery — July 12, 2026
description: 9 new Hermes and OpenClaw ecosystem skills discovered via skills.sh API sweep. OpenClaw plugin testing tools, skill distribution utility, Solana plugins, WeChat integration, and more.
---

# New Skills Discovery — July 12, 2026

**Date:** July 12, 2026
**Method:** skills.sh API sweep (10 standard + 15 broader ecosystem queries)
**Results:** 317 unique skills surfaced, 9 genuinely new Hermes/OpenClaw-relevant

---

## Summary

| Category | Skills | Total Installs |
|---|---|---|
| OpenClaw Ecosystem | 7 | 262 |
| Hermes Agent Utility | 1 | 59 |
| Agent Infrastructure | 1 | 55 |

**New & Noteworthy:**

- **distribute-skill-to-all-agents** (59 installs) — Sync skills across Codex, Claude Code, Pi, and Hermes agent folders. Canonical location management with symlink verification.
- **openclaw-pre-release-plugin-testing** (62 installs) — Test OpenClaw plugins in pre-release environments from steipete/clawdis.
- **openclaw-weixin-setup** (33 installs) — WeChat/Weixin integration for OpenClaw agents from skills.volces.com.

---

## All Discovered Skills

### Category: OpenClaw Plugin Development

| Skill | Installs | Source | Description |
|---|---|---|---|
| **openclaw-pre-release-plugin-testing** | 62 | steipete/clawdis | Pre-release plugin testing workflow for OpenClaw |
| **release-openclaw-plugin-testing** | 42 | steipete/clawdis | Production release testing pipeline for OpenClaw plugins |
| **openclaw-ref** | 30 | tenequm/skills | OpenClaw reference implementation and documentation |
| **openclaw-weixin-setup** | 33 | skills.volces.com | WeChat/Weixin integration for OpenClaw agents |

### Category: OpenClaw Platform Integrations

| Skill | Installs | Source | Description |
|---|---|---|---|
| **solana-trader** | 37 | solana-clawd/openclaw-solana-plugins | Solana blockchain trading plugin for OpenClaw |
| **bailian-multimodal-skills** | 26 | cclank/openclaw_provider_plugins | Bailian multimodal AI provider plugin for OpenClaw |

### Category: Hermes Agent Utilities

| Skill | Installs | Source | Description |
|---|---|---|---|
| **distribute-skill-to-all-agents** | 59 | davidondrej/skills | Distribute a skill across Codex, Claude Code, Pi, and Hermes agent skill folders. Manages symlink layout and verifies byte-identical copies. |

### Category: Agent Infrastructure

| Skill | Installs | Source | Description |
|---|---|---|---|
| **browser-harness** | 55 | davidondrej/skills | Browser automation harness for agent tools |

---

## Installation

```bash
# OpenClaw ecosystem
npx skills add steipete/clawdis --skill openclaw-pre-release-plugin-testing
npx skills add steipete/clawdis --skill release-openclaw-plugin-testing
npx skills add tenequm/skills --skill openclaw-ref
npx skills add skills.volces.com --skill openclaw-weixin-setup
npx skills add solana-clawd/openclaw-solana-plugins --skill solana-trader
npx skills add cclank/openclaw_provider_plugins --skill bailian-multimodal-skills

# Hermes utilities
npx skills add davidondrej/skills --skill distribute-skill-to-all-agents
npx skills add davidondrej/skills --skill browser-harness
```

---

## Notes

- **hermes-tweet** variants from wshobson/agents (72 installs) and davepoon/buildwithclaude (22 installs) surfaced but skipped — already catalogued as Xquik-dev/hermes-tweet in the ecosystem index.
- All OpenClaw skills are niche but extend the ecosystem into plugin testing, blockchain, WeChat, and multimodal AI — gaps not previously covered.
- `distribute-skill-to-all-agents` is the only genuinely new Hermes Agent skill. Full setup guide at [distribute-skill-to-all-agents →](/hermes/skills/catalog/distribute-skill-to-all-agents-setup/).

---

*← [Marketplace Index](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
