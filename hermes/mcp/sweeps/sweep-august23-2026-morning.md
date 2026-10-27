---
title: "MCP Discovery Sweep - August 23, 2026 (Morning)"
date: 2026-08-23
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3701-#3703 (Aug 23 04:42-07:48 UTC), mcp.so homepage recentServers + feed, mcpservers.org homepage; 4 catalogued with guides (FluentEDI, Domain MCP, Kirah Local Services, Truth Bear GAUGE), 5 skipped"
last_updated: "2026-10-24"
---

# MCP Discovery Sweep - August 23, 2026 (Morning)

- **Cutoff:** overnight cron sweep evaluated chatmcp/mcpso issues through #3700 (Aug 22 22:34 UTC)
- **Fresh window:** chatmcp/mcpso issues #3701-#3703 (Aug 23 04:42-07:48 UTC), mcp.so homepage recentServers + feed, mcpservers.org homepage slugs
- **Result:** 4 catalogued with guides, 5 skipped

## Catalogued (4 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| FluentEDI MCP (hosted keyless X12 EDI toolkit: edi_parse/validate/build for 850/856/810/855/997, JSON repair, contract-drift, cron/time utilities; endpoint fluentedi.com/mcp, live-probed v1.0.0, 17 exposed tools with tool_call dispatcher, batch of 20 per round trip) | n/a (new listing, repo created Aug 23) | Commerce & E-Commerce | mcp.so GitHub issue #3701 |
| Domain MCP (Dynadot domain portfolio management: 108 API actions in 10 composite tools; npm domain-mcp v2.0.0, MIT, 12 stars, npx install with DYNADOT_API_KEY, sandbox mode) | 12 | Productivity | mcp.so GitHub issue #3703 |
| Kirah Local Services MCP (local services marketplace: business search, service catalogs with pricing/intake, live availability, create/reschedule/cancel bookings; kirah.ai/api/mcp live-probed kirah-agent-gateway v2.16, 10 tools, keyless) | n/a (new listing) | Business Operations | mcpservers.org homepage |
| Truth Bear GAUGE (official government data - SEC/FDA/USGS/NOAA signals - with cryptographic proof: free find_signal + verify_citation, paid records x402 pay-per-call in USDC on Base; api.truthbear.co/mcp live-probed v1.0.0, 3 tools) | 0 | Compliance | mcp.so homepage recentServers |

## Skipped (5)

- **Infyicon (#3702)** - 161,000+ free hand-drawn icons with SVG/PNG retrieval. Design assets, not business data (QR Planet class).
- **Context.dev** (mcp.so feed, Aug 21) - web-data infrastructure for AI products. Saturated web-scraping category, same class as rasterly skip.
- **DotLy ID** (mcpservers.org homepage) - biolink and domain-registration vendor. Endpoint mcp.dotly.id/mcp not probeable (HTTP error on initialize), thin niche surface, Registly class.
- **Hypnothera** (mcp.so homepage) - personalized hypnosis sessions from what the assistant knows about the user. Consumer wellness; Jul 17 listing (catch-up noise).
- Feed and homepage repeats already evaluated: Agent Conductor, CodeSentinel, QR Planet, RADAAR, My AskAI, Dados B3, SavePropTax, Xverum, Hermoso, Simplepages, DPF, Webz.io, ship.page, Upfirst.

## Notes

- All 4 catalogued servers were live-probed before guide writing (probe is ground truth for tool counts): FluentEDI exposed 17 tools vs 36 claimed in the issue (tool_call dispatcher covers the rest); Kirah returned all 10 tools on kirah-agent-gateway v2.16; Truth Bear returned 3 tools on truthbear-gauge v1.0.0 with free-tool + x402 paid-record model confirmed by the server's initialize instructions.
- FluentEDI repo (mastermanas805/fluentedi-mcp) is brand new: created Aug 23, 2026, 0 stars, no license declared in README - guide notes this for enterprise embedding caution.
- Domain MCP npm package verified published (v2.0.0, created Dec 5 2025) before cataloguing, per the npm-unpublished skip rule.
- Truth Bear is a catch-up (mcp.so listing Aug 14) that carried real business data - catalogued per the "catalogue regardless of age when it carries real business data" rule and the x402 business-data test (RE Data Refinery / SYNTHORA precedent).
- Catalog index updated: 321 to 325 servers (+207 to +211 guides).
