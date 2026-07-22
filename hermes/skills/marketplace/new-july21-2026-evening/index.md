---
title: "New Skills — July 21, 2026 Marketplace Sweep (Evening)"
description: "7 additional Hermes-relevant skills discovered on skills.sh in evening sweep. 33.5K+ combined installs across the new batch. Evening sweep supplementing morning (10) and afternoon (6) discoveries."
---

# New Skills — July 21, 2026 (Evening)

Additional skills discovered during the July 21 evening marketplace sweep. 7 new setup guides created for Hermes agents. This supplements the morning sweep (10 skills, 458K installs) and afternoon sweep (6 skills, 12.3K installs).

## Summary

| Metric | Count |
|---|---|
| New skills found | 7 |
| Setup guides created | 7 |
| Combined installs | ~33,500+ |
| Quality: 🟢 Production | 1 |
| Quality: 🟡 Beta | 5 |
| Quality: 🔵 Community | 1 |

## New Skills

### Agent Self-Evolution & Infrastructure

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **self-improving-agent** | charon-fan/agent-playbook | 32,200 | 🟢 | [Setup Guide](/hermes/skills/catalog/self-improving-agent-setup/) |
| **hermes-agent-framework** | aradotso/ai-agent-skills | 176 | 🟡 | [Setup Guide](/hermes/skills/catalog/hermes-agent-framework-setup/) |

### Hermes UI & Workspace

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **hermes-webui-agent** | aradotso/hermes-skills | 240 | 🟡 | [Setup Guide](/hermes/skills/catalog/hermes-webui-agent-setup/) |
| **hermes-workspace-ai-agent-ui** | aradotso/hermes-skills | 196 | 🟡 | [Setup Guide](/hermes/skills/catalog/hermes-workspace-ai-agent-ui-setup/) |

### Security & MCP Integration

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **hermes-traffic-guardian** | prompt-security/clawsec | 42 | 🔵 | [Setup Guide](/hermes/skills/catalog/hermes-traffic-guardian-setup/) |
| **codex-mcp-server-integration** | aradotso/mcp-skills | 129 | 🟡 | [Setup Guide](/hermes/skills/catalog/codex-mcp-server-integration-setup/) |

### Growth & Marketing

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **social-media-marketing** | jk-0001/skills | 329 | 🟡 | [Setup Guide](/hermes/skills/catalog/social-media-marketing-setup/) |

## Notes

- **self-improving-agent** (32.2K installs) is the standout discovery — a universal agent self-evolution framework based on 2025 lifelong learning research. Uses multi-memory architecture (semantic + episodic + working) with hooks-based self-correction.
- **hermes-webui-agent** and **hermes-workspace-ai-agent-ui** extend the Hermes agent UI ecosystem with two different approaches: WebUI (lightweight Flask, daemon-managed) and Workspace (Next.js, swarm-enabled, full IDE-like experience).
- **hermes-traffic-guardian** is a specification-only skill (v0.0.1-beta5) from Prompt Security — builders implement the runtime. Currently a baseline for Hermes security posture integration.
- **codex-mcp-server-integration** bridges OpenAI Codex CLI into MCP-compatible editors, enabling AI code review and generation without leaving Hermes.
- These 7 skills were discovered using `npx skills find` with 16 targeted queries across Hermes, OpenClaw, MCP, security, and marketing domains.
- Total catalog now covers 347+ Hermes-relevant skills from skills.sh and community sources. Today's three sweeps (morning, afternoon, evening) added 23 total new setup guides.
