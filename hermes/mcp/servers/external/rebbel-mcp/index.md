---
title: "Rebbel MCP - Approval-Gated Social Marketing for SMBs"
description: "Plan campaigns and draft on-brand posts, captions and images for small business; nothing publishes until the operator approves, enforced server-side."
category: Social Media Management
stars: 0 (MIT)
added: 2026-09-29
source: "mcp.so server page (rebbel.io)"
relevance: ★★★
tags: [social-media, marketing, content, approval-gated, small-business, remote-mcp, oauth]
---

# Rebbel MCP

**A marketing department for small business, reachable from any MCP client.** Rebbel builds a brand guide from your website, plans a strategy and drafts campaigns - posts, captions and images in your brand voice - and enforces that nothing publishes until you explicitly approve it. Verified and featured on mcp.so.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Rebbel account sign-in)
Endpoint: https://app.rebbel.io/api/mcp
Tools: capability set from the listing (live tool list is served from the endpoint)
Pricing: account-based (rebbel.io)
Category: Social Media Management
Built by: Rebbel (rebbel.io); GitHub alexdaltonmccoy/rebbel-gemini-extension (MIT)
```

## Why This Matters for Operators

Small businesses rarely have a marketing department. Rebbel gives an operator one, reachable through the MCP client they already use: share your website and the assistant builds the brand guide, plans the strategy and drafts campaigns in the brand voice across posts, captions and images.

The differentiator is the approval model. Every post is shown for review and publishes only after explicit approval, enforced on the server - not just in a prompt. Publishing is limited to the accounts you connected (Facebook, Instagram, X, LinkedIn, Threads, Bluesky), and disconnecting stops all activity immediately. Operators can also ask performance questions like "How did last week's posts do?"

## Tools & Capabilities

| Capability | What it covers |
|---|---|
| Brand setup | Build a brand guide from your website |
| Campaign planning | Strategy and campaign drafting for a small business |
| Post drafting | Posts, captions and images in your brand voice |
| Approval gate | Server-enforced review before anything publishes |
| Channel connections | Facebook, Instagram, X, LinkedIn, Threads and Bluesky |
| Performance read-back | Ask how recent posts performed |

The live tool list is served from the endpoint; the capabilities above are the vendor's published feature set.

## Installation

```bash
claude mcp add rebbel --transport http https://app.rebbel.io/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "rebbel": {
      "type": "http",
      "url": "https://app.rebbel.io/api/mcp"
    }
  }
}
```

The first connection opens a browser window to sign in with your Rebbel account and authorize access; the credentials are reused for later sessions. Setup guides for Claude, Cursor and Gemini CLI are published at rebbel.io/mcp.

## Business Relevance

- **SMB operators** get brand guides, campaign drafts and on-brand posts without hiring
- **Agencies** give clients an approval-enforced publishing surface across six networks
- **Franchise and multi-location owners** keep brand voice consistent across accounts
- **Operators new to social** get safe defaults: nothing publishes until they approve

## Integration with CorpusIQ

Rebbel turns CorpusIQ business answers into published marketing. A composed workflow: CorpusIQ surfaces what is selling and to whom from Shopify, Stripe or GA4, the assistant drafts campaign posts around that signal, and Rebbel holds them at the approval gate until the operator says go. The operator's explicit approval stays the single publishing control.

## Limitations

- Listing does not publish a static tool table; verify the live tool list from the endpoint
- Requires a Rebbel account with connected social accounts to publish
- Approval gate covers publishing only; account setup remains in the Rebbel app
- Young listing (repo pushed Sep 3, 2026); monitor vendor uptime and changelog

## FAQ

### Which platforms can Rebbel publish to?

Facebook, Instagram, X, LinkedIn, Threads and Bluesky - only the accounts you connected. Disconnecting a platform stops all activity on it immediately.

### Can anything publish without my approval?

No. The approval gate is enforced on the server, not in the prompt. Every post is shown for review and publishes only after your explicit approval.

### What can I ask the assistant to do?

Setup prompts like "Set up my brand from mybusiness.com", drafting prompts like "Draft three posts for our weekend sale", and performance questions like "How did last week's posts do?"

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [SMAT MCP - Instagram and Facebook Publishing for Agents](/hermes/mcp/servers/external/smat-mcp/)
- [ContentStudio MCP Server - Social Publishing with Approvals for Agencies](/hermes/mcp/servers/external/contentstudio-mcp/)
