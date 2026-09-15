---
title: "Phonotheca MCP: Interview Transcript Search for Agents"
description: "Remote read-only MCP server for Phonotheca, the archive for recorded interviews. Full-text search across projects and interviews with speaker-labelled, timestamped transcript passages that return with their citation attached. Streamable HTTP at phonotheca.com/api/mcp with revocable bearer tokens; a free account is enough to start. License not declared."
category: Content & Research
stars: n/a (new listing)
added: 2026-08-24
source: mcpservers.org /all page 2
relevance: ★★
tags: [interviews, research, transcripts, search, remote-mcp, citations]
---

# Phonotheca MCP

**Search and read your interview transcripts from Claude or any MCP client, with every passage carrying its speaker, interview, project, and timestamp.** Phonotheca is the archive for recorded interviews, and its MCP server connects an agent to the workspace read-only: full-text search across every project, browsing projects and interviews, and reading speaker-labelled transcripts where a quote arrives with its citation attached. The connection cannot upload audio, start transcription, edit a transcript, or delete anything.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: Bearer token created in Settings, revocable at any time
Endpoint: https://phonotheca.com/api/mcp
Repo: github.com/adesiahq/phonotheca-mcp (0 stars, Aug 2026)
Tools: Search, browse projects and interviews, read timestamped speaker-labelled passages
```

## Why This Matters for Operators

Customer interviews are an operator's highest-signal research asset, and they usually die in a recordings folder. Phonotheca keeps them searchable, and the MCP server makes the archive queryable from inside the agent that writes the product spec or the sales pitch. Because passages come back with speaker, interview, project, and timestamp attached, an agent can cite what a customer actually said instead of paraphrasing from memory.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Full-text search | Searches every transcript across projects for passages matching a query |
| Project browsing | Lists projects and the interviews they contain |
| Interview reading | Reads speaker-labelled transcripts with timestamps |
| Citation attachment | Every returned passage carries its speaker, interview, project, and timestamp |

Capability-level table: the server publishes a read-only tool surface for search, browse, and read; exact tool identifiers are enumerated by the endpoint's tool listing after authentication.

## Installation

```json
{
  "mcpServers": {
    "phonotheca": {
      "type": "http",
      "url": "https://phonotheca.com/api/mcp"
    }
  }
}
```

Create a free account at phonotheca.com, then generate a bearer token in Settings. The token is shown once and can be revoked there at any time.

## Configuration

The server is Streamable HTTP and stateless; pass the bearer token through your client's header configuration. A free account is enough to try it; archive capacity and features scale with the Phonotheca plan. The connection is strictly read-only, which makes it safe to expose to agents that should not modify the research archive.

## Example Prompts

- "Search the interviews for everything customers said about onboarding friction."
- "What did the operations director say about reporting in the August interviews? Quote the passage."
- "List the projects in my Phonotheca archive and summarize each interview's themes."
- "Find every mention of pricing pushback and group them by speaker."

## Business Relevance

- **Product teams** ground specs in verbatim customer quotes instead of paraphrased notes
- **Founders** mine interview archives for positioning and objection language
- **User researchers** keep a queryable, citable archive across projects
- **Sales teams** reuse exact customer language in proposals and case studies

## Integration with CorpusIQ

Phonotheca supplies what customers said; CorpusIQ supplies what they did. An agent can pull the verbatim objections from Phonotheca interviews, then check churn, expansion, and product usage in CorpusIQ to test whether the spoken pain matches the behavioral data, producing research conclusions that are cited on both sides.

## Limitations

- New listing (Aug 2026, zero stars); the platform and endpoint are early.
- Read-only by design: recording and transcription happen in the Phonotheca app, not through MCP.
- License is not declared on the repository, which some procurement policies will flag.
- Research value depends entirely on getting interviews into the archive.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Feedback Synthesis MCP](/docs/hermes/mcp/servers/external/feedback-synthesis-mcp) - customer feedback aggregation and analysis
- [Arc Research MCP](/docs/hermes/mcp/servers/external/arc-research-mcp) - research workflow tools for agents
- [Tube Bridge MCP](/docs/hermes/mcp/servers/external/tube-bridge-mcp) - video content research and extraction
