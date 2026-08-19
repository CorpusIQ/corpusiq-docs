---
title: "MisarMail MCP - Transactional Email and Campaigns for AI Agents"
description: "MisarMail MCP server with 54 tools for email operations: send transactional email, run multi-step campaigns, manage contacts segments and automations, A/B test, warm up domains and audit deliverability from any MCP client"
category: Email Marketing
stars: n/a (new listing)
added: 2026-08-19
source: "mcp.so GitHub issue #3644"
relevance: ★★
tags: [email, transactional-email, campaigns, automations, ab-testing, deliverability, remote-mcp, npm]
---

# MisarMail MCP

**Email operations from any MCP client — send transactional email, run multi-step campaigns, manage contacts, segments and automations, A/B test, warm up domains, and audit deliverability with 54 tools.** Available as a local npm server or a hosted streamable-HTTP endpoint, with an optional API key (the server answers `initialize` and `tools/list` unauthenticated and exposes a browser `login` tool).

```
Server type: Local (npm, stdio) or Remote (Streamable HTTP)
Auth: Optional API key (browser login tool included)
Endpoint: https://mail.misar.io/api/mcp
Package: npx -y @misarmail/mcp (v5.1.1, MIT)
Tools: 54
Pricing: Free tier available
Category: Email Marketing
Built by: Misar AI
```

## Why This Matters for Operators

Email is the highest-leverage owned channel most operators have, and it is still run through dashboards with manual campaign setup. MisarMail moves the whole email stack into the agent session: an operator can send a transactional message, launch a multi-step campaign, segment contacts, run automations, A/B test subject lines, warm a new domain, and audit deliverability — all through tools inside the MCP client, without tabbing between an ESP and a spreadsheet.

The deliverability tooling is the differentiator: domain warmup and deliverability audits are usually separate paid services bolted onto an ESP. Here they sit next to the send tools in the same surface.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| Transactional send | Send transactional email (receipts, alerts, notifications) |
| Campaigns | Run multi-step email campaigns with sequencing |
| Contacts & segments | Manage contact lists and segmentation rules |
| Automations | Trigger-based email automations |
| A/B testing | Test subject lines and content variants |
| Domain warmup | Warm up new sending domains to protect reputation |
| Deliverability audit | Audit inbox placement and deliverability health |

## Installation

```bash
npx -y @misarmail/mcp
```

Or add the remote server to any MCP client:

```json
{
  "mcpServers": {
    "misarmail": {
      "type": "http",
      "url": "https://mail.misar.io/api/mcp"
    }
  }
}
```

The API key is optional: `initialize` and `tools/list` answer unauthenticated, and the server exposes a browser `login` tool for interactive auth. For local stdio use, set `MISARMAIL_API_KEY` in the environment when a key is configured.

## Configuration

```json
{
  "mcpServers": {
    "misarmail": {
      "command": "npx",
      "args": ["-y", "@misarmail/mcp"],
      "env": { "MISARMAIL_API_KEY": "<optional>" }
    }
  }
}
```

Registry ID: `io.github.Misar-AI/misarmail-mcp`. MIT licensed, repository at `github.com/Misar-AI/misarmail-mcp`.

## Business Relevance

- **E-commerce operators** send transactional receipts and post-purchase sequences from the agent
- **Newsletter owners** manage campaigns, segments, and A/B tests in one surface
- **Marketing teams** run automations without a separate ESP workflow builder
- **Growth operators** warm new domains and audit deliverability before scaling sends
- **Automation builders** trigger email from larger agent workflows via one endpoint

## Integration with CorpusIQ

CorpusIQ brings the customer and revenue layer (CRM, Stripe, QuickBooks) while MisarMail brings the email execution layer. An operator can run both in one agent session: CorpusIQ for customer records, revenue, and financials, MisarMail for transactional sends, campaigns, and deliverability — then join the two on email address for a full revenue-to-inbox pipeline.

## Limitations

- New listing (Aug 2026), no track record; single-star repository
- Free tier scope not fully documented; volume limits may apply to sends
- Hosted endpoint is a third-party dependency for remote use
- Sending infrastructure and IP reputation belong to Misar, not the operator

## See Also

- [MisarReach MCP — Outbound Sales and Lead Pipeline](/hermes/mcp/servers/external/misarreach-mcp/)
- [Misar.Blog MCP — Blog Publishing](/hermes/mcp/servers/external/misarblog-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
