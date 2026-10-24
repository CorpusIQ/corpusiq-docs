---
title: CorpusIQ MCP install instructions for agents
description: "Install the CorpusIQ MCP server in Cline, Claude Code, Cursor, VS Code, Gemini CLI or any remote MCP client. One HTTP endpoint, OAuth 2.1, no package to install."
last_updated: "2026-10-23"
---
# CorpusIQ MCP: install instructions for agents

This file is written for AI agents and coding assistants (Cline, Claude Code, Cursor, VS Code, Gemini CLI, Hermes, OpenClaw) that install MCP servers by reading a repository. It is the complete setup path. You do not need any other file.

## What this server is

CorpusIQ is a remote MCP server that gives an AI client read-only access to a business's own systems: QuickBooks, Shopify, Stripe, GA4, HubSpot, Klaviyo, Slack, and 40+ connectors in total. The client asks a question, CorpusIQ retrieves the records live from the connected source and returns them with the source cited. Nothing is stored.

- Transport: Streamable HTTP (remote, no local install, no container, no package)
- Endpoint: `https://mcp2.corpusiq.io/mcp`
- Auth: OAuth 2.1 with dynamic client registration and PKCE
- Access: read-only retrieval. Answers cite the source system.

## Install in three steps

1. Add the remote server entry to the client config shown below.
2. Start the client. It will open a browser for OAuth.
3. Sign in with a CorpusIQ account and approve. The 30-day trial needs no credit card.

There is no API key to paste and no environment variable to set. Authentication happens through the OAuth flow.

## Client configuration

### Claude Code

```bash
claude mcp add --transport http corpusiq https://mcp2.corpusiq.io/mcp
```

### Claude Desktop, Cline, and any client using `mcpServers`

```json
{
  "mcpServers": {
    "corpusiq": {
      "type": "http",
      "url": "https://mcp2.corpusiq.io/mcp"
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp"
    }
  }
}
```

### VS Code

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "corpusiq": {
      "type": "http",
      "url": "https://mcp2.corpusiq.io/mcp"
    }
  }
}
```

### Gemini CLI

```bash
gemini extensions install https://github.com/CorpusIQ/corpusiq-docs
```

This repository ships `gemini-extension.json`, so the extension name is `corpusiq` and the server is registered automatically.

### Generic remote MCP client

- URL: `https://mcp2.corpusiq.io/mcp`
- Transport: `streamable-http`
- Auth: OAuth 2.1, discovery at `https://mcp2.corpusiq.io/.well-known/oauth-protected-resource`
- Authorization server: `https://mcp2.corpusiq.io`
- Optional client registration endpoint: `https://mcp2.corpusiq.io/oauth/register`
- Scopes: `openid`, `email`, `profile`
- Token endpoint auth methods: `client_secret_basic`, `client_secret_post`, `none`

## Verify the installation

A correctly configured client completes this handshake. Sending `initialize` to the endpoint returns the server identity:

```bash
curl -s -X POST https://mcp2.corpusiq.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"install-check","version":"1.0"}}}'
```

A healthy server answers with `serverInfo.name` set to `multi-source-mcp`. After OAuth completes, `tools/list` returns the tool catalogue. The first tool to call for a general business question is `ask_corpusiq`.

## Expected behaviours that are not failures

- A plain `GET` to `/mcp` returns HTTP 406. That is correct. The endpoint speaks JSON-RPC over POST.
- An unauthenticated `tools/list` returns 401. That is the OAuth gate, not an outage.
- The negotiated protocol version may differ from the one requested. The server selects the version it supports.

## Frequently asked questions

### Do I need an API key or an environment variable?

No. Authentication is OAuth 2.1. The client opens a browser, the user signs in to CorpusIQ, and the client receives a token. There is no key to paste.

### Why does a plain GET to the endpoint return 406?

The endpoint speaks JSON-RPC over POST and requires an `Accept` header that includes `application/json` and `text/event-stream`. A 406 on a bare GET is the expected response and does not indicate an outage.

### Why does tools/list return 401 before the user signs in?

The server gates every tool behind OAuth. A 401 before the browser flow completes is the authentication gate working correctly.

### Does CorpusIQ store the data it retrieves?

No. CorpusIQ fetches source records live for the duration of the request and returns them to the client. Query text, per-user tool-call metadata and bounded outcome summaries are retained in operational logs for up to 30 days. Raw connector payloads are not retained and no embeddings or file indexes are built.

### Which tool should an agent call first?

`ask_corpusiq` for a general business question, including financial snapshots. It routes to the right connectors and returns an answer with the source cited.

## Support

- Documentation: https://docs.corpusiq.io
- Connector reference: https://www.corpusiq.io/connectors
- Connection troubleshooting: https://docs.corpusiq.io/hermes/troubleshooting/corpusiq/
