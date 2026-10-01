---
title: eCFR.io MCP - US Federal Regulations for Agents
description: "Free read-only MCP server for searching and reading the US Code of Federal Regulations, with legal citations linking back to ecfr.io."
category: Compliance
stars: n/a (hosted service, ecfr.io)
added: 2026-10-01
source: "mcpservers.org /all (lrehmann/ecfr-mcp)"
relevance: ★★★
tags: [regulations, compliance, federal-law, legal-research, ecfr, government, remote-mcp]
---

# eCFR.io MCP

**Read US federal regulations without a legal database subscription.** eCFR.io is an independent mirror of the daily electronic Code of Federal Regulations, and its MCP server lets an agent search the current CFR text, fetch a regulation by path, and read it in full with citations that link back to the source.

```
Server type: Remote (Streamable HTTP)
Auth: None (public, read-only, no API key)
Endpoint: https://ecfr.io/mcp
Tools: 3 (search, read, list titles)
Pricing: free
Category: Compliance
Built by: lrehmann (published in the official MCP registry as io.ecfr/ecfr)
```

## Why This Matters for Operators

Regulatory text is the kind of source that normally lives behind a subscription or a slow government interface. An operator who needs to check what a rule actually says, or quote it in a policy document, usually ends up with a browser tab and a copy-paste. This server puts the same text behind a tool call, so an agent can answer a compliance question and cite where the answer came from.

The citation handling is the part that matters. Every result carries an inline Markdown citation and a legal citation, both linking to ecfr.io, so a drafted policy or a due-diligence note arrives traceable to the regulation rather than to a model's memory. The server also returns source and body dates plus stale flags, which lets an agent say when a provision was last updated instead of presenting old text as current.

For any operator-facing workflow that touches US federal rules, advertising claims, employment, environmental or financial obligations, this turns a research chore into a query.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_regulations` | Search current CFR text or a citation such as 31 CFR 10.1; returns snippets with legal and inline citations |
| `get_regulation` | Read a regulation by the canonical path returned by search, with dates, stale flags and paginated text |
| `list_titles` | List the CFR titles available |

## Installation

```
claude mcp add --transport http ecfr https://ecfr.io/mcp
```

The endpoint is stateless, so no session ID or API key is involved. Any client that supports Streamable HTTP can connect with the URL alone.

## Configuration

```json
{
  "mcpServers": {
    "ecfr": {
      "type": "http",
      "url": "https://ecfr.io/mcp"
    }
  }
}
```

A local stdio adapter also ships in the `lrehmann/ecfr-mcp` repository for Node.js 20 or later, via `npm ci && npm run build && npm start`.

## Business Relevance

- **Compliance and legal operations** can pull the actual text of a rule into a review workflow and keep the citation attached to the claim.
- **Policy and content teams** can verify a regulatory statement before it goes into published material, with a source link on every quotation.
- **Due diligence and risk review** can check which obligations apply to a market or product without a seat on a legal database.
- **AI agents** get a grounded regulatory source they can quote with attribution rather than recalling rules from training data.

## Integration with CorpusIQ

CorpusIQ's business connectors supply the operating data, and eCFR.io supplies the rule text that governs it. An agent running on CorpusIQ can pull a compliance-relevant figure from the Finance or accounting connectors, then read the matching regulation through this server and return both the number and the citation in one answer. For teams tracking regulated activity, that turns a two-tool research loop into a single composed workflow, with CorpusIQ as the source of business truth and eCFR.io as the source of regulatory truth.

## Limitations

- Free and public, but explicitly an independent mirror of the unofficial daily eCFR compilation; the vendor directs users to official sources for legal reliance.
- Read-only; there is nothing to approve or roll back, but nothing to write either.
- US federal regulations only, so state and non-US rules are out of scope.
- Three tools, so it is a focused regulatory reader rather than a broad legal research platform.

## FAQ

### What does the eCFR.io MCP server do?

It lets an AI agent search the current US Code of Federal Regulations, fetch a regulation by path, and read the text with legal and inline citations that link to ecfr.io.

### Is the eCFR.io MCP server free?

Yes. It is public, read-only and needs no API key.

### How many tools does it expose?

Three: `search_regulations`, `get_regulation` and `list_titles`.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
