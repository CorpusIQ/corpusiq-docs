---
title: "Harness Atlas MCP - Wire-Harness Sourcing and Part Cross-Reference"
description: "Hosted keyless MCP server for wire-harness and cable-assembly sourcing. find_manufacturer searches the manufacturer directory by country, industry, capability or name; find_alternative cross-references part numbers against the XrefBase equivalence graph with verified replacement groups."
category: Business Operations
stars: 0
added: 2026-08-25
source: "mcp.so GitHub issue #3736"
relevance: ★★★
tags: [mcp-server, sourcing, wire-harness, manufacturing, supply-chain, cross-reference, procurement]
---

# Harness Atlas MCP

**Structured sourcing data for wire harnesses and cable assemblies.** Harness Atlas answers the two questions an agent cannot answer from general web knowledge: who manufactures this, and what part can replace this one. It is a hosted, public, keyless MCP server with per-field provenance, so sourcing agents query a structured directory instead of guessing from trade-directory PDFs.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://harnessatlas.com/api/mcp
Auth: None (public, unauthenticated)
Registry: io.github.pawel-kowalczyk/harness-atlas (v0.2.0, active)
Repo: github.com/pawel-kowalczyk/harness-atlas-mcp (MIT, Aug 2026)
Tools: 2 verified by live probe (find_manufacturer, find_alternative)
```

## Why This Matters for Operators

Wire-harness sourcing data is scattered across trade directories, PDF catalogues, and manufacturer sites that general-purpose models summarize badly and cite unreliably. Harness Atlas is a structured directory of the sector with per-field provenance, exposed over MCP so an agent can query it directly. Procurement engineers spend hours compiling manufacturer shortlists by country, industry, and process capability; the agent gets a filtered, cited result in one call, then cross-references part numbers against the XrefBase equivalence graph to find verified replacements instead of risking substitute parts.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `find_manufacturer` | Searches the wire-harness and cable-assembly manufacturer directory with optional filters: country, industry (aerospace, automotive, electronics, energy, hvac, industrial, marine, medical, off-road, rolling-stock, telecommunications, and more), process capability (crimp force monitoring, ultrasonic welding, overmolding, testing, IPC WHMA 620, and more), or name |
| `find_alternative` | Cross-references a component part number (connectors, terminals, seals, cable protection) against the XrefBase equivalence graph, grouped by relationship strength |

`find_alternative` result groups are explicit and not interchangeable: `verified_replacements` (corroborated drop-in or manufacturer-superseded parts), `functional_equivalents` (same job, needs engineering review), `same_series` and `variants` (same family, different configuration, not substitutes), and `mates_with` (the counterpart it plugs into).

## Installation

No installation. Connect any MCP client to the keyless endpoint:

```bash
claude mcp add --transport http harness-atlas https://harnessatlas.com/api/mcp
```

The endpoint moved to `harnessatlas.com` on 2026-08-24 (manifest v0.2.0). The previous URL still works and is not being retired, but the new address is canonical.

## Configuration

No API keys or environment variables. Punctuation and case are normalized in part numbers, so `1-967616-1` and `19676161` match the same record.

## Business Relevance

- **Manufacturer shortlisting:** filter the directory by country, industries served, and capabilities in one query.
- **Obsolescence management:** find verified replacements for discontinued connectors and terminals before they stop production.
- **Supplier discovery:** build a sourcing shortlist with profile URLs and plant counts without manual directory crawling.

## Integration with CorpusIQ

Harness Atlas output drops cleanly into procurement workflows: pair manufacturer search results with CorpusIQ's email connector to reach out to shortlisted suppliers, or log verified replacement decisions alongside ERP part records via the database connector.

## Limitations

- Directory scope is wire-harness and cable-assembly manufacturers; general electronics components are out of scope.
- `find_alternative` groups are relationship-graded; treat only `verified_replacements` as drop-in without engineering review.
- Catalog is young (first published Aug 2026); directory coverage grows with the maintainer's data pipeline.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Electronics RFQ Agent MCP - RFQ-to-Quote ERP Automation](/docs/hermes/mcp/servers/external/electronics-rfq-mcp)
- [Walmart Marketplace MCP](/docs/hermes/mcp/servers/external/walmart-marketplace-mcp)
