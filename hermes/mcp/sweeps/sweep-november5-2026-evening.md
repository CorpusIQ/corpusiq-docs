---
title: "MCP Server Discovery - November 5, 2026 (Evening Sweep)"
description: "Evening pass where the canonical stood still for a second time in one day, the mcp.so feed carried ten new cards in nine hours, and two servers were catalogued: a competitive analyst scored against your own won and lost deals, and a load planning engine that renders the plan in the conversation."
last_updated: 2026-11-05
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november5-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 5, 2026 (Evening Sweep)

## Summary

This pass fired on the **21:00 MST** tick, ten hours after the late morning read, and the two named discovery surfaces separated cleanly. The mcpservers.org twelve-sitemap canonical returned **19,513** server URLs after stripping the locale prefixes, **identical** to the 11:01 MST capture: **zero** additions and **zero** removals, the second exact empty diff in one day. `/all` answered **403** for the fifth consecutive pass, which is now a standing condition rather than an incident.

mcp.so carried the whole window: **172** timestamped cards on the page, collapsing to **140** parsed card objects across **117** distinct slugs, with **13** entries above the late morning stamp of `2026-11-05T17:29:38.960Z` that reduce to **10** distinct servers. Both reads, plain and cache-busted, returned the same newest stamp `2026-11-06T02:14:00.852Z`, so the feed was settled rather than mid-refresh. The submission queue added **23** items from `#6809` to `#6831`, one of them a listing update and **five** of them a single author's SEO fleet.

**Two** servers were catalogued, chosen on gaps rather than names: a competitive analyst that scores public signals against the customer's own won and lost deals, and a load planning engine that is the first bin-packing surface in the catalog.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 13 sitemap documents fetched directly with plain urllib, locale prefixes stripped, set difference against the 11:01 MST capture | **19,513** server URLs against **19,513**. **0** additions, **0** removals. A raw union reads **28,851** URLs and **9,338** of those are marketing, topic and search pages; only the `/servers/` subset is the server universe |
| mcpservers.org `/all` | direct fetch with a browser user agent | **403** Cloudflare, the fifth consecutive refusal. Not read |
| mcp.so homepage | two direct fetches, plain and cache-busted, `recentServers` parsed from the RSC payload | **172** timestamped cards, **140** card objects, **117** distinct slugs, newest `2026-11-06T02:14:00.852Z` on both reads, **13** entries above the late morning stamp reducing to **10** distinct servers |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included | **23** items, `#6809` to `#6831`, one listing update and one **5-item** author fleet |
| Official MCP registry API | search on both catalogued candidates | `ai.ripplewatch/ripplewatch` **0.1.0** active, published `2026-10-21T04:13:37Z`. Three searches on the load planning vendor returned **zero** records |
| Vendor surfaces | docs, pricing, security and OAuth metadata for both candidates | Ripplewatch: `/`, `/how-it-works`, `/pricing`, `/connect/guide`, `/faq`, `/security`, `/sitemap.xml` all **200**. LoadOptimizer: `/mcp-server/`, `/docs/ai-agents.html`, `/pricing` all **200** |

## New Servers Catalogued

### Ripplewatch MCP - Competitor Momentum Scored Against Your Own Deals

Relevance: HIGH. **Endpoint verified as gated** (keyless `initialize` returns **401** `{"error":"Authentication required."}` with a `WWW-Authenticate` header naming its protected-resource metadata), so the surface is documented rather than driven. Registered as `ai.ripplewatch/ripplewatch` **0.1.0** at `https://www.ripplewatch.ai/api/mcp`, active since **2026-10-21T04:13:37Z**.

The product is one join that the three competitive intelligence entries here do not make. Rivalize returns cited teardowns, Debriefing tracks evidence-backed signals, Klarix builds battlecards from public evidence: all three read the public web. Ripplewatch reads the public web **and** scores it against your positioning, your ICP and your closed deals, so the same price cut is urgent for one company and noise for another, with the reasoning printed beside the verdict.

