---
title: "Beamtrace MCP - AI Visibility Score Analysis for Agents"
description: "Beamtrace MCP, built by Elfsight, connects an agent to a brand's AI visibility data: analyze the Beamtrace score, explain what shifted it, see where a competitor is ahead, and pull the concrete fix behind each visibility gap. Five read-oriented tools over a hosted Streamable HTTP endpoint with API-key auth."
category: SEO
stars: 0
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [geo, ai-visibility, seo, brand-tracking, remote-mcp, elfsight]
---

# Beamtrace MCP - AI Visibility Score Analysis for Agents

**Remote MCP server (Streamable HTTP, API key)** - Beamtrace, from the Elfsight team, measures how visible a brand is to AI answer engines and hands the agent the analysis surface: current score, what shifted, competitor comparisons and the improvement actions behind each gap. Setup lives at beamtrace.com/setup.

```
Server type: Remote (Streamable HTTP)
Auth: API key (authorization header required)
Endpoint: https://beamtrace.com/api/mcp (probe-verified live, 401 without a key)
Tools: 5 (get_visibility, list_topics, list_prompts, list_competitors, list_improvements)
Pricing: Beamtrace plans at beamtrace.com
Category: SEO
Built by: Elfsight (elfsight.com); repo github.com/elfsight/beamtrace-mcp
```

## Why This Matters for Operators

When ChatGPT, Gemini or Claude answers a category question, the brands those engines cite win the pipeline. Most teams still have no read on whether they are cited at all. Beamtrace MCP turns that blind spot into an agent-queryable surface: the agent explains why the score moved, names the topics where competitors are being cited instead, and returns the specific fix behind a gap rather than a vague "improve your AI visibility" directive.

**The tool set is deliberately small and read-oriented - score, topics, competitor deltas, improvements - which makes it safe to hand to an agent that runs weekly visibility checkups on autopilot.**

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| get_visibility | The brand's Beamtrace visibility score with supporting breakdown |
| list_topics | The topics where the brand is or is not being cited by AI engines |
| list_prompts | Representative prompts where the brand does and does not surface |
| list_competitors | Competitor comparison showing where rivals are ahead |
| list_improvements | Concrete fixes behind each detected visibility gap |

## Installation

Create a Beamtrace account and follow the setup flow at beamtrace.com/setup, which issues the API key and client configuration for Claude, Cursor and other MCP clients.

```bash
claude mcp add --transport http beamtrace https://beamtrace.com/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "beamtrace": {
      "type": "http",
      "url": "https://beamtrace.com/api/mcp"
    }
  }
}
```

Attach the Beamtrace key as the bearer authorization header on requests. An unauthenticated initialize probe returns 401 with "missing authorization header" - the endpoint is live and key-gated.

## Business Relevance

- **SEO teams** get AI-answer-engine visibility as a weekly agent checkup instead of a quarterly consultant report.
- **Brand managers** see citation share versus named competitors per topic.
- **Content teams** get fix lists (topics, prompts, gaps) they can convert straight into briefs.
- **Agencies** run visibility monitoring across client brands from one tool.

## Integration with CorpusIQ

Beamtrace answers "are AI engines citing us"; CorpusIQ answers "did the traffic and revenue follow". A composed workflow: the agent pulls share-of-voice deltas and gap fixes from Beamtrace, tracks the resulting organic and paid performance through CorpusIQ's GA4 and Stripe connectors, and closes the loop on which fixes moved revenue.

## Limitations

- Brand new listing (mcp.so feed, Sep 7, 2026); repo carries registry metadata and a Cursor plugin, 0 stars, MIT.
- Five tools, all analysis-level; the platform's crawl and monitoring configuration stays in the Beamtrace web app.
- Tool outputs are summaries of the platform data; historical depth depends on the plan tier.

## See Also

- [Ranki MCP - SEO and AEO Audits](/docs/hermes/mcp/servers/external/ranki-mcp)
- [Encited MCP - SEO and AI Visibility for Agents](/docs/hermes/mcp/servers/external/encited-mcp)
- [CiteRank MCP - AI Search Visibility Audits](/docs/hermes/mcp/servers/external/citerank-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
