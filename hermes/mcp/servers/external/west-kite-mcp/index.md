---
title: "West Kite MCP - Owner Tracing for Commercial Property"
description: "US commercial parcels, the people behind the LLCs, their phone and email, and a prospecting pipeline, behind one OAuth connection."
category: Real Estate & Property Data
stars: n/a (vendor-hosted; no public repository)
added: 2026-11-07
source: "mcpservers.org sitemap slug westkite-com-mcp plus the vendor's llms.txt, product.md, pricing.md, agent-quickstart.md and the MCP endpoint itself"
relevance: ★★★
tags: [commercial-real-estate, property-ownership, owner-tracing, skip-tracing, prospect-lists, off-market, contact-data, oauth, remote-mcp, us-data]
last_updated: "2026-11-07"
---

# West Kite MCP

**Every commercial building has an owner. Most of them are an LLC with a registered agent and no way to reach a human. The deal is not the building, it is the person behind it, and that person is findable.**

```
Server type: Remote (Streamable HTTP) at https://app.westkite.com/mcp
Auth: OAuth, browser sign-in, no API key
Live check: POST initialize without a token returned HTTP 401 {"error":"Connect your West Kite account.","code":"SIGN_IN_REQUIRED"} with www-authenticate naming https://app.westkite.com/.well-known/oauth-protected-resource/mcp and scope "wk:data:read wk:saved:read wk:research:read wk:conversations:read wk:documents:read wk:assets:read wk:saved:write wk:research:write wk:documents:write wk:actions:write"
Discovery: that protected-resource document returns 200 naming resource https://app.westkite.com/mcp, authorization server on the same host, bearer in header, 15 scopes including profile and email, and resource_documentation https://westkite.com/agent-quickstart.md
Tools: not published as a list; the scope table is the capability envelope (data, saved, research, conversations, documents, assets, actions, each read or write)
Coverage: 107 million US parcels across 1,787 counties in 27 states and Washington DC, stated by the vendor to include all of California, Florida and Nevada
Pricing: $149 per month, one plan; 7-day free trial with 150 tokens and no card; 1,500 tokens a month, extra tokens $0.10
Vendor: West Kite, Inc. (westkite.com, San Francisco)
```

## Why This Matters for Operators

A broker or an investor with a list of buildings still has to answer the same two questions before anything else happens: who actually owns this, and how do I reach them. Public records answer the first one in the worst possible form, a parcel number and an LLC. The second question is where the work usually dies, because tracing an LLC to a person with a phone number is a paid data problem and a manual research problem at the same time.

West Kite answers both over MCP, with the source attached to each fact, and it does it for commercial property rather than the whole residential parcel universe. The filters it exposes are the ones that decide a commercial deal: type, size, last sale date, value, owner, permits, zoning, flood risk. The off-market angles it advertises are the useful ones too, long-held buildings, underbuilt lots and recent permits, because those are the properties where the owner has a reason to talk before the listing exists.

The one thing it does that almost nothing else in this catalogue does is keep the outreach inside the same record. The owner gets added to a pipeline, the draft is written from the property record, and the call note lands back on the same deal. That is a workflow, not a dataset, and it is the difference between a research tool and something a two person brokerage actually runs on.

## What It Actually Does

The vendor documents the surface, not a tool table, so this section records what the vendor states and what the endpoint's own scope metadata proves. Tool names are not published and are not invented here.

| Capability the vendor states | What it answers |
| --- | --- |
| Property search | Screen US commercial parcels by place, property type, size, sale date, value and owner, and read the evidence behind each result |
| Ownership research | Trace an LLC to the people behind it, then retrieve a phone number and an email |
| Records | Zoning, permits, sales, assessments, tax history, flood risk, brokers and market trends on one record |
| Export | A full result set as one file with an exact total and its sources, for example five years of sales in one county |
| Pipeline | Deals, replies and call notes, with add-to-pipeline and save-property actions |
| Documents | Draft outreach and write documents from the record |
| Second Brain | The firm's own knowledge made available to the agent |

Two behaviours are worth naming because they are how the same capability goes wrong elsewhere. **Nothing is sent from the assistant.** The agent drafts, and the person sends outreach from West Kite, so an automated mail merge cannot leave the building on the agent's authority. **Every change goes through a review link** that the person approves inside West Kite, and those links expire after 15 minutes. The vendor also states a 60 requests per minute per account ceiling, which is low enough to matter when an agent is paginating a county.

The endpoints an agent needs are all published in machine readable form, which is unusual and worth crediting: `https://westkite.com/llms.txt` for the product summary, `https://westkite.com/agent-quickstart.md` for a setup procedure written to be executed by a coding agent, and `https://app.westkite.com/auth.md` for a plain HTTP sign-in path for an agent that cannot open a browser.

## Verified, and What Is Not

**Verified in this pass.** The MCP endpoint answers `401` without a token and names its protected-resource document in `WWW-Authenticate`, with a scope list separating read from write surfaces. That document returns `200` and confirms the resource, the authorization server, the bearer method, the full 15 scope vocabulary and the setup documentation URL. The trial terms, the token costs and the coverage figures are read from the vendor's own `pricing.md` and `llms.txt`, not from a directory card.

**Not verified here.** Tool names, tool count and response shapes are unread, because the surface is OAuth gated and no account was created for a probe. The coverage figures and the county count are the vendor's claims. Contact token consumption is documented but not measured. The professional services answer is honest about the limit: **state by state, data varies, and many states do not publish sale prices**, and the product says when a field is missing rather than filling it in, which is the right behaviour but also means a prospect list built in one state may be thinner in the next.

## Neighbours, and Why This Is Its Own Entry

The real estate shelf here already has an owner for management and an owner for parcel research. [Hercules Property](/hermes/mcp/servers/external/hercules-property-mcp/), Dutch Property Context, AskRent and LucidRents run the property management job. [DFX Intelligence](/hermes/mcp/servers/external/dfx-intelligence-mcp/) and [dfx-real-estate](/hermes/mcp/servers/external/dfx-real-estate-mcp/) cover US parcels and recorded sales, and Homedex UK covers HM Land Registry sold prices. BatchData, the closest neighbour on skip tracing, was held earlier as a real estate class entry rather than catalogued.

West Kite is the first entry here built around the commercial prospecting loop rather than the record itself: identify a commercial parcel, name the person behind the LLC, deliver a phone number and an email, then track the deal in the same workspace. The distinction is the same one that separates a credit bureau from a sales floor. Reading a record is research; knowing who to call and what happened last time is the job.

## Who Should Use It

A small commercial brokerage, a CRE investor, or a business that sells to property owners, in the states the vendor covers and where the county publishes sale prices. A firm that needs lease comps or market forecasts should look elsewhere, and the vendor says so itself.

## Limits Recorded

- One plan at **$149 per month** with no seat tiers, and contact lookups metered on tokens rather than requests.
- **60 requests per minute** per account, stated by the vendor.
- Agent changes require a human approval through a link that expires in **15 minutes**.
- No published tool inventory, so an integration plan cannot be built from the docs alone.
- Coverage is county dependent, and sale prices are missing in many states.
- Pricing and coverage read on **2026-11-07**; re-read `https://westkite.com/pricing.md` before quoting either.

## See Also

- [DFX Intelligence MCP](/hermes/mcp/servers/external/dfx-intelligence-mcp/) - credit provider and parcel intelligence on one keyless endpoint
- [Hercules Property MCP](/hermes/mcp/servers/external/hercules-property-mcp/) - property management rather than prospecting
- [Otnox MCP](/hermes/mcp/servers/external/otnox-mcp/) - the public sector equivalent: buyer records joined to award history
