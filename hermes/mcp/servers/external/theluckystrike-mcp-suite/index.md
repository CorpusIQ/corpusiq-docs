---
title: TheLuckyStrike Ops Suite - Invoicing, Time Tracking
description: "Local-first business ops for freelancers: numbered PDF invoices, billable time tracking, spreadsheet editing and price watching, four MIT stdio servers, no SaaS."
category: Productivity
stars: n/a (new listing)
added: 2026-09-03
source: mcpservers.org
relevance: ★★
tags: [invoicing, time-tracking, spreadsheets, pdf, small-business, finance-ops, self-hosted]
---

# TheLuckyStrike Ops Suite

**Local stdio MCP servers (npx, MIT, no network calls)** - Four small business-ops servers from one author: numbered PDF invoices with tax lines, billable time tracking with invoice-ready summaries, safe xlsx and csv editing, and product price watching - all local JSON storage, all free tiers, all offline.

```
Server type: stdio (npx); optional one-click .mcpb bundles
Auth: None (local data; optional offline-verified Pro license key)
Endpoint: local files under ~/.local/share/mcp-servers/
Tools: 12 (invoice), 13 (time tracker), plus spreadsheet and price tracker
Pricing: Free tiers; Pro $19 per server or $39 for all, lifetime, offline
Category: Productivity
Built by: theluckystrike (github.com/theluckystrike/mcp-servers)
```

## Why This Matters for Operators

Freelancers and solo operators run their whole back office on chat now, but invoicing and time tracking still force a jump into a SaaS or a spreadsheet. This suite keeps it in the conversation: "make an invoice for Acme, 12 hours at 90 EUR, due in 14 days" returns a real A4 PDF.

**The money handling is the differentiator:** all amounts are integer minor units from an ISO 4217 table (2 decimals for most, 0 for JPY, 3 for KWD), every printed number carries its currency code, and rounding is per line then summed - a printed total can never disagree with the printed lines. Invoice numbers are sequential and never reused, allocated under an advisory file lock. Nothing is uploaded anywhere: no account, no network calls, license keys verified offline.

## Tools & Capabilities

The invoice server (12 tools): business_set, client_add, client_list, invoice_create, invoice_from_hours, invoice_list, invoice_get, invoice_mark_paid, invoice_pdf, overdue_report, license_status, license_activate.

The time tracker (13 tools): timer_start, timer_stop, timer_status, entry_add, entry_list, entry_edit, entry_delete, project_set_rate, report, export_csv, invoice_summary, license_status, license_activate - plus the timetracker://today resource and a daily_standup prompt.

The spreadsheet server reads, queries, edits and converts xlsx and csv safely; the price tracker checks and watches product prices on ordinary shop pages. An office-suite package bundles all four behind one install and one config entry.

## Installation

```bash
claude mcp add invoice -- npx -y @theluckystrike/mcp-invoice
claude mcp add time-tracker -- npx -y @theluckystrike/mcp-time-tracker
```

npm publishing is pending; until then the .mcpb one-click bundles from the latest GitHub release, or a clone-and-build path, are the working routes.

## Configuration

```json
{
  "mcpServers": {
    "invoice": {
      "command": "npx",
      "args": ["-y", "@theluckystrike/mcp-invoice"]
    }
  }
}
```

Data lives in JSON under ~/.local/share/mcp-servers/invoice/ and .../time-tracker/data.json; back up by copying the directory. Free tiers: 3 invoices per calendar month, 7-day readback window on time entries, 2 rated projects - Pro (one-time $19 per server, $39 for all) removes caps and branding.

## Business Relevance

- **Freelancers** invoice, track billable time and turn hours into invoice lines without leaving chat
- **Bookkeepers** get a CSV export and invoice-ready summaries per project
- **Small operators** keep the whole back office local and offline with no monthly SaaS fee

## Integration with CorpusIQ

The suite covers the lightweight back office that CorpusIQ's enterprise connectors overkill: a solo operator uses the local invoice server for PDF invoices and time tracking, while CorpusIQ's QuickBooks and Stripe connectors handle the accounting system of record and payment verification when the business grows into one. The composed flow: invoice_summary output maps directly onto invoice_create line items, and CorpusIQ's Stripe connector later confirms the payment landed - local first, connected when it matters.

## Limitations

- npm packages pending publication - .mcpb or clone-and-build for now
- Free tiers cap invoices (3 per month), history windows (7 days) and rated projects (2)
- No email sending, payment links or accounting sync in the invoice server
- Local files only - no team or multi-device sync

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [QuickBooks Connector by Meridian MCP - Hosted QBO for Agents](/hermes/mcp/servers/external/meridian-qbo-mcp)
- [jp-payroll MCP - Japanese Payroll and Social Insurance for Agents](/hermes/mcp/servers/external/jp-payroll-mcp)
- [Valuation API MCP - Deterministic Finance Math for Agents](/hermes/mcp/servers/external/valuation-api-mcp)
