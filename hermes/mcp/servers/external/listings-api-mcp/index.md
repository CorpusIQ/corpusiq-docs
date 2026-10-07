---
title: "Listings API MCP - Local Citations and Reviews"
description: "Publish a business to 80+ directories and maps from one write, manage reviews and Google Business Profile posts, from your agent."
category: Marketing
stars: n/a (hosted platform, listingsapi.com)
added: 2026-10-07
source: "mcp.so /feed (Oct 7, 2026 midday sweep)"
relevance: ★★★
tags: [local-seo, citations, reviews, google-business-profile, listings, agencies, oauth, remote-mcp]
---

# Listings API MCP

**Hosted MCP server (Streamable HTTP) for local search** - create a location once and publish it to Google, Apple, Bing, Yelp, Facebook and dozens more from a single write, catch new reviews across sites, reply on Google and Facebook, and post updates to Google and Facebook profiles, all callable by your agent.

```
Server type: Hosted (Streamable HTTP, POST only)
Auth: OAuth 2.0 sign-in or an API key sent as Authorization: API <key>
Endpoint: https://listingsapi.com/mcp
Tools: Locations, reviews, posts and analytics over the v4 API and an 80+ directory network
Pricing: From $99/mo with a 14-day free trial; no-card sandbox day pass available
Built by: ListingsAPI
```

## Why This Matters for Operators

Multi-location businesses and the agencies that run them live with a fragmentation tax: every directory is its own login, every review site its own inbox, and every name, address or phone change its own error source. Listings API collapses that into one record per location as the single source of truth: one write reaches the 80+ network, the premium listings read reports the live sync status per directory so drift is visible, reviews are crawled and replyable through the API, and posts go to Google and Facebook in one call with per-channel confirmation. The MCP server is agent-native: llms.txt, an auth.md guide, an OpenAPI spec and a loadable SKILL.md, so a coding agent can read the docs and write the integration itself.

## Tools & Capabilities

| Capability | What the agent can do |
|---|---|
| Locations | Create and update the source-of-truth record; read sync status; list premium listings per directory |
| Reviews | List new reviews across review sites; reply on Google and Facebook |
| Posts | Publish to Google and Facebook in one call; each channel reports when the post is live |
| Analytics | Read location and Google analytics |
| Agent docs | llms.txt, llms-full.txt, auth.md, openapi.yaml, SKILL.md and an RFC 9727 api-catalog |

The REST v4 API and typed Python and Node SDKs back the same operations for scheduled jobs and dashboards.

## Installation

```
claude mcp add --transport http listingsapi https://listingsapi.com/mcp --header "Authorization: API <your-api-key>"
```

In clients that support OAuth 2.0, skip the key and sign in; approving creates an API key named after the client, visible in your dashboard. Codex, Cursor and Windsurf configuration files are published on the MCP page; stdio-only clients bridge through `mcp-remote`.

## Configuration

```json
{
  "mcpServers": {
    "listingsapi": {
      "url": "https://listingsapi.com/mcp",
      "headers": { "Authorization": "API <your-api-key>" }
    }
  }
}
```

## Business Relevance

- **Multi-location operators:** keep addresses, phone numbers and hours synced across maps and directories from one record instead of a dozen logins.
- **Agencies:** run citation cleanups, review responses and local posts for client locations from the same chat that drafts the work.
- **Local SEO teams:** read the per-directory sync status after each write and verify the network actually updated instead of assuming it did.

## Integration with CorpusIQ

CorpusIQ surfaces what is happening with your locations from connected systems, read-only. Listings API maintains the public listings themselves. Read performance in CorpusIQ, make changes through Listings API, and verify each write with the sync status endpoint.

## Limitations

- Paid product: from $99/mo; the sandbox day pass is offered for limited periods.
- The MCP server answers POST only; use a client to reach it, not a browser GET.
- Review replies currently cover Google and Facebook; other sources are crawl-and-read.
- Writes are real: give the agent a dedicated key so it can be revoked on its own.

## FAQ

### How do I try it without paying?

The sandbox day pass needs no card. Sign up in the browser, or let your agent start it - the key arrives once you confirm by email.

### Which networks are covered?

Google Business Profile, Apple Maps, Bing Places, Yelp, Facebook, Tripadvisor, Instagram, Waze, MapQuest, Yellow Pages, Superpages, DexKnows, Citysearch, Opendi, iGlobal, Hotfrog and more, with per-plan coverage in the network overview.

### Can the agent reply to reviews?

Yes, on Google and Facebook. Other review sources are crawled and readable for monitoring.

### Does it manage Google Business Profile?

Yes - posts, reviews and insights for connected locations are part of the same location record and API surface.

## See Also

- [Localith MCP - Google Business Profile Data for Agents](/hermes/mcp/servers/external/localith-mcp)
- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp)
- [Revup MCP - Promotions, Forms and Giveaways](/hermes/mcp/servers/external/revup-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
