---
title: "Neleto CMS MCP - Site Editing from Any MCP Client"
description: "Edit pages, posts, events and files on a Neleto CMS site from any MCP client, through OAuth 2.1 or an API token."
category: Business Operations
stars: 0
added: 2026-09-29
source: mcpservers.org
relevance: ★★
tags: [cms, website-management, content, pages, blog, oauth, eu-hosting, remote-mcp]
---

# Neleto CMS MCP

**Every Neleto site ships with a native MCP server.** Neleto is an all-in-one CMS with a page builder, built-in rendering and EU hosting - and each site exposes its own MCP endpoint at `/api/mcp`. Claude, Cursor, VS Code and other MCP clients can create and edit pages, write and publish posts, build components and upload files directly, with the same role permissions as the admin.

```
Server type: Remote (Streamable HTTP), per-site endpoint
Auth: OAuth 2.1 (Claude apps) or API token (coding agents)
Endpoint: https://<your-neleto-site>/api/mcp
Tools: 57 (pages, posts, events, components, layouts, files, settings, languages, meta)
Pricing: Included with Neleto hosting plans (EU-hosted)
Category: Business Operations
Built by: Triple-A Software (neleto.io, github.com/Triple-A-Software/neleto-mcp)
```

## Why This Matters for Operators

Website content is the most common maintenance task operators delegate to an assistant - and the most error-prone when the assistant only produces text that a human then copies into a CMS. Neleto closes that loop: the agent reads the live site, edits pages and layouts, publishes posts and events, and can open the published page to confirm it rendered.

Access follows the same roles as the admin - admin, developer, editor, author - so an agent never gets more rights than the account it connects with. OAuth connections are reviewable and revocable under Profile, Security, Connected applications.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Pages | Create, update and duplicate pages, including layout and elements |
| Posts and events | Write, schedule and publish blog posts and events |
| Components and layouts | Build reusable HTML templates, CSS and form fields |
| Files | Upload files, including from a URL inside a page payload |
| Site settings | Read and change settings, languages and meta tags |
| Publishing checks | Check templates before publishing and verify the live page after |

The full 57-tool reference is published at neleto.io/docs/developer/mcp (registry name `io.neleto/cms`); tool names are served from the per-site endpoint.

## Installation

```bash
claude mcp add --transport http neleto https://<your-neleto-site>/api/mcp \
  --header "Authorization: Bearer <your-token>"
```

For Claude.ai and Claude Desktop, add the endpoint as a custom connector and sign in with your Neleto account - OAuth discovery, PKCE and dynamic client registration are built in, so there is no token to copy.

## Configuration

```json
{
  "mcpServers": {
    "neleto": {
      "url": "https://<your-neleto-site>/api/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

Create API tokens in the Neleto admin under Settings, API Tokens. Each connection inherits the permissions of the user who approved it.

## Business Relevance

- **Site owners and operators** delegate content updates to an assistant that edits the live site instead of handing over markdown
- **Agencies** maintain client sites through role-scoped connections, with every connection revocable
- **Content teams** schedule posts and events and verify publishing in one session
- **EU-based businesses** get EU hosting with no data-residency trade-off for the MCP layer

## Integration with CorpusIQ

Neleto covers the site while CorpusIQ covers the business-data layer. A composed workflow: CorpusIQ pulls performance context through its connectors - GA4 traffic, Stripe revenue, campaign data - and the assistant turns that into a concrete site change: a new landing page, an updated pricing block or a published announcement, executed through Neleto's MCP endpoint and verified live after publishing.

## Limitations

- Per-site endpoint; the MCP server is part of a Neleto instance, not a standalone service
- Requires a Neleto CMS site - no cross-platform CMS support
- Brand new repo (0 GitHub stars) documenting the server; the server itself ships with the product
- OAuth flow is Claude-first; other clients use API tokens

## FAQ

### Do I need to install a server?

No. The MCP server is part of every Neleto instance and runs at `/api/mcp` on your site. The GitHub repo documents the server and its 57 tools.

### How are permissions handled?

Access follows the same roles as the admin. An agent connected with an editor account can edit, but never gets more rights than that account has in the CMS.

### Where is data hosted?

Neleto is EU-hosted with built-in rendering, and the MCP endpoint runs on the same instance - no separate infrastructure to manage.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
