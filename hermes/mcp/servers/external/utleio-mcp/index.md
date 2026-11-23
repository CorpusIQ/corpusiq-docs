---
title: "Utleio MCP - Norwegian Landlord Rent Ledger"
description: "A Norwegian rental platform for landlords, measured to its OAuth gate: tenancy, invoice and deposit tools in Norwegian, plus the law behind the calculators."
category: "Finance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-23
source: "Submission chatmcp/mcpso #7912 filed 2026-11-23T17:19:15Z; registry record no.utleio/utleio 1.0.0 published 2026-11-23T17:13:12Z; a keyless initialize on https://utleio.no/api/mcp answering 401; the protected-resource document and the authorization-server metadata, both read 2026-11-23; the vendor pages utleio.no/ai and utleio.no/priser; lovdata.no for LOV-1999-03-26-17"
relevance: "★★★"
tags: [real-estate, rental, landlord, tenancy, norway, property-management, invoicing, oauth, remote-mcp]
last_updated: "2026-11-23"
---

# Utleio MCP

**A Norwegian landlord's month is a stack of small legal decisions: which rent invoice is overdue, how much of the deposit may legally be held, whether the rent may be regulated this year and by how much.** Utleio is a Norwegian rental platform for private landlords and companies, and its MCP endpoint exposes the landlord's own tenancies, invoices, overdue payments, deposits, expenses and finances to an assistant, with every outgoing action staged as a proposal the landlord confirms.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://utleio.no/api/mcp
Auth:        OAuth 2.1 against a Supabase authorization server; the landlord grants an app access to one area
Registry:    no.utleio/utleio 1.0.0, published 2026-11-23T17:13:12Z
Pricing:     Enkel 79 kr per tenancy per month, Pro 199 kr per month, read 2026-11-23
Tools:       named by the vendor, not readable without an account (see below)
Language:    tool names and descriptions are Norwegian
```

## What the gate says, measured

An anonymous `initialize` on `https://utleio.no/api/mcp` answers **HTTP 401** with a complete challenge and a plain JSON body:

```
WWW-Authenticate: Bearer
  resource_metadata="https://utleio.no/.well-known/oauth-protected-resource/api/mcp",
  error="invalid_token", error_description="Logg inn med Utleio"

{"error":"invalid_token","error_description":"Logg inn med Utleio"}
```

Three details are worth recording because most gates get them wrong. The body is **plain JSON and not JSON-RPC**, so a client that only renders `content` blocks shows the operator nothing at all. The `WWW-Authenticate` header carries the resource-metadata URL, which is the spec-correct discovery path and the reason a standards-following client can connect without any vendor documentation. And the description is in **Norwegian**, in the refusal itself, which tells you who the product is for before any tool list would.

`tools/list`, `ping` and a bare `GET` on the same path all answer the same **401**, so the surface is closed uniformly rather than leaking a tool inventory through one unguarded method.

## The OAuth chain, end to end

`https://utleio.no/.well-known/oauth-protected-resource` answers **200**, and the same document is served at the suffixed route `/.well-known/oauth-protected-resource/api/mcp`:

| Field | Value |
| --- | --- |
| `resource` | `https://utleio.no/api/mcp` |
| `authorization_servers` | `["https://beqpyarshyikeikuxkae.supabase.co/auth/v1"]` |
| `scopes_supported` | `openid`, `email`, `profile` |
| `bearer_methods_supported` | `header` |
| `resource_name` | `Utleio` |
| `resource_documentation` | `https://utleio.no/dashbord/innstillinger/integrasjoner#ai-apper` |

The named authorization server publishes a full RFC 8414 document at `https://beqpyarshyikeikuxkae.supabase.co/auth/v1/.well-known/oauth-authorization-server`, also **200**:

| Field | Value |
| --- | --- |
| `issuer` | `https://beqpyarshyikeikuxkae.supabase.co/auth/v1` |
| `authorization_endpoint` | `/auth/v1/oauth/authorize` |
| `token_endpoint` | `/auth/v1/oauth/token` |
| `registration_endpoint` | `/auth/v1/oauth/clients/register` (dynamic registration) |
| `grant_types_supported` | `authorization_code`, `refresh_token` |
| `code_challenge_methods_supported` | `S256`, `plain` |
| `token_endpoint_auth_methods_supported` | `client_secret_basic`, `client_secret_post`, `none` |

**The scope model is the interesting part, and it is unusual.** The only scopes offered are OIDC identity scopes: `openid`, `email`, `profile`. There is no `rent:read` and no `invoices:write`, so a token from this issuer says *who the landlord is* and says nothing about *what the app may touch*. The authorisation boundary lives one level up, in the landlord's own choice of which area the AI app is granted, which the submission states and the protected-resource `resource_documentation` points at. That is a legitimate design and a different one from the scoped-token servers in this catalog, such as [Koop](/hermes/mcp/servers/external/koop-mcp/) with its separate draft scope. An operator auditing an agent here should read the grant inside the Utleio dashboard, because the token will not tell them.

## The tool surface the vendor publishes

Eleven tools are named in the submission, all with Norwegian names. Translated, they cover the ledger and nothing speculative:

| Tool | What it covers |
| --- | --- |
| `hent_leieforhold` | the landlord's tenancies |
| `hent_fakturaer` | rent invoices |
| `hent_forfalte_fakturaer` | overdue invoices |
| `hent_okonomi` | the financial position |
| `hent_depositum` | deposits held |
| `beregn_indeksregulering` | index regulation of the rent |
| `beregn_markedsleie` | market rent estimate |
| `registrer_utgift` | register an expense |
| `foresla_send_faktura` | propose sending an invoice |
| `foresla_purring` | propose a reminder |
| `bekreft_forslag` | confirm a proposal |

