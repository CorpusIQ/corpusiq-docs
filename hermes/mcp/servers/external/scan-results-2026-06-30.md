---
title: "MCP Server Scan Results — 2026-06-30"
description: "Automated MCP server discovery scan results for June 30, 2026."
---

# MCP Server Directory Scan — June 30, 2026

## SOURCE: GitHub Search (created + pushed June 30, 2026) + mcpservers.org SSR

### Methodology
- GitHub API search: `topic:mcp-server` pushed >2026-06-29 + `mcp server` created >2026-06-29
- mcpservers.org /all page SSR payload extraction
- Cross-referenced against existing catalog (index.md, last updated June 29 PM)
- mcp.so was not used (Cloudflare blocking persists)
- mcpservers.org sitemaps dated June 27 (stale) — only homepage/all-page SSR contained newer data

---

## NEW BUSINESS-RELEVANT SERVERS

### 1. Eleata E-Invoice MCP ★ New
- **Category:** Compliance & Regulatory
- EU e-invoice validation MCP server — Peppol, XRechnung, Factur-X, UBL/CII validation with error code explanations. For AI agents processing EU-compliant electronic invoicing.
- GitHub: github.com/hernaninverso/eleata-einvoice-mcp
- Business relevance: EU e-invoicing mandates are rolling out across member states. Operators in EU markets need AI agents that can validate e-invoices against multiple national formats. First MCP-native EU e-invoice validator.

### 2. NotHumanSearch ★ New
- **Category:** Marketing / GEO
- Search engine for AI agents — ranks sites by agentic readiness (llms.txt, OpenAPI, MCP, ai-plugin). MCP server + REST API + full-text search.
- GitHub: github.com/unitedideas/nothumansearch
- Business relevance: As AI agents become the primary consumers of web content, operators need to understand how AI agents discover and rank their sites. New category: agentic SEO.

### 3. Geoly GEO MCP ★ New
- **Category:** Marketing / GEO
- Remote MCP server + geoly-mcp skill for AI brand visibility (GEO) reporting. Track how AI models mention and recommend brands.
- GitHub: github.com/geoly-ai/codex-plugins
- Business relevance: GEO/AI brand visibility monitoring — competitive with MentionsAPI. Essential for operators investing in AI-engine discoverability.

### 4. APIbase MCP Gateway ★ New
- **Category:** Development & Infrastructure
- Universal MCP gateway — 905 tools, 258 providers. Pay-per-call with x402 USDC on Base. One endpoint for all APIs.
- GitHub: github.com/whiteknightonhorse/APIbase
- Business relevance: The "one MCP to rule them all" approach — operators can access 905 tools through a single gateway instead of managing dozens of individual MCP servers. x402 micropayment model.

### 5. Sparkient MCP ★ New
- **Category:** Analytics & Business Intelligence
- Sub-100ms Decision Intelligence API via MCP. Instant structured decisions for content moderation, fraud detection, ticket triage, and approval workflows.
- mcpservers.org: sparkient/sparkient-mcp-server
- Business relevance: Real-time AI decision-making at sub-100ms latency. Operators running high-volume decision workflows (content moderation, fraud, support triage) can integrate via MCP.

### 6. Agent Warden — MCP Audit Proxy ★ New
- **Category:** Development & Infrastructure / Security
- Local MCP audit proxy — audit logs, policy enforcement, secret scrubbing, and kill switch between Claude Code and any MCP server.
- GitHub: github.com/yli769227-jpg/agent-warden
- Business relevance: Security layer for AI agent operations. Operators running MCP in production need audit trails, policy enforcement, and emergency kill switches.

### 7. SendGrid MCP ★ New
- **Category:** Communication / Marketing
- SendGrid email delivery via MCP. AI agents can send transactional emails, manage templates, and track delivery.
- mcpservers.org: neschadin/sendgrid-mcp
- Business relevance: Email delivery for AI agents — operators can automate transactional emails, marketing sends, and delivery tracking through MCP.

