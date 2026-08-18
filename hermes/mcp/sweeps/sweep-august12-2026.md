---
title: "MCP Sweep — August 12, 2026 - CorpusIQ Docs"
description: "Sweep following Aug 11 evening sweep. 6 new business-relevant MCP servers discovered — video production, organizational knowledge, agent commerce, payments"
date: 2026-08-12
sources: [mcp.so, mcpservers.org]
status: complete
finds: 6
guides: 6
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august12-2026/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — August 12, 2026

## Summary

- **6 genuinely new business-relevant servers found** since the August 11 evening sweep (~16 hours ago)
- **6 integration guides written** with full setup, tool descriptions, and verdicts
- **mcpservers.org was unreachable** (504 timeout on /all page) — mcp.so was primary source
- **mcp.so continues strong** — >22,000 servers, consistently adding 10-20/day

## Methodology

1. **mcp.so homepage** — Extracted Featured, Trending, and New Arrivals sections
2. **mcp.so /servers?sort=latest** — 30 newest servers (sorted newest-first)
3. **Cross-reference** — All candidates checked against the 200+ server catalog
4. **Business-relevance filter** — Only servers useful for business operators catalogued
5. **Individual server pages** — Extracted full details, tools, and configs from mcp.so detail pages
6. **mcpservers.org** — Attempted but timed out (504); no data captured from this source

## New Findings

### ★★★ Clipkit MCP — Catalogued with Guide

**What:** Video infrastructure for AI agents. Compose motion-graphics video from JSON documents via open Clipkit Protocol. Validate before rendering, preview stills in-chat, deterministic GPU output.

**Why it matters:** Video production is a top-3 operator pain point. Clipkit is the most production-ready agent-native video tool observed — protocol-first with deterministic rendering. Combines with HeyGen (UGC) and ViewMade (YouTube SEO) for a three-tier video stack.

**Guide:** `/hermes/mcp/servers/external/clipkit-mcp/`

---

### ★★★ Orcha MCP — Catalogued with Guide

**What:** Unified context layer for AI tools and agents. Stores organizational knowledge (files, databases, connected sources) with permissions, citations, and provenance. Agents query via MCP, CLI, or REST API.

**Why it matters:** The "context problem" is the #1 blocker for AI agents in business. Orcha provides a structured, permissioned knowledge layer — not just documents, but queryable databases. Different from PLUR (session memory) or Notion MCP (documents only).

**Guide:** `/hermes/mcp/servers/external/orcha-mcp/`

---

### ★★ FiatDock MCP — Catalogued with Guide

**What:** Agent marketplace with x402 per-call USDC payments. 24+ live MCP services, non-custodial settlement, on/off-ramp between USDC and fiat (EU/EEA). Agents discover and pay each other directly.

**Why it matters:** Signals the emergence of an agent-native economy. Per-call pricing ($0.001–$0.01), non-custodial, no subscriptions — the right architecture for agent commerce. Currently crypto/DeFi services; business APIs are the missing piece.

**Guide:** `/hermes/mcp/servers/external/fiatdock-mcp/`

---

### ★★ Apiosk MCP — Catalogued with Guide

**What:** AI-native payments infrastructure — 42 tools for discovering, paying for, executing, and publishing monetized APIs. Per-call USDC settlement over x402. Federated discovery across multiple marketplaces.

**Why it matters:** Most complete agent-payments solution observed. Wallet management, API publishing, federated discovery — the "Stripe for AI agents." Operators could publish paid APIs; agents could pay per call for business data.

**Guide:** `/hermes/mcp/servers/external/apiosk-mcp/`

---

### ★★ directree MCP — Catalogued with Guide

**What:** Query the honest software directory from any AI assistant. Reviews labeled by provenance: observed (crawled), AI-inferred (model-generated), and founder-edited (verified by owner).

**Why it matters:** Software selection is a persistent operator pain point. directree's provenance labeling is genuinely useful in an affiliate-dominated landscape. Currently early-stage with unknown directory coverage.

**Guide:** `/hermes/mcp/servers/external/directree-mcp/`

