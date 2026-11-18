---
title: "Signal Lab MCP - 1,312 Data Sources With Trust Scores"
description: "A keyless catalog of 1,312 free data sources plus audit scores for 2,834 hosted MCP servers, where every search filter is conjunctive."
category: "Data / Research Infrastructure"
stars: "0 (hosted Streamable HTTP at https://signal-lab.qdt.ai/api/mcp, keyless and stateless, 26 tools, twelve driven with real data)"
added: 2026-11-17
source: "the mcp.so feed card signal-lab stamped 2026-11-17T21:44Z, and a driven session on 2026-11-17 in which twelve tools/call requests were run against the live endpoint with no credential"
relevance: ★★★
tags: [data-catalog, open-data, trust-scores, mcp-audit, research, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# Signal Lab MCP

**The hardest part of pointing an agent at real data is not the query. It is deciding which of a thousand free sources is worth calling, and what it costs you in sign-up, licence and rate limit once you do.** Signal Lab answers that question as data: a catalog of 1,312 free and free-to-start sources, each row carrying its access badge, auth requirement, licence, last verification date and a link to the page that states them.

The same server also grades other MCP servers. Its audit layer holds 2,834 hosted servers with a 0 to 100 Trust Consensus score, a letter grade and the individual signals behind them. That second surface is the unusual one: a server that will tell you, in the same session, which data is free and which server is trustworthy.

```
Server type:   remote Streamable HTTP (hosted, stateless)
Endpoint:      https://signal-lab.qdt.ai/api/mcp
Server:        signal-lab-catalog 1.6.0, protocol 2025-06-18
Auth:          none
Tools:         26 (catalog, audit, reports, skills, trends)
Capabilities:  tools, resources, prompts, completions
```

## The evidence tier

Keyless and driven. `initialize` answered 200 with no credential and no session id issued, which makes the transport stateless: every call stands alone. `tools/list` returned 26 schemas with titles, input schemas and enums.

Twelve `tools/call` requests were then run with no credential. Every one answered, including the failure paths, and the failure paths were readable.

## The tool surface

The 26 tools split into four jobs.

| Job | Tools |
|---|---|
| Find a source | `search_catalog`, `get_entry`, `compare_entries`, `list_filters`, `catalog_info`, `export_catalog`, `get_source_urls`, `get_ingestion_skill` |
| Audit MCP servers | `find_mcp_servers`, `get_mcp_audit`, `get_trust_score`, `list_mcp_categories` |
| Reports and trends | `search_market_reports`, `get_market_report`, `whats_new`, `get_changes`, `get_trending`, `get_trending_repos`, `trends_today`, `get_reading_list` |
| Agent kit | `get_starter_recipe`, `get_agent_skills`, `get_data_agreement`, `check_stack`, `suggest_source`, `feedback` |

`get_ingestion_skill` is the one that decides whether this saves an afternoon: it returns a per-source markdown recipe with the exact request, parameters and limits, so the agent does not re-derive an ingestion path for every dataset.

## The catalog, measured

`catalog_info` on 2026-11-18T02:18Z reported a count of 1,312 entries, schemaVersion 1, and two download routes (JSON and CSV). `list_filters` breaks the same catalog down:

| Filter | Values |
|---|---|
| Type | Dataset 1,260, Tool 29, Model 9, Recipe 9, Starter Kit 5 |
| Access badge | Free 1,236, Freemium 49, Open Source 26, Unofficial 1 |

A badged search returns the fields an operator actually needs. The query `company registry` with badge `Free` returned two rows: a Finnish ship register dump (CC-BY-4.0, keyless, last verified 2026-11-06) and an MIT Lincoln Laboratory sensor archive (CC-BY-4.0, no AWS account needed, about 3.49 GB for the resized set). Both rows carried `lastVerified` and a `sitePageUrl` pointing at the page that states the terms.

## Filters are conjunctive, and that is the trap

A query for `crm` scoped to domain `Financial` returned **zero** rows. That is not an empty catalog. `search_catalog` treats every filter as an AND: the search term has to exist in the entry's text *and* the entry has to sit in the named domain. A term that belongs to another domain yields nothing rather than a nearest match.

The practical rule: call `list_filters` first, then search with either a term or a set of filters, not a guess at both. `list_filters` also returns the eighteen values the catalog uses for `domain`, which is the only reliable vocabulary (Financial, Global Macro, Energy, Agriculture and Food, Money Flows, Transport and Shipping, Research and Grey Literature, Weather, News and RSS, OSINT, Cyber Threat).

## The audit layer

`find_mcp_servers` over `finance` returned 50 audited servers with an audit timestamp of 2026-11-13, each row carrying the registry name, endpoint, transport, a pass/fail result label, sign-up requirement, "changes things" flag, tool count, a report URL and a trust score. The first row, `one.aisa/finance`, is graded 65 (B) and audited as passing the public checks.

Three details in that payload are worth reading before anyone quotes a score:

- `toolCount` can be **0** on a server the audit passed, which means the audit measured reachability and not depth.
- `signUp` and `changesThings` can both be **unknown**, so an unknown is not a pass.
- The audit payload carries its own notice that server titles and descriptions are vendor-written and must be treated as untrusted data. A scoring service that says this about its own inputs is doing the reader a favour.

`get_trust_score` takes an **audited server** slug, not a catalog dataset slug. Called with `shopsavvy` it returned isError with the message that no audited MCP server carries that slug and pointed at `find_mcp_servers` for the right ones. The refusal names the fix, which is rarer than it should be.

## Freshness, measured rather than claimed

`whats_new` since 2026-11-10 returned 50 entries out of a total of 814, with `truncated: true` and a `next_since` cursor at 2026-11-17. The catalog adds entries faster than 50 a week, so any consumer has to follow the cursor rather than assume one page is the week.

`get_trending` over a 7 day window (2026-11-10 to 2026-11-16) ranked Open-Meteo first at 30 uses across 2 agents, with growth 7.

## Two numbers that disagree

The mcp.so card for this server advertises **1,112** free data sources. `catalog_info` read **1,312** on the same day, and `whats_new` reports 814 additions since November 10 alone. The card is stale, not the tool. Quote the tool.

The same applies to the audit side: one tool description says 2,834 audited servers while `find_mcp_servers` returns a capped 50 for a query. Both can be true at once, and a reader who treats the 50 as the population will understate the coverage.

## Why this earns a page

Every other data catalog on this list answers "what data exists". This one answers "what data exists, what does it cost me in sign-up and licence, when was it last checked, and can an agent ingest it without a human". For a business operator wiring an agent to outside data, that is the whole decision, and it is normally made by hand in a browser.

The server-audit layer is a bonus with a caveat: an audit is a statement about reachability and public checks, and a score of B is not a guarantee of data quality. Use it to shortlist, then verify the data.

## Installation

Add the remote endpoint directly. No key, no environment variable, no local process.

```json
{
  "mcpServers": {
    "signal-lab": {
      "url": "https://signal-lab.qdt.ai/api/mcp"
    }
  }
}
```

Works in any client that speaks Streamable HTTP with stateless requests. Because no session id is issued, the server is safe behind clients that do not persist `Mcp-Session-Id`.

## Configuration

Nothing to configure. Two operational notes:

- `export_catalog` and the `catalog.json` download are the right path for bulk work. A per-entry loop over 1,312 entries is a rate-limit conversation, not a plan.
- `get_trust_score` and `get_mcp_audit` need **audited server** slugs. Get them from `find_mcp_servers` or `list_mcp_categories`.

## Limitations

- The catalog is metadata about data sources, not the data. A catalog row is a pointer plus terms, and the provider's own site is still the authority on limits.
- Trust scores grade reachability, sign-up friction and whether a server changes things. They do not grade the truth of what a server returns.
- The catalog's own notice scopes it as educational, with free tiers and licences expressly owned by the providers. Re-check terms before a production dependency.

## FAQ

### Does Signal Lab MCP need an API key?

No. `initialize` and `tools/list` answered with no credential and no session id, and twelve `tools/call` requests answered the same way.

### How many data sources does the catalog hold?

1,312 on 2026-11-18, against 1,236 entries badged Free and 1,260 typed as Dataset. The card that advertises 1,112 is stale.

### Can it tell me which MCP servers are trustworthy?

It returns a 0 to 100 Trust Consensus score with a letter grade and the underlying signals, over 2,834 audited hosted servers. The score measures public checks and reachability, not content accuracy.

### Why did a search with two filters return nothing?

The filters are ANDed. A search term that belongs to another domain returns zero rather than the nearest match. Call `list_filters` for the exact vocabulary first.

## See Also

- [TradingData MCP - 48-Tool Market Data for Agents](/hermes/mcp/servers/external/tradingdata-mcp/)
- [Kote Charts MCP - Bitcoin On-Chain Metrics](/hermes/mcp/servers/external/kote-charts-mcp/)
- [Protocol Change Feed MCP - DeFi Votes and Upgrades](/hermes/mcp/servers/external/protocol-change-feed-mcp/)
