---
title: "MailStream — Physical Mail MCP: Postcards & Letters from AI Agents"
description: "The first MCP server for physical mail. Send postcards and letters, manage mailing lists and campaigns — all through AI agent commands."
source: mailstream.app
stars: 0
language: N/A (Hosted SaaS)
transport: Streamable HTTP
auth: API Key
category: Marketing & Direct Mail
last_updated: 2026-07-21
---

# MailStream — Physical Mail MCP for AI Agents

**Physical mail operations through MCP.** MailStream is the first MCP server that lets AI agents send real postcards, letters, and manage direct mail campaigns. Operators can trigger physical mail from the same AI conversation where they're analyzing customer data.

## What It Does for Operators

- **Send postcards** — AI agents can trigger physical postcard sends to mailing lists
- **Send letters** — Full letter mailing with templates and personalization
- **Campaign management** — Create, manage, and track direct mail campaigns
- **List management** — Upload and manage mailing lists
- **Agent-native** — All direct mail operations through MCP tools

## Installation

```bash
# No installation — hosted platform
# Sign up at mailstream.app, configure campaigns
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "mailstream": {
      "type": "url",
      "url": "https://mailstream.app/developers/mcp-server"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `send_postcard` | Send a physical postcard to a recipient or list |
| `send_letter` | Send a physical letter with template |
| `create_campaign` | Set up a new direct mail campaign |
| `get_campaign_status` | Check delivery status and response rates |
| `manage_lists` | Upload, clean, and segment mailing lists |
| `estimate_cost` | Calculate postage and printing costs |

*Note: Tool names are approximate. Full documentation at mailstream.app.*

## Operator Use Cases

1. **Ecommerce Brands** — Trigger "We miss you" postcards to lapsed customers from AI agent
2. **B2B Sales** — Send personalized letters to high-value prospects after AI research
3. **Real Estate** — Automated "Just Sold" postcards to neighborhoods
4. **Non-Profits** — Thank-you letters triggered by donation events

## CorpusIQ Angle

MailStream bridges the digital-physical gap for operators. A complete workflow: (1) CorpusIQ identifies lapsed customers from Shopify/Stripe data → (2) AI agent drafts personalized reactivation offer → (3) MailStream sends physical postcard → (4) CorpusIQ tracks revenue impact. Physical mail as an AI-native channel.

## Limitations

- US-only delivery (as of July 2026)
- Physical mail has ~3-5 day delivery lag (not instant like email)
- Per-piece costs (postage + printing)
- Template design requires setup outside MCP
