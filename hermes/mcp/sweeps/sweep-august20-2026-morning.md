---
title: "MCP Discovery Sweep — August 20, 2026 (Morning)"
date: 2026-08-20
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso GitHub issues filed Aug 20 02:00 through 09:46 UTC plus mcp.so and mcpservers.org homepages; 3 catalogued with guides, 1 skipped"
---

# MCP Discovery Sweep — August 20, 2026 (Morning)

- **Cutoff:** prior sweep evaluated through issue #3653 (Aug 20 01:16 UTC)
- **Fresh window:** issues #3654–#3655, mcp.so homepage arrivals, mcpservers.org homepage slugs
- **Result:** 3 catalogued with guides, 1 skipped

## Catalogued (3 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Leadgen MCP (Romanian official ONRC registry — 4.2M+ firms, director/legal-representative search, website contact extraction, WHOIS/DNS/SPF-DMARC audits; remote at hermes.adrianhomelab.com/mcp, no auth validation phase; registry io.github.darksider4all/leadgen-mcp v1.0.0) | 0 | Lead Generation & Web Scraping | GH issue #3654 |
| tube-bridge MCP (self-hosted YouTube research: 17 tools, 14 keyless — search, transcripts, comments, playlists, ephemeral frames, local semantic corpora via SQLite+sqlite-vec+fastembed; PyPI v1.1.6, Docker, self-host HTTP option) | 0 | Content & Research | GH issue #3655 |
| Xverum MCP (hosted people search across 750M licensed professional profiles: plain-English search + full profile pull + Next Move Signal job-change prediction; x-api-key auth, OAuth in progress; registry com.xverum/mcp) | 0 | Sales & Outreach | mcp.so homepage arrival |

## Verification performed

- Leadgen: live JSON-RPC initialize + tools/list probe — serverInfo `leadgen`, session ID issued, all 4 tools enumerated with descriptions (lookup_business, lookup_director, extract_contacts, lookup_domain)
- tube-bridge: repo live (MIT, created Aug 7), README parsed from `master` branch for the 17-tool table, PyPI v1.1.6 published
- Xverum: repo live (MIT, created Aug 17, pushed Aug 20 — active), README parsed for tools + auth model, mcp.so detail page confirms 750M-profile positioning

## Skipped (evaluated, consistent with prior decisions)

- Vital Care Finder MCP (mcpservers.org homepage slug) — consumer doctor/dentist/nurse appointment booking; consistent with the MindMap AI consumer-niche skip

## Catalog state

- Before: 277 servers, 167 guides
- After: 280 servers, 170 guides
- CI frontmatter gate: 3,220 files scanned, all valid
- Next sweep cutoff: issue #3655
