---
title: "Foliyo MCP - Branded Client Reports and Proposals for Agents"
description: "Hosted MCP server that lets an agent create, brand, publish and track client-ready reports, proposals and research pages. Reusable client brands, stable share links, PIN and email gates, and access controls; pages are responsive static HTML that can be updated from another authorized client without changing the link. OAuth sign-in per client at foliyo.io/mcp."
category: Productivity
stars: n/a (new listing)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + vendor docs at foliyo.io"
relevance: ★★
tags: [reports, proposals, client-portals, publishing, agencies, html, oauth, hosting, share-links, remote-mcp]
---

# Foliyo MCP

**Client-ready documents, published from the conversation.** Foliyo is a hosted MCP server that creates, brands, publishes and tracks client-facing reports, proposals and research pages. Your agent loads a saved project, sender, brand guide, audience and sharing policy, composes responsive static HTML, includes the assets, checks the document, and publishes it to a lasting link - PIN-gated where the policy asks for it.

```
Server type: Remote (Streamable HTTP; stdio bridge for stdio-only clients)
Auth: OAuth 2.1 (browser sign-in per client); scopes mcp and workspace:write
Endpoint: https://foliyo.io/mcp (401-verified live, Sep 14 2026)
CLI: foliyo.mjs (Node 20+) for shell-driven publishing
Pricing: Foliyo account required; plan details at foliyo.io
Category: Productivity / Agencies
```

## Why This Matters for Operators

The last mile of every client deliverable is still manual: copy numbers into a template, export a PDF, email it, and lose track of which version the client saw. Foliyo moves that into the agent workflow. The context step loads the right client brand and sharing policy before composing; the publish step returns a live URL with a PIN where applicable; and the page can be retrieved and updated from another authorized client while keeping the same link.

Sharing policy is explicit rather than assumed. Your saved policy wins; without one, the agent can use a generated PIN and tell you, or ask one essential question. An email gate records a claimed address rather than proving identity, and publishing never implies permission to send announcement or update emails.

## Tools & Capabilities

- **prepare_foliyo** - load the matching project, sender, guide, audience and sharing policy.
- **brand_guide** - apply the reusable client brand to the document.
- **publish** - publish a document, with options such as title and gate (`{"title":"Client update","gate":"pin"}`).
- **get_page** - retrieve and update a published page from another authorized client; the link stays the same.
- **CLI tooling** - `foliyo.mjs login`, `tools`, `publish`, `doctor` for shell-driven workflows.
- **Scopes** - a restricted `mcp` grant keeps existing limits; approving `mcp workspace:write` extends edits to pages created in other clients.

Pages are responsive static HTML: CSS, raster images and fonts can be inlined as base64 assets. Script-driven charts and application screens need a static version first; Foliyo does not run arbitrary applications or backend services.

## Installation

**Claude Code:**

```bash
claude mcp add --transport http --scope user foliyo https://foliyo.io/mcp
claude mcp login foliyo
```

**Cursor** - add to `.cursor/mcp.json` or `~/.cursor/mcp.json`, then sign in:

```json
{
  "mcpServers": {
    "foliyo": { "url": "https://foliyo.io/mcp" }
  }
}
```

**Codex:**

```bash
codex mcp add foliyo --url https://foliyo.io/mcp
codex mcp login foliyo --scopes 'mcp,workspace:write'
```

**Replit Agent** - Integrations, MCP Servers, add `https://foliyo.io/mcp`, then Test and save.

There is also a standalone CLI with no npm install needed:

```bash
curl -fsSL https://foliyo.io/cli.mjs -o foliyo.mjs
node foliyo.mjs login
node foliyo.mjs publish ./report/index.html --options publish-options.json
```

And the vendor publishes an agent skill (`foliyo.io/skill.md`) that teaches the workflow; the MCP connection supplies the account tools.

## Business Relevance

- **Agencies and consultancies** publish branded client updates that stay current at a stable link.
- **Freelancers and fractional operators** produce proposal-grade documents without a design tool in the loop.
- **Sales teams** turn research into a shareable proposal page with appropriate access controls.
- **Operators** keep a durable record of what was shared with whom, gated according to an explicit policy.

## Integration with CorpusIQ

Foliyo publishes the narrative; CorpusIQ supplies the numbers with sources. Connect CorpusIQ and the same assistant can read revenue, pipeline, ad and product data (Stripe, HubSpot, GA4, Shopify, QuickBooks and more) with source-cited answers, then hand the verified figures to Foliyo to be formatted and published as a client-ready page. The report a client receives is built from data the client's own systems produced, published through a workflow that records where every number came from.

## Limitations

- **Account required** with plan-level limits; pricing is not enumerated on the MCP listing.
- **Static documents only**: no script-driven charts or backend services; interactive applications must be reduced to static form first.
- **OAuth needs a browser** per client; stdio-only setups go through a third-party bridge (mcp-remote).
- **The email gate verifies claimed addresses, not identity** - do not treat it as proof.
- **Setup documentation checked by the vendor on Sept 5, 2026**; UI flows in some clients may drift.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
