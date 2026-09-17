---
title: "MCP Directory Sweep Report - Aug 27, 2026 (Morning)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-aug27-2026-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Directory Sweep Report - Aug 27, 2026 (Morning)

**Shift:** Morning cron sweep, ~10:00 UTC start
**Issue cutoff for next shift:** chatmcp/mcpso issue #3791 (Aug 27 08:31 UTC) - start the next shift's issue scan at #3792
**Sources:** chatmcp/mcpso issues #3787-#3791, mcp.so homepage (8 recentServers) + feed (30 slugs), mcpservers.org homepage (18 slugs)
**Pushed from:** Spark (working copy current, .last-sweep was 8h prior)

## Catalogued (1 new, 1 guide)

| Server | Issue | Relevance | Category | Endpoint | Verification |
|---|---|---|---|---|---|
| Golf Intelligence by Stracka | #3787 | ★★ | Data & Analytics | mcp.golfintelligence.com/mcp | LIVE probe: /health 200, initialize serverInfo golf v1.0.0 (protocol 2025-06-18), all 5 tools confirmed via tools/list. Client-credentials auth (X-GI-Client-ID + X-GI-Active-Token headers). Credit-metered: search free, lookups 1-3 credits with confirm_spend gate. Personal $49/50 credits, Starter $399/mo/10k credits. Repo golf-data/golf MIT 0 stars (created Aug 27 02:01 UTC). Registry io.github.golf-data/golf v1.0.0 |

Guide: golf-intelligence-mcp. Catalog counts: 386 -> 387 servers, 272 -> 273 guides.

Notable: the repo README says the production URL "may not be live" (deployment caveat), but the endpoint IS live - DNS resolves and both /health and initialize answered. Live probe is the ground truth over README caveats.

## Skipped (evaluated, not catalogued)

- SwarmIO #3788: hosted research swarm (agents write cited reports, USDC top-ups on Base) - agent infra class, no business data (ArcadeOps/Fomite precedent).
- Vifo #3789: AI travel journal written by the user's agent (34 tools, freemium $6.9/mo) - consumer app class.
- Oblique Markets #3790: x402-paid tool marketplace (market stats, provider lookup, catalog diffs, experiment scoreboard) - x402 infrastructure class, 402oracle precedent.
- Focuh #3791: personal ADHD task/calendar/goal system for coding agents - personal productivity class, no business counterparty.
- Feed/homepage catch-ups recorded for a future sweep: Katto (AI video clipping to scored captioned 9:16 shorts, mcp.so recentServers today but createdAt Dec 2024 - creator/media utility class, klo-mcp precedent), Graviti (agent trust index, paid verification, tamper-evident ledger at graviti.thesingulariti.ai - agent infra class), YouTube Transcript AI (keyless transcript fetch, createdAt Jul 31 - dev utility class).
- mcpservers.org homepage: all 18 slugs already evaluated (famous servers + night-sweep skip mappings: agentcloud-so, count-nanocorp, fastgpu-co, proxyloom, runbear).

## Notes

- Only 1 of the 5 fresh issues was catalogue-worthy; the other 4 mapped to established skip classes without detail fetches.
- Golf Intelligence is the first golf-domain entry in the catalog (the official registry already carries several golf servers: loopgolf tee times, PGA, disc golf, caddence UK club prices - none in our catalog yet; future catch-up candidates).
- Guide verification: title 54 chars, description 280 chars, zero em dashes, zero credential-guard patterns, See Also slugs all resolve.
- Push required one rebase (nightly ecosystem discovery pushed mid-run at ~08:07Z); edits survived cleanly, final hash 911ca208.
