---
title: "Atono MCP Server - CorpusIQ Docs - CorpusIQ Docs"
description: "Atono project management over MCP: backlogs, bugs, sprints, and epics with AI-generated investigation context for your agents"
category: Productivity
stars: n/a (new listing)
added: 2026-08-17
source: "mcp.so GitHub issue #3621"
relevance: ★★
tags: [project-management, agile, backlog, sprints, bug-tracking, atono, stdio-mcp, docker]
---

# Atono MCP Server

**MCP server for Atono, a project management and agile tooling platform, giving AI agents direct access to the team's backlog, bugs, sprints, and AI-generated investigation context.** Agents can create and update stories and bugs, manage epics and timeboxes, link related work, attach files, and pull team workflow and glossary data without leaving the agent session. Apache-2.0, shipped as a Docker image.

```
Server type: Local (stdio or Docker)
Auth: Atono account credentials
Install: docker run atonoio/atono-mcp-server
Docs: docs.atono.io/docs/mcp-server-for-atono
Pricing: Free server, requires Atono product access
Category: Project Management
Built by: Atono (atono.io), repo github.com/atono-io/atono-mcp-server
```

## Why This Matters for Operators

The "what is my team actually working on" question is the hardest one for an agent to answer without a project tool that speaks MCP natively. Atono's MCP server closes that gap: an agent in a planning session reads the real backlog, links related work, and updates stories in place instead of producing a summary a human must retype.

The investigation context is the differentiator: Atono generates AI investigation summaries attached to work items, and the MCP surface exposes them. An agent picking up a bug gets the context Atono already assembled, which is one round of discovery saved per handoff.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Backlog access | Read stories and bugs with their full context |
| Work-item updates | Create and update stories and bugs in place |
| Epics and timeboxes | Manage epics and iteration boundaries |
| Related-work linking | Link work items to each other |
| File attachments | Attach files to work items |
| Team context | Pull workflow and glossary data so agents use the team's vocabulary |

## Installation

```bash
docker run -d atonoio/atono-mcp-server
```

Then point your MCP client at the container with your Atono credentials in the environment.

## Configuration

```json
{
  "mcpServers": {
    "atono": {
      "command": "docker",
      "args": ["run", "-i", "atonoio/atono-mcp-server"]
    }
  }
}
```

## Business Relevance

- **Product managers** let agents read and update the real backlog during planning sessions
- **Engineering leads** hand agents bug context that Atono already generated, cutting discovery time
- **Project operators** manage epics and timeboxes through the same surface the agent uses
- **QA teams** attach evidence to bugs without leaving the investigation thread
- **Scrum masters** keep agents aligned to team vocabulary through the glossary tool

## Integration with CorpusIQ

Atono answers what the team is doing; CorpusIQ answers what the business is doing. An operator runs Atono's MCP for sprint and backlog context while CorpusIQ connectors pull the financial and growth metrics (Stripe, GA4, QuickBooks) in the same session, joining delivery status to business outcomes. The agent reads from both and writes only where a human has approved: Atono for work items, never the ledger.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Requires an Atono account; the MCP is not a standalone product
- Young repository (0 stars at discovery): expect rough edges
- Write tools create and update work items: scope the credentials carefully
- Self-hosted server means you run and patch the container

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
