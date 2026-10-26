---
title: "MCP Discovery Sweep - August 23, 2026 (Evening)"
date: 2026-08-23
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3704-#3711 (Aug 23 11:48-16:42 UTC), mcp.so homepage recentServers, mcpservers.org homepage slugs; 2 catalogued with guides (Atlas Verified, OEDON), 6 skipped"
last_updated: "2026-10-19"
---

# MCP Discovery Sweep - August 23, 2026 (Evening)

- **Cutoff:** morning cron sweep evaluated chatmcp/mcpso issues through #3703 (Aug 23 07:48 UTC)
- **Fresh window:** chatmcp/mcpso issues #3704-#3711 (Aug 23 11:48-16:42 UTC), mcp.so homepage recentServers, mcpservers.org homepage slugs
- **Result:** 2 catalogued with guides, 6 skipped

## Catalogued (2 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Atlas Verified MCP (official-registry supply-chain verification: organic certification against USDA Organic Integrity Database, OFAC screening, FDA import controls, document authentication with 30+ automated multi-OCR checks, 0-1000 trust score, chain of custody, structured trade intelligence from 50+ attributed sources (WTO, IMF, UN Comtrade, US Census); registry ai.atlasverified/atlas-mcp v1.0.0 active Jul 21, OAuth 2.0 + PKCE at api.atlasverified.ai/mcp, anonymous probe HTTP 401 auth gate confirmed; hosted, no public repo) | n/a (new listing) | Compliance | GH issue #3711 + official registry record |
| OEDON MCP (hosted x402 Bitcoin on-chain intelligence: 1 live-probed tool with 9 query types - fee pressure, mempool stats, address analytics, hashrate, difficulty, block tip, mining pools, tx lookup, whale alerts; endpoint oedon.dev/mcp, anonymous initialize, server oedon v0.2.0 protocol 2025-11-05, 0.005 USDC per query on Base) | n/a (new listing) | Finance | GH issue #3706 + live endpoint probe |

## Skipped (6)

- **symfony-agent-mcp (#3704)** - read-only Symfony codebase introspection with 1,677 tools via progressive meta-tool discovery. Dev tool, not business data.
- **annolux (#3705)** - curated bilingual (EN/CN) web search API and MCP with fetched_at timestamps. Search utility class, same as Context.dev skip.
- **LUNO (#3707)** - AI backend platform for building and governing production backends. No tools listed. Dev infra.
- **target5 (#3708)** - read-and-post board where AI agents debate with hash-chain claims. Agent community infra, same class as Fomite skip.
- **BuyWhere (#3709)** - SEA e-commerce product search and price comparison. Resubmission of an already-catalogued index entry (BuyWhere MCP, Commerce category); no new capability surface.
- **GateCore (#3710)** - governed discovery and procurement marketplace for AI agents (PROCURE/REVIEW/DENY contract terms). Agent procurement governance infra, x402/agent-economy plumbing class.

## Notes

- Both catalogued servers verified before guide writing: OEDON was live-probed anonymously (initialize returned serverInfo oedon v0.2.0 and tools/list returned the full 1-tool schema with the exact 9 query_type enum values - probe is ground truth); Atlas Verified is OAuth-gated so the anonymous probe's HTTP 401 confirmed the endpoint is live, tool names are documented at capability level from atlasverified.ai/products with an explicit caveat in the guide per the prose-tools last-resort doctrine (no OpenAPI spec published, registry record carries no tool list).
- Atlas Verified official registry record verified: ai.atlasverified/atlas-mcp v1.0.0, status active since Jul 21, 2026, remote type streamable-http.
- OEDON is an x402 data server that carries real market data (Bitcoin network intelligence), so it passed the x402 business-data test (RE Data Refinery / SYNTHORA / Truth Bear precedent).
- Homepage signals were all repeats: mcp.so recentServers (8 entries) and mcpservers.org homepage (19 slugs) contained only servers already catalogued or skipped in prior sweeps (corpuslaw slug confirmed as the Aug 22 catalogued Corpus Law guide; mangii confirmed as the Aug 22 skip).
- Catalog index updated: 325 to 327 servers (+211 to +213 guides).
