---
title: "MCP Discovery Sweep — August 20, 2026 (Evening)"
date: 2026-08-20
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso GitHub issues filed Aug 20 10:44 through 16:42 UTC plus mcpservers.org /all JSON-LD page 1 and both directory homepages; 7 catalogued with guides, 4 catalog entries, 15+ skipped"
---

# MCP Discovery Sweep — August 20, 2026 (Evening)

- **Cutoff:** prior sweep evaluated through issue #3655 (Aug 20 09:46 UTC)
- **Fresh window:** issues #3656–#3663, mcpservers.org /all JSON-LD (30 newest), both homepages
- **Result:** 7 catalogued with guides, 4 catalog entries, 15+ skipped

## Catalogued (7 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Upfirst MCP (AI phone receptionist for small businesses: call transcripts, knowledge-gap audits, greeting/skill/transfer-rule configuration, schedules; hosted remote, in-app connector flow; upfirst.ai) | n/a | Communication | mcpservers.org /all |
| Atoa MCP (UK Pay by Bank + card payments: process/capture/cancel payments, customer management, refunds, transactions, webhooks, bank feeds, approvals; endpoint mcp.atoa.me/mcp, Bearer SDK token + X-Atoa-Env; FCA authorised, PCI DSS, ISO 27001, SOC 2) | n/a | Commerce & E-Commerce | mcpservers.org /all |
| LicenseGuard MCP (dependency license verdicts against distribution model: single-dep check, manifest/lockfile audit with transitive deps, clause-cited explainer; hosted no-auth at license-guard.rcc-aoki.workers.dev/mcp + local stdio Docker; Apache-2.0, Glama A/A) | n/a | Compliance & Regulatory | GH issue #3658 |
| AdMapix MCP (competitor ad creative intelligence: search_creatives by keyword/advertiser/category/ad copy, format/country/date filters, sort by first seen or estimated impressions; stdio via uvx, ADMAPIX_API_KEY; PyPI v1.0.0) | n/a | Marketing | GH issue #3663 |
| Simplepages MCP (landing pages built/edited from chat with visitors, leads and revenue readout; hosted remote, OAuth connect flow, per-workspace scoping; simplepages.ai) | n/a | Marketing | mcpservers.org /all |
| Giggal.ai MCP (email verification with catch-all/accept-all/SEG detection, credit and history lookup; hosted at mcp.giggal.ai/mcp, API key verify:read) | n/a | Marketing | mcpservers.org /all |
| Opportunity Atlas MCP (verified NE Ohio construction opportunity intelligence: free scout_capabilities + scout_preview, registered-agent full surface; Supabase-hosted remote, hashed 90-day keys, 20 req/min 100/day caps) | n/a | Sales & Outreach | mcpservers.org /all |

## Catalog entries (4, no guides)

| Server | Category | Source |
|---|---|---|
| Magnificent Jobs MCP (semantic search over 3.5M+ live US job postings scraped hourly from company ATS; free, read-only, no key, `npx magnificentjobs`) | Sales & Outreach | mcpservers.org /all |
| DPF MCP (NL data ingestion/transformation/analytics platform with revocable AWS IAM-role access and SFTP keypair connections; dpf-it.com) | Analytics & Business Intelligence | mcpservers.org /all |
| Teachfluence MCP (254 tools across 29 families for online educators: courses, community, forms, CRM, support, revenue; OAuth 2.1, per-org default-deny, audit row per call) | Productivity | mcpservers.org /all |
| Terno MCP (database intelligence layer for warehouse-scale DBs with strict access controls and LLM-optimized schema context; hosted OAuth or Django-embedded) | Analytics & Business Intelligence | mcpservers.org /all |

## Verification performed

- LicenseGuard: README parsed (3 tools, ecosystems, lockfile table, incomplete-scan-never-clean guarantee), hosted endpoint documented, Glama A/A confirmed in issue body
- AdMapix: repo live (fly0pants/admapix), README parsed for features/filters/sort, PyPI admapix-mcp v1.0.0 verified
- Atoa: first-party docs at docs.atoa.me/mcp-server — endpoint, Bearer + X-Atoa-Env headers, tool names recovered from embedded docs data (process_payment, capture_payment, cancel_payment, create/get/update/delete_customer, list_customers, initiate_refund, cancel_refund, get_transactions, create/delete_webhook)
- Upfirst, Simplepages, Giggal, Opportunity Atlas, Magnificent Jobs, DPF, Teachfluence, Terno: mcpservers.org detail pages parsed for description, auth, and tool surface
- All candidates cross-referenced against catalog index.md and the sweeps/ archive — zero prior mentions

## Skipped (evaluated, consistent with prior decisions)

- #3656 Proactive Vault — personal CRM for macOS; GitHub repo 404 at evaluation time (not consumable)
- #3659 Wondel Skills — skill-loader dev tool
- #3660 AI Developer Toolkit — AI-dev guide search (dev tool)
- #3661 2anki — consumer Anki-deck converter
- #3662 Fine Structure — full-stack app builder (dev)
- /all slugs: Clio for Creatio (platform dev tool), GlianaAI (x402 model-gateway infra), RiverScript (transcript-fetch niche), MarkIt (personal bookmarking), FaceSign (step-up verification dev flows), POB (Path of Exile gaming), Chamnan (Claude Code security plugin), AST (TypeScript dev), AgentTrust (XRPL blockchain referee), Agentic HIL (embedded hardware dev), Seedfast (synthetic test data), HTTP 402 AI Tollbooth (x402 infra), QR Planet (QR-code design utility)
- Repeats already catalogued or previously skipped: Booking.com Hotel Search (FlightPowers thin surface), Football Charts (sports precedent), 60fps, MindMap AI, Vital Care Finder, CSOAI GSPC, Waqi, Bitroad, 3gpp-mcp

## Catalog state

- Before: 280 servers, 170 guides
- After: 291 servers, 177 guides
- Next sweep cutoff: issue #3663
