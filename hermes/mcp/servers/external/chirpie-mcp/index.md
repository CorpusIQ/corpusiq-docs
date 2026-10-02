---
title: "Chirpie MCP - Unified Social Posting Across 14 Platforms"
description: "Chirpie MCP is a unified social media layer for AI agents: one API to post, thread, schedule, delete and pull analytics across X, Bluesky, LinkedIn, Threads, Mastodon, Instagram, Facebook, Telegram and more, with accounts connected through a browser OAuth flow started from the agent so there are no per-platform API keys to manage."
category: Social Media Management
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3947"
relevance: ★★★
tags: [social-media, multi-platform, oauth, scheduling, analytics, remote-mcp, stdio]
---

# Chirpie MCP - Unified Social Posting Across 14 Platforms

**Remote MCP server (Streamable HTTP) with an npm stdio package** - Chirpie collapses social publishing into one agent surface: post, thread, schedule, delete and pull analytics across fourteen platforms through a single API. Accounts connect through a browser OAuth flow started from the agent itself, so there are no per-platform API keys to mint, rotate or vault.

```
Server type: Remote (Streamable HTTP) or local stdio (npm @chirpie/mcp)
Auth: Browser OAuth per platform, started from the agent; API keys for the Chirpie service itself
Endpoint: https://chirpie.ai/mcp (probe-verified live; JSON-RPC Authentication required)
Tools: 22 (posting, threading, account management, analytics, key management, platform connectors)
Pricing: Chirpie plans at chirpie.ai
Category: Social Media Management
Built by: Chirpie (chirpie.ai); repo github.com/Firefloco/chirpie-mcp
```

## Why This Matters for Operators

Every social platform has its own API, its own rate limits and its own credential model - and agents that post to several of them carry all of that complexity. Chirpie's OAuth-from-the-agent design removes the credential burden: the agent starts the connection flow, the operator signs in, and the platform account is connected with no developer app or token juggling.

**The tool surface mirrors the workflow: post and thread, list and delete, account activation switches, analytics pulls, and API-key management for the Chirpie service itself - all under one namespace so the agent never confuses platforms.**

## Tools & Capabilities

| Group | Tools |
|---|---|
| Posting | chirpie_post, chirpie_thread, chirpie_list_posts, chirpie_get_post, chirpie_delete_post |
| Account management | chirpie_list_accounts, chirpie_activate_account, chirpie_deactivate_account |
| Analytics | chirpie_analytics |
| Service keys | chirpie_create_key, chirpie_list_keys, chirpie_revoke_key |
| Platform connectors | chirpie_connect_x, chirpie_connect_linkedin, chirpie_connect_threads, chirpie_connect_instagram, chirpie_connect_facebook, chirpie_connect_bluesky, chirpie_connect_mastodon, chirpie_connect_telegram |
| X key management | chirpie_set_x_keys, chirpie_get_x_keys_status, chirpie_remove_x_keys |

## Installation

```bash
npx @chirpie/mcp
```

Or connect directly to the hosted endpoint https://chirpie.ai/mcp. Full setup at chirpie.ai/docs/mcp.

## Configuration

```json
{
  "mcpServers": {
    "chirpie": {
      "type": "http",
      "url": "https://chirpie.ai/mcp"
    }
  }
}
```

Platform accounts are attached through the browser OAuth flow; the Chirpie API key scopes the service itself. The endpoint probe returns a JSON-RPC Authentication required error, confirming the auth gate.

## Business Relevance

- **Founders** post to every platform from one agent conversation with one credential model.
- **Content teams** thread, schedule and delete across networks without per-platform tooling.
- **Agencies** swap client accounts with activate and deactivate switches instead of key rotation.
- **Community managers** pull cross-platform analytics in one call.

## Integration with CorpusIQ

Chirpie distributes; CorpusIQ attributes. A composed workflow: the agent posts a campaign across platforms through Chirpie, then reads the revenue and traffic response from CorpusIQ's GA4 and Stripe connectors to decide what the next post should say.

## Limitations

- Brand new listing (issue #3947, Sep 5, 2026); 0-star repo, npm package v1.0.35 verified.
- Posting to each platform still depends on completing that platform's OAuth flow.
- Platform coverage is what Chirpie's connectors support today; the vendor lists more coming.
- Analytics depth varies by platform's API surface.

## See Also

- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/hermes/mcp/servers/external/bulkpublish-mcp)
- [Antwork MCP - Social Publishing with Learned Brand Voice](/hermes/mcp/servers/external/antwork-mcp)
- [PostBazooka MCP - Social Publishing with Commit Proof](/hermes/mcp/servers/external/postbazooka-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
