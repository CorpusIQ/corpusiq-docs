---
title: "cloro MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Live AI answer engine access for MCP agents — run prompts through ChatGPT, Gemini, Perplexity, Copilot, Grok, and Google AI Mode with cited sources and geo-targeting
category: Data & Analytics
stars: n/a (commercial)
added: 2026-08-12
source: mcp.so
relevance: ★★★
tags: [geo, aeo, ai-visibility, brand-monitoring, serp, market-research, remote-mcp]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/cloro-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# cloro MCP

**Remote MCP server (Streamable HTTP, API key) for cloro.** Gives any MCP-capable agent live access to AI answer engines and Google Search: it runs your prompt through ChatGPT, Google Gemini, Perplexity, Microsoft Copilot, Grok, and Google AI Mode, and returns each answer together with the sources it cited. Ten read-only tools, all annotated `readOnlyHint`.

```
Server type: Remote (Streamable HTTP)
Auth: API key (Bearer header, or key-in-path for restricted clients)
Endpoint: https://mcp.cloro.dev/mcp
Docs: https://cloro.dev/docs
Category: Data & Analytics / AI Visibility
```

## Why This Matters for Operators

The AI-answer layer is where brands are won and lost now — and most teams are blind to it. cloro turns "what does ChatGPT say about us?" into a structured tool call: answers with cited sources, per-engine, per-country, per-state. For GEO/AEO (generative/AI engine optimization) it answers the only question that matters: is our content being retrieved and cited, and by which engines?

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `scrape_chatgpt` / `scrape_gemini` / `scrape_perplexity` / `scrape_copilot` / `scrape_grok` | Prompt each AI engine and return the answer with cited sources |
| `scrape_google_ai_mode` | Google AI Mode answers with citations |
| `scrape_google` | Organic Google results, optional AI Overview + People Also Ask |
| `scrape_google_news` | News results |
| `list_countries` / `list_states` | Geo-targeting support per engine, so agents self-correct before calling |

Every result is scraped live at request time — no cache, no stored index. Responses report per-call credit usage. Device emulation (desktop/mobile) and multi-page results on the Google tools.

## Installation

```bash
claude mcp add cloro --transport http https://mcp.cloro.dev
```

## Configuration

```json
{
  "mcpServers": {
    "cloro": {
      "type": "http",
      "url": "https://mcp.cloro.dev/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_CLORO_API_KEY"
      }
    }
  }
}
```

Clients that can't set headers can embed the key in the path: `https://mcp.cloro.dev/YOUR_CLORO_API_KEY/mcp`. Create a key at [cloro.dev](https://cloro.dev/).

## Business Relevance

- **Brand monitoring** — track how each AI engine describes your brand and whether it cites you
- **Competitive research** — compare how engines answer the same commercial query for you vs. competitors
- **GEO / AI-search optimization** — verify your content is retrieved and cited in AI answers
- **Market comparison** — run the same prompt from multiple countries and states to see how answers change
- **SERP analysis** — organic results and AI Overviews as structured, agent-reasonable data

## Integration with CorpusIQ

cloro composes with CorpusIQ's data connectors as the measurement layer for AI-driven growth: an agent uses CorpusIQ (GA4, Search Console-style connectors, ad platforms) to see where traffic and revenue come from, and cloro to see whether AI engines are the reason — which brands they cite, from which countries. For teams running worldwide promotion or GEO programs, this is the feedback loop that closes the gap between "publishing content" and "being cited by the engines people actually ask."

## Limitations

- Commercial hosted service — API key and per-call credits billed to your account
- Live scraping means latency per engine; bulk queries cost credits fast
- Some engines don't support every country — check `list_countries` before scraping
- No caching — repeated identical prompts re-bill credits
- Not self-hostable; scraping-based answers can change run-to-run as engines update

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
