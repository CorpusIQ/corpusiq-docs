---
title: "MCP Directory Sweep Report - Aug 26, 2026 (Midday)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-aug26-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Directory Sweep Report - Aug 26, 2026 (Midday)

**Shift:** Midday cron sweep, 11:01 MST start
**Issue cutoff for next shift:** chatmcp/mcpso issue #3778 (Aug 26 17:59 UTC) - start the next shift's issue scan at #3779
**Sources:** chatmcp/mcpso issues #3758-#3778, mcpservers.org /all pages 1-3, mcp.so feed page 1 (browser, after web_extract 504 and curl shell)
**Pushed from:** Spark (fresher clone - Mac Mini sat at Aug 12 / 166 servers)

## Catalogued (6 new, 6 guides)

| Server | Issue | Relevance | Category | Endpoint | Verification |
|---|---|---|---|---|---|
| Nomos MCP | #3778 | ★★★ | Compliance | mcp.nomos.pro/mcp | HTTP 401 = auth gate live |
| Korea Ground-Truth | #3776 | ★★★ | Compliance | kr-groundtruth-mcp.vercel.app/api/mcp | INIT 200 stateless, serverInfo 0.1.0 |
| ScreenVerity | #3769 | ★★ | Compliance | stdio (npx screenverity-mcp) | n/a (stdio) |
| w0 MCP Server | #3758 | ★★★ | SEO | w0-mcp-server.modernai.workers.dev | HTTP 403 = Workers access layer live |
| UGC VZ | #3759 | ★★ | Content | ugc-vz.de/api/mcp | INIT 200 stateless, serverInfo 1.0.2 |
| iFillPDF | #3766 | ★★ | Content | mcp.ifillpdf.com/mcp | HTTP 401 = OAuth protected resource live |

Guides: nomos-mcp, korea-groundtruth-mcp, screenverity-mcp, w0-mcp, ugc-vz-mcp, ifillpdf-mcp.
Catalog counts: 375 -> 381 servers, 261 -> 267 guides.

## Skipped (evaluated, not catalogued)

- SocialDataX family #3770-#3775: six hosted read-only social-data wrappers filed in a 3-minute burst - commercial X-data reseller class (SocialData/TwitterAPIs precedent).
- Apple Mail MCP #3777: local macOS stdio, consumer utility class.
- AI Commander #3765: remote shell + detached jobs, dev infra class (SSH MCP Server precedent).
- Helena Good #3764: scientific sponsorship via Solana USDC, crypto/niche class.
- kbdb #3762: local file KB, dev tool class.
- Pīpīwai Trail #3761: park status, consumer niche.
- Vedaksha #3760: Vedic astrology, consumer class.
- BuyWhere #3767: resubmission of already-catalogued entry.
- /all pages 1-3: x402-payable family (Live Entity Verification, Public Tenders ES EU, Document Conversion API, Calibrated Similarity Search API, WebSocket Session Manager, Agent Verification API, ERC8004 Agent Liveness, New x402 Listings Feed, Onchain Activity Index, URL Metadata API, x402 Receipt Verifier), SoccerAPI (consumer sports), Walletwatch via loki-freedomlab slug (already evaluated night sweep), MCP Platform (REST-to-MCP gateway, agent infra class), Deep Art AI (consumer image gen).
- Feed page 1: all morning-sweep repeats (SocialRobot, Hologrow, MetricFire, OpenLore, Legion, fhirHydrant, Speccy, Jitsu, etc.).

## Notes

- web_extract on mcp.so/feed returned 504; curl returned a JS shell (0 __next_f chunks, no /server/ hrefs). Browser navigation worked and showed the feed page 1 - all entries were morning-sweep repeats. GitHub issues were the productive surface this shift, per the fresh-signal ordering (issues filed after the prior sweep cutoff).
- Public Tenders ES EU carries genuinely business-relevant data (TED procurement) but is x402-payable with thin docs - skipped per RE Data Refinery/Speccy x402 precedent. Revisit if the vendor publishes a free or OAuth tier.
- Nomos's GitHub repo (Nomos-Tech/nomos-mcp) is not yet public - guide notes this; registry name pro.nomos/nomos-mcp is the canonical identifier.
