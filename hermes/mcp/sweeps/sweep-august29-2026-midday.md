---
title: "Sweep Report - August 29, 2026 (Midday Cron Sweep)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august29-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 29, 2026 (Midday Cron Sweep)

**Run:** ~11:01 MST / 18:01 UTC, Saturday August 29, 2026
**Fresh window:** chatmcp/mcpso issues #3817-#3826 (after morning sweep's #3816 cutoff)
**Surfaces scanned:** GitHub issues (8 fresh), mcp.so feed (30 slugs), mcpservers.org /all pages 1-3 (90 slugs)
**Result:** 13 new business-relevant servers catalogued with guides; 28 evaluated and skipped
**Counts:** 417 → 430 servers (+13); 303 → 316 guides (+13)

## Catalogued (13)

| Server | Source | Category | Verification |
|---|---|---|---|
| Israel Business Intelligence MCP | issue #3826 | Business Intelligence | live-probed, 3 tools, x402 0.05 USDC/verify |
| Sourcey | issue #3823 | Business Operations | live-probed, 8 tools, keyless |
| ISO 20022 Generator | issue #3821 | Finance | 401-live, 4 documented tools |
| Equibles | /all p3 | Finance | 202-star repo, 61 tools, AGPL |
| Insourcia | /all p2 | Business Intelligence | hosted, OAuth/API-key, French company data |
| Apple Ads MCP | /all p3 | Marketing | 24 tools, Go binary, receipt-gated writes |
| Google Search Console MCP (ni-c) | issue #3824 | Marketing/SEO | 21 tools, npm, 3-API write-side setup |
| CRM Solid | /all p3 | Social Media | 13 tools, npm, 12 networks |
| Cookie Free Analytics MCP | /all p2 | Analytics | OAuth 2.1 PKCE, read-only, EU-hosted |
| healthchecks-mcp | issue #3822 | Business Operations | 14 tools, npm, get_ping_body |
| PolicyForge | /all p1 | Compliance | 11 tools, free unlimited audits |
| PreVibe | /all p3 | Business Operations | Google OAuth, SaaS research |
| AngelOne MCP | /all p2 | Finance | 32 tools, SmartAPI, Apache-2.0 |

## Skipped (28)

- Issues: Humanizer PRO #3817 (content-manipulation), ntfy-mcp #3819 (dev infra), woodpecker-ci-mcp #3820 (dev tool), Orphograph #3825 (agent provenance infra)
- /all: MarketMaster (gambling), Oblique Markets (x402 infra), Metalend (DeFi niche), Tillpad (agent infra), WonderCal (agent infra), Quartermaster (game assets), Valmera (native-creator video), Footix (gambling), IronShard (object storage), Hexum (dev tool), Kivgraph (dev tool), Firekeep (agent infra), Fatenava (astrology), OpenBoss (game), SuggestAPI (thin docs), APISelf (dev tool), Sirveil (consumer privacy), BidSwarm (rank bidding), Strunk (Booklet class), OctoWatch DLP (thin MCP docs), PilotMyX (thin docs), Peon/ConnectPeon (thin docs), CSVBox (thin MCP docs, /mcp 405)
- Feed: AdaptlyPost (no directory page, thin)
- /all: devinchen2014 x-twitter-mcp + weibo-mcp (consumer social scrapers)

## Notes

- Same-name different-vendor: GSC (ni-c) catalogued alongside yusofansari's read-only GSC server; distinct slug google-search-console-ni-c-mcp, differentiated on write-side setup (Site Verification + Indexing APIs).
- HasData family pages (google-maps, flights, trends, search, etc.) already disposed in prior sweeps.
- YNAB MCP and PersonaCLI were previously skip-prosed (July 27 evening, Aug 29 morning respectively) - not re-evaluated.
- Insourcia and PreVibe Tools tables are capability-level with caveat lines (anonymous enumeration not published); PolicyForge/Equibles/Apple Ads/GSC/CRM Solid/healthchecks/AngelOne tool names from vendor docs.
