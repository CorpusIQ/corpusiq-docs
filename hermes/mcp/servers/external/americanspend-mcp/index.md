---
title: "American Spend MCP - US Card Spending by Merchant"
description: "A sign-in MCP server over 2 billion card transactions a month, with documented spend, cohort and benchmark methods and a free tier of 2,500 credits."
category: "Business Data"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-26
source: "mcpservers.org canonical arrival /servers/americanspend/mcp in the November 26 midday wave; official registry `com.americanspend/insights`; initialize on https://platform.americanspend.com/mcp returned 401 with a resource_metadata challenge on 2026-11-26, the protected-resource document answered 200 at the /mcp suffix and the authorization-server metadata answered 200; methods, plans and figures read from the vendor docs at docs.americanspend.com and the llms.txt on americanspend.com"
relevance: "★★"
tags: [consumer-spending, retail, market-data, card-transactions, benchmarks, oauth, remote-mcp]
last_updated: "2026-11-26"
---

# American Spend MCP

**"Is this brand growing?" is the question a model answers from a news cycle, and card spending is the answer nobody has in a chat window.** American Spend indexes about 2 billion card transactions a month and resolves them to business, place and day, then exposes the result to agents over MCP alongside Census, BLS, BEA and OECD series for comparison. It is the first consumer-spend panel in this catalog, and the honest limitation is stated up front: the endpoint needs a signed-in account, so this guide documents the methods and the tiers from the vendor's own specification rather than from a driven tool list.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://platform.americanspend.com/mcp
              https://platform.americanspend.com/mcp-openai   (Codex)
Auth:         OAuth 2.1, sign-in in the browser, no API key to paste
Registry:     com.americanspend/insights
Challenge:    401 {"error":"unauthorized"} with
              WWW-Authenticate: Bearer resource_metadata=".../oauth-protected-resource/mcp"
Methods:      23 documented across six groups, not readable without an account
Free tier:    2,500 credits a month, no card
Pro tier:     $100 a month or $1,000 a year, 100,000 credits a month
```

## What the discovery documents say

The refusal is a proper OAuth challenge rather than a bare 401, and both documents behind it answer:

- **Protected resource**, at `/.well-known/oauth-protected-resource/mcp`, returns `resource: https://platform.americanspend.com/mcp`, `scopes_supported: ["openid","profile","email"]`, its own host as the authorization server, and `bearer_methods_supported: ["header"]`. The bare well-known path without the `/mcp` suffix answers **404 not_found**, the suffix trap recorded on other servers in this catalog.
- **Authorization server metadata**, at `/.well-known/oauth-authorization-server`, returns `authorization_code` plus `refresh_token`, **PKCE S256 only**, a registration endpoint, `token_endpoint_auth_methods_supported: ["none"]`, and `client_id_metadata_document_supported: true`.

The scope set is the thing to read twice. **Only identity scopes are advertised**, so the permission boundary is not a scope an agent can be granted narrowly: access control happens on the account, and the plan decides how much of the record is live.

## The documented methods

The vendor publishes 23 methods in six groups. They are listed here as documented, with the argument names the docs give, and no response shape is invented:

| Group | Methods | What the docs say they answer |
| --- | --- | --- |
| Merchant spend | `query_spend`, `search_merchants`, `compare_brands`, `find_groups` | aggregate spend for a merchant or a merchant set over a window, with `day`, `week` or `month` granularity, at most 16 weeks per weekly call and 366 days per window |
| Breakdowns | `breakdown`, `category_trends`, `category_summary` | spend split by up to two dimensions, including spender state, merchant state, merchant ZIP, spender metro and the card rail |
| Place and audience | `region_summary`, `cohort_overlap`, `cross_shop`, `wallet_migration` | growth by income tier per metro, the overlap between up to ten brand audiences, the merchants a cohort cross-shops, and wallet movement |
| Benchmarks | `list_benchmarks`, `benchmark_series`, `compare_to_benchmark` | BLS, Census, BEA and OECD series, with a model series set beside one of them |
| Model facts | `coverage`, `panel` | which days are complete, and how large the model is on a stated date |
| Account | `get_plan`, `get_credit_balance`, `create_upgrade_checkout`, `create_topup_checkout`, `get_topup_status`, `report_issue`, `about_american_spend` | plan, credits, Stripe checkouts, and a channel for a wrong answer |

