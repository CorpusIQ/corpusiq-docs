---
title: "SteadyScrape SEO Data MCP - SEO Priced Per Keyword"
description: "Nine read-only SEO tools that cost nothing to list and about four cents per ten keywords to run, billed through your own Apify account."
category: "Marketing"
stars: "n/a (vendor-hosted; runs on Apify Actors)"
added: 2026-11-23
source: "A canonical mcpservers.org arrival at /servers/steadyscrape/seo-data-mcp stamped 2026-11-24T00:21Z; keyless initialize and tools/list on https://mcp.steadyscrape.dev/seo/mcp answering 200 as steadyscrape-seo-data 0.2.0 with nine tools; a keyword_metrics call refused 401 -32001 'Sign in with Apify to use this tool.'; the protected-resource document at https://mcp.steadyscrape.dev/.well-known/oauth-protected-resource/seo/mcp and the Apify authorization-server document at https://console-backend.apify.com/.well-known/oauth-authorization-server, both read 2026-11-24; the vendor page https://mcp.steadyscrape.dev/seo and the pricing page https://steadyscrape.dev/pricing"
relevance: "★★★"
tags: [seo, keyword-research, serp, backlinks, google-trends, youtube, apify, oauth, remote-mcp, marketing]
last_updated: "2026-11-23"
---

# SteadyScrape SEO Data MCP

**The SEO tool market has a price problem: a mid-tier seat costs a couple of hundred dollars a month whether you ask three questions or three thousand.** SteadyScrape removes the seat and prices the question. Its SEO Data server exposes nine read-only tools over keyword volume, live Google results, rank checks, domain traffic, backlinks, Google Trends and YouTube, and every call is billed at the per-unit rate of the Apify Actor behind it, in the buyer's own Apify account.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.steadyscrape.dev/seo/mcp
Server name: steadyscrape-seo-data 0.2.0
Auth:        OAuth 2.1 against Apify (console-backend.apify.com), scope full_api_access
Billing:     per call, at the Apify Store list price of the underlying Actor
```

## What was measured

`initialize` and `tools/list` both answer **HTTP 200** with no credential, so the tool surface is public and an agent can decide whether it wants the server before anyone signs in:

```
initialize  -> 200  {"name":"steadyscrape-seo-data","title":"SteadyScrape SEO Data","version":"0.2.0"}
tools/list  -> 200  9 tools, every one annotated readOnlyHint: true
tools/call  -> 401  {"jsonrpc":"2.0","error":{"code":-32001,
                    "message":"Sign in with Apify to use this tool."}}
```

That shape is worth naming because it is the opposite of the common failure. Most gated servers refuse the handshake and tell you nothing. This one publishes its whole inventory and refuses only the thing that costs money. The refusal is **JSON-RPC in band** with `-32001`, not a bare HTTP error page, so any client renders it as an answer rather than as a transport failure.

The discovery chain is complete on both hops. `https://mcp.steadyscrape.dev/.well-known/oauth-protected-resource/seo/mcp` answers **200**:

| Field | Value |
| --- | --- |
| `resource` | `https://mcp.steadyscrape.dev/seo/mcp` |
| `authorization_servers` | `["https://console-backend.apify.com"]` |
| `scopes_supported` | `["full_api_access"]` |
| `bearer_methods_supported` | `["header"]` |
| `resource_name` | `SteadyScrape SEO Data` |

and the issuer publishes an RFC 8414 document at `https://console-backend.apify.com/.well-known/oauth-authorization-server`, also **200**, with `authorization_endpoint` on `console.apify.com/authorize/oauth`, a `token_endpoint`, a `device_authorization_endpoint`, a registration endpoint at `/oauth/apps`, scopes `openid`, `profile`, `email` and `full_api_access`, grants `authorization_code`, `refresh_token` and device code, and PKCE **S256**. A compliant client needs no vendor instructions to connect.

**The single scope is the operator's decision point.** `full_api_access` is not an SEO scope, it is the whole Apify account. A token minted here can drive every Actor in that account, so the account to connect is a billing account, not a trust boundary. Anyone who connects this to an assistant is lending it the same key that runs their scrapers.

## The nine tools, with the price beside each

Read from the vendor's own table on 2026-11-24 at Apify free-plan list prices, which the page states are lower on paid plans:

