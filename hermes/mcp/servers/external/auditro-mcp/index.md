---
title: "Auditro MCP - UAE ICV Scores and Emiratisation"
description: "OAuth-gated: In-Country Value scores, evidence gaps and MoHRE Emiratisation quotas, with the arithmetic on the server and the model only selecting records"
category: "Compliance / UAE Government Programmes"
stars: "n/a (hosted service; registry co.auditro/auditro 0.5.0)"
added: 2026-11-13
source: "the submission queue entry #7302, the official registry records at 0.2.0 and 0.5.0, a keyless handshake on this host that returned 401 with a protected-resource pointer, and the vendor's own MCP documentation page"
relevance: ★★★
tags: [icv, emiratisation, uae, compliance, mohre, procurement, oauth, mcp]
last_updated: "2026-11-13"
---

# Auditro MCP

**Two numbers decide whether a UAE company can win government work, and both are computed by someone else's rules.**

In-Country Value is the share of a contract's value that stays in the national economy, and a tender can be scored on it. Emiratisation is the quota of Emirati nationals in a private company's workforce, and a shortfall is a compliance event rather than a hiring preference. Both are calculated, both are auditable, and both are usually managed in a spreadsheet that one person maintains and nobody can reconstruct a year later.

Auditro's premise is that the calculation belongs on the server and the model should only choose which governed record to look at. Its MCP server is the surface: scores, gaps, evidence, action plans, fixed assets, suppliers and tenders, plus Emiratisation positions, read from a workspace the company already maintains.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.auditro.co/mcp
Auth:        OAuth 2.1 with PKCE and dynamic client registration; read-only by default
Server name: not readable keyless - initialize answers 401
Tools:       99 per the vendor's submission, 47 of them read-only (vendor-stated, not measured here)
Registry:    co.auditro/auditro 0.2.0 and 0.5.0 (0.5.0 latest)
Docs:        https://auditro.co/docs/connect-ai-tools/
Pricing:     no price on the MCP surface; an approved organisation and an active membership are required
```

## The evidence tier

This entry ships at the **OAuth tier**, and it says so rather than implying more. Measured on 2026-11-13 at 04:03Z from this host:

- `POST initialize` on `https://app.auditro.co/mcp` returned **401** with the body `{"error":"invalid_token","error_description":"Connect an authorized Auditro account."}`
- the response carried a correct challenge: `www-authenticate: Bearer resource_metadata="https://app.auditro.co/.well-known/oauth-protected-resource"`
- that document answered **200**: resource `https://app.auditro.co/mcp`, authorization server `https://app.auditro.co`, `bearer_methods_supported: ["header"]`, resource documentation `https://app.auditro.co/docs/mcp`, and **seven** scopes - `openid`, `email`, `offline_access`, `auditro:read`, `auditro:write`, `auditro:files`, `auditro:sync`
- the official registry holds **two** records under `co.auditro/auditro`, **0.2.0** and **0.5.0**, the later one describing itself as "UAE ICV compliance: governed scores, evidence gaps and actions with deterministic numbers"

Everything after this point about tools and behaviour is **the vendor's own documentation and submission text**, and is labelled as such. No tool was called, because every tool sits behind an account. The scope split is the one fact worth carrying: read and write are separate scopes, and files and sync are separate again, so a read-only connection is expressible rather than aspirational.

## Why This Matters for Operators

ICV is not a metric a company chooses to track. It is a scoring input in federal and many local tenders, and the difference between a certified ICV certificate and a self-assessed one is the difference between points awarded and points questioned. The arithmetic is not hard - local procurement, local wages, Emiratisation contribution, investment in fixed assets and a bonus for exports - but the evidence behind each line has to be a document somebody can audit, and the certificate cycle refreshes annually.

A model that recomputes a score in its head is worse than useless here: the number has to survive an auditor. The design Auditro states - every number calculated by the platform, the AI client only selecting governed records - is the correct one for this class of question, and it is the reason this entry is worth a file even at the OAuth tier.

Emiratisation adds a second, sharper edge: a quota position is a legal exposure with a deadline attached, and the difference between "we are at 6% against a required 7%" and "we are fine" is one governed record.

