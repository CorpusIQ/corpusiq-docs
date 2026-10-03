---
title: "Solnk MCP - Publish to Nine Social Platforms"
description: "Stateless remote MCP that publishes and schedules content across X, Instagram, TikTok, YouTube, Facebook, LinkedIn, Pinterest, Threads and Bluesky."
category: "Marketing"
stars: n/a (hosted + self-hostable, solnk.com)
added: 2026-10-03
source: "mcpservers.org server page (solnk-dev/solnk-mcp)"
relevance: ★★★
tags: [marketing, social-media, publishing, scheduling, multi-platform, remote-mcp, mit]
---

# Solnk MCP

**Hosted MCP server** - Solnk is a single tool surface for publishing and scheduling content across nine social platforms through one API key, with a thin stateless proxy to the Solnk public API.

```
Server type: Hosted (streamable HTTP) or self-hosted Cloudflare Worker
Auth: Solnk API key as a Bearer token
Endpoint: https://mcp.solnk.com/mcp
Platforms: X, Instagram, TikTok, YouTube, Facebook, LinkedIn, Pinterest, Threads, Bluesky
License: MIT (server); service proprietary
Category: Marketing
Built by: Solnk (solnk.com)
```

## Why This Matters for Operators

Anyone publishing across more than two platforms spends real time re-uploading the same asset with per-network quirks. Solnk collapses that to one request that fans out across nine networks, with a status model an agent can follow: publish immediately, schedule, or hold as a draft, then confirm, cancel or read aggregate status.

All auth, scope and quota enforcement happens server-side, and no credentials are stored in the worker, so a self-hosted instance carries no secrets at request time. The server exposes its tool list without a key, which means directories and inspectors can introspect it while a key is only needed to actually publish. That is a clean pattern for teams that want discovery separate from authority.

## Tools

| Tool | What it does |
| --- | --- |
| `solnk_list_accounts` | Connected accounts (id, platform, username, status, capabilities) |
| `solnk_get_usage` | Plan limits and usage; check `can_publish` before posting |
| `solnk_publish` | Publish to one or more platforms (`immediate`, `scheduled`, `draft`) |
| `solnk_confirm_publish` | Confirm a draft so it goes out now or scheduled |
| `solnk_cancel_publish` | Cancel a draft or not-yet-sent scheduled publish |
| `solnk_get_publish_status` | Aggregate status of a publish |
| `solnk_list_publishes` | Recent publishes with filters |
| `solnk_get_post_analytics` | Rolled-up or per-platform metrics, with live post URLs |
| `solnk_create_media_upload` | Presigned upload for a local image or video |
| `solnk_confirm_media_upload` | Finalize a presigned upload |
| `solnk_create_media_from_url` | Ingest an image or video by public URL |

## Connect

Clients with native Streamable HTTP connect directly to `https://mcp.solnk.com/mcp` with an `Authorization: Bearer <key>` header. Clients that reach remote servers through `mcp-remote` use:

```
{
  "mcpServers": {
    "solnk": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.solnk.com/mcp",
               "--header", "Authorization:Bearer <key>"],
      "env": { "SOLNK_API_KEY": "<key>" }
    }
  }
}
```

Create a key at `https://solnk.com/settings/api-keys`. Self-hosting is `pnpm install && pnpm deploy` to your own Cloudflare account, with `SOLNK_API_BASE` pointing at the API to proxy.

## Limitations

- Publishing requires a valid key; discovery does not.
- Media larger than a platform's own limit is still rejected by that platform.
- Analytics are per published post, not cross-network attribution.

## FAQ

### Can I publish without confirming?

Yes. `solnk_publish` supports `draft` to stage content, then `solnk_confirm_publish` to send it, or `immediate` to go straight out.

### Is the API key stored on the server?

No. The worker is a stateless proxy; your key is forwarded per request and never stored.

### Can I self-host it?

Yes. It is a single MIT-licensed Cloudflare Worker you can deploy to your own account.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
