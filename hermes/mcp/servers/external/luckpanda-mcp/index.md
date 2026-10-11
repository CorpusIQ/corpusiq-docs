---
title: "LuckPanda MCP - Invoices, Quotes and Receipts for Agents"
description: "Create invoices, quotes, proforma invoices, receipts and credit notes from any AI assistant: prefilled links or branded PDFs with GST, VAT and sales tax."
category: Finance & Accounting
stars: n/a (keyless public server)
added: 2026-10-11
source: "mcpservers.org /all (Oct 11, 2026 midday sweep)"
relevance: ★★★
tags: [invoicing, documents, gst, vat, pdf, keyless, remote-mcp]
---

# LuckPanda MCP

**Remote MCP server (Streamable HTTP, keyless public endpoint)** - connects any MCP client to a document generator for small-business paperwork: invoices, quotes, proforma invoices, receipts and credit notes, in any currency, with India GST, UK and EU VAT and US sales tax worked out per line.

```
Server type: Remote (Streamable HTTP)
Auth: None on the public server (rate-limited); the account server uses an agent key
Public endpoint: https://luckpanda.app/mcp/public
Account endpoint: https://luckpanda.app/mcp
Tools: 9 (documents, rules, calculators)
Pricing: free to create; signing in covers numbering, sending and getting paid
Built by: LuckPanda
Listing: mcpservers.org (Oct 2026)
```

## Why This Matters for Operators

Paperwork is the tail of every job: the quote that has to go out before the work, the invoice after it, the receipt the customer asks for, the credit note when something comes back. It is small work that eats hours, and it is exactly the kind of small work an assistant can draft in one request.

LuckPanda puts document creation behind an MCP endpoint with a deliberate rule: agents propose, people decide. Every document comes back as a draft link (or a PDF with a verification code), marked as filled in from a link, and nothing is numbered, sent or paid until the owner signs in. Tax is handled where the document lives: GST split and state codes for India, VAT contents for the UK and EU, sales tax for the US, per line.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_tools` | Lists the document pages (invoice, quote, proforma, receipt, credit note) and calculators, filterable by type, country or keyword |
| `get_document_rules` | Returns the fields and tax rules to collect for a type and country: tax ID names, required and recommended fields, GST split and state codes, credit-note reasons |
| `create_document_link` | Creates a prefilled document link that opens the editor as a draft, marked as filled in from a link |
| `create_document_pdf` | Creates a branded PDF with a verification code; 40 an hour and 150 a day per network |
| `calculate_gst` | Calculates India GST, including the CGST/SGST versus IGST split |
| `calculate_vat` | Calculates VAT |
| `calculate_emi` | Calculates a loan EMI |
| `check_gstin` | Checks the format of a GSTIN |
| `find_hsn_code` | Finds an HSN or SAC code for India GST |

The public server is keyless and rate-limited per network; the account server at `https://luckpanda.app/mcp` connects a business's own data (customers, items, numbering) with an agent key.

## Installation

```bash
claude mcp add --transport http luckpanda-tools https://luckpanda.app/mcp/public
```

Claude desktop and web use Settings, Connectors, Add custom connector. ChatGPT uses developer mode, Create, with authentication set to none. Cursor and VS Code declare the same URL as an http server. Any MCP client that accepts a remote server works the same way.

## FAQ

### Does the agent need an account or API key?
No. The public server is keyless, and the agent guide at `luckpanda.app/agents.md` is the setup reference. Rate limits (40 an hour and 150 a day for PDFs) keep the free surface sane.

### Can the agent send an invoice or take a payment?
No, by design. Every document is a draft: agents never issue, number, send or take payment. The person checks the draft, downloads it, and signs in only to number, send and get paid.

### Which taxes and currencies are covered?
India GST with the CGST/SGST and IGST split and state codes, UK and EU VAT, and US sales tax, across any currency, worked out per line. Tax results are general guidance, not tax advice.

### Where can the documents go?
Each draft link opens the editor with the document filled in, and the PDF endpoint returns a branded, paginated file with a verification code, ready to attach to an email or hand to a customer.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
