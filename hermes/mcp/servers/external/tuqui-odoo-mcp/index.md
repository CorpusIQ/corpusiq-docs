---
title: Tuqui MCP - Odoo in Chat, Read-Only by Default
description: "Remote MCP for Odoo 16 to 20 in Claude and ChatGPT with nothing installed in Odoo, read-only by default and scoped to the user's own access."
category: ERP and Finance Operations
stars: n/a (new listing)
added: 2026-10-30
source: "mcp.so detail card filed 2026-10-21 under the slug tuqui-odoo-mcp-for-claude-chatgpt, returning repository github.com/Tuqui-AI/tuqui-mcp (HTTP 200) and docs.tuqui.com (HTTP 200), LGPL-3.0, plus a keyless JSON-RPC probe on https://tuqui.com/mcp answering HTTP 401 unauthorized, and the vendor connection guide carried on the same card"
relevance: ★★★
tags: [odoo, erp, accounting, inventory, sales, read-only, oauth, remote-mcp, claude, chatgpt]
last_updated: "2026-10-30"
---

# Tuqui MCP

**Every Odoo question is a developer ticket in most companies, because the answer sits behind a Python model someone has to write. This server turns the question into a sentence and nothing else.**

Tuqui publishes a remote MCP endpoint at `https://tuqui.com/mcp` over Streamable HTTP. A keyless `tools/list` answers **HTTP 401** with `{"error":"unauthorized"}`, which is the expected state for a connector that authenticates against a Tuqui account rather than an API key copied out of a settings screen.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://tuqui.com/mcp
Auth:        Tuqui account, OAuth on first connect
Odoo:        16, 17, 18, 19, 20 - Community and Enterprise
Hosting:     Odoo Online, Odoo.sh, self-hosted
Access:      read-only by default, scoped to the Odoo user
Licence:     LGPL-3.0 (client at github.com/Tuqui-AI/tuqui-mcp)
Docs:        https://docs.tuqui.com
```

## What it does

The pitch is the absence of a build. Nothing is installed inside Odoo, no module is deployed, and the vendor states there is no development work on the customer side. You create a Tuqui account, connect an Odoo user, and add one URL to the assistant.

That one URL is the whole configuration:

```json
{
  "mcpServers": {
    "tuqui": {
      "url": "https://tuqui.com/mcp"
    }
  }
}
```

## The permission model

Two sentences in the vendor material do the work that a security review would otherwise ask for.

First, **access is read-only by default**. Second, and more specific, **the connector sees only what your Odoo user can see**. That is not a marketing phrase, it is the design decision that makes this deployable at all: Odoo already carries per-user record rules for multi-company and per-warehouse access, so binding the connector to an Odoo user reuses the permission model the business already maintains instead of inventing a parallel one. A sales rep's assistant and a finance director's assistant answer different questions from the same server, because the unread rows are filtered upstream in Odoo rather than by the connector.

An agent that quotes this server as "we have Odoo data access" without naming the user it is bound to has missed the only scope boundary that matters. The same instinct is present in the local Odoo server this catalogue already carries; what differs is who holds the credential.

## What the questions look like

The vendor's own examples are operator questions rather than SQL:

```
How much did we sell this month compared to the same month last year?
Which customers have invoices more than 30 days overdue?
Which products are below their minimum stock?
Give me this week's collections by salesperson.
```

Each of those is a join across Odoo modules that would otherwise be a custom report or an Excel export: sales against prior period, receivables against aging, stock against reorder points, and payments grouped by the commercial owner.

The vendor describes the layer above the raw tables as skills for sales, stock and collections, carrying both company context and per-user context. That framing matters for answer quality. A raw table dump hands the model a `product_template` id and lets it guess; a skill tells it that this company measures stock in pallets and that a collection is recognised on payment date rather than invoice date. The claim to verify in your own instance is whether the answers come back with the company's conventions already applied.

## Why it belongs in this catalogue

The catalogue already carries an Odoo server, and the honest comparison is not "one has setup and one does not", because both claim little or no Odoo-side configuration. The real split is three lines.

**Where the credential lives.** The catalogued local server runs on your machine as an `npx` process and takes `ODOO_URL`, `ODOO_DB`, `ODOO_USERNAME` and `ODOO_PASSWORD`, so the database password sits in your shell or your client config. Tuqui holds the Odoo session on its side and the customer holds a Tuqui account consent screen. That is the whole difference a security review turns on.

**What the model sees.** The local server is generic by design: query any Odoo model, filter by domain, read the fields the user can read. Tuqui puts a skills layer for sales, stock and collections in front of the ORM, carrying company and per-user conventions. A generic surface is more capable and asks more of the model; a curated one is narrower and likelier to answer the question the way the business means it.

**Versions and hosting.** Tuqui publishes a 16 to 20 window across Community, Enterprise, Odoo Online, Odoo.sh and self-hosted, which is a wider support claim than most Odoo integrations make and worth probing against an older instance before promising it to a client on 16.

## What this pass did not establish

`tools/list` needs a credential, so the tool names are not in this entry. The count, the schemas and the write behaviour are the vendor's published position, not a list this pass drove. Three things a buyer should confirm in a trial: whether any write path exists behind a flag, how a multi-company Odoo user resolves when the same person has access to two companies, and whether the collection figures follow payment date or invoice date for their own accounting convention.

## FAQ

### Does it need anything installed in Odoo?
No. The vendor states nothing is installed in Odoo and no development is required, on Odoo Online, Odoo.sh or a self-hosted instance.

### Which Odoo versions are covered?
16, 17, 18, 19 and 20, Community and Enterprise.

### Is it read-only?
Read-only by default, and limited to the records the connected Odoo user can already see. The trial should confirm whether any write path can be enabled.

### Does it work with ChatGPT as well as Claude?
Yes. The vendor names Claude, ChatGPT and Tuqui's own chat, with the same account across all three.

## See Also

- [Odoo MCP - Zero-Setup ERP Connector for AI Agents](/hermes/mcp/servers/external/odoo-mcp) - the local `npx` Odoo server, generic ORM access with the credentials on your own machine
- [Mighty Accounting MCP - UK Company Books in Chat](/hermes/mcp/servers/external/mighty-accounting-mcp/) - accounting reads without an ERP deployment
- [Stratum Shifts MCP - Next Week's Rota in Chat](/hermes/mcp/servers/external/stratum-shifts-mcp/) - the same operator-question instinct on scheduling
