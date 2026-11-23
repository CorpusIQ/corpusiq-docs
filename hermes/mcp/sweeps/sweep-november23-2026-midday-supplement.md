---
title: "MCP Server Discovery - November 23, 2026 (Midday Supplement)"
description: "An hour in which the directory did not move and the feed did not change a single card, so the whole window was one queue arrival worth a guide."
category: "MCP Ecosystem"
last_updated: "2026-11-23"
---

# MCP Server Discovery - November 23, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed on a capture stamped **17:00:40Z**. The canonical added and removed nothing, the mcp.so feed returned the same twenty-seven cards as the 17:01Z read, and the submission queue carried exactly one arrival. That arrival earned the hour.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,535   against 37,519 at the 17:00:40Z midday capture (+16)
  servers/1  ..... 4,156     servers/7  ..... 5,857     sums to 37,535 exactly
  servers/2  ..... 2,527     servers/8  ..... 2,741
  servers/3  ..... 2,943     servers/9  ..... 2,619
  servers/4  ..... 3,232     servers/10 ..... 2,617
  servers/5  ..... 3,358     servers/11 ..... 2,515
  servers/6  ..... 2,939     servers/12 ..... 2,031
distinct keys, maps 1-12      23,612   against 23,612         (0 / 0)
union raw                     37,801   against 37,785
union normalised keys         23,647   against 23,647         (0 / 0)
priority-servers.xml            251 raw,  34 distinct keys
remote-mcp-servers.xml           15 raw,   1 distinct key (fifteen locale forms of one slug)
lastmod, server maps          33,999 stamped pairs; ZERO rows at or after 17:00:40Z
mcp.so /feed                  200, 159,048 bytes, 34 anchors, 30 stamps, 27 paired cards
                              NONE above the cutoff; identical to the 17:01Z read
submission queue              #7912 only, filed 17:19:15Z
```

## A raw rise and a key set that did not move

**37,535** raw `<loc>` entries against **37,519** is **+16**, spread across seven maps that rose by one or two entries and `servers/5` (+16), with `servers/12` falling **9**. The per-map block sums to the stated total exactly. The distinct key set on the twelve-map basis is **23,612 on both captures**, and on the union basis **23,647 on both**, at the same URLs-per-key ratio.

So the correct reading of the hour is: sixteen rows re-served under forms that normalise to keys the index already had, and **0 additions, 0 removals**. The `lastmod` scan agrees independently: **33,999** stamped pairs across the server maps, and **zero** rows at or after the **17:00:40Z** cutoff, the newest stamp anywhere on the surface being **2026-11-23T11:19:12Z**.

The `/all` pages were not re-read: the surface has answered **403** by edge policy since 4 November.

## The feed did not change

**200** at **159,048** bytes against **159,050** at 17:01Z, **34** server anchors, **30** stamps. Pairing each anchor with its stamp in document order returns **27** cards on both reads, and the two lists are identical slug for slug and stamp for stamp, newest `scrumpy` at **16:16Z**. A two-byte difference between two reads of the same page is a render artefact, not a publication.

This is what a flat hour looks like on the push surface: not an empty feed, but the same feed, which is a different and stronger statement.

## Where the material came from

The submission queue. `chatmcp/mcpso` carried **#7912** only, filed at **17:19:15Z** by the vendor, six minutes after the official registry published `no.utleio/utleio` **1.0.0** at **17:13:12Z**. Registry first, submission second, endpoint named in both: that agreement is what makes the endpoint identity certain, and it is worth saying when a vendor does the listing work properly.

## Shipped: one, at the documented tier

### Utleio - the first Norwegian landlord ledger here

Submission **#7912**, `https://utleio.no/api/mcp`, registry `no.utleio/utleio` **1.0.0**, OAuth 2.1, eleven tools named by the vendor, none readable without an account.

What was measured, and it is a complete handshake chain rather than a 401 alone:

- `initialize`, `tools/list`, `ping` and a bare `GET` all answer **401** with `WWW-Authenticate: Bearer resource_metadata="https://utleio.no/.well-known/oauth-protected-resource/api/mcp", error="invalid_token"` and the Norwegian description *Logg inn med Utleio*. The body is **plain JSON, not JSON-RPC**, which is the detail that decides whether an operator sees an explanation.
- The protected-resource document answers **200** at the bare route and at the suffixed route, naming the resource, a Supabase authorization server, `bearer_methods_supported: header`, and three scopes that are **OIDC identity scopes only**.
- The authorization server publishes a full RFC 8414 document, **200**, with dynamic client registration, authorization code plus refresh, and PKCE **S256**.

The scope model is the finding worth carrying: there is no resource scope at all, so the token says who the landlord is and the permission boundary is the **area** the landlord grants inside the Utleio dashboard. An operator auditing an agent here has to read the dashboard grant, because the token will not describe it.

Two more things this entry measured that a vendor page would not have given: the pricing ladder read off the vendor site on the day (**Enkel 79 kr** per tenancy per month, **49 kr** on annual billing; **Pro 199 kr** per month with one tenancy and automatic KPI regulation) and the Norwegian statutory rules the two calculator tools serve, quoted from Lovdata rather than paraphrased: the **six-month** deposit ceiling in § 3-5, the CPI ceiling, the **twelve-month** floor and the **one-month** written notice in § 4-2, and the **two years six months** threshold in § 4-3. A landlord tool whose whole value is legal arithmetic is best judged against the law, and the law is public.

The organisation number in the submission, **932 746 174**, resolves in the Enhetsregisteret to an *enkeltpersonforetak*, which is recorded in the guide because procurement reads it.

Full guide: [Utleio MCP - Norwegian Landlord Rent Ledger](/hermes/mcp/servers/external/utleio-mcp/).

## Dispositions

**Nothing else arrived**, so there is no hold list to carry: the twenty-three items held by the midday pass stand unchanged, and no feed card or canonical slug in this window required a new verdict. One candidate was considered and recorded rather than shipped, on the standing rule that a slug alone is not a product: **#7912** was triaged first against the catalogue for landlord, rental and tenancy surfaces, and the nearest neighbours are all a different job - [Tenantback](/hermes/mcp/servers/external/tenantback-mcp/) audits a tenant's CAM reconciliation, [LucidRents](/hermes/mcp/servers/external/lucidrents-mcp/) reads US public property records, [Hercules](/hermes/mcp/servers/external/hercules-property-mcp/) serves US investor leads - so the Norwegian tenancy ledger is a new slice and not a duplicate.

## What this hour does not prove

A flat canonical and a flat feed in a one-hour slot is a weak test of the directory, because one hour is shorter than most publish cycles. The claim this page makes is bounded: **between 17:00:40Z and 18:00Z the index added no key and the feed published no card**, and the only arrival was a vendor filing its own registry record. The next six-hour pass carries the real window.
