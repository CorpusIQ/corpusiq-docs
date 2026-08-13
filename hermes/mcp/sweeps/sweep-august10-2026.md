---
title: "MCP Sweep — August 10, 2026"
description: "Post-July 31 sweep. 10 days of MCP server growth on mcp.so and mcpservers.org. 5 new business-relevant servers catalogued with integration guides."
date: 2026-08-10T12:00:00-07:00
sources: [mcp.so, mcpservers.org, github.com]
status: complete
finds: 5
guides: 5
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august10-2026/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — August 10, 2026

## Summary

- **5 genuinely new business-relevant servers found** across mcp.so and mcpservers.org
- **5 integration guides written** with full setup, tool tables, and verdicts
- **3 market signals noted** (FiatDock, Apiosk, FLINT Network) — agent payment infrastructure emerging
- **10-day gap** since last sweep (Jul 31) — significant new server velocity on mcp.so
- **All new servers are remote HTTP** — zero new stdio/local servers found. The MCP ecosystem is shifting decisively toward hosted/remote servers.

## Methodology

1. **mcp.so homepage** — New arrivals, trending, and featured sections
2. **mcp.so /servers full listing** — Cross-referenced ~60+ server entries against existing 128-server catalog
3. **mcpservers.org** — Checked for new arrivals; server listing page returned 404 on sort parameter
4. **GitHub repos** — Verified creation dates, commit activity, and README details for top candidates
5. **Cross-reference** — Checked each server against existing catalog directories to avoid duplicates

## Findings

### ★★★ Competitor Tracker & Co. — Catalogued with Guide

**What:** Agentic competitor intelligence — ~50 tools for tracking competitor pricing, product, messaging, and corporate changes via weekly website crawls. Remote MCP, OAuth or API-key auth.

**Why it matters:** First MCP server purpose-built for competitive website intelligence. Growth operators and product managers can ask "what changed across our competitors this week?" and get ranked answers with page snapshots — no separate dashboard required. ~50 tools with read/write/destructive tiers and confirm gates for safety.

**Details:**
- Remote MCP: `https://mcp.competitortracker.io/mcp` (Streamable HTTP)
- GitHub: `CofounderGPT/competitor-tracker-mcp` (0★, created Jul 15, 2026)
- ~50 tools (read, write, destructive with confirm gates)
- OAuth for interactive clients, X-API-Key for headless/automated
- Coin-based pricing

**Guide:** `/hermes/mcp/servers/external/competitor-tracker-mcp/`

---

### ★★★ Holdings — Catalogued with Guide

**What:** Agentic invoicing and payments — let your AI send invoices and collect payment via card or ACH. Free (no monthly fee; standard Stripe processing fees on payments). npm package or hosted endpoint.

**Why it matters:** First MCP server to bridge AI agents and real payment collection. Confirm-gated design (draft → preview → confirm → send) is exactly right for financial operations. Free pricing removes adoption barrier entirely. This represents a new category: agentic finance operations.

**Details:**
- stdio: `npx -y @getholdings/mcp` with `HOLDINGS_API_KEY`
- Remote: `https://mcp.getholdings.com/mcp`
- GitHub: `holdings-io/mcp` (0★, created Jul 28, 2026)
- npm: `@getholdings/mcp`
- MCP Registry: `com.getholdings/mcp`
- Free (Stripe processing fees only)

**Guide:** `/hermes/mcp/servers/external/holdings-mcp/`

---

### ★★★ Lawstronaut — Catalogued with Guide

**What:** Legal research infrastructure for AI agents — 50M+ laws and court cases from 155+ jurisdictions. Structured legal data, continuously updated. OAuth 2.0 + Bearer token auth. Published by Lawstronaut-FZCO.

**Why it matters:** Most comprehensive legal research MCP server — 155+ jurisdictions dwarfs any other legal MCP. Complementary to The Bot Wire (catalogued Jul 31) which covers US regulatory/economic primary sources. Together they form a complete compliance intelligence stack: Bot Wire for real-time regulatory monitoring, Lawstronaut for structured legal research.

**Details:**
- Remote MCP: `https://mcp.lawstronaut.com` (Streamable HTTP)
- GitHub: `Lawstronaut-FZCO/lawstronaut-mcp` (1★, created Jul 9, 2026)
- OAuth 2.0 or Bearer token
- 50M+ documents, 155+ jurisdictions
- Paid subscription required

**Guide:** `/hermes/mcp/servers/external/lawstronaut-mcp/`

---

### ★★ FlowyTeam OKR MCP Server — Catalogued with Guide

