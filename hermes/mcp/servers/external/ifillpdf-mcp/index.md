---
title: iFillPDF MCP - AI PDF Form Detection and Filling
description: Hosted MCP server that detects fillable fields in any PDF - including scanned and photographed paper forms - fills and signs them, and returns a finished flattened document.
category: Content
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3766"
relevance: ★★
tags: [pdf, forms, documents, productivity, e-signature, document-automation, remote-mcp]
---

# iFillPDF MCP

**Remote MCP server (Streamable HTTP, OAuth)** - iFillPDF detects fillable fields in any PDF with AI, fills them and signs them, and returns a finished, flattened document. Field detection works on arbitrary PDFs including scanned or photographed paper forms, and on documents with no AcroForm at all - the common case for administrative forms. Published in the official MCP registry as `com.ifillpdf/pdf` since 2026-07-27, hosted in the EU, endpoint live (OAuth protected resource verified by HTTP 401 on anonymous initialize).

```
Server type: Remote (Streamable HTTP)
Auth: OAuth - protected resource metadata at /.well-known/oauth-protected-resource
Endpoint: https://mcp.ifillpdf.com/mcp
Tools: Field detection, filling, signature, page operations (live list served from endpoint)
Pricing: Free tier without an account; one-off purchase removes the watermark
Category: Content
Built by: iFillPDF (ifillpdf.com)
```

## Why This Matters for Operators

Administrative paperwork is the last manual mile of business operations: tax forms, supplier questionnaires, permits and contracts that arrive as PDFs with no fillable structure. Staff retype the same company details into each one, or worse, print, hand-fill and scan.

**iFillPDF turns form filling into an agent task.** Give the server a PDF - or a photo of a paper form - and it returns a detected field map. Fill the values and get back a finished, flattened PDF, with signature and initials supported as image fields and page operations for reordering, deleting and inserting pages. The free tier needs no account, and the watermark removal is a one-off purchase rather than a subscription.

## Tools & Capabilities

iFillPDF publishes the live tool list from the endpoint; the table below groups the documented capabilities from the official listing.

| Capability | What it does |
|---|---|
| AI field detection | Detects fillable fields on arbitrary PDFs, including scanned and photographed forms |
| Filling | Fills detected fields with values and exports a finished, flattened PDF |
| Signature and initials | Places signature and initials as image fields |
| Page operations | Reorders, deletes and inserts pages from another PDF |
| AcroForm-free documents | Works on administrative forms with no fillable structure at all |

## Installation

```bash
claude mcp add ifillpdf --transport http https://mcp.ifillpdf.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "ifillpdf": {
      "type": "http",
      "url": "https://mcp.ifillpdf.com/mcp"
    }
  }
}
```

First connect runs the OAuth browser flow against the protected resource. The server manifest is published at ifillpdf.com/server.json and the docs at ifillpdf.com/mcp.

## Business Relevance

- **Operations teams** fill supplier questionnaires, permits and tax forms without retyping.
- **HR departments** complete onboarding paperwork from scanned templates.
- **Finance teams** process forms that arrive as paper photos, not structured PDFs.
- **Sales teams** assemble and sign contracts with page-level control in one flow.

## Integration with CorpusIQ

iFillPDF plugs into CorpusIQ's document-heavy workflows. A CorpusIQ-connected agent reading invoice and receipt data from QuickBooks or Stripe can generate the supporting form pack - tax declarations, vendor questionnaires, onboarding documents - via iFillPDF's field detection, pre-filling the values the connectors already hold so staff only review and sign. The flattened output stays archivable alongside the transaction record, closing the loop from business data to completed paperwork.

## Limitations

- Brand new - no track record yet, no public star count.
- OAuth required - no anonymous or API-key mode published.
- Live tool list is served from the endpoint; the listing groups capabilities rather than naming each tool.
- Free tier watermarks output; removal is a one-off purchase rather than a subscription.
- EU-hosted - documents leave your environment for processing.

## See Also

- [Acquisition.gov MCP - FAR Overhaul and Agency Deviations](/hermes/mcp/servers/external/acquisition-gov-mcp)
- [ATLASS OS MCP - Field-Service Business Platform](/hermes/mcp/servers/external/atlass-os-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