### 8. Google Ads MCP Server ★ New
- **Category:** Advertising
- Standalone MCP server for Google Ads — campaign management, performance data, and ad analytics for AI agents.
- GitHub: github.com/smileCompiler/google-ads-mcp-server
- Business relevance: Lightweight Google Ads MCP for operators who only need ad platform access without full 37-platform suite.

### 9. CarDossier MCP Server ★ New
- **Category:** Finance / Market Intelligence
- MCP Server for CarDossier Poland Market API — real-time used car market data: valuations, price history, liquidity metrics.
- GitHub: github.com/Joyall-au/cardossier-mcp-server
- Business relevance: EU used-car market intelligence — useful for automotive operators, fleet managers, and insurance in the Polish/EU market.

### 10. Bult.ai MCP ★ New
- **Category:** Development & Infrastructure
- Deploy and manage Bult.ai cloud hosting resources — projects, services, GitHub and Docker deployments via MCP.
- mcpservers.org: bultcloud/mcp-server
- Business relevance: Cloud infrastructure management via MCP — operators can deploy and manage hosting resources through AI agents.

### 11. MCPscan — MCP Supply Chain Security ★ New
- **Category:** Development & Infrastructure / Security
- Supply-chain security scanner for MCP servers & Claude Code projects — catch tool-poisoning, command injection, and risky package dependencies.
- GitHub: github.com/glatinone/mcpscan
- Business relevance: MCP security auditing — essential for operators deploying MCP servers in production.

### 12. CreateWorker MCP ★ New
- **Category:** Productivity
- Drive AI workers from Claude Code, Claude Desktop, Cursor, and other MCP clients. AI workforce orchestration.
- GitHub: github.com/CreateWorkerAI/createworker-mcp
- Business relevance: Operators deploying fleets of AI workers can orchestrate them through a single MCP server.

---

## ALSO NOTED (Lower Priority / Niche)

| Server | Category | Why Not Added |
|--------|----------|---------------|
| Kunjani WhatsApp Training MCP | Communication | Niche (WhatsApp gamified training) |
| Dear Agent (AI Diary MCP) | Productivity | Personal use, low operator relevance |
| Open Vision MCP | Content & Research | Commodity vision API wrapper |
| FemTech Radar MCP | Market Intelligence | Very niche (women's health focus) |
| SecOps Toolkit MCP | Security | Niche (defensive security helpers) |
| Kobel MCP | Security | Windows-only file permission gateway |
| AgenticBooks MCP | Content | Niche (self-building books concept) |
| Fantasy MCP Server | Entertainment | Zero business relevance |
| JuicedResume MCP | Productivity | Niche (single-purpose resume tool) |

---

## KEY TRENDS (June 30, 2026)

- **EU Compliance MCPs emerging**: Eleata E-Invoice signals regulatory compliance becoming an MCP category — Peppol/XRechnung/Factur-X are mandatory across EU
- **AI agent search optimization**: NotHumanSearch + Geoly show that "agentic SEO" is becoming its own category — operators need to optimize for AI agent discovery, not just human search
- **MCP security layer forming**: Agent Warden + MCPscan show security infrastructure for MCP is maturing — audit proxies, supply chain scanning, policy enforcement
- **Universal gateways consolidating**: APIbase (905 tools, 1 endpoint) signals MCP gateway consolidation trend
- **Real-time decision intelligence**: Sparkient (sub-100ms) shows MCP moving into latency-sensitive decision workflows
- **Vertical MCPs continue**: CarDossier (used cars), Eleata (e-invoicing) — industry-specific MCPs keep emerging

---

*Scan performed June 30, 2026. Sources: GitHub API (topic:mcp-server + created/pushed filters), mcpservers.org /all page SSR.*
*Note: mcp.so was unavailable (Cloudflare). mcpservers.org sitemaps dated June 27 (stale) — new data extracted from /all page SSR.*
