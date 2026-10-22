---
title: "CNC Compass MCP - Sourcing Suppliers From a Brief"
description: "Describe a machined part and get matching CNC suppliers with match reasons and quoted source evidence, over a keyless MCP server with three tools."
category: "Manufacturing & Industrial"
stars: n/a (hosted record, no public repo)
added: 2026-10-22
source: "chatmcp/mcpso issue #5925 (CNC Compass, October 22, 2026 midday sweep)"
relevance: ★★
tags: [sourcing, manufacturing, cnc-machining, suppliers, procurement, china-suppliers, remote-mcp, keyless]
---

# CNC Compass MCP

**Sourcing a machined part starts with a search that returns brochures and ends with a supplier you have to verify by hand. CNC Compass returns the supplier records instead, each with match reasons and the sentence from the source page that supports every field.**

```
Server type: Remote (Streamable HTTP), no key
Endpoint: https://cnccompass.com/mcp
Auth: none for the MCP tools; anonymous API callers share a per-IP quota
Live check: keyless POST initialize returned HTTP 200 (serverInfo CNC Compass 1.30.0, protocol 2025-03-26, tools, prompts and resources capabilities)
Tools: 3 from tools/list (search_suppliers, get_supplier, list_facets)
Index: 507 published supplier records declaring CNC milling, aluminum or anodizing; 472 declare CNC milling, 317 CNC turning, 226 sheet metal fabrication, 160 grinding, 99 five-axis, 91 EDM
Built by: CNC Compass (cnccompass.com)
```

## Why This Matters for Operators

The catalog already carries manufacturing knowledge and supplier price drift. What it did not carry is the first step: turning a sourcing brief into a shortlist that can be checked line by line.

CNC Compass does that in a way that is unusually honest about evidence. A record is marked Verified only after a person reviewed it, only reviewed records are indexable and in the sitemap, and the site states plainly that a supplier field is a claim from the cited source rather than a guarantee of capability. Each supplier row carries the quote that supports the match, so a buyer can go straight to the source page and check the claim instead of trusting a score.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_suppliers` | Takes a natural-language sourcing brief and returns a normalized brief, the fields it could not fill, a follow-up question, and matching supplier records with scores, match reasons, matched fields and evidence quotes |
| `get_supplier` | Returns one published supplier record in full by slug: identity, location, capabilities, certificates and the source of each field |
| `list_facets` | Lists the values the search can filter on with how many published suppliers declare each |

## Live Check

Called `search_suppliers` with "aluminum CNC machining with anodizing, medium volume". It returned a parsed brief (material Aluminum, process CNC milling, finish Anodizing), an explicit `missing: ["quantity"]`, a follow-up question about supplier location, and supplier rows carrying score, the three match reasons, a verified-source-factory flag, the marketplace profile URL, an inquiry URL, and the evidence quote from the supplier's own page. The stated count behind the answer was 507 records.

Then `list_facets` with `field=process` returned the real distribution rather than a rounded claim: 472 CNC milling, 317 CNC turning, 226 sheet metal fabrication, 160 grinding, 99 five-axis, 91 EDM, 66 3D printing, 17 Swiss machining.

## Installation

```json
{
  "mcpServers": {
    "cnc-compass": {
      "type": "http",
      "url": "https://cnccompass.com/mcp"
    }
  }
}
```

A JSON search API also exists at `https://cnccompass.com/api/search` (GET `?q=` or POST) and an OpenAPI description is published, so the same query works outside an MCP client.

## Limits Worth Knowing

- The corpus is Chinese machining suppliers, largely sourced from public company pages and marketplace listings. That is deep for that market and nothing else: a buyer sourcing in Europe or Mexico gets no coverage.
- 507 records is a curated index, not a market census. Absence of a supplier says nothing about that supplier.
- The search returns partial briefs on purpose and asks for what is missing. A quantity or tolerance the brief did not state shows up as a follow-up question, not as an assumption.
- Anonymous access is rate-limited per IP, and the site publishes a machine-access manifest rather than a price list, so heavy programmatic use should start from the published limits rather than discovering them.
- Records state capability claims, not capacity, lead time or price. The inquiry path is a marketplace form, and everything after the shortlist is ordinary sourcing work.

## FAQ

### Is a Verified record a quality guarantee?
No. Verified means a person reviewed the record and only those records are indexed and listed in the sitemap. Every field is still a claim from the cited source, which is why the record ships the quote alongside the value.

### Can it search by material or process directly?
Yes. `list_facets` returns the filter values and their record counts, and `search_suppliers` accepts material, process, finish and similar fields alongside the free-text query, so a structured filter and a brief can be combined.

### Why catalogue this when MechanoFab covers manufacturing?
MechanoFab answers how a process works. This answers who can make the part, with a record per supplier and a quote per field. Knowledge and sourcing are different steps in the same job, and the catalog had the first without the second.

## See Also

- [MechanoFab MCP - Manufacturing Knowledge for Agents](/hermes/mcp/servers/external/mechanofab-mcp/)
- [PayloadPier MCP - Supplier Price Drift for Purchasing](/hermes/mcp/servers/external/payloadpier-mcp/)
