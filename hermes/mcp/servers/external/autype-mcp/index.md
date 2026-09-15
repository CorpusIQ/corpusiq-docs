---
title: "Autype MCP - Branded Business Document Production for Agents"
description: Turn AI output into production-ready branded documents - create and revise reports, proposals, policies and forms from Extended Markdown with reusable styles, then render to PDF, DOCX, ODT or page images over OAuth 2.1 with per-tool scopes
category: Productivity
stars: n/a (new listing)
added: 2026-09-03
source: mcpservers.org
relevance: ★★★
tags: [document-generation, pdf, docx, templates, proposals, oauth, remote-mcp, brand-automation]
---

# Autype MCP

**Remote MCP server (Streamable HTTP) for production-ready branded business documents.** The agent authors in Autype Extended Markdown (AEM) plus compact JSON metadata - variables, citations, style preset IDs - and Autype renders to PDF, DOCX, ODT, PNG or JPEG with organizational styles applied. Build iteratively (create a session, append Markdown, render), reuse approved styles and content blocks, roundtrip Word documents, and process PDFs with OCR, classification and extraction. OAuth 2.1 with PKCE and dynamic client registration, per-tool scopes, no API keys in the client.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 PKCE + DCR; per-tool scopes
Endpoint: https://mcp.autype.com/mcp
Tools: 40+ (documents, renders, styles, reusable blocks, records, files)
Pricing: Requires Autype plan with Developer API access
Category: Document Production
Built by: Autype (autype.com)
```

## Why This Matters for Operators

The gap between "agent writes a report" and "report is branded, reviewed and sent" is where most document automation dies. Autype closes it inside one endpoint: the agent writes content, the organization's style presets do the branding, and the render engine produces the deliverable. Reusable blocks mean the legal boilerplate, the pricing table and the sign-off page are referenced, not regenerated - so the agent cannot drift them. The strict readiness check (`check_export_readiness`) catches redundant page breaks and broken references BEFORE credits are consumed.

**The consent model is the security model.** OAuth grants are bound to the selected organization and validated per tool - `read:documents`, `write:documents`, `render:documents`, `manage:resources`, `manage:files`, plus `offline_access` for rotating refresh tokens. A tool that needs an ungranted permission is rejected rather than silently broadened.

## Tools & Capabilities

| Tool family | Examples |
|---|---|
| Persistent documents | `documents_list`, `documents_create_markdown`, `documents_get_markdown`, `documents_patch_markdown`, `documents_render` |
| Render | `render_document` (AEM to PDF/DOCX/ODT), `render_document_images` (PNG/JPEG QA), `check_export_readiness`, `render_get_status`, `render_list_jobs` |
| Styles | `styles_list`, `styles_get`, `styles_create`, `styles_update`, `styles_delete` (workspace and immutable system presets) |
| Reusable blocks | `reusable_blocks_list`, `reusable_blocks_get`, `reusable_blocks_create`, `reusable_blocks_update`, `reusable_blocks_markdown_directive` |
| Records & files | `records_list` and file tools for media, PDF merge/split/convert/OCR, and DOCX roundtrip |

The Markdown-plus-metadata authoring model means agents never choose between "readable Markdown" and "full document control" - variables, citations and settings ride as separate fields, and advanced clients can still use the complete JSON schema.

## Installation

Add the remote URL in any MCP client that supports OAuth discovery:

```bash
claude mcp add --transport http autype https://mcp.autype.com/mcp
```

The client opens Autype in your browser: sign in, choose the organization, review the requested permissions, approve. ChatGPT, Claude, Claude Desktop, Claude Code, Cursor, Windsurf and VS Code (Copilot) are all documented; MCP Inspector is covered for testing.

## Configuration

Your Autype plan must include Developer API access. On sign-in you select the organization and approve scopes - that consent is the ceiling on everything the token can do. Organization style presets are managed in the Autype workspace and referenced by ID from the agent.

## Business Relevance

Consultancies, agencies and internal ops teams get branded proposal, report and policy production that repeats the company look without re-teaching the agent. The template-plus-approval workflow means reviewed documents stay reviewed; DOCX roundtrip keeps Word-native stakeholders in the loop. Credit cost per render is returned with the job status, so document spend is measurable.

## Integration with CorpusIQ

CorpusIQ answers operator questions from live business data. Autype is the last mile: the recap, proposal or policy an agent drafts from CorpusIQ numbers becomes a branded, citable, render-ready document with the organization's styles - closing the loop from data to deliverable without a human re-formatting pass.

## Limitations

- OAuth flow requires a browser on first connect and an Autype account with Developer API access
- Render jobs consume credits; strict validation is on by default
- Authoring language is Autype Extended Markdown (a superset of Markdown) - plain-Markdown habits mostly carry over

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Extend MCP - Document Intelligence with OCR and PDF Forms](/docs/hermes/mcp/servers/external/extend-mcp)
- [Gemina MCP - Document Extraction and Tagging for Agents](/docs/hermes/mcp/servers/external/gemina-mcp)
- [iFillPDF MCP - AI PDF Form Detection and Filling](/docs/hermes/mcp/servers/external/ifillpdf-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
