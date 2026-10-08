---
title: "Level MCP - AI-Rated Job Board for Agents"
description: "An AI job board over MCP: search live listings rated by how central AI is to the role, plus market stats and company rankings."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-07
source: "chatmcp/mcpso issue #4918 (Oct 7, 2026 evening sweep)"
relevance: ★★
tags: [jobs, careers, labor-market, ai-adoption, market-data]
---

# Level MCP

**Keyless MCP server over Level (jobsbylevel.com), an AI job board that rates every listing by how central AI is to the role** - from Little AI (AI Level 1) to Builds AI (AI Level 4). Search listings, read one in detail, pull market statistics, list companies ranked by AI level, and read the level definitions. Free, read-only, no sign-in.

```
Server type: Remote (Streamable HTTP at https://jobsbylevel.com/mcp)
Auth: None (free; rate-limited per IP)
Registry: com.jobsbylevel/level-jobs
Docs: https://jobsbylevel.com/developers (server card at https://jobsbylevel.com/.well-known/mcp/server-card.json)
Tools: search_jobs, latest_ai_jobs, get_job, market_stats, list_companies_by_ai_level, get_level_definitions
Category: Business Operations
Built by: Level (jobsbylevel.com)
```

## Why This Matters for Operators

Hiring is where AI appetite quietly becomes a business decision, and job data usually answers the wrong question: how many roles mention AI. Level rates each role on how central AI actually is - a support role that uses AI tools ranks below an engineer who builds AI systems. For an operator, that is a market read: see how competitors staff AI work, what titles and cities they post, and what the AI-intensity mix looks like by company. For job seekers, it is a filter that cuts the noise in both directions.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `search_jobs` | free-text search (title, tool, skill or company) with filters for AI level range, remote, city, company and posting age; 20 results per page, ranked by relevance with stemming |
| `latest_ai_jobs` | newest listings by AI level |
| `get_job` | one listing in full |
| `market_stats` | aggregate market statistics from the listings |
| `list_companies_by_ai_level` | companies ranked by AI level |
| `get_level_definitions` | the Little AI (1) to Builds AI (4) ladder explained |

Every result links back to its canonical page on jobsbylevel.com; the search tool deliberately never returns a direct link to the employer's ATS.

## Installation

```json
{
  "mcpServers": {
    "level-jobs": { "url": "https://jobsbylevel.com/mcp" }
  }
}
```

Any Streamable HTTP client works: Claude, ChatGPT, Cursor, Codex or another. No key, no account.

## Business Relevance

- **Founders and hiring managers:** size the AI-skill market before writing a role - which titles exist, at what AI intensity, in which cities, at which companies.
- **Market researchers:** use market stats and company rankings as a free, keyless signal of where AI work is actually being staffed.
- **Job seekers:** filter for roles by how central AI is, in either direction - roles that build AI, or roles that just use it.

## Integration with CorpusIQ

CorpusIQ answers questions about your own business - revenue, customers, pipeline - consistently across AI clients. Level answers questions about the market around you: pull your hiring plan context from CorpusIQ, then check what the market looks like for the same roles on Level, in one conversation.

## Limitations

- Read-only, and free: rate-limited per IP, no SLA.
- Results link back to jobsbylevel.com pages by design, not employer ATS links.
- Coverage is the Level job board itself; it is a market sample, not every posting everywhere.
- Brand new listing - no third-party track record yet.

## FAQ

### Does it need an API key or account?

No. The server is keyless and read-only; it is rate-limited per IP.

### What are the AI levels?

A four-step ladder from Little AI (AI Level 1, minimal AI involvement) to Builds AI (AI Level 4, the role builds AI systems). The `get_level_definitions` tool returns the full explanation.

### Can the agent apply to jobs?

No - every tool is read-only, and results link to jobsbylevel.com pages for a human to open.

### Is it limited to tech jobs?

It is limited to what is posted on Level, with AI centrality as the rating axis rather than a functional filter; search covers title, tool, skill and company across the board.

## See Also

- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/hermes/mcp/servers/external/worklittle-jobs)
- [Find Your Role First MCP - Job Search for Agents](/hermes/mcp/servers/external/find-your-role-first-mcp)
- [Parlel MCP - Keyless Professional Network Search for Agents](/hermes/mcp/servers/external/parlel-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
