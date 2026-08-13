---
title: MCP Server Sweep — July 27, 2026 (Morning)
description: "MCP server discovery sweep from July 27, 2026 (morning run). New MCP servers cataloged from across the ecosystem."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july27-2026-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Sweep — July 27, 2026 (Morning)

**Run:** 2026-07-27T10:05 UTC  
**Sources checked:** mcpservers.org /all, chatmcp/mcpso issues, awesome-mcp-servers PR queue  
**Catalogs scanned:** mcpservers.org (30 newest), mcpso issues (20 latest), awesome-mcp-servers (2 merged PRs)  

## Summary

| Metric | Count |
|--------|-------|
| Total scanned | 52 entries |
| Already cataloged | 12 |
| New servers (all priority) | 29 |
| Integration guides written | 8 |
| Business-relevant (HIGH/MEDIUM) | 13 |

---

## New Servers — Integration Guides Written (8)

### HIGH Priority (6)
| Server | Category | Transport | Auth | Repository |
|--------|----------|-----------|------|------------|
| **Fulcru** | Marketing/SEO | Remote HTTP | Bearer token | gsmmediaro/fulcru-agent |
| **Opportunity Exchange** | Gov/Procurement | Remote HTTP | Keyless | veilpoint.ca (operated) |
| **GTD Brain** | Productivity | Remote HTTP | OAuth 2.1 PKCE | gtdbrain.com (commercial) |
| **PingCheck** | DevOps/Monitoring | stdio (npx) | API key | Churman1113/pingcheck |
| **Peil** | Finance/Freelance | stdio | TBD | Luminc/peil-mcp |
| **x-use** | Social Media | stdio (pip) | Cookie-based | ihuzaifashoukat/x-use |

### MEDIUM Priority (2)
| Server | Category | Transport | Auth | Repository |
|--------|----------|-----------|------|------------|
| **Agentic Memory** | Knowledge/Memory | Remote SSE | API key | jyswee/agenticmemory |
| **Pathix** | Enterprise/ERP | Remote HTTP | OAuth (Entra) | Commercial, self-hosted |

---

## New Servers — Listed Only (21)

### From mcpservers.org /all:
- **CDN.MN** — CDN delivery MCP (already cataloged as cdnmn-mcp, re-verified)
- **BBW Belles Formalwear** — Consumer fashion, hard-gated size 22-40 (LOW)
- **Confluence to Markdown** — Confluence content indexing for AI (MEDIUM, not written — similar to existing confluence-mcp entries)
- **BountyVerdict** — GitHub bounty assessment, agent instruction audits (LOW)
- **AIQUAA Playwright** — Playwright BDD testing with business-rule traceability (MEDIUM)
- **Retasc** — Issue tracker for AI coding agents, 33 tools (MEDIUM)
- **Actvt** — Mac system metrics, Claude/Codex session history (LOW)
- **Grok Chat MCP** — xAI Grok API wrapper, chat/vision/search (LOW)
- **Santiment** — Crypto on-chain metrics, social sentiment (LOW)
- **Snipara** — Project intelligence, code graph tools (MEDIUM)
- **Fable MCP** — Claude Fable 5 planning/critique (LOW)
- **Claude Chat MCP** — Anthropic Claude Messages API wrapper (LOW)

### From chatmcp/mcpso issues:
- **Verificate MCP** — AI coding validation gates, ISO/IEC 25010 review (#3319, MEDIUM)
- **Health Export MCP** — 190 Apple Health metrics (#3312, LOW)
- **Nauti-Labs Clearance** — x402/USDC payment flow review (#3310, MEDIUM)
- **Sayba** — AI agent social network, 23 tools (#3308, LOW)
- **hwatu** — Visual verification browser for coding agents (#3304, LOW)
- **VK (VKontakte)** — Russian social network, 19 tools (#3303, LOW)
- **GoldBean** — 53 Chinese AI tools via x402 micropayments (#3299, LOW)
- **Prerender Buddy** — Crawler visibility for AI/search (#3297, MEDIUM)
- **Humanity4AI** — 9 humanity skills for AI agents (#3296, LOW)

---

## Source Health

| Source | Status | Notes |
|--------|--------|-------|
| mcpservers.org /all | ✅ Healthy | 30 items, JSON-LD extraction working |
| chatmcp/mcpso issues | ✅ Healthy | 20 issues scanned, 19 submissions + 1 removal |
| awesome-mcp-servers PR queue | ⚠️ Rate limited | gh API rate limited; unauthenticated curl returned only 2 merged PRs (both pre-dating last sweep) |
| mcp.so sitemap | ⏭️ Skipped | Not needed — mcpservers.org + mcpso issues provided sufficient coverage |

---

## git Push Status
Pushed to https://github.com/CorpusIQ/corpusiq-docs (main branch)
