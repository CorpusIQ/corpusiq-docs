---
title: hermes-studio-dashboard — Setup Guide
description: Web dashboard for Hermes Agent with multi-platform AI chat, session management, scheduled jobs, and usage analytics. From aradotso/hermes-skills.
---

# hermes-studio-dashboard — Setup Guide

**Source:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)
**Skill:** `hermes-studio-dashboard`
**Installs:** 38

A web-based management dashboard for Hermes Agent. Provides multi-platform AI chat interface, session management, scheduled job monitoring, and usage analytics — all from a browser UI.

## Installation

```bash
npx skills add aradotso/hermes-skills --skill hermes-studio-dashboard
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v2.0+ |
| Node.js | v18+ |
| Web browser | For dashboard UI access |
| Hermes gateway | Running for session/chat data |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Multi-platform chat | "Open the Hermes dashboard" | Web UI with chat interface |
| Session management | View active sessions in dashboard | Session list with controls |
| Job scheduling | Monitor cron/scheduled jobs | Job status dashboard |
| Usage analytics | View agent usage stats | Analytics charts and metrics |

## CLI/Command Reference

Once installed and loaded, the skill provides a web dashboard accessible at a local port:

```bash
# The dashboard typically starts on a local port — check output after skill activation
# Common: http://localhost:3000 or similar
```

## CorpusIQ Use Cases

1. **Multi-agent monitoring** — Monitor all CorpusIQ Hermes agents from one dashboard
2. **Session oversight** — Track active sessions across profiles (corpusiq, dev, support)
3. **Job health checks** — Monitor cron job execution status visually
4. **Usage analytics** — Track agent token usage and model routing patterns
5. **Team operations** — Provide dashboard access to team members for agent oversight

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Dashboard won't start | Port conflict | Check if port is in use: `lsof -i :3000` |
| No session data | Gateway not running | Ensure `hermes gateway status` shows active |
| Analytics empty | No usage data yet | Dashboard populates over time |
| UI not loading | Firewall/network | Check localhost access, try different port |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep hermes-studio-dashboard
```

The dashboard should be accessible after skill activation — check terminal output for the URL.
