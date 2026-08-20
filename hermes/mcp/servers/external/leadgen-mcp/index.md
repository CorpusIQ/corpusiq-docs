---
title: "Leadgen MCP - Romanian Business Registry & Contact Enrichment"
description: "Remote streamable-HTTP MCP server for Romanian business data and lead enrichment: official ONRC registry lookup across 4.2M+ firms with director and legal-representative search, website contact extraction, and WHOIS/DNS/SPF-DMARC domain audits for agents that research companies"
category: Lead Generation & Web Scraping
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so GitHub issue #3654"
relevance: ★★
tags: [romania, onrc, business-registry, lead-generation, contact-extraction, whois, dns-audit, remote-mcp, sales-intelligence]
---

# Leadgen MCP

**Lead generation and company enrichment for AI agents, grounded in Romania's official business register.** Leadgen MCP exposes four read-only tools: company lookup across the official ONRC (Romanian National Trade Register) snapshot — 4.2M+ firms — director and legal-representative search, website contact extraction, and WHOIS/DNS/SPF-DMARC domain audits. It is a hosted remote server with no local install, so any MCP client can pull registry-verified company data plus enrichment signals in one call sequence.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://hermes.adrianhomelab.com/mcp
Auth: None (public validation phase)
Tools: 4 (verified live via JSON-RPC probe, Aug 20 2026)
License: MIT
Registry: io.github.darksider4all/leadgen-mcp (v1.0.0, active)
Built by: darksider4all
```

## Why This Matters for Operators

Romanian company data normally means navigating ONRC's public portal, handling diacritic-sensitive name variants, and stitching contact details from a company's website by hand. Leadgen MCP collapses that into four agent calls: `lookup_business` for the registry record, `lookup_director` to reverse-search a legal representative across firms, `extract_contacts` to harvest emails, phones, and socials from the company site, and `lookup_domain` for the domain posture audit. The registry data comes from the official ONRC open-data snapshot on data.gov.ro loaded locally — not a third-party scraper — and name matching is FTS5-ranked and diacritic-insensitive, so `popescu` matches `Popescu` and `Popе́scu` alike.

The validation-phase posture is the honest caveat: the endpoint is served from the author's homelab with no authentication yet, so it is a public read service. That is acceptable for registry lookups (public data) but means the server carries no SLA and should not be treated as production infrastructure.

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| `lookup_business(query, max_results)` | Ranked FTS5 search of the official ONRC registry (4.2M+ firms) with company detail enrichment |
| `lookup_director(name, max_results)` | Companies by director / legal-representative name, diacritic-insensitive |
| `extract_contacts(website, max_pages)` | Crawls a site for emails, phone numbers, and social profiles |
| `lookup_domain(domain)` | WHOIS + DNS (A, MX, NS, TXT) + SPF/DMARC security audit |

All four tools are read-only; there is no write path to any registry or domain system.

## Installation

```json
{
  "mcpServers": {
    "leadgen": {
      "type": "http",
      "url": "https://hermes.adrianhomelab.com/mcp"
    }
  }
}
```

```bash
claude mcp add --transport http leadgen https://hermes.adrianhomelab.com/mcp
```

Nothing to install or self-host. The endpoint answers Streamable HTTP MCP (SSE-framed responses); a live `initialize` probe on Aug 20, 2026 returned serverInfo `leadgen` with a working session and all four tools enumerated.

## Configuration

No configuration required during the validation phase — no API key, no OAuth. Registry-aware clients can add `io.github.darksider4all/leadgen-mcp` by name via the official MCP Registry. The author has also whitelisted the data pipeline for agentic payments on Apify under `ro-business-data-mcp` for agents that route through Apify's network instead of the direct endpoint.

## Business Relevance

- **SDRs and lead-gen teams** verify Romanian prospect firms against the official register instead of scraped directories
- **Compliance and onboarding** check directors and legal representatives against registry records
- **Domain due diligence** pairs company lookup with WHOIS/DNS/SPF-DMARC posture in one session
- **Agent builders** get a free remote endpoint for EU company research without standing up their own ONRC ingestion

## Integration with CorpusIQ

Leadgen MCP covers the Romanian registry layer — a country-specific source none of CorpusIQ's connectors natively answers. The natural flow: an agent uses `lookup_business` to identify and verify a Romanian prospect, `extract_contacts` for reachable email addresses, then hands the qualified record to CorpusIQ — HubSpot or LeadConnector for CRM placement, email for the outreach thread, and QuickBooks once a deal invoices. The registry-verified record is the source-declared anchor that matches CorpusIQ's reporting discipline.

## Limitations

- Romanian business registry only — company data for other countries is out of scope
- Homelab-hosted endpoint in a no-auth validation phase: no SLA, not production infrastructure
- New listing (Aug 2026), zero-star repository, single maintainer
- `extract_contacts` is a website crawl — respect robots constraints and rate limits on target sites

## See Also

- [MisarReach MCP — Outbound Sales and Lead Pipeline for AI Agents](/hermes/mcp/servers/external/misarreach-mcp/)
- [Apollo.io MCP — B2B Contact Data and Sequences](/hermes/mcp/servers/external/apollo-io-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
