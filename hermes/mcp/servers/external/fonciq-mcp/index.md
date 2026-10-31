---
title: "Fonciq MCP - Quebec Flood Zones and Land Registry"
description: "Quebec land data in chat: a free flood-zone lookup at a point, plus registry indexes, deeds and cadastral plans billed per document."
category: Property / Legal
stars: n/a (free flood lookup, paid documents)
added: 2026-10-31
source: "The chatmcp/mcpso submission issue #6509 filed 2026-10-31 at 16:01Z; a keyless initialize and tools list against https://api.fonciq.ca/v1/mcp returning HTTP 200 with serverInfo fonciq 1.0.0 and fourteen tools; one live flood_zones_lookup call at 45.4865, -73.8980 returning a matched source zone with licence and freshness stamps; and an HTTP read on the free API documentation page"
relevance: ★★
tags: [quebec, land-registry, flood-zones, cadastre, property-due-diligence, registre-foncier, real-estate, open-data, remote-mcp]
last_updated: "2026-10-31"
---

# Fonciq MCP

**Two facts decide a Quebec property: whether water reaches it and who owns it. One is free, answered on the first call, and the other is a registry document that arrives with a fee attached. This connector keeps the two separate and prices them honestly.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.fonciq.ca/v1/mcp
Auth:        none for flood_zones_lookup, own Fonciq key for the other 13 tools
Tools:       14 measured live
Cost:        flood lookup free; registry documents CAD 0.99 each, excluding registry fees
```

## What it does

Fourteen tools over Quebec land data, split cleanly between the free indicative layer and the paid registry layer.

The free one is the reason to read this entry:

- `flood_zones_lookup` checks which of nine open flood-zone sources intersect a point, an address or a lot, given exactly one of latitude and longitude, a civic address matched to the provincial address register, or a lot number. It returns the zones found, the source zone type, the distance to the nearest zone, the CC BY 4.0 attribution per source and a disclaimer.

The registry side needs the caller's own key and is billed like the HTTP API it wraps:

- `lot_resolve` turns a Quebec address or an assessment-roll matricule into lot numbers and cadastre, `lot_get` returns a stored lot profile with the assessment-roll value in cents, and `registre_index_request` queues an index of immovables for one lot.
- `acte_get` returns the PDF of one deed by registration number and registration division, `plan_get` returns the cadastral plan of a lot, and `document_get` and `document_entries` read back an index or deed already produced for the organization.
- `batch_submit` queues an index for up to **500 lots** across the active registry accounts, `job_get` and `job_results` track the job and return parsed index lines, `watch_create` schedules a weekly or daily re-check of a lot's index against a baseline snapshot with a webhook, and `billing_get` and `billing_usage` price the period.

Only documents are billed, at **CAD 0.99** each and excluding registry fees: index, deed, plan. Lot reads, job reads and watch creation cost nothing, and test keys cost nothing.

## What this pass measured

`initialize` answered **HTTP 200** with `serverInfo` naming `fonciq` at **1.0.0**, and `tools/list` returned all **fourteen** tools with their schemas, so the surface is measured rather than quoted. The server's own instruction string states the pricing and the limits before any call: flood lookup is free at **30 requests per minute and 1,000 per day per IP**, the other tools use the caller's key, and the flood answers are indicative only.

One call was made, `flood_zones_lookup` at 45.4865, -73.8980, a point inside Montreal. It returned **HTTP 200** in 0.26 seconds with `any_zone_found: true`, the label "Zone trouvée à ce point", an exact coordinate match, and one matched source: the Ville de Montreal index of flood plains, published by the City of Montreal as a **reference layer**, with the dataset URL at donnees.montreal.ca, licence **CC-BY-4.0**, `mapping_generation: reference`, `historical: false`. The response also carried freshness stamps for the sources, the oldest checked at 13:44:31Z and the newest at 13:48:53Z on 2026-10-31, an attribution block naming BDZI, the MRNF presence grid and the 2017-2019 historical layer, and a `limits` block repeating 30 per minute, 1,000 per day, `key_required: false`.

A single hit on a reference layer is a weaker answer than a regulatory zone, and the response says so in its own vocabulary: the point was classified `a_verifier`, French for to be verified, described as an indicative Fonciq classification.

## The sentence that makes this usable

Most geo layers answer a question they were not asked and let the reader assume the rest. This one refuses three assumptions in the payload itself:

- A point is not a lot. The note states that the lot boundary is not evaluated, because the answer covers coordinates or an address point, and an address point often sits on the street side, so a lot can touch a zone even when its address point does not.
- No result is not a clean bill. The coverage note states that no zone found at a point never means the property is outside a flood zone, because only the nine listed open sources are consulted.
- Old maps are old. Since 1 March 2026 a new-generation mapping replaces the old one sector by sector, and it is not included, so every answer carries the official Quebec interactive map and the verification page for the government's own lookup.

That is the shape a compliance answer has to have. The tool that says what it cannot see is the one an agent can quote in a due diligence file.

## The operator decision this answers

For a business buying, leasing or insuring property in Quebec, the flood question arrives early and is answered late, usually by a municipal phone call. A free, dated, attributable answer at an address is a screening step that costs nothing and closes the obvious cases before a professional is paid.

The registry side is the expensive half, and it is priced accordingly: **0.99 Canadian dollars per document**, with registry fees on top and lot reads free. For an operator screening twenty sites, the free pass narrows the list and the documents only get bought for the shortlist. The batch tool, up to 500 lots, is what makes a portfolio review possible at all.

## Where it sits in this catalogue

This is the third land surface here, and the geography is the difference. [UK Land Registry MCP](/hermes/mcp/servers/external/uk-land-registry-mcp/) sells England and Wales sold-price packs, [Hercules MCP](/hermes/mcp/servers/external/hercules-property-mcp/) reads US property records and owner leads, and this one is Quebec, where the property regime, the language and the registry itself are different from both.

The free flood lookup has no equivalent in either: a point-level, licence-stamped, dated answer across nine open provincial sources.

## What this pass did not establish

Only the free tool was called. The thirteen registry tools, their output shapes and the per-document billing are the vendor's published surface, and the only evidence for the **0.99** dollar price is the instruction string and the submission text. The nine flood sources were not enumerated beyond the one that matched, so coverage outside the Montreal area is untested. Whether a batch of 500 lots is billed per lot or per job, and whether a watch re-check re-bills the index it compares against, are the two cost questions a trial should settle first. The `fq_test_` key path was not exercised.

## FAQ

### Can I use it without an account or a key?
For the flood lookup, yes. `initialize`, `tools/list` and a real `flood_zones_lookup` all answered without credentials, at 30 requests per minute and 1,000 per day per IP. Everything else needs your own Fonciq key in the Authorization header.

### What does it cost?
The free layer costs nothing. Registry documents are billed per document at 0.99 Canadian dollars each, index, deed or plan, excluding the registry fees themselves. Lot reads, job reads and watch creation are not billed, and test keys are free.

### Is a flood answer a determination?
No, and the payload says so in three places. It is indicative, drawn from nine open sources of old-generation and reference mapping, the lot boundary is not evaluated, and a negative result never means the property is outside a zone. The response links to the official provincial map to confirm.

### Does it work outside Quebec?
No. The corpus is the Quebec land regime: the cadastre, the Registre foncier, the assessment roll and the provincial address register, with municipal and MRC flood mapping.

### Can an agent buy documents without limit?
That depends on the Fonciq key it holds, and the catalogue position is that spending keys should be scoped and reviewed, since a tool that returns a PDF at 0.99 dollars per pull is a metered action rather than a read. Billing tools are in the surface, which is the right place to start an agent's month.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [UK Land Registry MCP - Sold Price Packs for Agents](/hermes/mcp/servers/external/uk-land-registry-mcp/) - the same registry question in another jurisdiction
- [Hercules MCP - US Property Records and Investor Leads](/hermes/mcp/servers/external/hercules-property-mcp/) - US property records
- [den MCP - Korean AEC Standards with Clause References](/hermes/mcp/servers/external/den-archi-mcp/) - building rules cited to the clause, another jurisdiction
