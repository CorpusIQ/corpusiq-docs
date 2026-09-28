---
title: "Scribase MCP - Hosted Postgres for Coding Agents"
description: "Scribase is a hosted Postgres backend for coding agents with confirm-gated writes and RLS isolation proven before any schema change ships."
category: DevOps
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (scribase.com)"
relevance: ★★
tags: [postgres, database, schema, dev-tools, rls, coding-agents, remote-mcp]
---

# Scribase MCP

**A hosted Postgres backend an AI agent cannot wreck.** Scribase gives Claude Code, Cursor and any MCP client 44 tools over your projects: reads run immediately, every write waits for an explicit confirm, and schema changes must pass a row-level-security isolation test before they can ship.

```
Server type: Remote (stdio or Streamable HTTP at /mcp)
Auth: personal access token or org API key, audited per call
Endpoint: https://api.scribase.com/mcp
Tools: 44 (schema, data, previews, backups, policies)
Pricing: vendor pricing (scribase.com)
Category: DevOps / Database
Built by: Scribase (scribase.com)
```

## Why This Matters for Operators

The moment you let a coding agent touch a production database you inherit a new failure class: plausible-looking schema changes that break isolation between tenants or destroy data. Scribase addresses the specific risk with two mechanisms, confirm-gated writes that return the exact request before execution, and an RLS proof system where `schema.apply` only accepts a token from `policy.test`, which proves the isolation matrix and then deliberately breaks each guarantee to show the proof works.

Preview branches add the last missing layer: changes land on a time-limited sanitized copy of production, and merges are foreign-key safe and preceded by a backup.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Reads and writes | 44 tools over projects; writes confirm-gated |
| Schema management | schema.apply requires a passing policy.test token |
| RLS policy testing | policy.test proves the isolation matrix before ship |
| Preview branches | TTL-swept sanitized copies for safe iteration |
| Backups and merges | Foreign-key safe merges, backups before every merge |

Only `schema.apply` and `policy.test` are named in the published docs; the remaining tools are served from the endpoint.

## Installation

```bash
claude mcp add scribase --transport http https://api.scribase.com/mcp
```

An install-once setup plus editor integration flow is documented on the server page.

## Configuration

```json
{
  "mcpServers": {
    "scribase": {
      "type": "http",
      "url": "https://api.scribase.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** let coding agents build internal tools against a database that cannot be silently broken
- **CTOs** get schema changes gated behind provable RLS isolation
- **Data teams** preview changes on sanitized branches before they touch production
- **Agencies** ship client data work with an audit trail per API call

## Integration with CorpusIQ

Scribase is the safe landing zone for data CorpusIQ connectors already pull: QuickBooks financials, Stripe charges and Shopify orders can be materialized into Scribase-managed Postgres for agent-driven analysis, where the confirm gate prevents an over-eager assistant from mutating source data.

The CorpusIQ GitHub connector closes the loop on delivery: schema changes proposed by an agent in Scribase can be reviewed as normal pull requests, with the RLS proof attached as evidence.

## Limitations

- New listing, no track record yet
- Only two of 44 tools are named in public docs
- No free tier disclosed on the directory listing
- Database-only scope, no application hosting
- Requires comfort with Postgres concepts to configure well

## FAQ

### How does it stop an agent from breaking production?

Writes are confirm-gated, meaning the agent must approve the exact request, and schema changes require a passing RLS isolation test first.

### What is the RLS proof?

policy.test proves the isolation matrix, then breaks each guarantee on purpose to show the proof can fail. Only that token unlocks schema.apply.

### Can I try changes safely?

Yes. Preview branches are time-limited sanitized copies of production, and merges are foreign-key safe with a backup first.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
