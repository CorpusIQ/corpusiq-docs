---
title: "AttriKit MCP - App Attribution That Returns a Decision"
description: "Stdio MCP over the AttriKit management API: 39 tools that join ad spend to iOS and Android installs and return a scale, cut or hold call."
category: Marketing / Attribution
stars: n/a (published npm package and MIT repo; no hosted endpoint to probe)
added: 2026-11-02
source: "chatmcp/mcpso submission #6592, the published npm package @attrkit/mcp 2.0.1 with its bin and repository metadata, the MIT repository at github.com/KamyarTaher/attrikit-mcp whose README carries the full 39-tool table, the MCP setup page at attrikit.io/en/docs/mcp and the pricing page at attrikit.io/en/pricing"
relevance: ★★★
tags: [attribution, mobile-apps, ad-spend, ios, android, revenuecat, meta-ads, tiktok-ads, marketing, stdio]
last_updated: "2026-11-02"
---

# AttriKit MCP

**Ad spend is the easiest number in a business to keep paying without asking what it bought. The question that saves money is not which link the install came from, it is whether this campaign earned the next month of budget.**

```
Server type: Stdio (local process, npx @attrkit/mcp)
Auth:        AttriKit management key, workspace or app scoped, read only or read write
Tools:       39 published, across apps, links, spend, decisions, integrations, exports
Runtime:     Node.js 22 or newer from 2.0.0
Pricing:     first 10,000 qualified installs free once, no card, then $249 a month
Retention:   25 months of attribution records
```

## What it does

AttriKit is web-to-app attribution for iOS and Android apps that buy ads. The MCP server is a thin client over the vendor's Management API: it holds no database access, and the tenant scope is resolved from the management key, so one key reaches one workspace or one app.

The 39 tools split by area rather than by screen.

| Area | Tools |
| --- | --- |
| Key and usage | `whoami`, `get_usage_cap`, `set_usage_cap` |
| Apps | `list_apps`, `create_app`, `get_app`, `update_app`, `archive_app` |
| SDK and management keys | `get_publishable_key`, `rotate_publishable_key`, `list_api_keys`, `create_api_key`, `revoke_api_key` |
| Campaign links | `list_links`, `create_campaign_link`, `update_link_status` |
| Reporting and decisions | `list_campaigns`, `list_ads`, `list_recent_events`, `list_event_deliveries`, `get_campaign_decision`, `record_campaign_decision`, `get_attribution_rollup`, `lookup_customer_attribution` |
| Spend and cost | `get_spend`, `import_spend`, `set_cost_model`, `pull_network_spend` |
| Ad integrations | `list_integrations`, `create_integration`, `update_integration`, `delete_integration` |
| RevenueCat | `get_revenuecat`, `configure_revenuecat` |
| Webhooks and export | `list_webhooks`, `create_webhook`, `delete_webhook`, `export_events`, `send_server_event` |

Two design decisions in that table are the reason this entry exists.

The first is that the decision is computed by the attribution engine, not by the model. `get_campaign_decision` returns the engine's call verbatim, and the vendor's own documentation states that the model reports it rather than recomputing it. `record_campaign_decision` then writes the operator's confirmation back with the inputs that produced it, so a scale, cut or hold call can be graded later against what actually happened. The vendor is explicit that the suggestion is not a profit guarantee and that later grading needs sufficient results before it means anything.

The second is that spend is a first-class input rather than something the model is asked to remember from an ad dashboard. `import_spend` takes ad level CSV rows, `pull_network_spend` reads a connected authorized ad account, and `set_cost_model` records how cost is allocated. `get_spend` returns it beside the install and event records, which is what makes cost per install, cost per purchase and payback answerable inside the same conversation.

Revenue joins the same way through RevenueCat: purchases, renewals and refunds are matched to installs when the webhook is configured and the same app user ID is used in both systems.

## Evidence tier, stated plainly

This entry is written from the published package and the vendor's documentation, not from a driven session.

There is no hosted endpoint to initialize against: the package is stdio only, it opens no network port, and it exits with an error naming the fix when no key is present. The first workspace key also has to be created in the dashboard, so a keyless probe is not possible by design.

What was verified:

- the package exists at `@attrkit/mcp` **2.0.1**, with bin `attrkit-mcp` and a repository field pointing at `github.com/KamyarTaher/attrikit-mcp`, last modified **2026-11-02T13:24:45Z**
- the README of that repository is MIT licensed and carries the 39-tool table reproduced above, area by area
- the MCP setup page publishes the same inventory, the same 39 count, the key resolution order and the client configs for Claude Code, Codex, Cursor and Gemini CLI
- the pricing page publishes the free allowance in its own headline

Unverified and recorded as such: no tool was called, so the shape of a decision payload, the confidence field, the evidence labels and the latency of `import_spend` against real data are the vendor's description. Treat the decision output as documented rather than measured until a workspace key is put behind it.

## The awkward parts worth knowing first

