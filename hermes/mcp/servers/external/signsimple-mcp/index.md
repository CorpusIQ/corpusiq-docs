---
title: SignSimple MCP
description: Free e-signature workflow over MCP — send PDFs for legally binding signature, track status, and use free legal templates, with no per-document fees and no monthly caps.
category: Productivity
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★
tags: [esignature, document-workflow, contracts, legal-templates, esign-act, pdf-signing, document-automation, remote-mcp]
---

# SignSimple MCP

**Remote MCP server (Streamable HTTP, API key)** — SignSimple makes the free e-signature workflow fully programmable for agents: send a PDF, get it legally signed by emailed signing links, and download the certified result. Four MCP tools, a parallel REST API, and a template gallery of free legal documents sendable by stable URL.

```
Server type: Remote (Streamable HTTP)
Auth: API key (ss_live_..., via X-Api-Key or Authorization: Bearer)
Endpoint: https://signsimple.app/mcp
Tools: 4 (send_for_signature, get_document_status, list_documents, list_templates)
Pricing: Free — no per-document fees, no monthly caps
Category: Document Workflow / E-Signature
Built by: SignSimple (signsimple.app)
```

## Why This Matters for Operators

Contract signature is the classic last-mile manual step in automated workflows — the deal is agreed in email, the PDF sits on a desktop, and the operator becomes the courier. SignSimple removes the courier: an agent sends the PDF, the recipient gets an emailed signing link, and polling returns a signed PDF with a certificate page listing every signer, timestamp, and the SHA-256 hash of the original document.

**The differentiator is that the entire loop is free and unlimited** — no per-document fees, no monthly caps, PDFs up to 15 MB and 10 recipients per send, legally binding under the US ESIGN Act.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `send_for_signature` | Send a PDF by URL, name recipients, set expiry — returns envelope ID and signing links |
| `get_document_status` | Poll an envelope; when complete returns the certified signed PDF URL |
| `list_documents` | List sent documents and their states |
| `list_templates` | List the free template gallery (NDA, lease, contractor agreement, liability waiver, bill of sale, promissory note) |

## Installation

```bash
claude mcp add --transport http signsimple https://signsimple.app/mcp \
  --header "Authorization: Bearer ss_live_..."
```

Discovery works without a key; account tools need one. Keys are minted on the profile page, shown once, and stored only as a hash.

## Configuration

```json
{
  "mcpServers": {
    "signsimple": {
      "type": "http",
      "url": "https://signsimple.app/mcp",
      "headers": {
        "Authorization": "Bearer ss_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

Auth notes: the same key works against the REST API (full OpenAPI 3.1 spec at /openapi.json). Signature and date fields are placed on the last page unless you pass a `fields` array with exact geometry.

## Business Relevance

- **Founders and ops teams** get NDAs and contractor agreements out the door from inside any agent workflow
- **Sales operations** get a send → poll → download loop that closes paperwork without leaving the CRM context
- **HR and legal-light workflows** get lease, waiver, and bill-of-sale templates by stable URL
- **Agent builders** get discovery endpoints (llms.txt, openapi.json, agent-card.json, well-known MCP card) alongside the endpoint

## Integration with CorpusIQ

SignSimple composes cleanly with CorpusIQ's document and CRM connectors. A closed loop: HubSpot connector surfaces the deal, the agent drafts the agreement, SignSimple's `send_for_signature` gets it signed, and `get_document_status` drops the certified PDF back into Drive via the Drive connector. Pair with QuickBooks to attach the signed PDF to the invoice record once the envelope completes. Because SignSimple certifies each PDF with the original document's SHA-256 hash, the signature certificate and the stored document can be cross-checked later — the same verify-before-trust pattern CorpusIQ connectors apply to financial data.

## Limitations

- Brand new listing — no long track record yet
- US-centric: binding under the ESIGN Act; check local e-signature law for cross-border use
- Signature placement defaults to the last page unless exact field geometry is passed
- Commercial cloud service; no self-host option published
- Free tier is generous but the vendor controls the service level — no SLA published

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