The shape is the point: five read tools, two calculators, one write, and two proposal tools in front of a single confirmation. The vendor states that **nothing is sent or sealed without the landlord's approval**, and the tool naming supports it, since sending an invoice has a `foresla_` (propose) tool of its own and the actual dispatch is not a tool at all.

**The tool list itself was not read.** `tools/list` sits behind the same 401, so this table is the vendor's own vocabulary, and no response shape, error contract or rate limit was observed. A guide that lists tools it never saw is a brochure with a catalog number; the section above is what was actually measured.

## The Norwegian rules the calculators implement

Two tools exist because Norwegian tenancy law has arithmetic in it, and the law is public, so it can be quoted rather than paraphrased. Both checks below were read at Lovdata on 2026-11-23 from the Husleieloven, LOV-1999-03-26-17.

**Deposit, § 3-5.** A deposit may be agreed up to **the sum of six months' rent**, covering unpaid rent, damage, costs of moving out without notice, and other claims arising from the tenancy. It must be placed in a **separate account in the tenant's name** with ordinary interest terms at a financial institution entitled to offer the service in Norway, and while the tenancy lasts **neither party may dispose of the amount**. The tenant may demand the accrued interest paid out. The deposit may be agreed to change in step with changes in the rent.

**Index regulation, § 4-2.** Either party may demand the rent changed without terminating the tenancy, with three limits that bind together: (a) the change may not exceed **the change in the consumer price index** since the last rent setting, (b) it may take effect **at the earliest one year** after the last setting took effect, and (c) the other party must receive **written notice with at least one month's notice** before it takes effect.

**Market rent, § 4-3.** Once the tenancy has lasted at least **two years and six months** without other changes than those § 4-2 allows, either party may demand the rent set to the going rate for similar premises on similar terms, with a deduction for the value the tenant's own improvements created. That adjustment may take effect at the earliest **six months** after the written demand, and at the earliest **one year** after a previous change took effect.

That is why `beregn_indeksregulering` is not a spreadsheet convenience: the twelve-month floor, the CPI ceiling and the notice period are all conditions, and a landlord who breaks one has overcharged. The catalog had no Norwegian tenancy surface before this entry, so these are the first rules of this kind it carries.

## Pricing, as published

Read from `utleio.no/priser` on 2026-11-23, priced per **leieforhold** (tenancy), with the page itself stamped *Priser per 23. november 2026*:

- **Enkel** - **79 kr** per tenancy per month, or **49 kr** per month on annual billing. Dashboard, property register, market data, digital lease, move-in and move-out protocols, document folder, deposit overview, support.
- **Pro** - **199 kr** per month, one tenancy included. Adds **automatic KPI index regulation**, advanced tools, portfolio reports, an inkasso (collection) notice and package, full AI integration, priority support.
- **Bedrift Start** and **Bedrift Vekst** - quoted per portfolio, for 1 to 10 tenancies and upwards, with role management, CSV export, activity log and contract handling.

The MCP tools are stated to work **for areas with a paid Utleio subscription**, so the connector is not a separate line item on this page; the subscription is the gate. Note also that automatic index regulation is a **Pro** feature, which is exactly where the § 4-2 arithmetic becomes software rather than a manual check.

## Who is behind it

The organisation number published in the submission, **932 746 174**, resolves in the Enhetsregisteret to **DANIEL HARTOLD KAPITAL**, an *enkeltpersonforetak* (sole proprietorship) registered **2024-01-02** in Kristiansand under NACE **62.100** (computer programming). That is public registry data and it is written here because procurement reads it: a Norwegian landlord contracting for a tenancy ledger is contracting with a sole proprietorship, not with an AS.

## How to connect

The handshake is standard enough that a compliant client needs no vendor instructions: the 401 names the protected-resource document, that document names the Supabase authorization server, and that server offers dynamic client registration with PKCE. In practice:

1. Add the server as a remote MCP endpoint at `https://utleio.no/api/mcp` in a client that implements OAuth 2.1 (Claude Code's `/mcp`, for example).
2. Complete the sign-in, then choose **which area** the app is granted in the Utleio dashboard. This is the real permission boundary, not a scope.
3. Start with the read tools. `foresla_send_faktura` and `foresla_purring` stage drafts, and `bekreft_forslag` files one, so the first month should be watched rather than delegated.

## What this guide can and cannot certify

Measured: the endpoint, the 401 with its challenge, both metadata documents, the registry record, the published pricing, the tool vocabulary and the statutory rules the calculators serve.

Not measured: any tool response, any error contract, whether the calculators apply the CPI figure themselves or take it as an argument, and whether `hent_depositum` returns the six-month ceiling as a check or only the balance. Those are the four questions to ask of the first response, and a reader who needs them should connect an account rather than trust a description.

## Verdict

**The first Norwegian landlord-operations entry in this catalog, and the first tenancy ledger.** Three stars, and the missing two are about evidence rather than quality: every tool sits behind an account, so the gate, the metadata and the law are certified and the arithmetic in the calculators is not. A Norwegian landlord already paying for Utleio gets a useful assistant surface from this; anyone else should read the pricing page first, because the connector is only as available as the subscription behind it.
