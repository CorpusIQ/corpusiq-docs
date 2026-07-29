---
title: "Sweep Report — July 29, 2026 (Afternoon)"
date: 2026-07-29
sources: mcpservers.org /all SSR, sitemaps 1-6, mcp.so
status: complete
---

# MCP Directory Sweep — July 29, 2026 (Afternoon)

## Summary

Afternoon sweep of mcpservers.org JSON-LD data (30 newest servers via SSR), sitemap lastmod dates (July 29 entries), and mcp.so /servers page. Firecrawl + web_extract DOWN — used curl + SSR data extraction (proven fallback).

**Result:** 3 business-critical servers discovered (all absent from catalog), 4 secondary finds noted. Total mcpservers.org now at 10,377 servers (up from ~10,360 this morning).

---

## ★★★ Business-Critical (3 Guides Written)

### QuickBooks MCP Server ★★★ — July 29 afternoon
**First comprehensive QuickBooks MCP — 550+ tools, OAuth2, hosted by datagrout.ai.** AI agents connect to QuickBooks Online for invoices, bills, reports, and inventory. Write operations disabled by default (opt-in per integration). This fills the single biggest gap in accounting MCP — until now, QuickBooks access required Laravel community packages or read-only connectors. `datagrout.ai/integrations/quickbooks-mcp-server` · [Guide →](/hermes/mcp/servers/external/quickbooks-mcp/)

### Oracle MCP Server ★★★ — July 29 afternoon
**First Oracle Fusion Cloud MCP — 1,000+ tools, OAuth2, hosted by datagrout.ai.** AI agents connect to Oracle's ERP: Financials, Procurement, Inventory, Suppliers, Tax, and Workforce. Write operations disabled by default. The first enterprise-grade Oracle MCP — previously, Oracle access required custom REST/SOAP integrations or middleware like Boomi/MuleSoft. `datagrout.ai/integrations/oracle-mcp-server` · [Guide →](/hermes/mcp/servers/external/oracle-mcp/)

### DealMachine MCP ★★ — July 29 afternoon
**Real estate property intelligence MCP — 17 command groups, OAuth 2.1 + API key.** AI agents search properties, look up owners, skip-trace contacts, analyze comps, and manage lead lists. First major real estate data platform to ship an MCP server. Self-contained Commander.js CLI with zero internal dependencies — communicates entirely through DealMachine's public REST API. `github.com/DealMachine/dealmachine-cli` · [Guide →](/hermes/mcp/servers/external/dealmachine-mcp/)

---

## ★★ Secondary Finds (Noted, No Guides Yet)

| Server | Source | Category | Notes |
|--------|--------|----------|-------|
| SMKlog Parcel Quotes | mcpservers.org /all | Shipping/Logistics | Live USPS, UPS, FedEx rates from plain-text descriptions. E-commerce operators. `smklog.com/api` |
| MaxStat MCP | mcpservers.org /all | Marketing | Messenger analytics — channel/post search, audience growth, engagement tracking. Official from `fbmdata/maxstat-mcp`. `github.com/fbmdata/maxstat-mcp` |
| XiaoFlow MCP | mcpservers.org /all | Marketing/SEO | AI SEO Tools + Etsy Market Intelligence. Official MCP. `github.com/xiaoq-in/xiaoflow-mcp` |
| SotaProxy MCP | mcpservers.org /all | Web Scraping | Buy and manage proxies (residential, ISP, IPv4/IPv6, mobile) in plain language. Prepaid balance. `github.com/SotaProxy/sotaproxy-mcp` |

---

## ★ Noted (No Guides)

| Server | Notes |
|--------|-------|
| Profitelligence MCP | Business intelligence/profitability analytics. `github.com/profitelligence/profitelligence-mcp-server` |
| Lightrun MCP | Production debugging platform. `github.com/lightrun-platform/lightrun-mcp-server` |
| Compeller MCP | Needs research — mcpservers.org promoted server |
| On-Page.ai SEO MCP | SEO optimization — niche, overlaps with existing Ahrefs/Apify |
| Open Medici MCP | Public fellowship and grant search. Read-only remote. `openmedici.com` |
| TDPro | Stock gapper scanner (Warrior Trading methodology). Finance/niche. |
| openagentemail | Self-hosted email for AI agents with OTP extraction. `github.com/openagentemail/openagentemail` |

---

## Already Covered / Developer Tools / Skipped

- Various memory MCPs (Vision Memory, State Memory, Toon Memory, Simple Memory, Wuniq) — crowded category, no standout differentiation
- AIQUAA QA suite (3 servers) — testing/QA tools, developer-focused
- mcp-expect — Jest-style assertions for MCP testing, developer tool
- restic-defensive-mcp — backup repository inspection, devops
- Solidworks MCP — CAD engineering, not business-ops
- airquality-tr-mcp — Turkey air quality data, regional/niche
- grand-lyon-mcp — Lyon France open data, regional
- UIZZE — UI/design review tool, developer-focused

---

## Notable Ecosystem Trend

**Datagrout is becoming the "enterprise ERP connector factory" for MCP.** In one day, they shipped both QuickBooks (550+ tools) and Oracle Fusion Cloud (1,000+ tools) MCP servers with consistent security models (OAuth2, writes-off-by-default, opt-in write capabilities). This is the same playbook as CData's MCP connectors but focused on the top-tier ERP/accounting platforms rather than long-tail APIs. Expect Sage, NetSuite, and SAP Business One MCPs from datagrout next.

The gap between "enterprise software" and "AI agents" is closing faster than anyone predicted in January. By end of 2026, every major ERP/accounting platform will have at least one MCP server — whether official or community-maintained.

---

## Sources Used

- ✅ mcpservers.org JSON-LD + SSR data: extracted from /all page (30 newest)
- ✅ mcpservers.org sitemaps 1-6: curl + grep for July 29 lastmod entries
- ✅ mcpservers.org priority sitemap: curl + grep
- ✅ mcp.so /servers: SSR extraction attempted (limited data)
- ❌ Firecrawl API: not configured
- ❌ web_extract: not configured
- ❌ web_search: not configured

---

## Stats

| Metric | Value |
|--------|-------|
| mcpservers.org total servers | 10,377 (up from ~10,360 morning) |
| Newest 30 scanned | 30 (from /all page) |
| Business-critical new finds | 3 (QuickBooks, Oracle, DealMachine) |
| Secondary finds | 4 (SMKlog, MaxStat, XiaoFlow, SotaProxy) |
| Guides written | 3 |
| Total catalog after sweep | 278 entries (+3 from morning's 275) |
