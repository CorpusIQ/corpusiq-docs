---
title: "Granola MCP — AI Meeting Notes for Hermes Agent"
description: "Connect Granola meeting notes to Hermes Agent. Query your notes, search transcripts, and get meeting insights directly from any AI client. Official MCP from Granola."
category: mcp
tags: [mcp-server, granola, meeting-notes, productivity, transcription, knowledge-retrieval, search]
last_updated: 2026-07-03
---

# Granola MCP Server ★ New (July 3)

## Overview

Granola MCP (`granola-mcp`) connects AI agents to your Granola meeting notes library. Query past meetings, search transcripts, extract action items, and surface insights from your entire meeting history — all from your AI assistant. Official MCP server from Granola.

**Key advantage**: Turn your meeting notes into a queryable knowledge base. AI agents can answer "what did we decide about pricing in the Q2 review?" by searching your actual meeting transcripts, not guessing.

## Key Features

- **Meeting search**: Full-text search across all meeting titles, notes, and transcripts
- **Transcript access**: Retrieve full meeting transcripts with speaker labels
- **Action item extraction**: Pull action items and decisions from any meeting
- **Cross-meeting insights**: Find patterns and recurring themes across multiple meetings
- **Date-range queries**: Filter by meeting date, participant, or project
- **Remote endpoint**: Hosted MCP server — connect directly, no installation

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add granola --url https://api.granola.ai/mcp

# Authenticate with API key
hermes mcp auth granola --api-key YOUR_GRANOLA_API_KEY
```

## Manual Configuration

```json
{
  "mcpServers": {
    "granola": {
      "type": "sse",
      "url": "https://api.granola.ai/mcp",
      "headers": {
        "Authorization": "Bearer ${GRANOLA_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **Granola Account**: Sign up at [granola.ai](https://granola.ai)
2. **API Key**: Generate from Granola Settings → Integrations → API
3. **Meeting History**: At least a few recorded meetings for meaningful queries

## Business Use Cases

1. **Meeting Prep**: Before a client call, ask AI agent "what did we discuss last time with Acme Corp?" — get full context from Granola
2. **Decision Tracking**: Query "what pricing decisions were made in Q2?" and get exact meeting references
3. **Action Item Follow-up**: AI agent surfaces unresolved action items from past 30 days of meetings
4. **Project Retrospectives**: Search all project meetings for blockers, decisions, and timeline commitments
5. **Knowledge Transfer**: New team members ask the AI agent about historical decisions documented in meetings

## Business Relevance

Granola is the go-to meeting notes platform for operators who live in meetings. MCP integration means meeting knowledge escapes the silo — AI agents now have access to the richest source of institutional knowledge: what was actually discussed and decided.

## Limitations

- Granola API is read-only (no meeting creation via MCP yet)
- Requires Granola subscription for API access
- Transcript quality depends on recording quality
- Search limited to meetings recorded/uploaded to Granola

## See Also

- Cal.com MCP — for scheduling automation
- NotebookLM MCP — for AI research notebooks
- CorpusIQ MCP — for cross-platform business data (CRM, email, analytics)
