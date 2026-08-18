---
title: "HelpDocs MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Connect AI assistants to your HelpDocs knowledge base. Search, read, draft, and update articles, reorganize categories, and pull analytics on what readers search for.
category: Productivity
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★
tags: [knowledge-base, documentation, support, customer-support, analytics, content-ops, productivity, remote-mcp]
---

# HelpDocs MCP

**Remote MCP server (Streamable HTTP, account authorization)** — the official HelpDocs connector that lets AI assistants work directly in your knowledge base. Search and read articles, draft and update content, reorganize categories, and pull analytics on what readers actually search for — all from the assistant's interface.

```
Server type: Remote (Streamable HTTP)
Auth: Account authorization flow
Endpoint: Per-account URL (Settings > AI > MCP Access)
Tools: Search, read, create/update/delete, analytics, account details
Pricing: Available on certain HelpDocs plans
Category: Productivity
Built by: HelpDocs (helpdocs.io)
```

## Why This Matters for Operators

Support documentation rots because updating it is a separate chore from the work that reveals the gaps. The knowledge base answers live customer questions all day, and nobody has time to keep it current.

**HelpDocs MCP closes the loop inside the assistant you already work in.** When a support conversation surfaces a gap, the same assistant searches the KB, drafts the article, and files it. The analytics tools close the second loop: pull what readers search for, and you know what to write next.

## Tools & Capabilities

| Capability | What the assistant can do |
|---|---|
| Search | Find articles and categories |
| Read | Full content of any article |
| Write | Create, update, and delete articles and categories, including drafts |
| Analytics | What readers search for, plus account details |

## Installation

First enable MCP in HelpDocs: Settings → AI → check Enable AI Tools → select MCP Access in the Choose features dropdown → Save. Then add the server to your client:

```bash
claude mcp add helpdocs --transport http <your-account-mcp-url>
```

The authorization flow lets you pick which HelpDocs account to connect when you have several.

## Configuration

```json
{
  "mcpServers": {
    "helpdocs": {
      "type": "http",
      "url": "<your-account-mcp-url>"
    }
  }
}
```

## Business Relevance

- **Support leads** draft answers for tickets without leaving the assistant
- **Docs writers** close gaps the moment they are spotted in chat
- **Product teams** mine search analytics for feature-request signal
- **Founders** keep the KB current with zero context switching

## Integration with CorpusIQ

HelpDocs MCP complements the CorpusIQ docs workflow: corpusiq-docs holds the product documentation, while HelpDocs serves customer-facing knowledge bases. A composed workflow reads search analytics from HelpDocs, drafts the missing articles, and uses CorpusIQ's SEO and GEO tooling (Ahrefs, Search Console) to verify the pages earn visibility once published.

## Limitations

- Available on certain plans only
- Per-account endpoint with authorization flow per connection
- Write access requires careful scoping — drafts first
- Commercial SaaS

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
