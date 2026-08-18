---
title: "Just Domain MCP - CorpusIQ Docs"
description: Domain availability and pricing checks for AI assistants — first-year and renewal costs from justdomain.ai, the domain registrar for businesses built with AI
category: Productivity
stars: n/a (new listing)
added: 2026-08-13
source: mcp.so
relevance: ★★
tags: [domains, domain-registration, branding, business-ops, remote-mcp]
---

# Just Domain MCP

**Remote MCP server (Streamable HTTP, no auth) from Just Domain.** A read-only domain research surface: an AI assistant checks domain availability and both prices — first year and renewal — then hands back a checkout link for justdomain.ai. Read-only by design: no purchase ever happens inside the chat. Built for the moment a founder or operator is naming a business, a product, or a sub-brand and wants the domain economics next to the shortlist, not in another tab.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://mcp.justdomain.ai/
Tools: Domain availability check, first-year + renewal pricing lookup, checkout link generation (live tool list served from the endpoint)
Pricing: Free to query; registration happens on justdomain.ai
Category: Domains / Business Ops
Built by: Just (github.com/just-done/just-domain-mcp)
```

## Why This Matters for Operators

Domain research is a naming-adjacent chore that happens in every rebrand, product launch, and microsite decision. Agents can already brainstorm names; what they could not do was close the loop on availability and real pricing — especially renewal pricing, which is where registrars quietly make their margin. Just Domain puts both numbers in the chat, so the assistant can rule out names whose renewal cost doubles next year, and only then produce a checkout link.

**The read-only design is the feature.** The agent can never register, charge, or commit — it only ever hands back a link that a human opens and completes. That is the same human-gate pattern now showing up across the better new MCP servers, and it makes the server safe to wire into any assistant.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Domain availability check | Search availability for a candidate domain across supported TLDs |
| Pricing lookup | Return first-year AND renewal price for an available domain |
| Checkout link | Hand back a justdomain.ai registration link for a chosen domain |

The server exposes an agent-skills index at `https://mcp.justdomain.ai/.well-known/agent-skills/index.json`; the live tool list is fetched from the endpoint itself.

## Installation

```bash
claude mcp add just-domain --transport http https://mcp.justdomain.ai/
```

Works with Claude Code, Codex, Cursor, and VS Code. No API key, no account, no install — the endpoint is public.

## Configuration

```json
{
  "mcpServers": {
    "just-domain": {
      "type": "http",
      "url": "https://mcp.justdomain.ai/"
    }
  }
}
```

## Business Relevance

- **Founders naming a company** get availability plus true first-year and renewal pricing for every shortlisted name before the brand discussions start.
- **Operators launching sub-brands or product lines** check domain economics without routing every query through a broker or registrar rep.
- **Agencies running naming sprints** let the assistant produce a priced shortlist — the human still completes every purchase.

## Integration with CorpusIQ

Just Domain is a research layer, not a data layer — that is where CorpusIQ fits. The workflow composes: the assistant checks domains over Just Domain while CorpusIQ connectors supply the business context that decides which names matter (which products are growing in Shopify, which channels GA4 shows pulling traffic, which campaigns Ahrefs and Search Console show ranking). CorpusIQ answers "what deserves a domain"; Just Domain answers "what does that domain cost". They never overlap on data, which makes them a clean pair rather than competitors.

## Limitations

- Brand new — no track record yet, tool list not yet indexed by mcp.so's crawler
- Read-only by design: registration happens on justdomain.ai, outside the MCP surface
- Single registrar — pricing only reflects justdomain.ai, not the wider market
- No bulk search surface documented yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
