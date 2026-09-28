---
title: "AgileHero MCP - Agile Project Management for Agents"
description: "AgileHero runs the whole agile motion as shared MCP tools: board, backlog, roadmap, whiteboards, retros, metrics and wiki."
category: Productivity
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (mcp.agilehero.io)"
relevance: ★★★
tags: [agile, project-management, sprints, roadmap, retrospectives, productivity, remote-mcp]
---

# AgileHero MCP

**An agile workspace AI agents and people drive together.** AgileHero is an all-in-one agile project management platform where the MCP endpoint at `https://mcp.agilehero.io/mcp` exposes every module, board, backlog, roadmap, whiteboards, retros, metrics and wiki, as tools an AI assistant can operate on your behalf.

```
Server type: Remote (Streamable HTTP)
Auth: account auth (docs at agilehero.io/docs/mcp)
Endpoint: https://mcp.agilehero.io/mcp
Tools: board, backlog, roadmap, whiteboards, retros, metrics, wiki
Pricing: vendor pricing (agilehero.io)
Category: Productivity / Project Management
Built by: AgileHero (agilehero.io, github.com/agilehero-io/agilehero-mcp)
```

## Why This Matters for Operators

Agile rituals consume the exact time operators do not have: grooming backlogs, updating boards, pulling sprint metrics, writing retro notes. When the tooling itself understands agent commands, a founder can ask for the state of the sprint and get an answer assembled from live data instead of a status meeting.

The value compounds because the workspace is shared. The assistant updates the board from chat, the team sees it in the web app, and the metrics module reads the same source of truth. Nothing gets reconciled twice.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Board and backlog | Create, move and update work items across sprints |
| Roadmap | Track initiatives and releases against dates |
| Whiteboards | Draft and structure planning artifacts |
| Retros | Capture and action retrospective notes |
| Metrics | Pull sprint and delivery metrics |
| Wiki | Maintain project documentation from chat |

Tool names are served from the endpoint; the table reflects the vendor's published module set.

## Installation

```bash
claude mcp add agilehero --transport http https://mcp.agilehero.io/mcp
```

Connection and authorization steps are documented at agilehero.io/docs/mcp.

## Configuration

```json
{
  "mcpServers": {
    "agilehero": {
      "type": "http",
      "url": "https://mcp.agilehero.io/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** get sprint status and roadmap answers without opening a board
- **Product managers** groom backlogs and write retros from chat
- **Engineering leads** pull delivery metrics on demand
- **Agencies** run client-facing sprints with a shared agent-operable workspace

## Integration with CorpusIQ

AgileHero's metrics module pairs with the CorpusIQ GitHub connector's delivery data: sprint commitments from AgileHero against actual pull request and milestone velocity from GitHub give a single delivery picture without manual exports.

For ops cadence, the CorpusIQ Calendar and Slack connectors carry the schedule and the threads while AgileHero holds the work items, so a weekly review can be assembled from all three surfaces in one agent session.

## Limitations

- Brand new listing, no track record yet
- Tool names are not published; live catalog is served from the endpoint
- Pricing is not disclosed on the directory listing
- Agile-only scope, no kanban-only or waterfall-only alternatives
- Public repository has no stars yet

## FAQ

### Does this replace Jira or Linear?

It is a full agile workspace in its own right. The practical question is whether your team is willing to move boards; the agent surface is the differentiator.

### Can the agent update the board while the team uses the web app?

Yes. The workspace is shared, so chat-driven updates and human edits land in the same source of truth.

### What is the MCP endpoint?

https://mcp.agilehero.io/mcp with Streamable HTTP transport and account authorization on first connect.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
