---
title: "Reachkit MCP - Cold Email Campaigns an Assistant Can Run"
description: "Find B2B leads, import verified work emails, write sequences and launch campaigns from Claude or ChatGPT, with an approval step before anything sends."
category: Sales / Cold Outreach
stars: n/a (subscription plus contact credits)
added: 2026-10-27
source: "live MCP probes on reachkit.ai/mcp (initialize 401 unauthorized), RFC 9728 protected-resource and RFC 8414 authorization-server documents read live, official MCP registry entry ai.reachkit/reachkit 1.0.0, and the vendor integration page reachkit.ai/ai-assistants"
relevance: ★★★
tags: [cold-email, b2b-leads, prospecting, outreach, sequences, sales, campaigns, oauth]
last_updated: "2026-10-27"
---

# Reachkit MCP

**The outreach pipeline that most operators run across four tools now sits in one conversation: find the people, import the emails, write the sequence, launch it, then answer what comes back.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://reachkit.ai/mcp
Transport:   JSON-RPC over POST
Auth:        OAuth 2.1 with dynamic client registration, or an account access token
Scopes:      mcp (plus openid, email for sign-in)
Tools:       lead search, contact import, list research, sequence builder,
             campaign launch and analytics, Unibox replies
Built by:    Reachkit (reachkit.ai)
Registry:    ai.reachkit/reachkit version 1.0.0, active
```

## Why This Matters for Operators

Cold email is the one acquisition channel where the work is entirely mechanical and entirely sequential: search a list, enrich it, write the sequence, attach an inbox, schedule it, then read replies and answer them. That is six tools and a spreadsheet in most companies, and the handoff between each one is where campaigns stall.

Putting it in the assistant does not change the strategy. It changes how much of the strategy actually gets executed, and it is the first server in this catalog where an agent can spend sending reputation rather than money.

## What It Actually Does

`initialize` without a token returned HTTP 401 with `{"error":"unauthorized"}`. The discovery documents answer without an account:

- `/.well-known/oauth-protected-resource` returned HTTP 200: resource `https://reachkit.ai/mcp`, authorization server `https://reachkit.ai`, `bearer_methods_supported: ["header"]`, `scopes_supported: ["mcp"]`.
- `/.well-known/oauth-authorization-server` returned HTTP 200 with a **registration endpoint** at `/oauth/register` (RFC 7591, so a client registers itself), `token_endpoint_auth_methods_supported: ["none"]` (public client), PKCE `S256` only, authorization code and refresh grants, `authorization_response_iss_parameter_supported: true`, a userinfo endpoint, and identity claims `sub`, `email`, `email_verified`.

The vendor documents the surface as six flows:

| Flow | What the agent does |
|---|---|
| Find leads | Search 500M+ people and 70M+ companies by title, seniority, industry, location, company size and technology. Searching is free inside a daily allowance. |
| Import contacts | Import with verified work emails at one credit each, and matches without a verified email are refunded. |
| Research the list | Break a list down row by row and save findings as columns that become merge tags. |
| Build campaigns | Write the sequence with A/B variants, merge tags and spintax, and preview every email as it will send. |
| Launch and manage | Attach inboxes, set the schedule, pause and resume, read analytics by campaign and reply rate. |
| Answer replies | List, label and answer Unibox conversations, on the Scale plan. |

## The Part That Costs You Something

Two things here are not reversible in the way a document edit is.

**Launching spends sending reputation.** A campaign goes out from inboxes that are attached to your domains, and the blocklist and bounce handling that come with the account are what stand between a bad import and a burned domain. The vendor states that the assistant shows the campaign and waits for a go before launching, and that drafts and previews never send - but that gate lives in the client's approval behaviour, not in the token scope, because the scope is a single `mcp`.

**Imports spend credits.** Verified-email imports bill one credit each, with a refund when no verified email is found. The search itself is free within the daily allowance, so the cost is in the import, which is the step worth pricing before it runs.

## How It Is Contained

- **OAuth sign-in as you.** The assistant acts with your workspace, your member permissions and your plan limits, and access is revoked from the account page immediately.
- **Identity scopes only.** `mcp`, `openid` and `email` - no per-object permission split, so the containment is the account role plus the approval step.
- **Previews are free.** Sequence previews and drafts do not send, which makes the review step genuinely non-destructive.
- **Private client registration.** `token_endpoint_auth_methods_supported: ["none"]` with mandatory PKCE is the correct shape for a desktop or CLI client that cannot keep a secret.

## Limitations Recorded

- No tool call was executed: every path requires an account, so the capability groups come from the vendor's integration page rather than a live `tools/list`.
- **Reply handling is plan-gated.** Reading and answering the Unibox requires the Scale plan; a lower tier gets find, import, sequence and launch only.
- **One scope for everything.** An agent that can read analytics can also launch a campaign, so the operator's approval behaviour is the only brake on the spending path.
- Lead counts are directory matches, not intent. Title and technology filters select who exists on a list, not who is buying this quarter.
- Importing contacts a second time is a paid import again unless deduplication against existing campaigns is done first, which the vendor documents as part of the import step.

## FAQ

### Is this a scraping tool for LinkedIn?
No. It searches Reachkit's own people and company index, which is why searching is free and importing verified emails is what costs credits.

### Can the agent send email without me seeing it?
Launching is documented as an approval step, and previews never send. The token carries one scope, so the protection is the client's confirmation, and it is worth testing that your client asks before you attach a real sending inbox.

### What should I actually test first?
One narrow segment and one sequence. The expensive mistake is not the credit spend, it is a 200-contact send from a domain whose reputation you need for the next year.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Adspy MCP - competitor ad libraries](/hermes/mcp/servers/external/adspy-mcp/)
- [CorpusIQ connectors for CRM and marketing data](/hermes/mcp/)
