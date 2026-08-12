---
title: "MCP Sweep — August 12, 2026 (Afternoon)"
description: "Follow-up to the Aug 12 morning sweep (~6 hours later). 10 new business-relevant MCP servers catalogued, 6 integration guides written — content quality tooling, finance, sales intelligence, and AI-engine visibility."
date: 2026-08-12
sources: [mcpservers.org, mcp.so]
status: complete
finds: 10
guides: 6
---

# MCP Server Discovery Sweep — August 12, 2026 (Afternoon)

**Timestamp:** 2026-08-12 (afternoon, UTC)  
**Sources scanned:** mcpservers.org /all pages 1-3 (90 newest servers, curl + regex slug extraction), mcp.so Feed (30 newest submissions, web_extract), mcp.so server detail pages (9 fetched for endpoint/auth/tool verification)  
**New servers found:** 10 business-relevant (6 guides written, 4 catalog entries)

---

## Summary

- **10 genuinely new business-relevant servers** since the Aug 12 morning sweep (~6 hours ago)
- **6 integration guides written** with verified endpoints, auth models, tool lists, and CorpusIQ integration sections
- **mcpservers.org /all reachable** (page 1 + 2 + 3, 90 unique slugs) — the morning sweep reported 504 timeouts on it; recovered this cycle
- **mcp.so Feed productive** — 30 submissions in ~5 days, several never surfaced in directory views
- **Two ecosystem patterns:** (1) human-gate content tooling — Prose Coach (deterministic de-AI filter), BanProof (script compliance), Plainpaper (human-approved campaigns); (2) financial-data MCPs keep compounding — ROIC.ai joins the 5+ market-data servers already catalogued

## Methodology

1. **mcpservers.org /all** — curl pages 1-3, regex-extracted 90 server slugs
2. **mcp.so /feed** — web_extract, 30 newest submissions with timestamps
3. **Cross-reference** — all 90 slugs + 30 feed names OR-searched against the catalog index.md; any hit verified individually with `grep -n`
4. **Detail verification** — 9 mcp.so server detail pages fetched for endpoints, auth, and tool lists (no unverified claims in guides)
5. **Business-relevance filter** — HIGH → guide; notable MEDIUM → catalog entry; rest → also-identified

---

## 🔥 New Business-Relevant Finds (Guides Written)

### ★★★ Prose Coach MCP — Guide Written
Deterministic AI-writing filter — 43 patterns flagged with the triggering line quoted and the fix attached. Remote Streamable HTTP, no auth, one URL. Free tier 3 drafts/day @12K chars; PRO $5/mo. First MCP purpose-built to de-AI content before it ships. `prose.coach/mcp` · [Guide →](/hermes/mcp/servers/external/prose-coach-mcp/)

### ★★★ ROIC.ai MCP Server — Guide Written
Financial data for 60,000+ public companies — prices, statements, earnings transcripts, fundamentals, ratios, valuation multiples. One server covers the whole stack. Streamable HTTP + API key. `mcp.roic.ai/mcp` · [Guide →](/hermes/mcp/servers/external/roic-ai-mcp-server/)

### ★★★ cloro MCP — Guide Written
Live AI answer engine access — ChatGPT, Gemini, Perplexity, Copilot, Grok, Google AI Mode with cited sources; Google Search/News with country/state geo-targeting. Purpose-built for brand monitoring and GEO/AEO. API key. `mcp.cloro.dev` · [Guide →](/hermes/mcp/servers/external/cloro-mcp/)

### ★★★ Stratyfix MCP — Guide Written
Sales intelligence — 10 read-only tools over live pipeline (deal forecasts, pace-to-target, coaching queue, team coverage). OAuth per-user permissions; honesty rule: withholds numbers it can't defend instead of guessing. `app.stratyfix.com/api/mcp` · [Guide →](/hermes/mcp/servers/external/stratyfix-mcp/)

### ★★ FlowyTeam OKR MCP — Guide Written
Native OKR server — objectives, key results, tasks for Claude, ChatGPT, n8n; check-ins and KR progress moves from chat. MIT, OAuth. `github.com/flowy-team/okr-mcp-server` · [Guide →](/hermes/mcp/servers/external/flowyteam-okr-mcp/)