Two details in that table change how a client should be written. `coverage` and `panel` cost nothing **with or without an account**, so an agent can date the data before it pays for anything. And `query_spend` prefers `merchant_id` once known, because *"a name search is a lookup, not the first step of a spend question you can already name"*.

## The model, in the vendor's own numbers

The published figures are **$1.2 trillion** of annual consumer spend tracked, **2 billion** transactions indexed per month, **150 million or more** monthly active accounts, and **1 million** merchant locations, with the live dates and live model size to be read from `coverage` and `panel` rather than from the byline. Three disclosures matter more than any of them:

1. **Card only.** Credit, debit and alternative debit. Cash, checks and bank transfers never touch a card, so the panel never sees them, and the dollar totals are that slice of the market.
2. **Not revenue.** The panel sees card purchases at the merchant, so its figures sit well below a company's reported sales, which include cash, wholesale, gift cards, international sales and timing. The vendor states that the gap holds steady brand by brand, so growth tracks while levels do not.
3. **Revised.** A day's first read lands within hours and most of it is in later, and later transactions change the newest days. Nothing on this surface is final on the day it is read.

Accuracy is checked against company-reported sales and Census retail sales, with a benchmark page comparing the model against reported revenue for **53 companies**. That page is the reference to send anyone who asks whether the numbers can be trusted.

## Plans and what a call costs

- **Free:** 2,500 credits a month, no card, sign-in only.
- **Pro:** 100,000 credits a month at **$100 a month or $1,000 a year**, bought through Stripe Checkout from inside the server.
- **Top-ups:** credit packs of 10,000 to 100,000 at **$1 per 1,000 credits**, Pro keys only.
- **Institutional:** the Revere product and API licensing are sold separately.
- A call that fails costs nothing, and the account tools stay callable when the balance is gone.

## Client support, as documented

Claude (custom connector, works on the free plan), Claude Code, Codex at the `/mcp-openai` endpoint, Cursor, VS Code and Antigravity are documented with exact install commands. **ChatGPT is documented as coming soon and is not available**, so any surface that claims a ChatGPT one-click for this server is ahead of the vendor.

One organisational constraint worth surfacing early: on a Team, Enterprise, Business or Edu workspace, only an admin can add a connector, so the check happens before the spend, not after.

## Where it fits a business-answer system

Every business question about demand eventually needs a volume number, and this is the first external server in this catalog whose volume number is a transaction panel with a stated coverage boundary and a published accuracy check. The pairing that matters is `compare_to_benchmark`: a brand's card spend set beside a Census or BLS series is exactly the shape of a defensible market answer, with the vendor's own caveat that a CPI category and a merchant classification are not the same object and the category mapping's fit has to be read before they are treated as one.

## Can these figures be quoted as a company's revenue?

No. They are card purchases at the merchant, which excludes cash, wholesale, gift cards and international sales, and the vendor states the dollar figures sit below reported sales by design. Quote them as panel spend with the date, and use the growth direction rather than the level.

## Does the free tier cover a real question?

Yes, on paper: 2,500 credits a month with no card is enough for a handful of merchant, category and coverage calls, and the model-fact tools cost nothing at all. The credit cost per call is published on the vendor's pricing page rather than in the handshake, so read it before building a loop.

## What is not verifiable from outside?

The 23 method names, their arguments and the pricing come from the vendor's documentation, not from a driven `tools/list`, because the endpoint refuses every unauthenticated call. The authentication chain, the scope set and the two well-known documents were verified live. Treat the method list as documented by the vendor.

## Connecting it

Add `https://platform.americanspend.com/mcp` as a remote MCP server in any OAuth-capable client, or `https://platform.americanspend.com/mcp-openai` for Codex, then sign in through the browser. No key is pasted. Start with `coverage` and `panel`, which cost nothing, then `search_merchants` once, then `query_spend` on the `merchant_id` for everything after that.

## See also

- [SEA Cold Chain MCP](/hermes/mcp/servers/external/seacoldchain-mcp/) for another first-of-class market total with a coverage share attached
- [External MCP server catalog](/hermes/mcp/servers/external/index.md) for the rest of the market-data group
