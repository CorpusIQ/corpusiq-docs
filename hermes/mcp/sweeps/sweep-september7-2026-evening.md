---
title: "MCP Server Discovery - September 7, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so feed (30 server blocks) and mcpservers.org /all page 1 via the r.jina.ai reader proxy. 5 new business-relevant servers catalogued with guides across sales intelligence, German e-invoicing, human judgment markets, video pipeline and GDPR form classes."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-07
---

# MCP Server Discovery - September 7, 2026 (Evening Sweep)

**Source:** mcp.so feed (30 server blocks, TanStack Router $R-stream), mcpservers.org /all page 1 (r.jina.ai reader proxy; direct curl Cloudflare-challenged)
**Method:** feed $R-block parsing (Pattern C), /all page 1 slug extraction, detail-page fetches via r.jina.ai, keyless JSON-RPC tools/list probes (fundz, rechnungslotse, countersignatory), OAuth-gated liveness probe (treza 401), vendor MCP docs (formdall.de/mcp)
**Date:** September 7, 2026 ~19:00-20:30 MST (Sep 8 ~02:00-03:30 UTC)

## Summary

| Metric | Count |
|---|---|
| mcp.so feed fresh blocks | 6 (1 already catalogued - Fruit Stand - 5 evaluated) |
| mcpservers.org /all page 1 | 30 entries (all classified) |
| Detail pages fetched | 9 (7 r.jina.ai, 2 vendor docs pages) |
| Endpoints probed | 4 (3 keyless with captured tool lists, 1 OAuth 401 liveness) |
| New servers catalogued | 5 |
| Integration guides written | 5 |
| Skipped (not catalogued) | 22 classes/families plus 3 prior dispositions |

## New Business-Relevant Servers (5 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| Fundz Agent API | fundz-agent-api | Sales trigger intelligence (SEC filings) | Keyless tools/list probe captured events_for_icp + predicted_next schemas |
| Rechnungslotse MCP | rechnungslotse-mcp | German e-invoicing (XRechnung/ZUGFeRD) | Keyless tools/list probe; 7 free tools with readOnlyHint annotations |
| Countersignatory | countersignatory-mcp | Human judgment spot markets | No-auth SSE tools/list probe captured full quote schema |
| Treza MCP | treza-mcp | AI video pipelines to social channels | 401 on keyless tools/list = live OAuth-gated endpoint |
| Formdall MCP | formdall-mcp | GDPR form backend (DSGVO) | Vendor docs: endpoint, OAuth flow, 10 tools, rate limits |

## Skipped (not catalogued)

- Datapika family (4 slugs: Meta Ad Library, Jobs, Trustpilot Reviews, Reddit scraper) - pay-per-call scraping family, fetcher.sh/Cracked precedent; the Meta Ad Library member is the most operator-relevant of the family
- Advisors AI readiness check - services agency page (audit pricing packages), no MCP endpoint or tool list
- GoBuy Product Trust - thin listing: 2 consumer shopping tools, broken config block, no verified tool list
- dxpert UNS tools - industrial IoT namespace validation (Sparkplug B/UNS), industrial niche
- Tessryx - app-builder dev platform (Huxly precedent)
- mcp-memorybank, Memra - agent memory infra class (Memwyre/Facthouse precedent)
- Sorify - agent QA platform (dev class); SnipperApp - macOS snippet manager (dev utility); Convert3D (3D conversion dev utility); Capacitor MCP + Capawesome MCP (docs/dev infra); figma-mcp-bridge (design tool class); Rendi FFmpeg API (thin vendor surface); Ergonia Works (agent task marketplace infra); MCP ADMIN MCP (MCP admin infra)
- BagIQ (disc golf), TrainBud (Garmin fitness), Wellness Project (health aggregator), FrameThrower (film stills), Carpedia (Brazilian vehicle catalog), Export Poe Chats (consumer utility), Zoteus (academic Zotero reference manager)
- Prior dispositions on page 1: marketcode-ai, personalknowhow, fr-legal-kit (CF 1042 premature listing)
- Feed repeats already catalogued (Fruit Stand Fund Returns - Aug 25 night) or disposed by the midday/day/night sweeps (create-prints and the post-boundary block)

## Actions Taken

- 5 guides written to hermes/mcp/servers/external/<slug>/index.md
- Index updated: last-updated line (585 servers, +471 guides), top evening sweep section, tail block entry
- `.last-sweep` stamped (hermes/mcp/.last-sweep)
- validate-guides.py 5/5 PASS expected; See Also targets verified by dir existence