### ★★ QuestDB MCP Server — Guide Written
Official QuestDB MCP — notebook cells, queries, charts against a running Web Console session. `npx @questdb/mcp-server-questdb setup`. Apache-2.0. `github.com/questdb/mcp-server-questdb` · [Guide →](/hermes/mcp/servers/external/questdb-mcp/)

---

## 📋 Catalogued (Notable MEDIUM, no guide)

| Server | Category | Why catalogued |
|---|---|---|
| **Plainpaper MCP** | Marketing | AI marketing canvas — 54 tools, campaigns as cards, brand rules, human approval gate. OAuth. Starter $29/mo |
| **Contio MeetingOS MCP** | Meetings | Agendas, transcripts, action items without recording audio/video. OAuth. `mcp.contio.ai/mcp` |
| **MachineTranslation.com MCP** | Translation | Multi-model-consensus translation via MCP — global content ops. Commercial (tomedes-org) |
| **BanProof AI** | Content Compliance | Audits TikTok Shop + Amazon affiliate scripts for policy violations before recording/publishing. `banproof.io` |

---

## Also Identified (Not Catalogued)

| Server | Source | Why Not Catalogued |
|---|---|---|
| **Canvas API MCP** | mcpservers.org | Education niche (per Aug 11 decision) — 16 student tools + gateway to 1,116 Canvas endpoints |
| **MoodleMCP** | mcpservers.org | LMS — education niche |
| **React SEO Skills** | mcpservers.org | Dev-tool adjacent (SEO linting for coding agents) |
| **Faxer** | mcp.so | Ops utility — fax delivery with Stripe checkout; niche but useful for fax-only vendors |
| **Constants** | mcp.so | Workspace + ad creative tools; overlaps with catalogued ad MCPs |
| **LabTestSuperstore** | mcp.so | Lab-supplies commerce; ecommerce niche |
| **GetLulu 6-pack** | mcpservers.org | Micro-utilities (crypto price, domain RDAP, FX, holidays, registry, weather) |
| **Conqueror** | mcp.so | Unclear scope |
| **CR8 Agent Commons** | mcp.so | Agent message board — consumer/infra |
| **x402 Merchant Check** | mcp.so | Crypto (Base on-chain) |
| **GoLeasy MCP** | mcp.so | German leasing — regional niche |
| **Departi** | mcp.so | Travel compliance — consumer |
| **Andrii Co Notary** | mcp.so | WA state notary — regional niche |
| **~25 dev-tool/utility entries** | mcpservers.org /all | bunkerweb, humanpen, lobu, mercury-cortex, strata, sonaprompt, ohm, sshmng, python-code-validator, website-analyzer, canvora, citerank, and more |
| **rudrendupaul burst (~30 entries)** | mcpservers.org /all | EXCLUDED — classic AI-generated catalog-spam signals (haltproof, shimguard, toolgovern, tokentrust…); single-author bulk submission pattern |

---

## Morning Sweep Note

The Aug 12 morning sweep's 6 servers (Orcha ★★★, Clipkit ★★, FiatDock ★★, Apiosk ★★, directree ★★, LocalCan ★) have guides at `/hermes/mcp/servers/external/{orcha,clipkit,fiatdock,apiosk,directree,localcan}-mcp/` but were never added to the catalog index body. This afternoon sweep's catalog update counts them in the totals (Catalog: 162 servers, +58 guides) for accuracy; their entries remain in the morning sweep report.

---

## Key Observations

1. **Human-gate content tooling is the trend.** Prose Coach (deterministic de-AI filter), BanProof (policy compliance before publish), and Plainpaper (human approval board) all insert a human gate or deterministic check between the agent and the publish button. The ecosystem is shipping answers to the #1 operator objection: "agents write content that sounds like agents."
2. **Financial-data MCPs keep compounding.** ROIC.ai is the 6th market-data/finance MCP catalogued this month. Category saturation means differentiation now comes from coverage breadth (60K companies) and transcript access, not raw price feeds.
3. **AI-engine visibility is becoming its own category.** cloro joins AI Footprints and similar tools in the "what do AI engines say about you" space — the GEO measurement layer the worldwide-promotion playbook needs.
