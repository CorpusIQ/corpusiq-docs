---
title: Mnemos MCP - Local-First Meeting Memory
description: "Mnemos records and transcribes meetings on-device, extracts decisions and action items, and exposes history to MCP clients."
category: Productivity
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + github.com/pushkarrmandot/mnemos"
relevance: ★★
tags: [meeting-notes, transcription, action-items, meeting-memory, local-first, self-hosted]
---

# Mnemos MCP

**Meeting memory that stays on the machine.** Mnemos is a local-first meeting memory tool: it records and transcribes meetings on-device, extracts decisions and action items, and exposes the meeting history to MCP clients like Claude Code. Nothing is uploaded to a third-party transcription service, which is the point for operators who discuss sensitive material.

```
Server type: Local (self-hosted)
Auth: none (local process)
Endpoint: stdio from the repo
Tools: meeting capture, transcription, decisions and action-item extraction, history search
Pricing: free and open source
Category: Productivity / Meetings
Built by: Mnemos (github.com/pushkarrmandot/mnemos)
```

## Why This Matters for Operators

Meeting follow-through usually dies in the gap between the call ending and the notes being written. Mnemos closes the gap with on-device recording and transcription, then structures the output into decisions and action items an agent can act on. The agent can answer questions about what was decided and by whom without re-listening to anything.

The local-first property is the differentiator against cloud meeting tools: the audio and transcripts never leave the machine, which matters for client calls, board discussions and anything under NDA.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Recording | On-device meeting capture |
| Transcription | Local transcription of meeting audio |
| Extraction | Decisions and action items pulled from the transcript |
| History | Meeting history exposed to MCP clients |

## Installation

```bash
git clone https://github.com/pushkarrmandot/mnemos
```

Follow the repo README to run the server and connect it to Claude Code or another MCP client.

## Configuration

```json
{
  "mcpServers": {
    "mnemos": {
      "command": "<per-repo-launch-command>"
    }
  }
}
```

## Business Relevance

- **Founders** keep board and investor call decisions searchable
- **PMs** turn meeting action items into tracked work
- **Agencies** keep client call history local and queryable
- **Teams** get meeting context without a cloud subscription

## Integration with CorpusIQ

Mnemos pairs with CorpusIQ's Notion and Monday connectors: decisions extracted from meetings can be pushed into Notion databases or Monday boards where CorpusIQ reads project state for recaps. CorpusIQ's calendar connector surfaces the meetings, and Mnemos turns them into retrievable institutional memory.

## Limitations

- Local-first means each machine keeps its own history; no native sync yet
- Transcription quality depends on the on-device model
- Young open-source project with no public adoption track record
- Single-purpose: meeting memory, not general note-taking

## FAQ

### Where do recordings live?

On the operator's machine; Mnemos is local-first with no third-party transcription upload.

### What does it extract from meetings?

Decisions and action items, exposed as searchable history to MCP clients.

### How do I run it?

Clone the repository and follow the README to launch the server and connect Claude Code or another MCP client.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
