---
title: "Zovo MCP Servers - 58 Back-Office Servers for Small Business"
description: "Invoices, VAT, bank reconciliation, cash book and dunning letters as local-first MCP servers, MIT licensed, with a one-time Pro unlock."
category: Back Office / Accounting
stars: n/a (MIT, optional one-time Pro per server)
added: 2026-10-27
source: "live discovery document read from mcp.zovo.one/mcp (41 hosted endpoints with 400+ tool names), bare-endpoint initialize returning 200, official MCP registry entries under io.github.theluckystrike, and the repository README at github.com/theluckystrike/mcp-servers"
relevance: ★★★
tags: [invoicing, vat, bookkeeping, bank-reconciliation, cash-book, asset-register, dunning, small-business, mit]
last_updated: "2026-10-27"
---

# Zovo MCP Servers

**Fifty-eight small business back office jobs, each its own server, each computing on your machine: an invoice with a VAT rate and a numbered PDF, a bank statement reconciled to expenses, a trial balance that ties to the minor unit.**

```
Server type: Local stdio (Claude Desktop bundle or source build),
             41 of them also hosted
Hosted base: https://mcp.zovo.one/mcp/<server>
Transport:   Streamable HTTP for hosted, stdio for local
Auth:        Static bearer token, no OAuth. Free anonymous token or a
             Pro token signed with Ed25519
Tools:       400+ tool names across 41 hosted endpoints, read from the
             discovery document
Built by:    theluckystrike (Michael Lip)
Licence:     MIT
Registry:    io.github.theluckystrike/* per server
```

## Why This Matters for Operators

The back office is where a small business accumulates the most unpaid clerical work: matching a supplier invoice to a purchase order and a delivery note, chasing an overdue balance with the right dunning letter, building an asset register that depreciates on the rates the tax authority actually publishes, and proving a trial balance that ties.

None of that is strategy. All of it is work that gets deferred until month end and then done badly. A server that computes it inside the conversation, on the operator's own machine, at minor-unit precision, changes the shape of the month.

## What It Actually Does

The hosted root at `https://mcp.zovo.one/mcp` answers a plain `GET` with a JSON discovery document rather than a challenge, and a bare child endpoint (`/mcp/time-tracker`) answers `initialize` with HTTP 200. The document lists 41 hosted endpoints with every tool name. A sample of what is there:

| Server | Tools | What it does |
|---|---|---|
| `invoice` | 12 | Business and client records, `invoice_create`, `invoice_from_hours`, numbered PDFs |
| `bank-statement` | 15 | Import the CSV export, `transactions_search`, categorise and reconcile with expenses |
| `cash-book` | 8 | `ledger_build`, `trial_balance`, `month_close`, `ledger_export_csv` - double entry derived from the books you keep |
| `asset-register` | 8 | `asset_schedule`, `asset_journal`, `asset_dispose` - depreciation on published rates, with the gain on sale |
| `billing-docs` | 14 | Credit notes and purchase orders on the invoice engine |
| `statement-of-account` | 8 | `statement_aging`, `statement_pdf`, `dunning_text` per customer |
| `dunning-letters` | 11 | `overdue_list`, `aging_summary`, `letter_render`, `letter_sent` |
| `work-order`, `change-order`, `job-card` | 11-12 each | Trades and field service: labour and material lines, status, change control |
| `per-diem`, `mileage-log`, `deposits`, `petty-cash`, `amortization` | 8-10 each | Allowances, mileage rates, customer deposits, the petty cash float, loan schedules |
| `spreadsheet`, `pdf`, `docx`, `zip`, `barcode` | 10-15 each | `sheet_query` over a workbook, PDF merge and count, Word documents, QR and SEPA payment codes |

The repository counts 57 servers plus an office-suite aggregator, 46 of them reachable as a hosted endpoint; the discovery document advertises 41. Every server is `MIT` and every one runs locally, so the data path never leaves the machine unless the hosted endpoint is the one you chose.

## The Money Path and the Floor Under It

The pricing is unusually plain for this catalog: free tier on every server, and Pro as a one-time payment of **$19 per server or $39 for the bundle, lifetime** - no subscription. Hosted access takes a static token rather than an OAuth flow, and the token can be supplied three ways:

- `Authorization: Bearer ***` where the client can set a header,
- `https://mcp.zovo.one/mcp/<server>/t/<token>` where the client only takes a URL,
- `?token=` where the client takes a query string but no header.

An anonymous token mints free with `anon_` prefix, 30 day retention and 600 calls an hour; Pro tokens verify offline with Ed25519 and run at 6000 calls an hour. Buying through `/buy/<product>?tenant=<anonymous token>` binds the purchase to that same anonymous data document, so a trial that upgrades keeps its data.

## How It Is Contained

- **Local by default.** The stdio servers keep every record on your machine, and the vendor states the demo tasks send no field values.
- **No OAuth to phish.** There is no consent screen to fake; the credential is a bearer token you mint and can revoke.
- **Bare endpoints are read-only in effect.** A bare hosted endpoint can initialize and list tools but does not authorize tool calls, which the README states explicitly - the credential has to be in the URL or header.
- **Deterministic money.** Schedules are computed to the minor unit rather than estimated, which is the difference between an assistant that drafts and one whose output can be filed.

## Limitations Recorded

- **npx is not an install path.** The npm packages are not published; the vendor says to use the `.mcpb` bundle, the source build or a hosted endpoint. A README note records a dead npm publish token.
- **The URL forms are the credential.** A token in a path segment or query string is private by definition, so a URL pasted into a chat log or a shared config has leaked the account.
- No tool call was executed. Tool names come from the live discovery document; arithmetic correctness was not exercised.
- **Local tax rules are jurisdiction specific.** The depreciation and VAT behaviour follows the rates the vendor encoded, so an operator outside those jurisdictions must check the numbers rather than trust them.
- Pro is sold per server, and the bundle price is a one-time $39 - the cheapest shape in this catalog, but it is one maintainer.

## FAQ

### Do I need a subscription to use it?
No. Every server has a free tier, and Pro is a one-time payment of $19 per server or $39 for the bundle for life.

### Where does the bookkeeping data live?
On your machine for the local servers. With the hosted endpoint the records live with the vendor's Cloudflare Worker, bound to the token you minted.

### What is the most useful single server here for an operator?
`bank-statement` with `cash-book` behind it: import the export, categorise it, and get a trial balance that ties, which is the monthly job most small businesses defer until the accountant asks for it.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [QuickBooks connector guide](/hermes/mcp/connectors/)
- [CorpusIQ connectors for accounting data](/hermes/mcp/)
