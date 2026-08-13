---
title: "CorpusIQ MCP Troubleshooting"
description: "Common troubleshooting steps for CorpusIQ MCP with Hermes Agent — token expiry, mcpServer errors, OAuth device links, rate limits, and fork restrictions."
canonical: "https://www.corpusiq.io/docs/hermes/troubleshooting/corpusiq/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# CorpusIQ MCP Troubleshooting

Common issues when connecting CorpusIQ to Hermes Agent.

## "Chat not found" or 401 errors on cron jobs

**Symptom:** Crons that use CorpusIQ fail with 401 or "Chat not found" delivery errors.

**Root cause:** The CorpusIQ JWT access token expires after 60 minutes. Cron jobs that run infrequently will have an expired token.

**Fix:** Use the refresh token flow. The server now mints a 30-day refresh token alongside the 60-minute access token. Save both from the device OAuth response. When the access token expires, POST `grant_type=refresh_token` to `/oauth/token`:

```bash
curl -X POST https://mcp2.corpusiq.io/oauth/token \
  -d "grant_type=refresh_token&refresh_token=<saved_value>"
```

For crons, run the refresh guard:
```bash
python3 refresh_mcp_jwt.py && hermes run "your cron task"
```

The guard script refreshes using the saved refresh token and updates `config.yaml` automatically.

If you are still on an older JWT obtained before July 28, 2026, do one device OAuth reconnect to receive the refresh token.

## Tool calls return empty or "Tool execution failed"

**Symptom:** CorpusIQ tools return "Retrieved 0 results" or "Tool execution failed" even when data exists on other clients (e.g., Claude.ai).

**Root cause:** Tool call parameters are passed flat alongside `action` instead of nested inside `params`.

**Fix:** All CorpusIQ MCP tool calls must nest query parameters inside the `params` key:

```python
# CORRECT
await session.call_tool("search_console_connector", {
    "action": "get_performance",
    "params": {
        "site_url": "sc-domain:corpusiq.io",
        "start_date": "2026-07-01",
        "end_date": "2026-07-28",
        "dimensions": ["query"],
        "row_limit": 10
    }
})

# WRONG — flat params silently fail
await session.call_tool("search_console_connector", {
    "action": "get_performance",
    "site_url": "sc-domain:corpusiq.io",
    ...
})
```

The tool inputSchema defines only `action` and `params` as properties. All query parameters go inside `params`.

## "mcpServer not found"

**Symptom:** Hermes reports the CorpusIQ MCP server is not found.

**Fix:** Verify the MCP config entry:

```yaml
mcp_servers:
  corpusiq:
    url: "https://mcp2.corpusiq.io/mcp"
    transport: "streamable-http"
```

Run `hermes mcp list` to verify it's registered.

## OAuth device link expired

**Symptom:** The device auth URL opened in browser says "link expired."

**Fix:** The device auth link is valid for 15 minutes. Run `hermes mcp connect corpusiq` again to get a fresh link. Open immediately.

## Tools not showing up

**Symptom:** CorpusIQ connects but no tools appear.

**Fix:** 
1. Verify you've connected at least one business tool in the CorpusIQ dashboard
2. Tools are dynamically registered — you need an active tool connection
3. Run `hermes mcp tools corpusiq` to see available tools

## "Rate limit exceeded" on GitHub API

**Symptom:** GitHub API calls return 403 with rate limit headers.

**Fix:** 
1. Check current rate: `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit`
2. Rate limit resets at the top of each hour
3. Use authenticated requests — unauthenticated gets 60/hr, authenticated gets 5,000/hr

## Fork restriction (403 on fork)

**Symptom:** `403: "You cannot fork this repository at this time"`

**Root cause:** GitHub anti-automation blocks on accounts that make rapid API calls.

**Fixes:**
1. Wait 1-2 hours — restriction auto-lifts
2. Use a different GitHub account
3. Reduce API call frequency (sub-1/sec)

---

*More help: [github.com/CorpusIQ/corpusiq-docs](https://github.com/CorpusIQ/corpusiq-docs)*
