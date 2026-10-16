---
title: "Form 5500 MCP - US Retirement Plan Filings in Chat"
description: "Free keyless MCP server over the U.S. DOL Form 5500 filings: search plans by sponsor or EIN, benchmark fees and read plan changes."
category: "Finance / Retirement"
stars: n/a (new listing)
added: 2026-10-15
source: "mcpservers.org /all (October 15, 2026 evening sweep)"
relevance: ★★★
tags: [form-5500, retirement-plans, dol, pension, benefits, benchmarking, public-data, keyless]
---

# Form 5500 MCP

**Every retirement and welfare plan filed with the U.S. Department of Labor is public, and this server puts the whole filing set behind nine MCP tools. An assistant can search plans by sponsor, EIN, state, type or size, read one plan's filed profile, rank plans by a filed metric, compare cohorts by percentile and walk a filing's history field by field. No login, no API key.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://5500mcp.ai/mcp
Auth: None (public DOL filings; no account, no key)
Server: 5500mcp v1.0.0
Works with: Claude, ChatGPT, Cursor and any client that accepts a remote MCP server
Data: U.S. DOL / EBSA Form 5500 and 5500-SF retirement and welfare plan filings
Publisher: 5500mcp (5500mcp.ai); vintage 2026-09-03, updated daily
Listing: mcpservers.org /all, October 15, 2026 evening sweep
```

## Why This Matters for Operators

Plan data is already public, but it lives in a form-based government search that returns pages, not answers. The questions an operator actually asks are comparative: what do plans my size pay in service-provider fees, how did this plan's financials move year over year, and does this sponsor look like a plan worth approaching. Those are cohort questions, and this server answers them with filed figures only.

## What You Can Do Today

| Tool | What it does |
|---|---|
| `search_plans` | Find filers by sponsor name, plan name, EIN, state, plan type or subtype, form type, participant band, asset band |
| `get_plan` | Full filed profile for one plan |
| `top_plans` | Rank plans by a filed metric (participants, total assets, sponsor name) |
| `plan_changes` | Field-level filing history for a plan |
| `cohort_stats` | Percentile distributions and base rates for a defined cohort |
| `cohort_chart` | Percentile box plot with one plan marked |
| `list_skills` / `get_skill` | Eight guided workflows: Form 5500 literacy, plan fee benchmark, plan diligence brief, fee transparency report, compliance flag scan, committee review inputs, verify a plan claim, plan prospecting screen |
| `server_info` | Server and dataset metadata |

## Business Relevance

- **HR and benefits teams** get a like-for-like fee benchmark for their own plan without a consultant's first pass
- **Retirement plan advisors and recordkeepers** get a prospecting screen over the filed population, filtered by state, size and plan type
- **M&A and diligence work** reads a target's plan history and committee inputs in the same assistant that already holds the deal context
- **Auditors and committees** get compliance flag scans and a plain-language fee transparency report built from filed figures
- **Reporting discipline is built into the server:** every answer is either a filed figure or a computed percentile over the filed population, labelled as such, and the instructions forbid estimating, modelling or imputing a figure a plan did not file

## Integration with CorpusIQ

Plan questions rarely stand alone. CorpusIQ connects the surrounding business systems over read-only tools - accounting, HR, documents, email - and this server adds the public filing layer, so one conversation can move from a plan's filed fees to the company records that explain them. Because the endpoint is keyless and read-only, it is safe to attach to any client for a first look.

## Limitations

- **Filing scope:** Form 5500 and 5500-SF only; plan documents, SPDs and participant-level detail are not part of the public filing set
- **As filed:** the server reports what was filed and refuses to model or project, so gaps in a filing stay gaps
- **Bounded queries:** search is typed-filter only, with a limit of 100 rows per call and an offset cap
- **Cohort math, not advice:** percentiles describe the filed population and are not a fiduciary or actuarial opinion
- **Adjacent server exists:** a separate wrapper of the same EFAST2 search service is published as `io.github.pipeworx-io/form5500`, so expect to see both in registries

## FAQ

### Do I need an account or an API key?

No. The endpoint is public DOL filing data, and a keyless `initialize` call returns 200 as server `5500mcp` v1.0.0 with all nine tools listed.

### Can it find a specific company's plan?

Yes. `search_plans` accepts a sponsor name, a plan name or an EIN, plus state, plan type, participant band and asset band filters, and returns the most recent filing captured for each matching plan.

### Is the data current?

The server describes itself as updated daily over DOL Form 5500 and 5500-SF filings, with a 2026-09-03 dataset vintage on the listing.

### Where can I get the underlying data?

`list_datasets` exposes the tables behind the tools as CSV and JSON downloads.
