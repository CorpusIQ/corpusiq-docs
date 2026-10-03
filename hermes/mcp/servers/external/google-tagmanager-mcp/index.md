---
title: "Google Tagmanager MCP - GTM Containers for Agents"
description: "OAuth MCP over Google Tag Manager API v2: inspect tags, triggers and variables, edit a draft workspace, then publish a version."
category: "Marketing"
stars: n/a (open source, github.com/A1-x-Tech/mcp-google-tagmanager)
added: 2026-10-02
source: "mcpservers.org server page (a1-x-tech/mcp-google-tagmanager)"
relevance: ★★★
tags: [gtm, tag-manager, analytics, tracking, marketing-ops, google, stdio]
---

# Google Tagmanager MCP

**Local and hosted MCP server (stdio via npx, OAuth)** - A1 Google Tag Manager MCP lets an agent inspect and manage Google Tag Manager containers in plain language, working with the real container, workspace and version rather than guessing a setup.

```
Server type: Local (npx) with an OAuth connect flow
Auth: Google OAuth (PKCE, caught on 127.0.0.1)
Endpoint: npx mcp-google-tagmanager
Tools: 25 (10 read, 4 draft-creating, 5 altering/compiling/publishing, plus supporting operations)
Pricing: Free, MIT licensed
Category: Marketing
Built by: A1-x-Tech (github.com/A1-x-Tech/mcp-google-tagmanager)
```

## Why This Matters for Operators

Tag Manager changes are high-stakes and easy to break: one wrong trigger and analytics stop, one wrong tag and the site slows. This server makes the change loop explicit. Read operations inspect what actually fires, edits land in a draft workspace, and publishing is a separate, deliberately destructive step the operator chooses.

**Draft-first is the operator safeguard.** Tags, triggers and variables are created in a workspace, so an agent can propose a change and a human reviews it before anything goes live, and the server spaces requests at least 4.2 seconds apart to respect GTM's 0.25-requests-per-second project quota.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Read operations (10) | Inspect containers, tags, triggers, variables and what fires on a page |
| Draft operations (4) | Create drafts and change built-in variables in a workspace |
| Destructive operations (5) | Alter, delete, compile or publish live configuration |
| Connect | Walk through the OAuth client and catch the redirect on 127.0.0.1 with PKCE |

25 tools total: 10 operate read-only, 4 create drafts or change built-ins, and 5 can alter, delete, compile or publish.

## Installation

Connect from the conversation by saying "connect Google Tag Manager"; the server walks through the OAuth client, catches Google's redirect on `127.0.0.1` with PKCE and keeps the tokens itself, with no config files and no restart. It also ships on npm as `mcp-google-tagmanager` for stdio clients.

## Configuration

```json
{
  "mcpServers": {
    "google-tagmanager": {
      "command": "npx",
      "args": ["-y", "mcp-google-tagmanager"]
    }
  }
}
```

The server requests only the Tag Manager scopes needed for reading, editing, versioning and publishing, and it uses the operator's own OAuth credentials.

## Business Relevance

- **Marketing ops teams** audit which tags fire on a page-view trigger without reading the GTM UI by hand.
- **Analytics engineers** propose tag and variable changes as drafts, then publish deliberately.
- **Growth teams** verify that a tracking change landed before trusting the data downstream.
- **Agencies** run the same read-then-draft loop across client containers.
- **Any operator** who has ever broken analytics with an untested tag edit.

## Integration with CorpusIQ

Google Tag Manager is upstream of the measurement chain CorpusIQ's GA4 connector reads. An agent can use this server to check that a conversion tag actually fires for a CorpusIQ-tracked funnel, and pair that with the GA4 connector so the tag change and the resulting data movement are verified in one workflow. The Tag Manager server maintains the measurement plumbing; CorpusIQ reads the business numbers that plumbing produces, so a funnel question can be traced from tag to revenue without leaving the agent.

## Limitations

- Brand new, no track record yet.
- Requires Google OAuth with access to the target GTM account.
- Publishing is destructive and should stay behind human review in any autonomous flow.
- The API quota is 0.25 requests per second per project, so the server deliberately paces calls.
- Scope is Google Tag Manager only, not Google Analytics or other Google products.

## FAQ

### Does the server need Google credentials configured in advance?

No config files are required. Say "connect Google Tag Manager" and it walks through the OAuth client, catching the redirect on `127.0.0.1` with PKCE and storing the tokens itself.

### Can an agent publish changes without review?

Technically yes, but publishing is a separate destructive operation and edits land in a draft workspace first, so the intended flow is draft, review, then publish.

### Why does it space out requests?

Google Tag Manager allows 0.25 requests per second per project, so the server waits at least 4.2 seconds between calls to avoid overwhelming the API.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
