---
title: "Extend MCP - Document Intelligence with OCR and PDF Forms"
description: "Turn documents into structured data from chat: OCR to markdown, field extraction, document classification, bundle splitting and PDF form filling across PDFs, images, Office files and emails."
category: Productivity
stars: n/a (new listing)
added: 2026-09-03
source: mcp.so
relevance: ★★★
tags: [document-processing, ocr, pdf, data-extraction, classification, document-ai, remote-mcp]
---

# Extend MCP

**Remote MCP server (Streamable HTTP, OAuth)** - Extend turns the messy document layer of a business into structured data an agent can act on: parse with OCR to markdown, extract fields, classify documents, split multi-document bundles and fill PDF forms, across PDFs, images, Office docs, spreadsheets and emails.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://mcp.extend.ai/mcp
Tools: capability set served from the endpoint (live tool list not yet indexed by mcp.so)
Pricing: account required (extend.ai)
Category: Productivity
Built by: Extend (github.com/extend-hq/extend-agent-plugin)
```

## Why This Matters for Operators

Every operator runs a parallel paper business: contracts that need fields pulled, invoice PDFs that need data, onboarding bundles that mix five document types. That work is currently either manual or a brittle per-format script. Extend moves it into the agent loop.

**The differentiator is scope in one call:** one hosted endpoint handles OCR, extraction, classification, bundle splitting and PDF form filling, so the agent does not need five different tools and a Python environment to process a client packet. The agent goes from "here is a folder of PDFs and images" to structured rows, classifications and filled forms.

## Tools & Capabilities

The live tool list is served from the endpoint; the listing documents these capability areas:

| Capability | Purpose |
|---|---|
| Parse | OCR any PDF, image, Office doc, spreadsheet or email to clean markdown |
| Extract | Pull named fields per natural-language instructions or a schema |
| Classify | Sort documents into types (invoice, contract, ID, report) |
| Split | Break multi-document bundles into individual documents |
| Fill forms | Populate PDF forms programmatically |

## Installation

```bash
claude mcp add extend --transport http https://mcp.extend.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "extend": {
      "type": "http",
      "url": "https://mcp.extend.ai/mcp"
    }
  }
}
```

First connect opens a browser for OAuth sign-in; the client reuses the session afterward. Setup snippets for Claude Code, Codex, Cursor and VS Code ship on the mcp.so listing page.

## Business Relevance

- **Operations teams** get invoice and contract fields extracted without OCR tooling
- **Agencies** can classify and split multi-document client packets in one instruction
- **Finance operators** get PDF form filling for standardized filings and applications

## Integration with CorpusIQ

Extend complements CorpusIQ's structured business data: CorpusIQ reads the system of record (QuickBooks, Stripe, HubSpot) while Extend handles the unstructured document layer around it. A composed workflow: Extend extracts line items from a vendor invoice PDF, CorpusIQ's QuickBooks connector verifies the vendor and amounts, and the agent flags mismatches. Extracted contact fields can flow into the HubSpot connector for CRM hygiene.

## Limitations

- Brand new listing with no public track record yet
- Tool names not yet indexed; capability table comes from the listing prose
- OAuth required - no anonymous or key-only access documented
- Commercial service; free tier details not published

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [DocMake MCP - Template-Driven DOCX and PDF Generation](/hermes/mcp/servers/external/docmake-mcp)
- [PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/hermes/mcp/servers/external/policyforge-mcp)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp)
