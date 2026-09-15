---
title: Abyssale MCP - Ad Creative Production for Agents
description: Hosted MCP server from Abyssale for programmatic ad creative. Browse workspace designs, projects and fonts, generate banners, videos and print-ready PDFs, and import designs from JSON from Claude, ChatGPT or Cursor with per-client OAuth scopes and a credit system.
category: Marketing
stars: n/a (new listing)
added: 2026-09-05
source: mcpservers.org
relevance: ★★★
tags: [creative-production, ad-banners, html5-ads, design-automation, marketing-ops, oauth, streamable-http, remote-mcp]
---

# Abyssale MCP

**Remote MCP server (Streamable HTTP, OAuth)** - lets an AI assistant act on an Abyssale workspace from a conversation: browse designs and projects, look up fonts and credit balance, generate banners, videos and print-ready PDFs, and import new designs from JSON, without writing any code against the REST API.

```
Server type: Remote (Streamable HTTP, POST only, stateless)
Auth: OAuth (Abyssale account sign-in, per-client scopes, no API keys)
Endpoint: https://mcp.abyssale.com/mcp
Tools: 16 (identity, discovery, generation, design import)
Pricing: Workspace credits and plans, tracked via get_remaining_credits
Category: Marketing
Built by: Abyssale (abyssale.com)
```

## Why This Matters for Operators

Ad creative production is the highest-volume, most repetitive asset pipeline a marketing team runs: one design concept needs resizes for every placement, translated variants, animated HTML5 versions and print-ready exports. Abyssale MCP turns that pipeline into conversation, so an operator can say "generate this banner in all six IAB sizes" and the agent handles the format matrix.

OAuth scopes are per client, which makes the server safe to hand out: a designer's agent can be limited to browsing designs while only the media-buyer's agent can spend generation credits. Registered clients today are Claude Code CLI, Claude.ai, ChatGPT/Codex and Cursor.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_me` | Check which Abyssale workspace the client is connected as |
| `list_designs` / `search_designs` | Browse and search the workspace design library |
| `get_design` / `get_design_format` | Full design detail and its export formats |
| `get_design_as_import` | Export a design as an importable JSON structure |
| `list_projects` / `create_project` | Browse projects and create new ones |
| `list_fonts` | Font library available for designs |
| `get_remaining_credits` | Generation credit balance |
| `generate_static_banner` | Single image render on demand |
| `generate_banners_async` | Multi-format, multi-banner batch generation (images, video, animated GIFs, HTML5) |
| `generate_multipage_pdf` | Print-ready PDF output |
| `check_generation_status` | Poll asynchronous generation state |
| `import_design_from_json` | Create a design from a JSON structure, including images that live on the local machine |
| `check_design_import_status` | Import progress and validation errors |

## Installation

```bash
claude mcp add --transport http abyssale https://mcp.abyssale.com/mcp
```

Then complete the OAuth sign-in with an Abyssale account. The vendor publishes per-client setup steps for Claude Code CLI, Claude.ai, ChatGPT/Codex and Cursor.

## Configuration

```json
{
  "mcpServers": {
    "abyssale": {
      "url": "https://mcp.abyssale.com/mcp"
    }
  }
}
```

Auth notes: the MCP server uses OAuth, not the REST API's x-api-key header. There is no key to copy; access is scoped per client, so a client can be allowed to read designs without being allowed to spend generation credits.

## Business Relevance

- **Marketing teams** produce the banner matrix for every campaign in one conversation instead of manual editor sessions.
- **Agencies** scope client access per agent: designers browse, buyers generate.
- **E-commerce operators** generate product visuals and HTML5 ads from a sheet of product data plus a design template.
- **Print operations** get multi-page PDF exports through the same toolset as digital banners.

## Integration with CorpusIQ

CorpusIQ reads campaign and store performance - ad spend, ROAS, conversion data - while Abyssale produces the creative assets that feed those campaigns. When a CorpusIQ report shows which creative is tiring, the operator hands the winning and losing variants to the Abyssale agent to generate the next test batch from the same design system. CorpusIQ measures, Abyssale produces, and the loop closes on data.

## Limitations

- Registered clients are Claude Code CLI, Claude.ai, ChatGPT/Codex and Cursor; other MCP clients are not registered yet.
- Stateless sessions (POST only), so no long-lived connection state to reconnect.
- Generation spends real workspace credits; scope the write tools carefully per client.
- The MCP surface covers 16 tools; deeper REST API operations stay outside MCP.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [OpenShorts MCP - Video Clipping and Publishing for AI Agents](/docs/hermes/mcp/servers/external/openshorts-mcp)
- [Viral Manager MCP - Creator Intelligence for AI Agents](/docs/hermes/mcp/servers/external/viral-manager-mcp)
