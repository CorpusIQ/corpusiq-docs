---
title: JobYap MCP
description: Job postings aggregated from tech companies' official careers sites with public discussion threads — search jobs, salaries, locations, and community signal over MCP with no API key.
category: Productivity
stars: n/a (new listing)
added: 2026-08-14
source: mcp.so
relevance: ★★
tags: [jobs, job-search, hiring, recruiting, salaries, job-board, talent, remote-mcp]
---

# JobYap MCP

**Remote MCP server (Streamable HTTP, no auth)** — a job search engine that aggregates live postings directly from companies' official careers sites and attaches a public discussion thread to every listing. Search by title, company, location, remote/hybrid, and freshness; read salaries, full descriptions, apply URLs, and community comments (salary talk, interview notes, team signal). Read-only, no API key, no account.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://mcp.jobyap.com/mcp
Tools: 8 (search_jobs, get_job, get_job_comments, search_locations, list_companies, get_job_stats, search, fetch)
Pricing: Free
Category: Productivity
Built by: JobYap (jobyap.com)
```

## Why This Matters for Operators

Job boards recycle listings; JobYap pulls from the source. Every posting is aggregated directly from a company's official careers page, so the description, salary range, and apply URL are what the company actually published — not a third-party copy that has drifted or expired.

**The discussion thread is the moat.** Every posting carries a public comment thread where candidates and employees talk salary reality, interview process, and team health — the signal that never appears in a job description. Threads stay open even after a posting expires, so the historical record survives.

For agents, the value is a keyless, read-only API into hiring reality: which companies are hiring for what, at what pay, with what community sentiment — usable as a labor-market signal as much as a job board.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_jobs` | Structured job search: title query, company (exact names from list_companies), location identifiers (from search_locations), remote/hybrid filter, freshness, pagination cursor, sort by newest or discussion activity |
| `get_job` | Full posting as markdown: description, salary ranges, locations with work mode, derived employment types, apply URL, posting dates, canonical discussion URL |
| `get_job_comments` | Chronological, threaded community discussion with like counts |
| `search_locations` | Resolve free-text places ("bay area", "Germany") to location identifiers |
| `list_companies` | Every tracked company with active job counts |
| `get_job_stats` | Aggregate stats: companies tracked, active jobs, newest posting date |
| `search` | Natural-language job search, returns citable result IDs and URLs |
| `fetch` | Full JobYap document for a search result: posting as markdown plus top community comments |

## Installation

```bash
claude mcp add jobyap --transport http https://mcp.jobyap.com/mcp
```

The same job data is also available as a keyless JSON API at jobyap.com/api/v1 and as an Agent Skill in github.com/jobyap/agent-skills.

## Configuration

```json
{
  "mcpServers": {
    "jobyap": {
      "url": "https://mcp.jobyap.com/mcp"
    }
  }
}
```

No authentication, no account, no API key. Read-only by design — the server exposes no apply or post actions.

## Business Relevance

- **Founders and hiring managers** get live competitor hiring signals — who is staffing up, for which roles, at what published pay — as a structured query
- **Recruiters** combine search_jobs with get_job_comments to see candidate-side sentiment on interviews and comp before sourcing
- **Job seekers and career agents** search titles, filter remote, and read the salary reality in the comments before applying
- **Analysts** use get_job_stats and list_companies to track labor-market expansion and contraction by company

## Integration with CorpusIQ

JobYap's hiring signals feed the people side of CorpusIQ's business-ops stack. A composed workflow: JobYap's search_jobs surfaces a competitor's sudden hiring burst, CorpusIQ's HubSpot connector records the competitor account with that signal attached, and GA4 + Klaviyo trigger a nurture sequence targeting operators who match the churn-risk profile — before the hiring wave becomes churn. For talent teams, JobYap's candidate-side comment data pairs with CorpusIQ's CRM connectors to attach real interview and comp sentiment to every tracked candidate.

## Limitations

- Tech-company careers sites only — no agency postings, no generic board scraping
- Title-only text query on search_jobs (try synonyms and shorter tokens when results are thin); company names must match list_companies exactly
- Read-only: no applications, no alerts, no notifications over MCP
- Community comments are user-generated content — treat them as signal, not fact
- Brand new listing (Aug 2026) — catalog coverage is still growing

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
