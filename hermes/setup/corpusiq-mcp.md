---
title: "How to Add CorpusIQ MCP to Hermes Agent"
description: "Connect CorpusIQ MCP to Hermes Agent — query business data from 37+ tools directly through your AI assistant. Step-by-step setup guide."
---

# How to Add CorpusIQ MCP to Hermes Agent

Hermes Agent can use CorpusIQ as an MCP server to query business data from 37+ tools. Here's how.

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
```

Or if using `hermes mcp` CLI:

```bash
hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp --transport streamable-http
```

## 4. Authenticate

Hermes will open a device auth link. Open it in a browser, approve the connection. The JWT token auto-saves.

## 5. Ask questions

Now your Hermes Agent can answer business questions from live data:

> "What's our revenue this month vs last month across Stripe and QuickBooks?"

> "Show me HubSpot pipeline by stage. Which deals are stuck?"

> "What's our blended ROAS across Google Ads and Meta Ads this week?"

## Tools available

CorpusIQ exposes all 37+ connectors as MCP tools. Hermes auto-discovers them. No code. No SDK. Just connect and ask.

## Read-only guarantee

All CorpusIQ connections are read-only by design. OAuth scopes only request read access. There is no write path. Your data stays in your tools.

## Token refresh for crons

If you're running Hermes crons with CorpusIQ, the JWT expires hourly. Use the token refresh guard:

```bash
python3 token_refresh_guard.py && hermes run "your task"
```

This checks token validity before every run and auto-refreshes if needed.

---

*Complete docs: [github.com/CorpusIQ/corpusiq-docs](https://github.com/CorpusIQ/corpusiq-docs)*
