---
title: "MCP Direct Connection"
description: "Connect any AI model  --  Claude, ChatGPT, Perplexity, local LLMs, or API-only models  --  to 38+ business data sources via CorpusIQ MCP. One endpoint. Works with every AI. OAuth 2.0 device flow, ~500 tools, 150+ skills."
category: "Documentation"
tags: ["mcp direct connection", "connect any llm to business data", "local llm business data", "mcp endpoint", "oauth device flow", "claude mcp", "chatgpt mcp", "ollama mcp", "openrouter mcp"]
last_updated: "2026-06-18"
canonical: "https://www.corpusiq.io/docs/ai-agent-users"
robots: "index,follow"
---
# MCP Direct Connection  --  Any AI, Any Model

**CorpusIQ doesn't care which AI you use.**

ChatGPT. Claude. Perplexity. A local Ollama model. OpenRouter. Any MCP-compatible client. If it speaks MCP, it works with CorpusIQ.

You don't need a ChatGPT Plus subscription. You don't need a Claude account. CorpusIQ is a standalone MCP server at `https://mcp2.corpusiq.io/mcp`  --  connect any AI that supports the Model Context Protocol.

38 connectors. 150+ pre-built skills. Nearly 500 tools. All through one MCP endpoint.

## One Endpoint. Every AI.

```
            ┌─────────────────────────┐
            │   Any AI Model           │
            │   Claude | ChatGPT       │
            │   Local LLM | API        │
            │   Perplexity | Agent     │
            └──────────┬──────────────┘
                       │ MCP Protocol
                       ▼
            ┌──────────────────────────┐
            │  CorpusIQ MCP Endpoint   │
            │  mcp2.corpusiq.io/mcp   │
            │  ~500 tools across 38   │
            │  business connectors    │
            └──────────┬───────────────┘
                       │ OAuth 2.0 Device Flow
                       ▼
    ┌──────────────────────────────────────────┐
    │ 38 Business Data Sources                 │
    │ Shopify · QuickBooks · Stripe · HubSpot  │
    │ GA4 · Gmail · Google Ads · Meta Ads      │
    │ PostgreSQL · MSSQL · MongoDB · +29 more  │
    └──────────────────────────────────────────┘
```

No platform lock. No vendor gate. CorpusIQ is the validation layer between your AI and your data  --  whichever AI you choose.

## Agent Authentication Process

CorpusIQ uses OAuth 2.0 Device Flow for agent authentication. No browser required on the agent side:

1. Your agent initiates a connection to `https://mcp2.corpusiq.io/mcp`
2. CorpusIQ returns a device code and verification URL
3. You verify the connection once via any browser or mobile device
4. Your agent receives an access token
5. Subsequent connections use the refresh token

**Device login takes approximately 45 seconds from start to finish.**

[Watch the device login demo](https://github.com/CorpusIQ/corpusiq-docs/blob/main/assets/mcp-device-login-demo.mp4)

## Connection Requirements

- Any MCP-compatible AI (Claude, Cursor, Hermes, Windsurf, local LLM, or custom client)
- Internet connection
- One-time device verification via browser or mobile device
- No API keys needed from individual data sources

## Supported MCP Capabilities

| Capability | Description |
|-----------|-------------|
| **tools/list** | Discover all ~500 available data query tools |
| **tools/call** | Execute queries against connected data sources |
| **resources/list** | List available data sources and schemas |
| **resources/read** | Read specific data from a connected source |

## Available Tools and Actions

Your AI can query across 38 connectors through the MCP endpoint:

**Revenue & Financial:**
- Query Stripe revenue, invoices, subscriptions
- Pull QuickBooks P&L, balance sheet, transactions
- Check payment status and history

**Customer & CRM:**
- Search HubSpot contacts and deals
- Query customer purchase history
- Access Close CRM, LeadConnector, Axonaut

**E-commerce:**
- Query Shopify orders and products
- Check inventory levels
- Pull Amazon Seller and eBay metrics

**Marketing:**
- Query Meta Ads campaign performance
- Pull Google Analytics (GA4) data
- Check Klaviyo, Mailchimp, ActiveCampaign email metrics

**Database:**
- Execute PostgreSQL and MSSQL queries
- Query MongoDB collections
- Query Azure CosmosDB

**Full connector list: 34 total  --  view in your [CorpusIQ dashboard](https://www.corpusiq.io/dashboard) after signing up.**

## Security Considerations

- OAuth 2.0 Device Flow with refresh tokens
- All connections use HTTPS/TLS
- Tokens scoped to specific data sources
- No raw API keys exposed to AI agents
- Device verification prevents unauthorized access
- Refresh tokens revocable at any time
- Audit logging of all queries

## Troubleshooting

**Connection refused:**
- Verify the MCP endpoint URL: `https://mcp2.corpusiq.io/mcp`
- Check internet connectivity
- Ensure your agent supports MCP protocol

**Authentication failed:**
- Verify your device code hasn't expired (5 minute window)
- Complete device verification at the provided URL
- Check that your account has active data source connections

**Tool not found:**
- Run `tools/list` to see available tools
- Ensure your data sources are connected in the CorpusIQ dashboard
- Some tools require specific data source connections

## Frequently Asked Questions

**Q: How does an AI agent connect to CorpusIQ?**  
A: Connect via `https://mcp2.corpusiq.io/mcp` using OAuth 2.0 Device Flow. Your agent receives a device code, you verify once via browser, and the agent gets a persistent refresh token  --  takes ~45 seconds.

**Q: What AIs work with CorpusIQ?**  
A: Any MCP-compatible client. Claude, ChatGPT, Perplexity, local Ollama models, OpenRouter, Cursor, Hermes, Windsurf, and any custom Python/Node.js client using the MCP protocol.

**Q: Do I need a ChatGPT or Claude subscription?**  
A: No. CorpusIQ is a standalone MCP server. You can use it with a local LLM, any API provider, or any MCP-compatible tool. No vendor lock.

**Q: What data operations can my AI agent perform?**  
A: Your agent can query ~500 tools across 34 business connectors  --  Stripe revenue, QuickBooks P&L, HubSpot deals, Shopify orders, Meta Ads campaigns, GA4 analytics, PostgreSQL/MSSQL/MongoDB queries  --  all read-only.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
