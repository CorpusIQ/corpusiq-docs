---
title: "Mighty Accounting MCP - UK Books Your Assistant Drafts"
description: "A UK limited company's books behind one MCP server: dashboards, invoices, bank categorisation drafts, receipts and HMRC-rate mileage."
category: Finance / Accounting
stars: n/a (hosted inside the Mighty service)
added: 2026-10-24
source: "mcpservers.org /all p1-20 fresh cohort (late sweep, October 24 2026) + live endpoint probe and vendor documentation"
relevance: ★★★
tags: [accounting, uk, limited-company, vat, invoicing, bank-reconciliation, receipts, mileage, corporation-tax, year-end]
last_updated: "2026-10-24"
---

# Mighty Accounting MCP

**The accounting system behind a UK limited company, exposed to an assistant with the approval step left where it belongs.** Mighty is a fixed-fee online accountant for UK limited companies, and its MCP server puts the same books an owner sees into any MCP client: dashboard figures, invoices, uncategorised bank transactions, the receipt box, mileage claims and the three reports an accountant signs.

```
Server type: Remote (Streamable HTTP)
Endpoint: https://api.mightyaccounting.com/mcp
Auth: organisation API key, created in the Mighty app, scoped to one organisation
Tools: 26 documented (reports, invoices, bank, post box, mileage, periods)
Probe: unauthenticated POST initialize returned HTTP 401 (live, key-gated)
Pricing: Mighty Plan 60 GBP plus VAT per month billed annually, or 70 GBP plus VAT monthly
Also available: REST API at https://api.mightyaccounting.com/documentation/
Built by: Mighty Accounting (mightyaccounting.com)
```

## Why This Matters for Operators

Most small companies answer "how did we do" by emailing their accountant. The accounts are prepared quarterly, the number arrives late, and by the time it does the decision it was meant to inform has passed. The owner is not short of data, they are short of a current answer from the same books the tax return will be filed from.

What makes this server different from a bookkeeping connector is the boundary the vendor drew. The assistant can read everything the owner can read, and it can prepare work, but it cannot approve a categorisation, move money out of the books or send anything to HMRC. Every record it creates is labelled as AI-created. The accountant still prepares and files.

## What It Actually Does

The published guide documents 26 tools. Grouped by the question they answer:

| Area | Tools | What an operator asks |
|---|---|---|
| Position | `get_dashboard`, `refresh_dashboard` | bank balance, net profit, corporation tax, VAT liability, dividends available, invoices outstanding |
| Reports | `get_profit_and_loss`, `get_balance_sheet`, `get_trial_balance`, `list_accounting_periods` | the three reports, with the prior period alongside every line when comparatives are requested |
| Sales | `list_sales_invoices`, `get_sales_invoice`, `create_sales_invoice` | what is unpaid, one invoice with its payments, a draft invoice raised from a prompt |
| Bank | `list_bank_accounts`, `list_unreconciled_bank_transactions`, `list_bank_categories`, `list_bank_match_candidates` | what still needs categorising and what each transaction could match |
| Bank drafts | `save_bank_transaction_draft`, `clear_bank_transaction_draft`, `get_bank_transaction_documents`, `read_bank_transaction_document` | suggested categories saved for approval, with the receipt read |
| Receipts | `list_postbox_documents`, `get_postbox_document`, `read_postbox_document_file`, `create_expense_from_postbox_document`, `match_postbox_document_to_bank_transaction` | what arrived in the Post Box, what the scan read from it, and the expense or match it becomes |
| Mileage | `list_mileage_claimants`, `list_mileage_claims`, `lookup_mileage_distance`, `create_mileage_claim` | who claimed what this tax year, the driving distance between two places, a claim at the rate Mighty works out |

The safety model is in the tool surface, not in a paragraph of policy. The bank tools save drafts only and never approve; VAT can only be entered on transactions dated while the company was VAT-registered; a Post Box document becomes an expense the owner checks and finalises, and matching it only attaches the receipt. Mileage is the deliberate exception, because Mighty has no draft mileage claim, so a claim the assistant records posts to the accounts immediately and is removed in the app. That exception is stated rather than hidden.

## Installation

1. In the Mighty app, create an organisation API key. A key works for one organisation and takes about a minute to set up.
2. Add `https://api.mightyaccounting.com/mcp` as a custom connector or remote MCP server in the client, with the key as a bearer credential.
3. Ask for the dashboard first, then move to invoices or bank work.

The same capabilities are reachable over the REST API documented at `https://api.mightyaccounting.com/documentation/` if a team would rather build than prompt.

## Business Relevance

Accounting is the densest connector class in this catalog and every entry has a different edge. QuickBooks and QuickBooks Desktop carry the market-leading ledgers, Caribooks carries QuickBooks Online Canada, Oracle Fusion carries the enterprise ERP, and ATLASS OS carries the construction trades with double-entry books inside its own platform.

Mighty's edge is the UK limited company shape: VAT, corporation tax, dividends available, director payroll and HMRC-rate mileage are first-class in the data model, and the service behind the software includes a named accountant. For a UK contractor, consultant or small agency, that is the whole financial surface in one server.

## Integration with CorpusIQ

For a UK limited company, this is the ledger the revenue question resolves to. Connected alongside a payment processor and a bank feed, an operator can ask why net profit moved and get the report line, the invoices and the transactions in one answer instead of reconciling three tools by hand.

## Limitations

- UK limited companies only. The tax model is UK VAT, corporation tax and HMRC mileage rates, so a US LLC or an EU GmbH is out of scope.
- It is a paid accountancy service, not a free connector. The Mighty Plan is 60 GBP plus VAT a month billed annually, or 70 GBP plus VAT a month billed monthly, with personal Self Assessment, a registered address at 10 GBP plus VAT a month and payroll for additional non-spouse employees at 5 GBP plus VAT each as extras.
- No tool call was possible in this sweep because every tool needs an organisation key that only exists inside a customer account. The live probe confirmed the endpoint answers (401 without a key) and the tool surface is taken from the vendor's published guide.
- No official MCP registry entry exists for Mighty Accounting as of October 24, 2026; a registry search for "mighty" returns unrelated companies.
- Mileage claims post immediately, so an assistant mistake there is a real ledger entry that must be deleted in the app rather than a draft.

## FAQ

### Can the assistant approve transactions or file anything?

No. Bank categorisations are saved as drafts, invoice and expense work is left for the owner to check, and nothing goes to HMRC from the assistant. Records it creates are labelled AI-created.

### Which reports can it produce?

Profit and loss, balance sheet and trial balance, per accounting period, with the prior period alongside each line when comparatives are requested. They return the same figures as the report screens in the app.

### Does it read receipts?

Yes. The Post Box tools list documents with what the scan read from each, return the file itself so the assistant can read it, create an expense to finalise, or attach the document to a bank payment as its receipt.

### What does it cost?

The Mighty Plan is 60 GBP plus VAT per month billed annually, or 70 GBP plus VAT per month billed monthly. The assistant connection is part of the service, not a separate line.

## See Also

- [QuickBooks MCP - Ledger, Invoices and Payments](/hermes/mcp/servers/external/quickbooks-mcp/)
- [Caribooks MCP - QuickBooks Online for Canada](/hermes/mcp/servers/external/caribooks-mcp/)
- [ATLASS OS MCP - Trades Business With Real Books](/hermes/mcp/servers/external/atlass-os-mcp/)
