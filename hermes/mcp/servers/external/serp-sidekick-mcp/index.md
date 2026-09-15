---
title: Serp Sidekick MCP - Live SEO and AI-Visibility Data
description: "Remote MCP server that gives any AI assistant real SEO data: keyword research with live search volumes, Search Console query mining for the pages sitting just off page one, competitor ranking gaps, single-page audits, and brand visibility checks across ChatGPT and Google AI Overviews. 15 tools over OAuth at serpsidekick.com/mcp; free tier for your own Search Console data, credits from $5."
category: SEO
stars: n/a (new listing)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + vendor docs at serpsidekick.com"
relevance: ★★★
tags: [seo, geo, aeo, keyword-research, search-console, competitor-analysis, ai-visibility, google-rankings, oauth, remote-mcp]
---

# Serp Sidekick MCP

**Give your AI real SEO data.** Serp Sidekick is a remote MCP server that turns SEO questions into live lookups instead of guesses: which phrases people actually search, which queries your site already ranks page-two for, what competitors rank for that you do not, and whether ChatGPT and Google AI Overviews mention your brand at all. Paste one URL, sign in with Google, and ask in your own words.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Google sign-in; no API key)
Endpoint: https://serpsidekick.com/mcp (401-verified live, Sep 14 2026)
Tools: 15
Pricing: Free tier (your Search Console data); pay-as-you-go credits, $5 buys 5,000 credits, never expire
Category: SEO / GEO
```

## Why This Matters for Operators

SEO questions show up in every growth conversation, and the honest answer usually requires data: is anyone searching for this, which pages need attention, what should we write next, where is the competitor winning. Serp Sidekick answers those inside the assistant you are already using:

- **"Is anyone searching for this?"** - turns an idea into the phrases people type, with demand and difficulty for each.
- **"Which pages need attention?"** - reads your Search Console data and finds queries sitting just off page one, with the one fix worth doing this week.
- **"What should I write next?"** - related keywords grouped by intent, and which three pages to write first, in what order.
- **"What do my competitors rank for?"** - the terms a rival ranks for that you do not, and whether the gap is content or links.
- **"Does my brand appear in AI answers?"** - checks ChatGPT and Google AI Overviews for your brand against competitors, and shows which sites they cite instead.
- **"What needs fixing on this page?"** - single-URL audit that leads with the one fix that matters most.

Pricing is explicit per call: page audits from 1 credit, keyword lookups from 97 credits per run, competitor gaps from 169, AI visibility reports from 202. Every answer states the exact charge.

## Tools & Capabilities

15 tools across the search-data surface: keyword research with live volumes and difficulty, Search Console performance mining (calls, impressions, positions, indexing, read-only), competitor ranking comparison, page audits, keyword grouping by intent, and AI-answer brand monitoring. Google sign-in only; Config-file clients add the URL as a remote server with no command and no API key.

## Installation

**Claude** - Settings, Connectors, Add custom connector, paste `https://serpsidekick.com/mcp`, sign in with Google and approve. Start a new chat and ask an SEO question. For repeat use, enable the connector from the tools menu in each chat.

**Cursor** - Settings, MCP, add a new server, paste the URL, approve the sign-in in your browser.

**Config-file clients** - add the URL as a remote server entry:

```json
{
  "mcpServers": {
    "serp-sidekick": {
      "type": "http",
      "url": "https://serpsidekick.com/mcp"
    }
  }
}
```

Want your own site's data? After signing in, connect a Search Console property from the dashboard. That part is free.

## Business Relevance

- **Founders** validate demand for a product or landing page before writing it, with real volumes instead of assumptions.
- **SEO specialists** turn Search Console mining, competitor gaps and page audits into one conversational workflow.
- **Content teams** get the next three pages, ranked, from live data rather than a keyword dump.
- **Brand teams** see whether AI answers mention them and which sites get cited in their place, the metric that matters as AI Overviews expand.
- **Agencies** run the same checks for client domains and bring the reasoning to the client meeting.

## Integration with CorpusIQ

Serp Sidekick answers the demand side of the funnel (what people search, what ranks, what AI answers say) and CorpusIQ answers the business side (what the site and the back office actually did). With a CorpusIQ connection, the same assistant that pulls keyword and AI-visibility data also reads GA4 sessions, Search Console performance, Shopify orders and Stripe revenue with source citations, so a content decision runs from "this query is winnable" to "this page produced these conversions" without leaving the conversation.

## Limitations

- **Credits are consumed per call** and the expensive operations (competitor gaps, AI visibility) start at 104 to 202 credits per run.
- **Search Console access is read-only** and optional; without it you get the demand data but not your own query mining.
- **Google account required** (OAuth sign-in); no key-only path is documented for config that cannot open a browser.
- **New listing**: no third-party track record at catalog time.
- **Google-centric** data (volumes, positions, AI Overviews); other engines are not covered.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [geolint MCP - AI Search Readiness Linter for Websites](/docs/hermes/mcp/servers/external/geolint-mcp)
- [Attensira MCP - AI-Search Visibility Data for Agents](/docs/hermes/mcp/servers/external/attensira-mcp)
