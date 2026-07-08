---
title: "MCP Server Discovery — July 2, 2026 (Afternoon Update)"
description: "Second daily sweep of mcp.so and mcpservers.org. 14 new business-relevant MCP servers across ERP, ecommerce, legal, billing, supply chain, agent infrastructure, and content categories."
category: mcp
tags: [mcp-servers, daily-scan, july-2026]
last_updated: 2026-07-08
---

# MCP Server Discovery — July 2, 2026 (Afternoon Update)

**Source:** mcp.so/feed (Next.js RSC payload extraction), mcpservers.org  
**Method:** curl + Python regex (`__next_f.push` extraction)  
**Date:** July 2, 2026 afternoon sweep  
**Prior scan:** [July 2 morning scan](/hermes/mcp/servers/external/scan-results-2026-07-02/)

## Summary

| Metric | Count |
|--------|-------|
| Total servers extracted from mcp.so | 25 |
| Already catalogued (prior scans/guides) | 2 |
| Non-business (dev tools, niche) | 9 |
| **New business-relevant** | **14** |

## New Servers Found

### ERP & Business Systems

| Server | Description | Source |
|--------|-------------|--------|
| **Odoo MCP** | AI layer for Odoo ERP v16+ — zero Odoo-side setup, full accounting/inventory/CRM access | `tuanle96/mcp-odoo` |
| **BillingServ MCP** | Customer, invoice, and order lookup via BillingServ API | `BillingServ/MCP` |

### Ecommerce & Retail

| Server | Description | Source |
|--------|-------------|--------|
| **Launch Fast MCP** | Amazon FBA product research, seller analytics, Brand Analytics, ads diagnostics | `BlockchainHB/launchfast-mcp` |
| **AppSigma App Store Data MCP** | Full public App Store search — rankings, reviews, ASO keywords, sponsored slots | `appsigma.io` |

### Supply Chain & Logistics

| Server | Description | Source |
|--------|-------------|--------|
| **Container Tracking MCP** | Ocean container tracking across 200+ shipping lines — live milestones, vessel positions | `lxxmng/container-tracking-mcp` |

### Marketing & Content

| Server | Description | Source |
|--------|-------------|--------|
| **NaturalMelo MCP** | AI content detection — naturalness scoring, flagged AI-template patterns | `carter-wzq/naturalmelo-mcp` |
| **Userbrain MCP** | User testing data exploration — summarize feedback, uncover UX insights from test sessions | `userbrain.com` |

### Business Intelligence & Procurement

| Server | Description | Source |
|--------|-------------|--------|
| **Booyah Index MCP** | Directory of 3,520 local businesses across 14 Southeast Asian cities | `sarapab-th/booyah-index-mcp` |
| **qlows MCP** | Real-time tender/RFP search across 35 WTO-GPA countries (US, EU, Australia) | `getqlows/qlows-mcp` |

### Legal & Compliance

| Server | Description | Source |
|--------|-------------|--------|
| **Kvasir Legal MCP** | Verifiable German, Bavarian & EU law — canonical objects with provenance and pinpoint citations | `kvasir.legal` |
| **SaferAgenticAI MCP** | AI safety framework for agentic coding assistants — governance guardrails over MCP | `NellInc/SaferAgenticAI` |

### Agent Infrastructure

| Server | Description | Source |
|--------|-------------|--------|
| **SPM — Structured Project Memory** | Project-scoped remote MCP connector for agent memory — context packs, provenance, access control | `getspm/spm-agent-connectors` |

### Finance & Crypto

| Server | Description | Source |
|--------|-------------|--------|
| **AICryptoVault MCP** | MCP-native treasury infrastructure — agent-managed crypto wallet operations | `browtastic/cloudaiwallet-mcp-servers` |

### DevOps & Monitoring

| Server | Description | Source |
|--------|-------------|--------|
| **Drumbeats MCP** | Cron/heartbeat and uptime monitoring from any AI client — incident triage, status pages | `drumbeats-io/mcp` |

## Trends

- **ERP connectors expanding**: Odoo joins the ERP MCP ecosystem alongside existing connectors (QuickBooks via CorpusIQ). Free, no-Odoo-side-setup approach lowers barrier significantly.
- **Supply chain goes MCP**: Container tracking is the first logistics/shipping MCP server — opens a new vertical.
- **Agent memory infrastructure**: SPM joins existing memory solutions (Honcho, GBrain, mcp-long-term-memory) with a project-scoped, provenance-focused approach.
- **Legal AI grounding**: Kvasir represents growing trend of jurisdiction-specific legal MCP servers with verifiable provenance.
- **Tender/procurement**: qlows is the first procurement-focused MCP covering WTO-GPA zone — new business vertical.

## Actions Taken

- 14 new integration guides created (see individual `.md` files in this directory)
- Index updated with new entries under appropriate category sections
- Combined guides: `pipeworx-business-data.md` style for related suites where applicable

## Non-Business Servers (Not Catalogued)

- `tidewave-phoenix` — Elixir dev tooling
- `tidewave-rails` — Rails dev tooling  
- `jsonaut` — JSON repair utility
- `imageat-ai` — Image/video generation (media tooling)
- `well` — No description, unclear purpose
- `infranode` — German city open data (niche)
- `remodeleriq` — Home remodeling bids (niche consumer)
- `naturalmelo` — Duplicate of naturalmelo-mcp
- `safer-agentic-ai-framework` — Duplicate of saferagenticai-mcp
