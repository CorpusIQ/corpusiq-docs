---
title: "InvoiceParser Pro MCP - Invoice to Excel from Chat"
description: "Turn invoices into Excel or CSV, check the math and pull structured fields from any MCP client - PDFs and photos up to 10 MB, free trial."
category: Finance / Accounting
stars: n/a (hosted service, invoiceparserpro.com)
added: 2026-10-05
source: "mcpservers.org /all"
relevance: ★★
tags: [invoices, accounting, extraction, excel, finance, oauth, free-trial, remote-mcp]
---

# InvoiceParser Pro MCP

**Invoices in, spreadsheets and verified numbers out.** InvoiceParser Pro reads a supplier invoice the same way it does on its website - PDF or photo in, header fields, line items and totals out - and hands the result back inside the chat: an Excel file, a CSV, or structured JSON. Its distinctive move is the math check: every line against quantity times unit price, the lines against the subtotal, the tax against its printed rate, and the total, with a one-line verdict.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in or an ipp_mcp_ assistant key; a free trial lane works without either
Endpoint: https://api.invoiceparserpro.com/mcp
Tools: 4 (invoice_to_excel, check_invoice, extract_invoice_data, get_result)
Input: PDFs and photos up to 10 MB, via https link, base64 bytes, or a ChatGPT attachment
Pricing: Free trial; Free plan 25 invoices a month; paid plans per workspace
Built by: InvoiceParser Pro
```

## Why This Matters for Operators

Bookkeeping drudgery comes in two flavors: retyping invoices and discovering months later that a total did not add up. This server removes both from the human's plate. An operator forwards a bill and asks for the spreadsheet; the assistant calls `invoice_to_excel` and returns download links to .xlsx and .csv, plus every line item. When a number is suspect, the same chat runs `check_invoice` and reports each problem with the invoice's own figures, not a vague warning.

**The output is built to be filed, not just read.** Results come back as real spreadsheet files with links that work for an hour, and signed-in workspaces hold the documents like any website upload - so what the agent produced is the same artifact the accounting process already expects.

## Tools

| Tool | What it does |
|---|---|
| `invoice_to_excel` | Reads the invoice; returns header fields, every line item, and download links to an .xlsx and a .csv |
| `check_invoice` | Checks each line, the lines against the subtotal, the tax against its rate, and the total; returns a verdict and every problem found |
| `extract_invoice_data` | The whole read as JSON: vendor, customer, numbers, dates, PO number, currency, totals, tax lines, line items, and confidence per field |
| `get_result` | Fetches a slow read by job id when a document was still processing |

Each tool takes exactly one file: an https link the server can download (`file_url`), the file's bytes in base64 (`file_base64`), or a chat attachment in ChatGPT.

## Installation

Claude Code, without a key (sign in on first use):

```bash
claude mcp add --transport http invoiceparser-pro https://api.invoiceparserpro.com/mcp
```

Claude Code with an assistant key:

```bash
claude mcp add --transport http invoiceparser-pro https://api.invoiceparserpro.com/mcp \
  --header "Authorization: Bearer ipp_mcp_your_key"
```

Claude (web and desktop) adds it under Connectors, Add custom connector; ChatGPT connects it as an app in developer mode; Cursor and other JSON clients point at the same URL with an optional Authorization header. Signed out, the client uses the free trial lane; signed in, documents go into the chosen workspace and count against its plan.

## Business Relevance

- **Founders and office managers** turn a folder of supplier invoices into spreadsheet rows without retyping anything.
- **Bookkeepers and accountants** get a first-pass math check with the problem lines called out, before a human review.
- **Agencies billing clients** extract the fields they need (PO number, totals, tax) directly into the tools that need them.
- **Teams on the free plan** process up to 25 invoices a month with no card, then decide on a paid tier.

## Integration with CorpusIQ

Invoices describe what was billed; the ledger says what was paid. InvoiceParser Pro extracts the document side of that comparison: vendor, amounts, tax, due dates. CorpusIQ reads the systems side: QuickBooks, Stripe and the connected accounts. An operator can ask "does the invoice match what the ledger shows" and have the agent line the extracted fields up against real system data, both sides pulled read-only at answer time.

## Limitations

- One document per call: no batch folder uploads through MCP.
- PDFs and photos up to 10 MB; 60-minute spreadsheet links for unsigned sessions.
- Only public https links are downloaded: private, internal and plain-http addresses are refused, including through redirects.
- Free trial lane is limited to 3 documents a day per network address and can be exhausted on shared hosted assistants.
- Unsigned uploads and results are deleted after 7 days; signed-in workspaces persist the documents.

## FAQ

### Can I try it without an account?

Yes. The free trial lane processes up to 3 documents a day per network address, every answer ends with a link that saves results to a free account, and the Free plan covers 25 invoices a month.

### What does the math check actually verify?

Each line (quantity times unit price), the lines against the subtotal, the tax against its printed rate, and the total, returning a one-line verdict and every problem found, with the invoice's own numbers.

### Which file types work?

PDFs and photos, up to 10 MB, passed as an https link, base64 bytes, or a ChatGPT attachment. Links always work for hosted assistants; private or internal addresses are refused.

### Is my invoice data used elsewhere?

The document is read as on the website; unsigned uploads and results are deleted after 7 days, trial usage is counted under a keyed hash of the connection's IP, and workspace privacy details are on the vendor's security page.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [SuperBooks MCP - Bookkeeping for Agents](/hermes/mcp/servers/external/superbooks-mcp/)
- [gofact MCP - Local French E-Invoicing with Legal Numbering](/hermes/mcp/servers/external/gofact-mcp/)
- [Factur-X by Orvel MCP - Hosted French E-Invoicing for Agents](/hermes/mcp/servers/external/facturx-orvel-mcp/)
