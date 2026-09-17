---
title: "Sweep Report - August 29, 2026 Morning Cron Sweep"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august29-2026-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 29, 2026 Morning Cron Sweep

**Date:** 2026-08-29 (~03:00 MST)
**Sources:** chatmcp/mcpso issues #3811-#3816 (fresh window after night sweep's #3810 cutoff), mcp.so homepage + feed, mcpservers.org homepage + /all pages 1-3
**Outcome:** 8 new servers catalogued with guides

## Catalogued (8 guides)

| Server | Source | Endpoint | Verification | Relevance |
|---|---|---|---|---|
| YG3 MCP | mcp.so issue #3811 | https://mcp.yg3.ai/mcp | /api/health live (197 tools, v0.2.0); anon initialize 401 | ★★★ Marketing |
| GrowSurf MCP | mcpservers.org /all p1 | https://mcp.growsurf.com (hosted) + npm | npm @growsurfteam/growsurf-mcp published; official vendor org | ★★★ Marketing |
| site-spec | mcpservers.org /all p1 | stdio npx site-spec-mcp | npm published, llms.txt documents all 4 tools | ★★★ SEO |
| CN Intel Board | mcp.so issue #3814 | https://cn-intel-mcp.lory69060.workers.dev/mcp | 401 Unauthorized = live (bearer auth) | ★★ Data & Analytics |
| Contexter | mcp.so issue #3812 | https://contexterai.com/mcp | 401 unauthorized = live (OAuth DCR) | ★★ Productivity |
| NoClick | mcp.so issue #3816 | https://api.noclick.io/mcp | 401 Bearer token required = live; 47 tools from docs | ★★ Productivity |
| PairBook | mcpservers.org /all p1 | stdio npx pairbook-mcp | npm 1.3.0; keyless API documented | ★★ Finance |
| Otto | mcpservers.org /all p1 | https://otto.islaintel.com/api/mcp | 401 missing_authorization = live | ★★ Marketing |

## Also identified (not catalogued)

- dataloupe #3813: offline stdio explorer for local CSV/Parquet/Excel - local data-file utility class, redundant with existing local tooling.
- thing #3815: durable artifact publishing for coding agents - dev publishing utility class (Booklet precedent: versioned links and comments, no measurable readership).
- /all catch-up skips: YardStock (NZ dealer used-car inventory, micro geo-niche), SafeSelect (Postgres/MongoDB read access for coding agents, dev tool), Domain Search King (RDAP .com availability, thin utility), TooHardBasket (escrow agent task marketplace, TaskMarket class), Blck Alpaca Knowledge Base (vendor marketing KB prose), Savee (design bookmarking, consumer creative), PersonaCLI (local personal workspace, consumer productivity), MCP Marketplace (server search directory, agent infra), search2chart (charting dev utility), Lyrenth (web extraction, saturated scraping class), AgentMailkit (local email digests, personal utility), Session Bridge (browser automation, dev automation), Maroo and Kalyvox (no repo or description), consumer/crypto repeats (YNAB, Pi Delegate, Parlay, OpenEphemeris, Bilibili, Zhihu).
- Future catch-up candidates: HasData batch (Airbnb, Booking, Zillow MCPs), SocialDataX batch.

## Actions Taken

- 8 integration guides written to hermes/mcp/servers/external/<slug>/index.md, validated (YAML, title/description lengths, em-dash scan, credential-guard scan, See Also dir + label checks).
- index.md patched atomically: last-updated line, new top sweep section, 8 docs-links tail entries.
- Report file written, .last-sweep stamped, committed and pushed to main.
