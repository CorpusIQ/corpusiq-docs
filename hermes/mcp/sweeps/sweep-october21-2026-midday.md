---
title: "MCP Server Discovery - October 21, 2026 (Midday Sweep)"
description: "Midday delta cataloguing four business servers with guides and live probes: BOM pricing, live AIS, creator payouts and real participant research."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october21-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 21, 2026 (Midday Sweep)

Midday delta about seven hours after the night capture. The shape was the reverse of the night cycle: mcpservers.org `/all` pages 1 to 4 through the r.jina.ai reader proxy carried three of the four entries, the chatmcp/mcpso issue window carried the fourth, and the mcp.so `/feed` page 1 came back with the night cycle's cards plus almost nothing new. Every entry was settled by running the endpoint rather than by reading a listing.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Next Everything MCP](/hermes/mcp/servers/external/nexteverything-mcp/) | Manufacturing and Hardware | A bill of materials priced for a real build. Remote server at `https://mcp.nexteverything.io/mcp` with a bearer API key, and an unauthenticated `POST initialize` returned HTTP 401. Eight tools turn a CSV or TSV BOM into matched, priced, orderable lines against 630,000+ JLCPCB/LCSC parts refreshed daily with DigiKey and Mouser checked live per line, plus lifecycle warnings and JLCPCB extended-part fees. `check_bom` returns a per-distributor comparison, shipments and a `quote_id`; `update_bom_line` re-prices after a swap; `place_order` requests an order and charges nothing, with the team re-checking stock and emailing a payment link. Quotes are USD, valid 24 hours, duties excluded. Gap closed: the only bill-of-materials entry here belonged to a wire-harness diagram tool. |
| [AIS Trail MCP](/hermes/mcp/servers/external/aistrail-mcp/) | Compliance and Regulatory | Live and historical AIS. `https://api.aistrail.com/mcp`, stateless Streamable HTTP. Probed live: unauthenticated `POST initialize` returned HTTP 200 (serverInfo `aistrail-ais` 1.5.1) and `tools/list` returned 11 tools. Six work keyless (search, vessel, area, nearby, port find, data status), five read the archive with a key (track, vessel port calls, port calls, vessel events, sanctions lookup). Port call and event rows carry the sanctions list codes naming the ship's IMO. Positions are never interpolated, jumps are flagged, attribution travels with each answer, and private vessels are never listed individually. Free 500 credits a month, Starter $29, Pro $129 with live positions and a stream, Business $249. Gap named rather than closed: the class held container milestones and chokepoint intel, not what a specific ship is broadcasting now. |
| [ViewsBase MCP](/hermes/mcp/servers/external/viewsbase-mcp/) | Marketing | Creator payouts for clipping and UGC campaigns. `https://viewsbase.com/mcp`, OAuth 2.1 scoped per workspace with read-only as the default, submitted as issue #5881 under registry `io.github.funCapital/viewsbase`. Unauthenticated `POST initialize` returned HTTP 401. 29 tools: reads cover posts, views, creators, campaigns, payment requests and history; `get_payouts_summary` splits owed and final, ready to pay, blocked, details to check, held for a views spike and still counting. Eight writes cover CPM, finalisation, refresh, creators, offers and links. Money tools need payment rights and a viewer gets a 403; no tool returns emails or payout details. 120 requests and 30 writes a minute per connection, AI access on Growth and up. Gap closed: UGC tooling here was creative only, nothing reconciled views against the agreed deal. |
| [UXArmy MCP](/hermes/mcp/servers/external/uxarmy-mcp/) | Design and Product | User research that runs rather than reports. `https://app.uxarmy.com/mcp`, unauthenticated `POST initialize` returned HTTP 401; `uxarmy.com/mcp` is a 404 and `mcp.uxarmy.com` does not resolve. Reads search studies by description, extract themes, sentiment and quotes, flag studies below target and tasks nobody reached, return transcripts with speaker labels and timestamps in the original language, and open one participant down to device, task answers and replay. Acts recommend the method, build the survey or study, trim to a duration, set panel targeting by country, age and device, draft screeners, and launch only after the operator says so. Panel recruiting draws on separately bought credits; every plan including Free can invite its own participants. Gap named rather than closed: the existing entries simulate testing or read tests already run. |

## Surface Results

- mcp.so `/feed` page 1: 30 cards, mostly the night cycle's cohort. The unledgered cards resolved to 404 detail shells or to prior dispositions, and three feed cards (FERS, Zeptap, IQFluence) were carried from earlier cycles.
- mcpservers.org `/all` pages 1 to 4 through the reader proxy: 116 unique slugs. Eleven were genuinely unledgered and were read at detail level; four became entries and the rest were classed below.
- chatmcp/mcpso issue window: #5862 through #5887, with the #5841 and #5844 gap fills, read with bodies in one authenticated call.

## Held This Cycle

WebGlazer held against the saturated AI visibility class (geolint, LogNorm, CiteLadder, Cite42). SitePatent held as a directory of other people's tools. Cloudzyro and Lavela held as deployment and hosting infrastructure. AnimatedWebs and AIKIZI held as creative assets. TechFabric held as a developer docs utility. ProSignature held as a productivity utility with no data behind it. Agent Paywire held as the agent payments knowledge class. Underanchor held against the document and notes class. ShadowCursor held as agent infrastructure. ACTN held as the agent labour marketplace class. Indiax BookKaro and A1 Towing NYC held as regional and consumer. Pear carried its October 20 disposition.

Vendor fleets were not cherry-picked. The `openkrill` quintet lands in saturated classes already classed for that vendor (SEO, hiring signals, email verification, vulnerability scanning, tool aggregation). The `mambalabsdev` / `mambabuilt` quintet is a vendor already catalogued three times, with each angle covered elsewhere here. The fourteen-server `pooriaarab` burst was excluded whole under the single-author burst doctrine.

On the issue window, Buzzberg held against the dense filings and sentiment cohort, Murkuz SEO against a saturated SEO class and our own first-party connectors, PassTunnel, stackhint and Enni as developer and networking infrastructure, Ncrypt, Locul and PushNotif as memory, notification and sharing infrastructure, IZeat, PaletteGet, Tesla Wrap Designer and Velocity OSINT as consumer and creative utilities, and the two HasData submissions as scraping-vendor surfaces.

Five `/all` cards served a 404 shell through the proxy (Yuppsy, SnapDub, UnblockingAPI, HiveMindUnit llmintel, Shaangs Ventriloquist), which is the sitemap-fresh-but-not-live class and not a finding.

## Catalog Count

961 to 965 servers, 841 to 845 guides.
