---
title: "Social Glass MCP: Cultural Intelligence for Brand and Research Teams"
description: "Remote MCP server that gives brand and research teams evidence-backed cultural intelligence: search Insights, Posts, Creators, and Audiences inside the signed-in user's permitted Social Glass organizations. OAuth on connect, read tools for members, write tools for admins."
category: Content & Research
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3734"
relevance: ★★★
tags: [consumer-insights, cultural-intelligence, social-media-research, brand-strategy, audience-research, marketing, oauth, remote-mcp]
---

# Social Glass MCP

**Remote MCP server (Streamable HTTP, OAuth) for evidence-backed cultural intelligence.** Built by Social Glass, this server lets authorized brand and research teams explore live culture and consumer insights directly from an agent: search Insights, Posts, Creators, and Audiences within the organizations the signed-in user is permitted to access. Read tools are the default; write tools are reserved for Social Glass admins.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (preferred) or Clerk API key with social-glass:mcp scope
Endpoint: https://mcp.socialglass.ai/mcp
Tools: Read tools over Insights, Posts, Creators, Audiences (exact names served after OAuth)
Pricing: Not published (account-gated)
Category: Data & Analytics / Research
Built by: Social Glass (repo: Social-Glass-AI/social-glass-agent-plugins)
```

## Why This Matters for Operators

Consumer insight work today means a human analyst copying platform posts into a spreadsheet, manually sizing audiences, and guessing which creators actually matter. Social Glass MCP moves that into the agent loop: the model can search evidence-backed insights, pull post and creator data, and size audiences, then reason over the results in the same conversation where the business question was asked. **The evidence is attached to the claim** - insights, posts, and creators come back with the underlying data, so recommendations read as findings, not vibes.

For a growth team, the practical win is speed: a positioning question ("what are operators actually complaining about around agent tooling this month") becomes one prompt instead of an afternoon of manual platform browsing.

## Tools & Capabilities

Exact tool names are served from the endpoint after the OAuth flow completes (anonymous enumeration is refused, HTTP 401 before auth). The documented surface:

| Tool | Purpose |
|---|---|
| `get_context` | Session and organization context bootstrap; call first, per the vendor docs |
| Insight search | Search evidence-backed cultural insights across permitted organizations |
| Post search | Search platform posts with engagement evidence |
| Creator search | Discover creators with audience and content data |
| Audience search | Size and segment audiences for targeting decisions |

Capability-level table from vendor documentation; the live tool list is served post-auth.

## Installation

```bash
claude mcp add --transport http social-glass https://mcp.socialglass.ai/mcp
```

Claude Code users finish signing in with `/mcp`. Codex users run `codex mcp add social-glass --url https://mcp.socialglass.ai/mcp` then `codex mcp login social-glass --scopes profile,email`. The vendor also ships a plugin for Codex and Claude Code that installs the MCP connection plus workflow skills together.

## Configuration

```json
{
  "mcpServers": {
    "social-glass": {
      "type": "http",
      "url": "https://mcp.socialglass.ai/mcp"
    }
  }
}
```

OAuth is the preferred path: connect to the endpoint and complete the browser sign-in. If the client cannot retain OAuth sessions and the workspace has Clerk user API keys enabled, create a key with the `social-glass:mcp` scope and send it as the bearer token. Troubleshooting per the vendor: 401 means reconnect and finish signing in; 403 means the account cannot access the selected organization (write tools also require an admin account).

## Business Relevance

- **Growth and marketing teams** search evidence-backed consumer insights instead of manually browsing platforms
- **Brand strategists** ground positioning work in cultural data with the evidence attached
- **Research agencies** run audience sizing and creator discovery inside the agent conversation
- **Media planners** identify creators and audiences with data instead of gut feel

## Integration with CorpusIQ

Social Glass answers "what is culture doing"; CorpusIQ answers "what is the business doing". The two compose cleanly: an agent can search Social Glass for audience and creator intelligence on a target segment, then pull campaign spend, web traffic, and conversion data from the CorpusIQ Meta Ads, GA4, and Klaviyo connectors to see whether that segment is actually converting. A positioning exercise becomes one workflow: cultural evidence from Social Glass, commercial truth from CorpusIQ.

## Limitations

- Brand new listing (Aug 24, 2026); repo has no star history yet.
- OAuth-gated: anonymous tool enumeration is refused, so pre-purchase evaluation requires an account.
- Pricing is not published; read access follows account and organization permissions.
- Write tools are admin-only, so agent workflows that mutate data need an admin seat.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
