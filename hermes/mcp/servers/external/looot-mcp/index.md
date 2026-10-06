---
title: "looot MCP - One Balance for 2,350 Data APIs"
description: "One key and one prepaid balance for 2,350 data endpoints from 76 providers - email finding, enrichment, SEO, scraping and social data, pay per call."
category: Data & Analytics
stars: n/a (hosted gateway, looot.ai)
added: 2026-10-05
source: "mcp.so /feed (verified, featured)"
relevance: ★★★
tags: [data, enrichment, seo, scraping, social, pay-per-call, oauth, gateway, remote-mcp]
---

# looot MCP

**One key for the data providers your agent keeps needing.** looot is a prepaid data gateway: 2,350 endpoints across 209 platforms from 76 providers behind one account, one balance and one MCP endpoint. Email and phone finding, company and people enrichment, Google SERP and SEO data, social profiles and posts, web search and scraping, news, finance, ads, audio and video. Every call shows its price before it runs, and a failed call costs nothing.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in, or scoped agent tokens for headless use
Endpoint: https://api.looot.ai/mcp
Catalog: 2,350 endpoints, 209 platforms, 1,940 jobs, 16 categories (October 2026)
Pricing: Pay per call, no subscription - top up from $5; failed calls are free
Registry: ai.looot/looot
Built by: looot.ai
```

## Why This Matters for Operators

The usual pattern for agent data work is signing up for one more tool per need: an email finder here, a SERP API there, a scraper for the competitor pages, a social data provider after that. Each one has its own key, pricing page and failure modes. looot collapses that into a single prepaid balance and a single connection, priced per call.

**Every call is priced before it runs and a failed call costs nothing.** The gateway picks the cheapest provider that can answer a job and moves to the next one on a miss, so the agent does not have to know which vendor does what. Runs carry attempt-level evidence with receipts, so spend is auditable. Top-ups start at $5 and there is no monthly fee: you fund the balance, the agent spends it, and nothing runs until the price was shown.

## Tools

19 MCP tools, split between discovery (free) and execution (paid, priced up front):

| Tool | What it does |
|---|---|
| `search_catalog` | Ranked search by job in plain words, with job expansion, stats and access states |
| `search` | Catalog search by text or filters; returns endpoints to inspect and run |
| `discover` | Up to 5 eligible endpoints for a task, scored by relevance, evidence, availability and price |
| `discover_smart` | Judges a shortlist against a longer plain-English use case with one small AI call |
| `catalog_overview` | What the catalog covers, as categories, platforms and jobs, with counts |
| `inspect` | An endpoint's exact input and output, price formula, worst-case cost and a ready example |
| `run` | Runs an endpoint, a job by id (`job:<id>`) or a workflow, with idempotent retries and optional fallback |
| `runs_get` | One run's status, result and cost once settled |
| `runs_list` | Your run history, filtered by status or job, paged |
| `runs_cancel` | Stops a queued or running run |
| `runs_evidence` | Every attempt of a run with status, latency, receipt id and cost |
| `media_link` | A short-lived download link for a file a run produced (audio, image, video, PDF or large text) |
| `balance` | Available and reserved credit, the top-up link and its minimum |
| `top_up` | A Stripe checkout link for your human; the agent never enters card details |
| `capability_request` | Asks for a provider or job the catalog does not cover yet |
| `my_tools` | Tools your own workspace registered, and whether each is callable now |

Jobs are the key idea: you run `job:people.email.find` or `job:web.scrape.markdown` and looot routes it to whichever connected provider answers cheapest. Worked examples in the docs include email finding from $0.0036 per call, competitor pricing pages turned into markdown and diffed over time, and social listening feeds.

## Installation

Claude Code:

```bash
claude mcp add looot --transport http https://api.looot.ai/mcp
```

Or install the CLI, which configures common clients and gives scripts a full workflow:

```bash
npm install -g looot
looot init
```

JSON clients connect to the same endpoint:

```json
{
  "mcpServers": {
    "looot": {
      "url": "https://api.looot.ai/mcp"
    }
  }
}
```

For headless agents, CI and servers, create a scoped agent token in the dashboard and send it as a bearer token. The same API is also available over REST under `https://api.looot.ai/v1/` when a client needs plain HTTP.

## Business Relevance

- **Founders and growth teams** run lead research, enrichment and competitor monitoring without buying and stitching five data subscriptions.
- **Agencies** price client-facing data work per call instead of paying flat monthly minimums across tools.
- **Operations leads** get attempt-level receipts for every paid call, so agent data spend is auditable line by line.
- **Anyone running agents in the cloud** gives them one credential and one balance instead of a drawer of provider keys.

## Integration with CorpusIQ

CorpusIQ answers from the systems a business already owns: Stripe, QuickBooks, GA4, ad platforms and 40+ connectors, all read-only. looot supplies the outside world: the lead's work email, the competitor's new pricing page, the Google results for a target term. Composed, an operator can ask one question and get both halves: what the pipeline looks like inside, and who those prospects are outside. Both surfaces are read-only from the agent's side, and neither replaces the other: CorpusIQ is the system of record, looot is the data on demand.

## Limitations

- Prepaid balance only: runs draw down credit, and the agent hands you a Stripe link when it is low.
- Some endpoints need your own provider accounts connected first (sending email, reading mailboxes and ad accounts); the catalog marks those clearly.
- The AI-judged discovery modes cost extra on top of the data call.
- Data quality varies by provider; use `runs_evidence` to see which provider answered and at what cost.
- Fair-use rule from the vendor: above 100 calls in one go, the agent should confirm the estimated total with a human first.

## FAQ

### Do I pay a subscription?

No. looot is top-up only: add credit from $5, pay per call, and failed calls cost nothing. There is no monthly fee.

### How does the agent pick a provider?

You run a job, not a vendor. looot routes each job to the cheapest connected provider that can answer and falls back to the next one on a miss, with every attempt recorded.

### Can the agent spend without me?

The balance is prepaid and each call is priced before it runs, so the worst case is bounded by what you topped up. The agent can only fetch a Stripe top-up link; it never touches card details.

### Does it work in non-MCP clients?

Yes. The same gateway drives the `looot` CLI and a REST API, both with the same catalog and balance.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Nexlab MCP - Cited Data Intelligence Across 23 Servers](/hermes/mcp/servers/external/nexlab-mcp/)
- [ScrapeAtlas MCP - Social Data Access for Agents](/hermes/mcp/servers/external/scrapeatlas-mcp/)
- [Listar MCP - Verified B2B Contact Data](/hermes/mcp/servers/external/listar-mcp/)