- **Ten inputs**, each scored **-100 to +100**: hiring, pricing activity, product changes, press and funding, relevance trend, win rate against you, review sentiment, Reddit and Hacker News buzz, GitHub activity (opt-in) and ad activity (opt-in).
- **Five labels**: Heating up, Steady, Cooling, Gone quiet, Not enough history yet, with a low-confidence marker when the data behind a label is thin. The consumer page states the numeric band as below **-15** Cooling and above **+15** Heating up.
- **Six ingestion paths** for win and loss history: plain English, the Settings form, a CRM CSV export, an email forward address, an assistant reading closed deals from a tool it can already reach (HubSpot has an official connector; Gong's is read-only and returns summaries), or a scheduled prompt that runs the pull on a cadence.
- **Delivery**: Slack as the team feed (high-relevance alerts only, a weekly briefing at a chosen time, a monthly recap from week three), the assistant as the analyst, email as the fallback to the account owner.
- **Pricing read from the page**: **$29 a month** plus prepaid usage from a **$50** balance, first charge **$79**, no seat fee, unlimited teammates, platform fee and unused balance refundable within **30 days**. Answers and each tracked competitor both draw from the balance, so watching costs as well as asking.
- **Limits recorded in the guide**: no published tool names, no SOC 2 (the vendor says so on its own security page), business context is sent to Anthropic's Claude models per request, and the authorization server advertises `plain` alongside `S256` for PKCE.

### LoadOptimizer MCP - Truck, Container and Pallet Load Planning in Chat

Relevance: MEDIUM HIGH. **Endpoint verified as gated** (keyless `initialize` returns **401** with an empty body and `WWW-Authenticate: Bearer resource_metadata=..., scope="email"`).

This is the first load-planning surface in the catalog. The logistics corner here is about finding and tracking (Fitralo finds carriers, HaulierScope reads GB operator licences, Container Tracking follows shipments, PackIndex prices packaging) and nothing answers the question that sets the cost: what fits, in what order, and what is left over.

- The assistant checks a request, plans the load, follows it to completion, reports **per carrier** what fit and what did not, and can find, rename and cancel earlier plans. Libraries, stacking rules and saved loads are all reachable, and rule changes need an owner's connection.
- In Claude and ChatGPT the plan renders **as a 3D view inside the conversation**, and stacking rules render as a matrix that can be edited cell by cell. Loading-instruction PDFs remain web-app only.
- Approval covers four things: the account, full access versus read-only, public share links (off unless ticked), and which app is asking (other clients are refused).
- **Pricing**: Free with **15** optimizations a month, Standard **EUR 39.99**, Pro **EUR 99.99**, Business **EUR 399**, Enterprise custom, yearly 15 percent lower, VAT excluded. The connector needs a plan with API access, which starts at **Pro**, so the honest monthly cost of the MCP route is **EUR 99.99**; the 10-day full Pro trial needs no card.
- **Limits recorded in the guide**: the assistant shares the account's quota and request rate with API keys, actions are attributed to the approving user tagged `via: agent`, analytics record tool use and an assistant-written goal description with long numbers and contact details stripped, there is **no official registry record** on three searches, and ChatGPT needs OpenID Connect turned off or the approval page fails.

## Read and Held

Both new surfaces also carried a crowd. From the mcp.so feed, **10** distinct new servers were read; from the submission window, **23** items. Two were catalogued; the rest were individually evaluated and held:

| Candidate | What it is | Held on |
| --- | --- | --- |
| WisePPC | Amazon Ads and Seller Central, about 80 datasets, listing and ad changes with permissions | Amazon seller and ads class, carried by Sellermate, Nova Amazon, AMZ Vault and Webotee |
| Torvex `#6816` | media buyer traffic analytics, campaign ROI, affiliate spend | ad analytics class |
| Merit Ukrainian Law | Ukrainian legislation, case law and state registers, 120+ read-only tools | single-market legal research; the tool table was not verified this pass, so it is held rather than guessed at |
| FlowRunner Prompt to Flow `mcp.so` | describes an automation in English and builds a flow with approval steps, 25+ tools | automation builder class, carried by n8n MCP |
| Taskriz | asks a person for a decision, a date, a photo or a document and returns a structured answer | human-in-the-loop class, carried by PingRoom with 41 tools |
| Android Texter | SMS and MMS from the operator's own Android number, no Twilio | SMS gateway class, carried by InstantReply, Flyn and Soprano Connect |
| Faxbeep | sends a test fax and reads what arrived | fax testing vertical, no operator data |
| relvectors | PC maintenance, disk cleanup and overheating control across three operating systems | local system maintenance, no business surface |
| STRG `mcp.strg.com` | S3-compatible object storage over remote MCP | one-line listing with no tool surface published; **401** only |
| Ava Advisor `#6809` | stock screening and market news | personal finance class |
| Motion Reel `#6810` | Reels scheduling to Instagram, TikTok and YouTube Shorts | social scheduling class |
| post2all `#6811` | social scheduling and cross-posting | social scheduling class |
| Harbor `#6812` | read-only container registry: projects, quotas, scan results, replication | developer infrastructure, no operator data |
| Screwtape.ai `#6813` | decides whether an agent is allowed to run an action, API key or x402 | agent authorization and payments class |
| VidFare `#6814` | video generation cost per second, keyless | media cost comparison, thin surface |
| PepBank `#6815` | peptide research studies and trials | health research vertical |
| emissaoja `#6817` | Brazilian NFS-e service invoices | geo-niche accounting, carried by JaKonto, DokladBot, Pohoda and siblings |
| Keysrs `#6818` | macOS Keychain API-key vault with Touch ID for agents | secrets class |
| work-access-tools `#6819` | product categorization on a Cloudflare Worker with a 50-call free tier | thin, unverified product index |
| pagenull `#6820` | HTML or URL to PDF and screenshots with Ed25519-signed receipts | document rendering class, carried by RelayPDF, DocMake and Browserless |
| brewpage-mcp `#6821` | listing update: about text says 5 tools, now 20, config pinned 1.14.4 against 1.16.10 | not a new server |
| Datacircle `#6822` | keyless search over a directory of GTM APIs | a directory of APIs rather than a data source |
| CrakSEO fleet `#6823` to `#6827` | five submissions from one author: SEO MCP, free Search Console, SERP API, keyword research, backlink checker | one author's fleet under the single-author rule, and the SEO class is already deep here |
| QuotedPart `#6828` | prices CNC machined parts, OAuth, nothing priced anonymously | manufacturing quoting class, carried by CNC Compass, Mechanofab and Cutting Tools AI |
| FixMyPrompt `#6829` | prompt memory with index, merge, tighten and trim tools | memory and prompt tooling class |
| Holdbird `#6830` | dials customer service lines, waits on hold, rings your phone when a human answers | telephony automation with no business data surface |
| CorpusFetch `#6831` | a repository of concluded operational experiences for agents | description is one line and the product surface was not published; nothing to document yet |

## Core Listing Check

- **mcpservers.org**: LISTED. `/servers/corpusiq-io` is present in the twelve-sitemap canonical. The detail page itself answers **403**, which is the platform block that also refuses `/all`, not a delisting.
- **Glama**: LISTED. `https://glama.ai/mcp/connectors/io.corpusiq/multi-source-mcp` returns **200** on the connectors route.
- **Official MCP registry**: `io.corpusiq/multi-source-mcp` **1.0.0** with the `https://mcp2.corpusiq.io/mcp` remote, status active. The description still reads **30+** business systems against a catalog that now states 40+, which stays metadata drift to correct at the next publish.
- **mcp.so**: NOT LISTED. All four direct slug forms (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) return **404**, and the paid route stays declined under the no-payment rule, so it is not retried.

## Counts

Guide tree **1,104** directories before this pass, **1,106** after; **1,247** entries counting single-file guides before, **1,249** after. Two guides added: `ripplewatch-mcp` and `loadoptimizer-mcp`.
