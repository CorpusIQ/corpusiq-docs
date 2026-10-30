---
title: Sprouts Data MCP - Business Corpus in Any Client
description: "Remote MCP server over 43M companies, 200M people and seven document collections, with per-field provenance and an async research run."
category: Business Data & Research
stars: n/a (new listing)
added: 2026-10-30
source: "mcpservers.org /all, card sproutsdata.ai"
relevance: ★★★
tags: [business-data, market-research, company-data, patents, funding, provenance, remote-mcp, oauth, api-key, credits]
last_updated: "2026-10-30"
---

# Sprouts Data MCP

**Forty-three million companies, two hundred million people and seven document collections behind one URL - and a citation on every field, including the fields it does not have.**

Sprouts Data publishes its platform corpus over MCP at `https://dashboard.sproutsdata.ai/mcp`. A bare `initialize` returns **HTTP 401** with the JSON-RPC error `-32000` reading `No credential. Send your Sprouts API key as an X-API-Key header (or Authorization: Bearer ...). Keys are issued in the dashboard; sk_dsp_test_ keys hit the same corpus at zero credit cost.` That last clause is the reason this entry is catalogued with evidence rather than a card: a test key reads the real corpus, so the tool list can be driven before anyone pays.

```
Server type: Remote (Streamable HTTP)
Auth: sk_dsp_ API key via X-API-Key or Authorization, or OAuth 2.1
Endpoint: https://dashboard.sproutsdata.ai/mcp
Surface: 9 tools, 6 prompts, 8 resources, inline cards (vendor counts)
Corpus: 43M+ companies, 200M+ people, 470M affiliation edges
Scopes: dsp.search.read, dsp.entities.read, dsp.agents.write, dsp.usage.read
```

## Why This Matters for Operators

Most business-data connectors answer one question: who do I sell to. They return rows and a confidence score, and the operator has no way to tell a stale record from a live one, or a missing company from a company the vendor never indexed.

The root cause is that a record set without provenance is only as trustworthy as the vendor's silence about its gaps. This corpus is shaped differently. Records carry per-field provenance, and the vendor documents "honest misses" as a product behaviour rather than an error state: `sprouts_entity_lookup` charges **nothing** when a record is not found, and `sprouts_coverage` returns a `not_in_index[]` array naming the gaps in plain language. The missing data is published deliberately, which is what makes the present data worth acting on.

Search also runs across nine categories, not one: companies, people, patents, news articles, trends, market reports, funding rounds, research papers and job openings. That changes the questions a chat can answer. Not only which companies fit a profile, but what a sector has been patenting, who raised in it, what the published research says, and whether the hiring pattern moved before the funding did.

## Tools and Capabilities

Twelve tools are documented on the vendor's tools page. The server landing page still says nine, so the twelve below is the reading of the page that lists them individually.

| Tool | What it answers | Credits |
|---|---|---|
| `sprouts_search` | Describe who to find, across all nine categories | 0.5 or 0.595 first 10 results, then 0.08 or 0.085 each |
| `sprouts_similar` | Name example companies, get ranked look-alikes | 2 first 10, then 1 per next 10 |
| `sprouts_entity_lookup` | Enrich identifiers you already hold, in batch | 1 per record found, misses free |
| `sprouts_relationships` | Two-sided questions over the affiliation graph | 2 first 10, then 1 per next 10 |
| `sprouts_org_chart` | The shape of one company's team, as counts | 1 per call, free when nobody matches |
| `sprouts_research_run` | One search cannot answer it | 1.02 to 85 by effort, charged only on success |
| `sprouts_lists` / `sprouts_list_edit` | Saved lists, CSV export, add and remove rows | Free |
| `sprouts_coverage` | What the index holds, and what it does not | Free |
| `sprouts_usage` | What this has cost, and replaying prior results | Free |
| `sprouts_feedback` | A result was wrong, missing or stale | Free |
| `sprouts_top_up` | Opens a payment page, never charges in chat | Free |

`org_chart` returns counts and never names, which is the right default for a headcount question and the wrong tool for a person question. `list_edit` is the only destructive tool in the set and is annotated as such, so a client that surfaces destructive hints will warn before a saved list is changed.

## What a Query Costs

Metering is in credits and the prices are published per tool, so a run can be budgeted before it happens. The two shapes worth knowing: `sprouts_search` is cheap at the first page and steep on the tail if a client pages deep, and `sprouts_research_run` is the only tool whose cost is open-ended by design, priced by effort and **charged only when the run succeeds**. An asynchronous run is submitted with `sprouts_research_run` and resumed by `run_id`, so a long research brief does not hold a conversation open.

## Connecting

1. Create an `sk_dsp_` key in the dashboard, or use an `sk_dsp_test_` key to read the same corpus at zero credit cost.
2. Add `https://dashboard.sproutsdata.ai/mcp` as a custom connector.
3. Send the key as `X-API-Key` or `Authorization: Bearer`, or sign in over OAuth 2.1 if the client can only take a URL.
4. Ask a coverage question first: `sprouts_coverage` is free and tells you what the index holds before you spend a credit.

In ChatGPT Business or Enterprise and Claude Team or Enterprise, a workspace administrator may need to enable custom connectors before any individual can connect an account.

## Limits Worth Knowing

Keys are per deployment and the failure is indistinguishable. Sprouts runs more than one deployment, each with its own dashboard, data and billing, and a key from the wrong one fails as `401 auth.invalid_key` - the same error as a revoked key, with nothing in it naming the environment. When a working config stops working, check which deployment the endpoint belongs to before anything else.

Two versioning facts are worth pinning: the data contract is `v1` and changes inside it are additive, and the tool names are frozen (`sprouts_search`, `sprouts_similar`, `sprouts_entity_lookup`, `sprouts_relationships`, `sprouts_research_run`, `sprouts_coverage`, `sprouts_usage`, `sprouts_feedback`, `sprouts_top_up` are all named as fixed). The protocol revision is negotiated per session, so there is nothing for a client to pin.

This pass verified the authorization boundary, the credential contract and the published tool and pricing pages. It did not drive `tools/list`, because that requires a key. The nine-tool figure on the landing page against twelve on the tools page is recorded rather than resolved.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)

## FAQ

### What does the Sprouts Data MCP server do?

It exposes a business corpus as tools inside Claude, ChatGPT, Cursor or any MCP client: 43M+ companies, 200M+ people and seven document collections covering patents, news, trends, market reports, funding rounds, research papers and job openings, with searching, look-alike accounts, batch enrichment, a relationship graph, saved lists and an asynchronous deep-research run.

### Does it need an API key?

Yes. It accepts a Sprouts `sk_dsp_` key as an `X-API-Key` header or as a Bearer token, and also supports OAuth 2.1 for clients that can only take a URL. Test keys prefixed `sk_dsp_test_` read the same corpus at zero credit cost.

### How is usage billed?

In credits, priced per tool and published per page of results. Searches cost 0.5 or 0.595 credits for the first ten results and 0.08 or 0.085 for each additional result. The asynchronous research run costs between 1.02 and 85 credits depending on effort, and is only charged when the run succeeds.

### Can the assistant see data the vendor does not have?

It says so explicitly. `sprouts_coverage` reports what each corpus holds plus a `not_in_index[]` list of the gaps, and a lookup miss is charged at zero, which means the absence of a record is a first-class answer rather than a silent one.

### What happens if a key stops working?

The most common cause is the wrong deployment. Each Sprouts deployment has its own dashboard, data and billing, and a key from another one fails as `401 auth.invalid_key`, which reads exactly like a revoked key and names no environment.
