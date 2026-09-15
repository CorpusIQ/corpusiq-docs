---
title: "Gemina MCP - Document Extraction and Tagging for Agents"
description: "Hosted document intelligence from Gemina: extract, tag, search and aggregate invoices, receipts, contracts, forms and your own custom templates with 13 tools. OAuth 2.1 sign-in or API key, free FileTag tier, data residency in the EU, US, Israel or Asia. Endpoint api.gemina.co/api/v1/mcp/."
category: Document Intelligence
stars: "n/a (hosted, no public repo)"
added: 2026-08-30
source: "mcp.so feed (listed Jul 21, 2026; first evaluated Aug 30)"
relevance: ★★
tags: [mcp-server, documents, ocr, extraction, invoices, contracts, tagging, oauth]
---

# Gemina MCP

**Extract, search and tag any document from any MCP client.** Gemina turns invoices, receipts, contracts, forms or your own templates into structured, searchable data with 13 tools over a hosted endpoint. One sign-in (OAuth 2.1) or an API key, a free FileTag tier, and data residency choices in the EU, US, Israel or Asia.

```
Server type: Hosted (Streamable HTTP)
Endpoint: https://api.gemina.co/api/v1/mcp/
Auth: OAuth 2.1 sign-in (from Claude Code, Cursor, VS Code, Codex, ChatGPT and more) or an API key
Tools: 13 (extract, index, query, aggregate, tag, templates, feedback)
Pricing: Free FileTag tier; paid plans for extraction volume (gemina.co)
Residency: EU, US, Israel or Asia (chosen at signup)
Console: console.gemina.co
Built by: Gemina (gemina.co)
```

## Why This Matters for Operators

Document-heavy back offices - AP, AR, contract review, compliance - are exactly the workflows agents are good at and bad at the same time: good at reading, bad at remembering where the field was. Gemina's design targets that split.

First, **extraction is a first-class tool, not a side effect.** `extract_document` pulls structured fields from invoices, receipts, contracts and forms; `get_extraction_result` and `list_extractions` let the agent check on and reuse past runs instead of re-reading originals.

Second, **your own templates mean your own schema.** `custom_template` lets you define the fields for your document types, so the extracted JSON matches your systems rather than a generic receipt schema.

Third, **tagging and querying close the loop.** `tag_file` and `tag_url` build a searchable index, `index_document`, `query_documents` and `aggregate_documents` answer questions across the corpus, and `submit_extraction_feedback` tunes results over time.

## Tool Groups (13 tools)

- **Upload:** `files_create_upload`, `files_create_extraction_upload`
- **Extraction:** `extract_document`, `get_extraction_result`, `list_extractions`
- **Index and query:** `index_document`, `query_documents`, `aggregate_documents`
- **Tagging:** `tag_file`, `tag_url`
- **Templates and onboarding:** `custom_template`, `explain_filename_patterns`, `explain_upload_flow`
- **Feedback:** `submit_extraction_feedback`

Tool names recovered from the mcp.so listing state (Aug 30, 2026); the listing advertises 13 tools, and the recovered set matches that count.

## Verification (Aug 30, 2026)

- Endpoint URL recovered from the vendor's own official MCP config snippets on gemina.co/product/agents (streamable-http, oauth per the snippet's transport and auth fields)
- mcp.so listing: websiteUrl gemina.co/product/agents, description confirms OAuth 2.1 or API key, free FileTag tier and residency options
- Tool names recovered from the listing's embedded state

## Notes and Caveats

- Hosted only: no self-host or stdio variant
- Metered extraction: the free FileTag tier covers tagging; extraction volume is plan-tiered
- Residency is a signup-time choice: verify the region before routing sensitive documents
- No public repo or star history: the surface is the hosted product

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [PassportCraft MCP: EU Digital Product Passports](/docs/hermes/mcp/servers/external/passportcraft-mcp)
- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/docs/hermes/mcp/servers/external/bulktranscripts-mcp)
