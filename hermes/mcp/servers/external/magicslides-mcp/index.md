---
title: MagicSlides MCP
description: Presentation generation over MCP — turn any topic into a designed slide deck, document, spreadsheet or meeting notes from chat, with 70+ templates, a hosted share link, an editor, and PPTX/PDF export.
category: Productivity
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★
tags: [presentations, slides, documents, spreadsheets, meeting-notes, office]
---

# MagicSlides MCP

**Hosted document-generation server (remote connector, no API key)** — MagicSlides turns plain-language requests into designed deliverables: slide decks from 70+ templates, rich documents, spreadsheets, and structured meeting notes. Every result gets a hosted share link, a live editor, and PPTX/PDF export. Authentication is a sign-in, not a key — the operator connects once and the client handles the rest.

```
Server type: Hosted remote (connector install, no API key)
Auth: MagicSlides account login (OAuth-style flow, nothing to paste)
Endpoint: Connector URL installed via the magicslides.mcpb extension or manual add
Tools: Deck, doc, sheet, and meeting-note generation plus in-place edits
Pricing: Early access — all tools free
Category: Productivity
Built by: magicslides.app
```

## Why This Matters for Operators

Deck building is where operator time goes to die — the slide polish eats the analysis. MagicSlides splits the work the right way: the operator's AI writes the content, MagicSlides fills the template, resolves images, and hosts the result. "Make a 10-slide investor pitch for my SaaS in the editorial template" becomes a Present, Download PPTX/PDF, or Edit button — not a weekend.

The editing loop is the differentiator: ask the agent to revise an existing document or spreadsheet and it reads the current version, reasons about the change, and rewrites in place. No re-uploading, no starting over. It also stays out of the way of the model — MagicSlides adds no AI charges of its own, the operator's assistant does the writing.

## Tools & Capabilities

| Output | Capability |
|---|---|
| Presentations | Full designed decks, template-filled, hosted with a live present link |
| Documents | Rich docs with share link and editor |
| Spreadsheets | Sheets built from rows or structured data, editable in place |
| Meeting notes | Transcript to structured note — summary, action items, decisions |
| Edits | Agentic revision of existing docs and sheets, rewritten in place |

## Installation

Download the `magicslides.mcpb` extension, double-click to install (Claude, Cursor, and VS Code open pre-filled), then log in with MagicSlides when prompted. Or add the connector URL manually to any MCP client and sign in — there is no API key to generate or manage, and the connection can be revoked from MagicSlides at any time.

## Business Relevance

- **Founders** produce investor decks and board materials from conversation, with PPTX export for distribution
- **Operators** turn meeting transcripts into structured notes with action items in one pass
- **Finance teams** build budget sheets from structured numbers without spreadsheet fiddling
- **Agencies** draft client documents in the client's voice, then edit in place through review cycles

## Integration with CorpusIQ

MagicSlides is the presentation layer over the data layer CorpusIQ provides: CorpusIQ answers "what do the numbers say" across QuickBooks, GA4, and CRM connectors, and MagicSlides turns that answer into a board-ready deck with a share link. The QBR workflow — pull metrics through CorpusIQ, draft the deck through MagicSlides, review in the editor — covers the full deliverable loop without leaving the chat.

## Limitations

- Early-access pricing is free now; paid tiers are expected but unpublished
- Template library (70+) covers common use cases but not deep brand systems
- Your AI does the writing — output quality tracks the assistant in use
- Hosted service; documents live in MagicSlides infrastructure with share links

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
