---
title: "Family Office Registry MCP - Sourced Investor Data"
description: "Search 388 verified family offices across Switzerland, Liechtenstein, Austria, Germany and Dubai, each record sourced, dated and honest about gaps."
category: Finance
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (familyofficeregistry.com)"
relevance: ★★
tags: [finance, investors, family-offices, fundraising, registry, verified-data, europe, remote-mcp]
---

# Family Office Registry MCP

**Sourced, dated records of family offices, with explicit honesty about what the registry does not know.** The open tier needs no account and lets an assistant search 388 verified family offices in Switzerland, Liechtenstein, Austria, Germany and Dubai by name, country, canton or classification, and page through records. Every record cites its sources and carries its last-verified date, and the accompanying skill file states what the registry deliberately does not hold: no estimated assets under management, no personal email addresses, no ranking, no claim of complete coverage.

```
Server type: Remote (Streamable HTTP)
Auth: None (open tier) or Bearer subscription key
Endpoint: https://familyofficeregistry.com/api/mcp
Tools: 2 (search_registry, get_record)
Pricing: open tier free, 25 records/page, 60 calls/hour; CHF 99/month or CHF 890/year for full records
Category: Finance
Built by: familyofficeregistry.com
```

## Why This Matters for Operators

Fundraising lists are usually either stale scrapes or guessed contact data. This registry replaces both failure modes with a verification discipline: a blank verification date means nobody has re-checked that record, not that it is current, and answers carry the date and the source. An operator deciding which family offices to approach can separate verified records from assumptions at a glance.

The open tier is genuinely useful before any subscription: classification (SFO, MFO, intermediary), country, canton, legal form, register identifier, whether the firm allocates to external funds, focus tags and the verification date are all public. The subscription adds named roles with sources, contact channels, the purpose clause and the full source list.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| search_registry | Search by name, country, canton or classification, one page of results at a time |
| get_record | One firm by registry id, including whether it allocates to external funds |

The descriptor endpoint returns what the server is, what the open tier includes and where the skill lives, with no key required. Subscribers get the change feed and export for pipeline building.

## Installation

```bash
claude mcp add --transport http family-office-registry https://familyofficeregistry.com/api/mcp
```

Nothing else is needed for the open tier. Annual subscribers send the organization key as a bearer Authorization header; the key is shown once on the subscription page and is the organization's credential, not a person's.

## Configuration

```json
{
  "mcpServers": {
    "family-office-registry": {
      "type": "http",
      "url": "https://familyofficeregistry.com/api/mcp"
    }
  }
}
```

With a subscription key, add a headers block to the same entry carrying the bearer Authorization value. The terms do not permit taking a copy of the compilation.

## Business Relevance

- **Founders fundraising in the DACH region** build verified target lists instead of scraped ones
- **Fund managers** identify which family offices allocate to external funds
- **Business development teams** qualify prospects before spending outreach cycles
- **Compliance and research teams** get answers with dates and sources attached

## Integration with CorpusIQ

The registry supplies the counterparty picture while CorpusIQ supplies the performance picture. A composed workflow: an operator researching a family office reads the sourced, dated registry record through this server, then answers the firm's own financial questions from CorpusIQ's QuickBooks, Stripe and GA4 connectors. Investor intelligence and business data land in one evidence-first session.

## Limitations

- Regional scope: Switzerland, Liechtenstein, Austria, Germany and Dubai only
- No assets under management, no personal emails, no ranking, no complete-coverage claim
- Open tier is capped at 25 records per page and 60 calls per hour
- Full records, the change feed and export need an annual subscription with machine access

## FAQ

### What does a blank verification date mean?

The record has not been re-checked since it was added, not that it is current. Answers should carry the last_verified date and the source link.

### Is the open tier really free?

Yes. Classification, country, legal form, allocation flag, focus tags and verification dates need no account and no key, capped at 60 calls per hour.

### Does it estimate assets?

Deliberately not. The registry states this outright and publishes a skill file listing everything it does not hold.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Kresmion MCP - Market Intelligence for Agents](/hermes/mcp/servers/external/kresmion-mcp/)
- [MentionFox MCP - Cited Reports and Mention Scans](/hermes/mcp/servers/external/mentionfox-mcp/)
- [iMario MCP - Synthetic Audience Research for Agents](/hermes/mcp/servers/external/imario-mcp/)