---

### ★ LocalCan MCP — Catalogued with Guide

**What:** Give AI agents public URLs (tunnels) for localhost, live HTTP traffic inspection, snapshot publishing. ngrok alternative with MCP-native interface.

**Why it matters:** Utility tool for operators who demo local work or test webhook integrations. Not a core growth tool but useful for technical operators.

**Guide:** `/hermes/mcp/servers/external/localcan-mcp/`

---

## Also Identified (Not Catalogued)

| Server | Source | Added | Why Not Catalogued |
|--------|--------|-------|--------------------|
| **NERAI Risk Intelligence** | mcp.so New | 19h ago | Already catalogued (nerai-risk-intelligence-mcp) |
| **Stoxly** | mcp.so New | Yesterday | Already catalogued (stoxly-mcp) |
| **FLINT Network** | mcp.so New | 3 days | Already catalogued (flint-network-mcp) |
| **q-ring** | mcp.so New | 4 days | Dev tool (quantum keyring) |
| **crosscode-cli** | mcp.so New | 2 days | Dev tool (coding sync) |
| **scvd.store** | mcp.so New | Yesterday | Crypto infra (x402 trust) |
| **SportsTrackLive** | mcp.so New | 3 days | Consumer (sports tracking) |
| **Trimtab AIS** | mcp.so New | 6 days | Maritime niche |
| **Nero AI Image** | mcp.so New | 7 days | Image processing (consumer) |
| **Repo Test Architect** | mcp.so New | 7 days | Dev tool |
| **ScrapeCheck** | mcp.so New | 8 days | Dev tool |
| **Screenshot Scout** | mcp.so New | 8 days | Dev tool |
| **Muumuu Domain** | mcp.so New | 9 days | Japanese domain registrar (regional niche) |
| **Sphere** | mcp.so New | 9 days | Agent marketplace (overlaps with FiatDock/Apiosk) |
| **GetIntel** | mcp.so New | 9 days | Dev tool |
| **Glasswarp** | mcp.so New | 13 days | Dev tool (Windows control) |
| **Designesy** | mcp.so New | 13 days | Dev tool (design verification) |
| **Floors.live** | mcp.so New | 14 days | Consumer (event planning) |
| **Orders of Magnitude** | mcp.so New | 16 days | Crypto (x402 catalog) |
| **Kavel Image Studio** | mcp.so New | 17 days | Consumer (image generation) |
| **AptiBuild AI** | mcp.so New | 17 days | Career (consumer niche) |
| **Bernstein** | mcp.so New | 18 days | Dev tool (orchestration) |
| **AgenticMemory** | mcp.so New | 18 days | Dev tool (memory) |
| **Stealth Web Search** | mcp.so New | 18 days | Dev tool (web search) |
| **Tako** | mcp.so New | 18 days | Dev tool (licensed data search) |
| **SecretCarousel** | mcp.so New | 19 days | Dev tool (secret vault) |

## Ecosystem Observations

1. **Agent commerce is accelerating.** FiatDock, Apiosk, Sphere, and Orders of Magnitude all launched within 2 weeks — all building on x402/USDC for agent payments. This is not a coincidence; the infrastructure layer is forming.

2. **Video production is the most contested MCP category.** Clipkit, AI Video MCP by AITuber, ViewMade, and Kavel Image Studio all launched recently. Each approaches video differently (JSON protocol vs prompt-driven vs research-first).

3. **Knowledge management is fragmenting.** Orcha, Groundwork, PLUR, AgenticMemory, and SecretCarousel all address "agent context" but from different angles: organizational knowledge, company memory, session memory, persistent memory, and secret management.

4. **mcpservers.org reliability is declining.** Second consecutive sweep where the /all page timed out. mcp.so is now the more reliable primary source.

## Catalog Stats

- **Total servers catalogued:** 200+ (prior) + 6 (this sweep) = **206+ servers**
- **Guides written this sweep:** 6
- **Business-relevant hit rate:** 6/30 (20%) — consistent with historical average
