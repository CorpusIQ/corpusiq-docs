---
title: "MisarReach MCP - Outbound Sales and Lead Pipeline for AI Agents"
description: "MisarReach MCP server with 27 tools for outbound sales: build and qualify lead lists, verify emails, run multi-step outreach sequences across channels, check deliverability and review pipeline from any MCP client"
category: Sales Outreach
stars: n/a (new listing)
added: 2026-08-19
source: "mcp.so GitHub issue #3639"
relevance: ★★
tags: [sales, outbound, lead-generation, email-verification, cold-outreach, pipeline, remote-mcp, npm]
---

# MisarReach MCP

**Outbound sales from any MCP client — build and qualify lead lists, verify emails, run multi-step outreach sequences across channels, check deliverability, and review the pipeline with 27 tools.** Available as a local npm server or a hosted streamable-HTTP endpoint, with an optional API key (the server answers `initialize` and `tools/list` unauthenticated and exposes a browser `login` tool).

```
Server type: Local (npm, stdio) or Remote (Streamable HTTP)
Auth: Optional API key (browser login tool included)
Endpoint: https://api.misar.io/reach/mcp
Package: npx -y @misarreach/mcp (v5.1.1, MIT)
Tools: 27
Pricing: Free tier available
Category: Sales Outreach
Built by: Misar AI
```

## Why This Matters for Operators

Operators who run outbound motion currently stitch together list building, verification, sequencing, and CRM review across four or five tools. MisarReach collapses the whole outbound stack into one MCP server: an agent can build a lead list, verify the addresses, launch a multi-step sequence across channels, check deliverability before the blast, and review pipeline health — all inside the assistant it already uses, without leaving the conversation for a separate sales platform.

The optional-auth design matters for automation: tools can be listed and inspected without a key, so evaluation costs nothing, and the browser login flow handles the human approval step when a key is needed.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| Lead discovery | Build and qualify lead lists from search criteria and company signals |
| Email verification | Verify addresses before sending, cutting bounce risk |
| Outreach sequences | Run multi-step, multi-channel sequences (email, follow-ups) |
| Deliverability checks | Check domain and content deliverability before campaigns |
| Pipeline review | Review pipeline state and stage movement |

## Installation

```bash
npx -y @misarreach/mcp
```

Or add the remote server to any MCP client:

```json
{
  "mcpServers": {
    "misarreach": {
      "type": "http",
      "url": "https://api.misar.io/reach/mcp"
    }
  }
}
```

The API key is optional: `initialize` and `tools/list` answer unauthenticated, and the server exposes a browser `login` tool for interactive auth. For local stdio use, set `MISARREACH_API_KEY` in the environment when a key is configured.

## Configuration

```json
{
  "mcpServers": {
    "misarreach": {
      "command": "npx",
      "args": ["-y", "@misarreach/mcp"],
      "env": { "MISARREACH_API_KEY": "<optional>" }
    }
  }
}
```

Registry ID: `io.github.Misar-AI/misarreach-mcp`. MIT licensed, repository at `github.com/Misar-AI/misarreach-mcp`.

## Business Relevance

- **Sales operators** run lead list building, verification, and sequencing from chat instead of a sales platform
- **Founders and growth leads** test outbound motion without onboarding a full sales stack
- **Agencies** script repeatable outreach workflows for client accounts
- **RevOps** reviews pipeline stage movement inside the agent session
- **Automation builders** fold outbound steps into larger agent workflows via one endpoint

## Integration with CorpusIQ

CorpusIQ brings the money and customer layer (Stripe, CRM, QuickBooks) while MisarReach brings the outbound motion layer. A growth operator can run both in one agent session: CorpusIQ for pipeline accounting, deal tracking, and financials, MisarReach for lead generation, verification, and outreach sequences — then join the two on email or company name.

## Limitations

- New listing (Aug 2026), no track record; single-star repository
- Free tier scope not fully documented; some tools may require a paid Misar account
- Hosted endpoint is a third-party dependency for remote use
- Email deliverability depends on Misar's sending infrastructure, not yours

## See Also

- [MisarMail MCP — Transactional Email and Campaigns](/hermes/mcp/servers/external/misarmail-mcp/)
- [Misar.Blog MCP — Blog Publishing](/hermes/mcp/servers/external/misarblog-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
