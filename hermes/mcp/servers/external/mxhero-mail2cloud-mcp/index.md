---
title: "mxHERO Mail2Cloud MCP - Enterprise Email Search"
description: "Governed, read-only search over an enterprise email archive: years of correspondence across teams and mail systems, in plain language via MCP."
category: Productivity
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 midday sweep)"
relevance: ★★
tags: [enterprise, email-archive, search, governance, compliance, read-only, remote-mcp]
---

# mxHERO Mail2Cloud MCP

**Remote MCP server (Streamable HTTP, OAuth)** - governed, read-only AI access to an enterprise email archive. mxHERO Mail2Cloud captures email into secured, AI-ready storage with compliance tagging and metadata enrichment; the mxMCP connector searches years of correspondence across teams and mail systems in plain language, with links back to every source.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (consent screen + work-email sign-in code)
Endpoint: https://mcp.mxhero.com/mcp2/connect
Tools: 2 capabilities - search email archives; get local time
Pricing: Requires a Mail2Cloud Advanced subscription
Built by: mxHERO
Registry: via mcp.mxhero.com
```

## Why This Matters for Operators

Email is the largest untapped data source in most businesses and the most sensitive one. Asking an AI about email normally means forwarding threads into a chat window - which leaks data and loses context. mxMCP takes the governed route: the archive is captured in real time into secure vector storage, the connector is strictly read-only, searches stay inside your tenant, and your existing permissions are respected rather than widened.

The practical surface is deliberately small - search the archive, and get the time - but the depth is the point. Search covers message bodies, standard headers, thread relationships and text extracted from attachments (with OCR and metadata filtering), and answers link back to the source emails, so a question like "how many emails do we have from this supplier" or "what did we agree in this thread" resolves to a count and a citation, not a summary from memory.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Search email archives | Runs a search and returns matching messages, their metadata and attachment text; read-only |
| Get local time | Returns the current local date and time, so relative questions like "last quarter" resolve correctly |

## Installation

In Claude (steps are similar for other clients): Settings, then Connectors, then add a connector with this URL:

```
https://mcp.mxhero.com/mcp2/connect
```

Approve the mxHERO consent screen, sign in with your work email, enter the code mxHERO sends, and confirm the connection by asking a question your archive can answer.

## Configuration

```json
{
  "mcpServers": {
    "mxhero": {
      "url": "https://mcp.mxhero.com/mcp2/connect"
    }
  }
}
```

## Business Relevance

- **Sales teams** search years of correspondence with leads and clients across multiple mailboxes, with the source thread attached.
- **Operations and support** recover what was agreed, without digging through folders or exporting mailboxes.
- **Compliance-minded firms** get the read-only, tenant-scoped shape their policies require: no send, no delete, no move.
- **IT administrators** control which mailboxes and date ranges are archived and searchable.

## Integration with CorpusIQ

CorpusIQ's read-only connectors run to the systems of record - accounting, payments, ads, analytics. Mail2Cloud adds the conversation layer those systems never capture: what was promised in email, to whom, and when. Together, an operator can check the numbers and the correspondence behind them in one governed, read-only loop - no data leaves either system, and every answer cites its source.

## Limitations

- Requires a Mail2Cloud Advanced subscription; plain Mail2Cloud archives are not indexed for search.
- The connector can only read - it cannot send, reply, forward, modify, delete or move messages.
- Your administrator decides which mailboxes and date ranges are searchable.
- New listing: no track record in this catalog yet.

## FAQ

### Is it really read-only?

Yes. The connector exposes exactly two capabilities - search and local time - and there is no tool that changes anything in the archive.

### Can I search another organization's email?

No. Searches return results only from your organization's archive, and the connector respects the access your mxHERO account already has.

### What does the archive contain?

Message bodies, standard headers (sender, recipients, subject, date), thread relationships, and text extracted from attachments, for the mailboxes and date ranges your administrator configured.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Kapa MCP - Docs and Tickets into an AI Knowledge Base](/hermes/mcp/servers/external/kapa-mcp/)
- [Debriefing MCP - Competitor Moves with Evidence](/hermes/mcp/servers/external/debriefing-mcp/)
