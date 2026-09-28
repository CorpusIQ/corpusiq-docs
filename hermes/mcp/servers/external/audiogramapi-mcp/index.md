---
title: "Audiogram API MCP - Podcast Search and Transcripts"
description: "Audiogram API exposes podcast search and transcript retrieval over MCP so agents can research episodes and pull quotes."
category: Content & Research
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (audiogramapi.com)"
relevance: ★★
tags: [podcasts, transcripts, audio-search, content-research, media, remote-mcp]
---

# Audiogram API MCP

**Podcast search and transcripts as agent tools.** Audiogram API's remote MCP server lets an AI assistant search published podcasts and retrieve available transcripts, so research that used to mean scrubbing through audio by hand becomes a query.

```
Server type: Remote (Streamable HTTP)
Auth: vendor auth (connector flow documented per client)
Endpoint: https://mcp.audiogramapi.com/mcp
Tools: podcast search, transcript retrieval
Pricing: vendor pricing (audiogramapi.com)
Category: Content & Research / Media
Built by: Audiogram API (audiogramapi.com)
```

## Why This Matters for Operators

Podcasts are where operators, investors and buyers explain their thinking at length, and until now that corpus was effectively unsearchable: audio scrubbing is too slow, and transcript coverage varies by episode. An MCP tool that searches and pulls available transcripts turns a listening backlog into a queryable research surface.

For competitive research, customer calls and market education, the value is the same shape as any data connector: the agent can retrieve evidence and quote it with a source instead of paraphrasing from memory.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Podcast search | Find published episodes by topic, show or keyword |
| Transcript retrieval | Pull available transcripts for an episode |

The vendor notes transcript coverage varies by episode; tool names are served from the endpoint.

## Installation

```bash
claude mcp add audiogram --transport http https://mcp.audiogramapi.com/mcp
```

The vendor publishes a step-by-step Claude connector walkthrough on the server page.

## Configuration

```json
{
  "mcpServers": {
    "audiogram": {
      "type": "http",
      "url": "https://mcp.audiogramapi.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** research how peers describe their categories before drafting positioning
- **Competitive teams** pull what executives actually said on air instead of paraphrases
- **Content teams** find quotable moments with source timestamps
- **Sales teams** listen to prospect appearances before calls

## Integration with CorpusIQ

Audiogram feeds the research leg of a CorpusIQ go-to-market workflow: the agent pulls podcast evidence about a competitor, combines it with firmographic data from the HubSpot or Salesforce connectors, and drafts outreach that references what the prospect actually said on air.

The output also pairs with CorpusIQ Content connectors: quotable passages become source-cited material for blog posts and social drafts.

## Limitations

- New listing, no track record yet
- Transcript coverage varies by episode, not every episode has one
- No published tool catalog beyond search and retrieval
- Pricing not disclosed on the directory listing

## FAQ

### Does every podcast have a transcript?

No. The vendor states coverage varies by episode, so retrieval is best-effort.

### What is the MCP endpoint?

https://mcp.audiogramapi.com/mcp with a connector flow documented for Claude and other clients.

### Is this a full media monitoring tool?

No. It covers podcast search and transcript retrieval only, which pairs well with broader research and monitoring stacks.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
