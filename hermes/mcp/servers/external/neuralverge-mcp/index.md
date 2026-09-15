---
title: "NeuralVerge MCP - B2B People and Company Data"
description: "B2B people and company data for prospecting: LinkedIn profile and employee search, email finding and validation, phone enrichment and Crunchbase profiles over one HTTP endpoint."
category: Sales & Outreach
stars: n/a (no public repo)
added: 2026-09-03
source: mcpservers.org
relevance: ★★★
tags: [sales-intelligence, lead-enrichment, email-finder, linkedin, company-data, prospecting, remote-mcp]
---

# NeuralVerge MCP

**Remote MCP server (Streamable HTTP, bearer token)** - NeuralVerge exposes its full B2B data API as MCP tools: person and company profile lookup, LinkedIn people and company search, employee search, email finding and validation, phone enrichment, Crunchbase profiles, plus web search, page extraction and async deep research.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer token (same as the REST API)
Endpoint: https://api.neuralverge.ai/functions/v1/mcp-server
Tools: 16 (AI Research, AI Extract, Search, LinkedIn, Email and Phone, Company)
Pricing: token-based (402 Payment Required surfaces usage limits)
Category: Sales & Outreach
Built by: NeuralVerge (docs.neuralverge.ai/mcp-server)
```

## Why This Matters for Operators

Outbound data work is a patchwork: one vendor for LinkedIn, one for email verification, one for enrichment, each with its own API and billing. NeuralVerge collapses the stack into one stateless HTTP endpoint where every REST capability is a thin 1:1 MCP tool.

**The error semantics are built for agents:** a missing or invalid token fails the whole request with 401 before any tool runs, while per-call failures (invalid parameters, 402 Payment Required for usage limits, upstream failures) come back inside the tool result with isError true, so the calling model sees and reacts to them instead of the whole request dying. The async run_research workflow returns a session_id to poll with get_session_status - designed for agent loops, not human dashboards.

## Tools & Capabilities

Sixteen tools across four groups, documented with exact names:

| Group | Tools |
|---|---|
| AI Research | run_research (async, returns session_id), get_session_status |
| AI Extract | run_extract (page URL to structured data per instructions or schema) |
| Search | run_search (synchronous ranked results) |
| LinkedIn | run_linkedin_email, run_linkedin_domain, run_linkedin_company_search, run_linkedin_people_search, run_linkedin_company_employee |
| Email and Phone | run_email_enrichment, run_email_validation, run_email_finder, run_phone_enrichment, run_phone_enrichment_us |
| Company | run_crunchbase_company |

## Installation

```bash
claude mcp add --transport http neuralverge https://api.neuralverge.ai/functions/v1/mcp-server
```

Then attach the NeuralVerge access token in the Authorization header (Bearer scheme) on that server config, per the vendor's Claude Code walkthrough.

## Configuration

```json
{
  "mcpServers": {
    "neuralverge": {
      "type": "http",
      "url": "https://api.neuralverge.ai/functions/v1/mcp-server"
    }
  }
}
```

Two request headers matter: the access token in the Authorization header (Bearer scheme - the same token as the REST API), and Accept set to application/json, text/event-stream. See the vendor's Authentication page for minting.

## Business Relevance

- **SDRs** find and validate prospect emails and phones without leaving the agent loop
- **Recruiters** run employee and people searches with free-text and advanced filters
- **RevOps teams** enrich company and Crunchbase data ahead of CRM sync

## Integration with CorpusIQ

NeuralVerge feeds the top of the funnel while CorpusIQ tracks what happens after: a composed workflow enriches an inbound lead (NeuralVerge email validation, company lookup, employee map), pushes it into the HubSpot connector for tracking, and CorpusIQ's Stripe and GA4 connectors later close the loop on whether that lead converted and what it was worth. NeuralVerge's run_research also covers the account-research step that CorpusIQ's read-only business connectors intentionally do not.

## Limitations

- Paid token model - costs scale with enrichment volume
- Usage limits surface as 402 Payment Required inside tool results
- Cloud-only, no self-host option
- No published free tier details beyond the REST API's own limits

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Xverum MCP - People Search Across 750M Professional Profiles](/docs/hermes/mcp/servers/external/xverum-mcp)
- [StackScope MCP - Technographic Sales Intelligence for Agents](/docs/hermes/mcp/servers/external/stackscope-mcp)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/docs/hermes/mcp/servers/external/worklittle-jobs)
