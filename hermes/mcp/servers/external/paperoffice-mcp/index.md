---
title: PaperOffice AI MCP - Headless Document Management for Agents
description: "PaperOffice is the headless DMS an agent can operate: search, read, upload, extract and sign documents with AI-OCR and e-signatures."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (mcp.paperoffice.ai)"
relevance: ★★★
tags: [dms, document-management, ocr, invoice-capture, e-signature, audit-trail, eu-hosting, remote-mcp]
---

# PaperOffice AI MCP

**A document management system with no UI tax, because agents operate it directly.** PaperOffice is a headless DMS exposed through one MCP endpoint at `https://mcp.paperoffice.ai/dms`. Agents search, read, upload, extract and sign business documents with no glue code: AI-OCR, invoice capture and 60-plus IDP collections, e-signatures and a full audit trail. Fourteen tools plus discovery tools reach 300-plus API and MCP tools. Hosting is EU Tier III data centres on the vendor's own hardware with no third-party AI subprocessors, and bring-your-own-storage is available.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (Client ID Metadata Documents) or user token / po_gt_ group token
Endpoint: https://mcp.paperoffice.ai/dms
Tools: 14 plus discovery to 300+ API/MCP tools
Pricing: free account available; vendor plans
Category: Business Operations / DMS
Built by: PaperOffice (paperoffice.ai)
```

## Why This Matters for Operators

Document operations are the classic glue-work sink: find the contract, extract the invoice fields, route it for signature, file it back. PaperOffice removes the glue by making the DMS the agent's native surface. The agent searches the archive, extracts structured fields, sends documents for signature and keeps every action in the audit trail, which is the part operators will actually be asked about in a dispute or an audit.

The EU hosting posture matters for operators with data residency obligations: Tier III data centres, own hardware, no third-party AI subprocessors, and bring-your-own-storage for those who must keep files in their own bucket.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Search | Find documents across the archive |
| Read | Open and read document content |
| Upload | File documents into the DMS |
| Extract | AI-OCR and IDP extraction across 60+ collections, including invoices |
| Sign | E-signatures with a full audit trail |
| Discovery | Reach 300+ additional API and MCP tools |

## Installation

```bash
claude mcp add paperoffice --transport http https://mcp.paperoffice.ai/dms
```

First connect opens the PaperOffice sign-in for OAuth; token-based auth is documented for headless use.

## Configuration

```json
{
  "mcpServers": {
    "paperoffice": {
      "type": "http",
      "url": "https://mcp.paperoffice.ai/dms"
    }
  }
}
```

System and publishable keys are rejected; only user tokens or group tokens authenticate.

## Business Relevance

- **Ops teams** replace manual filing and extraction with agent-driven flows
- **Finance operators** capture invoice data straight from the archive
- **EU businesses** get compliant hosting without third-party AI subprocessors
- **Compliance leads** get an audit trail on every document action

## Integration with CorpusIQ

PaperOffice pairs with CorpusIQ's document and finance connectors: extracted invoice fields can reconcile against QuickBooks invoices, and signed contracts can be logged against HubSpot companies through the CorpusIQ CRM connector. CorpusIQ's cash-recovery engine can search PaperOffice for contract terms while QuickBooks lists overdue balances.

## Limitations

- Deep feature set (300+ tools) is reached through discovery tools rather than a flat list
- EU hosting may not fit operators with other residency requirements
- Vendor product family is broad; the MCP surface is the newest entry point
- New listing; free account scope is limited to the trial surface

## FAQ

### How is the archive reached?

One MCP endpoint to search, read, upload, extract and sign documents, with no UI and no glue code.

### Where is data hosted?

EU Tier III data centres on the vendor's own hardware with no third-party AI subprocessors, plus bring-your-own-storage.

### What auth modes are supported?

OAuth 2.1, or a user token or po_gt_ group token; system and publishable keys are rejected.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
