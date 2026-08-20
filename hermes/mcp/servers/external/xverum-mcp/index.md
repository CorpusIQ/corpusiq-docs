---
title: "Xverum MCP - People Search Across 750M Professional Profiles"
description: "Hosted remote MCP server for people search and enrichment across 750 million professional profiles: natural-language search by role, seniority, skills, industry, and location, full profile pulls with work history and education, and Next Move Signal job-change prediction for sourcing and prospecting"
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so homepage new arrival (Aug 20)"
relevance: ★★
tags: [people-search, talent-sourcing, prospecting, enrichment, hiring, sales-intelligence, remote-mcp, professional-data]
---

# Xverum MCP

**People search and enrichment for AI agents across 750M professional profiles, with a job-change prediction signal.** Xverum MCP is a hosted remote server with two tools: `xverum_search_people` finds people matching a natural-language description — candidates, prospects, or decision-makers — and `xverum_get_profile` pulls the full profile by id with work history, seniority, and background. Queries are plain English ("find senior data engineers in Amsterdam", "VPs of sales at Series A SaaS companies"), and results carry a Next Move Signal estimating who is likely to change jobs next.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://mcp.xverum.com/mcp
Auth: API key header (x-api-key); OAuth in progress
Tools: 2 (read-only)
License: MIT
Registry: com.xverum/mcp
Built by: Xverum LLC
```

## Why This Matters for Operators

Hiring and prospecting both fail on the same bottleneck: converting a job spec or an ideal-customer profile into a concrete list of reachable people with current, verifiable backgrounds. Xverum turns that into a single agent call — describe the person in plain language, get ranked profiles; ask about one, get the full background. The dataset is a licensed professional-profiles corpus (750M profiles), not a scraping layer, and the server exposes exactly two read-only tools, so there is no write path to abuse.

The Next Move Signal is the operational hook: instead of reaching prospects when they have settled into a role, an agent can prioritize people whose tenure and trajectory suggest imminent movement — standard practice for recruiters, now available to any MCP client.

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| `xverum_search_people` | Ranked profiles matching a natural-language description — role, seniority, skills, industry, location filters |
| `xverum_get_profile` | Full profile for one person by id: work history, education, seniority, background |

Profile data comes from Xverum's licensed dataset; the MCP gateway is a stateless passthrough that never stores the caller's API key.

## Installation

```bash
claude mcp add --transport http xverum https://mcp.xverum.com/mcp \
  --header "x-api-key: YOUR_KEY"
```

```json
{
  "mcpServers": {
    "xverum": {
      "type": "http",
      "url": "https://mcp.xverum.com/mcp",
      "headers": { "x-api-key": "YOUR_KEY" }
    }
  }
}
```

Create a key at xverum.com → Settings → API Keys. Registry-aware clients can add `com.xverum/mcp` by name. There is nothing to self-host.

## Configuration

Per-request API key via the `x-api-key` header — works in any client that supports custom headers (Claude Code, Cline, Cursor). OAuth is in progress per the project's authentication roadmap and will remove the key-pasting step plus unlock OAuth-only clients such as ChatGPT and Claude.ai. The key is validated per request and never stored by the gateway.

## Business Relevance

- **Talent teams** source candidates by role, skills, seniority, and location without boolean-search gymnastics
- **SDR teams** build lead lists of decision-makers with current titles and tenure, prioritized by Next Move Signal
- **Founders** map markets and accounts — who works where, at what seniority — before outreach
- **Agent builders** embed people intelligence into recruiting and prospecting workflows with two simple tools

## Integration with CorpusIQ

Xverum supplies the people layer — who to contact and when they might move; CorpusIQ supplies the account and engagement layer. A natural flow: `xverum_search_people` identifies decision-makers at target accounts, CorpusIQ's HubSpot or LeadConnector connectors verify and store the account record, email handles the outreach thread, and QuickBooks tracks the pipeline once it converts. The combination gives one agent both the person graph and the money graph.

## Limitations

- 2 tools only — search and profile pull; no write, no CRM sync
- API key auth today (OAuth in progress); pricing/limits published on xverum.com, not in the repo
- New listing (Aug 2026), zero-star repository
- Professional-profiles data is licensed third-party data — compliance with data-protection rules (GDPR etc.) rests with the operator using it

## See Also

- [Apollo.io MCP — B2B Contact Data and Sequences](/hermes/mcp/servers/external/apollo-io-mcp/)
- [MisarReach MCP — Outbound Sales and Lead Pipeline for AI Agents](/hermes/mcp/servers/external/misarreach-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
