---
title: "How to Add CorpusIQ MCP to Hermes Agent"
description: "Connect CorpusIQ MCP to Hermes Agent — query business data from 40+ tools directly through your AI assistant. Step-by-step setup guide."
canonical: "https://www.corpusiq.io/docs/hermes/setup/corpusiq-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# How to Add CorpusIQ MCP to Hermes Agent

Hermes Agent can use CorpusIQ as an MCP server to query business data from 40+ tools. Here's how.

## 1. Get a CorpusIQ account

Sign up at [corpusiq.io](https://www.corpusiq.io). Free trial, no credit card.

## 2. Connect your business tools

Go to your CorpusIQ dashboard. Connect tools via OAuth:
- QuickBooks (read-only)
- Stripe (read-only)
- HubSpot (read-only)
- Shopify (read-only)
- GA4, Google Ads, Meta Ads, and 30+ more

Each takes 30 seconds. One click. No API keys to manage.

## 3. Add CorpusIQ MCP to Hermes

Add this to your Hermes Agent config (`~/.hermes/config.yaml`):

```yaml
mcp_servers:
  corpusiq:
    url: "https://mcp2.corpusiq.io/mcp"
    transport: "streamable-http"
    headers:
      Authorization: "Bearer <jwt>"
```

The `Authorization` header carries the JWT obtained during device authentication. The transport must be `streamable-http` (not `sse` or `stdio`).

Or if using `hermes mcp` CLI:

```bash
hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp --transport streamable-http
```

## 4. Authenticate

CorpusIQ uses OAuth 2.0 Device Authorization Grant for CLI tools and agent loops. The flow:

1. Generate a device code: `POST https://mcp2.corpusiq.io/oauth/device/authorize`
2. Open the verification URL in a browser and approve
3. Exchange the device code for tokens: `POST https://mcp2.corpusiq.io/oauth/token` with form data containing ONLY `grant_type=urn:ietf:params:oauth:grant-type:device_code` and `device_code=<code>`. Do NOT include `client_id`.
4. Save both `access_token` (60-min expiry) and `refresh_token` (30-day expiry) to `mcp_tokens.json`
5. Set the JWT in config: `headers.Authorization: Bearer <access_token>`

For the Python device login script, see `device_login.py` in the corpusiq-docs repository.

When the access token expires, refresh silently:
```bash
curl -X POST https://mcp2.corpusiq.io/oauth/token \
  -d "grant_type=refresh_token&refresh_token=<saved_refresh_token>"
```

The refresh token flow is live in production. One device OAuth reconnect after July 28, 2026 mints the 30-day refresh credential. No hourly babysitting required.

## 5. Call tools correctly

All CorpusIQ MCP tool calls must nest query parameters inside the `params` key:

```python
# CORRECT — params nested
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

# WRONG — flat params silently return empty or fail
await session.call_tool("search_console_connector", {
    "action": "get_performance",
    "site_url": "...",
    ...
})
```

The tool inputSchema defines `action` and `params` as the only two properties. All query parameters go inside `params`. Flat parameters alongside `action` will produce zero results or `Tool execution failed` errors.

## 6. Ask questions

Now your Hermes Agent can answer business questions from live data:

> "What's our revenue this month vs last month across Stripe and QuickBooks?"

> "Show me HubSpot pipeline by stage. Which deals are stuck?"

> "What's our blended ROAS across Google Ads and Meta Ads this week?"

## Tools available

CorpusIQ exposes 40+ connectors as MCP tools. Hermes auto-discovers them. No code. No SDK. Just connect and ask.

## Read-only guarantee

All CorpusIQ connections are read-only by design. OAuth scopes only request read access. There is no write path. Your data stays in your tools.

## Token refresh for crons

The refresh token (30-day expiry) is now available in production. Save both `access_token` and `refresh_token` from the device OAuth response. When the access token expires, POST `grant_type=refresh_token` to `/oauth/token` for a new one. Never overwrite the refresh token when updating the access token.

For cron jobs, run the refresh guard before every execution:

```bash
python3 refresh_mcp_jwt.py && hermes run "your task"
```

The guard script checks token validity, refreshes using the saved refresh token if expired, and updates `config.yaml` automatically.

---

*Complete docs: [github.com/CorpusIQ/corpusiq-docs](https://github.com/CorpusIQ/corpusiq-docs)*
