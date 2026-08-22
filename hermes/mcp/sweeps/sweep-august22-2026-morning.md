---
title: "MCP Discovery Sweep - August 22, 2026 (Morning)"
date: 2026-08-22
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3683-#3690 (Aug 22 03:54-07:49 UTC) + mcp.so/mcpservers.org homepages + mcp.so Feed; 3 catalogued with guides, 2 skipped"
---

# MCP Discovery Sweep - August 22, 2026 (Morning)

- **Cutoff:** prior sweep (overnight) evaluated through issue #3682 (Aug 21 23:20 UTC)
- **Fresh window:** issues #3683-#3690 (Aug 22 03:54-07:49 UTC), mcp.so homepage recentServers, mcpservers.org homepage slugs, mcp.so Feed
- **Result:** 3 catalogued with guides, 2 skipped

## Catalogued (3 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Crisphive MCP (hosted field-service dispatch and technician scheduling: 43 tools generated from the same OpenAPI spec as the REST SDKs, preview/commit pairs on every mutation, idempotency keys, typed error codes, sub-3-second cascade rescheduling; OAuth 2.1 DCR+PKCE or chsk_test_/chsk_live_ API keys; endpoint api.crisphive.com/mcp, HTTP 401 auth gate confirmed live, stateless JSON) | 0 (repo created Jul 7, 2026) | Business Operations | GH issue #3690 |
| Dados B3 MCP (auditable Brazilian stock B3 fundamentals 2010-today: 402 listed companies + FII rankings, point-in-time multiples, Piotroski F-Scores with auditable criteria, republication tracking, CVM source accounts, public methodology; endpoint dadosb3.com/mcp/, live-probed v1.29.0, all 14 tools) | 0 (repo created Aug 11, 2026) | Finance | GH issue #3684 |
| Staddress AI MCP (Japanese address normalization over stdio: structured components, lat/lng, confidence score, address code; batch up to 100; usage checks; npx -y @staddress/mcp with STADDRESS_API_KEY; MIT client, npm v0.1.0) | 0 (repo created Jun 16, 2026) | Data & Analytics | GH issue #3686 |

## Skipped (2)

- **Lachesis (#3689)** - compiler-precise code property graph for C/Python/TypeScript (local stdio). Developer/code-analysis infrastructure, not business data. Skip class.
- **x402 Bazaar Doctor (#3683)** - deterministic diagnostics for settled-but-not-indexed x402 payments. Pure x402 payment plumbing, same class as 402oracle skip.

## Homepage and Feed repeats (previously evaluated)

mcp.so recentServers: all 8 entries repeats (QR Planet, RADAAR, Xverum, SavePropTax, CSOAI GSPC, 3gpp-mcp, Waqi, Bitroad). mcpservers.org homepage: 17 slugs, all famous/known or previously skipped (claudenews-online, doc-2328-io, www-getmaxim-ai-bifrost skipped overnight). mcp.so Feed: 29 slugs, all previously evaluated except html-css-to-image (dev utility, skip class - first noted this sweep).

## Verification performed

- Crisphive: OpenAPI spec fetched (43 operationIds = tool names, CI-enforced parity with REST SDKs); endpoint returns HTTP 401 auth gate (live per endpoint-verification doctrine)
- Dados B3: both endpoints live-probed (dadosb3.com/mcp/ and onrender mirror), v1.29.0, 14 exact tool names captured
- Staddress: repo + npm registry verified (v0.1.0 published), issue-body tool list used (stdio, key-gated)
- All 3 GitHub repos verified via API (0 stars each, created dates confirmed)
- All 3 guides pass YAML frontmatter gate, title/description length asserts, em-dash scan
- index.md patched with atomic patcher (all anchors asserted before write)
- Frontmatter CI gate green on all 3,304 files (scripts/validate_frontmatter.py)
- Push verified: local HEAD == origin/main
- Next cutoff: issue #3691
