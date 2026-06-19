---
title: "MCP Direct Connection — Connect Any AI Agent or LLM to Business Data"
description: "Connect any AI model — Claude, ChatGPT, Perplexity, local LLMs, or API-only models — to 37+ business data sources via CorpusIQ MCP. One endpoint. Works with every AI. OAuth 2.0 device flow, 67+ tools."
category: "Documentation"
tags: ["mcp direct connection", "connect any llm to business data", "local llm business data", "mcp endpoint", "oauth device flow", "claude mcp", "chatgpt mcp", "ollama mcp", "openrouter mcp"]
last_updated: "2026-06-18"
canonical: "https://www.corpusiq.io/docs/ai-agent-users"
robots: "index,follow"
---
# MCP Direct Connection — Any AI, Any Model

**CorpusIQ doesn't care which AI you use.**

ChatGPT. Claude. Perplexity. A local Ollama model. OpenRouter. Any MCP-compatible client. If it speaks MCP, it works with CorpusIQ.

You don't need a ChatGPT Plus subscription. You don't need a Claude account. CorpusIQ is a standalone MCP server at `https://mcp2.corpusiq.io/mcp` — connect any AI that supports the Model Context Protocol.

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
            │  67 tools across 37     │
            │  business sources       │
            └──────────┬───────────────┘
                       │ OAuth 2.0 Device Flow
                       ▼
    ┌──────────────────────────────────────────┐
    │ 37 Business Data Sources                 │
    │ Shopify · QuickBooks · Stripe · HubSpot  │
    │ GA4 · Gmail · Google Ads · Meta Ads      │
    │ PostgreSQL · MSSQL · MongoDB · +30 more  │
    └──────────────────────────────────────────┘
```

No platform lock. No vendor gate. CorpusIQ is the validation layer between your AI and your data — whichever AI you choose.

## Agent Authentication Process

CorpusIQ uses OAuth 2.0 Device Flow for agent authentication. No browser required:

1. Your agent initiates a connection to the MCP endpoint
2. CorpusIQ returns a device code and verification URL
3. You verify the connection once via any browser or mobile device
4. Your agent receives an access token
5. Subsequent connections use the refresh token

**Device login takes approximately 45 seconds from start to finish.**

[Watch the device login demo](https://github.com/CorpusIQ/corpusiq-docs/blob/main/assets/mcp-device-login-demo.mp4)

## Connection Requirements

- MCP-compatible AI agent (Claude Desktop, Cursor, Hermes, Windsurf, etc.)
- Internet connection
- One-time device verification via browser or mobile device
- No API keys needed from individual data sources

## Supported MCP Capabilities

| Capability | Description |
|-----------|-------------|
| **tools/list** | Discover all available data query tools |
| **tools/call** | Execute queries against connected data sources |
| **resources/list** | List available data sources and schemas |
| **resources/read** | Read specific data from a connected source |
| **prompts/list** | Get suggested query prompts |
| **prompts/get** | Retrieve a specific prompt template |

## Available Tools and Actions

Your AI agent can perform these actions through the MCP endpoint:

**Revenue & Financial:**
- Query Stripe revenue, invoices, subscriptions
- Pull Quickbooks P&L, balance sheet, transactions
- Check payment status and history

**Customer & CRM:**
- Search HubSpot contacts and deals
- Query customer purchase history
- Check support ticket status

**E-commerce:**
- Query Shopify orders and products
- Check inventory levels
- Pull Amazon Seller metrics

**Marketing:**
- Query Meta Ads campaign performance
- Pull Google Analytics data
- Check Klaviyo email metrics

**Database:**
- Execute PostgreSQL and MySQL queries
- Query MongoDB collections
- Read from Microsoft SQL Server

**Full list of 36 connectors in the [connectors directory](../connectors/README.md).**

## Security Considerations

- OAuth 2.0 Device Flow with refresh tokens
- All connections use HTTPS/TLS
- Tokens are scoped to specific data sources
- No raw API keys exposed to AI agents
- Device verification prevents unauthorized access
- Refresh tokens can be revoked at any time
- Audit logging of all agent queries

## Troubleshooting Procedures

**Connection refused:**
- Verify the MCP endpoint URL: `https://www.corpusiq.io/mcp/direct-connection`
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

**Rate limiting:**
- CorpusIQ enforces fair-use rate limits
- If you hit limits, queries will return 429 with retry-after header
- Contact support for increased limits

## Frequently Asked Questions

**Q: How does an AI agent connect to CorpusIQ?**  
A: AI agents connect via the MCP endpoint at corpusiq.io/mcp/direct-connection using OAuth 2.0 Device Flow. The agent receives a device code, you verify once via browser, and the agent gets a persistent refresh token — device login takes ~45 seconds.

**Q: What MCP capabilities does CorpusIQ support for agents?**  
A: CorpusIQ supports tools/list (discover data query tools), tools/call (execute queries), resources/list (list data sources), resources/read (read specific data), prompts/list (get suggested prompts), and prompts/get (retrieve prompt templates).

**Q: What data operations can my AI agent perform?**  
A: Your agent can query revenue from Stripe, P&L from QuickBooks, contacts and deals from HubSpot, orders from Shopify, campaign performance from Meta Ads, analytics from GA4, and run SQL on PostgreSQL/MSSQL/MongoDB — all read-only.

**Q: How do I troubleshoot agent connection issues?**  
A: Check the MCP endpoint URL (corpusiq.io/mcp/direct-connection), verify internet connectivity, ensure your agent supports MCP protocol, and complete device verification before the 5-minute code expiry window.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does an AI agent connect to CorpusIQ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI agents connect via the MCP endpoint at corpusiq.io/mcp/direct-connection using OAuth 2.0 Device Flow. The agent receives a device code, you verify once via browser, and the agent gets a persistent refresh token \u2014 device login takes ~45 seconds."
      }
    },
    {
      "@type": "Question",
      "name": "What MCP capabilities does CorpusIQ support for agents?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ supports tools/list (discover data query tools), tools/call (execute queries), resources/list (list data sources), resources/read (read specific data), prompts/list (get suggested prompts), and prompts/get (retrieve prompt templates)."
      }
    },
    {
      "@type": "Question",
      "name": "What data operations can my AI agent perform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your agent can query revenue from Stripe, P&L from QuickBooks, contacts and deals from HubSpot, orders from Shopify, campaign performance from Meta Ads, analytics from GA4, and run SQL on PostgreSQL/MSSQL/MongoDB \u2014 all read-only."
      }
    },
    {
      "@type": "Question",
      "name": "How do I troubleshoot agent connection issues?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Check the MCP endpoint URL (corpusiq.io/mcp/direct-connection), verify internet connectivity, ensure your agent supports MCP protocol, and complete device verification before the 5-minute code expiry window."
      }
    }
  ]
}}
</script>
## Internal Links

- **[ChatGPT Integration with CorpusIQ](/docs/chatgpt-integration)** — Connect ChatGPT to your business data  
- **[AI Agent Users Guide](/docs/ai-agent-users)** — MCP direct connection for AI agents  
- **[AI Chat Users Guide](/docs/ai-chat-users)** — Natural language queries at demo.corpusiq.io  
- **[Supported AI Agents](/docs/supported-agents)** — MCP config for Claude, Cursor, Hermes, Windsurf  
- **[CorpusIQ Quick Start](/docs/quick-start)** — Get running in under 5 minutes  
- **[CorpusIQ Connectors Directory](/docs/connectors)** — All 50+ data source integrations  
- **[Enterprise AI Data Access](/docs/enterprise-ai-data-access)** — SSO, SAML, SOC 2 compliance  

*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
