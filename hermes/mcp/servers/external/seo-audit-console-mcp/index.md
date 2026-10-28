---
title: "SEO Audit Console MCP - 143 Checks on Your Own Data"
description: "Search Console plus a first party crawl plus optional DataForSEO in local SQLite, ranked into one fix list where every finding is labelled."
category: Marketing / SEO
stars: n/a (free, Apache-2.0, local)
added: 2026-10-28
source: "npm registry record for @houtini/seo-audit-console 0.17.0 published 2026-08-03 and modified 2026-10-25, Apache-2.0, and the vendor README as published on mcp.so covering 64 tools, 143 checks, the storage model, the optional paid keys and the source repository github.com/houtini-ai/seo-audit"
relevance: ★★★
tags: [seo, search-console, crawl, technical-audit, core-web-vitals, ai-overviews, local-sqlite, claude-desktop]
last_updated: "2026-10-28"
---

# SEO Audit Console MCP

**Every SEO tool in the market answers with a list. The operator's problem is that the list has 300 rows and no order, and no tool will tell you which row is worth a day of work.**

```
Server type: Local (stdio)
Install:     npx -y @houtini/seo-audit-console
Auth:        Google service account with access to the property
             DataForSEO, Majestic and CrUX optional
Tools:       64
Checks:      143, ranked by recoverable clicks
Storage:     local SQLite, joined on a normalised URL
Licence:     Apache-2.0
```

## Why This Matters for Operators

Technical SEO fails quietly. A page that ranks and is blocked by robots.txt reads as healthy in a rank tracker and as zero clicks in Search Console, and neither report on its own says why. The joins are where the answer is: traffic to dead URLs, high-demand pages buried deep in the site, sitemap and index reconciliation, pages that lost clicks while a third-party estimate still says the traffic is fine.

This server does the join rather than the report. It pulls Search Console history for a property you own, runs a polite first-party crawl of that site, stores both in SQLite keyed on a normalised URL, and then ranks 143 checks by recoverable clicks. The labelling is the part that earns trust: every finding is marked deterministic, backed by the bytes it cites, or judgement. An operator can act on the first class without re-checking it.

The second thing it does that most audit tools do not is write the fix, not just the finding: JSON-LD to paste, a 301 map, internal-link suggestions, all generated from the evidence in the store.

## What It Returns, Verified

The package is real and current: `@houtini/seo-audit-console` on npm at 0.17.0, published 2026-08-03, last modified 2026-10-25, Apache-2.0, with the source at `github.com/houtini-ai/seo-audit` and docs in the repository's `manual/` folder.

The published surface, from the vendor README:

- **143 checks** across crawlability, indexation, canonicals, redirects, hreflang, structured data, Core Web Vitals, internal PageRank, cannibalisation, soft 404s, JavaScript-render divergence and AI-answer readiness
- **Search Console and crawl joins**, including decay and lost queries over time
- **64 tools**, with long jobs running in the background and every figure carrying its date window
- **Live dashboards** in chat or a local browser tab, plus a shareable HTML export
- **A portfolio view** where measured Search Console clicks sit beside estimated traffic, referring domains, domain rank and AI mentions from Google AI Overviews and ChatGPT, with a needs-attention tab
- **AI search readiness**: whether an AI Overview cites the page, passage scoring on a local model with no API cost, an agent-readiness score, and content recon that explains why a page is losing

Setup is a service-account key with access to the property and nothing else. Search Console data and the crawl are free. DataForSEO is optional and pay-as-you-go, cached for 20 days, and the vendor prices a weekly portfolio refresh for eight sites at about $0.22. Majestic adds Trust Flow on link prospects, CrUX is free and adds real-user Core Web Vitals.

It also runs under the Docker MCP gateway with a job-runner sidecar, which is the shape a long crawl needs if the client has a short timeout.

## Limits Worth Recording

- **One property at a time, and only yours.** The crawler is for sites you own, identifies itself and respects robots.txt. Competitor data comes from DataForSEO, never from crawling their site.
- **The best findings need the paid key.** Everything built on Search Console history and the crawl is free. Competitor, keyword, backlink and AI-search data unlock with DataForSEO, so a fully free run is an audit of your site, not of your market.
- **No endpoint to probe.** This is a local stdio server, so there is no JSON-RPC surface to drive from a sweep and no server-side tool list to confirm. The install path, the package version and the published checks are the evidence, and the honest statement is that the tool list was not enumerated by hand.
- **Node 20 or newer**, and the crawl is polite by design, so a large site takes real time rather than finishing in a minute.
- **Everything is local.** Nothing leaves the machine except calls to the optional third-party APIs, which also means the audit is only as current as the last refresh you ran.

## Wiring It Up

```json
{
  "mcpServers": {
    "seo-audit-console": {
      "command": "npx",
      "args": ["-y", "@houtini/seo-audit-console"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/service-account.json"
      }
    }
  }
}
```

```bash
claude mcp add seo-audit-console --env GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json -- npx -y @houtini/seo-audit-console
```

Then ask it to refresh a domain and run the audit. The optional keys are `DATAFORSEO_USERNAME` and `DATAFORSEO_PASSWORD`, `MAJESTIC_API_KEY` and `CRUX_API_KEY`.

## FAQ

### Is it actually free?

Yes. The server is Apache-2.0, Search Console data and the crawl cost nothing, and the audit runs on a local SQLite file. Money only enters if you configure DataForSEO or Majestic, and the portfolio refresh quotes its cost before it runs.

### Does it replace a rank tracker?

No. It answers why a page underperforms, not where you rank today. For position tracking you still need a rank source; for the reason behind a drop, the Search Console history and the crawl are the better evidence.

### Can it audit a competitor's site?

Not by crawling it. Competitor pages, keywords, gaps and link intersects come from DataForSEO on demand, which is the API-clean path and the reason the crawl stays polite.

### Where does the data live?

In local SQLite files on your machine, joined on a normalised URL. The only outbound calls are the third-party APIs you configure, and DataForSEO responses are cached for 20 days.
