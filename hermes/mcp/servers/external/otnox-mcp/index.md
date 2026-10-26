---
title: "Otnox MCP - Public Procurement With Buyer History"
description: "Tender notices from 78 national portals normalised into one record, joined to award history and buyer behaviour."
category: Data & Analytics
stars: n/a (vendor-hosted; no public repository)
added: 2026-10-24
source: "mcpservers.org /all page 1 (slug otnox-com-en-claude) plus the vendor's llms.txt, /en/api, /en/pricing and the MCP endpoint root page"
relevance: ★★★
tags: [procurement, tenders, b2g, government-contracts, buyer-intelligence, competitive-intelligence, award-history, public-data, remote-mcp, oauth]
last_updated: "2026-10-24"
---

# Otnox MCP

**A company that sells to governments loses most of its bids before it writes them. The award record already says who wins a buyer's work, at what price, and how often the same three suppliers keep coming back.**

```
Server type: Remote (Streamable HTTP) at https://mcp.otnox.com/mcp
Auth: OAuth 2.1, authorization code with PKCE S256, dynamic client registration, scopes otnox:read and otnox:write, token_endpoint_auth_methods_supported ["none"]
Live check: POST initialize without a token returned HTTP 401 {"jsonrpc":"2.0","id":null,"error":{"code":-32001,"message":"Authentication required"}} with www-authenticate naming https://mcp.otnox.com/.well-known/oauth-protected-resource
Discovery: that document returns 200 with resource https://mcp.otnox.com, authorization server on the same host, bearer in header, and resource_documentation https://mcp.otnox.com/; /.well-known/oauth-authorization-server adds authorize, token, register and revoke endpoints, code and refresh grants, S256, and no client secret
Tools: 5, documented by the vendor as read-only - search_tenders, get_tender_details, get_buyer_profile, get_competition_signals, qualify_opportunity (the only paid one, priced in AI credits)
Coverage: 89 markets claimed in the vendor's coverage snapshot dated 2026-10-19; 78 national markets, 11.43M tenders indexed and 47,000+ classification codes on the data API page
Pricing: Trial EUR 0 for 7 days with 50 credits and no card; Premium EUR 98 per month plus VAT with 1 market and 200 credits a month; Enterprise with unlimited markets, API access and scheduled exports
Vendor: Otnox (otnox.com)
```

## Why This Matters for Operators

Public procurement is the largest buyer-side dataset a small company can act on, and it is the one dataset almost nobody joins. The notices are public by law. The award results are public by law. What is missing is the link between the two: the same buyer, the same category, the winner, the value, and how often that winner was the same company as last time.

A supplier that can see that link stops guessing. It knows which buyers concentrate their awards in one supplier, which buyers spread them across twelve, and which tenders are the fourth attempt at the same requirement after three failed runs. That is the difference between bidding on everything open in your sector and bidding on the four that are winnable this quarter.

The catalog had two entries in this space, and both were built as narrow readers: EU TED notices through an Apify actor, and Texas ESBD solicitations through an Apify actor with your own token. Useful, and each stops at the notice. Otnox is the first entry here that carries the notice, the buyer, the award history and a verdict tool on one connection, across markets rather than one agency.

## What It Actually Does

Five tools, all documented as read-only on the endpoint's own root page.

| Tool | What it answers |
|---|---|
| `search_tenders` | Live or awarded notices by keyword, market, CPV code, value and deadline |
| `get_tender_details` | The full record for one notice, including the source documents where the market supports them |
| `get_buyer_profile` | Buyer behaviour: volumes, categories, bidder statistics and winner concentration |
| `get_competition_signals` | Who else tends to bid, for a tender or a whole market segment |
| `qualify_opportunity` | A bid/no-bid assessment against your company profile, priced in AI credits |

The first four are the data. The fifth is the judgement, and it is the only metered call: the vendor's own documentation states that the verdict costs 5 credits, that searching, opening a tender, reading a buyer history and checking who else bids are free and unmetered, and that re-asking about the same tender is free for 30 days. That pricing shape is deliberate and worth noting - it charges for the answer, not for the reading, which is the opposite of how most data connectors meter.

Underneath the tools, the vendor's data API page describes the pipeline in concrete terms: 78 national markets on 6 continents, 11.43M tenders indexed, 47,000+ classification codes across CPV, UNSPSC, CPC and national systems, with published cross-walks so a Spanish CPV code can match a Peruvian UNSPSC code. Source formats named are OCDS releases, eForms, CSV dumps, DataTables and hidden JSON APIs, refreshed daily from national portals rather than mirrored from an aggregator.

The coverage snapshot the vendor publishes is dated, which matters more than the headline number: 89 markets verified on 19 October 2026, with the accompanying statement that coverage does not mean every market carries equally complete data or daily new notices. A dated claim that admits unevenness is a better signal than a round number.

## Installation

```bash
claude mcp add --transport http otnox https://mcp.otnox.com/mcp
```

For Hermes:

```bash
hermes mcp add otnox --url https://mcp.otnox.com/mcp
```

Either client discovers the authorization server from the 401 and runs the OAuth flow itself. Nothing is configured by hand and there is no API key to paste.

