---
title: "ParrotNotes MCP - Meeting Notes Search for Agents"
description: "ParrotNotes exposes recorded in-person meeting notes to AI assistants for search, summarization and action-item follow-up."
category: Productivity
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (parrotnotes.app)"
relevance: ★★
tags: [meeting-notes, transcription, productivity, notes-search, remote-mcp]
---

# ParrotNotes MCP

**Your in-person conversations become a searchable library for agents.** ParrotNotes records conversations on your phone or Mac and turns them into transcripts, summaries and action items. The hosted MCP server exposes that library to an AI assistant, so you can ask questions of your own notes without opening the app.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth via Dynamic Client Registration, no API key
Endpoint: https://mcp.parrotnotes.app/mcp
Tools: list recordings, search notes, summarize, save insights back
Pricing: free tier available
Category: Productivity / Meeting Notes
Built by: ParrotNotes (parrotnotes.app)
```

## Why This Matters for Operators

Operators live in conversations: client commitments, site visits, interviews, walkthroughs. Most of it evaporates because notes are siloed in whatever app captured them. ParrotNotes closes that loop by giving the assistant read access to the recording library, so follow-up questions like what did this client commit to become agent tasks instead of memory exercises.

The zero-config auth is a practical advantage: clients register themselves through Dynamic Client Registration and you sign in through the browser, no API keys to mint or rotate.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Recent recordings | List and surface the newest notes and recordings |
| Note search | Ask questions across the full library |
| Summarization | Pull key points from a specific meeting |
| Insight capture | Save an answer back to a note |

Tool names are served from the endpoint; the table reflects the vendor's published capability set. Notes are created in the ParrotNotes apps; the server reads that library and cannot create recordings.

## Installation

```bash
claude mcp add --transport http parrotnotes https://mcp.parrotnotes.app/mcp
```

On first connect you are redirected to parrotnotes.app/auth/authorize to sign in and grant consent.

## Configuration

```json
{
  "mcpServers": {
    "parrotnotes": {
      "type": "http",
      "url": "https://mcp.parrotnotes.app/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** keep client commitments as queryable notes instead of memory
- **Sales teams** review what prospects said before follow-up calls
- **Consultants** turn site visits into action lists in one prompt
- **Teams** search every recorded conversation by tag or project

## Integration with CorpusIQ

ParrotNotes supplies the conversational record that CorpusIQ CRM connectors turn into pipeline: after a call, the agent pulls the ParrotNotes summary and updates the HubSpot deal or Salesforce opportunity with commitments and action items, in the same session it reads the CRM.

The CorpusIQ Calendar connector adds the context layer: scheduled meetings name the recording to search, and the assistant assembles prep notes from both surfaces before the next call.

## Limitations

- New listing, no track record yet
- Reads the existing library only; cannot create recordings
- Requires at least one saved note for tools to return results
- Tool names are not published; live catalog is served from the endpoint

## FAQ

### Does it record meetings itself?

No. Recording happens in the ParrotNotes iOS, Android and macOS apps. The MCP server reads that library and can save insights back.

### Do I need an API key?

No. Clients register themselves through Dynamic Client Registration and you authorize through the browser.

### What is the MCP endpoint?

https://mcp.parrotnotes.app/mcp with Streamable HTTP transport and OAuth sign-in.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
