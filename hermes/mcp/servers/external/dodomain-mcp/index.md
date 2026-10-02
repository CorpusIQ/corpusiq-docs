---
title: DoDomain MCP - Domain and DNS Operations for Agents
description: "OAuth remote MCP server with eight scoped tools for checking a domain's DNS provider, minting connect sessions and verifying DNS."
category: Business Operations
stars: n/a (hosted service, dodomain.io)
added: 2026-10-01
source: "mcpservers.org /all (dodomain-io-docs-connecting-ai-assistants)"
relevance: ★★
tags: [domains, dns, infrastructure, devops, oauth, remote-mcp]
---

# DoDomain MCP

**Domain and DNS checks an agent can run and verify.** DoDomain exposes its DNS tooling over a remote MCP server: check a domain's DNS provider, mint a connect session, hand a user the hosted connect link, and verify DNS records - all using the same REST API and permissions an integration already has.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: OAuth 2.1 with PKCE and dynamic client registration
Endpoint: https://app.dodomain.io/api/mcp
Tools: 8 (domain checks, connect sessions, DNS verification)
Pricing: requires a DoDomain account
Category: Business Operations
Built by: DoDomain
```

## Why This Matters for Operators

DNS is a piece of infrastructure that agents are asked to touch constantly and are usually bad at, because verification is a separate manual step. DoDomain closes that loop in tools: an agent can check what provider a domain uses, walk a user through connecting it, and then verify the records landed - rather than declaring success and leaving a broken zone behind.

The setup is agent-native too. A single prompt to a coding agent fetches DoDomain's setup instructions, adds the server, installs the matching SDK and verifies the result, so onboarding is one sentence rather than a config hunt.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Provider check | Identify a domain's DNS provider |
| Connect session | Mint a connect session and hand the user a hosted connect link |
| DNS verification | Verify DNS records after a change |
| Scoped access | Eight tools, each carrying its own permission from the integration's existing model |

Eight scoped tools. The public page describes the capability set and the OAuth flow rather than publishing the full identifier list.

## Installation

```
claude mcp add --transport http dodomain https://app.dodomain.io/api/mcp
```

For Codex:

```
codex mcp add dodomain --url https://app.dodomain.io/api/mcp
codex mcp login dodomain
```

Or paste this into Claude Code, Cursor, OpenCode or Copilot to let the agent set itself up:

```
Fetch and execute the appropriate instructions to set me up for DoDomain from https://dodomain.io/agent-setup/prompt.md
```

## Configuration

```json
{
  "mcpServers": {
    "dodomain": {
      "url": "https://app.dodomain.io/api/mcp"
    }
  }
}
```

## Business Relevance

- **Agencies and web shops** can have an agent check a client's DNS, run the connect flow and verify the records, without a specialist.
- **SaaS onboarding teams** can turn "point your domain at us" into an agent-guided, verified step.
- **DevOps and platform teams** get a verification loop built into the change rather than a separate check.
- **AI agents** get an infrastructure surface that verifies its own work instead of assuming success.

## Integration with CorpusIQ

CorpusIQ holds the business and customer record; DoDomain verifies the infrastructure those customers depend on. An agent can read which domains belong to which accounts from CorpusIQ's connectors, then check DNS health and run a connect flow through DoDomain - customer data and infrastructure state in one workflow, so a provisioning task has both the who and the whether-it-worked.

## Limitations

- Requires a DoDomain account; tools carry the permissions of the connected integration.
- Focused on domain and DNS operations, not a general infrastructure control plane.
- Uses OAuth 2.1 with dynamic client registration, so the client must support the standard discovery documents.
- The public page describes eight scoped tools at a capability level rather than listing identifiers.

## FAQ

### What does the DoDomain MCP server do?

It lets an AI agent check a domain's DNS provider, mint a connect session, hand a user a hosted connect link and verify DNS records, using the same permissions the integration already has.

### How does authentication work?

OAuth 2.1 with PKCE and dynamic client registration; the server publishes RFC 9728 and RFC 8414 discovery documents so clients register and sign in automatically. No API keys are involved.

### Which clients work?

Claude, Claude Code, Codex, Cursor, OpenCode, GitHub Copilot and any MCP client that supports remote servers with OAuth.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
