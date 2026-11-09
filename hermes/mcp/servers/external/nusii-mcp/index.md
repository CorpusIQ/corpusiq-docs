---
title: "Nusii MCP - The Proposal Pipeline Inside the Chat"
description: "Draft a proposal from your own template, rework the line items in a sentence, and read the pipeline without opening the app."
category: Productivity
stars: "n/a (hosted SaaS; OAuth sign-in, 14-day trial)"
added: 2026-11-09
source: "the mcp.so feed card filed 2026-11-09T13:41:38Z; the Nusii MCP page at nusii.com/mcp; the OAuth protected-resource document at app.nusii.com; the endpoint itself, where a keyless initialize answered 401; and the vendor's State of Proposals 2026 report"
relevance: ★★
tags: [sales, proposals, quoting, pipeline, agencies, signatures, remote-mcp]
last_updated: "2026-11-09"
---

# Nusii MCP

**A proposal is where a service business either wins the work or loses a week writing it, and the two failure modes are the same in every agency: the pricing gets rebuilt from scratch on every call, and nobody can say what the pipeline looks like without opening the tool. Nusii has carried that workflow since 2013 for agencies, sales teams, SaaS companies and construction firms. Its MCP surface puts the draft and the pipeline inside the assistant, with the send button left where it belongs.**

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.nusii.com/mcp
Resource doc: https://app.nusii.com/admin_mcp
Auth:        OAuth sign-in to Nusii; scopes admin:read and admin:write
Tools:       not published as a table; the vendor names the operations
Trial:       14 days free, 60-day money-back guarantee
Docs:        nusii.com/mcp
```

## What the endpoint says about itself

A keyless `initialize` is refused rather than redirected:

```text
POST https://app.nusii.com/mcp   ->   401
{"jsonrpc":"2.0","error":{"code":-32001,"message":"Unauthorized"},"id":null}
```

The protected-resource document is published and it is unusually blunt about the reach of this connector: the resource is `https://app.nusii.com/admin_mcp`, the authorization server is `https://app.nusii.com`, and the only scopes offered are `admin:read` and `admin:write`. That is the tier this entry rests on: **live, gated, with the scopes documented by the vendor.** There is no keyless path, so nothing below is a claim about output from a live call. What the guide can measure is the endpoint, the scope pair and the vendor's own description of what the assistant does.

## What the assistant is asked to do

The vendor's page is a worked transcript rather than a feature list, and the operations it names are the whole proposal workflow:

| Operation the vendor names | On what |
|---|---|
| Templates list | The proposal templates the account already runs. |
| Clients search | Existing clients and contacts. |
| Create proposal from template | A draft built from a named template for a named client. |
| Update line items, update section, create section | The priced body of the draft. |

In the example, the assistant is asked for a proposal for a named client from a website redesign template, with five page templates and SEO as an optional extra, and it returns `$8,400.00` for the five templates with SEO priced as an add-on the client can take. The line the vendor puts under it is the design decision worth recording: **"I haven't sent anything, so review it and send it when you're happy."** The write path stops at the draft.

The second half of the same page is the pipeline read. Asked how the month looks, the assistant answers from the account: **12** proposals sent, **5** accepted, a **41.67%** acceptance rate, **4** pending, with the revenue, estimated pipeline value, view counts and the activity feed behind it. That is a question a founder currently answers by opening a browser tab.

## Why the draft and the pipeline belong together

Most of the friction in a proposal is not the writing. It is that the numbers live in one place, the accepted version lives in another, and the only person who knows how the month went is the one who sent them. A connector that can both draft and read the pipeline closes that loop inside the tool where the conversation already happens: you ask for the draft, you argue about price in the same thread, and then you ask what the acceptance rate has been so you can decide whether the price is right.

## The vendor's own numbers

The State of Proposals 2026 report is built on **9,022** proposals sent through Nusii in 2025 and states that **50.2%** of them got a yes. It is the vendor's own transaction data, not a survey, so treat it as a useful base rate for a proposal-driven business rather than an independent benchmark. The customer stories the vendor publishes quote conversion above 50% after switching, which is the usual selection effect and is recorded here as a claim rather than evidence.

## The class it enters, with the owners named

Signature execution already has owners here: [SignWell](/hermes/mcp/servers/external/signwell-mcp/), [SignSimple](/hermes/mcp/servers/external/signsimple-mcp/) and [Countersignatory](/hermes/mcp/servers/external/countersignatory-mcp/) all put a document in front of a counterparty and return a signed artefact, and Nusii ships electronic signatures too, but that is a feature beside its real surface. What is not carried here is the **priced proposal pipeline**: a template, a set of line items with prices, a client, a view counter and an acceptance rate, joined to the draft itself. Questionnaires and RFPs have an owner in ResponseHub, and that is the inbound side; this is the outbound priced offer that follows the call.

## Limits, stated as limits

No published tool table, so the operation names above come from the vendor's own page and the submission rather than from a `tools/list` behind the 401, which means an integrator cannot count the tools before signing in. The scopes are `admin:read` and `admin:write`, a wide pair by the standards of this catalogue: a `write` grant here can change the priced body of a live proposal, so the same caution that applies to any broad scope applies double, because the object being written is a document another party is waiting on. It is one vendor's product, so a business that already runs Proposify, PandaDoc or Qwilr gets a second system rather than a layer over the first. And the trial clock starts when the account is created, not when the connector is useful.

## Frequently asked questions

### Can the assistant send a proposal on its own?

Not by design. The vendor's own transcript has the assistant stop at the draft and say it has not sent anything, and the acceptance of the proposal is a client action in the web app. That is the right boundary for a document that commits price, and it means the connector's most useful jobs are drafting and reading rather than transmitting.

### What can I ask once it is connected?

Three kinds of question, all from the vendor's page: draft a proposal from a named template for a named client with a described scope, change the line items or a section in a sentence, and report the pipeline: proposals sent, accepted, pending and viewed, with the acceptance rate and estimated pipeline value.

### Is this a CRM?

No. It carries the priced document and its acceptance state, which is the part of a deal a client signs. A CRM carries the relationship and the forecast, and a business usually runs both. What this connector adds is that the proposal no longer has to be assembled by hand from a template plus a memory of last month's price.

### How does it compare with the signature connectors here?

Those take an existing document and return a signature. This creates the document that gets signed, prices it from a template, and then tracks whether it was opened and accepted, which is the step before the signature rather than a replacement for it.
