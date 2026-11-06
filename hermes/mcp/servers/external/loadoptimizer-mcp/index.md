---
title: "LoadOptimizer MCP - Load Planning in Claude and ChatGPT"
description: "Plan truck, container and pallet loads from a sentence in Claude or ChatGPT, against your own carriers and stacking rules, with a 3D view."
category: Logistics and Supply Chain
stars: n/a (hosted, 10-day full trial then EUR 39.99 to 399 a month; the connector needs a plan with API access)
added: 2026-11-05
source: "The mcp.so card loadoptimizer at 2026-11-05T20:54:26.172Z (Other, verified and featured, OAuth, remote); HTTP reads on loadoptimizer.ai/mcp-server/ (200, the capability table, the per-assistant setup and the 3D view), loadoptimizer.ai/docs/ai-agents.html (200, what the approval covers, the shared quotas and the analytics record), loadoptimizer.ai/pricing (200, the five-tier ladder in euros, the yearly discount and the trial terms); the OAuth metadata at /.well-known/oauth-protected-resource/mcp (200, Supabase authorization server, scope email) and the Supabase authorization-server metadata (200, authorization_code plus refresh_token, dynamic client registration, S256 and plain); three registry searches for the vendor name returning zero records; and one keyless JSON-RPC initialize against the endpoint returning HTTP 401"
relevance: ★★
tags: [logistics, supply-chain, load-planning, container-loading, palletizing, 3d, stacking-rules, oauth, remote-mcp, manufacturing, 3pl]
last_updated: "2026-11-05"
---

# LoadOptimizer MCP

**A load plan is arithmetic with geometry on top, which is exactly the kind of question an assistant should be able to answer and almost never can.** LoadOptimizer puts a 3D loading engine behind an MCP endpoint so a planner can say "plan 36 Euro pallets on a standard 13.6 m trailer, what does not fit" and get a plan per carrier rather than a rule of thumb in cubic metres. The assistant works in the customer's own account, against their own carriers, products and stacking rules, and the result appears in the conversation as a 3D view that can be turned, zoomed and clicked.

```
Server type: Remote, Streamable HTTP
Endpoint:    https://mcp.loadoptimizer.ai/mcp
Auth:        OAuth through the vendor web app, account chooser and consent, then a
             full-access or read-only grant; authorization server is Supabase,
             scopes email (resource metadata advertises e-mail only)
Registry:    no official MCP registry record found on three searches
Tools:       not published by name; five capability groups documented by the vendor
Pricing:     Free tier, then EUR 39.99, EUR 99.99 and EUR 399 a month; the connector
             needs a plan that includes API access, which starts at Pro
Trial:       10 days of full Pro access including the API, no credit card
Vendor:      LoadOptimizer, loadoptimizer.ai (prices in euros, VAT excluded)
```

**Evidence tier.** A keyless `initialize` against `https://mcp.loadoptimizer.ai/mcp` returned **HTTP 401** with an empty body and a `WWW-Authenticate` header carrying `Bearer resource_metadata="https://mcp.loadoptimizer.ai/.well-known/oauth-protected-resource/mcp", scope="email"`. The protected-resource document answers **200** and names a Supabase project as the authorization server. That authorization server's metadata answers **200** with `authorization_code` and `refresh_token` grants, a dynamic client registration endpoint, and `code_challenge_methods_supported: ["S256","plain"]`. So the endpoint is live and gated, and no tool was called. What was measured: the 401 shape, both metadata documents, the vendor's capability table, its approval model, its quota statement and its published price ladder. Tool names are not published, so this entry documents capability groups rather than a `tools/list` result.

**It is not in the official MCP registry.** Three searches of the registry API, for `loadoptimizer`, `load optimizer` and `load planning`, each returned zero records. That is not a defect, but it means there is no registry-verified metadata to cross-check the vendor's own claims against, and it is the reason this entry leans on the vendor's documentation pages and marks them as such.

## What the assistant can do, by area

| Area | Capability |
| --- | --- |
| Load plans | check a request, plan a load, follow it until it is done, show the result per carrier and what did not fit, find earlier plans, rename and cancel them |
| Libraries | find your carriers and products, use them in a plan, and add, change or delete library entries |
| Stacking rules | see your cargo classes and rule sets, use them in a plan, and add, change or delete them |
| Saved loads | list saved loads, save a plan, and stop keeping one |
| Sharing | create or stop a link to the 3D view, only when public share links were approved at consent |

Three of those are worth pausing on. **The result is per carrier, not per question**: the same cargo gets planned again against other vehicles, which is how a planner learns that 1,500 boxes need one 40-foot high cube and a 20-foot for the rest. **Stacking is opt-in**: nothing is stacked unless the request says it may be, so the default answer is conservative rather than optimistic. **The 3D view and the stacking matrix are rendered inside the conversation** in Claude and ChatGPT, which makes this one of the few integrations here where the chat output is not a text summary of a plan but the plan itself.

One documented gap: loading-instruction PDFs are not available through an assistant yet. For those, open the order in the web app.

## What the approval actually covers

The consent screen is more specific than most, and the four items are the ones an operations lead should read:

- **The account.** The assistant works in the account chosen at approval and never in another one.
- **Full access or read-only.** Read-only can look up and see stacking rules; full access can also plan, change and save, including rule sets. Neither exceeds what the human approving it may do: a team member's assistant can plan with the rules, but only an owner's assistant can change them.
- **Public share links.** Off unless ticked, because a share link opens the 3D view to anyone holding it.
- **Which app is asking.** Only the named assistants are accepted, and any other client is refused.

That last point is unusual and worth crediting: the vendor restricts which MCP clients may complete the flow rather than accepting any client that can speak OAuth.

