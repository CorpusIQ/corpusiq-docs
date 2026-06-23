---
title: Honcho Integration  --  Setup Guide for Hermes Agents
description: Complete setup guide for honcho-integration  --  persistent agent memory, session management, and peer context for Hermes agents via the Honcho MCP server.
---

# Honcho Integration Setup Guide

**Skill:** `honcho-integration` from [plastic-labs/honcho](https://skills.sh/plastic-labs/honcho/honcho-integration)
**Installs:** 534+
**Category:** Agent Memory & Context Management
**Hermes Compatibility:** Full  --  used in production by CorpusIQ Hermes agents

## 1. Prerequisites

- Hermes Agent installed and running
- A running Honcho server (self-hosted or Honcho Cloud)
- Python 3.10+ for the Honcho MCP server

## 2. What Honcho Does for Hermes Agents

Honcho provides persistent, cross-session memory for AI agents:

- **Session Memory:** Every conversation is stored and searchable  --  agents recover context after restarts
- **Peer Context:** Track what agents know about users, other agents, and themselves
- **Conclusion Derivation:** Automatically distill conversations into durable facts
- **Dream Cycle:** Background memory consolidation (analogous to human sleep)
- **Peer Cards:** Compact biographical summaries for quick context retrieval

For Hermes agents specifically, Honcho enables:

| Capability | MCP Tool | Use Case |
|---|---|---|
| Context recovery | `honcho_get_peer_context` | Recover channel status, token state, active rules after restart |
| Knowledge queries | `honcho_chat` | "What tokens are expired?" "What channels are banned?" |
| Session handoff | `honcho_get_session_context` | Pass context between agent sessions |
| Memory persistence | `honcho_create_conclusions` | Save durable facts that survive agent restarts |
| Dream scheduling | `honcho_schedule_dream` | Consolidate observations into insights |

## 3. Installation

```bash
# From skills.sh
npx skills add plastic-labs/honcho/honcho-integration

# Or clone directly
git clone https://github.com/plastic-labs/honcho.git
cd honcho
pip install honcho-ai
```

## 4. MCP Server Configuration

Add to your Hermes MCP config (`~/.hermes/config.yaml`):

```yaml
mcp:
  servers:
    honcho:
      command: python
      args: ["-m", "honcho.mcp.server"]
      env:
        HONCHO_API_KEY: "${HONCHO_API_KEY}"
        HONCHO_BASE_URL: "http://localhost:8000"
```

## 5. CLI Reference

| Command | Description |
|---------|-------------|
| `honcho-chat` | Query Honcho's knowledge about a peer |
| `honcho-create-conclusions` | Persist durable facts about a peer |
| `honcho-get-peer-context` | Full context: representation + peer card |
| `honcho-get-session-context` | Session messages optimized for LLM context window |
| `honcho-schedule-dream` | Trigger background memory consolidation |
| `honcho-search` | Semantic search across all messages |

## 6. CorpusIQ Production Pattern

The CorpusIQ session start ritual uses Honcho as the primary anti-amnesia mechanism:

```
1. honcho_get_peer_context(peer_id="hermes", target_peer_id="hermes")
   → Returns: channel bans, token expiry, cron state, active rules
   
2. honcho_chat(peer_id="hermes", query="What channels are blocked?")
   → Returns: current blocker status, resolution paths

3. After session: honcho_create_conclusions()
   → Persist: what was accomplished, any new rules, system changes
```

This one call replaces manually searching through SESSION_STATE.md, checking crons, and testing each channel.

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `honcho_get_peer_context` returns "None" | New peer, no conclusions saved yet | Fall back to GBrain + session_search, then save conclusions |
| Honcho MCP tools time out (120s) | `get_connector_status` is slow | Use `hermes mcp test corpusiq` instead  --  returns in <1s |
| Dream cycle not completing | Background queue backed up | Check `honcho_get_queue_status`, schedule dream manually |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Honcho CLI Setup](/hermes/skills/catalog/honcho-cli-setup/) →*
