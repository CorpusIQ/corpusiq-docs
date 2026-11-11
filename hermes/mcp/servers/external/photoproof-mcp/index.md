---
title: "photoproof MCP - Client Proofing for Photographers"
description: "OAuth-gated galleries where a client selects, rejects and confirms, with Lightroom paste codes and full-resolution delivery"
category: "Business Operations"
stars: "n/a (hosted, OAuth 2.1, free plan includes proofing and delivery)"
added: 2026-11-11
source: "the mcp.so submission #7133 for photoproof.io, the official registry record io.photoproof/mcp 1.0.0, the endpoint at https://photoproof.io/mcp where a keyless initialize answered 401 with a resource_metadata challenge, both OAuth metadata documents read in full, and the vendor llms.txt and feature pages for product facts and plan pricing checked 2026-11-11"
relevance: ★★★
tags: [photography, proofing, client-selection, galleries, lightroom, delivery, smb, creative, oauth, pkce, streamable-http, remote-mcp]
last_updated: "2026-11-11"
---

# photoproof MCP

**A photographer's client does not want a gallery, they want to get to the end of choosing.** Most gallery products are built to sell prints, so the selection step sits inside a shop; this one is built to collect picks and stop. The MCP server puts the same question in front of an assistant: what is still unconfirmed, what did this client reject, and what are the file codes I paste into Lightroom.

```text
Server type:   Remote (Streamable HTTP)
Endpoint:      https://photoproof.io/mcp
Auth:          OAuth 2.1, authorization code with PKCE (S256), dynamic registration
Scopes:        galleries:read, galleries:write
Registry:      io.photoproof/mcp 1.0.0
Discovery:     keyless initialize 401 with a protected-resource challenge; calls need sign-in
Operator:      xolqy.com, the team that builds and runs the service
```

## The gate, measured in two documents

A keyless `POST initialize` answered **401** with the challenge in the header rather than in a body:

```text
WWW-Authenticate: Bearer realm="OAuth",
  resource_metadata="https://photoproof.io/.well-known/oauth-protected-resource/mcp",
  scope="galleries:read galleries:write"
```

Following the named path returned the protected-resource document, and this is the part that saves a client from guessing:

```json
{"resource":"https://photoproof.io/mcp",
 "authorization_servers":["https://photoproof.io"],
 "scopes_supported":["galleries:read","galleries:write"],
 "bearer_methods_supported":["header"],
 "resource_name":"photoproof.io"}
```

The authorization-server metadata on the same host then completes the picture: `authorization_endpoint` `/oauth/authorize`, `token_endpoint` `/oauth/token`, `registration_endpoint` `/oauth/register`, `response_types` `code` only, `grant_types` `authorization_code` and `refresh_token`, token auth methods `client_secret_basic`, `client_secret_post` and **`none`**, `code_challenge_methods` **`S256` only**, a revocation endpoint, and the `iss` authorization-response parameter supported.

Two scopes in a read and write pair is the cleanest delegation story in this catalog: **a reporting assistant can hold `galleries:read` and never be able to create or change a gallery**, while the working assistant holds both. No wildcard scope, no account-wide token, and nothing in either document suggests a permission beyond galleries. The `none` token auth method and the registration endpoint together mean a client can onboard itself without a shared secret, which is what makes this usable from a personal assistant rather than only from a registered partner.

## What the assistant can actually do

The endpoint is gated, so the tool list is described from the vendor's own connector page and product documentation rather than from a `tools/list` this pass could read. The published capability is narrow and specific:

- **Ask about galleries in plain words** and get answers about what is in them, what each client picked, and what is still waiting.
- **Get the selected photo codes** so they can be pasted into Lightroom, which turns a client selection into a develop session without anyone retyping file numbers.
- **Create a gallery**, which is the write half of the scope pair.

The proofing model behind those calls is the product. A client opens one link, **selects, rejects or comments on each photo without creating an account**, and presses **Confirm** to lock the selection; the Confirm step is what turns a wish list into a deliverable, and it is the state an assistant should be reporting on. Galleries can carry a password, a **burned-in watermark**, a download lock and view tracking, and the delivery side takes **finals up to 4 GB per file** with single-file or ZIP download, where large sets are split into roughly 2 GB parts.

Plan shape, checked **2026-11-11** from the vendor's published pricing: **Free at 0 forever** with 2 GB, galleries expiring after 30 days and a small badge; **Gallery Pass 5 one-off per gallery** with 10 GB and 90 days; **Pro 8 per month or 72 per year** with 100 GB and custom expiry up to two years; **Studio 19 per month or 180 per year** with 500 GB; white-label on request. Prices are in euro with VAT included, there is **no commission on sales**, and every proofing feature is on every plan, which is the line that separates this from gallery products that meter the selection workflow.

### Why would an assistant need access to a photo gallery at all?

Because the expensive part of a photography business is the week between the shoot and the final selection, and it is a status question rather than an editing question. "Which of my clients have not confirmed yet" and "what did the wedding client reject" are answered today by opening galleries one at a time. The same reason applies on the client side: a selection that goes stale costs a reshoot or a re-edit, so an assistant that can see which galleries are still open is the cheapest possible reminder system.

## The honest boundary

This entry is recorded at the **OAuth evidence tier**: the handshake, the challenge, both metadata documents and the scope pair were read and reproduced above, and the tool names and product behaviour come from the vendor's own documentation, not from a `tools/list` this pass executed. That is the same tier used for other OAuth-gated entries in this catalog, and it is stated rather than blurred.

Two other items are worth naming as vendor statements rather than measurements. The submission says the assistant **only sees the account that authorised it**, which is consistent with a per-account token and a two-scope grant, but it was not tested. And a client-facing workflow claim, that a client never creates an account to select photos, is on the product's own pages and is the kind of claim only a real gallery would prove.

## Good for

A wedding, portrait or product photographer running a small studio who needs the status of client selections without opening each gallery, and who wants the picks in Lightroom file codes rather than as a list of thumbnails. A studio that hands a read-only connection to a reporting assistant while keeping writes on the working connection.

Not for: print sales, portfolio sites or stock licensing, which the vendor explicitly does not do; teams that need multi-user studio roles, since the scope pair is per-account; or anyone who needs a selection workflow without the Confirm step, because locking the selection is the point.

## Related in this catalog

- [Cotlet MCP - The Apps That Have No API](/hermes/mcp/servers/external/cotlet-mcp/) - the nearest neighbour in the catalog, which fronts SmugMug among hundreds of per-app connectors; SmugMug hosts portfolios and client galleries, while this is proofing only, with a confirming client and a Lightroom export code.
- [Milemarker MCP](/hermes/mcp/servers/external/milemarker-mcp/) - another single-profession operating surface where the assistant answers a status question about real client work.
- [Genaya MCP](/hermes/mcp/servers/external/genaya-mcp/) - the same two-scope discipline for a service business, with a confirm step between an assistant's intent and a client-visible change.
