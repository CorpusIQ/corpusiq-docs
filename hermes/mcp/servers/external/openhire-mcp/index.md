---
title: OpenHire MCP - AI, Infra, and Robotics Jobs from Employer
description: "Privacy-first stdio MCP server that turns an AI assistant into a job radar over 16,000+ live AI/infra, autonomous-driving and embodied-AI postings from 120+ employers' first-party ATS APIs (Greenhouse, Lever, Ashby, Beisen) across the US, Europe and China, with verified_at freshness stamps, ghost_score stale-listing detection and employer-native apply links. Matching runs locally and résumés never transit the server. 5 tools, MIT, PyPI package."
category: Business Operations
stars: 2 (github.com/gzchenhao/openhire)
added: 2026-08-31
source: "mcp.so GitHub issue #3845"
relevance: ★★
tags: [mcp-server, jobs, hiring, recruiting, ai-jobs, robotics, workforce-data, stdio-mcp]
---

# OpenHire MCP

**Agent-native job protocol over 120+ employers' first-party ATS APIs.** 16,000+ live AI/infra, autonomous-driving and embodied-AI postings across the US, Europe and China, every listing stamped with `verified_at`, scored for staleness with `ghost_score`, and deep-linked to the employer's own application URL. Matching runs entirely on your machine: no account, no signup, and a résumé structurally cannot transit the server (the authorization tool has no file parameter). MIT, PyPI `openhire` v0.2.0, registry `io.github.gzchenhao/openhire`.

```
Server type: Local (stdio)
Auth: None (matching is client-side; only an anonymous fingerprint reaches the server)
Distribution: PyPI openhire (pipx install openhire, uvx openhire serve)
Tools: 5 (search_jobs, watch_intent, check_watches, get_company_info, authorize_application)
Data: 16,000+ live postings, ~120 companies, first-party ATS sources only (Greenhouse, Lever, Ashby, Beisen)
Pricing: Free, open source
Built by: OpenHire Protocol (github.com/gzchenhao/openhire, MIT)
Registry: io.github.gzchenhao/openhire (v0.2.0)
```

## Why This Matters for Operators

Tech hiring searches are dominated by job boards that resurface stale listings and hide the source. OpenHire indexes only first-party data: the same public ATS endpoints (Greenhouse, Lever, Ashby, Beisen) that power employers' own career pages, never a third-party board. Every listing carries `verified_at` (last moment confirmed live on the employer's site), `source` (always `employer_site` or `ats_public_api`), and a `ghost_score` computed from the real posting date, so ghost and zombie listings rank visibly worse.

The niche is deliberate and operator-relevant: AI/infra, autonomous-driving and embodied-AI roles, including Chinese robotics employers (Unitree, UBTECH, Galaxea, Dobot, Mech-Mind, Pudu, SIASUN and more). For a founder tracking the talent market, a recruiter sourcing robotics engineers, or a hiring manager benchmarking salary floors against live postings, that is a signal-dense window on the highest-stakes hiring segment right now.

**Job-market questions become one chat thread with first-party freshness stamps instead of board surfing.**

## Tools & Capabilities

All 5 tool names verified from the README and the mcp.so submission:

| Tool | Capability |
|---|---|
| search_jobs | Hard-filter the live index by required_skills (AND), role_family, remote_scope, min_salary and currency; results carry verified_at, datePosted, days_open, ghost_score, remote_scope, eligible_regions and apply_channel |
| watch_intent | Register a standing intent once; new matching jobs are waiting on the next check, even after the terminal closes |
| check_watches | Pull matches that are new since the last check (client-pull; stdio has no push) |
| get_company_info | Aggregate anonymous trust signals for one employer: ghost_score_avg, active_jobs, index_built_at |
| authorize_application | One explicit confirmation per job; records the authorization and returns the employer's own deep-linked application URL. Structurally cannot accept a résumé |

Every listing is valid schema.org/JobPosting plus five protocol fields: `verified_at`, `source`, `ghost_score` (0-1, lower is better, computed from the real posting date), `response_sla_days` (employer response window, null in v0.1) and `apply_channel` (always the employer's own URL, deep-linked to the specific job).

## Installation

```bash
# 1. Install (pipx keeps it isolated and puts ohp on your PATH)
pipx install openhire

# 2. Bootstrap the job index (default: public snapshot, then an incremental live refresh)
ohp bootstrap
#   --fresh      crawl the public ATS from scratch (heuristic, free)
#   --deepseek   higher-quality extraction using your own DEEPSEEK_API_KEY

# 3. Serve MCP to your client
ohp serve
```

Or without installing, via uvx: `uvx openhire serve`.

## Configuration

Claude Desktop (`claude_desktop_config.json`), Cursor (`~/.cursor/mcp.json`) and Windsurf (`~/.codeium/windsurf/mcp_config.json`) all take the same stdio entry:

```json
{
  "mcpServers": {
    "openhire": {
      "command": "ohp",
      "args": ["serve"]
    }
  }
}
```

Run `ohp bootstrap` once first so the index has data. Default storage is a local SQLite file (`~/.openhire/openhire.db`); set `OPENHIRE_DATABASE_URL` to a Postgres URL to share one index across machines. Optional and entirely local: `ohp init --scan <dir>` derives a skill fingerprint from your own repos, so matching can run without ever writing a résumé.

## Business Relevance

- **Founders and hiring managers** benchmark live salary floors and skill requirements for AI/infra and robotics roles before opening requisitions.
- **Recruiters** filter by required_skills and role_family, then lean on verified_at and ghost_score to skip stale or ghost listings.
- **Talent market analysts** use get_company_info trust signals (ghost_score_avg, active_jobs) to compare employer hiring velocity.
- **Job seekers** register watch_intent intents once and collect new matches without re-running searches, then apply through the employer's own deep-linked URL.

## Integration with CorpusIQ

OpenHire answers who is hiring for what; CorpusIQ answers the business questions behind the hire. A composed workflow: the assistant watches robotics-engineering intents in OpenHire and benchmarks salary floors against live postings, then checks QuickBooks cash runway and HubSpot pipeline via CorpusIQ connectors to time the requisition. Hiring research and business readiness in one conversation, no board logins and no résumé uploads.

## Limitations

- Young listing: repo created Jul 14, 2026, 2 stars, v0.2.0; single-maintainer project.
- Narrow niche by design: AI/infra, autonomous-driving and embodied-AI roles only; not a general job board.
- stdio only: no hosted remote endpoint; each user runs the local server against a public index.
- China coverage is limited to Beisen tenants (11 robotics and embodied-AI companies today); Moka is on the roadmap and Feishu Hire is explicitly unsupported out of respect for its anti-bot measures.
- response_sla_days is null in v0.1; employer SLA enforcement (7-day auto-delist) is planned for v0.3.
- ~120 companies is a curated first-party set, not the entire market; company inclusion happens via GitHub issue.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Vocaneo MCP - French Jobs, Diplomas, and Training Data](/docs/hermes/mcp/servers/external/vocaneo-mcp)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/docs/hermes/mcp/servers/external/worklittle-jobs)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
