---
title: "AskOne MCP - Live Q&A and Polls for Events"
description: "Run free live audience Q&A and polls from any agent: rooms, votes, moderation, FAQ drafts and results for webinars, classes and meetings."
category: Productivity
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 midday sweep)"
relevance: ★★
tags: [q-and-a, polls, events, webinars, meetings, moderation, stdio]
---

# AskOne MCP

**Local MCP server (stdio via npx, organization API token)** - live audience Q&A and polling for talks, webinars, classes and meetings. The audience joins from a link or QR code on their phones with no account and no app, asks anonymously and upvotes; the MCP server lets an agent run the whole session and draft the FAQ afterwards.

```
Server type: Local (stdio via npx)
Auth: Organization API token (ASKONE_API_TOKEN)
Package: npx -y askone-mcp
Tools: Rooms, polls, question moderation, results, FAQ draft
Pricing: Free tier covers every feature - 1 open room, up to 100 participants; paid adds capacity and branding
Built by: AskOne
Registry: npm askone-mcp
```

## Why This Matters for Operators

Every webinar, all-hands and training session ends with the same mess: questions scattered across chat, hands, and a moderator's notes. AskOne puts the audience into a structured room - anonymous questions, upvotes, ranked walls - and the MCP server lets an agent do the moderator's work: launch polls, approve or hide questions, mark them answered, close the room, then hand back the questions as a FAQ draft and the results as data.

The "who reads them first" control - nobody, a person, or the AI - can change mid-session, and all three modes are available on every plan. For operators running recurring sessions, the FAQ draft is the compounding asset: each session's questions become next session's onboarding material.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Rooms | Start a room, close it, read session state |
| Polls | Add and launch polls, quizzes, ratings and word clouds |
| Moderation | Approve or hide questions, mark them answered, change who reads questions first |
| Ranking | Rank questions by votes and drive the wall display |
| Results | Read poll results and the question list as a FAQ draft |
| Clients | Works in the browser, Zoom, Google Meet and ChatGPT |

## Installation

```bash
claude mcp add askone --transport stdio -- npx -y askone-mcp
```

Set `ASKONE_API_TOKEN` (an organization API token from your AskOne account) in the server environment.

## Configuration

```json
{
  "mcpServers": {
    "askone": {
      "command": "npx",
      "args": ["-y", "askone-mcp"],
      "env": {
        "ASKONE_API_TOKEN": "YOUR_ASKONE_API_TOKEN"
      }
    }
  }
}
```

## Business Relevance

- **Teams running webinars** get structured audience Q&A and polls without a second operator babysitting the room.
- **Trainers and educators** collect anonymous questions, then export the session as a FAQ draft.
- **Founders at demo days and AMAs** rank questions by audience votes instead of moderating by hand.
- **Small teams** get every feature free: one open room at a time, up to 100 participants, AI moderation included.

## Integration with CorpusIQ

CorpusIQ answers business questions from the connected stack; AskOne handles the other direction - what the audience asks. An operator can run a session where the audience's top questions come from real votes, then feed the FAQ draft into the same knowledge workflows the rest of the stack supports.

## Limitations

- One open room at a time on the free tier; free rooms cap at 100 participants.
- Local stdio server - it runs on the machine of whoever hosts the session, not in the cloud.
- Requires an AskOne organization API token.
- New listing: no track record in this catalog yet.

## FAQ

### Is the audience side really free?

Yes. Audiences join with a link or QR code, no account and no app, and every feature - Q&A, polls, the projector, AI moderation - is on the free tier. Paid plans buy capacity and branding, not features.

### Does the agent act on its own?

No. The agent calls the tools you allow; approve, hide and close actions are explicit calls, and the room state is readable at any point.

### Can it produce a FAQ afterwards?

Yes. After the room closes, the agent reads the questions and results and drafts them as a FAQ document.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Revup MCP - Promotions, Forms and Giveaways](/hermes/mcp/servers/external/revup-mcp/)
- [Kapa MCP - Docs and Tickets into an AI Knowledge Base](/hermes/mcp/servers/external/kapa-mcp/)
