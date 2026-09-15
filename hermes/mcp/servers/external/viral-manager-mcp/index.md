---
title: Viral Manager MCP - Creator Intelligence for AI Agents
description: Viral Manager exposes 50 read and write MCP tools so an agent can run part of a creator operation. Find viral posts, read AI breakdowns, create assignments, manage watchlists and pull download links. Published in the official MCP registry for creator agencies.
category: Marketing
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [creator-economy, viral-posts, content-ops, social-intelligence, influencer-marketing, oauth, remote-mcp]
---

# Viral Manager MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** - the agent surface of Viral Manager, a virality-detection platform for creator agencies. Fifty read and write tools let an assistant read the night's viral posts, draft briefs and assign them before the team's first coffee. It is not a read-only feed: an agent can run part of the operation.

```
Server type: Remote (Streamable HTTP, standard MCP)
Auth: API key from workspace settings or OAuth from an MCP client
Endpoint: Provisioned by the vendor via the official MCP registry (com.viral-managers/viral-manager)
Tools: 50 (read and write)
Pricing: Included with Scale and Empire plans · 7-day free trial
Category: Marketing
Built by: Viral Manager
```

## Why This Matters for Operators

Creator operations live and die by how fast a team spots a viral post and turns it into a brief. Viral Manager makes that loop conversational: an agent reads the discovery feed, surfaces the winners, drafts assignments against the right creator model and files them. **The vendor does not publish a raw endpoint URL; the server is published in the official MCP registry as com.viral-managers/viral-manager and most directories mirror it, so clients that browse a catalogue find it there. Connect via OAuth from an MCP client or generate a key in workspace settings.**

Permissions inherit from the key or account used to connect, including category restrictions on team members. Destructive tools respect the same role gating as the dashboard, and no training happens on workspace data.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_viral_posts` | Read viral posts filtered by niche and minimum score |
| `get_post_analysis` | Pull the AI breakdown of a post (views, hooks, structure) |
| `create_assignment` | Draft and assign a brief to a creator model with a due date |
| `list_watchlist_accounts` | List tracked accounts sorted by growth |
| `get_trending_sounds` | Trending sounds for a niche over a rolling window |
| `summarize_my_accounts` | Summarize own account performance for a period |
| Folder, tag and category tools | Move, tag and organize posts in the library |
| Asset tools | Pull download links for approved assets |
| Analytics tools | Read own-account analytics across the workspace |

## Installation

Connect via OAuth from an MCP client, or generate a key in workspace settings and point the client at the vendor endpoint. Claude Desktop, Claude Code and other MCP clients connect as-is through the standard MCP flow.

## Configuration

```json
{
  "mcpServers": {
    "viral-manager": {
      "url": "https://mcp.your-workspace.viral-manager.com/mcp"
    }
  }
}
```

Auth notes: the vendor does not publish a static endpoint URL. The server is provisioned per workspace: resolve the exact URL from the official MCP registry entry (com.viral-managers/viral-manager), the Glama or Smithery listings, or the in-app connection flow, and substitute it above. The agent inherits the permissions of the key or account it connects with.

## Business Relevance

- **Content team leads** wake up to an agent that already read the night's viral posts and drafted the briefs.
- **Creator agencies** route assignments, watchlists and asset downloads through a conversational surface instead of five tabs.
- **Growth operators** ask for trending sounds and niche winners without touching the dashboard.
- **White-label teams** expose the same MCP surface on white label workspaces.

## Integration with CorpusIQ

Viral Manager finds what is winning on social; CorpusIQ tells you what it means for the business. An operator can have an agent surface a batch of high-scoring viral posts through Viral Manager, then pull revenue, conversion and channel data from CorpusIQ's Stripe, Shopify and GA4 connectors to decide which format deserves production budget. CorpusIQ reads the business, Viral Manager reads the feed, and the operator reads a single conversation.

## Limitations

- MCP is only on the Scale and Empire plans (plus white label workspaces), not lower tiers.
- The endpoint URL is not published on the vendor site; it resolves through the official registry and in-app flow.
- No public tool schema reference; the 50-tool surface is described by the vendor, not probeable anonymously.
- Rate limits exist and are sized for routine automation, not bulk backfills.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Buska MCP - Social Listening and Buying Signals for AI Agents](/docs/hermes/mcp/servers/external/buska-mcp)
- [OmniSocials MCP - Multi-Platform Social Publishing for AI Agents](/docs/hermes/mcp/servers/external/omnisocials-mcp)
