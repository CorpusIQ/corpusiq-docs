---
title: "MCPGRAM MCP - OAuth Connectivity Gateway for AI Agents"
description: "MCPGRAM MCP server connects Slack, GitHub, Google, Salesforce and 30+ business apps to any AI agent through one OAuth 2.1 gateway with per-workspace consent, token isolation, and a single Streamable HTTP endpoint"
category: Connectivity
stars: n/a (new listing)
added: 2026-08-19
source: "mcp.so GitHub issue #3646"
relevance: ★★
tags: [connectivity, oauth, gateway, slack, salesforce, github, integrations, remote-mcp, productivity]
---

# MCPGRAM MCP

**One OAuth gateway that connects Slack, GitHub, Google, Salesforce, and 30+ business apps to any MCP client.** MCPGRAM acts as both MCP server and authorization server: a single Streamable HTTP endpoint where an agent authenticates once with OAuth 2.1 (DCR + PKCE), consents to a workspace, and receives a token scoped to that workspace's tools only.

```
Server type: Remote (Streamable HTTP) or local stdio
Auth: OAuth 2.1 (DCR + PKCE) or bearer workspace API key
Endpoint (OAuth): https://mcpgram-mcp-server.vercel.app/mcp
Endpoint (API key): https://mcpgram.vercel.app/api/mcp
Apps: Slack, GitHub, Google, Salesforce + 30 more
Pricing: Not published (website + docs at mcpgram.vercel.app)
Category: Connectivity
Built by: Aryan418-dev (MCPGRAM)
```

## Why This Matters for Operators

Operators today wire each business app into each agent separately: one OAuth flow for Slack, another for Salesforce, another for GitHub. MCPGRAM collapses that into one consent screen and one token per workspace. The isolation design is the key safety property: each user's OAuth token only carries their own selected workspace API key, so one agent session cannot silently reach another tenant's tools.

For operators running multiple client workspaces or internal teams, this means a single gateway to configure and audit — the consent flow records which workspace an agent was granted access to, instead of scattering API keys across client config files.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Multi-app gateway | Connects Slack, GitHub, Google, Salesforce, and 30+ apps through one endpoint |
| OAuth 2.1 flow | Built-in DCR, PKCE, authorize, token, and revoke endpoints — no external Auth0/WorkOS dependency |
| Workspace consent | Consent selects the workspace; tokens bind to that workspace's API key |
| Token isolation | Each user's token only carries their own workspace key |
| Dual paths | OAuth for Claude/Cursor; bearer workspace API key for HTTP clients |

## Installation

OAuth path (Claude, Cursor — the client discovers authorization on the same origin):

```json
{
  "mcpServers": {
    "mcpgram": {
      "type": "http",
      "url": "https://mcpgram-mcp-server.vercel.app/mcp"
    }
  }
}
```

API-key path (HTTP clients such as Manus):

```json
{
  "mcpServers": {
    "mcpgram": {
      "type": "http",
      "url": "https://mcpgram.vercel.app/api/mcp",
      "headers": { "Authorization": "Bearer <workspace-key>" }
    }
  }
}
```

Smithery install: `npx -y smithery mcp add aaryanverma4326/Mcpgram`

## Configuration

Self-hosting the gateway requires the full OAuth environment: `MCP_PUBLIC_URL`, `OAUTH_JWT_SECRET`, Supabase URL/anon key/service key, and `MCPGRAM_BASE_URL` pointing at the MCPGRAM API. The hosted deployment at mcpgram-mcp-server.vercel.app needs none of this — connect and consent.

Repository: `github.com/Aryan418-dev/mcpgram-mcp-server` (server) and `github.com/Aryan418-dev/mcpgram-dashboard` (dashboard). No license file declared on either repository at time of cataloguing (checked Aug 19, 2026).

## Business Relevance

- **Agency operators** manage many client workspaces through one consent screen instead of per-app OAuth dances
- **RevOps and IT** get a single audit point for which agent touched which workspace
- **Automation builders** reach Slack, Salesforce, and GitHub from one endpoint without managing three token stores
- **Security-conscious teams** get per-workspace token isolation instead of shared org-wide keys

## Integration with CorpusIQ

MCPGRAM is the app-connectivity layer; CorpusIQ is the business-data layer. An operator can run both in one agent session: CorpusIQ for financials, CRM records, and marketing data across 40+ connectors, MCPGRAM for the workspace tools those same teams live in — Slack threads, GitHub repos, Salesforce objects — then join the two on customer or project identifiers. They overlap on Salesforce and Google: use CorpusIQ when you need structured analytics across connectors, MCPGRAM when you need the raw app surface.

## Limitations

- New listing (Aug 2026), zero-star repositories, no track record
- No license declared on either repository — review before commercial use
- Tool surface depends on which apps the workspace has connected
- Hosted endpoints are third-party dependencies; self-hosting requires a Supabase-backed OAuth stack
- Pricing for the hosted gateway is not published in the docs

## See Also

- [WaveSpeed MCP — Media Generation](/hermes/mcp/servers/external/wavespeed-mcp/)
- [SYNTHORA MCP — Verified Multi-Source Intelligence](/hermes/mcp/servers/external/synthora-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