## Why this earns an entry

The logistics corner of this catalog is about finding and tracking, not about loading. [Fitralo MCP](/hermes/mcp/servers/external/fitralo-mcp/) finds European road freight carriers by lane, equipment and certificate. [HaulierScope MCP](/hermes/mcp/servers/external/haulierscope-mcp/) reads GB operator licence data from DVSA open data. [Container Tracking](/hermes/mcp/servers/external/container-tracking-mcp) follows shipments. [PackIndex MCP](/hermes/mcp/servers/external/packindex-mcp/) prices packaging materials and finished packs. None of them answers the question that decides the cost of the shipment: what fits, in what arrangement, and what is left over.

There is no load-planning or bin-packing entrant in the catalog, and a search across the guide tree for container loading, 3D load and load optimization returns nothing. An operator asking an assistant how many pallets fit a trailer today gets a volumetric estimate and a caveat. This is the first entry that answers with an engine, and it does it against the carrier and product libraries the customer already maintains rather than a generic table of trailer sizes.

## What it costs, read from the pricing page

Prices are published in euros and exclude VAT. The yearly option is 15 percent below the monthly rate.

| Plan | Monthly | API and connector | What else it adds |
| --- | --- | --- | --- |
| Free | EUR 0 | no | 15 AI optimizations a month, manual edit mode, Excel and CSV import, partial PDF and Excel export |
| Standard | EUR 39.99 (EUR 407.90 a year) | no | unlimited AI optimizations, full exports, shareable 3D links, axle weight and centre of gravity, cylindrical and tapered cargo, multi-vehicle optimization |
| Pro | EUR 99.99 (EUR 1,019.90 a year) | **yes** | REST API access with keys, so planning can be automated from an ERP, TMS or WMS |
| Business | EUR 399 (EUR 4,069.80 a year) | yes | three team accounts at EUR 29.99 each extra, 1,500 loads a month for the team including API, up to 25 carriers, 1,000 saved plans, group onboarding |
| Enterprise | custom, yearly | yes | on-premise or private cloud, custom integrations, SLA |

**The connector is not on the free or Standard plan.** The vendor's own wording is that it works "on plans that include API access", and API access is listed from Pro upward. So the honest cost of the MCP route is **EUR 99.99 a month**, not the free tier, and the 10-day full Pro trial is the only way to test it without paying. The trial needs no card and the account drops to Free afterwards rather than billing.

## Limits, and the claims this pass could not verify

- **Same quota as an API key.** The assistant runs under the plan's limits and the same request rate per account, shared with any API keys in use. A team running automated planning and chatting at the same time draws from one bucket.
- **Actions are attributed to you, through an agent.** The vendor records what the assistant does as the approving user, tagged `via: agent`, so the audit trail says both who and by what. Worth knowing before handing a team member's assistant write access.
- **Analytics are collected on tool use.** The vendor states it records which tools were used, whether they succeeded, the name of the model the assistant runs on, and a short description the assistant writes of each action's goal, with e-mail addresses, phone numbers and long numbers stripped before storage. It says requests and results themselves are not included. That is a reasonable design, and it is still a record of what your planning was about.
- **The OAuth metadata advertises `plain` alongside `S256`.** A client that accepts `plain` gives up part of the protection PKCE exists to provide. Insist on `S256` where the client allows it.
- **No registry record and no directory listing yet.** The vendor says it is working on official Claude and ChatGPT listings, which is why the connector is added by pasting an address today. A buyer cannot verify the server against the official registry in the meantime.
- **ChatGPT needs one setting changed.** In the connector's authentication settings, OpenID Connect must be turned off, because the vendor does not support it; left on, the approval page reports that the app asked for access the vendor does not support. This is the single most likely cause of a failed first connection.
- **The engine is a planning tool, not a data source.** Nothing here reads an order book, an ERP or a warehouse. It plans what you describe, which is useful and is not the same as reconciling what shipped.

## Common questions

### Can I try it without paying?

Yes, for ten days and with full Pro features including the API and the connector, with no credit card. After that the account falls back to the free plan with 15 optimizations a month and no API access, so the connector stops working until a Pro or Business plan is chosen.

### Does the assistant see my carrier rates?

It sees the carriers and products in your libraries, which is what lets it plan per carrier. Nothing in the vendor's documentation shows a freight rate or cost model being passed through the connector, and the pricing pages describe cost and mixed-fleet optimization as in development, so treat the plan as geometry and axle compliance rather than as a landed-cost answer.

### What happens to stacking rules an assistant creates?

They are saved to the account as rule sets, and saving needs an owner's connection. A team member's assistant can plan against existing rules but cannot create or change them. That is the right way round, and it is the reason to connect with an owner account only when rule maintenance is the job.

### Can someone else see a plan?

Only if a share link is created, and those are off at consent unless the person approving ticks the box. The link opens the 3D view to anyone who holds it.

## How to start

1. Add `https://mcp.loadoptimizer.ai/mcp` as a custom connector in Claude or ChatGPT. In ChatGPT, turn OpenID Connect off in the connector's authentication settings before approving, or the flow fails.
2. Sign in on the approval screen, pick the account, and choose read-only unless the assistant is meant to plan and save.
3. Ask one real question from your own week before touching the libraries: a trailer, a stop order, a set of pallet sizes. Read what did not fit before reading what did.
4. Say explicitly whether cargo may be stacked. The default is no, and a plan that assumes nothing stacks will under-fill the trailer.
5. Keep rule maintenance on an owner connection and everything else on a team member's, so a planning conversation cannot quietly rewrite the rules everyone else plans against.
