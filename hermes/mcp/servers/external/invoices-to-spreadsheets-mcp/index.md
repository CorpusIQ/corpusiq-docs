---
title: "Invoices to Spreadsheets MCP - The Checks Sheet"
description: "Keyless: invoices in, an Excel workbook out with a Checks sheet for VAT arithmetic, missing fields and duplicates - and one check that never fires."
category: "Finance / Accounts Payable"
stars: "n/a (hosted service, no repository; registry com.invoicestospreadsheets/invoice-spreadsheets 1.0.0)"
added: 2026-11-13
source: "the submission queue entry #7318, the official registry record, and a keyless session on this host: initialize, tools/list, six tools/call requests, and the returned workbook downloaded and read cell by cell"
relevance: ★★★
tags: [invoices, accounts-payable, excel, reconciliation, vat, duplicates, keyless, mcp]
last_updated: "2026-11-13"
---

# Invoices to Spreadsheets MCP

**Every invoice tool reads the document. Almost none of them checks what it read.**

Extraction is the part that gets demonstrated: an agent reads a PDF, pulls the supplier, the VAT and the total, and hands back a spreadsheet. The part that costs an accounts team its week is the next step - the total that does not equal net plus VAT, the VAT that is not the rate printed beside it, the same invoice number filed twice by two different people, the field that was blank on the paper and went into the ledger as a zero.

Invoices to Spreadsheets puts the check first and calls the file an output. It takes the values your assistant already read and returns three things: what is arithmetically wrong, what is missing, what looks like a duplicate - and, if you want the file, a workbook with a `Checks` sheet carrying the same findings beside the numbers.

```
Server type: Remote (Streamable HTTP), sessionless - no Mcp-Session-Id issued
Endpoint:    https://invoicestospreadsheets.com/api/mcp
Auth:        none, no account, no key
Server name: invoices-to-spreadsheets 1.0.0, protocol 2025-06-18 (title Invoices to Spreadsheets)
Tools:       3, read from a live tools/list
Built by:    invoicestospreadsheets.com (Clerk-backed site; the MCP endpoint itself is open)
Registry:    com.invoicestospreadsheets/invoice-spreadsheets 1.0.0
Pricing:     no published price on the MCP surface; no account is requested to call it
```

## The evidence tier

Everything below was measured on 2026-11-13 between 04:04Z and 04:06Z against the live endpoint, with no key and no account: `initialize` returned HTTP 200 as `invoices-to-spreadsheets` **1.0.0** on protocol `2025-06-18` with `tools.listChanged` as its only capability and no session id in the response headers, `tools/list` returned **3** tools, six `tools/call` requests were driven, and the workbook returned by one of them was downloaded and opened - **10,374 bytes**, content type `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, four worksheets, every cell read by reference.

The vendor's own instruction string is the product brief, and it is unusually strict about where the assistant's job ends:

> Turns invoices into an Excel workbook and checks them. Read the invoice files the user provides yourself, then pass every invoice to create_invoice_spreadsheet with values exactly as printed (null when not printed or not legible; never estimate). [...] The tools do not read files, give tax advice or file returns.

That last sentence is the boundary that makes the surface trustworthy: it does not claim to read PDFs, so an extraction error is the client's error and not a hidden one.

## Why This Matters for Operators

A bookkeeper's month is not spent typing numbers, it is spent finding the six invoices out of four hundred that do not add up. The arithmetic is trivial and the volume is not. An agent that answers "here is your spreadsheet" has moved the typing and left the checking. An agent that answers "here are six things to check, here is the file" has moved the part that takes the time.

The second reason is provenance. A `Checks` sheet inside the workbook survives being emailed to an accountant; a chat message does not. When a client asks why a figure was flagged, the reason travels with the file.

## What It Actually Does

Three tools, all read-through:

| Tool | Input | Output |
|---|---|---|
| `check_invoices` | `invoices[]` | findings and totals per currency, no file |
| `create_invoice_spreadsheet` | `invoices[]`, `title` | `.xlsx` download link valid 24 hours, plus the same findings |
| `list_spreadsheet_templates` | none | six blank templates as direct `.xlsx` links |

An invoice object carries **14** fields - `supplier`, `supplier_tax_id`, `invoice_number`, `po_number`, `date`, `currency`, `net`, `vat`, `vat_rate`, `total`, `description`, `category`, `notes`, `line_items` - and none of them is required, which is the correct schema for paper that arrives half-printed. `line_items` takes up to **2,000** rows with `description`, `quantity`, `unit_price` (and net, VAT, currency and category per line); one request carries up to **200** invoices.

## The five-invoice run, and what fired

A test set of five invoices was built to exercise each check exactly once: a clean invoice, a duplicate copy of it, one whose net plus VAT misses its total, one whose line items sum below its net, and one handwritten receipt with no header at all. `check_invoices` returned **6** findings:

| Invoice | Severity | Finding |
|---|---|---|
| INV-1001 (row 2) | Error | Same supplier and invoice number as invoice 1: likely a duplicate |
| KF-2207 (row 3) | Error | Net 500.00 plus VAT 90.00 is 590.00, but the total is 600.00 |
| KF-2207 (row 3) | Warning | VAT 90.00 is not 20% of net 500.00 (that would be 100.00) |
| row 5 | Warning | Supplier is missing |
| row 5 | Warning | Invoice number is missing |
| row 5 | Warning | Invoice date is missing |

Both arithmetic findings were re-derived by hand: `500.00 + 90.00 = 590.00` against a printed total of `600.00`, and `500.00 x 20% = 100.00` against a printed `90.00`. The duplicate is keyed on supplier plus invoice number rather than on the whole record, which is why a duplicate with a different description still matched.

Totals came back per currency, as printed and never converted:

| Currency | Invoices | Net | VAT | Total |
|---|---|---|---|---|
| GBP | 3 | 2,500.00 | 490.00 | 3,000.00 |
| EUR | 1 | 250.00 | 50.00 | 300.00 |
| USD | 1 | 75.50 | 0.00 | 75.50 |

Note what the GBP net of `2,500.00` includes: the invoice with the wrong total. **The totals add up what was printed; the `Checks` sheet is where the correction lives.** That is the right split - a spreadsheet that silently corrected a supplier's invoice would be a worse document than one that shows the invoice and flags it.

## The workbook, opened

The download link is a capability URL on the vendor's own host, `https://invoicestospreadsheets.com/api/sheets/<22-character token>`, returned with `content-disposition: attachment; filename="CorpusIQ-invoice-check-2026-11-13.xlsx"` and an `expires_at` exactly **24 hours** after creation. It answered **200** without any credential, which is worth saying plainly: anyone holding the link can fetch the file for a day, so treat the link the way you would treat an emailed attachment.

