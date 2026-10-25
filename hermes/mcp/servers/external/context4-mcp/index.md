---
title: "Context4 MCP - One Gateway to CRM and Work Tools"
description: "One MCP endpoint over seven business services: amoCRM, Bitrix24, Pipedrive, Linear, GitHub, Sentry and Grafana, with 164 actions and per-account consent."
category: Business Operations / CRM
stars: n/a (commercial, free start, hosted)
added: 2026-10-25
source: "mcpservers.org /all p1 (midday sweep, October 25 2026) + live 401 probe and OAuth discovery + vendor published connector catalog"
relevance: ★★★
tags: [crm, pipedrive, bitrix24, amocrm, linear, sentry, grafana, oauth, business-context, action-layer]
---

# Context4 MCP

**One endpoint, seven business services, and a permission per service.** Context4 sits between an assistant and the systems a business actually runs on. The agent searches for a tool, asks for its schema, and executes it against an account the operator has explicitly connected.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://context4.me/mcp
Transport:   JSON-RPC 2.0 over HTTP, SSE responses
Auth:        OAuth 2.1, discovery at /.well-known/oauth-protected-resource/mcp
Scope:       mcp:tools (one scope at the door, permissions per connected account)
Tools:       5 stable meta-tools, 164 provider actions behind them
Built by:    Context4 (context4.me)
```

## Why This Matters for Operators

The assistant does not need a hundred tools. It needs a reliable way to find the right one and a record of who allowed it.

That is the shape Context4 chose. Rather than exposing every CRM field as a separate MCP tool, the server exposes five meta-tools and resolves the rest at call time from a published action catalog. Two consequences follow. The tool list stays stable as services are added, so an operator's client does not break every time a connector ships. And the permission boundary sits at the connected account, not at the tool name, so revoking a service is one action in a console rather than a client reconfiguration.

## What It Actually Does

The endpoint was probed live. An unauthenticated `POST initialize` to `https://context4.me/mcp` returned HTTP 401 with a structured error, `{"type":"urn:context4:error:authentication_required","title":"Authentication required","status":401,"code":"authentication_required","request_id":"..."}`, so the route is live and fronted by its own error contract rather than a generic 404.

Discovery answers properly. `/.well-known/oauth-protected-resource/mcp` returns 200 with resource `https://context4.me/mcp`, authorization server `https://context4.me`, scope `mcp:tools`, bearer in header and a documentation pointer. `/.well-known/oauth-authorization-server` adds `authorize`, `token`, `register` and `revoke`, `authorization_code` plus `refresh_token`, and `token_endpoint_auth_methods_supported: ["none"]`, which is a public client with PKCE, so nothing secret is stored on the operator's machine.

The five meta-tools are documented with full JSON Schemas and strict input validation, which rejects unknown fields and caps `arguments` at 65,536 serialized characters:

| Meta-tool | What it does |
|---|---|
| `CONTEXT4_SEARCH_TOOLS` | Finds provider actions for a task, returns connection readiness, filters on tags such as `read-only`, `destructive`, `idempotent` |
| `CONTEXT4_GET_TOOL_SCHEMAS` | Returns the exact input and output schema for a discovered action |
| `CONTEXT4_MANAGE_CONNECTIONS` | Starts and manages the connection to a provider account |
| `CONTEXT4_WAIT_FOR_CONNECTIONS` | Blocks until a consent flow finishes |
| `CONTEXT4_MULTI_EXECUTE_TOOL` | Runs one or more discovered actions against connected accounts |

The provider actions come from the vendor's own catalog file, `https://context4.me/docs/connectors.json`, read in this sweep: seven connectors, all marked `beta`, 164 actions in total.

| Connector | Version | Auth | Actions |
|---|---|---|---|
| amoCRM | 2.2.0 | OAuth 2 | 21 |
| Bitrix24 | 1.1.0 | OAuth 2 | 23 |
| GitHub | 1.1.0 | OAuth 2 | 24 |
| Grafana | 1.2.0 | API key | 38 |
| Linear | 1.4.0 | OAuth 2 | 18 |
| Pipedrive | 1.0.0 | OAuth 2 | 15 |
| Sentry | 1.1.0 | API key | 25 |

