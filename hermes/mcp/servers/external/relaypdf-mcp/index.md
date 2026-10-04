---
title: RelayPDF MCP - PDF Generation and Extraction
description: Remote and local MCP that generates PDFs from HTML, URLs, Markdown and templates, converts Office and image files, edits PDFs, and extracts OCR text and JSON.
category: Productivity
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [productivity, documents, pdf, conversion, ocr, extraction, remote-mcp, oauth]
---

# RelayPDF MCP

**Remote and local MCP server (Streamable HTTP with Clerk OAuth or Bearer key, plus npx stdio)** - RelayPDF handles document work for agents. It generates PDFs from HTML, URLs, Markdown and templates, converts Office files, images and email, edits PDFs (merge, split, fill, protect, optimize), and extracts OCR text and JSON. Generating tools return a 24-hour URL rather than filesystem paths or raw bytes, so hosted clients can consume output directly.

```
Server type: Remote (Streamable HTTP) + local stdio via npx
Auth: Clerk OAuth (browser login) or Bearer API key
Endpoint: https://api.relaypdf.com/mcp (or npx @relaypdf/cli mcp)
Tools: Generate, convert, edit and extract across PDFs and Office documents
Pricing: RelayPDF plan; free starting point on relaypdf.com
Category: Productivity
Built by: RelayPDF
```

## Why This Matters for Operators

Document work is where agent automation usually hits a wall: an assistant can draft a document but cannot produce a clean PDF, split a contract, or pull structured data out of a scanned invoice. RelayPDF's mechanism is **one surface for the whole lifecycle** - generate, convert, edit, extract - with hosted output delivered as short-lived URLs so nothing needs to touch a local filesystem.

For operators, that means proposals, invoices, contracts and reports move from draft text to shippable, human-ready files inside the assistant. Extraction in OCR text and JSON turns scanned documents into data an agent can act on, which is where back-office automation usually stalls.

**The key advantage is a full generate-convert-edit-extract document pipeline callable from any client, hosted or local.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Generate | Builds PDFs from HTML, URLs, Markdown and templates |
| Convert | Converts Office files, images and email into PDF and back |
| Edit | Merges, splits, fills, protects and optimizes PDFs |
| Extract | Pulls OCR text and structured JSON from documents |

Two transports expose the same tools: hosted Streamable HTTP for remote clients, and local stdio via npx for desktop clients after `relaypdf setup`.

## Installation

```bash
npx @relaypdf/cli mcp
```

Or add the hosted endpoint to a remote client: use POST https://api.relaypdf.com/mcp when the host needs a public URL (Claude, Relevance, remote Cursor).

## Configuration

```json
{
  "mcpServers": {
    "relaypdf": {
      "type": "http",
      "url": "https://api.relaypdf.com/mcp"
    }
  }
}
```

Hosted auth is Clerk OAuth (browser login) or a Bearer API key; agents should never ask a human to paste a key into chat. Generated output comes back as a 24-hour URL.

## Business Relevance

- **Operators producing proposals and invoices** can generate client-ready PDFs from a draft.
- **Back-office teams** can extract OCR text and JSON from scanned invoices and contracts.
- **Legal and compliance** can merge, split, fill and protect PDFs without a desktop editor.
- **Marketing teams** can turn Markdown and HTML templates into branded PDFs at volume.
- **Anyone wiring documents into agents** gets a hosted URL output that drops straight into other tools.

## Integration with CorpusIQ

RelayPDF is the document-output layer for CorpusIQ workflows. Where CorpusIQ's QuickBooks, Stripe and HubSpot connectors supply the numbers and records, RelayPDF turns an assistant's summary into a formatted, shippable PDF or extracts structured data from a scanned document back into the pipeline.

A composed workflow: pull monthly figures from CorpusIQ's QuickBooks connector, have the assistant assemble a report, then call RelayPDF to render it as a professional PDF and return a shareable URL. In reverse, RelayPDF extracts a scanned contract to JSON that an assistant can match against CorpusIQ's CRM records. CorpusIQ reads the business; RelayPDF produces and reads the paperwork.

## Limitations

- Hosted generation requires an account and plan; local stdio needs `relaypdf setup`.
- Generated files are served as 24-hour URLs, not persistent storage.
- OCR quality depends on scan quality and document layout.
- Hosted and proprietary; the npx client is the only self-hostable path.
- Complex PDF editing is bounded by what the tool surface exposes.

## FAQ

### Does RelayPDF work locally or only hosted?

Both. Hosted Streamable HTTP covers remote clients; local stdio via npx covers desktop clients after setup.

### How are generated files delivered?

Hosted generating tools return a 24-hour URL rather than a filesystem path or raw bytes.

### Can RelayPDF read scanned documents?

Yes. It extracts OCR text and structured JSON from documents.

### Do I need to paste an API key?

No. Hosted auth uses Clerk OAuth browser login; API keys are optional, and agents should never ask you to paste a key into chat.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
