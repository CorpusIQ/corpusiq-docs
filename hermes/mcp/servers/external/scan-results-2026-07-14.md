---
title: "MCP Server Scan Results — July 14, 2026"
description: "Daily MCP server discovery scan from mcp.so/feed. 16 new servers found today (July 14), 5 business-relevant guides created."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-14
---

# MCP Server Scan — July 14, 2026

**Source:** mcp.so/feed (text-stripping extraction — SPA client-rendered, no RSC payloads)
**Date:** July 14, 2026
**Previous scan:** July 13, 2026
**GitHub API:** Unavailable (search rate limit 0/10, flagged as spammy since July 12)
**mcpservers.org:** Unavailable (SolidJS SPA, no server data in initial HTML)
**Firecrawl:** Unavailable (billing down)

## Methodology

mcp.so migrated to a client-rendered React SPA. No server data in initial HTML — all content loaded dynamically. Used text-stripping: curl → strip script/style/HTML tags → extract meaningful text blocks → parse server name + description + submission time from flattened text. Cross-referenced all candidates against the existing catalog (index.md + 70+ guide files + prior scan reports).

## New Servers Found: 16 total, 5 guide-worthy

### Category: Marketing & SEO

| Server | Description | Guide |
|--------|-------------|-------|
| **AI Visibility Analytics** ★ | Brand visibility monitoring across 15+ AI providers (ChatGPT, Perplexity, Gemini, AI Overviews). MCP connector for scans, competitor mentions, and brand tracking. Submitted July 14. | [Guide](/hermes/mcp/servers/external/ai-visibility-analytics/) |
| **Podcast Sponsorship Discovery** ★ | Find brands that sponsor podcasts like yours, reveal the buyer by name and email. Detected from 4M+ podcast sponsorships, updated daily. Submitted July 14. | [Guide](/hermes/mcp/servers/external/podcast-sponsorship-mcp/) |

### Category: DevOps & Infrastructure

| Server | Description | Guide |
|--------|-------------|-------|
| **LLM Observability (LangTrace)** ★ | Open source LLM observability and monitoring. Drop-in proxy for OpenAI, Anthropic, and Gemini with request logging, cost tracking, and agent tracing. Self-host with one Docker command. MIT license. Submitted July 14. | [Guide](/hermes/mcp/servers/external/llm-observability-mcp/) |

### Category: Business Intelligence

| Server | Description | Guide |
|--------|-------------|-------|
| **SaaS & AI Pricing API** ★ | Free REST API and MCP server for verified SaaS, AI, and LLM pricing across 490+ tools. OpenAPI 3.1, no API key required. Submitted July 14. | [Guide](/hermes/mcp/servers/external/saas-pricing-mcp/) |

### Category: Operations & Project Management

| Server | Description | Guide |
|--------|-------------|-------|
| **Project Management for Coding Agents** ★ | Project management for coding agents — bugs, features, sprints, cross-tenant contracts. 71 MCP tools. Submitted July 14. | [Guide](/hermes/mcp/servers/external/coding-agent-pm-mcp/) |

### Category: INDEX-ONLY (business-adjacent but niche or single-use)

| Server | Description |
|--------|-------------|
| **ClassQuill MCP** | Read-only access to tutoring-business data (sessions, students, tutors, invoices, payments, reports) for Claude, Codex, Cursor. Education niche. |
| **Microphone & Speech-to-Text MCP** | Give AI agents the ability to listen — microphone capture and speech-to-text tools for MCP-compatible agents. Agent infrastructure. |
| **Writing Style Checker (WSC)** | Prose linter + AI-slop detector: weasel words, passive voice, hedging, and 190+ research-cited AI tells. Web editor, API, MCP server, CLI, GitHub Action. Content quality. |
| **Persistent Memory for Coding Assistants** | Persistent memory and cross-session learning for AI coding assistants. Cloud-based context management via MCP. Redundant category (we have 3+ memory MCPs already). |
| **Floot** | Build and host full-stack apps with your own AI. Connect the Floot MCP server to Claude, Cursor, ChatGPT, and any MCP client. Development platform. |
| **Quality Clouds Hub** | AI code governance rules injected into Cursor, Claude Code and other MCP clients at generation time. Overlaps with vrules (already catalogued). |
| **Threat Modeling & Security Scanning** | Threat modeling, code, cloud and pipeline scanning, shadow-AI discovery, compliance checks and fixes. Overlaps with SaferAgenticAI (already catalogued). |
| **ShortsMonkey YouTube Outlier Research** | Find YouTube outliers, daily viral Shorts, and analyze video performance. Content strategy tool. |
| **URL → PNG/JPEG/PDF Capture** | URL to image/PDF capture API + MCP server for AI agents. Playwright + Fastify, deploy-ready on Fly.io. Utility for agent screenshots. |

### Category: SKIPPED

| Server | Reason |
|--------|--------|
| **GPU Rental via MCP (x402/Robinhood Chain)** | Crypto/blockchain niche — AI agents rent GPUs & pay in USDG over x402 on Robinhood Chain. Not business-operator relevant. |
| **Government Surplus Auction Data** | Niche government auctions — live listings, sold-price comps, Flip Score resale signals. Too narrow. |
| **TrustyData MCP** | France-only — French address data quality, geocoding & routing (BAN/INSEE/OSM). Regional scope. |

## Previously Documented (July 13 servers — confirmed still in feed)

These 7 servers from the July 13 scan were still visible in the feed (submitted ~17-20h ago):
- AI Localization Agent, HTMLPub MCP, Horizon AI Intelligence, AppAmbit MCP, Bothread, ResolveMesh, Toolzy

## Trends

1. **Content & marketing tools surge:** 4 of 16 new servers target content creation, brand monitoring, or marketing intelligence — AI visibility analytics, podcast sponsorships, writing style checker, YouTube analytics. The MCP ecosystem is expanding beyond developer tooling into marketing operations.

2. **Agent infrastructure maturing:** LLM observability, persistent memory, code governance, and threat modeling all address the "agent in production" problem. Operators deploying AI agents need monitoring, memory, and security — these MCPs fill those gaps.

3. **Pricing intelligence emerges:** The SaaS/AI pricing API with 490+ tools fills a genuine business need — competitive intelligence and market research for operators evaluating tool stacks.

4. **GitHub API remains blocked:** Search endpoint flagged as spammy since July 12. All discovery now depends on mcp.so text-stripping. No repo metadata (stars, creation dates) available for cross-reference. Consider rotating the GitHub token or waiting for rate limit reset.

## Actions Taken

- ✅ 5 integration guides created for business-relevant servers
- ✅ 9 servers added to index.md as INDEX-ONLY entries
- ✅ 3 servers skipped (niche/regional/crypto)
- ✅ Scan report published
- ⚠️ GitHub API enrichment unavailable — guide descriptions derived from mcp.so text only
