---
title: CourtListener MCP - US Legal Research for Agents
description: Self-hosted MCP server over the CourtListener legal database API v4, GovInfo US statutes and Regulations.gov federal rulemaking - search opinions, dockets, courts, judges, oral arguments and regulations with citation parsing and verification.
category: IP/Legal
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [legal, courtlistener, case-law, regulations, compliance, research, self-hosted]
---

# CourtListener MCP

**LLM-friendly access to three US legal sources in one server** - CourtListener API v4 (millions of opinions, dockets, judges, oral argument audio), GovInfo for United States statute lookup, and Regulations.gov for federal rulemaking document search. Built with FastMCP, runs via Docker or uv.

```
Server type: Self-hosted (Docker or uv / FastMCP)
Auth: CourtListener API token (free) + api.data.gov key for Regulations.gov
Install: docker pull ghcr.io/travis-prall/court-listener-mcp:latest (or vesha/court-listener-mcp)
License: Community project (Travis-Prall/court-listener-mcp)
Built by: Travis Prall (community)
```

## Why This Matters for Operators

Legal questions - competitor trademarks, regulatory filings, customer contract disputes - force operators into expensive research or lawyer calls. **CourtListener MCP puts the primary sources inside an agent's toolchain**: an assistant can pull the actual opinion, the docket history and the oral argument audio, then cite them precisely, instead of paraphrasing what it half-remembers. The citation tool family is the differentiator: batch lookups, citation parsing, format verification and extraction from free text mean the agent can quote what the sources actually say, with verifiable citations.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_opinion` / `get_cluster` | Retrieve court opinions and opinion clusters |
| `get_docket` | Full docket entries for a case |
| `get_court` / `get_person` | Court and judge/attorney lookup |
| `get_audio` | Oral argument audio for a case |
| `latest` | Newest opinions |
| `citation_batch_lookup` / `citation_lookup_citation` / `citation_get_citation_details` | Citation resolution at scale |
| `citation_extract_citations_from_text` / `citation_parse_citation` | Pull citations out of free text |
| `citation_enhanced_citation_lookup` / `citation_verify_citation_format` | Enriched lookup and format validation |
| `regulations_get_document` | Federal rulemaking documents from Regulations.gov |

## Installation

```bash
docker pull ghcr.io/travis-prall/court-listener-mcp:latest
docker run -d ghcr.io/travis-prall/court-listener-mcp:latest
# or the docker-compose.yml shipped in the repo
```

Local/uv route:

```bash
git clone https://github.com/Travis-Prall/court-listener-mcp.git
cd court-listener-mcp && uv run
```

## Configuration

Get a free CourtListener API token from the Free Law Project, and an api.data.gov key for the Regulations.gov tools, then supply both to the server environment. Point your MCP client at the running server (stdio locally, or the served endpoint when deployed).