| Tool | Returns | Price |
| --- | --- | --- |
| `keyword_metrics` | volume, CPC, competition, difficulty, intent, 12-month trend, up to 100 keywords | $0.039 per 10 keywords with data |
| `google_serp` | live top 10-100, SERP features, **AI Overview text**, People Also Ask, one domain's position | $0.006 per 10 results of depth |
| `rank_check` | one domain across up to 10 keywords, live, one country | $0.006 per 10 results of depth per keyword with results |
| `domain_overview` | estimated organic traffic, ranking keywords, domain rank, backlinks, referring domains, up to 100 domains | $0.111 per 10 domains with data |
| `ranked_keywords` | keywords a domain or URL ranks for, with position, URL, volume, estimated visits | $0.071 per call with data |
| `backlinks` | backlinks or referring domains, strongest first | $0.082 per call with data |
| `google_trends` | interest over time for up to 5 keywords | $0.035 per call |
| `youtube_search` | ranked results with views, channel, duration, date | $0.006 per 20 results |
| `youtube_video` | public stats for one video, optional transcript | $0.018 per video, +$0.018 with transcript |

A session fee of **$0.005** is charged once per session, on the first call that returns data. Errors and refusals are free, and so are listing tools and connecting.

The parameters are the ordinary ones and the schemas are readable without an account: `keyword_metrics(keywords, country, language)`, `google_serp(keyword, country, language, device, depth, target_domain)`, `rank_check(keywords, target_domain, country, language, device, depth)`, `domain_overview(domains, country, language)`, `ranked_keywords(domain, country, language, limit)`, `backlinks(target, mode, limit, dofollow_only)`, `google_trends(keywords, country, time_range, search_type)`, `youtube_search(query, country, language, max_results)` and `youtube_video(video, include_transcript, language)`. Published limits: **60 tool calls per minute per account**, up to **100** keywords or domains per call, **10** keywords per rank check, and live SERP calls that take **5 to 30 seconds**.

## The limit that decides whether this is for you

On a free Apify plan the gateway caps these tools at roughly **$0.25 of usage per account per UTC day**, shared across all free accounts, with the reset at 00:00 UTC; paid Apify plans are not limited by the gateway. That is about **six ten-keyword metric batches**, or two thirds of one 100-domain traffic pull, so the free plan is a testing budget rather than a working one. The honest way to read the pricing is per unit of work: a 100-keyword volume pull is **$0.39**, a 100-domain traffic comparison is **$1.11**, and a weekly rank check of 50 keywords at depth 20 costs **$0.006 x 2 x 50 = $0.60** per refresh.

## Where the data comes from, and the double-pay risk

The vendor states on the server page that the SEO data comes from **DataForSEO under licence**, served through the *SteadyScrape SEO Data MCP Server* Actor on Apify. That matters for procurement: DataForSEO sells API access directly, and anyone already holding a DataForSEO contract is buying the same feed twice, once per unit and once again as an Apify margin. The product is not the data, it is the packaging: one endpoint, nine stable tool names, a schema an agent can read, and billing that lands on a subscription most teams already have.

The same company's second product explains the business model. SteadyScrape's Sheets add-on sells credit packs at **$9 for 1,500 credits, $29 for 6,000 and $79 for 20,000**, credits that do not expire, with keyword functions at 1 credit per cell and `DOMAIN_TRAFFIC` at 1 per cell against `BACKLINKS_TOP` at 20 per domain. The MCP server is the same data priced the same way, aimed at the assistant instead of the spreadsheet.

## How to connect

1. Add a remote Streamable HTTP server at `https://mcp.steadyscrape.dev/seo/mcp`. In Claude Code that is `claude mcp add --transport http steadyscrape-seo https://mcp.steadyscrape.dev/seo/mcp`, then `/mcp` to sign in.
2. Sign in with the **Apify account you want billed**. The vendor never sees the password; Apify runs the OAuth flow.
3. Start with `keyword_metrics` on ten keywords, which costs about four cents, and confirm the numbers against a source you already trust before widening to a 100-keyword run.

## What this guide can and cannot certify

Measured: the endpoint, the handshake on both methods, the refusal and its code, both metadata documents, the nine tool names with their schemas and annotations, the published per-tool prices and limits, and the company's published address (SteadyScrape, 91 - 1554 Carling Avenue, Ottawa, ON K1Z 7M4, Canada). Not measured: any tool response, because every call needs an Apify session, and the accuracy of any figure the tools would return.

## Verdict

**Three stars, and the missing two are about evidence rather than design.** Every tool response in this entry is the vendor's word, because the gate sits at the expensive step by design. What is certified is the part that usually goes wrong: a public schema, a spec-correct OAuth chain, a per-call price a finance person can forecast, and a refusal that says what to do next. For an operator already paying for an SEO seat, the interesting question is not whether this works but whether fifty cents of questions replaces the seat.