A parallel HTTP API exists at `https://context4.me/v1`, and a Composio-compatible base URL at `https://context4.me/compat/context4/v1` names where the execution layer comes from: the provider calls are proxied, which is why one endpoint can carry seven services.

## Installation

Add the remote server to any client that supports streamable HTTP and let OAuth discovery do the rest.

```
claude mcp add --transport http context4 https://context4.me/mcp
```

The vendor publishes client guides for ChatGPT, Claude, Codex, Claude Code, Hermes and OpenClaw, plus an `llms.txt` and an agent index at `https://context4.me/docs/agent-index.json`. Accounts are connected in the console at `https://console.context4.me/integrations`, and access can be revoked per service there.

## Business Relevance

Ask a question that spans two systems and the answer needs both. "Which deals did the client mention in last week's support incident?" is a CRM record plus an error report. "Which open issues are blocking the billing migration?" is Linear plus GitHub.

An assistant given read access to a CRM can answer those. An assistant given the action layer can also file the follow-up task in the same breath. What this catalog cares about is the middle: does the operator know, and control, what each service allowed. Here the answer is yes, per connected account, with a single scope at the door and a per-service switch in the console.

## Integration with CorpusIQ

The services Context4 fronts are the same class CorpusIQ connects directly: CRM, project tracking and engineering telemetry as read-only sources, with the operator keeping the account. It is catalogued as a comparison point and as a route for teams already standardised on amoCRM or Bitrix24, which this catalog had no entry for.

## Limitations

- No tool call was executed in this sweep. Every action needs an OAuth session, a workspace and a connected provider account, none of which this pass creates. The 401, the two discovery documents and the published catalog are the evidence; the executed path is the gap.
- No entry in the official MCP registry: `registry.modelcontextprotocol.io` search for `context4` returned zero servers on October 25, 2026.
- All seven connectors are marked `beta`, which is stated by the vendor rather than inferred.
- Documentation and the console are in Russian. The MCP contract is machine-readable and English-keyed, but an English-only operator is reading vendor pages through translation.
- The vendor's homepage illustrations show services that are not in the published catalog, including Wazzup and FinTablo, and the markup labels those as illustrations rather than live data. Treat `connectors.json` as the real list.
- No public price list was found on the pages read. The site advertises a free start, and plan limits sit inside the tools rather than at the door.
- The catalog already carries CRM servers at product level, including OnePageCRM, Perfex CRM and onvela CRM. What none of them carry is Pipedrive, Bitrix24 or amoCRM, or a single gateway over several business services with per-account consent, which is the slot this entry fills.

## FAQ

### Do I need a paid plan?

No price list was published on the pages read in this sweep, and the site advertises a free start. Plan limits are enforced inside the tools, so a capped call returns an error rather than refusing the connection.

### Which services can an agent reach?

Seven, from the published connector catalog: amoCRM, Bitrix24, Pipedrive, Linear, GitHub, Sentry and Grafana. All are marked beta. Anything else is not reachable until it appears in that catalog.

### Can the agent change data?

Yes, and that is the point of the action layer. Individual actions carry tags including `read-only` and `destructive`, so a client can search only for reads, and each connected account is separately revocable in the console.

### Where does the credential live?

Nowhere on the operator's machine. The client registers as a public OAuth client with PKCE, and provider tokens stay server-side against the connected account.

## See Also

- [Perfex CRM MCP - Self-Hosted CRM for Agents](/hermes/mcp/servers/external/perfex-crm-mcp/)
- [CRMSolid MCP - CRM Records for Agents](/hermes/mcp/servers/external/crmsolid-mcp/)
- [Muvia BI MCP - Governed Data Platform for Agents](/hermes/mcp/servers/external/muvia-bi-mcp/)
