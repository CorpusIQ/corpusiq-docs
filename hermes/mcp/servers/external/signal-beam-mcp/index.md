---
title: "Signal Beam MCP - Check Conversion Tracking"
description: "Audit server-side conversion tracking from chat: report reads, blocked events and duplicate pixels, with every fix proposed for owner approval"
category: Advertising & Marketing
stars: "n/a (hosted; OAuth 2.0 with a two-scope split, proposals approved in the dashboard)"
added: 2026-11-10
source: "the mcpservers.org thirteen-sitemap canonical (slug www-signalbeam-co) and the official registry record co.signalbeam/signal-beam 1.0.0, published 2026-11-10T06:14:37Z; the endpoint at app.signalbeam.co/mcp measured with a POST initialize that answered HTTP 401 and a protected-resource document listing two scopes; the capability and permission model read from www.signalbeam.co/ai"
relevance: ★★★
tags: [conversion-tracking, server-side-tracking, attribution, meta-ads, google-ads, consent, event-log, proposals, read-only-option, oauth, remote-mcp]
last_updated: "2026-11-10"
---

# Signal Beam MCP

**Every ad account has two failure modes that cost money silently: the purchase that never reached Meta, and the pixel that is installed twice and counts it twice. Neither shows up in a dashboard, because a dashboard only reports what arrived. Signal Beam's MCP server is built to answer the question behind them, which is what did not arrive and why, and to write the fix as a proposal a person approves rather than a change an agent made.**

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://app.signalbeam.co/mcp
Auth:         OAuth 2.0, normal Signal Beam login
Scopes:       sites:read, changes:propose
Registry:     co.signalbeam/signal-beam, version 1.0.0, status active,
              published 2026-11-10T06:14:37Z
Docs:         https://www.signalbeam.co/ai/
Guide:        https://www.signalbeam.co/guides/connect-ai-assistant/
```

## What the endpoint answers before it will talk

An unauthenticated `POST initialize` returned **HTTP 401** carrying a JSON-RPC error rather than a bare body: `{"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"Sign in to use this server."}}`. That is a small thing done right. A generic 401 leaves a client guessing whether the URL was correct; an error object on the protocol it speaks tells the caller the endpoint is a working MCP server that wants credentials.

The protected-resource document at `https://app.signalbeam.co/.well-known/oauth-protected-resource` returned **200** and is the most interesting part of the measurement, because the scope list is the product argument in two strings:

```text
resource:              https://app.signalbeam.co/mcp
authorization_servers: https://app.signalbeam.co
scopes_supported:      sites:read, changes:propose
resource_name:         Signal Beam
```

Two scopes, and the second one is a verb the model cannot complete on its own: it may **propose**. Nothing was driven past the handshake, because the session needs a login, so everything below about individual capabilities comes from the vendor's own documentation and is labelled as such.

## The permission model is the whole design

Most write-capable marketing servers in this catalog solve the trust problem with a preview flag the agent sets on itself. This one puts the gate outside the conversation. Every change is saved as a proposal with a link, and nothing happens until an owner or admin approves it on the AI access page. A connection can also be created read-only, which drops the propose scope entirely.

What a proposal can contain, per the vendor: blocking rules, custom events, page triggers, test event codes, pixel names, Stripe settings, and a site's name or currency. What the server cannot do, again per the vendor, is worth listing because each item removes a failure an operator has actually experienced with an over-eager agent:

- No tool deletes a site, a pixel or a rule.
- No access to ad accounts or campaigns, so it cannot change spend.
- No editing or publishing of the website.
- It never asks for or sees passwords, access tokens or API keys.
- Emails and phone numbers stay hashed, and the assistant is told only whether one was supplied, never the hash.

For a taxonomy that puts measurement next to money, that is a defensible boundary: the thing that decides whether an event counted is editable, and the thing that spends is not.

## What it reads

The read half is where an operator gets value on day one, and it maps cleanly onto the questions that normally need three tabs:

- Totals by day or week against the period before, revenue by source and campaign, and customer journeys.
- The event log, and one event's outcome at each destination platform, which is the "did every purchase reach Meta yesterday, and if not why not" question.
- Events held back and the reason, which in a consent-gated market is usually the honest answer rather than a bug.
- How often each custom event fires, which is how a double-installed pixel surfaces.
- An audit of each site with the most important problem first, a check that the script is on the live page, and a look for pixels installed twice.

The page's own example cards name three calls, `get_overview`, `get_blocked_events` and `propose_page_trigger`. Those are vendor copy rather than a `tools/list` response, so treat the names as illustrative until a connected client lists them.

## Connecting

The server address is `https://app.signalbeam.co/mcp`. Sign in with the normal Signal Beam login and choose whether the connection may suggest changes or only read.

```bash
claude mcp add --transport http signal-beam https://app.signalbeam.co/mcp
```

Then sign in from `/mcp`. A dashboard token works as well, with a lifetime of 30 days, 90 days or a year, and a session created by signing in asks for a fresh sign-in after 30 days without use. Claude and ChatGPT take the same URL as a custom connector or MCP server. The vendor states the server is included on every plan including the free trial, that a site added from a chat counts towards the plan's site limit like any other, and that the trial runs 7 days.

Three prompts from the vendor that are also a fair acceptance test, because each one requires reading rather than writing:

- "Did every purchase reach Meta yesterday? If not, why not?"
- "Why are events being held back, and how many?"
- "How many of my events carry an email or phone for matching?"

## The class it enters

Two neighbours need naming, because the honest question is why this is not one of them. [PaidSync](/hermes/mcp/servers/external/paidsync-mcp/) runs paid media from chat with 630+ approval-gated tools across fourteen platforms, and it includes conversion setup across GTM, GA4 and Google Ads. That is campaign operations with a tracking task inside it. Signal Beam is the measurement layer on its own: server-side event delivery, consent blocking, match quality and duplicate pixels, with no campaign surface at all. An operator who already has ad-ops automation has a reason to keep this separate, because the tool that can pause a campaign is not the tool you want auditing the thing that reports on it.

The second neighbour is the general analytics connector. A GA4 or GTM connector reads what the tag manager sent; this one reports what each destination received and what it refused, which is the difference between a traffic number and a conversion number you can defend.

## FAQ

### Can the assistant change my tracking without asking?

No. Every change is a proposal that an owner or admin approves in the dashboard, and a connection can be created read-only so that no proposal is possible at all.

### Does it see customer emails and phone numbers?

Emails and phone numbers are stored only as hashes, and the assistant is told whether one was supplied, never the hash itself. The vendor states the server has no access beyond what the connecting user can see in the dashboard.

### Does it count as a second site against my plan?

Yes. The vendor says a site added from a chat counts towards the plan's site limit like any other site, and the server is included on every plan including the free trial.

### What is the difference between this and my ad platform's own tracking report?

An ad platform reports what it received. Signal Beam reports what was sent, what each destination kept, what was held for consent and what was duplicated, which is the only view that explains a conversion gap instead of reproducing it.

## See also

- [PaidSync MCP](/hermes/mcp/servers/external/paidsync-mcp/) for approval-gated campaign operations across fourteen ad and measurement platforms
- [Linkly MCP](/hermes/mcp/servers/external/linkly-mcp) for click and attribution data on tracked links
- [Agent Help Network MCP](/hermes/mcp/servers/external/agent-help-network-mcp/) for what a host declares to an agent before a request is retried
