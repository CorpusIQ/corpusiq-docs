---
title: "MCP Directory Sweep Report - Aug 27, 2026 (Evening)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-aug27-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Directory Sweep Report - Aug 27, 2026 (Evening)

**Shift:** Evening cron sweep, ~18:00 UTC start
**Issue cutoff for next shift:** chatmcp/mcpso issue #3793 (Aug 27 15:47 UTC) - start the next shift's issue scan at #3794
**Sources:** chatmcp/mcpso issues #3792-#3793, mcp.so homepage (8 recentServers) + feed (30 slugs), mcpservers.org homepage (18 slugs)
**Pushed from:** Spark (working copy current; .last-sweep was 10:08 UTC this morning)

## Catalogued (3 new, 3 guides)

| Server | Issue | Relevance | Category | Endpoint | Verification |
|---|---|---|---|---|---|
| TubeScout | #3792 | ★★ | Content & Research | local stdio (`npx -y tubescout`) | npm tubescout v0.1.1 published Aug 27; repo not0lucky/tubescout MIT, 0 stars; 6 tools + 6 skills documented in README; keyless (InnerTube) |
| DrillerDB | #3793 | ★★★ | ERP | https://mcp.drillerdb.com | INIT 401 `{"error":"missing_token"}` = live OAuth gate; 45 tools (37 read + 8 write) enumerated in README; official registry com.drillerdb/drillerdb v1.0.0 active (published Aug 27 15:46 UTC); repo CraigVG/drillerdb-mcp MIT docs |
| BidSkim | feed (bidskim-uk-tenders-contract-renewals) | ★★★ | Compliance | https://mcp.bidskim.com/mcp | INIT 401 with full auth instructions (OAuth 2.1 or x-api-key header) = live; 8 read-only tools with exact names from README; repo 23shim/bidskim-mcp docs-only; registry com.bidskim/mcp |

Guides: tubescout-mcp, drillerdb-mcp, bidskim-mcp. Catalog counts: 387 -> 390 servers, 273 -> 276 guides.

## Skipped (evaluated, not catalogued)

- Foremerge (mcp.so feed + recentServers, stars=50, repo naw103/foremerge Apache-2.0): open-source coordination protocol for coding agents built above Git (Rust CLI + MCP, "catch intent conflicts before code conflicts") - dev tool class, kbdb and AI Commander precedent, no business counterparty.
- OrbitWan (mcp.so feed, orbitwan-io): Wanchain blockchain explorer (address, transaction, block, validator search) - crypto/niche class; zero MCP mentions on orbitwan.io, thin vendor surface.
- Feed/homepage repeats already evaluated in Aug 24-27 sweeps: Katto, Uwear.ai, OmniSocials, Graviti, Speccy x402, Jitsu, Hologrow, OpenLore, Legion, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe, Alpha Sophia, HostTracker, Batru, Magic Hour, Ice Juice, Routebase, SSH MCP Server, Agentic Atlas, RE Data Refinery, AgentRisk M2M, OAIA Arena, ReactVision, uxgen, SocialRobot (catalogued Aug 26).
- mcpservers.org homepage: all 18 slugs already evaluated (famous servers + night-sweep skip mappings: agentcloud-so, count-nanocorp, fastgpu-co, proxyloom, runbear).

## Notes

- 2 of 2 fresh issues were catalogue-worthy, plus 1 feed find (BidSkim) - first sweep in several shifts where the issues window was 100% productive.
- DrillerDB is the catalog's first drilling/field-service vertical ERP; category ERP per the ATLASS OS precedent (field-service business platform).
- BidSkim landed in Compliance per the GovGazette precedent (federal contract and award intelligence = same product class, government procurement).
- TubeScout is the third YouTube research server (after BulkTranscripts hosted and tube-bridge self-hosted); catalogued on its demand-signal angle (autocomplete as search demand, likesPer1kViews resonance, research skill pack), not the transcript utility surface.
- Probe note: both hosted endpoints 401 on anonymous initialize - BidSkim's 401 body documented the exact auth paths (OAuth 2.1 RFC 9728 or API key as x-api-key header), which is quoted in the guide.
- Registry response shape reminder: `/v0/servers?search=X` returns `{"servers": [{"server": {...}}], "metadata": {...}}` - parse at `item["server"]` (the earlier addenda's shape held).
- Guide verification: titles 53-59 chars, descriptions 302-328 chars, zero em dashes, zero credential-guard patterns, See Also slugs all resolve and labels verified against target frontmatter (TEOS label corrected pre-commit).
- CI gate: local validate_frontmatter.py green (3518 files); index patch atomic (all asserts passed pre-write).
