---
title: "Vocaneo MCP - French Jobs, Diplomas, and Training Data"
description: "Official keyless remote MCP server from Vocaneo, the French career-guidance platform: 13 read-only tools to search jobs, RNCP and RS diplomas, certifications, and 135,000 training programs with skills comparison, career pathways, training centers, and French location resolution, verified live at the Streamable HTTP endpoint with no account required."
category: Business Operations
stars: n/a (new listing, github.com/CIB-PROD/vocaneo-mcp-connector)
added: 2026-08-28
source: "mcp.so GitHub issue #3804"
relevance: ★★
tags: [mcp-server, jobs, training, france, hr, workforce-data, remote-mcp]
---

# Vocaneo MCP

**Official MCP server from Vocaneo, the French career-guidance platform run by a social-economy company.** 13 keyless read-only tools expose the national job referential, RNCP and RS diplomas and certifications, and 135,000 real training programs in France, plus tools that compare a candidate's stated skills against a target job, list career pathways, and resolve French locations. The endpoint answered initialize and tools/list anonymously with no account and no session header (verified live, server version 2.0.0).

```
Server type: Remote (Streamable HTTP), keyless
Auth: None (read-only)
Endpoint: https://mcp.vocaneo.com/mcp
Tools: 13 (verified live)
Pricing: Free
Category: Business Operations / Workforce data
Built by: Vocaneo (vocaneo.com, GitHub CIB-PROD/vocaneo-mcp-connector, MIT)
Registry: com.vocaneo/vocaneo (official, v1.0.1)
```

## Why This Matters for Operators

French labor-market data is spread across official portals, each with its own search UI and export limits. Vocaneo consolidates the referential (jobs), the credentials layer (RNCP and RS diplomas and certifications), and the supply layer (135,000 trainings and their centers) behind one keyless endpoint. For an operator hiring, relocating, or building HR tooling in France, that is three datasets in one call surface.

Two tools make it more than a lookup API. compare_skills takes skills written in plain language and returns what matches and what is missing against a target job, useful for gap analysis before hiring or reskilling. get_job_pathways answers "how to become X" with the diplomas and certifications that lead to a job and how many trainings prepare for each, useful for workforce planning.

**French hiring, credential, and training questions become one chat thread instead of three portals.**

## Tools & Capabilities

All 13 tool names verified by live anonymous probe:

| Tool | Capability |
|---|---|
| search_jobs | Search the French job referential by keywords, activity sector, minimum salary, and ease of entry |
| get_job | Full job profile: missions, skills, titles, entry conditions, and labor-market data (tension, salaries, offers) |
| compare_skills | Compare plain-language skills against a target job's requirements and report matches and gaps |
| get_similar_jobs | Jobs close to a given one, ranked by shared know-how |
| list_job_sectors | List activity sectors with their identifiers for whole-sector searches |
| get_job_pathways | Diplomas and certifications that lead to a job, with the number of trainings per path |
| search_certifications | Search RNCP and RS diplomas and certifications by name, code, type, or exit level |
| get_certification | Full diploma or certification profile: codes, level, access routes, average training price |
| search_trainings | Search 135,000 trainings by keywords, location, and delivery mode |
| get_training | Full training profile: objectives, program, prerequisites, admission terms, price, eligibility |
| search_training_centers | Search French training organizations, CFAs, and skills-assessment centers |
| get_training_center | Full establishment profile: legal name, address, city, status, and types |
| resolve_location | Resolve a French postal code or city name into exact values for the search tools |

## Installation

```bash
claude mcp add vocaneo --transport http https://mcp.vocaneo.com/mcp
```

No key and no signup; the endpoint is read-only and public.

## Configuration

```json
{
  "mcpServers": {
    "vocaneo": {
      "type": "http",
      "url": "https://mcp.vocaneo.com/mcp"
    }
  }
}
```

## Business Relevance

- **HR operators in France** search the national job referential and salary ranges for job descriptions and benchmarks.
- **Recruiters** run compare_skills against candidates to quantify skill gaps before interviews.
- **Training providers** search the 135,000-program catalog and training centers for competitive positioning.
- **Relocation and mobility teams** resolve locations and map local trainings and centers.
- **Workforce planners** use get_job_pathways to model reskilling routes between job families.

## Integration with CorpusIQ

Vocaneo answers labor-market questions; CorpusIQ answers the business questions behind them. A composed workflow: the assistant benchmarks salaries and skill requirements for a planned French hire with Vocaneo, then checks QuickBooks cash flow and HubSpot pipeline via CorpusIQ connectors to time the hire. Hiring research and business readiness in one conversation, no portal logins.

## Limitations

- France-only data; no cross-border or multi-country coverage.
- Read-only surface; no writes, no account features like saved searches.
- Jobs data is the national referential, not a live job-board feed of open positions.
- Tool descriptions are in French; clients and assistants should expect French-language payloads.
- Young listing: repo created Aug 27, 2026, 0 stars; MIT license.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/hermes/mcp/servers/external/worklittle-jobs)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
