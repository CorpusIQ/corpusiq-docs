---
title: "Taiwan Law MCP - CorpusIQ Docs"
description: Taiwan legal research over MCP — statutes, court judgments, constitutional interpretations and legislative history from official government sources, free with no API key.
category: Compliance
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [legal-research, taiwan, statutes, judgments, compliance, government-sources, free, remote-mcp]
---

# Taiwan Law MCP

**Remote MCP server (Streamable HTTP, no auth)** — a server for verifying Taiwanese law against official government sources: statutes (Ministry of Justice), court judgments (Judicial Yuan), constitutional interpretations, and legislative history (Legislative Yuan). Fourteen tools, free, no API key, no signup. Registry name `tw.org.legaltech/taiwan-law`.

```
Server type: Remote (Streamable HTTP) or self-hosted (npx / Docker)
Auth: None
Endpoint: https://legaltech.org.tw/mcp
Tools: 14 (intent analysis, statutes, judgments, interpretations, legislative history)
Pricing: free
Category: Compliance
Built by: LegalTech Taiwan (legaltech.org.tw)
```

## Why This Matters for Operators

Legal research by an agent fails in one of two ways: it hallucinates citations, or it summarizes a summary and loses the source. Taiwan Law MCP eliminates both by making the official source the tool surface: every result carries a `source_url` to the government record, judgments are queried live with zero stored copies, and the model is instructed to open the returned URLs when quoting.

**The intent-analysis gate is the notable design choice**: `analyze_legal_intent` runs before a query to analyze research intent and privacy risk, and explicitly does not draw legal conclusions about the case. That separation keeps the tool a verifier of law rather than a pretend lawyer, and the published guidance states plainly that the service is research assistance, not legal advice.

Coverage spans the four sources an operator doing business in Taiwan actually needs: national statutes and administrative interpretations, published judgments, constitutional-court decisions, and the legislative record of a bill's versions and progress.

## Tools & Capabilities

| Source | Tools |
|---|---|
| Intent analysis | `analyze_legal_intent` — research intent and privacy risk before querying |
| Statutes & interpretations | `search_taiwan_laws`, `search_taiwan_regulations`, `get_taiwan_pcode`, `search_moj_interpretations`, `get_moj_draft_announcements` |
| Judgments | `search_taiwan_judgments`, `get_taiwan_judgment` |
| Constitutional interpretations | `search_taiwan_interpretations`, `get_taiwan_interpretation`, `get_taiwan_interpretation_citations` |
| Legislative history | `get_taiwan_law_progress`, `get_taiwan_law_versions`, `search_taiwan_bills` |

## Installation

```bash
claude mcp add --transport http taiwan-law https://legaltech.org.tw/mcp
```

Self-host when data privacy matters: `npx taiwan-law-mcp` (Node 22+) or `docker run -d -p 8787:8787 -v tlm-data:/data legaltechtw/taiwan-law-mcp`, endpoint at `http://localhost:8787/mcp`. Questions never leave the local machine; statute and judgment lookups still connect directly to the official databases.

## Configuration

```json
{
  "mcpServers": {
    "taiwan-law": {
      "type": "http",
      "url": "https://legaltech.org.tw/mcp"
    }
  }
}
```

No credentials, no OAuth field to fill. For Claude.ai or ChatGPT, add it as a custom connector with the OAuth field left blank.

## Business Relevance

- **Operators with Taiwan entities** can verify the current text of the laws they must comply with
- **Compliance teams** get cited, source-linked answers instead of model recall
- **Legal ops** can trace a bill's progress and versions through the Legislative Yuan record
- **Risk researchers** can check judgments and constitutional interpretations against official records

## Integration with CorpusIQ

Taiwan Law MCP composes with the CorpusIQ compliance and document stack as the jurisdiction specialist. Where Legalcode MCP covers 44 general jurisdictions, Taiwan Law MCP goes deep on one — an operator's compliance sweep can cite Taiwan statutes with government URLs while the CorpusIQ document-intelligence tools organize findings, and the canonical context layer can store the verified citations as facts. For operators running Taiwan entities through the CorpusIQ connectors (QuickBooks for books, Stripe for payments), the legal server answers the question the financial connectors cannot: what the current law actually requires, straight from the official source.

## Limitations

- Brand new — no track record yet; listed August 17, 2026, public beta
- Taiwan jurisdiction only — no cross-border coverage
- Research assistance, not legal advice; judgments can be updated or removed by the courts
- Hosted endpoint is a third party (EU-adjacent privacy posture is not stated; self-host if confidential)
- Free tier is rate-limited as a public beta; reliability not SLA-backed

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
