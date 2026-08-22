---
title: "ship.page MCP - Deploy HTML Pages from Any Agent"
description: "Zero-config remote MCP server that turns HTML into a live, unguessable URL in one call: deploy single pages, multi-file sites and CI reports, claim drops to an account, list and delete. Free anonymous tier, Pro at $4 per month."
category: Content & Publishing
stars: n/a (new listing)
added: 2026-08-22
source: mcp.so
relevance: ★★
tags: [html, hosting, deployment, preview, ci-reports, static-sites, remote-mcp]
---

# ship.page MCP

**A zero-config remote MCP server that turns raw HTML into a live, unguessable URL in one call.** ship.page (`ship.page/mcp`) is built for agents that need to put content on the public internet right now: deploy a single page, a multi-file site or a CI report, then hand the human a link. Anonymous deploys work with no signup and no OAuth dance; an optional `sp_` key upgrades to 30-day drops, listing, deletion and named drops. The endpoint is live and served all 7 tools to an anonymous probe. Built by the same team behind lucid.page.

```
Server type: Remote (Streamable HTTP)
Auth: None for anonymous deploys; Bearer sp_ key for account features
Endpoint: https://ship.page/mcp
Tools: 7 (deploy_html, deploy_files, list_drops, claim_drop, delete_drop, get_limits, get_account)
Pricing: Free anonymous tier (7-day drops); Pro $4/mo (30 days, named drops); Team $19/mo
Built by: Bitgate (Bart Pelle) - the lucid.page team
```

## Why This Matters for Operators

Sharing work product from an agent usually means copy-pasting output into an email or a doc. **ship.page removes that step: the agent deploys the artifact and returns a link.** Preview deploys for mockups and dashboards, CI reports (Playwright runs, coverage HTML, build output), one-off pages - every deploy lands on an unguessable `*.shipped.page` subdomain mounted at root, so absolute paths just work.

The claim-token flow is the smart part for teams. Anonymous drops get a one-time `spc_` token; claiming attaches the drop to your account, extends its life to 30 days, and makes it listable and deletable. A throwaway preview can become a shareable asset without redeploying anything.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `deploy_html` | Deploy one HTML document to a live unguessable URL (7-day anonymous expiry) |
| `deploy_files` | Deploy a multi-file site map (index.html required; up to 100 files anonymous) |
| `list_drops` | List account-owned drops with slug, URL, name, file counts and expiry |
| `claim_drop` | Attach an anonymous drop to an account via its one-time claim token |
| `delete_drop` | Permanently delete an owned drop - the URL stops serving immediately |
| `get_limits` | The plan matrix (anonymous vs Pro vs Team) and current account status |
| `get_account` | Plan, subscription status and usage for the authenticated account |

A full OpenAPI 3.1 spec is published at ship.page/openapi.json; agent docs at ship.page/docs/agents.

## Installation

```bash
claude mcp add ship-page --transport http https://ship.page/mcp
```

Works with Claude Code, Codex, Cursor and VS Code out of the box.

## Configuration

```json
{
  "mcpServers": {
    "ship.page": {
      "type": "http",
      "url": "https://ship.page/mcp"
    }
  }
}
```

No key needed for anonymous deploys (10 per minute per IP, 10 MB body cap, 7-day expiry). Add `Authorization: Bearer sp_...` for account features.

## Business Relevance

- **Analytics leads** ship dashboard mockups and report previews as links instead of screenshots.
- **Engineering managers** publish CI artifacts (test reports, coverage HTML) straight from the pipeline via the GitHub Action or plain curl.
- **Agencies** send client previews as unguessable links that clients can claim or let expire.
- **Anyone running an agent** gets an audit trail via list_drops for everything the agent has deployed.

## Integration with CorpusIQ

ship.page is the output layer for CorpusIQ's analysis workflow. An agent that answers a question with CorpusIQ connectors - GA4 traffic, QuickBooks P&L, Shopify orders - can render the answer as an HTML recap and call `deploy_html`, returning a link instead of a wall of text. CorpusIQ's own visual-answer rendering and report generation pair naturally with ship.page as the publishing endpoint for anything that should leave the chat.

The claim flow makes it collaborative: the agent deploys anonymously, hands the operator the link and the claim token, and the operator's account takes ownership for the full 30-day window - no redeploys, no key sharing with the agent.

## Limitations

- New listing: no independent track record as an MCP server yet.
- Anonymous drops expire in 7 days (30 days claimed or Pro).
- Hosted service - pages live on shipped.page infrastructure, not yours.
- Named drops and higher file counts are Pro features ($4/mo).
- Unguessable URLs are private, not secure: treat drops like shared links, not a vault.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
