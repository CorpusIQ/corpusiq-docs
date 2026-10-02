---
title: Worklittle Jobs MCP - Job Search and Market Data
description: "Search over 4 million job listings with filters for visa status, distance, salary and seniority, browse a company index, and read market overview statistics through 21 live-probed tools at mcp.worklittle.com. Account tools add AI-assisted apply and saved-job tracking."
category: Business Operations
stars: 0
added: 2026-08-25
source: "mcp.so GitHub issue #3739"
relevance: ★★
tags: [mcp-server, jobs, hiring, labor-market, recruiting, job-search, workforce]
---

# Worklittle Jobs MCP

**A 4-million-listing job market behind one MCP endpoint.** Worklittle Jobs exposes the Worklittle workforce marketplace as 21 MCP tools: search job listings by keyword, company, location, job type, seniority, or recency; browse a ranked company index; read skill keywords extracted from descriptions; and pull aggregate labor-market statistics. Account tools add AI-assisted apply, resume handling, and saved-job tracking.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://mcp.worklittle.com/
Auth: Public search tools work without an account; API key / OAuth for apply and profile tools
Repo: github.com/worklittle/jobs-mcp (MIT, Aug 2026)
Tools: 21 verified by live probe
Docs: docs.worklittle.com/mcp
```

## Why This Matters for Operators

Labor-market questions are business questions: what roles is a competitor hiring for, what are market-rate skill mixes, where is hiring concentrated. Worklittle's data tools answer those without an ATS: `search_jobs` filters across 4 million listings (visa status, distance, salary, seniority), `search_companies` pulls enriched employer profiles, `get_job_keywords` returns the skill and technology keywords stripped of narrative prose, and `get_market_overview` gives aggregate statistics on the indexed job market. For recruiting operators, that is competitive hiring intelligence and market-rate benchmarking in one toolset.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_jobs` | Searches job listings by keyword, company, location, job type, seniority, or recency |
| `search_companies` | Ranked typeahead search over the market company index, with enrichment fields for employers |
| `load_more_job_cards` | Fetches the next page of job cards for the current search |
| `get_job_details` | Full job details including responsibilities, qualifications, and company info |
| `get_job_keywords` | Skill and technology keywords extracted from a job description, stripped of prose |
| `get_market_overview` | Aggregate statistics about the current indexed job market |
| `track_applied_job` / `delete_applied_job` | Records and removes saved/applied/skipped jobs for the connected account |
| `get_connected_account` | Reads the connected account's user profile and settings |
| `start_apply_with_ai` | Starts an Apply-with-AI session for eligible jobs |
| `upload_profile_resume` / `get_profile_resume_status` / `remove_profile_resume` | Resume handling for the apply pipeline |

Widget-facing tools (`mint_mcp_ui_embed_session`, `mint_chatgpt_embed_session`, `get_maps_api_key`, `update_connected_profile`, `update_connected_email_prefs`, `remove_connected_profile_photo`, `logout_connected_account`) support the embedded Job Cards UI and are not needed for data queries.

## Installation

Connect any MCP client to the hosted endpoint:

```bash
claude mcp add --transport http worklittle https://mcp.worklittle.com/
```

## Configuration

Public search and market tools work without credentials. Connect a Worklittle account (API key or OAuth) to unlock saved jobs, resume upload, and Apply-with-AI; those tools operate on the connected account's own data. Personal API keys also open a watcher for the apply session.

## Business Relevance

- **Competitive hiring intelligence:** see who is hiring, where, and for what skill mix.
- **Market-rate benchmarking:** market overview and keyword data inform comp and job-description decisions.
- **Candidate pipeline support:** search with visa-status, distance, and salary filters before engaging candidates.

## Integration with CorpusIQ

Use Worklittle market data alongside CorpusIQ's CRM connectors: pull competitor hiring signals from `search_jobs` and `get_market_overview`, then log insights to HubSpot or Close deals via CorpusIQ, or store skill-keyword trends in your database for quarterly hiring reviews.

## Limitations

- Consumer-oriented platform: apply flows target individual job seekers; operator use is strongest on the data tools.
- Public search has no documented rate limits but no SLA either; treat it as market intelligence, not an ATS replacement.
- Apply-with-AI requires an eligible job and a connected account; it is not a bulk-apply tool.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [JobYap MCP](/hermes/mcp/servers/external/jobyap-mcp)
