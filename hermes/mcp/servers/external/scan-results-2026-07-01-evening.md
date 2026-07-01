---
title: "MCP Server Scan Results — 2026-07-01 (PM Evening Update)"
description: "Evening update to the July 1 MCP server discovery scan. 5 new business-relevant servers found via GitHub API."
---

# MCP Server Directory Scan — July 1, 2026 (PM Evening Update)

## SOURCE: GitHub API (created >2026-07-01T12:00)

### Methodology
- GitHub API search: `topic:mcp-server created:>2026-07-01T12:00Z`
- 50 repos returned; 5 passed business-relevance filter
- Cross-referenced against existing catalog (index.md, morning + afternoon scans)
- mcp.so and mcpservers.org both accessible but serve SSR SPAs — scraping yields no new data
- This is the third scan of the day (morning, PM, PM evening)

---

## NEW BUSINESS-RELEVANT SERVERS

### 1. vrules — Agent Governance & Guardrails ★ New
- **Category:** Compliance / Security / Agent Infrastructure
- Open-source, vendor-neutral agent-governance and LLM guardrails framework. Vector-enabled rules engine for MCP proxying, policy-as-code, conditional organizational memory, and browser/WASM execution.
- GitHub: github.com/ops-ping/vrules (⭐0)
- **Business relevance:** First dedicated agent-governance MCP server. Operators deploying AI agent fleets in production need programmable guardrails, policy enforcement, and governance without vendor lock-in. vrules fills this gap with a vector-enabled rules engine that matches intent (not just keywords) and an MCP proxy architecture that sits between agents and their tools. Essential for regulated industries and any team running multi-agent deployments. **Created integration guide.**

### 2. Hermes Plant MCP Server — Deterministic Finance & Quant APIs ★ New
- **Category:** Finance / Quantitative Analysis
- Runnable MCP server for deterministic finance and quant APIs paid over x402. Provably correct financial calculations, quantitative models, and market analytics with cryptographic payment rails.
- GitHub: github.com/JesseGdotIO/hermesplant-mcp-server (⭐0)
- **Business relevance:** Bridges the trust gap between AI agents and financial computation. Every calculation is deterministic (same inputs → same outputs, like a smart contract) with x402 micropayment rails for pay-per-call pricing. Essential for operators building AI-driven quantitative finance workflows — portfolio analysis, options pricing, risk management, DCF modeling — where hallucinated numbers are unacceptable. **Created integration guide.**

### 3. Google Analytics MCP — Open-Source GA4 ★ New
- **Category:** Analytics / Marketing
- Free, open-source MCP server (44 tools) connecting Google Analytics 4 to Claude, Cursor, Windsurf, and any MCP client. Traffic analysis, funnel exploration, real-time reporting, and e-commerce analytics via natural language. MIT license.
- GitHub: github.com/yusofansari/google-analytics-mcp (⭐0)
- **Business relevance:** First fully open-source, MIT-licensed GA4 MCP server with 44 tools. Unlike existing analytics MCPs (Clamp Analytics, datavessel), this is focused exclusively on GA4 with zero vendor lock-in. Essential for operators who want GA4 data in their AI workflows without proprietary dependencies.

### 4. Google Ads MCP (Open Source) ★ New
- **Category:** Marketing / Advertising
- Free, open-source MCP server (57 tools) connecting Google Ads to Claude, Cursor, Windsurf, and any MCP client. Campaign management, keyword optimization, GAQL querying, and competitive analysis via natural language. MIT license.
- GitHub: github.com/yusofansari/google-ads-mcp (⭐0)
- **Business relevance:** Second Google Ads MCP server discovered today (earlier: smileCompiler's google-ads-mcp-server from June 30). This one is fully MIT-licensed with 57 tools (vs. smileCompiler's more limited set). Signals growing demand for zero-cost, open-source marketing MCPs. The yusofansari suite (GA4 + Ads + GSC) represents a complete Google Marketing Platform for AI agents.

