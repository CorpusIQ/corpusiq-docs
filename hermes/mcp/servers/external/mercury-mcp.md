---
title: "Mercury MCP — Business Banking Data for AI Agents"
description: "Official Mercury MCP server (beta) giving AI agents read-only access to accounts, transactions, balances, and cards via OAuth 2.0. Hosted at mcp.mercury.com/mcp with Dynamic Client Registration support."
category: mcp
tags: [mcp-server, fintech, banking, mercury, official, finance, startup-operations]
last_updated: 2026-07-17
---

# Mercury MCP Server ★ Official (Beta) — New July 17

Mercury's official MCP server connects AI agents to your Mercury business banking data — accounts, transactions, balances, and cards — through a secure OAuth 2.0 flow. The hosted server at `https://mcp.mercury.com/mcp` supports Dynamic Client Registration (RFC 7591) so you can register clients without manual setup.

This is a landmark MCP server: Mercury is the first banking platform to ship an official MCP server, enabling AI agents to access financial data in a read-only, OAuth-secured model.

**Source:** mcp.so (discovered July 17, 2026)
**Category:** Finance / Banking / Startup Operations
**Author:** Mercury (Official)
**Docs:** https://docs.mercury.com/docs/connecting-mercury-mcp
**Endpoint:** https://mcp.mercury.com/mcp
**Status:** Beta (MCP added ~July 6, 2026)

## What It Does

- **Accounts** — list and view Mercury business accounts
- **Transactions** — search and retrieve transaction history
- **Balances** — check current balances across accounts
- **Cards** — view Mercury debit/credit card information
- **Read-only by design** — Mercury scoped the MCP to prevent unintended actions

## Key Innovation: Banking Data Without Credential Exposure

Mercury's MCP design mirrors the emerging enterprise pattern: the agent orchestrates financial queries while OAuth enforces the security boundary. Your Mercury login credentials are never shared with the AI tool — authentication happens through Mercury's OAuth flow.

Sessions remain active for 3 days per chat thread, after which re-authentication is required.

## Setup

### Quick Start (Claude/ChatGPT)

1. Open **Add Connectors** in Claude or **Apps & Connectors** in ChatGPT
2. Create a new custom connection
3. Add Mercury as a new MCP using URL: `https://mcp.mercury.com/mcp`
4. Start a chat asking about Mercury data — OAuth login prompt appears
5. Authenticate with your Mercury credentials

### Dynamic Client Registration (For App Developers)

Mercury supports OAuth 2.0 Dynamic Client Registration (RFC 7591). Register your client:

```bash
curl -X POST https://mcp.mercury.com/register \
  -H "Content-Type: application/json" \
  -d '{
    "redirect_uris": ["https://your-app.com/callback"],
    "client_name": "Your App Name"
  }'
```

You'll receive a `client_id` and `client_secret` for the standard OAuth authorization code flow. Client names must not contain "Mercury."

### Hermes/Claude Code Config

```json
{
  "mcpServers": {
    "mercury": {
      "url": "https://mcp.mercury.com/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Business Relevance

1. **First banking MCP:** Mercury is the first financial institution to ship an official MCP server. This signals that regulated financial services are embracing the protocol.

2. **Operator dashboard in AI:** Business operators can query account balances, recent transactions, and card activity directly from their AI workspace — no context-switching to Mercury's dashboard.

3. **Startup finance automation:** AI agents can monitor cash position, flag unusual transactions, and generate financial summaries without manual data entry or API integration work.

4. **Read-only safety:** Mercury's scoping to read-only access is the right pattern for financial MCP servers. Operators get data visibility without risking unintended transfers.

## Use Cases for Business Operators

- **Daily cash position check:** "What's my current balance across all Mercury accounts?"
- **Transaction monitoring:** "Show me all transactions over $5,000 this week."
- **Spend categorization:** "Categorize last month's card transactions by vendor type."
- **Financial snapshots:** "Give me a summary of cash flow for the past 30 days."
- **Vendor analysis:** "How much have we paid AWS this quarter?"

## Limitations

- **Hosted only:** Mercury does not offer a non-hosted/local MCP at this time
- **Read-only:** No transaction creation, transfers, or account management via MCP
- **3-day sessions:** OAuth sessions expire after 3 days per thread
- **Beta status:** API may change; production reliance should include fallback

## See Also

- [Asana MCP](/hermes/mcp/servers/external/asana-mcp/) — project management MCP
- [1Password MCP](/hermes/mcp/servers/external/1password-mcp/) — secrets management MCP
- [External MCP Catalog](/hermes/mcp/servers/external/)