The first key is a dashboard bootstrap. After that a workspace key can manage every customer operation the Management API exposes, but billing, sign in, organization membership, workspace deletion and internal administration are outside the MCP surface, and an app-scoped key cannot create sibling apps or manage workspace-wide integrations.

Two delivery rules bite on Meta and TikTok. `delivery_scope` is `all` by default, which sends every install with measurement consent including organic ones, or `attributed`, which sends only installs the engine matched to that network. `renewal_event` defaults to `purchase` and can be switched to a custom `subscription_renewed` event carrying its value. A Google integration refuses both `attributed` and `custom`, and Google conversion delivery is gated on certification that is still pending, so a Google ads account reads but does not deliver yet.

Three operational limits are published rather than discovered later. Most tools time out at 15 seconds, while `export_events`, `import_spend` and `pull_network_spend` get 120 seconds; a timed out write should be retried with the same `idempotency_key` rather than a new one because the first attempt may have landed. `export_events` version 1 returns at most the 100,000 most recent events inside a range and silently cuts a busier range to that newest slice, so version 2 with its `next_cursor` paging is the correct call for a full export. Management keys carry per-key global, mutation and expensive operation limits, and a 429 carries `Retry-After` in seconds.

The web SDK is not published on npm yet, so click capture comes from campaign links while first opens come from the iOS and Android SDKs. A workspace also allows one member today, with team invitations not available, which matters to anyone planning to share the connection across a team.

## Where it sits in this catalogue

[Mobzio MCP](/hermes/mcp/servers/external/mobzio-mcp/) is the closest neighbour and answers a different question. It is marketplace deeplink attribution for Wildberries, Ozon, Yandex Market and Kaspi: it says which link produced an order, link by link, eight read tools and one write. It is link level by design and it stops at the order.

AttriKit starts where that ends. The record is an app install joined to ad spend and to subscription revenue, and the output is a budget call with the evidence and the inputs retained, which is the number an operator actually argues over: keep paying, cut, or hold and watch. A link shortener cannot produce that, and a model asked to eyeball two dashboards cannot produce it reproducibly.

The ad side of this catalogue is otherwise about the creative. [Abyssale MCP](/hermes/mcp/servers/external/abyssale-mcp/) generates the asset, [AdTest.AI MCP](/hermes/mcp/servers/external/adtest-mcp/) scores it before spend, [Ad Library Intelligence MCP](/hermes/mcp/servers/external/ad-library-intelligence-mcp/) and [Adspy MCP](/hermes/mcp/servers/external/adspy-mcp/) read what competitors run, and [AdMake AI MCP](/hermes/mcp/servers/external/admake-ai-mcp/) joins research to generation and publishing. None of them closes the loop to what the spend returned. That loop, install to revenue to decision, is the gap this entry fills.

It is also the first entry here where the model is explicitly restricted to reporting a computed verdict rather than producing one, which is the same trust boundary this catalogue argues for elsewhere.

## FAQ

### Do I need an attribution SDK in the app?

Yes, for installs. The iOS and Android SDKs capture first opens and are installable today. Campaign links capture web clicks on the way to the store without the web SDK, and the web SDK is not on npm yet.

### Can an agent change a campaign budget?

No. The write surface here is links, apps, integrations, spend records, decisions and webhooks. Recording a decision is not the same as executing one: the change still happens in the ad platform, and a read only key gets `403 forbidden_scope` on every mutation.

### How does the agent know a decision is safe to trust?

It does not compute it. `get_campaign_decision` returns the engine's call with its evidence, and `record_campaign_decision` stores the inputs used, so the call can be graded later once enough results exist. The vendor states plainly that a suggestion is not a profit guarantee.

### What does it cost?

The first 10,000 qualified installs are free once with no card. After that Starter is **$249** a month including 10,000 qualified installs, then **$0.015** each, which prices 50,000 installs at **$849** and 100,000 at **$1,599**. A monthly usage cap can be set no lower than 10,000; once it is exceeded, additional install charges stop while measurement continues and the monthly plan fee remains.

### Which clients can run it?

Any MCP client that can launch a stdio server: Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, VS Code and Windsurf all have published configs. Node.js 22 or newer is required from version 2.0.0; 1.x accepted Node 18.

### Where does the key live?

`npx -y @attrkit/mcp login` stores it in the macOS Keychain with echo off and checks it against AttriKit first, or `ATTRKIT_API_KEY` can be set in the environment of the process that starts the client. An unexpanded placeholder such as `${ATTRKIT_API_KEY}` counts as unset, and the check order is documented.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Mobzio MCP - Marketplace Deeplinks and Attributed Orders](/hermes/mcp/servers/external/mobzio-mcp/) - link level attribution for marketplace sellers, the question before this one
- [AdTest.AI MCP - Pre-Spend Ad Creative Scoring](/hermes/mcp/servers/external/adtest-mcp/) - the check before the spend rather than the account of it
- [Ad Library Intelligence MCP - Competitor Ads on Demand](/hermes/mcp/servers/external/ad-library-intelligence-mcp/) - what the other side is running while your budget is out