### 5. Google Search Console MCP (Open Source) ★ New
- **Category:** Marketing / SEO
- Free, open-source MCP server (43 tools) connecting Google Search Console to Claude, Cursor, Windsurf, and any MCP client. Search analytics, indexing checks, cannibalization detection, and sitemap management via natural language. MIT license.
- GitHub: github.com/yusofansari/google-search-console-mcp (⭐0)
- **Business relevance:** Third open-source GSC MCP server (after GSC Wizard MCP and GSC SEO MCP), but this one is MIT-licensed with 43 tools. Complements the GA4 and Ads MCPs in the yusofansari open-source suite. Essential for SEO operators who want comprehensive Google Search Console data in their AI workflows without paid tools.

---

## ALSO NOTED (Lower Priority / Niche)

| Server | Category | Why Not Added |
|--------|----------|---------------|
| medoxisto/toolbox-mcp | Utility | 35 local tools (PDF, math, image, crypto). General utility, not business-specific. |
| xyun1996/ocular | Dev/Vision | Vision for text-only agents. Niche dev tool. |
| SaharshPamecha/drawx-mcp-server | Creative | draw.io diagrams from AI. Niche creative tool. |
| nickcheban/influx-mcp | Dev/IoT | InfluxDB for Home Assistant. Home automation niche. |
| nickcheban/pihole-mcp | Dev/Networking | Pi-hole v6 MCP. Home networking niche. |
| nickcheban/ruckus-mcp | Dev/Networking | Ruckus Wi-Fi MCP. Enterprise networking niche. |
| nickcheban/mikrotik-mcp | Dev/Networking | MikroTik RouterOS MCP. Enterprise networking niche. |
| yilmazali325/getmcpauth | Dev/Auth | OAuth 2.1 scaffolding tool for MCP servers. Dev utility. |
| the-ai-entrepreneur-ai-hub/sports-betting-operator-leads | Sales/Leads | B2B sports betting leads. Very niche vertical. |
| eon01/awesome-mcp | Meta/Curation | Curated list, not an MCP server. |
| Kuberwastaken/awesome-codex-mcp-servers | Meta/Curation | Curated list, not an MCP server. |

---

## KEY TRENDS (July 1 PM Evening)

- **Agent governance emerges as a category**: vrules is the first dedicated agent governance MCP server. As operators move from single-agent experiments to multi-agent production deployments, programmable guardrails become essential infrastructure. This category will grow rapidly.
- **Open-source Google Marketing Suite arrives**: yusofansari's trio (GA4 + Ads + GSC, all MIT-licensed) signals a shift toward zero-cost, no-vendor-lock-in marketing MCPs. Perfect for operators who want Google data without proprietary MCP dependencies.
- **Deterministic finance meets crypto payment rails**: Hermes Plant combines provably correct financial computation with x402 micropayments — a model for trustless, verifiable AI agent finance. The "smart contract for quant finance" pattern could become standard.
- **3rd scan of the day**: The MCP ecosystem is now generating enough new servers daily to warrant multiple sweeps. Morning (pushed), afternoon (created), and evening (created after noon) each yield different results.

---

## ACTIONS TAKEN

- ✅ Added 5 new servers to `index.md` catalog
- ✅ Created integration guide: vrules (`vrules.md`)
- ✅ Created integration guide: Hermes Plant (`hermesplant-mcp-server.md`)
- ✅ Updated "last updated" timestamp
- ✅ Updated ecosystem stats (483 cumulative, 35 sweeps)
- ⬜ Push to GitHub

---

*Scan performed July 1, 2026 PM evening. Source: GitHub API (topic:mcp-server created >2026-07-01T12:00Z).*
*Morning scan (pushed >2026-06-30): 4 servers. PM scan (created >2026-06-30): 2 servers. PM evening scan (created >2026-07-01T12:00): 5 servers.*
*Total new servers today: 11 across 3 sweeps.*
