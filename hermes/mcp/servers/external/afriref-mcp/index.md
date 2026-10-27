---
title: "Afriref MCP - Tax, VAT and Wage Data for 129 Countries"
description: "Official government reference data for 129 countries: tax bands, VAT rates, minimum wages, holidays and FX, each value cited to its source."
category: Finance
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5198 (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [tax, vat, payroll, compliance, international, government-data, reference-data, remote-mcp]
last_updated: "2026-10-24"
---

# Afriref MCP

**Remote MCP server (Streamable HTTP, no key for reference lookups)** - official tax, VAT, CPI, policy-rate, wage, holiday and FX data for 129 countries across seven regional servers, every value cited to the gazette, revenue notice or central-bank instrument it came from, with effective dates, last-confirmed dates and a stale flag. Computed answers (a VAT breakdown, a payroll check, a settlement date) run on the same cited series and can return a signed Ed25519 answer receipt you can verify offline.

```
Server type: Remote (Streamable HTTP)
Auth: no key for reference lookups; paid answer tools settle per call, with optional Ed25519 answer receipts
Endpoint: https://afriref.dev/mcp
Tools: 16 (series lists and history, holidays, calendar, minimum wage, VAT, working days, settlement dates, income tax, statutory interest, payroll, receipt verification, snapshots, changes, alerts)
Pricing: free reference lookups; computed answers and certified extracts paid per call
Category: Finance / Reference Data
Built by: Afriref (afriref.dev, hosted service)
Website: afriref.dev
Listing: chatmcp/mcpso issue #5198 (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Cross-border payroll, VAT filing and contractor payments all fail on the same hidden dependency: the official rate you looked up last quarter is not the rate today, and the source is a notice you cannot read. Afriref turns that lookup into a tool call. Ask what the minimum wage in Kenya is this month, what VAT applies to a software invoice in Spain, whether a payment settles before a holiday weekend in Nigeria, and get the number with the instrument it came from, its effective date and when it was last confirmed.

The data is honest about itself. Every series carries a stale flag and a last-confirmed date, so an assistant can say "this value has not been reconfirmed since March" instead of presenting an old number as current. Computed answers can carry an Ed25519 receipt over the cited series, which gives finance teams a verifiable trail for the figures they use.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Series | list_series, get_series, get_series_history, get_snapshot, get_changes: browse and read the cited series, including the full change history |
| Calendars | get_public_holidays, get_calendar, count_working_days: holidays, business days and date arithmetic per country |
| Pay and tax answers | check_minimum_wage, compute_vat, compute_income_tax, compute_statutory_interest, compute_payroll, settlement_date: computed answers over the cited series |
| Integrity and alerts | verify_answer_receipt (check an Ed25519 answer receipt), register_alert: follow a series and get told when it changes |

## Installation

```bash
claude mcp add --transport http afriref https://afriref.dev/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "afriref": {
      "type": "http",
      "url": "https://afriref.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Finance and payroll teams** working across borders can resolve the current rate instead of the remembered one, with the source instrument named on every answer.
- **VAT and e-invoicing flows** get the applicable band and the on-time settlement date for a payment window, holidays included.
- **Compensation planning** for contractors and staff in other countries draws on the same cited minimum-wage and contribution series.
- **Compliance reviews** can cite a citable artifact: the gazette or central-bank instrument, its effective date, and a receipt that separates the free lookups from the paid answers.

## Integration with CorpusIQ

CorpusIQ answers from the business systems around the transaction; Afriref supplies the official rate the transaction must obey. Connect a QuickBooks, Stripe or Shopify source, then ask the assistant to check a cross-border invoice: CorpusIQ reads the actual amounts and currency from the source of record, and Afriref returns the statutory VAT figure, the minimum wage behind a payroll line, or the settlement date for the payment run, each with its citation. The pair turns "are we paying this correctly in that country" into one conversation with both ends of the answer sourced.

## Limitations

- Coverage is 129 countries across seven regional servers; the vendor states what is not covered rather than guessing, so some jurisdictions will simply answer "not covered".
- Reference lookups are free, but computed answers and certified extracts are paid per call, settled in USDC; heavy answer usage needs a funded setup.
- An answer receipt covers the computation over the cited series as of last_confirmed; the vendor states it is not a series certified extract and not legal advice.

## FAQ

### Do I need an API key or an account?

No. The MCP endpoint answers keyless initialize and the reference tools are free to call; paid answer tools quote and settle per call on the same endpoint.

### What do the "cited to source" and "last confirmed" fields actually give me?

Every value names the gazette, revenue notice or central-bank instrument it came from, plus its effective date and last-confirmed date. When something has not been reconfirmed recently, a stale flag travels with it.

### What is the Ed25519 answer receipt?

When a paid answer tool is called with receipt enabled, a successful answer embeds a signed receipt covering the computation over the cited series. You can verify it offline with verify_answer_receipt; it is included in the answer price.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
