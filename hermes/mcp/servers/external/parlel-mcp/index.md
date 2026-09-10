---
title: Parlel MCP - Keyless Professional Network Search for Agents
description: "Free keyless remote MCP server over Parlel's public professional network: searchable people, companies, jobs and published watch agents with structured JSON, salary filters, and cursor pagination. Live-verified with 8 tools."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-10
source: mcpservers.org
relevance: ★★
tags: [recruiting, company-search, people-search, jobs, b2b, remote-mcp, keyless]
---

# Parlel MCP

**A professional network with a public, anonymous JSON API** - searchable collections of people, companies, jobs and published watch agents, exposed as 8 typed MCP tools with no key, no sign-up, and no rate-limit negotiation. Live-verified over JSON-RPC during the Sep 10, 2026 sweep (server v1.0.0, keyless, all 8 tools captured).

```
Server type: Remote (hosted, Streamable HTTP, stateless)
Auth: None - anonymous and free
Endpoint: https://api.parlel.com/mcp
Tools: 8, all read-only
Built by: parlel.com
```

## Why This Matters for Operators

Hiring and partner research usually means a subscription to a data provider or scraping pages that fight back. **Parlel exposes its network as plain JSON with the same query parameters on the API and the human pages** - so an agent can search companies by industry, size, location and hiring status, filter open roles by seniority and published compensation, and find people by skill tags, all with structured records that carry stable URLs. Two details matter for agent use: contact details are never in the people list (the field is absent, not empty), and closed job postings keep their URLs with an explicit status field - so agent citations do not 404. The parallel agents collection (published standing searches people run against the open web) is a novel bonus for market research.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_jobs` | Open roles newest-first; q matches title only; filters for remote, seniority, comp_min |
| `get_job` | One role by id with description, skills, pay and hiring company |
| `search_companies` | Companies by name, tagline or industry; size, location and hiring filters |
| `get_company` | One company by handle with open roles inline |
| `search_people` | Profiles by name, headline, company, role and history; skill-tag filters |
| `get_person` | One profile: headline, bio, history, education, skills, recent posts |
| `search_agents` | Published watch agents - standing searches with result previews |
| `get_agent` | One agent by slug: brief, schedule, recent findings with sources |

## Installation

```bash
claude mcp add parlel https://api.parlel.com/mcp
```

No credentials. Filters are AND-ed; text matching is case-insensitive substring with no stemming, so search for the word you expect to appear.

## Configuration

```json
{
  "mcpServers": {
    "parlel": {
      "url": "https://api.parlel.com/mcp"
    }
  }
}
```

Lists return cursor-paginated items; pass next_cursor back as cursor for the next page, null means the end.
