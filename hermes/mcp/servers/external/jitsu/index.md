---
title: "Jitsu MCP - Manage Customer Data Pipelines from AI Agents"
description: "Official MCP server from Jitsu, the open-source Segment alternative with 5k+ GitHub stars. Agents manage the CDP workspace directly: list, create, update and delete destinations, streams, services, functions and connections, plus query live events. OAuth 2.1 or personal API key."
category: Data & Analytics
stars: 5043
added: 2026-08-25
source: "mcp.so GitHub issue #3740"
relevance: ★★★
tags: [mcp-server, cdp, customer-data, data-pipelines, jitsu, analytics, oauth]
---

# Jitsu MCP

**Give an AI agent direct control of your customer data platform.** Jitsu, the open-source Segment alternative, now runs an official MCP server so agents can manage the pipeline itself: create destinations, wire up streams, inspect Live Events, and edit Functions, all from inside a conversation. Every configuration object follows the same list / get / create / update / delete shape, so an agent that learns one resource knows them all.

```
Server type: Remote Streamable HTTP (official, hosted by Jitsu)
Endpoint: https://use.jitsu.com/mcp (self-hosted: /mcp on your own console host)
Auth: OAuth 2.1 browser approval (interactive) or personal API key (CI / headless)
Repo: github.com/jitsucom/jitsu (MIT, 5,043 stars)
Tools: 9 documented (list_workspaces, list_resources, get_resource, get_resource_schema,
  create_resource, update_resource, delete_resource, list_event_sources, query_events)
Verified: live endpoint confirmed; initialize returns 401 missing_token without auth
```

## Why This Matters for Operators

CDP configuration drift is a silent killer of data quality: a destination stops syncing, a function starts throwing, and nobody notices until a dashboard breaks. Jitsu MCP lets an agent both inspect and repair the pipeline: `query_events` exposes the same real-time stream as the Live Events UI (incoming events, function logs, warehouse write statuses, with an errors-only filter), and because Functions are configuration objects, the agent can read a failing function's code with `get_resource` and ship a fix with `update_resource` without leaving the conversation. The agent can even verify its own work: create a connection, send a test event, check that it landed.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_workspaces` | List the workspaces your account can access |
| `list_resources` | List resources of a type (destination, stream, service, function, connection) in a workspace |
| `get_resource` | Get a single resource by id |
| `get_resource_schema` | Get the JSON Schema for creating or updating a resource type |
| `create_resource` | Create a resource |
| `update_resource` | Update a resource by id |
| `delete_resource` | Delete a resource by id |
| `list_event_sources` | List the sources (streams, connections, destinations) you can read events for |
| `query_events` | Read recent Live Events for a stream, connection, or destination, with an errors-only filter |

## Installation

Interactive clients (Claude Code, Claude Desktop, Cursor, VS Code) connect with one URL and approve via a browser tab:

```bash
claude mcp add --transport http jitsu https://use.jitsu.com/mcp
```

Self-hosters replace `use.jitsu.com` with their own console host; the server is served at `/mcp` on the same host.

## Configuration

- **Interactive:** OAuth 2.1. The first tool call opens a browser tab asking you to approve the connection. The scoped, revocable token appears under your account settings and can be revoked any time.
- **CI / headless:** OAuth needs a browser, so generate a personal API key on the user settings page (`use.jitsu.com/user`) and pass it as `Authorization: Bearer <api-key>`. Keys have the format `{keyId}:{keySecret}`, the secret is shown once, and keys can be set to never expire. The key maps to your user and inherits your workspace access, so an agent running with it can do anything you can.

## Business Relevance

- **Pipeline self-healing:** agent detects a failing function from Live Events and patches it in place.
- **Faster integrations:** new destinations and streams configured by natural-language request instead of console clicking.
- **Auditable data ops:** every change goes through the same Management API as the UI, so it lands in your audit trail.

## Integration with CorpusIQ

Jitsu MCP covers pipeline configuration and live event inspection; CorpusIQ's connector fleet covers the business reporting layer on top of the warehouse. Use Jitsu MCP to verify a new stream is landing events, then query the results through CorpusIQ's database, GA4, or Stripe connectors for revenue and behavior analysis.

## Limitations

- No webhook or account/plan management tools; those stay in the Jitsu Dashboard.
- The MCP mirrors the Management API surface; advanced UDF testing still happens in the Jitsu UI.
- A CI-scoped API key inherits full workspace access: rotate and scope keys carefully.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Snowflake MCP - Data Warehouse Access for Agents](/hermes/mcp/servers/external/snowflake-mcp)
- [Crustdata MCP - Company and People Data APIs](/hermes/mcp/servers/external/crustdata)
