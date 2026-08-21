---
title: "CuttingToolsAI MCP - Carbide Grade Cross-Reference for Machining"
description: "Keyless remote MCP server with one read-only tool, grade_xref, that cross-references carbide insert grades across manufacturers at the same ISO application position: ask what is comparable to Sandvik GC4325 or Kennametal KC5010 and get catalog-verified comparable grades with provenance for every row, so procurement and CAM teams find equivalent inserts without vendor lock-in"
category: Data & Analytics
stars: 0
added: 2026-08-21
source: "mcp.so GitHub issue #3666"
relevance: ★★
tags: [manufacturing, machining, carbide, procurement, industrial-data, cross-reference, remote-mcp, cnc]
---

# CuttingToolsAI MCP

**Brand-neutral carbide grade cross-reference for machining, as a one-tool keyless MCP server.** CuttingToolsAI exposes a single read-only tool, `grade_xref`, that answers the procurement question that burns machining hours: "what is comparable to this grade?" Ask for Sandvik GC4325 or Kennametal KC5010 and the server returns catalog-verified comparable insert grades across manufacturers at the same ISO application position, with provenance for every row. The server never invents a grade — unknown codes return an empty result.

```
Server type: Hosted remote (Streamable HTTP, Cloudflare Worker)
Endpoint: https://cuttingtoolsai-mcp.memmizgezgin.workers.dev
Auth: None (no API key)
Tools: 1 (read-only, verified live Aug 21, 2026)
Server: cuttingtoolsai-xref v1.0.0
License: MIT
Repository: memmizgezgin-creator/cuttingtoolsai-mcp
Built by: CuttingToolsAI (cuttingtoolsai.eu)
```

## Why This Matters for Operators

Machine shops lose real money when a preferred grade is discontinued, on backorder, or marked up. The existing workflow — thumbing manufacturer catalogs or asking a distributor who has an incentive — is slow and vendor-biased. CuttingToolsAI encodes the comparison logic from manufacturer-published application charts and serves it through an MCP endpoint, so a CAM programmer, quoting engineer, or procurement agent can ask for equivalents in one call and get rows with provenance.

The scoping is honest: comparability means a shared ISO application position in manufacturer-published charts, not physical interchangeability — the tool description says so explicitly. No tools are sold and no manufacturer commission is taken.

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| `grade_xref` | Comparable carbide grades across manufacturers at the same ISO application position, with provenance per row. Parameters: `grade` (required), `brand` (optional) |

Live probe Aug 21, 2026: server `cuttingtoolsai-xref` v1.0.0, `grade_xref` confirmed on the endpoint. Unknown grade codes return an empty result rather than a guess.

## Installation

```bash
claude mcp add --transport http cuttingtoolsai https://cuttingtoolsai-mcp.memmizgezgin.workers.dev
```

```json
{
  "mcpServers": {
    "cuttingtoolsai": {
      "type": "http",
      "url": "https://cuttingtoolsai-mcp.memmizgezgin.workers.dev"
    }
  }
}
```

No API key and no self-hosting — the server is a Cloudflare Worker fronting the public REST endpoint at cuttingtoolsai.eu/api/xref, which is also listed in public-apis.

## Configuration

Nothing to configure. The single tool is stateless and read-only. The backing data is the public xref endpoint; rate limits are not published on the free endpoint, so treat heavy batch lookups as best-effort.

## Business Relevance

- **Machine shops** resolve equivalents when a preferred grade is discontinued or backordered
- **Procurement teams** build vendor-neutral RFQs and spot grade-level markup before quoting
- **CAM programmers** substitute inserts without re-quoting the whole job
- **Job shops quoting new work** check whether a customer-specified grade has a cheaper comparable before pricing

## Integration with CorpusIQ

CuttingToolsAI supplies the technical data point — the equivalent grade — and CorpusIQ supplies the commercial layer around it: procurement teams can pair a `grade_xref` lookup with CorpusIQ's QuickBooks connector to compare landed cost against the original grade, and distributors running ecommerce can attach the xref result to product records through the SHOPLINE or Amazon Seller connectors for listing descriptions.

## Limitations

- One tool only, one grade per call — no batch endpoint
- Comparability is by ISO application position, not interchangeability; test cuts still rule
- Brand-new listing (repo created Aug 18, 2026, MIT, zero stars)
- Coverage is bounded by manufacturer-published charts; niche or private-label grades may not resolve

## See Also

- [Opportunity Atlas MCP — Construction Opportunity Intelligence](/hermes/mcp/servers/external/opportunity-atlas-mcp/)
- [Dutch Vehicle Context — Dutch Vehicle Reports](/hermes/mcp/servers/external/dutch-vehicle-context/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
