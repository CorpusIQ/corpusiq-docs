---
title: "TaiLexi AI MCP - Taiwan Legal Research for Agents"
description: "Taiwan legal research MCP server that searches court judgments, indictments, statutes, administrative interpretations and constitutional rulings in plain language. A proprietary index of 20M+ documents with official source links, per-result summaries and citation counts. Token-authenticated hosted endpoint."
category: IP/Legal
stars: "n/a (hosted service, no public repo)"
added: 2026-09-03
source: "mcpservers.org /all listing (www-twlawbot-com-mcp)"
relevance: ★★★
tags: [legal-research, taiwan, judgments, statutes, compliance]
---

# TaiLexi AI MCP - Taiwan Legal Research for Agents

**Hosted MCP server (token-authenticated)** - legal research for Taiwan built on a proprietary search index rather than a wrapper around official interfaces. Verified endpoint at mcp.twlawbot.com/mcp (401 without a token proves liveness). The vendor's design goal is AI-readable legal data: summaries and citation counts on every result so agents know which documents to deep-read.

## Spec Block

| Field | Value |
|---|---|
| Server name | TaiLexi AI (twlawbot.com) |
| Endpoint | https://mcp.twlawbot.com/mcp |
| Transport | Streamable HTTP |
| Auth | Token (obtain via twlawbot.com) |
| Coverage | 20M+ court judgments, 1M+ indictments, 100K+ judicial interpretations, 50K+ administrative interpretations, 10K+ laws (from 1928) |
| Verification | Every result carries an official source link (Judicial Yuan, Ministry of Justice, Laws and Regulations Database) |
| License | Proprietary hosted service |

## Why This Matters for Operators

Taiwan legal data is fragmented: indictments are not searchable on the Judicial Yuan judgment system, and administrative interpretations that finance and compliance teams use daily are scattered across the FSC, central bank and industry association sites. TaiLexi collects both, plus the full set of constitutional court rulings and grand justice interpretations, and weights authoritative interpretations above ordinary judgments in search ranking. For compliance, diligence and dispute work, the agent sees the authoritative answer first, not a keyword-matched district-court judgment.

## Tools & Capabilities

Capability-level table from the vendor's listing and site; anonymous enumeration is refused by token auth.

| Capability | Description |
|---|---|
| Judgment and interpretation search | Plain-language semantic search across judgments, interpretations and indictments |
| Full-text retrieval | Pull complete judgment text by case number |
| Statute lookup | Look up statutes directly, so agents do not cite hallucinated articles |
| Colloquial court filter | Filter by plain names such as "Supreme Court" or "Taipei District Court" |
| Indictment and interpretation search | 1M+ indictments and 50K+ administrative interpretations, otherwise hard to find |
| AI-optimized results | Each result includes a summary and citation count; ranking weights constitutional rulings first |

## Installation

Add `https://mcp.twlawbot.com/mcp` as a remote MCP server in any MCP client, then supply the token obtained from twlawbot.com.

## Configuration

Token authentication (the endpoint answers 401 invalid_token without one). Pricing is not published on the directory listing; the vendor site is in Chinese and positions the service as "set up once, use permanently" for Claude, GPT and ChatGPT users.

## Business Relevance

Taiwan-market operators need this for due diligence on counterparties, compliance reviews of administrative interpretations, and dispute preparation. Financial and legal teams get the interpretation layer (FSC, central bank, guild letters) that ordinary judgment search cannot reach, with official links for per-document verification.

## Integration with CorpusIQ

Legal research pairs with CorpusIQ's compliance and finance connectors: verify a Taiwanese counterparty's litigation exposure alongside company financials, and attach statute or interpretation citations to compliance workflows surfaced through CorpusIQ.

## Limitations

Token-gated (anonymous enumeration refused); pricing not published on the listing; data counts are vendor-published. Taiwan jurisdiction only. No public repo - the product is a hosted service.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Legalize MCP - Point-in-Time Legislation with Git Provenance](/hermes/mcp/servers/external/legalize-mcp)
- [mcp-sanctions - Watchlist Screening for KYC and AML](/hermes/mcp/servers/external/mcp-sanctions)
