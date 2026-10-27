---
title: "byondr Receipts MCP - Receipts to Checked CSV"
description: "Turn receipt and invoice photos or PDFs into checked line items and QuickBooks CSV, keyless, with doubtful fields flagged instead of guessed."
category: Finance / Bookkeeping
stars: n/a (free within a daily quota)
added: 2026-10-27
source: "live MCP probes on byondr.co/receipts/mcp (initialize 200, tools/list 200, two tools with full input schemas), the vendor start.md and mcpservers.org listing text, and the official MCP registry entry co.byondr/receipts"
relevance: ★★★
tags: [receipts, invoices, bookkeeping, quickbooks, ocr, csv, expense, keyless]
last_updated: "2026-10-27"
---

# byondr Receipts MCP

**Every bookkeeping backlog is the same shape: a folder of receipts and invoices, a deadline, and a person retyping vendor, date, tax and total into a spreadsheet. The work is mechanical, and the part that actually matters is knowing which numbers are reliable.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://byondr.co/receipts/mcp
Transport:   JSON-RPC over POST
Auth:        none on the free surface, nothing stored
Tools:       extract_documents, create_upload
Limits:      25 documents per call, 10 MB each, PDFs up to 10 pages
Exports:     CSV, line-item CSV, QuickBooks CSV, or a zip of the
             originals renamed by date, vendor and total
Built by:    byondr (byondr.co)
Registry:    co.byondr/receipts
```

## Why This Matters for Operators

Extraction is the easy half. The half that decides whether the output is usable is trust: was the tax line found, was the total legible, is this the same receipt that was already entered last month.

This server returns each field marked `ok`, `check` or `missing`, flags doubtful documents with the reason instead of filling the gap with a plausible number, and marks repeated receipts as duplicates. That is the difference between a CSV an operator can import and a CSV that has to be re-checked line by line, which would have cost more than typing it.

## What It Actually Does

`initialize` on `https://byondr.co/receipts/mcp` returns HTTP 200 as "Receipts & invoices to spreadsheet" version 0.1.0. `tools/list` returns two tools with complete schemas:

| Tool | What it does |
|---|---|
| `extract_documents` | Reads receipts and invoices (JPG, PNG, WebP, HEIC, PDF or a zip of them, one document per file or per PDF) into checked numbers. Inputs: `files`, `country`, `currency`, `date_order`, `exports`, `quickbooks_currency`, `quickbooks_date_format`. Returns vendor, date, currency, line items, tax and total with a per-field state. |
| `create_upload` | Gets a one-hour signed upload URL for a document or zip that is too large to send inline, over 2 MB and up to 100 MB, or that already sits on disk. Inputs: `bytes`, `filename`. |

The QuickBooks-specific inputs are the tell that this was built for a real workflow rather than a demo: currency and date format are set for the export, because a QuickBooks import fails on a date it cannot parse. The zip export renames each original by date, vendor and total, which is what makes the source documents findable when an accountant asks for the receipt behind a line.

## The Part That Costs You Something

Nothing is charged on the free surface and nothing is retained, so the cost is in what gets imported.

- **A `check` field is not a number.** A row with a `check` on the total is a question, not an expense. An agent that pastes the row into a ledger without surfacing the flag has undone the only thing this tool does better than a form.
- **Duplicates need a decision.** A receipt submitted twice comes back marked as a duplicate of the earlier one, which the operator has to accept as a duplicate rather than import twice.
- **Free within a daily quota.** A large backlog will take more than one day, so plan the run rather than discovering the cap halfway through a month.

## How It Is Contained

- **Keyless and stateless.** No account and no key to manage; the free surface needs nothing to connect.
- **Files are deleted after 24 hours** and the vendor states they are never used for training, which is the shortest retention this catalog records for a document extraction service.
- **Large files never travel inline.** `create_upload` issues a one-hour signed URL for anything over 2 MB, so a 100 MB zip goes around the JSON-RPC body rather than through it.
- **Nothing is guessed.** Fields that cannot be read come back `missing` with a reason, which is the behaviour that keeps a clean-looking spreadsheet from hiding a hole.

## Limitations Recorded

- Two tools only: extraction and upload. There is no list, no query and no per-document read, so results are returned from the call that produced them.
- 25 documents per call, 10 MB per file, and PDFs up to 10 pages. A scanned 20 page invoice needs splitting.
- Line items are extracted where the document has them; a thermal receipt with a photo of a crumpled total may return the total as `check` rather than a number.
- The server is at version 0.1.0, so the shape may still move.

## FAQ

### Is this a bookkeeping system?
No. It is the intake step: documents in, checked rows and a QuickBooks-ready CSV out. The ledger, the categorisation and the approval remain wherever the operator already keeps them.

### What happens to the receipts after extraction?
The vendor states files are deleted after 24 hours and never used for training. The renamed zip of originals exists so the operator keeps their own copy rather than relying on the service's retention.

### What should I test first?
Five receipts with one deliberately duplicated and one photographed at an angle, then check that the duplicate is marked and that the bad photo returns `check` rather than a confident wrong total.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Seller Profit Doctor MCP - storefront profit math](/hermes/mcp/servers/external/seller-profit-doctor-mcp/)
- [CorpusIQ connectors for finance and accounting data](/hermes/mcp/)
