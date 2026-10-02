---
title: "Crawdar MCP - Qualified Prospect Research for Agents"
description: "Crawdar MCP gives an agent qualified prospects instead of raw pages: natural-language and structured business search with criterion-level match explanations, a classified public contact route and supporting sources for every result, plus durable async lead-search jobs with progress, export, retry and cancel. Remote MCP, keyless probe verified."
category: Lead Generation & Web Scraping
stars: 0
added: 2026-09-07
source: mcpservers.org /all
relevance: ★★★
tags: [prospecting, lead-generation, company-research, business-search, remote-mcp]
---

# Crawdar MCP - Qualified Prospect Research for Agents

**Remote MCP server (Streamable HTTP)** - Crawdar converts "find companies that match this" into qualified prospects: each result carries why the company matches, criterion-level decisions, a classified public contact route and the supporting sources. A versioned JSON API and a browser-capable interface sit alongside the MCP surface.

```
Server type: Remote (Streamable HTTP)
Auth: Tool surface served anonymously (probe-verified); search capacity via the vendor's plans
Endpoint: https://crawdar.com/api/mcp (probe-verified live; 9 tools)
Tools: 9 (research_businesses, search_businesses, sandbox_businesses, lead-search job lifecycle, explain_crawdar)
Pricing: Plans at crawdar.com
Category: Lead Generation & Web Scraping
Built by: Crawdar (crawdar.com)
```

## Why This Matters for Operators

Prospecting tooling falls into two bad shapes: raw page scrapes the agent must re-interpret, and closed CRMs that hide why a lead was surfaced. Crawdar sits in the middle: every result names the match reasons and cites the sources, so the operator can audit the recommendation instead of trusting a black box - and the sandbox tool lets agent loops be tested on deterministic fictional businesses before touching live capacity.

**The durable job model is the workflow win: start_lead_search returns a private job with progress, export, retry and cancel URLs, so long searches survive the conversation instead of blocking the agent call.**

## Tools & Capabilities

| Tool | What it does |
|---|---|
| research_businesses | One-call natural-language search with compact or full output |
| search_businesses | Structured search with explicit target, geography, qualifier and field selection |
| sandbox_businesses | Deterministic fictional results for contract and agent-loop testing |
| start_lead_search | Creates a private async search job with progress, status, export, retry and cancel URLs |
| get_lead_search | Reads job progress or cursor-paginated result pages |
| refine_lead_search | Creates a new job by changing the brief or criteria, preserving the original |
| retry_lead_search | Replaces a failed or window-expired job; the original stays available for audit |
| cancel_lead_search | Cancels a queued or running job; completed and failed jobs remain immutable |
| explain_crawdar | Returns result semantics, limits, interface URLs and safe operating guidance |

## Installation

Point any Streamable HTTP client at the endpoint. Start with sandbox_businesses to validate schemas and agent loops without consuming live search capacity.

```json
{
  "mcpServers": {
    "crawdar": {
      "type": "http",
      "url": "https://crawdar.com/api/mcp"
    }
  }
}
```

## Configuration

The probe served the full 9-tool surface anonymously; live search capacity is governed by the operator's Crawdar plan. The explain_crawdar tool documents result semantics and limits from inside the client.

## Business Relevance

- **Sales teams** replace manual list-building with sourced, reason-carrying prospect searches.
- **RevOps teams** run durable async lead searches that survive the conversation.
- **Agencies** test prospect pipelines in the sandbox before spending live capacity.
- **Founders** get qualified prospects with contact routes for first outbound motion.

## Integration with CorpusIQ

Crawdar finds the prospects; CorpusIQ verifies the business. A composed workflow: the agent pulls qualified prospects from Crawdar, enriches the shortlist through CorpusIQ's business data connectors, and tracks pipeline-to-revenue through the CRM and Stripe data - sourcing, qualification and attribution in one loop.

## Limitations

- Brand new listing (mcpservers.org /all, Sep 2026); no public repository located, stars n/a.
- Result quality and capacity depend on the Crawdar plan tier.
- Contact routes are public-facing classifications, not personal-contact data.
- The sandbox is deterministic but fictional; it validates loops, not real data quality.

## See Also

- [Leadgen MCP - Romanian Business Registry & Contact Enrichment](/hermes/mcp/servers/external/leadgen-mcp)
- [registry-mcp - Company Registry Data for AI Agents](/hermes/mcp/servers/external/registry-mcp)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/hermes/mcp/servers/external/worklittle-jobs)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
