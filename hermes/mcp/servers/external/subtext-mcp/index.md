---
title: "Subtext — Agent Session Replay MCP"
description: "Session replay built for AI agents. Captures production sessions and connects them to your coding agent for debugging and analysis. 9 GitHub stars. By Fullstory."
category: mcp
tags: [mcp-server, agent-analytics, session-replay, debugging, monitoring]
source: mcp.so
discovered: 2026-07-22
stars: 9
author: Subtext by Fullstory
---

# Subtext MCP

**Agent-native session replay** from Fullstory. Captures production sessions of your application and connects them to your coding agent — Claude Code, Cursor, Codex — so it can debug issues, analyze user behavior, and improve UX from real session data.

## Why It Matters for Operators

For operators running SaaS products or web applications, Subtext MCP bridges the gap between production issues and AI-driven debugging:

- **Agent-Driven Debugging:** Your AI agent replays the exact user session where a bug occurred
- **UX Analysis:** AI reviews real user sessions to identify friction points
- **Support Triage:** Connect support tickets to session replays for faster resolution
- **No Context Switching:** Debug production issues without leaving your coding agent

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Remote MCP |
| **Auth** | API Key (Fullstory/Subtext account required) |
| **Category** | Data & Analytics |
| **Source** | [mcp.so/servers/subtext](https://mcp.so/servers/subtext) |
| **Author** | Subtext by Fullstory |
| **Created** | July 21, 2026 |
| **Stars** | ⭐ 9 |
| **Verified** | ✅ |

## Setup

### Claude Code / Codex
```bash
claude mcp add subtext --url https://api.subtext.fullstory.com/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

## CorpusIQ Integration

Subtext helps operators who use CorpusIQ alongside customer-facing applications:

1. **Bug → Fix Pipeline:** Customer reports issue → Subtext replays session → Agent diagnoses → fix deployed
2. **Conversion Analysis:** Subtext session replays + CorpusIQ Stripe data = full purchase funnel visibility
3. **Support Efficiency:** Reduce time-to-resolution by giving agents direct access to session context

## Limitations

- Requires Fullstory/Subtext subscription
- 9 stars — early adoption, API may evolve
- Only useful for operators with web applications (not API-only products)
- Session data can be large — consider sampling for agent analysis

## See Also

- [[index]] — Full external MCP catalog
- AppAmbit MCP — Mobile app analytics MCP
- Fleets — Multi-site analytics MCP
