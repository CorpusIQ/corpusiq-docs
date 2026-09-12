---
title: "MCP Server Discovery - September 12, 2026 (Midday Sweep)"
description: "Midday sweep over the mcp.so feed (30 server blocks), mcpservers.org /all page 1 via the r.jina.ai reader proxy (26 slugs batch-classified) and chatmcp/mcpso issues #4083-#4085. 3 new business-relevant servers catalogued with guides: B2B Creators MCP (multi-profile LinkedIn content operations), CraftStory MCP (talking-avatar and UGC video generation) and InstantReply MCP (Instagram, WhatsApp and Messenger inbox with 29 tools)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-12
---

# MCP Server Discovery - September 12, 2026 (Midday Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged at 403), chatmcp/mcpso issues #4083-#4085
**Method:** feed $R-block parsing, /all slug extraction, issue-body classification, npm registry + GitHub API verification, JSON-RPC liveness probe (initialize)
**Date:** September 12, 2026 ~10:00-11:00 MST (17:00-18:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so) |
| /all slugs batch-classified | 26 (page 1, r.jina.ai) |
| GitHub issues reviewed | 3 (#4083-#4085) |
| Detail pages fetched | 5 |
| Endpoints live-probed | 1 (B2B Creators - 401 auth gate) |
| npm/GitHub artifacts verified | 2 (CraftStory, InstantReply) |
| New business-relevant servers | 3 |
| Integration guides written | 3 |

## Core Listing Re-checks

| Directory | Status | Evidence |
|---|---|---|
| mcpservers.org | LISTED | r.jina.ai proxy on /servers/corpusiq-io - HTTP 200, title "CorpusIQ MCP Server | Awesome MCP Servers", 40+ connectors copy (direct curl CF-challenged 403, walled not removed) |
| glama.ai | LISTED | HTTP 200 on /mcp/servers/@corpusiq/corpusiq-docs |
| smithery.ai | LISTED | registry API ?q=corpusiq - displayName CorpusIQ at benoit-p/Cprusiq, unlisted=false; direct slug 200 with 9 corpusiq mentions (no flap) |
| mcp.so | NOT LISTED | SSR search payload - query echo only (2 occurrences, both query/lastMatchId); no corpusiq server object in the results array; quarantine holds (~51st cycle), no resubmit |
| PulseMCP | LISTED | r.jina.ai proxy - title "Official CorpusIQ MCP Server | PulseMCP" |

## New Business-Relevant Servers

| Server | Category | Why it matters | Endpoint |
|---|---|---|---|
| B2B Creators MCP | Social Media Management | LinkedIn content layer for outbound teams - plan, approve and publish across every personal profile (5-500 people), client approval links, per-profile + company page + LinkedIn Ads reporting, Canva import | https://mcp.b2b-creators.com/mcp (401 auth gate, Streamable HTTP; first 2 profiles free) |
| CraftStory MCP | Content | Talking-avatar and UGC video generation - photo to lip-synced video (CraftStory 2.0, up to 30 min) or 5-15 s clips (MiniMax H3); 10 tools, 180+ voices, cost preview, bounded job polling | npm @craftstory/mcp v0.1.3 (stdio; api.craftstory.com; MIT repo) |
| InstantReply MCP | Communication | Instagram / WhatsApp / Messenger inbox for agents - 29 annotated tools (conversations, contacts, WhatsApp template lifecycle, journeys, delivery debugging), 11 prompts, scope-mapped keys | npm @instantreply.co/mcp v0.2.0 (stdio; MIT repo) |

## Skipped (Not Catalogued)

- RecipeBee MCP (#4084): recipe search, previews and meal plans - consumer food class.
- MutalaaMCP (#4085): Turkish legislation, court decisions and Constitutional Court rulings - geo-niche legal class (LEGAION/Qotien precedent).
- Prior-sweep dispositions respected across the feed and /all repeats: SlateVM, MatPlotLibNet, failecho, loudreader, EU AI Act Compliance #4081, Errand #4082, requisition-audit #4080 - all disposed in the Sep 12 morning sweep; /all page-1 author shells (jpol34, mokhtarabadi, renezander030, vasilicasijarvis, wgd5678, wlsdks, xkqg, 15998194110) and feed repeats from the Sep 11 sweeps.

## Actions Taken

1. Wrote 3 integration guides (b2b-creators-mcp, craftstory-mcp, instantreply-mcp) following the recordwire/pixelesq guide shape; all 3 PASS validate-guides.py on the first pass.
2. Live-probed the B2B Creators endpoint over JSON-RPC initialize: HTTP 401 `{"error":"unauthorized"}` - endpoint live and auth-gated (the listing FAQ's no-auth claim is wrong; probe takes precedence).
3. Verified npm packages (@craftstory/mcp v0.1.3, @instantreply.co/mcp v0.2.0) and both source repos (MIT, pushed 2026-09-12).
4. Updated catalog index.md (last-updated line, frontmatter, top sweep section, docs-links tail block). Catalog now 651 servers (+537 guides).
5. Stamped .last-sweep and committed the sweep to corpusiq-docs main.
