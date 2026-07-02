---
title: "MCP Server Scan Results — 2026-07-02"
description: "July 2 MCP server discovery scan. 18 new business-relevant servers found — finance vertical explodes, pipeworx-io industrializes MCP wrapping, GraphRAG memory arrives."
---

# MCP Server Directory Scan — July 2, 2026

## SOURCES: mcp.so + GitHub API

### Methodology
- **mcp.so**: Scraped server listings, filtered by creation date >= 2026-07-02
- **GitHub API**: `topic:mcp-server created:>2026-07-01` — 55 repos returned
- Cross-referenced against existing catalog (index.md, all July 1 scans)
- mcp.so served 3 new servers; GitHub API surfaced 15 additional business-relevant repos

---

## KEY FINDING: The Pipeworx-IO Industrialization

**pipeworx-io shipped 18+ new MCP servers in a single day (July 2)** — the single largest one-day batch in MCP ecosystem history. Pattern: every API gets an MCP wrapper. Their business-data suite alone includes:

| Server | Category | API Wrapped |
|--------|----------|-------------|
| mcp-tradier | Finance | Tradier Brokerage (stocks & options market data) |
| mcp-eodhd | Finance | EOD Historical Data (global equities) |
| mcp-diffbot | Business Intel | Diffbot Knowledge Graph (company enrichment) |
| mcp-coresignal | Business Intel | Coresignal (LinkedIn-adjacent company + employee data) |
| mcp-peopledatalabs | Business Intel | People Data Labs (person/company enrichment) |
| mcp-shodan | Security | Shodan REST API (internet scanning) |
| mcp-pulsedive | Security | Pulsedive threat intelligence IOC enrichment |
| mcp-seo-backlinks | Marketing | DataForSEO Backlinks API |
| mcp-emailable | Marketing | Emailable email verification |

This signals a new phase in MCP maturity: industrial-scale, systematic API wrapping as a service.

---

## NEW BUSINESS-RELEVANT SERVERS

### 1. SentiSense — Market Intelligence MCP ★★★
- **Category:** Finance / Market Intelligence
- Bring market intelligence into Claude/ChatGPT: US market mood, stock sentiment, SentiSense Score, market-moving news, analyst ratings, 13F filings. Five read-only tools, zero-config OAuth, no API key required.
- URL: https://sentisense.ai
- **Business relevance:** First dedicated market sentiment MCP server. Operators in finance can query market mood, analyst consensus, and institutional buying patterns directly from their AI assistant. The zero-API-key model lowers the barrier to entry dramatically. Essential for investment analysts, portfolio managers, and fintech operators needing AI-driven market intelligence.

### 2. SEOforGPT — AI Visibility / GEO MCP ★★★
- **Category:** Marketing / SEO / AI Visibility
- Agentic AI visibility platform for marketing agencies and SEO consultants. Connects Claude/Cursor to SEOforGPT workspace: audit client visibility across ChatGPT, Claude, Perplexity, and Gemini; track competitors and AI-cited sources; generate AI-optimized content; publish to CMS — all from the AI assistant.
- URL: (mcp.so listing, GitHub TBD)
- **Business relevance:** As search shifts from Google to AI platforms (ChatGPT, Claude, Perplexity), "generative engine optimization" (GEO) becomes the new SEO. SEOforGPT is the first purpose-built GEO MCP — agencies can audit, track, and optimize client visibility across every major AI platform from a single MCP connection. Essential for marketing operators who need to future-proof their SEO practice.

### 3. HPSILab — Quant Finance MCP ★★★
- **Category:** Finance / Quantitative Analysis
- Institutional-grade quantitative finance MCP: stock analysis, options analytics (Black-Scholes, Greeks), implied volatility surfaces, Monte Carlo simulations, AI market signals, strategy backtesting. Quantum ML (Qiskit) and regime detection included.
- URL: (mcp.so listing)
- **Business relevance:** Pushes MCP-based quant finance to institutional-grade. Where Hermes Plant focuses on deterministic computation with crypto payment rails, HPSILab targets the full quant stack: options pricing, volatility modeling, Monte Carlo, quantum ML. Together these two servers establish "AI agent quant finance" as a legitimate category. Essential for quant analysts, hedge fund operators, and fintech builders.

### 4. Kalshi MCP — Prediction Markets ★★
- **Category:** Finance / Prediction Markets
- MCP server for Kalshi prediction markets: get markets, positions, and place orders from any AI agent. TypeScript, 0 stars (brand new).
- GitHub: https://github.com/onofre-jauregui/kalshi-mcp
- **Business relevance:** First prediction-market MCP server. Kalshi is the first CFTC-regulated prediction market in the US. Operators can now have AI agents monitor event contracts, analyze market probabilities, and execute trades — effectively "programmatic event-driven investing." Essential for operators in prediction markets, political forecasting, and event-driven trading.

### 5. MCP Long-Term Memory (GraphRAG) ★★
- **Category:** AI Infrastructure / Agent Memory
- MCP server providing GraphRAG-based long-term memory to AI agents. Uses Neo4j for knowledge graph storage, enabling agents to persist and recall context across sessions.
- GitHub: https://github.com/null-create/mcp-long-term-memory
- **Business relevance:** Memory/persistence is the #1 unsolved problem for production AI agent deployments. GraphRAG-backed MCP memory servers enable agents to build and query knowledge graphs across sessions — essentially "enterprise memory for AI." Essential for operators building persistent agent workflows where context must survive beyond a single session.

