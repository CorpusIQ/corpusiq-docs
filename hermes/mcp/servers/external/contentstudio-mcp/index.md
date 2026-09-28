---
title: ContentStudio MCP Server - Social Publishing for Agencies
description: "ContentStudio's official hosted social MCP: draft, schedule, publish, approvals, analytics and inbox for agencies across connected networks."
category: Social Media Management
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + docs.contentstudio.io"
relevance: ★★★
tags: [social-media, scheduling, publishing, approvals, analytics, social-inbox, agencies, remote-mcp]
---

# ContentStudio MCP Server

**The official hosted social MCP from ContentStudio, built for agencies that need approvals before anything ships.** The server at `https://mcp.contentstudio.io/mcp` connects AI assistants to draft, schedule and publish content, route it through approval flows, read analytics and manage the social inbox across the networks connected to a ContentStudio workspace. It is a hosted server from the vendor, listed in the Marketing category of the major directories, with documentation at docs.contentstudio.io.

```
Server type: Remote (Hosted)
Auth: ContentStudio account (OAuth)
Endpoint: https://mcp.contentstudio.io/mcp
Tools: draft, schedule, publish, approvals, analytics, inbox
Pricing: ContentStudio plans
Category: Social Media Management
Built by: ContentStudio (contentstudio.io)
```

## Why This Matters for Operators

Agency social workflows break when the drafting surface and the approval surface are different tools. ContentStudio's MCP closes that gap: the agent drafts and schedules inside the conversation, the approval flow stays in ContentStudio where clients or managers sign off, and nothing publishes without passing the existing workspace rules. Analytics and inbox management come along so the agent can also report and triage without switching contexts.

For operators running many client networks, the win is consolidation: one hosted endpoint, one workspace, and the agent inherits whatever networks and permissions the account already has.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Drafting | Compose posts for connected networks |
| Scheduling | Queue posts across channels and time slots |
| Publishing | Publish directly or via workspace approval flows |
| Approvals | Route content through the existing approval pipeline |
| Analytics | Read post and account performance |
| Inbox | Manage comments and messages across networks |

## Installation

```bash
npx add-mcp 'https://mcp.contentstudio.io/mcp'
```

Installs into Claude Code, Codex, Cursor and other clients. Claude desktop and claude.ai users add the URL under Settings > Connectors > Add custom connector.

## Configuration

```json
{
  "mcpServers": {
    "contentstudio": {
      "type": "http",
      "url": "https://mcp.contentstudio.io/mcp"
    }
  }
}
```

First connect signs into the ContentStudio account that owns the workspace.

## Business Relevance

- **Agencies** keep agent drafting behind client approvals already configured in ContentStudio
- **Social managers** move drafts, schedules and inbox triage into one conversation
- **Multi-brand operators** scope each connection to its workspace
- **Content teams** get analytics readouts without opening dashboards

## Integration with CorpusIQ

ContentStudio pairs with CorpusIQ's social posting stack: Postiz publishing operations and the social cadence engine schedule the owned channels, while ContentStudio can run agency-client networks with approval gates. Post performance from ContentStudio analytics can join CorpusIQ's GA4 recaps to connect social output with site sessions and signups.

## Limitations

- Hosted by the vendor; no self-hosted MCP option
- Capabilities are bound to the ContentStudio plan and workspace permissions
- Detail documentation on the vendor docs page is thin for the MCP surface
- New listing; tool-by-tool documentation still maturing

## FAQ

### Who is the ContentStudio MCP built for?

Agencies and teams that need approvals before social content ships; the agent drafts and schedules while the workspace approval flow stays in charge.

### What surfaces does it cover?

Drafting, scheduling, publishing, approvals, analytics and the social inbox across connected networks.

### Is it self-hostable?

No. It is a hosted server from ContentStudio; capabilities follow the workspace plan and permissions.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