## Configuration

```json
{
  "mcpServers": {
    "otnox": {
      "type": "http",
      "url": "https://mcp.otnox.com/mcp"
    }
  }
}
```

A keyless call is refused by design, so a probe that stops at `initialize` will always see a 401 here. That is the healthy state, not a broken endpoint: the metadata documents resolve and name the scopes before any credential exists.

## What It Costs

| Plan | Price | What changes |
|---|---|---|
| Trial | EUR 0 for 7 days, no card | 1 market, full product including the MCP connection, 50 AI credits |
| Premium | EUR 98 per month plus VAT | 1 market, 200 AI credits a month, award and buyer history, match scoring and verdicts, alerts to email, Slack, Teams and Telegram, CRM pipelines, auto-translation across 16 languages |
| Enterprise | Quoted | Unlimited markets, full API access and scheduled exports, separate workspaces per department, granular permissions, SSO and SAML, SLA, custom market onboarding |

On Premium, each extra user is EUR 10 a month and each extra department workspace EUR 15. Credit packs are sold separately at EUR 9 for 100, EUR 39 for 500 and EUR 99 for 1,500, and they do not expire. Markets are the real meter: one market is included and an operator selling into three countries is buying three times the base plan, which is the number to check before adopting.

## Integration with CorpusIQ

The question Otnox answers is not in any of the operator's own systems, and the question the operator's own systems answer is what makes Otnox usable.

CorpusIQ reads what the business already recorded: won and lost deals from a CRM connector, revenue and margin from QuickBooks or Stripe, delivery costs from the project tools. Otnox reads what every other supplier in the market was doing at the same time. Put together, the operator can ask which categories their own win rate is strongest in, then ask which buyers in those categories concentrate awards in a single incumbent - and get a shortlist where the buyer's own award record is the evidence, not a score.

The second pairing is the honest one for pricing. Because `qualify_opportunity` costs credits while reading is free, the sequence that pays for itself is: read broadly across markets, then spend credits only on the tenders that survived the operator's own filter. That is a different usage pattern from a connector that meters every call, and it is the reason this entry is useful to a small supplier and not only to a bid team with a subscription.

## Limitations

- **No tool call was possible without an account.** The endpoint, the OAuth metadata and the five tool names are verified live; the schemas behind those five names are the vendor's documentation and its pricing page, not a response this sweep observed. Stated plainly rather than implied.
- **The market count is stated four different ways on the vendor's own surfaces.** "50+ markets" on the MCP endpoint page, "78 national markets" on the data API page, "80+ markets" on the Claude and ChatGPT pages, and "89 markets verified 19 October 2026" in the coverage snapshot, which also says coverage depth varies by market. Treat 78 national portals as the defensible number and the 89 as the snapshot date's inclusive count.
- **The MCP surface is narrower than the platform.** The vendor sells monitoring, exports, CRM pipelines and document analysis on the platform; the connector exposes search, detail, buyer profile, competition and verdict. An operator who needs scheduled exports is buying the Enterprise API, not this connection.
- **One market per plan unit.** Premium covers a single market and Enterprise is the only unlimited tier, so the effective cost of a multi-country question is a multiple of the headline price.
- **Award data and estimated values are different things.** The vendor says so in its own methodology notes: keep the currency and the value type as shown, and read missing values as unknown rather than zero. Amendments, lots and award notices can describe the same procedure more than once, so a naive count of notices overstates the number of opportunities.
- **It is an aggregator, not a portal.** The vendor states outright that Otnox is not a government procurement portal and that original notices are authoritative for deadlines and submission rules. Every figure that matters legally should be read at the source document, which the tools link to where the market supports it.
- **Listed on mcpservers.org, absent from mcp.so.** The detail page served normally on 24 October 2026 and `mcp.so/server/otnox` returned 404 on the same day.

## FAQ

### Can an agent use it without an account?

No, and that is the whole gate. `POST initialize` returns HTTP 401 with `Authentication required` before anything else happens. The trial is 7 days with 50 credits and no card, so the cost of finding out is a sign-up, not a purchase.

### Does the verdict make it a decision tool rather than a data tool?

It makes it both, with the meter on the decision. Four of the five tools read; `qualify_opportunity` returns an assessment against your own company profile and charges credits for it. An operator can therefore use this as a pure data source and never spend a credit, or use it as a bid filter and pay per question.

### How does this differ from the TED and Texas entries already in this catalog?

Those two are single-source readers delivered over Apify, and each needs your own Apify token. Otnox normalises 78 national portals into one schema with cross-walked CPV, UNSPSC and CPC codes, then joins the notices to award history so a buyer's past winners are readable. Depth per market varies - the vendor says so - but the join is the difference.

### Who is this actually for?

B2G suppliers and the people who decide what to bid on: an SMB selling into public tenders in one or two countries, or a bid team that wants a shortlist instead of a spreadsheet. A company that sells only to consumers gets nothing from it.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [TED Tender Monitor](/hermes/mcp/servers/external/ted-tender-monitor)
- [Texas ESBD Procurement MCP](/hermes/mcp/servers/external/tx-esbd-procurement-mcp)
- [Klarix Intelligence Engine](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
