---
title: "Fakto.app wFirma MCP - CorpusIQ Docs"
description: Full read-write MCP server for wFirma.pl Polish accounting — invoices, contractors, expenses, warehouse, KPiR and ZUS, with reports and cashflow forecasts
category: Finance
stars: n/a (new listing)
added: 2026-08-13
source: mcp.so
relevance: ★★
tags: [accounting, invoicing, erp, finance, oauth, poland, remote-mcp]
---

# Fakto.app wFirma MCP

**Remote MCP server (Streamable HTTP, OAuth 2.0) for wFirma.pl — the only MCP integration for one of Poland's most popular small-business accounting platforms.** Full read-write, not read-only: the assistant creates and searches invoices, manages contractors, records expenses and payments, tracks warehouse stock, reads KPiR tax ledgers and ZUS contributions, and produces cashflow forecasts. ~45 tools behind a hosted endpoint; OAuth 2.0 with dynamic client registration (RFC 7591) works out of the box as a custom connector in claude.ai, ChatGPT, and Claude Desktop.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 (RFC 7591 dynamic client registration) or Bearer token
Endpoint: https://fakto.app/wfirma/stream
Tools: ~45 (invoices, contractors, expenses, payments, warehouse, KPiR/ZUS records, reports, forecasts, payment reminders)
Pricing: Free tier 100 requests/month; paid from 19.90 PLN/month; 7-day trial, no card
Category: Finance / ERP (Poland)
Built by: Fakto.app (github.com/nulline-apps/fakto-mcp)
```

## Why This Matters for Operators

Polish SMB accounting runs on wFirma.pl, and until now every integration into it was a bespoke API project. Fakto.app makes the assistant an operator inside the ledger — not a viewer. The assistant can draft an invoice, chase an overdue payment with an automatic reminder, or answer "what is my cash position next quarter" straight from the books.

**The write path is real but structured.** OAuth scopes and Bearer tokens gate access, and one subscription covers both the wFirma and the sister Fakturownia.pl server — so a Polish operator with books in either system pays once. n8n and Make templates ship ready-made for teams that want the same tools outside a chat client.

## Tools & Capabilities

| Area | Capabilities |
|---|---|
| Invoicing | Create, search, fetch details, download PDFs |
| Contractors | Add, update, look up by tax ID (NIP) |
| Expenses & payments | Record and query costs, payment status, overdue reminders |
| Warehouse | Goods, stock levels, low-stock alerts |
| Tax records | KPiR revenue/expense ledger, ZUS contributions |
| Analytics | Revenue/expense reports, month-over-month comparisons |
| Forecasting | Cashflow, sales and payment predictions |
| Automation | Automatic payment reminders for overdue invoices |

## Installation

```bash
claude mcp add fakto-wfirma --transport http https://fakto.app/wfirma/stream
```

First connect triggers the browser OAuth flow (dynamic client registration — no pre-created client ID needed). For n8n and Make.com, generate a Bearer token in the web panel instead.

## Configuration

```json
{
  "mcpServers": {
    "fakto-wfirma": {
      "type": "http",
      "url": "https://fakto.app/wfirma/stream"
    }
  }
}
```

OAuth-capable clients bootstrap automatically from the 401 challenge; Bearer-token clients pass the header explicitly.

## Business Relevance

- **Polish small businesses on wFirma.pl** get their first AI-native accounting layer — invoice drafting, stock alerts, and cashflow forecasts in chat.
- **Accountants and bookkeepers** hand the assistant recurring work (payment reminders, overdue lists) and keep final sign-off.
- **Ecommerce operators in Poland** connect warehouse stock and payment tracking to the same surface that answers "what is owed to us".
- **n8n/Make teams** get the identical ~45 tools as workflow steps with ready-made templates.

## Integration with CorpusIQ

Fakto.app extends the CorpusIQ accounting story into a locale CorpusIQ connectors do not cover natively: CorpusIQ's QuickBooks and Axonaut connectors handle US and French books; wFirma is the Polish ledger. An operator running both worlds composes cleanly — CorpusIQ answers multi-market revenue and spend questions (Stripe charges, Shopify orders, GA4 traffic), while Fakto answers the Polish-book questions (KPiR, ZUS, local invoices) the global layer never sees. For a Polish entity, the pair is the practical stack: global business data from CorpusIQ, local compliance from Fakto.

## Limitations

- Brand new — no track record yet
- Poland-specific: wFirma.pl and Fakturownia.pl only; no other locales
- Cloud-only (hosted endpoint, no self-host option)
- Free tier capped at 100 requests/month
- Write access is broad — OAuth scope review matters before production use

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
