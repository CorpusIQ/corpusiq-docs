---
title: "Zenith MCP - Live European Bank Data for Agents"
description: "Zenith connects business bank accounts through PSD2 open banking and serves normalized transactions, balances, counterparties and expense aggregates to AI assistants over a hosted MCP endpoint. 2,400+ banks across 30 European countries, multi-bank and multi-entity, strictly read-only, OAuth sign-in."
category: Finance
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 midday, submitted ~5h before the sweep) + mcp.so detail page via the r.jina.ai reader proxy"
relevance: ★★★
tags: [banking, psd2, open-banking, bookkeeping, reconciliation, transactions, europe, remote-mcp]
---

# Zenith MCP

**Live bank transactions your assistant can actually read.** Zenith links a business's bank accounts through PSD2 open banking and normalizes every institution into one schema: date, counterparty, amount, currency, EUR-converted amount, running balance and category. Every bank returns data differently, and Zenith flattens that into consistent fields, so prompts and downstream tooling need no per-bank special cases. The same normalized data is available over MCP, a REST API, Google Sheets, Notion and scheduled CSV exports.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect, revocable from the Zenith dashboard)
Endpoint: https://hub.zenith-books.com/api/public/v1/mcp
Tools: Live tool list served from the endpoint (transactions, balances, bank accounts, counterparties, expenses, aggregates)
Pricing: Zenith account required (pricing not published on the MCP listing)
Category: Finance / Banking data
Built by: Zenith (zenith-books.com)
```

## Why This Matters for Operators

Bank data is where bookkeeping actually starts, and it is usually trapped in per-bank export files that someone has to download, transform and reconcile by hand. Zenith keeps the connection live instead: the assistant reads real transactions rather than exports, so questions like what did we spend on software last quarter or list every payment to this supplier in 2026 are answered from what actually moved.

**The safety model is the differentiator.** The PSD2 connection is account information access only: there is no write surface, no payment initiation, and every tool is scoped to the authenticated account. Multi-bank and multi-entity support means several companies' accounts sit behind one connection, which matters for operators running more than one legal entity in Europe.

## Tools & Capabilities

The mcp.so listing shows no extracted tool list; the endpoint was verified live at sweep time (an unauthenticated initialize returns a clean `missing_token` OAuth error). Capabilities documented by the vendor:

| Capability | What it covers |
|---|---|
| Transactions | Normalized, categorized reads across connected banks |
| Balances | Current and running balances per account |
| Bank accounts | Multi-bank and multi-entity account inventory |
| Counterparties | Tracing payments to suppliers and from customers |
| Expenses | Category-level spend questions and uncategorized items |
| Aggregates | Quarterly and yearly totals, with EUR conversion alongside native currency |

Vendor example prompts: "What did we spend on software last quarter?", "List every payment to this supplier in 2026.", "What's our cash position across all accounts and currencies?", "Which transactions last month are still uncategorised?"

## Installation

```bash
claude mcp add zenith-bank-sync --transport http https://hub.zenith-books.com/api/public/v1/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "zenith-bank-sync": {
      "type": "http",
      "url": "https://hub.zenith-books.com/api/public/v1/mcp"
    }
  }
}
```

Auth is OAuth: the first connection opens a browser to sign in to Zenith and authorize access, and clients reuse the credential for future sessions. Access is revocable from the Zenith dashboard.

## Business Relevance

- **Founders and finance leads** get cash position and supplier spend answers without opening banking portals or building spreadsheet exports.
- **Bookkeepers** read categorized transactions ready for reconciliation, with counterparty and expense views built for accounting questions.
- **Fractional CFOs** run multi-entity, multi-bank reviews in one session instead of chasing per-bank statements.
- **Operations teams** trace payments to suppliers and flag uncategorized transactions before month-end.
- **EU businesses** keep data processing under GDPR with EU residency and no use of customer data for model training.

## Integration with CorpusIQ

CorpusIQ's connectors (QuickBooks, Stripe, GA4, Shopify, HubSpot and 40+ more) cover the operational and accounting records, while Zenith covers the bank side for European entities. A worked pattern: ask CorpusIQ for invoiced revenue and processor volume, ask Zenith what actually landed in the bank, and reconcile the gap in one conversation. Because both surfaces are read-only, write-back workflows stay in the systems of record, which keeps the audit trail clean.

## Limitations

- European coverage only: 2,400+ banks across 30 countries via PSD2. US and other regions are not covered.
- Strictly read-only: no payment initiation or write tools, by design.
- A Zenith account is required and pricing is not published on the MCP listing.
- Brand new to this catalog; no long track record in the sweep data yet.
- Bank coverage and freshness vary by institution, and PSD2 consent must be renewed periodically.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