## What the vendor states it does

Across **99** tools, **47** read-only, in the categories the submission lists: ICV scores and score gaps, evidence, action plans, finance data, entities and certificates, Emiratisation quota positions, fixed assets and capex, suppliers and tenders. With full access it will update records and action plans, which is why the write scope is separate and why read-only is the documented default.

The connection flow in the vendor's own documentation is a model of what a governed remote server should say:

- Every AI tool uses the same address, and the app supplies its own name.
- The client must support remote Streamable HTTP, OAuth discovery and PKCE; a permanent token in a config file is explicitly discouraged.
- On the consent screen the user checks the account, the **organisation**, the app name and the callback destination.
- **Read-only is the default.** Full access appears only if the client requests additional permissions **and** the user's role allows them.
- The first call should be `get_workspace`, to confirm which organisation was actually connected.

One sentence in that documentation is worth quoting because almost no vendor writes it: *Auditro labels its identity unverified. Only continue if you started the connection in a client you trust.* That is an OAuth client-identity problem stated out loud by the party that would otherwise be its victim.

## The public surface beside the server

The documentation site's navigation carries an **ICV calculator** and an **Emirati hire calculator** as public pages, which is the cheapest way to see whether the programme arithmetic is explained the way you expect before you connect an account. That is where a business owner should start: run a real example through the public calculator, then decide whether the governed workspace is worth wiring up.

## Setting it up in Hermes

```bash
hermes mcp add auditro --url https://app.auditro.co/mcp
hermes mcp test auditro
```

The test will report the 401 - that is the handshake working, not a failure. Complete the OAuth login from the client (`/mcp` then choose Auditro in Claude Code, or the equivalent in your client), confirm the organisation on the consent screen, and ask for `get_workspace` before anything else. Grant `auditro:read` alone unless there is a reason to let an agent act.

```bash
claude mcp add --transport http --scope user auditro https://app.auditro.co/mcp
```

## Where this sits in the catalog

This is the **first entry in this catalog for In-Country Value and MoHRE Emiratisation**, and the search that establishes it is worth stating: no guide, heading or sweep note here mentions In-Country Value, ICV as a compliance score, MoHRE or Emiratisation. The nearest compliance neighbours are sanctions and payment screening (`mcp-sanctions`, QoreNext Trade Screening, Atlas Verified), the Peppol e-invoicing class, and the tax-deadline surfaces such as [Nishka](/hermes/mcp/servers/external/nishka-mcp/) - all of them adjacent to regulated money and none of them in UAE procurement scoring.

The class it belongs to is governed compliance arithmetic for a specific jurisdiction. That class is thin here and this is the first member: a national programme with a scoring formula, an audit trail and a certificate.

## Limitations recorded

- **Nothing below the handshake was measured.** Tool count, read-only count and the category list are the vendor's, not this pass's.
- An approved organisation and an active membership are prerequisites, so there is no free path to a first number through MCP.
- The server requires an authenticator app at sign-in; a connection is a two-device operation.
- The vendor marks the connecting app's identity **unverified**, and says so on its own consent screen.
- No pricing is published on the MCP surface. Procurement is a conversation, not a checkout.
- The registry carries two versions (0.2.0 and 0.5.0) and no changelog was read; the served version could not be observed behind the 401.
- ICV rules vary by emirate and by programme, and nothing in the public documentation promises which version of the formula a given workspace is scored against.

### Do I need an Auditro account to use it?

Yes. Every tool sits behind the OAuth flow, the workspace belongs to an approved organisation, and access follows the user's role inside that organisation.

### Can an agent change a score?

The scores are computed by the platform, and the submission states the client only selects governed records. Write access is a separate scope (`auditro:write`), read-only is the documented default, and the scopes are declared separately so a connection that only needs to read can be created that way.

### Is this useful outside the UAE?

Only for a company that tenders there or hires under MoHRE rules. The formulas are programme-specific - ICV for procurement scoring, Emiratisation for workforce quota - and neither transfers to another jurisdiction's compliance regime.
