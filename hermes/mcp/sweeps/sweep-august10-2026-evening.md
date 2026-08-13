---
title: "MCP Sweep — August 10, 2026 (Evening Follow-Up)"
description: "Post-morning sweep follow-up. 4 additional business-relevant MCP servers discovered from mcp.so deep scan."
date: 2026-08-10T18:30:00-07:00
sources: [mcp.so, mcpservers.org]
status: complete
finds: 4
guides: 4
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august10-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — August 10, 2026 (Evening)

## Summary

- **4 genuinely new business-relevant servers found** from mcp.so deep scan (pages 1-3)
- **4 integration guides written** with full setup, tool descriptions, and verdicts
- **Morning sweep (12:00 PT)** found 5 servers; this evening follow-up adds 4 more
- **1 brand-new server** (Stoxly, added 4 hours ago) — appeared after morning sweep
- **3 missed-in-morning-sweep** servers (Perfex CRM, Fund Momentum, FCA Handbook) — were listed on mcp.so but not in top ~60 entries scanned earlier

## Methodology

1. **mcp.so /servers?sort=latest** — Full deep scan across 3 pages (~90 entries)
2. **mcpservers.org /all** — Latest 30 entries cross-referenced
3. **Cross-reference** — Each candidate checked against 133-server catalog
4. **Business-relevance filter** — Only servers useful for business operators (finance, CRM, compliance, fundraising)

## Evening Findings

### ★★★ Perfex CRM MCP — Catalogued with Guide

**What:** Self-hosted MCP server for Perfex CRM — full REST API exposed as typed MCP tools. Leads, customers, invoices, tickets, projects, contracts, subscriptions. Read + write with scoped API keys, read-only mode, granular tool control, and full request logging.

**Why it matters:** First self-hosted CRM MCP server. Perfex is the leading self-hosted CRM for small/medium businesses. This MCP lets operators ask "which clients have overdue invoices older than 45 days?" and get answers in one prompt. Staff-level permissions respected. No third-party relay — data stays on your server.

**Details:**
- stdio + HTTP transports
- GitHub: `themesic/perfex-rest-api-examples` (MIT)
- Category: CRM / Productivity
- Auth: Perfex API keys (staff-level scoping)
- Added to mcp.so: ~4 days ago (Aug 6)

**Guide:** `/hermes/mcp/servers/external/perfex-crm-mcp/`

---

### ★★ Stoxly — Catalogued with Guide

**What:** Remote MCP server for free stock & ETF fundamental analysis — 10-point score, verdict, and metrics for any ticker. By wizard-exe.

**Why it matters:** Lightweight, free financial analysis MCP. Complements heavier financial MCPs (Sugra, Fintel, Capital.com) with instant fundamental scores. No API key required. Good first financial MCP for operators who want quick equity research without paid subscriptions.

**Details:**
- Remote MCP (likely Streamable HTTP)
- Author: wizard-exe
- Free, no API key
- Added to mcp.so: ~4 hours ago (Aug 10 evening)

**Guide:** `/hermes/mcp/servers/external/stoxly-mcp/`

---

### ★★ Fund Momentum MCP — Catalogued with Guide

**What:** VC intelligence for AI assistants — 920+ active VC funds, live investor signals, AI-powered startup matching. Remote MCP with API key.

**Why it matters:** First dedicated VC/fundraising intelligence MCP. For founders and operators raising capital, this replaces manual CrunchBase/Angellist research. Live investor signals and AI-powered matching make it actionable, not just a database. Complements akta.pro (company intelligence, catalogued this morning) for the fundraising use case.

**Details:**
- Remote MCP: `https://fundmomentum.vc/_api/mcp`
- GitHub: `schneidavie/fundmomentum`
- API key required
- 920+ VC funds, investor signals, startup matching
- Added to mcp.so: ~8 days ago (Aug 2)

**Guide:** `/hermes/mcp/servers/external/fund-momentum-mcp/`

---

### ★★★ FCA Handbook MCP (Metis Harness) — Catalogued with Guide

**What:** UK Financial Conduct Authority (FCA) Handbook compliance MCP — 10,000+ handbook entries, verbatim citations, structured applicability evaluation. Stateless, one-shot design. MIT licensed.

**Why it matters:** First regulatory compliance MCP server. Transforms UK financial services compliance from manual handbook searching to AI-agent queries. Returns verbatim citations with binding levels (R=Rule, G=Guidance). Stateless design fits enterprise security standards. Essential for any UK fintech/financial services operator using AI agents.

**Details:**
- stdio: `fca-handbook-harness-mcp` (pip install)
- Homepage: `fcahandbookharnessimplementation.onrender.com`
- GitHub: `99blakeD99/the-metis-fca-handbook-ai-harness-mcp-files` (MIT)
- 10,000+ FCA Handbook entries
- Quick mode (~60-120s) or full mode (detailed)
- Paid: Metis API key required
- Added to mcp.so: ~7 days ago (Aug 3)

**Guide:** `/hermes/mcp/servers/external/fca-handbook-mcp/`

---

## Also Identified (Not Catalogued)

| Server | Type | Why Not Catalogued |
|--------|------|--------------------|
| Trimtab AIS (5 days ago) | Ship/port AIS data — 8 US container gateways | Niche logistics. Free, no key. Good signal for supply-chain MCPs but narrow audience. |
| Goalie Trademark Search (18 days ago) | 14M+ USPTO trademark records | IP legal niche. Useful for operators managing trademarks but overlaps with Pangolinfo (catalogued Jul 31). |
| Pickle (19 days ago) | ClickUp/Slack/Teams ops manager | Productivity tool. Free, local. Worth monitoring but not unique — overlaps with existing task/project MCPs. |
| Anomalia (mcpservers.org) | Marketing content planning | Growth tool but light on details. Premature for guide. |
| Exchangerate.dev (mcpservers.org) | Keyless FX rates, 465 pairs | Useful financial utility but thin — more of a building block than a full MCP server. |

## Catalog Status After Evening Sweep

- **Servers:** 137 (+4 from morning's 133)
- **Guides:** 37 (+4 from morning's 33)
- **This sweep's additions:** Perfex CRM MCP (★★★), FCA Handbook MCP (★★★), Stoxly (★★), Fund Momentum MCP (★★)

## Notes

- The mcp.so /servers?sort=latest listing is paginated deeply — morning sweep only scanned ~60 entries, missing servers on pages 2-3. Future sweeps should scan at least 3 pages (90 entries).
- Stoxly appeared between the morning sweep and this evening follow-up — mcp.so velocity is high enough that same-day follow-ups now yield finds.
- Regulatory compliance (FCA Handbook) and CRM (Perfex) are new MCP categories — signals that MCP is moving beyond developer tools into line-of-business operations.
- mcpservers.org continues to be mostly developer-tool and niche servers; mcp.so is the better discovery source for business-relevant servers.
- GitHub token auth works via `gh` CLI — pushes to `CorpusIQ/corpusiq-docs` are confirmed working.
