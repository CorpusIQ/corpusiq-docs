---
title: "Giggal.ai MCP - Email Verification with Catch-All Detection"
description: "Remote MCP server for Giggal.ai email verification: deep mailbox existence checks that verify catch-all, accept-all, and SEG-protected addresses from inside any MCP client, with credit and history lookup"
category: Marketing
stars: n/a (new listing)
added: 2026-08-20
source: mcpservers.org
relevance: ★★
tags: [email-verification, deliverability, catch-all-detection, lead-validation, sales-operations, list-hygiene, remote-mcp, api-key]
---

# Giggal.ai MCP

**Remote MCP server (Streamable HTTP, API key) — deep mailbox existence verification, including catch-all detection, directly from an AI assistant.** Giggal.ai runs a mailbox-existence check that distinguishes real addresses from catch-all, accept-all, and SEG-protected mailboxes — the cases most verification APIs mark as "deliverable" because the domain accepts anything. The MCP server puts that check inside Claude, ChatGPT, Cursor, VS Code, or any MCP client, so list validation happens where the outreach workflow already runs.

```
Server type: Hosted remote (Streamable HTTP)
Auth: API key (verify:read scope)
Endpoint: https://mcp.giggal.ai/mcp
Tools: verify addresses, check credits, lookup past verifications
Pricing: Giggal.ai credits (API key required)
Category: Marketing / Email Verification
Built by: Giggal.ai (giggal.ai)
```

## Why This Matters for Operators

Bounce rates are a deliverability tax and catch-all domains are the hidden cause. A catch-all mailbox accepts mail for any address, so a naive SMTP check says "valid" — then your campaign bounces the moment a real recipient does not exist. Giggal.ai's deep check is built to answer the catch-all question specifically, which is the difference between a list that looks clean and a list that sends. Verifying from inside the agent means the check happens at the moment of use: before the agent drafts a send to a scraped lead, it can verify the address, check remaining credits, and pull the history of past verifications — no export-import loop between a verification SaaS and the outreach tooling.

The connector-first design also keeps setup trivial. There is no SDK: one MCP URL, added as a custom connector, with an OAuth-style grant of `verify:read` — verify addresses, check credits, and look up past verifications, and nothing else. The scope is exactly the verification surface, which is what you want a sales agent holding.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Verify addresses | Deep mailbox existence check: catch-all, accept-all, and SEG-protected detection |
| Check credits | Remaining verification balance |
| Past verifications | Look up verification history for previously checked addresses |

Tool names are served from the live endpoint; the capability surface above is the vendor-published description. Works with an existing Giggal.ai API key — catch-all verification included, no SDK.

## Installation

Add Giggal.ai as a custom connector in Claude (or the equivalent flow in any MCP client): Settings → Connectors → Add custom connector → name it Giggal.ai → paste the MCP URL → Connect → Allow to grant `verify:read`.

```bash
claude mcp add giggal --transport http https://mcp.giggal.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "giggal": {
      "type": "http",
      "url": "https://mcp.giggal.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Auth note: the endpoint works with your existing Giggal.ai API key; the connect flow above grants the `verify:read` scope against it.

## Business Relevance

- **Sales operators** verify scraped or purchased lead lists at point of use instead of after the bounce report
- **Email marketers** cut catch-all and accept-all addresses before they damage sender reputation
- **Outbound agencies** keep verification history inside the agent so re-checks and credit spend are visible
- **RevOps teams** get list hygiene as a step in the agent's workflow rather than a separate SaaS tab

## Integration with CorpusIQ

Giggal.ai MCP is the hygiene gate in front of the outbound stack that CorpusIQ reads. Before a lead list lands in the CorpusIQ HubSpot or Close connector, the agent verifies the addresses through Giggal and drops the catch-all and accept-all rows — so the CRM stores contacts that can actually receive mail, and downstream metrics stop counting phantom leads. For email-sending operators, the CorpusIQ Klaviyo or ActiveCampaign connectors show campaign sends and opens while Giggal supplies the pre-send validity check, tightening the loop between list quality and engagement numbers. The direction of flow: Giggal.ai MCP verifies the addresses; CorpusIQ reads the CRM and email systems they feed.

## Limitations

- Credit-based commercial service — an API key with balance is required
- Verification scope only — no enrichment, no sending, no CRM features
- Brand new MCP surface — capability list from vendor docs; live tool names served from the endpoint
- Verification quality depends on Giggal's mailbox probing; results are advisory, not contractual
- History lookup scoped to past checks made through the service

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
