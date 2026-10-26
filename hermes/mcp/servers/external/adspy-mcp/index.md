---
title: "Adspy MCP - Competitor Ad Creative Research in the Assistant"
description: "Meta and Google ad creatives in an MCP client with hook, angle, format, CTA and transcript per ad, plus organic posts later run as ads."
category: Marketing / Advertising Intelligence
stars: n/a (paid, from $19 a month; OAuth sign-in or API key)
added: 2026-10-26
source: "live MCP probe on www.adspy.sh/mcp (HTTP 401 invalid_token) + RFC 9728 protected resource and authorization server metadata + vendor pricing page + mcp.so feed card 2026-10-26T09:48Z"
relevance: ★★★
tags: [advertising, meta-ads, google-ads, tiktok, creative-research, competitor-analysis, marketing, oauth]
last_updated: "2026-10-26"
---

# Adspy MCP

**Competitor research that used to mean a browser tab per advertiser, now a question in the assistant you already pay for.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://www.adspy.sh/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        OAuth 2.1 authorization code with PKCE, plus a client ID metadata document
Tools:       not readable without a session
Built by:    Adspy (adspy.sh)
Registry:    not listed in the official MCP registry
```

## Why This Matters for Operators

Every operator eventually asks what a competitor is actually running. The answer decides creative, offer and channel, and almost nobody gets it from the public ad libraries because reading them by hand is a second job.

The interesting part of this server is that it does not connect an ad account. It reads public advertising, so the analysis is available to a business that has no relationship with the competitor and no access to their spend. What it gives back per advert is the hook, the angle, the format, the call to action and a transcript, which is the material you would otherwise screenshot and describe to somebody.

## What It Actually Does

`initialize` on the endpoint returned **HTTP 401** with `{"error":"Connect an authorized Adspy account.","code":"invalid_token"}`, so the capability below is read from the server's own discovery documents and the vendor's published product, and this guide says which is which.

The RFC 9728 protected resource at `/.well-known/oauth-protected-resource` returned `resource: https://www.adspy.sh/mcp`, a single authorization server at `https://www.adspy.sh`, header bearer tokens, and five scopes: `read`, `write`, `discovery`, `export`, `usage`, with `resource_name: Adspy creative research`.

The authorization server metadata returned `issuer: https://www.adspy.sh` with `/oauth/authorize`, `/oauth/token`, `/oauth/revoke` and `/oauth/register` endpoints, `response_types_supported: ["code"]`, authorization code and refresh grants, PKCE `S256`, `token_endpoint_auth_methods_supported: ["none"]`, and `client_id_metadata_document_supported: true` - a modern profile where the client identifies itself by a hosted metadata URL instead of a pre-registered secret.

Per the vendor listing, the library holds over two million creatives from 2,000+ advertisers over Meta (Facebook and Instagram) and Google (including YouTube), with organic TikTok, YouTube and Instagram posts on the paid tiers, and each result returns the hook, angle, format, CTA and a full transcript. Findings can be saved into collections with notes, and an ad can be traced to the same creative later run as an organic post, or the reverse.

### What it costs

| Plan | Price | Coverage | Credits |
|---|---|---|---|
| Starter | $19/mo, one user | one source: Meta, Google or TikTok | 2,000/mo - about 22 Brand Full Analyses, 33 social reports or 5 new brands |
| Pro | $39/mo, one user | every source | 6,000/mo - about 66 analyses, 100 reports or 15 new brands |
| Unlimited | $99/mo, one user | every source | no credit count, fair use on browsing and new collections |
| Enterprise | contract | every source | adds the REST API |

Extra users are +$5, +$15 and +$29 a month. The credit conversion is published, which lets an operator price a research habit rather than guess at it.

## What It Does Not Do

- **No spend and no ROAS.** It reads what brands run and for how long, not what it cost them. Any claim about competitor budget built on this data is invention.
- It does not connect an ad account, so it cannot read your own campaigns and it is not a replacement for a Google Ads or Meta Ads connector.
- Every result sits behind a paid plan; there is no free tier on the endpoint.
- The tool schemas were not read directly because discovery needs a session, so argument names in this guide are not quoted as schema.
- Library coverage per brand is the vendor's claim and was not sampled from outside an account. The vendor does take requests to add a missing brand.

## FAQ

### Is this competitive intelligence or ad management?
Research. It answers what a brand is running, in what format, with which hook, and for how long a creative has survived, which is a decent proxy for whether it works. It cannot launch, pause or budget anything.

### Why does the OAuth profile matter?
Because a client that only supports static secrets cannot complete the flow, while any client that supports PKCE and client metadata documents can register itself. `token_endpoint_auth_methods_supported: none` plus PKCE is the public-client pattern, and `client_id_metadata_document_supported: true` means no manual app registration.

### How long a creative has run is a signal, is it not?
It is the only performance proxy the public data offers, and the vendor exposes it as duration per ad. Treat it as evidence of what a brand kept, not as a measured result.

### Does it cover TikTok ads?
Organic TikTok posts are covered on the paid tiers; the paid sources are Meta and Google. Starter covers exactly one source, so a TikTok-first brand should read the plan table before paying.

## The Operator Test

Pick the competitor you lose deals to and ask for their ads from the last ninety days with the openings quoted. If the first three hooks are better than yours, the $39 was the cheapest creative brief you will get this quarter.

Pairs with `paidsync-mcp` and `adrails-mcp` for running campaigns, and with `openadlibrary-mcp` for a second read on the same public ad data, because research, execution and measurement are three different legs.