The workbook that arrived had the four sheets the description promises:

- **Invoices** - 14 columns, one row per invoice, with an `Invoice ID` (`INV-001` to `INV-005`) and a `VAT rate (%)` column added by the service. Empty cells are omitted from the XML rather than written as blanks, so the columns stay aligned.
- **Line Items** - one row per line item with invoice number, supplier, description, quantity and unit price, cross-referenced to its `Invoice ID`.
- **Checks** - row, invoice ID, invoice number, severity and the sentence to act on; **6** rows for **6** findings.
- **Totals** - the per-currency block above, verbatim.

## The check that never fires

The tool description says `check_invoices` reports "whether line items add up". Two targeted tests say it does not.

An invoice with net **250.00** and two line items of **100.00** each returned:

> Checked 1 invoice. No arithmetic, completeness or duplicate problems found.

An invoice with net **100.00** and one line item of quantity **3** at **40.00** (that is 120.00) returned the same clean bill of health. Both are genuine 50.00 and 20.00 gaps between the lines and the net, both are the exact class of error the description promises to catch, and neither produced a finding, an error or a warning.

This matters more than a missing feature usually does, because the tool's whole reason to exist is the check it advertises. A team that reads "line items add up" on the tin will trust a clean report as evidence that the lines were verified. They will not be.

## Two more defects, both small and both worth knowing

**A null VAT is read as 0.00.** An invoice with `vat_rate: 19` and `vat: null` was reported as "Net 100.00 plus VAT 0.00 is 100.00, but the total is 119.00". The instruction string tells the assistant to send `null` for a value that is not printed and never to estimate it - but the checker then substitutes a zero and compares against it. The invoice would have been correct at 19%. What should have been reported is that VAT was missing.

**The Line Items `Net` and `VAT` columns are always empty.** Both columns exist on the sheet, quantity and unit price are populated, and the product of the two is left blank for the reader to compute.

## The blank templates

`list_spreadsheet_templates` returns six real `.xlsx` files at their own URLs, which is a quieter feature than the invoice path and probably useful on its own: an invoice tracker, a UK self-employed income and expenses sheet under Self Assessment headings, CIS subcontractor payments by tax month, landlord income and expenses per property and tax year, construction job costs against a budget, and property development costs against an appraisal. Every one is a UK-shaped document, which tells you who the vendor built this for.

## Setting it up in Hermes

```bash
hermes mcp add invoices-to-spreadsheets --url https://invoicestospreadsheets.com/api/mcp
hermes mcp test invoices-to-spreadsheets
```

No key, no account, no configuration. The assistant reads the invoice files itself and passes the values as printed; the server refuses to guess what it was not given.

## Where this sits in the catalog

Two neighbours, neither a duplicate. [DocQuery](/hermes/mcp/servers/external/docquery-mcp/) owns the document-to-table join: spreadsheets and PDFs inside one workspace, queried by SQL, on a public demo key. [CalcBloc](/hermes/mcp/servers/external/calcbloc-mcp/) owns payroll arithmetic with a source attached to every figure. Invoices to Spreadsheets owns the reconciliation layer that sits between them - the arithmetic, completeness and duplicate check over a batch of supplier documents - and it is the only one of the three that returns a file an accountant will accept. The slice is real; the line-item check is the gap.

## Limitations recorded

- The advertised line-item check does not fire on either gap tested (250.00 against 100 + 100, and 100.00 against 3 x 40.00).
- A `null` VAT is reported as `0.00` and compared against the total instead of being flagged as missing.
- The Line Items sheet never fills its `Net` or `VAT` columns.
- Totals follow the printed totals, including ones the `Checks` sheet calls wrong; the workbook is a record, not a corrected ledger.
- The download link is a bearer capability URL valid for 24 hours with no authentication on the fetch.
- Six templates, all United Kingdom tax shapes; nothing for EU VAT or US sales tax.
- No tax advice, no filing, and no PDF reading by design - the client does the extraction.

### Does it need an account?

No. `initialize`, `tools/list` and all three tools answered with no credential on 2026-11-13, and the download link fetched without one.

### Can it fix an invoice that fails a check?

No, and that is deliberate. It reports; the correction stays with the person who has the supplier's document in front of them.

### What happens after 24 hours?

The download link expires. The workbook is not gone from the account that made it because there is no account - the API returns the file once and keeps a link alive for a day.
