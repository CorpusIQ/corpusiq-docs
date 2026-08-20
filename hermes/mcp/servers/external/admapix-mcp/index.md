---
title: "AdMapix MCP - Competitor Ad Creative Intelligence"
description: "Local stdio MCP server over the AdMapix ad-intelligence API: search competitor ad creatives by keyword, advertiser, category or ad copy, filtered by format, country and date range, returning raw structured records with media URLs and metrics"
category: Marketing
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so GitHub issue #3663"
relevance: ★★
tags: [ad-intelligence, competitor-research, ad-creatives, marketing-intelligence, advertising-data, creative-research, stdio-mcp, api-key]
---

# AdMapix MCP

**Local stdio MCP server (uvx, API key) — raw competitor ad creative data from the AdMapix ad-intelligence API for MCP-compatible agents.** AdMapix MCP exposes a single `search_creatives` tool that queries the AdMapix ad library and returns structured JSON records — media URLs, first-seen dates, estimated impressions, days-active — rather than screenshots or summaries. Presentation and analysis are deliberately out of scope; the server is the data pipe, and the agent decides what to do with it.

```
Server type: Local stdio (Python, mcporter installer or uvx)
Auth: ADMAPIX_API_KEY environment variable
Endpoint: n/a (stdio; calls the AdMapix API)
Tools: 1 (search_creatives) with rich filtering
Pricing: requires an AdMapix API key from your admin
Category: Marketing / Ad Intelligence
Built by: fly0pants (PyPI admapix-mcp v1.0.0)
```

## Why This Matters for Operators

Competitor ad research is the most manual task in performance marketing: open the ad libraries, search each brand, screenshot what changed, paste into a doc, repeat next week. AdMapix MCP collapses that into a callable query. `search_creatives` accepts keyword, app name, advertiser, category, or ad copy, and filters by creative format (image, video, playable ad), country or region, and date range — then returns the raw API records with media URLs and metrics like estimated impressions and days active. Because the output is structured, an agent can diff competitor creative over time, spot what a rival is scaling, and feed findings into a brief without anyone touching an ad library UI.

The sorting surface is what makes it an intelligence tool rather than a search box: results can be ordered by first seen, relevance, estimated impressions, or days active, and pagination carries the same filters forward. That is the loop a growth operator actually runs — what is new, what is spending, what has been live forever — expressed as parameters instead of tab-hoarding.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_creatives` | Search competitor ad creatives by keyword, app name, advertiser, category, or ad copy; filter by creative type (image, video, playable), country/region, and date range; sort by first seen, relevance, estimated impressions, or days active; paginated |

Returns raw structured records: media URLs, first-seen dates, estimated impressions, days active, and other API metrics. Natural-language examples map cleanly: "video ads for puzzle games in the US" becomes `keyword="puzzle games"`, `creative_team`, `country_ids=["US"]`.

## Installation

```bash
# PyPI install (recommended)
uvx --from admapix-mcp admapix-mcp

# or installer script
git clone https://github.com/fly0pants/admapix.git
bash admapix/install.sh <YOUR_API_KEY>
```

The installer sets up Python, Node, mcporter, the server in `~/.admapix/`, the key in `~/.mcporter/mcporter.json`, and an OpenClaw skill. Windows PowerShell path is documented in the README.

## Configuration

```json
{
  "mcpServers": {
    "admapix": {
      "command": "uvx",
      "args": ["--from", "admapix-mcp", "admapix-mcp"],
      "env": {
        "ADMAPIX_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

The API key is issued by an AdMapix administrator — the MCP package itself is installable, but queries require account access.

## Business Relevance

- **Performance marketers** get competitor creative search and change tracking as agent tooling instead of ad-library tab-hopping
- **Creative teams** see what formats and angles rivals are running in a market before briefing new work
- **Brand operators** monitor when competitors launch fresh campaigns by first-seen sorting
- **Media buyers** filter by estimated impressions and days active to separate scaled winners from experiments

## Integration with CorpusIQ

AdMapix MCP feeds the planning side of a paid-marketing stack that CorpusIQ reads on the performance side. An operator pulls competitor creative intelligence through AdMapix — who is running video vs playable ads, in which countries, for how long — and then reads the same markets' spend and conversion reality through the CorpusIQ Meta Ads and Google Ads connectors. The pairing turns "what are they running" into "what are they running, and what is it costing us to hold share". GA4 traffic from the CorpusIQ GA4 connector closes the loop on which of your own landing pages the market responds to. The direction of flow: AdMapix MCP supplies market-side creative data; CorpusIQ reads the operator's own ad and site performance.

## Limitations

- Single-tool surface — one search endpoint, no write path, no alerts or monitoring
- Requires an AdMapix API key, which is account-gated rather than public
- Brand new listing — no community track record yet
- Stdio only — no hosted remote endpoint
- Raw records need an agent (or analyst) to interpret; no built-in summaries or recommendations

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
