---
title: "Gastrosync MCP - Catering and Event Operations"
description: "Turn catering inquiries into event and quote drafts, prepare kitchen briefings and track open offers and unpaid invoices from any MCP client."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 midday sweep)"
relevance: ★★
tags: [catering, events, hospitality, quotes, invoices, operations, remote-mcp]
---

# Gastrosync MCP

**Remote MCP server (Streamable HTTP, OAuth)** - connects AI assistants to Gastrosync for catering and event management. Email inquiries become event and quote drafts, the kitchen gets structured briefings, and open offers and unpaid invoices stay visible - all from the conversation.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in with your Gastrosync account
Endpoint: https://gastrosync.com/mcp
Tools: Events, quotes, kitchen briefings, offers, invoices, search, updates
Pricing: Included with a Gastrosync account
Built by: Gastrosync
Registry: via gastrosync.com
```

## Why This Matters for Operators

Catering operations run on a loop that is easy to drop: an inquiry arrives by email, becomes a quote, becomes an event, becomes a kitchen briefing, becomes an invoice. In practice the loop lives across inboxes, spreadsheets and memory. Gastrosync's MCP surface keeps each step as a tool: draft events from saved inquiries and templates, prepare unsigned quote drafts from event details, build kitchen briefings with products, quantities, schedules, notes and packing lists, and find open offers and unpaid invoices at any time.

The confirm-first shape matters here: quotes are drafted unsigned, and event details and product-library data update after approval. The planning happens in chat; the commitments stay human.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Events | Create draft catering events from saved inquiries and event templates |
| Quotes | Prepare unsigned quote drafts from event details |
| Kitchen | Build briefings with products, quantities, schedules, notes and packing lists |
| Money | Find open offers and review unpaid invoice statuses and totals |
| Search | Find events, customers, templates and product-library items |
| Updates | Update event details and maintain product-library data after approval |

## Installation

Add `https://gastrosync.com/mcp` as a remote MCP connector in your client, then sign in with your Gastrosync account when prompted. There is a ChatGPT-oriented walkthrough at gastrosync.com/chatgpt.

## Configuration

```json
{
  "mcpServers": {
    "gastrosync": {
      "type": "http",
      "url": "https://gastrosync.com/mcp"
    }
  }
}
```

## Business Relevance

- **Caterers and event teams** turn inbox inquiries into structured events and draft quotes the same day.
- **Kitchen leads** get briefings built from the real product library - quantities, schedules and packing lists included.
- **Owners** see open offers and unpaid invoices without opening the back office.
- **Small teams** keep the approval gate: quotes stay unsigned drafts until a person signs off.

## Integration with CorpusIQ

CorpusIQ reads the systems of record read-only; Gastrosync handles the operational middle where a catering business actually commits - quotes, events, invoices. The two combine cleanly for hospitality operators: the financial and marketing picture from the connected stack, the event pipeline from Gastrosync, each answer with its own source.

## Limitations

- Requires a Gastrosync account; the connector works inside that account's data.
- Quote drafts are unsigned and updates apply after approval - by design.
- Catering and event workflows specifically; not a general CRM.
- New listing: no track record in this catalog yet.

## FAQ

### What does the connection cover?

Draft events, unsigned quote drafts, kitchen briefings, open offers, unpaid invoices, search across events, customers, templates and the product library, and post-approval updates.

### Do quotes go out automatically?

No. Quote drafts are prepared unsigned, and event and product-library updates apply after approval.

### Which clients are supported?

Any MCP-compatible client; the vendor publishes a ChatGPT setup walkthrough at gastrosync.com/chatgpt.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Revup MCP - Promotions, Forms and Giveaways](/hermes/mcp/servers/external/revup-mcp/)
- [InvoiceParser Pro MCP - Invoice to Excel from Chat](/hermes/mcp/servers/external/invoice-parser-pro-mcp/)
