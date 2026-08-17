---
title: "Legalcode MCP - CorpusIQ Docs"
description: Free legal research over MCP — statutes, case law, regulatory guidance and agreements across 44 jurisdictions, with 299 reusable legal workflows. Searches are processed, never stored; EU-hosted and privacy-by-design.
category: IP/Legal
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★
tags: [legal, research, compliance, contracts, case-law, citations]
---

# Legalcode MCP

**Remote legal-research server (Streamable HTTP, no API key)** — Legalcode plugs primary legal sources across 44 jurisdictions into the assistant an operator already uses. 391 primary sources, 299 reusable legal skills (NDA review, DPIA generation, contract analysis), and 26.5M documents, with the privacy posture operators care about: searches are processed, never stored, nothing is uploaded, and infrastructure is EU-hosted.

```
Server type: Hosted remote (Streamable HTTP)
Auth: None for Free tier — paste the endpoint URL
Endpoint: https://mcp.legalcode.md/mcp
Tools: Discover, Search, Fetch, Trace, Analyze (5 legal research operations)
Pricing: Free (30 requests/day, 600/month) · Pro $25/mo annual or $39.99 monthly (25K weighted units)
Category: IP/Legal
Built by: Fordæmi ehf (legalcode.md)
```

## Why This Matters for Operators

Legal AI platforms cost $500–1,200 a month and demand that client files get uploaded to yet another vendor. Legalcode inverts that: the operator brings the agent and the documents stay local, while Legalcode supplies verifiable law over MCP — statutes, judgments, and guidance with source identity so every answer can be checked. For a business operator, that converts "ask the lawyer about the GDPR deadline" from an invoice into a conversation with citations.

The free tier is genuinely usable (30 requests a day, 600 a month), which makes this the first serious legal-research MCP with a real zero-cost entry point.

## Tools & Capabilities

| Operation | Purpose |
|---|---|
| Discover | Explore available sources and skills |
| Search | Query legislation, case law, and guidance across 44 jurisdictions |
| Fetch | Retrieve full source text through MCP Fetch where supported |
| Trace | Follow amendment chains and version history |
| Analyze | Run packaged legal workflows (NDA review, DPIA generation, contract analysis) |

Weighted units: Discover/Search/Fetch cost 1 unit, Trace 2, Analyze 10. Pro adds patent search, signed full-document REST downloads, organization API keys, and 25,000 units a month.

## Installation

1. Copy the endpoint: `https://mcp.legalcode.md/mcp`
2. Paste it into the client — in Claude, Settings → Connectors → Add custom connector
3. Start a new chat and toggle Legalcode on (already-open conversations may not see the new server)
4. Ask a verifiable question: "What does the GDPR say about the deadline to report a data breach? Give me the exact article and a citation."

Live in Claude, ChatGPT, Copilot, Cowork, Claude Code, Codex, and any MCP-compatible client.

## Business Relevance

- **Contract review** before signing, with citations instead of vibes
- **Regulatory checks** across jurisdictions for market-entry questions
- **Privacy compliance** work with the guarantee that searches are never logged
- **Cost control** — replaces per-seat legal AI platforms with a $0–25/month protocol

## Integration with CorpusIQ

Legalcode complements CorpusIQ's business-data layer on the compliance side: CorpusIQ answers the operational questions (what does our spend, pipeline, and risk exposure look like), while Legalcode answers the legal ones (what does the law say and which workflow checks the draft). A due-diligence run could pull financial facts through CorpusIQ connectors and the regulatory position through Legalcode — both over MCP, both in the operator's own agent.

## Limitations

- Free tier caps at 30 requests/day — heavy research needs Pro
- Coverage depth varies by jurisdiction (check the source list for your markets before relying on it)
- Searches processed but "never stored" is a vendor promise — review the security documentation for your risk posture
- Legal answers still deserve human review; the tool supplies sources, not legal advice

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
