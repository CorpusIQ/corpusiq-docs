---
title: "Skywalk MCP - AppFolio Data for Property Managers"
description: "Give an AI assistant live AppFolio Property Manager data: properties, units, leases, ledgers and work orders."
category: "Real Estate & Property Management"
stars: n/a (new listing)
added: 2026-10-13
source: "mcpservers.org /all (Oct 13, 2026 night sweep)"
relevance: ★★
tags: [property-management, appfolio, real-estate, leasing, work-orders, owner-reporting, proptech, remote-mcp]
last_updated: "2026-10-24"
---

# Skywalk MCP

**Remote MCP server (Streamable HTTP, OAuth sign-in with your AppFolio account)** - a live connection between AI clients and AppFolio Property Manager: read a portfolio's properties, units, leases, tenants, ledgers, work orders and owners in plain language, and post tenant charges, bills, purchase orders and new vendors back into AppFolio when writes are switched on, one scope at a time. Built by Skywalk API, a third-party AppFolio integration layer shipping since 2018.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in (browser; your existing AppFolio account, or a dedicated user with chosen visibility)
Endpoint: https://mcp.skywalkapi.com
Tools: 40+ endpoints across Portfolio, People, Money and Operations; read-only by default with opt-in writes
Pricing: Free trial (limited version, no credit card); paid plans quoted per AppFolio database by volume; the read-only Analyze tier includes 10,000 read requests a month, hourly refresh, every read endpoint and webhooks, and higher tiers add write requests
Category: Real Estate & Property Management
Built by: Skywalk API (skywalkapi.com, Los Angeles; third-party software, not affiliated with AppFolio)
Website: skywalkapi.com/mcp
Listing: mcpservers.org /all (Oct 13, 2026 night sweep)
```

## Why This Matters for Operators

Property managers live inside AppFolio, and everyone else waits on exports: the weekly owner report, the vacancy list, the delinquency chase, the maintenance follow-up. Most integrations run on reports scheduled and emailed out of AppFolio - a snapshot, a few columns, one direction. **Skywalk is the connection itself: every answer reflects the AppFolio database as it stands right now**, every record carries a stable ID that matches across calls, and the same live data reaches your assistant, your dashboard, your spreadsheet or your own product.

The agent surface is deliberately conservative. Reads come first; writes for tenant charges, bills, purchase orders and vendors sit behind scopes you enable key by key, and the vendor's agent page states the connection is read-only by design with every call logged. That is the right shape for property data: ask freely, change nothing until you say so.

## Tools & Capabilities

The MCP server exposes the Skywalk data surface (40+ endpoints, each object addressable by ID). The live tool list is served from the endpoint after sign-in; this is the surface map:

| Area | Covers |
|---|---|
| Financial | cash flow, balance sheet, general ledger |
| Property data | properties, units, unit photos |
| Leasing | guest cards, applications, vacancies, leases |
| Accounting | bills, tenant ledgers, bank activity |
| People | tenants, owners, vendors |
| Operations | work orders, attachments, letters, emails (beta) |

Writes (opt-in): post tenant charges, bills and purchase orders into AppFolio, and add new vendors. Webhooks push refreshed data out to your systems (or a tool such as Zapier).

## Installation

```bash
claude mcp add skywalk --transport http https://mcp.skywalkapi.com
```

Any Streamable HTTP client works (Claude, ChatGPT, Copilot, Cursor, Claude Code or your own agent). The vendor documents a three-step walkthrough: connect your AppFolio account, add the server, ask.

## Configuration

```json
{
  "mcpServers": {
    "skywalk": {
      "type": "http",
      "url": "https://mcp.skywalkapi.com"
    }
  }
}
```

On first connect your client opens a browser sign-in through your existing AppFolio account. The endpoint publishes OAuth protected-resource and authorization-server metadata (authorize, token and dynamic-registration endpoints), so standards-compliant clients authenticate without a pasted API key.

## Business Relevance

- **Property managers** ask "which leases expire next month, which units are due for a rent increase, who is behind on rent" and read the answer from live data, in chat.
- **Portfolio managers and owners** get weekly summaries and manager-performance comparisons from the same live connection instead of report exports.
- **Accounting teams** see tenant ledgers, bills and bank activity next to the rest of the books, and can post charges and purchase orders back with intent.
- **Leasing teams** work guest cards, applications and vacancies from one surface, and spot a coming vacancy wave before it lands.
- **PropTech builders** can offer a "Connect with Skywalk" flow so their customers' AppFolio data reaches their product about three minutes after sign-in.

## Integration with CorpusIQ

Skywalk covers the property-management side; CorpusIQ answers from the business systems around it. Ask about a portfolio's delinquency trend and CorpusIQ's read-only connectors (QuickBooks, Stripe, GA4, Shopify and the rest of the stack) show how it lands in the books and the bank, while Skywalk reports the live rent roll, ledgers and work orders behind the same number.

A composed workflow: run the Friday owner report from live Skywalk data, reconcile it against QuickBooks income and Stripe payouts in the same conversation, and hand the assistant the maintenance queue to chase - reads first, writes only where the operator turns them on.

## Limitations

- Brand new to the catalog: the MCP surface is a fresh listing, and the vendor's pricing is quote-based rather than published, so budget approval is manual.
- Third-party software: Skywalk is not affiliated with AppFolio, and access runs through your own AppFolio account sign-in; the connection layer is hosted by Skywalk.
- The write path posts real tenant charges, bills and purchase orders into AppFolio - start read-only and enable scopes deliberately.
- The email area is marked beta by the vendor.
- The free trial is a limited version of the product; full read and write volume sits behind paid tiers.
- AppFolio Property Manager is a US-market platform, so the portfolio scope follows it.

## FAQ

### What do I need to get started?

An AppFolio Property Manager account and a Skywalk connection: sign in once, add the server URL to your assistant, and ask your first question. The trial needs no credit card.

### Does the assistant change anything in AppFolio by default?

No. The connection is read-only by default; writes (tenant charges, bills, purchase orders, vendors) are enabled scope by scope, and every call is logged.

### Which assistants can connect?

Anything that speaks MCP over Streamable HTTP - Claude, ChatGPT, Copilot, Cursor, Claude Code, or your own agent - plus the same live data through Skywalk's REST API for spreadsheets and BI.

### Is Skywalk affiliated with AppFolio?

No. Skywalk is third-party software that connects using your own AppFolio account; the vendor states it has delivered live AppFolio data since 2018.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [AskRentAI MCP - Rent Manager Property Intelligence](/hermes/mcp/servers/external/askrentai-mcp/)
- [LedgerCrossing MCP - QuickBooks Desktop for AI Agents](/hermes/mcp/servers/external/ledgercrossing-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
