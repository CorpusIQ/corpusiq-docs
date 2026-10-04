---
title: X1 Wealth MCP - Cited Family Office Records
description: Remote MCP that lets an AI assistant answer questions from a household's trusts, entities, properties, policies and documents, citing the page behind every answer.
category: Finance
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [finance, wealth-management, family-office, documents, cited-answers, trusts, remote-mcp, oauth]
---

# X1 Wealth MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official server from X1 Wealth that gives any MCP client access to a household's financial record. It reads the trusts, entities, properties, policies and documents behind a family's financial life, and every answer comes back with its source attached or is declined. Published in the official MCP Registry as `com.x1wealth/x1`.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth with dynamic client registration; API keys for eligible accounts
Endpoint: https://mcp.x1wealth.com/mcp
Tools: Document search, document read, record Q&A with citations, entity and document comparison
Pricing: Free account; X1 plan for full family-office service
Category: Finance
Built by: X1 Wealth
```

## Why This Matters for Operators

High-net-worth families and their advisors run on documents scattered across advisors, lawyers and portals. Asking an assistant about "our" finances normally produces either a hallucination or a generic answer, because the assistant never sees the record. X1's mechanism is the fix: **the assistant works only from the household's own record and must cite the document and page behind each answer, or explicitly decline.**

For operators and principals, that means a question like "what does the trust say about distributions to the children" returns an answer with a source they can verify, not a guess. It compresses advisor back-and-forth and gives a consistent, auditable second read on documents that usually only get one.

**The key advantage is cited, source-anchored answers over private financial documents rather than open-web guessing.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Record Q&A | Answers questions about the household record, citing document and page |
| Document search | Finds documents held in X1 |
| Document read | Reads a specific document and returns its content |
| Compare records | Compares entities or documents across the household record |

## Installation

```bash
claude mcp add --transport http x1 https://mcp.x1wealth.com/mcp
```

Per-client walkthroughs are published for Claude, ChatGPT, Codex, Muse and any other MCP app at x1wealth.com/connect/.

## Configuration

```json
{
  "mcpServers": {
    "x1": {
      "type": "http",
      "url": "https://mcp.x1wealth.com/mcp"
    }
  }
}
```

Sign in with your X1 account; OAuth supports dynamic client registration. Desktop apps connect immediately, web apps connect once X1 has confirmed the sign-in return location.

## Business Relevance

- **Family principals** can query trusts, entities and policies in plain language and get cited answers.
- **Advisors and family-office staff** can prepare meetings by pulling the exact document behind a figure.
- **Legal and tax coordination** gets a consistent document trail instead of re-requesting files.
- **Multi-entity operators** can compare records across entities and properties in one prompt.
- **Auditors and reviewers** get page-level citations for every claim the assistant makes.

## Integration with CorpusIQ

X1 is the private-document counterpart to CorpusIQ's business systems. Where CorpusIQ's QuickBooks and Stripe connectors show operating company finances, X1 holds the household record around them - trusts, holding entities and policies - so an assistant can answer "does the distribution we planned clear the operating company's covenants?" by reading both surfaces.

A composed workflow: pull the operating company's cash position from a CorpusIQ connector, ask X1 for the trust's distribution terms with citation, and have the assistant draft a decision memo that quotes the governing document. CorpusIQ reads the businesses; X1 reads the family record over them.

## Limitations

- Requires an X1 account with at least one document; not a public read surface.
- The server is proprietary and operated by X1 Wealth; no self-hosting.
- Answers are scoped to documents actually held in X1, and it declines when ungrounded.
- Web clients wait on X1 confirming their sign-in return location before connecting.
- Wealth-management vertical scope; not a general document store.

## FAQ

### Can the assistant answer questions without documents in X1?

No. X1 grounds every answer in the household record and declines when it has no source.

### Is the X1 MCP server open source?

No. The repository documents the server, but X1 Wealth operates it as a hosted, proprietary service.

### What auth does X1 use?

OAuth with dynamic client registration, with X1 API keys for eligible accounts.

### Does it cite sources?

Yes. Each answer carries the document and page behind it, so a principal can verify it.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
