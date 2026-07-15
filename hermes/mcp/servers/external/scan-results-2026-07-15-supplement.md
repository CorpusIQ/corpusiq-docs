---
title: "MCP Server Scan Supplement — July 15, 2026 (Evening)"
description: "Supplemental mcp.so feed scan. 7 new servers found since morning scan, 2 business-relevant guides created."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-15
---

# MCP Server Scan Supplement — July 15, 2026 (Evening)

**Source:** mcp.so/feed (mcp.so not scanned in morning cycle — supplemental coverage)
**Date:** July 15, 2026 (evening)
**Previous scan:** July 15, 2026 (morning — 11 servers from mcpservers.org sitemap)

## Methodology

The morning July 15 scan used mcpservers.org sitemap extraction only (mcp.so deferred due to cron limitations). This supplement covers the mcp.so feed — servers submitted July 14-15 that weren't captured by the mcpservers.org sitemap. mcp.so returned full structured data (RSC payloads) — extraction confirmed via `$R` array parsing.

## New Since Morning Scan: 7 servers, 2 guides created

### Guide-Worthy (Business-Relevant)

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **Lawstronaut** ★ | mcp.so | Millions of official legal and regulatory source documents from 155+ jurisdictions via MCP. Structured legal research. By Lawstronaut-FZCO. Submitted July 15. | [Guide](/hermes/mcp/servers/external/lawstronaut-mcp/) |
| **Unstructured Transform MCP** ★ | mcp.so | Document processing platform connector — parse PDFs, CSVs, and documents into structured AI-ready data. Remote MCP transport. By Unstructured / Chris Maddock. Submitted July 15. | [Guide](/hermes/mcp/servers/external/unstructured-transform-mcp/) |

### INDEX-ONLY (Niche or Developer-Focused)

| Server | Source | Description |
|--------|--------|-------------|
| **APIMart** | mcp.so | Unified AI API platform — access GPT-5, Claude 4.5, Gemini, Sora 2 & Flux.1 through one OpenAI-compatible key. Client listing (not MCP server). |
| **Sitespeak Claude Plugin** | mcp.so | Manage SiteSpeakAI chatbot from Claude Code — MCP server for chatbot optimization. Narrow platform tool. |
| **Linkly Link Shortener** | mcp.so | URL shortener with geo redirects, click & conversion tracking, link rotators. Commodity utility — too narrow for business catalog. |
| **SVGator** | mcp.so | SVG animation from AI assistants. Design tool — not business-operator relevant. |
| **Gocosmik** | mcp.so | MCP client at gocosmik.com. Client listing (not MCP server). |

## Previously Covered

These mcp.so feed entries were already documented in the morning July 15 scan or July 14 scans:
- Rankbits → Already covered as AI Visibility Analytics (July 14 scan)
- ClassQuill → Already INDEX-ONLY (July 14 scan)
- WeClaw → Consumer AI, previously skipped

## Trends (Supplemental)

1. **Legal MCPs diversifying:** Lawstronaut joins Kvasir Legal, GoldLegal, and EU Textile Sustainability in the legal MCP category. The category is evolving from single-jurisdiction tools (EU-only Kvasir) to global coverage (155+ jurisdictions with Lawstronaut). Watch for the "universal legal MCP" race.

2. **Document intelligence consolidating:** Unstructured's Transform MCP represents a major document-processing platform entering the MCP ecosystem. Unlike standalone PDF parsers, Unstructured brings enterprise document processing infrastructure — this signals platform-grade tools entering MCP, not just indie developer projects.

3. **Infrastructure MCPs emerging:** APIMart (unified AI API) represents a new subcategory — MCP-native API aggregation. Not an MCP server itself but a client/infrastructure layer. Watch for more API gateway/aggregation tools appearing in MCP directories.

4. **Submission velocity increasing:** 7 new servers submitted to mcp.so in ~24 hours (July 14-15), suggesting the mcp.so feed is capturing 5-10 new submissions per day — consistent with mcpservers.org sitemap velocity.

## Actions Taken

- ✅ 2 integration guides created: Lawstronaut, Unstructured Transform MCP
- ✅ 5 INDEX-ONLY entries documented
- ✅ index.md updated with new entries
- ✅ Scan supplement report published
- ⚠️ GitHub API still rate-limited — repo metadata unavailable for enrichment

---

*Next scan: July 16, 2026. Continue dual-source approach (mcpservers.org sitemap + mcp.so feed).*
