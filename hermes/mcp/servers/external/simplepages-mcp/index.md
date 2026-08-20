---
title: "Simplepages MCP - Landing Pages Built and Measured from Chat"
description: "Simplepages workspace connector for MCP clients: build and edit landing pages from plain-language prompts, list pages and sites with status, and pull visitors, leads and revenue per page or workspace"
category: Marketing
stars: n/a (new listing)
added: 2026-08-20
source: mcpservers.org
relevance: ★★
tags: [landing-pages, page-builder, conversion-tracking, marketing-websites, no-code, oauth, workspace-scoped, remote-mcp]
---

# Simplepages MCP

**Remote MCP server (Streamable HTTP, OAuth-style connect flow) — the Simplepages landing-page workspace as agent tools.** Point an MCP client at Simplepages and it works with pages the way you already work with the assistant: describe a page and it builds one, tell it to change a headline and it edits in place, ask how a page is doing and it returns visitors, leads, and revenue. Connection is per-workspace and user-approved, with the assistant's chats never seen by the vendor.

```
Server type: Hosted remote (Streamable HTTP)
Auth: OAuth connect flow (per-workspace approval; optional token)
Endpoint: provisioned in-app (Simplepages Settings → MCP access)
Tools: workspace, page, and performance operations (see below)
Pricing: Simplepages account required; free to connect
Category: Marketing / Landing Pages
Built by: Simplepages (simplepages.ai)
```

## Why This Matters for Operators

Landing pages are the step between ad spend and revenue, and the usual loop — ask a freelancer for a page, wait, request edits, wait, then export analytics to judge it — takes days per iteration. Simplepages MCP compresses it to a conversation. "Build a coffee-subscription landing page" produces a page in the workspace ready for the editor; "make the headline say Book now" edits it in place and saves the draft. The operator keeps the final publish action, which is the right human gate: the assistant builds, edits, and reads back; you take the page live.

The measurement side is what makes it a growth tool rather than a page generator. The agent can ask how a single page is doing — visitors, leads, revenue — or pull the whole workspace at a glance, so the question "is the new pricing page converting?" is answered from the same surface that edits the page. Publishing-from-chat is on the vendor's roadmap, which would close the loop fully.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Describe-to-build | Create a landing page from a plain-language description in your workspace |
| Chat edits | Change copy, headlines, and layout from conversation; saved to draft |
| Workspace readout | List pages and sites with status and links |
| Performance pull | Visitors, leads, and revenue per page, or whole-workspace view |

Tool names are served from the provisioned endpoint; the capability surface above is the vendor-published description. Clients that speak MCP (Claude, ChatGPT, Gemini, and others) connect the same way.

## Installation

Connection is created from the app, not assembled from a URL: open Simplepages, go to Settings → MCP access, grab the URL, add it as a custom connector in your MCP client, sign in with your existing Simplepages account, and pick which workspace the assistant may touch.

```bash
# Once the URL is provisioned in-app:
claude mcp add simplepages --transport http <provisioned-endpoint-url>
```

If your client asks for a token instead of a Connect button, generate one on the same settings page. Access is revocable any time from Settings.

## Configuration

```json
{
  "mcpServers": {
    "simplepages": {
      "type": "http",
      "url": "<endpoint-url-from-settings>"
    }
  }
}
```

Auth notes: approval happens through your existing Simplepages login; the connection is scoped to the one workspace you pick; nothing runs until you allow it; the vendor states it never sees your assistant's chats.

## Business Relevance

- **Growth marketers** go from brief to live-ready landing page in one session, then read conversion results from the same tool
- **Agencies** build and revise client pages from chat while the client keeps the publish control
- **Founders** get a no-code page pipeline that works inside the assistant they already use
- **CRO teams** pull per-page visitors, leads, and revenue to prioritize which page to fix next

## Integration with CorpusIQ

Simplepages MCP fits the attribution loop that CorpusIQ already reads: the CorpusIQ Meta Ads and Google Ads connectors show which campaigns drive clicks, the CorpusIQ GA4 connector shows what happens after the click, and Simplepages MCP supplies the page layer in between — build the variant in chat, then judge it against ad-driven traffic and conversion data from CorpusIQ. For ecommerce operators, the CorpusIQ Shopify connector shows order value while Simplepages reports page-level leads and revenue, so the agent can tie a landing-page experiment to store outcomes. The direction of flow: Simplepages MCP builds and measures the page; CorpusIQ reads the ads and commerce systems around it.

## Limitations

- Publishing from chat is not shipped yet — the assistant builds, edits, and reads back; the human publishes
- Endpoint URL is provisioned per account in-app, not published publicly
- Commercial tool — requires a Simplepages account; page depth and pricing per vendor
- Brand new MCP surface — the connection flow is documented, the tool list is served live
- Workspace scoping means the agent sees only what you point it at

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
