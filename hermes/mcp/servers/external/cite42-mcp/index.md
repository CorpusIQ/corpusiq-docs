---
title: "Cite42 MCP - AI Search Visibility Tracking for AI Agents"
description: "MCP server with 26 tools for tracking brand rankings, AI citations and competitor presence across ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews. Covers AI search, rankings, competitor compare, citations, sentiment, SEO keywords, search trends, Reddit and YouTube trends, plus scheduled trackers and stored run history. npx stdio client, API key auth, $1 free start."
category: SEO
stars: n/a (new listing)
added: 2026-09-15
source: "mcpservers.org /all page 2 + vendor docs at cite42.dev/docs"
relevance: ★★★
tags: [ai-visibility, geo, citations, brand-monitoring, competitor-tracking, keyword-research, trends, trackers, api-key, self-hosted]
---

# Cite42 MCP

**Where your brand shows up when the answer engine answers.** Cite42 is an AI search visibility tracker: 26 tools that monitor brand rankings, AI citations and competitor presence across ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews, plus keyword research, search trends, Reddit and YouTube trends, and scheduled monitoring through trackers.

```
Server type: stdio (npx, local)
Auth: API key (CITE42_API_KEY, shown once when created at cite42.dev/app/keys)
Endpoint: npx -y @cite42/mcp (REST API available for non-MCP environments at cite42.dev/docs/api)
Tools: 26 (search, rankings, compare, citations, sentiment, keywords, trends, trackers, run history)
Pricing: $1 free start; billed scheduled, manual and live-data calls; free tracker management and history reads
Category: SEO / AI Visibility
Built by: Cite42 (cite42.dev)
```

## Why This Matters for Operators

Traditional rank tracking answered "where am I on Google." The question operators now face is "where am I when the answer is generated" - inside ChatGPT, Perplexity, Gemini and AI Overviews, where the result is a paragraph, not ten blue links, and your brand either appears in that paragraph or does not exist for that buyer. Cite42 makes that measurable: per-model rankings for a question set, citation monitoring, competitor share of voice, and drift alerts when visibility moves.

The second half of the product is audience data: Reddit and YouTube trend tools surface where the category's conversation is actually happening, and SEO keyword tools connect it back to a search strategy. For a team running GEO, this is the measurement loop in one MCP server: prompt tracking, citation monitoring, and trend discovery.

## Tools & Capabilities

| Tool group | What it does |
|---|---|
| AI Search | Live answers from ChatGPT, Claude, Perplexity, Gemini and AI Overviews for tracked questions |
| AI Rankings | Per-model ranking of your brand for question sets |
| AI Competitor Compare | Side-by-side visibility across competitor brands |
| AI Citations | Which sources feed the answers, and how often your brand is cited |
| AI Sentiment | Brand sentiment inside AI answers |
| SEO Keywords | Keyword research volume and difficulty |
| Search Trends | Market trend queries over time |
| Reddit Trends | Trending topics in relevant subreddits |
| YouTube Trends | Trending videos and topics in the niche |
| Trackers | Scheduled monitoring with lifecycle management and stored run history |

## Installation

```bash
claude mcp add cite42 -e CITE42_API_KEY=$CITE42_API_KEY -- npx -y @cite42/mcp
```

Registers 26 tools in about 15 seconds. Create the key at cite42.dev/app/keys (shown once); the same key works for the REST API.

## Configuration

```json
{
  "mcpServers": {
    "cite42": {
      "command": "npx",
      "args": ["-y", "@cite42/mcp"],
      "env": {
        "CITE42_API_KEY": "your_key_here"
      }
    }
  }
}
```

The stdio client runs locally; the API key is the only credential, and calls are billed against the account credits.

## Business Relevance

- **Growth and GEO leads** get per-model visibility rankings and citation monitoring instead of manual prompt checks.
- **Founders** get competitor compare and sentiment for the brands they benchmark against.
- **Content teams** get Reddit and YouTube trend inputs for the content calendar, tied to keyword research.
- **Agencies** get scheduled trackers and run history to report client visibility movement over time.

## Integration with CorpusIQ

Cite42 measures the answers; CorpusIQ feeds them the data. A GEO workflow pairs them: use Cite42 to find the questions where the brand is absent from ChatGPT and Perplexity answers, pull the underlying business facts from CorpusIQ (GA4 traffic that proves intent, Stripe or QuickBooks data that proves outcomes), and turn the gap list into content grounded in the operator's real numbers. The loop closes when Cite42 trackers confirm the brand now appears in the answer set. No manual rank-check spreadsheet survives contact with this pairing.

## Limitations

- Brand new: fresh on mcpservers.org at sweep time; no long public track record.
- stdio-only MCP (no hosted remote endpoint); non-MCP environments use the REST API instead.
- Credit-billed calls: live and scheduled data calls cost credits, so long-run trackers are a recurring cost.
- English-first tooling; verify non-English question coverage in your markets.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
