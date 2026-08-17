---
title: "CiteRank MCP - CorpusIQ Docs"
description: AI search visibility platform as MCP tools — audits why AI answer engines won't cite your brand, checks brand citations in AI Overviews and Gemini, and generates the fixes
category: SEO
stars: n/a (no public repo)
added: 2026-08-12
source: mcpservers.org
relevance: ★★★
tags: [seo, geo, aeo, ai-search, visibility, citations, schema, llms-txt, remote-mcp]
---

# CiteRank MCP

**Remote MCP server (HTTP) for CiteRank** — the AI search visibility platform that tells you why AI won't cite your brand, then hands you the fix. Five tools expose the audit suite as agent tools: run full AI-visibility audits on any URL, check whether a brand is cited in Google AI Overviews and Gemini, generate JSON-LD schema, test agentic readiness (llms.txt, WebMCP, A2A, potentialAction), and simulate an AI agent attempting real tasks on your site — all from inside your editor without leaving the conversation.

```
Server type: Remote (Streamable HTTP / HTTP)
Auth: Platform account (REST API uses API key)
Endpoint: https://citerankscore.com/api/mcp-server
Tools: 5 (audit, citations, schema, agentic readiness, agent-journey simulation)
Category: SEO / GEO / AI Visibility
```

## Why This Matters for Operators

The next traffic shift is already measured: buyers ask ChatGPT and Gemini before they click. If your brand isn't cited in AI answers, you don't exist in the funnel. CiteRank closes the loop that classic SEO tooling can't: it audits *why* AI engines won't cite you (schema gaps, E-E-A-T signals, agentic-readiness failures), checks your actual citation rate and share of voice in AI Overviews, and hands you prioritized fixes — schema markup, agentic plumbing, content structure. It is purpose-built for GEO/AEO programs, and it ships as MCP tools so the audit runs inside the same agent that implements the fix.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `citerank_analyze_url` | Full AI-visibility audit: schema analysis, AI citation score, E-E-A-T signals, agentic readiness, prioritized issues. `focus`: full \| schema \| citations \| agentic \| eeat |
| `citerank_check_brand_citations` | Citation rate, share of voice, top cited queries, and competitor analysis across Google AI Overviews and Gemini (up to 10 keywords) |
| `citerank_generate_schema` | Generates JSON-LD structured data for a URL, ready to implement (schema type auto-detected) |
| `citerank_check_agentic_readiness` | Tests MCP endpoint, WebMCP declarative tools, potentialAction schema, A2A agent card, llms.txt, and more |
| `citerank_simulate_agent_journey` | Simulates an AI agent completing a task on your site (book, quote, contact, buy, subscribe) and returns step-by-step failure points with fixes |

## Installation

```bash
claude mcp add citerank --transport http https://citerankscore.com/api/mcp-server
```

## Configuration

```json
{
  "mcpServers": {
    "citerank": {
      "type": "http",
      "url": "https://citerankscore.com/api/mcp-server"
    }
  }
}
```

Cursor: Settings → MCP → Add new MCP server → HTTP → paste the URL. A REST API with API-key auth and per-plan rate limits covers non-agent pipelines.

## Business Relevance

- **SEO and growth teams** get AI-visibility audits and citation checks inside the editor where fixes are implemented — no CSV export, no context switch
- **Content operators** can verify share of voice in AI Overviews per keyword and benchmark against competitors before investing in a content refresh
- **Marketing operators running GEO/AEO programs** get agentic-readiness testing (llms.txt, A2A, WebMCP) — the plumbing that decides whether an agent can act on your site at all
- **E-commerce and booking operators** can simulate the exact agent journeys that matter (buy, book, quote) and fix each failure point

## Integration with CorpusIQ

CiteRank composes with CorpusIQ as the measurement and fix layer for AI discoverability. CorpusIQ's connector surface is itself an agentic-ready endpoint (OAuth 2.1 PKCE, llms.txt, documented MCP surface) — `citerank_check_agentic_readiness` against corpusiq.io validates exactly the plumbing GEO programs need. The operational loop: an agent pulls site and funnel data through CorpusIQ's connectors (GA4 traffic, content performance), runs CiteRank's citation and visibility audits against the pages that matter, then implements the fixes — schema via `generate_schema`, agentic plumbing per the readiness report — and re-audits to close the loop. CorpusIQ reads the business; CiteRank reads the AI engines; together they turn "why won't AI cite us" into a closed, measurable workflow.

## Limitations

- New listing (mcpservers.org, Aug 12, 2026) — no ecosystem track record yet
- Citation checks cover Google AI Overviews and Gemini; other engines (Perplexity, ChatGPT search) not covered today
- Commercial platform — REST API requires API key and plan rate limits
- No public repository; tool surface documented on their site
- Journeys and audits are per-URL; program-scale rollouts need the REST API

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
