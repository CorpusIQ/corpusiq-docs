---
title: Ransack MCP - Source-Attributed Search and Research
description: "Hosted Streamable HTTP MCP for search and research with source-attributed answers: 6 tools cover live search, page fetch, multi-step cited research reports, semantic memory over fetched pages, async task polling and US building-permit lookup. Unreadable pages are reported, not guessed. Bearer API key."
category: Content & Research
stars: n/a (docs-only repo; service closed-source)
added: 2026-08-27
source: "mcp.so feed (ransack)"
relevance: ★★
tags: [search, research, citations, web-fetch, reports, permits, remote-mcp]
---

# Ransack MCP

**Hosted remote MCP server (Streamable HTTP, Bearer API key) for source-attributed search and research.** Ransack is a search and research service for AI agents with one hard rule: every result carries its source URL, and pages the server cannot read - login-walled news, bot-blocked retailers - are reported as limitations rather than silently skipped or guessed. Six tools cover live search, page fetch, multi-step research pipelines, semantic recall over previously fetched pages, async task polling, and a US building-permit lookup.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key from ransack.tools/trial
Endpoint: https://ransack.tools/mcp
Tools: 6
Pricing: Free trial key; paid plans opening once billing is verified
Repo: github.com/chancewalker165-dot/ransack (docs-only; service proprietary)
Category: Content & Research
```

## Why This Matters for Operators

Research tools that quietly fabricate are worse than useless for operators - a hallucinated citation in a vendor report or an RFP answer is a liability. Ransack is built around the opposite contract: every answer is source-attributed, deduplicated results carry their URLs, and unreadable pages are disclosed rather than papered over. **The honest-limitations section of its own docs names the failure modes (paywalled pages, hard-blocking retailers) instead of hiding them** - the right posture for business research where the difference between "we found nothing" and "we guessed" matters legally.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `ransack` | One tool, many modes: search, fetch, discover, hosts, verify, research - with recency filters and source-attributed, deduplicated results |
| `execute_research` | Multi-step pipeline (discover, fetch, extract, synthesize) into a cited report |
| `get_report` | Retrieve a persisted report by report_id |
| `search_memory` | Semantic recall over previously fetched page chunks |
| `tasks_get` | Poll an asynchronous research task |
| `ransack_permit_search` | US building-permit lookup (currently Brevard County FL) |

Output formats: Markdown, JSON or hybrid.

## Installation

```bash
claude mcp add --transport http ransack https://ransack.tools/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Get a trial key at ransack.tools/trial, then add the server to any MCP client.

## Configuration

```json
{
  "mcpServers": {
    "ransack": {
      "type": "streamable-http",
      "url": "https://ransack.tools/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Research teams** get cited multi-step reports where every claim carries its source
- **BD and sales teams** research prospects with deduplicated, source-attributed results
- **Analysts** poll async research tasks for long-running sweeps
- **Real-estate and construction operators** run permit lookups alongside web research

## Integration with CorpusIQ

Ransack covers external research; CorpusIQ covers the operator's internal record. A market-research mission can run Ransack's cited reports on competitors while CorpusIQ's Shopify and Stripe connectors provide the company's own performance numbers - the composed answer cites sources for the outside view and pulls real books for the inside view. For due-diligence workflows, Ransack's source URLs give the evidence trail that CorpusIQ's financial connectors can then cross-check against actual payables and revenue.

## Limitations

- Brand new - listing submitted Aug 27, 2026; paid plans not yet open
- Proprietary hosted service - repo is documentation and config only, no self-host
- Paywalled and hard-blocking sites are reported as limitations, not read
- Permit lookup currently limited to Brevard County FL
- Trial key required; rate and quota terms unpublished

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
