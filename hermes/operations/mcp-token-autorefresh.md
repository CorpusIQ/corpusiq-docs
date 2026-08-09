# MCP Token Auto-Refresh for Hermes Agent

## Problem

CorpusIQ's Growth Agent runs 24/7 with 50+ crons. The MCP server JWT expires every hour. When the token silently expires, every cron fails. Without an external watchdog, the agent goes completely dark — as happened during a 48-hour outage on Aug 6-8, 2026.

The root cause: the internal MCP client caches connection state and does not auto-retry after token refresh. Config.yaml updates but the agent process doesn't pick up the change.

## Solution: Two-Layer Defense

### Layer 1: Token Auto-Refresh (System Cron)

Python script running every 30 minutes via system crontab. Refreshes the MCP JWT via OAuth refresh_token grant and updates both config.yaml and mcp_tokens.json.

**Design:** Runs as system cron (not Hermes cron). Survives Hermes failures. Uses existing refresh_token. Logs every refresh for audit trail.

### Layer 2: External Agent Watchdog (System Cron)

Daily check at 7 PM MST: MCP token freshness, social post activity, daily report delivery. Alerts founder via Gmail API on failure.

**Design:** Completely outside Hermes. Cannot be killed by the failures it monitors. Silent when healthy.

## Architecture

```
System Crontab (survives everything)
├── */30 * * * *  mcp_token_autorefresh.py   ← Token freshness
└── 0 19 * * *    agent_watchdog.py           ← Liveness check

Hermes Crontab (can fail silently)
├── 50+ growth crons
├── Social posting
└── Ecosystem discovery
```

## Why This Works

Hermes crons cannot monitor themselves. When MCP dies, all dependent crons die. The escalation tracker is itself a cron. The only reliable monitor is outside the system.

Cost: ~$0.02/month in API calls. Prevents unlimited downtime.

## Files

- `scripts/mcp_token_autorefresh.py`
- `scripts/agent_watchdog.py`

Part of the CorpusIQ Hermes Operations guide series.
