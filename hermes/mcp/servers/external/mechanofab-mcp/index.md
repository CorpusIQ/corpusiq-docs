---
title: "MechanoFab MCP - Manufacturing Knowledge for Agents"
description: "Query a manufacturing capability graph: materials, processes, ISO 2768 tolerances, equipment specs and instant quotes for CNC, molding and 3D printing."
category: Manufacturing & Industrial
stars: n/a (new listing)
added: 2026-10-11
source: "chatmcp/mcpso issue #5116 + official MCP Registry (com.mechanofab/mechanofab) + live endpoint probe; catalogued at the October 11, 2026 night sweep"
relevance: ★★★
tags: [manufacturing, cnc, injection-molding, 3d-printing, engineering, quotes, remote-mcp]
last_updated: "2026-10-24"
---

# MechanoFab MCP

**A manufacturing capability graph for AI agents, served keyless** - 20 engineering tools that answer the questions that usually cost a phone call: which material is equivalent to SS304, what tolerance ISO 2768 gives a 50 mm feature, which machine can hold a fine layer thickness, whether ABS survives 80 degrees C, what the medical device industry expects, and what a 3D printed part will cost. The vendor (MechanoFab) publishes it as an AI-native B2B manufacturing hub with 437+ solutions across injection molding, 5-axis CNC and 3D printing behind the knowledge base.

```
Server type: Remote (Streamable HTTP at https://mcp.mechanofab.com/mcp, keyless)
Auth: None (knowledge tools plus a quote calculator; no account required)
Tools: 20 (materials, processes, equipment, tolerances, compliance, quotes)
Category: Manufacturing & Industrial
Built by: MechanoFab (official MCP Registry entry com.mechanofab/mechanofab v1.0.0)
```

## Why This Matters for Operators

Manufacturing decisions run on lookups scattered across catalogs, standards and institutional memory: engineers comparing materials, procurement checking compliance, product teams sanity-checking tolerances and process choices before committing to a vendor, and anyone estimating what a printed part should cost before the quote comes back. Putting the knowledge base behind MCP means the assistant reaches the answer in the same conversation where the question came up - materials resolved from industry grades, trade names or Chinese terms, alternatives suggested when a lead time or price problem appears, ISO 2768 tolerance tables read directly, and `quote_calc` pricing 3D prints on the spot.

## Tools & Capabilities

All 20 tools verified against the live endpoint (keyless initialize 200, `mechanofab-mcp-server` v0.1.0; `tools/list` returns all 20):

| Group | Tools | What they do |
|---|---|---|
| Materials | `search_materials`, `compare_materials`, `find_equivalent_materials`, `filter_materials_by_constraint`, `match_industry_materials` | Resolve a material from an industry grade, trade name or Chinese term; compare pairs like AL6061 vs SS304; find replacements for SS304 or titanium; filter by constraints such as density, tensile strength or max temperature; match approved materials to industries |
| Compliance and environment | `get_material_compliance`, `check_material_environment_compatibility`, `check_service_temperature`, `get_industry_requirements` | RoHS and FDA-style regulatory checks, operating environment suitability (temperature, humidity, UV, chemicals), service-temperature ratings, and industry requirements such as aerospace or medical device expectations |
| Processes | `get_process_specs`, `compare_processes`, `find_alternative_processes`, `get_material_process_compatibility` | Process specs and constraints (tolerance, build volume), comparisons (SLS vs FDM vs SLA, CNC vs injection molding), alternatives when lead time or cost forces a switch, and which processes a material supports |
| Equipment | `find_equipment_by_process`, `compare_equipment`, `check_equipment_capability`, `get_equipment_qc_specs` | Find machines by process or material (PEEK-capable printers, large build envelopes), compare specific machines, check capability questions (layer thickness, part size), and read certification and dimensional-accuracy specs |
| Engineering math | `get_iso2768_tolerances`, `calculate_part_mass`, `quote_calc` | ISO 2768 general tolerance lookups by dimension, part mass and weight from volume and material, and 3D printing price calculation from material, color, lead time, quantity and part size |

## Installation

```json
{
  "mcpServers": {
    "mechanofab": {
      "url": "https://mcp.mechanofab.com/mcp"
    }
  }
}
```

Keyless: no account, no API key, no local install. Any MCP client that speaks Streamable HTTP can connect.

## Configuration and Safety

- Knowledge surface plus a quote calculator: the 20 tools answer engineering questions and calculate prices; nothing is bought, ordered or changed through them.
- Keyless endpoint: fine for evaluation and daily lookups; the public surface is new (v0.1.0), so expect it to move.
- Quotes: `quote_calc` computes a 3D printing price from the vendor's pricing data (material, color, lead time, quantity, part dimensions) - a planning number, not a binding quote.

## Business Relevance

- **Product teams and engineers**: material selection, tolerance checks and process comparisons before design freeze.
- **Procurement and sourcing**: equivalent-material swaps, compliance statements and equipment capability checks when qualifying suppliers.
- **Manufacturing and job shops**: quick pricing sanity checks and capability claims answered from a structured graph rather than a PDF.

## Integration with CorpusIQ

A manufacturing answer has two halves: the engineering capability itself, and the business context around it - what the last order cost, who the supplier was, how the margin moved. Run the mechanical check in chat, then ask CorpusIQ for the numbers your connectors already hold, every figure cited. One thread, engineering and business side by side.

## Limitations

- The MCP surface is young (v0.1.0) and the vendor's public documentation is thin beyond the tool schemas themselves; `tools/list` is the live source of truth.
- Coverage is the vendor's published knowledge base (they advertise 437+ solutions); materials and equipment outside it will not resolve.
- `quote_calc` covers 3D printing pricing; quoting for other processes goes through the vendor's own platform.
- It is a knowledge tool, not a certification: compliance outputs summarize the vendor's data and do not replace the certificate itself.

## FAQ

### Does the MechanoFab MCP server cost anything?

No - the endpoint is keyless and public: initialize returns 200 with no account, and all 20 tools list without authentication.

### What is the fastest useful query?

Price sanity checks and material swaps: ask for an equivalent to a material you already buy, or run a quote calculation on the part in front of you; both return structured answers on the spot.

### Is it an official server?

Yes - it is published in the official MCP Registry as `com.mechanofab/mechanofab` (v1.0.0) and served by the vendor at `mcp.mechanofab.com`.

## See Also

- [CuttingToolsAI MCP - Carbide Grade Cross-Reference for Machining](/hermes/mcp/servers/external/cuttingtoolsai-mcp)
- [Harness Atlas MCP - Wire Harness Manufacturer Directory](/hermes/mcp/servers/external/harness-atlas)
- [Gemalli B2B Trade MCP](/hermes/mcp/servers/external/gemalli-b2b-trade-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
