---
title: Elium MCP - Enterprise Knowledge Base for Agents
description: "OAuth-gated MCP connector for Elium knowledge bases. Exposes five read-only tools that run with the permissions of the authenticated user: semantic article search, filtered search, full article reads, space listing and template listing, served per platform at your-subdomain.elium.com."
category: Productivity
stars: n/a (new listing)
added: 2026-09-05
source: mcpservers.org
relevance: ★★★
tags: [knowledge-management, enterprise-search, semantic-search, oauth, remote-mcp, documentation, intranet]
---

# Elium MCP

**Remote MCP server (per-instance endpoint, OAuth)** - bridges an Elium knowledge base to AI assistants like ChatGPT and Claude. An assistant can query company content, answer questions with sources, summarise documentation and provide context-aware support without manual copy or export, and every result is bound by the authenticated user's permissions.

```
Server type: Remote (per-instance endpoint)
Auth: OAuth (every tool runs with the authenticated user's permissions)
Endpoint: https://your-platform-name.elium.com/services/mcp
Tools: 5 (all read-only)
Pricing: Platform plans from EUR 15/mo per user (Team, minimum 10 users)
Category: Productivity
Built by: Elium (elium.com, ISO 27001 certified, EU-hosted)
```

## Why This Matters for Operators

Company knowledge lives in wikis, SOPs, decision records and product docs, and agents usually cannot see any of it. Elium MCP gives an assistant governed access to exactly the content the signed-in user may already read - no exports, no copy-paste, no new permission model to manage.

Because each tool executes with the permissions of the authenticated user, an assistant can only ever surface content that user is allowed to see in Elium. That single property is what makes the connector safe to roll out across a team: interns and executives can share the same agent without sharing the same visibility.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `findRelevantArticles` | Semantic (meaning-based) search of the whole knowledge base from a natural-language question, ranked by relevance; the default tool for answering. Results carry title, link and matching snippet, including snippets from attached documents |
| `findSpecificArticles` | Search with filters: keywords, template, spaces and date range |
| `readArticle` | Full content and metadata of one article |
| `findSpaces` | List the spaces the authenticated user can access |
| `findTemplates` | List the article templates available |

## Installation

```bash
claude mcp add --transport http elium https://your-platform-name.elium.com/services/mcp
```

Replace `your-platform-name` with the Elium platform subdomain. Complete the OAuth sign-in with an Elium account; the connection then inherits that account's permissions.

## Configuration

```json
{
  "mcpServers": {
    "elium": {
      "url": "https://your-platform-name.elium.com/services/mcp"
    }
  }
}
```

Auth notes: access is managed via OAuth, ensuring only authorised users and applications can retrieve information based on their Elium permissions. Each Elium instance exposes its own endpoint.

## Business Relevance

- **Support teams** give agents the product KB with sources, so answers come with the documentation to back them.
- **Onboarding** turns the company wiki into an askable assistant for new hires.
- **Compliance-conscious operators** get ISO 27001 certified, EU-hosted infrastructure for knowledge access.
- **Agencies** serving enterprise clients can connect to client knowledge bases without standing up exports.

## Integration with CorpusIQ

CorpusIQ reads the operational business - Stripe, HubSpot, QuickBooks and the other 40+ connectors - while Elium supplies the company's own documented knowledge. Combined, an agent can answer "what does our refund policy say, and how many refunds hit last month" by pulling policy from Elium and numbers from CorpusIQ in the same conversation.

## Limitations

- Read-only: the five tools retrieve knowledge; they do not write articles, so knowledge creation stays in Elium itself.
- Endpoint is per instance; the platform subdomain must be known before connecting.
- Results are permission-bound, so different users get different agent answers from the same server.
- The Team tier starts at 10 users; smaller teams may find the platform pricing heavy.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [AnswerLoops MCP - Community Support Knowledge Base for Agents](/docs/hermes/mcp/servers/external/answerloops-mcp)
- [Extend MCP - Document Intelligence with OCR and PDF Forms](/docs/hermes/mcp/servers/external/extend-mcp)
