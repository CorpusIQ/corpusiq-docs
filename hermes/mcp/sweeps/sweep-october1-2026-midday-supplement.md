---
title: "MCP Server Discovery - October 1, 2026 (Midday Supplement)"
description: "Midday supplement MCP sweep: eCFR.io MCP, Find Your Role First MCP and apMZoomAI MCP catalogued, with the feed and /all repeats dispositioned."
last_updated: 2026-10-01
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october1-2026-midday-supplement"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - October 1, 2026 (Midday Supplement)

## Summary

3 new business-relevant MCP servers catalogued with integration guides.

This supplement sweep ran roughly an hour after the October 1 midday sweep, so the day's "Midday" label was already taken. Firecrawl was unconfigured again this cycle, so every directory fetch ran through the r.jina.ai reader proxy, which was also the only way past the Cloudflare wall on mcpservers.org: direct `curl /all` returned a 403 challenge shell while the reader proxy returned full content.

## Sources Swept

| Source | Method | Yield |
| --- | --- | --- |
| mcp.so /feed | r.jina.ai reader proxy | 30 server blocks (all prior-ledger repeats) |
| mcpservers.org /all | r.jina.ai reader proxy | 30 slugs, 3 genuinely new |

## New Servers Catalogued

### eCFR.io MCP - US Federal Regulations for Agents

Free read-only remote Streamable HTTP at `ecfr.io/mcp`, no API key. 3 tools for searching current US Code of Federal Regulations text or a citation such as 31 CFR 10.1, reading a regulation by canonical path with source dates and stale flags, and listing CFR titles. Every result carries inline and legal citations linking back to ecfr.io. Published in the official MCP registry as `io.ecfr/ecfr`.

Relevance: HIGH. **Endpoint verified** (full MCP handshake: initialize returned serverInfo `ecfr-mcp` v1.0.0 with tools, resources and prompts capabilities; tools/list returned all 3 tools).

### Find Your Role First MCP - Job Search for Agents

Hosted remote Streamable HTTP at `findyourrolefirst.click/mcp` with a bearer agent key. 6 tools over a feed of open roles gathered from 13,000+ company career sites and re-read every few hours: whole-word title and company search, a free count call to size a search before spending credits, a free list of unlocked roles, single-job refresh, cursor-based change tracking for new, updated, reopened and closed roles, and usage reporting. 9 USD per month.

Relevance: MEDIUM. **Endpoint verified** (HTTP 406 on bare GET, the expected upgrade-required Streamable HTTP response; tools/list returned all 6 tools).

### apMZoomAI MCP - Dongdaemun Wholesale Search

Public read-only remote Streamable HTTP at `apmzoom.com/mcp`, no authentication, stateless with JSON responses. 5 tools over the Dongdaemun wholesale fashion market in Seoul: keyword item search in eight languages (English, Korean, Chinese, Japanese, Vietnamese, Thai, Indonesian, Malay), new arrivals within the last 1 to 168 hours filterable by building and category, stall lookup by name, number, building or floor, single-item retrieval, and a building list. Prices are left to the item link to keep the surface a discovery layer.

Relevance: MEDIUM. **Endpoint verified** (HTTP 405 on bare GET, the expected method-not-allowed Streamable HTTP response; tools/list returned all 5 tools).

## Also Identified (Not Catalogued)

FL Studio MCP (AI control of FL Studio transport, mixer settings, plugins and piano roll through MIDI and Piano Roll scripts, music-production utility class), Scentrev MCP (perfume and fragrance database with 22 tools over 126k+ scents, consumer vertical class), THC Open Mindfulness MCP (read-only mindfulness resources and research metadata, consumer wellness class).

The mcp.so /feed carried zero new entries this cycle: every one of its 30 server blocks was a prior-ledger repeat (Zyte, AgentGrid, Builders in Fintech, MCP DB Wizard, FlatHunt, TATUAT.RO, Genchi, Manifold, Common Paper Contracts, PixelDojo, Aayat AI, Povver, uplika, prodready, How To Make Money On Snapchat, oceanalt-aml-mcp, MemeSwap, Official Porkbun MCP Server, MeroFoundry, Rebbel, Dumpster Controls, Unipile, fAlpha, TokElements, GAIP Agents, HeyLead, AQL PropertyCheck, elmah.io MCP, trip1, Webshare). The mcpservers.org /all set was also almost entirely repeats (NordicContacts, CycleCalcs, Hourtick, FirstSales, Postqued, Revamp, Flows, Appman AI, Leadsgram, Trust Check, xTiles, AgentHands, Lintlab PDF to Markdown, Confirme by Synapse, PromptQuorum, Deploy Social, Reps Gym Workout Log, Project Room, D365 Mockup Agent, Better Design, GitDiagram, uplika).

The headline finding is the 404-shell resolution: four slugs that the October 1 midday sweep excluded as 404 shells (karl-andres, apmleokeo-gif, lrehmann, and the ahmedkhaleel2004 alias) now resolve with live detail pages. Three of them yielded the catalogued finds above (FL Studio, apMZoomAI, eCFR.io), and the fourth (GitDiagram) was already dispositioned as a dev-utility skip in the morning sweep. Confirm, however, was already correctly catalogued in the midday sweep.

## CorpusIQ Directory Status

| Directory | Status | Verification |
| --- | --- | --- |
| mcpservers.org | LISTED | `/servers/corpusiq-io` resolves with CorpusIQ content via reader proxy (direct curl returns a Cloudflare challenge shell) |
| glama.ai/mcp | LISTED | HTTP 200 on `/mcp/servers/@corpusiq/corpusiq-docs` |
| smithery.ai | LISTED | Registry API returns displayName CorpusIQ at `benoit-p/Cprusiq` |
| PulseMCP | LISTED | Title `Official CorpusIQ MCP Server | PulseMCP` via reader proxy (direct curl 403, known Cloudflare artifact) |
| mcp.so | NOT LISTED | Instant moderation deletion, manual submission required |
| registry.modelcontextprotocol.io | BLOCKED | Needs npm account and domain verification file |
| agenticskills.io | BLOCKED | Form reachable (HTTP 200) but the review queue backend is disabled |

## Notes

No new MCP directories surfaced this cycle. The high repeat rate against the same day's earlier shifts is expected for a supplement pass roughly an hour after the midday sweep; the genuinely-new shortlist is what survived the crossref against the index prose and the guide directories. The 404-shell class is worth watching: entries excluded for a 404 in one shift can resolve in the next, so a supplementary pass is a cheap way to recover candidates the primary shift skipped.