**What:** Native OKR/KPI MCP server — 33 tools covering OKRs, KPIs, tasks, projects, employees, attendance, leave, tickets, clients, leads, and invoicing. One connection, full operational stack. OAuth with PKCE for desktop/web, Bearer token for CLI.

**Why it matters:** First MCP server purpose-built for business performance management (OKRs + KPIs). The 33-tool surface goes beyond OKRs to cover the full operational stack — tasks, projects, team management, CRM, and invoicing. Makes OKR management conversational instead of quarterly dashboard check.

**Details:**
- OAuth: `https://flowyteam.com/api/mcp/cloud/rpc` (Claude Desktop, ChatGPT)
- CLI: `https://flowyteam.com/api/v2/mcp/rpc` (Claude Code, Cursor, VS Code)
- Gateway: `https://flowyteam.com/api/mcp/gateway` (no token, onboarding only)
- GitHub: `flowy-team/okr-mcp-server` (0★, created Aug 7, 2026)
- 33 tools across OKRs, KPIs, tasks, projects, employees, CRM, invoicing

**Guide:** `/hermes/mcp/servers/external/flowyteam-okr-mcp/`

---

### ★★ akta.pro — Catalogued with Guide

**What:** Private company intelligence MCP — company search, structured profiles, news monitoring, and alternative signals (headcount trends, web traffic, reviews). Published by Wokelo AI (due diligence platform). Remote HTTP, OAuth or API key auth.

**Why it matters:** Consolidates company research that normally requires 5+ separate tools (LinkedIn, SimilarWeb, news, review sites) into a single MCP connection. Alternative signals (headcount, traffic, reviews) provide a more complete picture than traditional firmographic databases. Backed by Wokelo AI, an established due diligence platform.

**Details:**
- Remote MCP: `https://mcp.akta.pro/mcp` (Streamable HTTP)
- GitHub: `akta-pro/akta.pro-mcp`
- OAuth or x-api-key header
- Publisher: Wokelo AI (wokelo.ai)
- Paid subscription

**Guide:** `/hermes/mcp/servers/external/akta-pro-mcp/`

---

### Market Signals (Not Catalogued)

| Server | Type | Why Not Catalogued |
|--------|------|--------------------|
| FiatDock (2 days ago) | AI agent marketplace, USDC/x402 payments | Market signal — indicates growing agent-to-agent payment infrastructure. Not an operational tool for business operators. |
| Apiosk (3 days ago) | AI-native payments marketplace, x402/USDC | Similar to FiatDock — agent payment infrastructure. Watch for convergence with MCP billing. |
| FLINT Network (yesterday) | Agent integrity verification before money movement | Interesting fintech security concept but narrow: a "SKILL.md" rather than a full MCP server. Premature for integration guide. |

### Emerging Trend: Agent Payment Infrastructure

FiatDock, Apiosk, and Orders of Magnitude (x402 API Catalog, also new) represent a clear trend: AI agents paying other AI agents for services via USDC over x402 protocol. While not operational tools for business operators today, this infrastructure layer will eventually enable agent-to-agent commerce — your operations agent paying a research agent for market data, or a content agent paying a design agent for graphics. Monitor this space.

### Remote-Only Trend

All 5 servers catalogued in this sweep are remote/HTTP. Zero new stdio/local servers. The MCP ecosystem is shifting decisively toward hosted servers — easier onboarding, no local runtime dependency, OAuth-based auth. This aligns with the broader trend of MCP moving from developer tooling to business operations.

## Catalog Status After Sweep

- **Servers:** 133 (+5 from July 31)
- **Guides:** 33 (+5 from July 31)
- **This sweep's additions:** Competitor Tracker & Co. (★★★), Holdings (★★★), Lawstronaut (★★★), FlowyTeam OKR (★★), akta.pro (★★)

## Notes

- The 10-day gap since the last sweep yielded 5 quality finds — MCP server creation velocity is accelerating
- mcp.so's "New Arrivals" section is the most reliable signal for genuinely new servers; the /servers page mixes new and old with unclear sorting
- GitHub creation dates are a better signal than mcp.so "Added X days ago" badges, which can reflect re-listing or metadata updates
- The July 31 sweep missed Competitor Tracker (Jul 15) and Lawstronaut (Jul 9) — both were created before the sweep window but not yet surfaced on mcp.so at that time
- The shift to remote-only servers means integration guides need less npm/install content and more OAuth/endpoint configuration
- mcpservers.org continues to be less useful for discovery than mcp.so — server listing page broke on sort parameter
