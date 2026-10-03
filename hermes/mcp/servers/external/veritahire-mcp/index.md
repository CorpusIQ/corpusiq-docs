---
title: "VeritaHire MCP - Live US Jobs for Agents"
description: "Keyless remote MCP over US jobs read straight from employer career sites, with full postings, open-status checks and pay benchmarks."
category: "Business Operations"
stars: n/a (hosted platform, veritahire.com)
added: 2026-10-02
source: "mcpservers.org server page (veritahire-com-for-ai)"
relevance: ★★★
tags: [jobs, recruiting, hiring, careers, salary, staffing, remote-mcp]
---

# VeritaHire MCP

**Remote MCP server (Streamable HTTP, no key)** - VeritaHire reads every US job directly from the employer's own careers site, re-reads it on a schedule, and retires it within about 36 hours of the role leaving the site, so an agent works with postings that are real today rather than stale aggregator rows.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless, limited per address)
Endpoint: https://veritahire.com/mcp
Tools: 4 (search_live_jobs, get_job, save_search, report_problem)
Pricing: Free, no key
Category: Business Operations
Built by: VeritaHire (veritahire.com)
```

## Why This Matters for Operators

Job aggregators routinely carry roles that closed weeks ago, so a recruiting pipeline built on them wastes candidate and hiring-manager time on dead requisitions. VeritaHire inverts the model: each posting is read from the source employer, re-read on a schedule, and marked closed once it disappears. The result is a search surface an agent can trust to answer "is this real and still open" without a human re-checking every link.

**The differentiator is provenance, not volume.** Every result carries the employer's own apply link, posted pay, the requirement facts the posting lists, a distance from the given location, and when the listing was last confirmed. An operator can screen and shortlist from the same facts a candidate would see.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_live_jobs` | Find live jobs near a place by title, keywords or remote-only, returning up to 25 with pay, requirements, distance and apply link |
| `get_job` | Read one full posting: whole text, requirement facts, pay, benefits, open status and apply link |
| `save_search` | Email the user new jobs for a saved search, daily, after they confirm by click |
| `report_problem` | Record a data problem such as a job listed open that the employer's site shows closed |

## Installation

```bash
claude mcp add veritahire --transport http https://veritahire.com/mcp
```

In Claude or ChatGPT, add `https://veritahire.com/mcp` as a custom connector. A public OpenAPI description is available at `https://veritahire.com/openapi.json` and an `llms.txt` at `https://veritahire.com/llms.txt`.

## Configuration

```json
{
  "mcpServers": {
    "veritahire": {
      "type": "http",
      "url": "https://veritahire.com/mcp"
    }
  }
}
```

No API key and no OAuth step. The endpoint is rate-limited per address, so unattended high-volume use should expect throttling.

## Business Relevance

- **Recruiters** shortlist live roles with posted pay and requirement facts in one pass, without re-verifying that each link still works.
- **Hiring managers** check whether a competitor's role is still open and how nearby employers pay for the same title.
- **Sales and partnerships teams** watch hiring signals for account expansion, since a careers page that keeps adding roles is a growth indicator.
- **Compensation analysts** benchmark healthcare pay against nearby employers using the same source the applicant sees.
- **Founders** scope a new market by reading who is actually hiring there right now.

## Integration with CorpusIQ

VeritaHire answers "who is hiring and what do they pay", which pairs with CorpusIQ's business-data connectors. A team tracking an account in HubSpot can have an agent check that company's live hiring and surface it on the account record as a growth signal; a GA4 or Shopify read that shows a merchant scaling can be matched against the roles they are opening. VeritaHire supplies the external hiring picture, CorpusIQ supplies the internal revenue and pipeline context, and the two compose into an account-health view neither carries alone.

## Limitations

- Brand new, so no track record yet.
- United States only, and strongest for healthcare roles where pay benchmarking is offered.
- Free and keyless, which means per-address rate limits and no SLA.
- Only the filters given are applied; requirement facts are listed rather than used to drop results.
- The daily-email tool sends to the user's own address and needs their click to activate.

## FAQ

### Does VeritaHire need an API key?

No. The MCP endpoint at `https://veritahire.com/mcp` is keyless and read-only, limited per address.

### How current is the job data?

Postings are read from employers' own careers sites, re-read on a schedule, and retired within about 36 hours of leaving the site, so a result is a live posting rather than an aggregated estimate.

### Can an agent set up recurring job alerts?

Yes, through `save_search`, which emails the person and starts a daily digest only after they click to confirm.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
