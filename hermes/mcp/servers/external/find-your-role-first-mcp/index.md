---
title: Find Your Role First MCP - Job Search for Agents
description: "Hosted MCP server letting an agent search over a million open postings from 13,000+ company career sites, read straight from the source."
category: Business Operations
stars: n/a (hosted service, findyourrolefirst.click)
added: 2026-10-01
source: "mcpservers.org /all (find-your-role-first-mcp)"
relevance: ★★
tags: [job-search, hiring, recruiting, career-sites, labor-market, remote-mcp]
---

# Find Your Role First MCP

**Job search that reads company career sites directly.** Find Your Role First exposes a hosted MCP server over a feed of open roles gathered from more than 13,000 company career sites, checked every few hours. An agent asks for roles in plain English and gets a shortlist with the original posting and application links, without a job-board middleman.

```
Server type: Remote (Streamable HTTP)
Auth: API key (Bearer header; created in the account)
Endpoint: https://findyourrolefirst.click/mcp
Tools: 6 (search, count, list, get, changes, usage)
Pricing: $9 per month, cancel any time
Category: Business Operations
Built by: Find Your Role First
```

## Why This Matters for Operators

Reading roles from job boards means reading a copy that is often stale, reposted or advertised by a third party. This feed goes to the source instead: it re-reads each company career site and compares it every few hours, so what an agent returns is the posting as the company published it, with the original URL and the application link.

The tool set is shaped around sizing before spending. A free `count_jobs` call answers how many roles a search would match, up to 1,000, without unlocking anything, and `get_changes` reports what is new, updated, reopened or closed since a saved cursor. For an operator tracking a market or competing for talent, that turns a manual sweep of career pages into a scheduled query.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_jobs` | Whole-word search across titles and companies, up to 20 results, newest first, with location, remote and recency filters |
| `count_jobs` | Count how many roles a search would match, up to 1,000; free and uses no credits |
| `list_my_jobs` | List the roles already unlocked on the account, newest first; free |
| `get_job` | Refresh one job's metadata, dates, known status and links |
| `get_changes` | New, updated, reopened and closed jobs after a saved cursor |
| `get_usage` | Check the remaining monthly allowance; free |

## Installation

```
claude mcp add --transport http jobfeed https://findyourrolefirst.click/mcp
```

The client must support Streamable HTTP with a custom bearer authorization header. OAuth-only connector flows are not supported by this version of the server.

## Configuration

```json
{
  "mcpServers": {
    "jobfeed": {
      "type": "http",
      "url": "https://findyourrolefirst.click/mcp"
    }
  }
}
```

Create an agent key in the account, then attach it in the Authorization header (Bearer scheme) on each request.

## Business Relevance

- **Founders and hiring managers** can track what roles competitors are opening and where they are hiring, straight from the companies' own sites.
- **Recruiters and talent teams** can size a market with the free count call before spending allowance on a full search.
- **Market and competitive researchers** can use new-postings and closed-roles changes as a signal of where a sector is expanding or contracting.
- **Operators running their own search** can ask an agent for a shortlist and follow each link to the original posting.

## Integration with CorpusIQ

The job feed is a source of market signal that composes with CorpusIQ's business connectors. An agent can read a company's revenue and customer data through the corpusiq connector set, then check the same company's hiring through this server, so a competitive picture is assembled from both the numbers and the roles being opened. For operators watching a specific market, the two together answer both what a business is earning and where it is investing next.

## Limitations

- Paid subscription at $9 per month; there is no free tier beyond the free counting and listing calls.
- The server returns basic job details, source dates and links, but not full descriptions or generated summaries; the agent needs its own web or browser tool to read requirements at the source.
- The client must support a custom bearer header, which rules out OAuth-only connectors.
- Searches are capped at 20 results per call and 1,000 per count, so breadth comes from repeated, filtered queries.

## FAQ

### What does the Find Your Role First MCP server do?

It gives an AI agent a searchable feed of open jobs gathered from more than 13,000 company career sites, with the original posting and application links for each role.

### How much does it cost?

$9 per month, cancel any time, with a three-day refund window. Counting and listing calls are free and use no allowance.

### Does it work with any MCP client?

It needs a client that supports Streamable HTTP with a custom bearer authorization header. OAuth-only connector flows are not supported in this version.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
