---
title: "CRM Solid MCP - Social DM Inbox and Scheduling Across 12 Networks"
description: "Social DM inbox and post scheduling MCP server across 12 networks from Claude, Cursor, or ChatGPT, with typed tools to triage messages, draft replies, schedule posts, and pull stats."
category: Social Media
stars: 3
added: 2026-08-29
source: mcpservers.org /all page 3
relevance: ★★
tags: [mcp-server, social-inbox, dm-management, post-scheduling, instagram, whatsapp, linkedin, remote-mcp]
---

# CRM Solid MCP

**A social media MCP server that gives Claude Desktop, Claude Code, Cursor, and ChatGPT typed access to your social DM inbox and posting calendar across 12 platforms, so you can triage messages, draft replies, schedule posts, and pull stats without opening a single dashboard.** Install is zero-infrastructure: npx fetches the package on first run, and the only requirement is an API key minted in the CRM Solid developer settings.

```
Server type: Remote (stdio via npm @crmsolid/mcp-server; talks to CRM Solid cloud)
Auth: API key (CRMSOLID_API_KEY, csk_live_...)
Endpoint: npx -y @crmsolid/mcp-server
Tools: 13 (conversations, messages, posts, scheduling, stats)
Pricing: CRM Solid account plans (free tier available)
Category: Social Media / CRM
Built by: CRM-Solid/crmsolid-mcp; MIT; docs at docs.crmsolid.com/integrations/mcp/
```

## Why This Matters for Operators

Social DMs are the inbox nobody owns: Instagram, WhatsApp, X, and LinkedIn conversations each live in their own app, and the posting calendar lives in another. CRM Solid collapses all of it into one MCP surface - an agent lists connected accounts, triages conversations, drafts and sends replies, schedules posts, and pulls post stats with typed tools.

The key pattern is the inbox summary tool: instead of reading every conversation, the agent pulls a structured digest of what needs attention and only drills into the ones that matter. Thirteen tools cover the full loop - read, reply, schedule, revise, cancel, and measure.

**One MCP surface for the social inbox and the posting calendar across 12 networks.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `crm_list_social_accounts` | List connected social accounts across platforms |
| `crm_list_social_conversations`, `crm_get_social_conversation` | Browse and open DM conversations |
| `crm_list_social_messages` | Read messages inside a conversation |
| `crm_send_social_message` | Send a reply |
| `crm_mark_social_conversation_read` | Mark conversations handled |
| `crm_social_inbox_summary` | Structured digest of what needs attention |
| `crm_list_social_posts`, `crm_get_social_post` | Browse scheduled and published posts |
| `crm_schedule_social_post`, `crm_update_social_post`, `crm_cancel_social_post` | Schedule, revise, and cancel posts |
| `crm_social_post_stats` | Pull per-post performance stats |

## Installation

```bash
claude mcp add crmsolid --env CRMSOLID_API_KEY=csk_live_... -- npx -y @crmsolid/mcp-server
```

Create the key at app.crmsolid.com/settings/developers. Per-client config files are documented for Claude Desktop, Cursor, and other clients in the repo docs.

## Configuration

```json
{
  "mcpServers": {
    "crmsolid": {
      "command": "npx",
      "args": ["-y", "@crmsolid/mcp-server"],
      "env": { "CRMSOLID_API_KEY": "csk_live_..." }
    }
  }
}
```

The same server entry works across clients; restart the client after config changes and ask the agent to list connected social accounts as the smoke test.

## Business Relevance

- **Founders wearing the social hat** triage DMs and replies from one chat instead of five apps.
- **Support teams** pull the inbox summary and handle priority conversations without a social suite.
- **Marketing operators** schedule and revise posts, then read per-post stats in the same surface.
- **Agencies** manage client social inboxes through one MCP key per workspace.

## Integration with CorpusIQ

CRM Solid covers the conversational front office while CorpusIQ covers the data back office: a CorpusIQ workflow pulling Shopify or Stripe signals can have the agent post the resulting update through CRM Solid's scheduling tools, and inbound social DMs can be triaged with the same agent that reads the customer's order history from CorpusIQ connectors. For operators already running social publishing through the catalog's other multi-platform servers, CRM Solid differentiates on the DM inbox side, which pairs cleanly with CorpusIQ's lead and support data.

## Limitations

- Brand new - first sweep August 29, 2026; 3-star repo.
- Cloud-dependent - the npm package talks to CRM Solid's hosted backend, so an account and API key are required.
- Platform coverage depends on CRM Solid's connectors; verify your networks are among the 12 before committing.
- Stats depth is per-post; deep cross-platform analytics still need a dedicated tool.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [OmniSocials MCP - Multi-Platform Social Publishing for AI Agents](/docs/hermes/mcp/servers/external/omnisocials-mcp)
- [SocialRobot MCP - Social Media Scheduling and Analytics for AI Agents](/docs/hermes/mcp/servers/external/socialrobot-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
