---
title: "Blog2Social MCP - Multi-Network Social Publishing"
description: "Blog2Social MCP publishes and schedules to 30+ social, blogging and community networks over OAuth, with per-network post types and media support."
category: Marketing
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (docs.blog2social.com)"
relevance: ★
tags: [social-media, publishing, scheduling, oauth, multi-network, remote-mcp, automation]
---

# Blog2Social MCP

**Schedule and publish across dozens of networks from one endpoint.** Blog2Social runs a hosted MCP server in front of its social publishing API, so an assistant can connect accounts, publish content with media, and automate distribution across social, blogging, business and community platforms from a single interface.

```
Server type: Remote (Streamable HTTP, no local install)
Auth: OAuth (no password or static access token in the client config)
Endpoint: https://api.blog2social.com/mcp
Coverage: 30+ networks
Category: Marketing
Built by: blog2social.com
```

## What it exposes

The published platform guide covers per-network post types and media support, including Facebook (posts and Reels), X, LinkedIn, Instagram (images and videos), Pinterest (pins and boards), Reddit (posts and subreddits), Tumblr, Medium, Threads, Mastodon, Bluesky, TikTok, YouTube, Vimeo, Telegram, Discord, Google Business Profile, Xing, VK and a long tail of blogging and bookmarking networks such as Blogger, DEV, Instapaper, Diigo, Bloglovin and Ravelry. The underlying REST API surface is documented as nineteen operations: `POST /user/auth`, `/user/list`, `/user/delete`, `/network/list`, `/network/add`, `/network/update`, `/network/categories`, `/network/properties`, `/user/auth/list`, `/user/auth/delete`, `/network/post/create`, `/network/post/remove`, `/video/upload`, `/video/check` and four app-scoped operations.

## Connecting

```
{
  "name": "blog2social",
  "url": "https://api.blog2social.com/mcp"
}
```

Complete the OAuth flow when the client prompts for it. The vendor's own guidance is explicit that no Blog2Social password or access token belongs in a client configuration file. The server is also listed on Smithery and Glama for one-click discovery.

## Notes

This is a broad publishing surface rather than an analytics or insights tool: the value is reach across networks and per-network post-type handling, not performance data. Error semantics are unusually well documented for an MCP server, with a full HTTP-status to JSON-RPC-code table covering session, initialization, `tools/list` and `tools/call` failures. Sits in a well-served publishing category alongside ContentStudio, Rebbel, SMAT and PostBazooka.

## See Also

- [Social publishing MCP servers](/hermes/mcp/servers/external/)
- [Marketing MCP servers](/hermes/mcp/servers/external/)