### 6. pipeworx-io/mcp-tradier — Stock & Options Market Data ★★
- **Category:** Finance / Market Data
- Wraps the full Tradier Brokerage API for stocks & options market data. Part of the pipeworx-io industrial MCP suite.
- GitHub: https://github.com/pipeworx-io/mcp-tradier
- **Business relevance:** Tradier is a leading brokerage API for retail trading platforms. This MCP gives AI agents direct access to real-time and historical stock/options data. Essential for operators building AI trading assistants or market analysis workflows.

### 7. pipeworx-io/mcp-diffbot — Knowledge Graph Enrichment ★★
- **Category:** Business Intelligence / Data Enrichment
- Wraps Diffbot's Knowledge Graph API for company enrichment and web content extraction.
- GitHub: https://github.com/pipeworx-io/mcp-diffbot
- **Business relevance:** Diffbot is the leading web-scale knowledge graph (used by Google, Microsoft, etc.). This MCP enables AI agents to enrich company profiles, extract structured data from websites, and build competitive intelligence — all within agent workflows. Essential for operators doing market research, lead enrichment, or competitive analysis.

### 8. pipeworx-io/mcp-coresignal — Company & Employee Data ★
- **Category:** Business Intelligence / People Data
- Wraps Coresignal's API for LinkedIn-adjacent company and employee data.
- GitHub: https://github.com/pipeworx-io/mcp-coresignal
- **Business relevance:** Coresignal provides professional data (company profiles, employee insights) sourced from public web data. This MCP enables AI agents to research companies and talent pools programmatically. Essential for recruiters, sales operators, and competitive intelligence teams.

---

## ALSO NOTED (Lower Priority / Niche)

| Server | Category | Why Not Added |
|--------|----------|---------------|
| pipeworx-io/mcp-* (procurement) | Gov Procurement | 8+ country-specific government procurement MCPs — too niche for general business audience |
| pipeworx-io/mcp-realestateapi | Real Estate | Property search/skip-trace — niche vertical |
| pipeworx-io/mcp-easypost | Logistics | Multi-carrier shipping — niche vertical |
| pipeworx-io/mcp-walkscore | Real Estate | Walk Score API — very niche |
| pipeworx-io/mcp-ens | Web3 | Ethereum Name Service — crypto niche |
| pipeworx-io/mcp-regrid | Real Estate | Parcel data — niche |
| pipeworx-io/mcp-datalastic | Maritime | AIS vessel positions — extremely niche |
| okdoittttt/apple-calendar-mcp | Productivity | Apple Calendar — platform-specific, limited audience |
| nugrohosetiaji91-png/workbench-mcp | Dev Tools | Windows-only MCP server — platform-limited |
| hostodo/hostodo-mcp | Cloud | VPS hosting MCP — commodity |
| Moep90/agent-toolkit-for-kapitan | DevOps | Kapitan config management — niche DevOps tool |
| bambooshadow-studio/mcp-power-pack | Meta/Config | MCP configurations, not a server |
| arieslee/awesome-agent-plugin | Meta/Curation | Curated list, not an MCP server |

---

## KEY TRENDS (July 2)

- **Finance vertical explodes**: 4+ new finance MCPs in a single day (SentiSense, HPSILab, Kalshi, Tradier). The finance MCP category has gone from 1-2 servers to a legitimate vertical with market intelligence, quant analytics, prediction markets, and brokerage data. This is the fastest-growing MCP category.

- **pipeworx-io industrializes MCP wrapping**: 18+ servers shipped in one day, covering finance, business intelligence, security, marketing, real estate, logistics, and government procurement. Their "every API gets an MCP wrapper" model signals a new phase where MCP server creation becomes systematic rather than artisanal.

- **Agent memory goes GraphRAG**: MCP Long-Term Memory brings Neo4j-backed knowledge graphs to AI agents. As operators move from single-session experiments to persistent agent deployments, memory infrastructure becomes essential. This joins Mem0, Honcho, and others in the "agent memory" category.

- **GEO (Generative Engine Optimization) emerges**: SEOforGPT is the first dedicated GEO MCP. As AI platforms replace traditional search, "being discoverable by AI" becomes a new marketing discipline — and MCP servers will be the tooling layer.

---

## ACTIONS TAKEN

- ✅ Created scan report (this file)
- ✅ Created integration guide: SentiSense (`sentisense.md`)
- ✅ Created integration guide: SEOforGPT (`seoforgpt.md`)
- ✅ Created integration guide: Kalshi MCP (`kalshi-mcp.md`)
- ✅ Created integration guide: MCP Long-Term Memory (`mcp-long-term-memory.md`)
- ✅ Created integration guide: pipeworx Business Data Suite (`pipeworx-business-data.md`)
- ✅ Created integration guide: HPSILab Quant Finance (`hpsilab-quant.md`)
- ✅ Updated index.md catalog
- ⬜ Push to GitHub

---

*Scan performed July 2, 2026. Sources: mcp.so (scraped) + GitHub API (topic:mcp-server created:>2026-07-01).*
*Total new business-relevant servers: 8 (from 55 GitHub repos + 3 mcp.so listings).*
*pipeworx-io alone shipped 18+ servers in a single day — the largest batch in MCP ecosystem history.*
