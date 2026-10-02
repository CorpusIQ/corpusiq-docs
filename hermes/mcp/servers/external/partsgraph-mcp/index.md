---
title: "Partsgraph MCP - Electronic Parts Search and BOM Building"
description: "Keyless MCP catalog for electronic and mechanical parts: provenance-backed search, part records with datasheet-sourced specs, compatibility checks, and priced BOM building over the Partsgraph demo catalogue. Live endpoint, no auth, 11 tools verified."
category: Business Operations
stars: n/a (hosted)
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★
tags: [mcp-server, parts, sourcing, bom, procurement, electronics, datasheets]
---

# Partsgraph MCP

**The agent-ready parts data layer.** Partsgraph turns product catalogs into a canonical Parts Graph and serves it to AI agents over MCP. The public demo catalogue carries provenance-backed part records with datasheet-sourced specs, compatibility checks, and BOM building for reference builds. The company model is enterprise: the same graph technology serves your own product catalog over MCP, agent-readable pages, and shopping feeds.

```
Server type: Remote Streamable HTTP (hosted, keyless)
Endpoint: https://partsgraph.ai/api/mcp
Auth: None
Tools: 11 verified by live probe (server v1.4.0)
Registry: ai.partsgraph/catalog
Scope: demo catalogue, 35 provenance-backed part records, 3 reference builds
```

## Why This Matters for Operators

Parts sourcing drowns in PDFs and vendor silos: a spec change means re-checking compatibility, and a BOM means pricing dozens of line items. Partsgraph makes the loop agent-native. `search_parts` finds real parts with provenance-backed attributes, `get_provenance` shows where each spec came from, `check_compatibility` validates part pairs before procurement, and `build_bom` composes a priced bill of materials. The demo catalogue is the public sandbox; the enterprise product applies the same tools to your own catalog.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_parts` | Search real electronic and mechanical parts with provenance-backed attributes |
| `get_part` | Full record for one part with datasheet-sourced specs |
| `get_provenance` | Provenance trail for a part's attributes |
| `compare_parts` | Side-by-side part comparison |
| `list_categories` | Browse the parts taxonomy |
| `list_builds` | Reference builds in the demo catalogue |
| `check_compatibility` | Compatibility checks between parts |
| `build_bom` | Compose a priced bill of materials |
| `search`, `fetch`, `view_bom` | Generic catalog search, retrieval, and BOM views |

## Installation

Connect directly; no account or API key required for the demo catalogue:

```json
{
  "mcpServers": {
    "partsgraph": { "type": "http", "url": "https://partsgraph.ai/api/mcp" }
  }
}
```

## Configuration

None for the public demo. The endpoint is Streamable HTTP with public initialize and tools/list. Enterprise deployments serve your own catalog as a Parts Graph over the same protocol.

## Business Relevance

- **Sourcing:** search and compare real parts with datasheet provenance instead of vendor PDFs.
- **Compatibility risk:** check part pairs before committing to a BOM.
- **Costing:** priced BOMs for early build-cost estimates.
- **Catalog strategy:** the enterprise product makes your own catalog agent-readable.

## Integration with CorpusIQ

Partsgraph's structured part and BOM output pairs with CorpusIQ connectors for procurement workflows: push BOM line items into Airtable or Notion for tracking, log supplier quotes in your CRM, and render BOM cost dashboards from the returned priced data.

## Limitations

- The public endpoint serves a demo catalogue (35 part records, 3 reference builds), not the full parts universe.
- Enterprise deployments for your own catalog are a commercial engagement with partsgraph.ai.
- No public repository; the platform is hosted.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Harness Atlas - Wire-Harness Manufacturer Directory and Cross-Reference](/hermes/mcp/servers/external/harness-atlas)
