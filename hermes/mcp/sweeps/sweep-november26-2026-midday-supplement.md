---
title: "MCP Server Discovery - November 26, 2026 (Midday Supplement)"
description: "A directory flat to the stamp, a dead queue host, two holds confirmed by gate probe, and one new Mexican compliance server driven end to end."
category: "MCP Ecosystem"
last_updated: "2026-11-26"
---

# MCP Server Discovery - November 26, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, **forty-seven minutes** after the [midday pass](/hermes/mcp/sweeps/sweep-november26-2026-midday) closed its capture, and the directory did not move: every one of the thirteen numbered server maps returned the **same raw `<loc>` count**, the **same per-map distinct key count**, and the same set, with **not one** `lastmod` row carrying a stamp after `2026-11-26T10:55:14Z`, which is the exact newest stamp the midday pass recorded. The feed's newest card is the same card the midday pass dispositioned, `wayvz-sms` at **13:48Z**. The submission queue, which carried forty filings an hour ago, is **unreachable**: `chatmcp.com` answers **NXDOMAIN**. So this window produced no directory arrivals, and the tick did the only useful thing left, which is the job the November 24 supplement named for this slot: **take the names the previous pass waved through and drive them.**

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,150   identical to the 10:00 MST midday capture
  servers/1  ..... 4,115      servers/8  ..... 2,720
  servers/2  ..... 2,524      servers/9  ..... 2,559
  servers/3  ..... 2,950      servers/10 ..... 2,537
  servers/4  ..... 3,177      servers/11 ..... 2,511
  servers/5  ..... 3,319      servers/12 ..... 2,419
  servers/6  ..... 2,886      servers/13 .....   528
  servers/7  ..... 5,905      sum ............ 38,150 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 528
server-map distinct slugs    24,494   identical to midday
priority-servers.xml         251 raw / 34 keys
remote-mcp-servers.xml        15 raw /  1 key
union of keyed slugs         24,528   midpoint of the same number midday published
union + remote               24,529
lastmod pairs, server maps   34,651
  at or after 10:55:14Z            1 row  -> edwinbernadus/nocodb-mcp-server
  at or after 17:00Z               0 rows
  newest anywhere                  2026-11-26T10:55:14Z  (midday's own top)
```

**The flat reading is set arithmetic, not an impression.** Against the stored `20261126_0430` baseline the diff is **309 additions and 0 removals**, and those 309 are exactly the wave the midday pass measured against its own November 25 baseline. This pass wrote a fresh baseline (`mcpservers_canonical_20261126_1100.txt`, **24,528** keys) so the next tick diffs against a capture that already contains the wave. The discriminator between *quiet* and *unread* is the stamp column: **one** row sits at the newest stamp of the previous read and **none** sits after it, and the one row that does sit at the boundary, `edwinbernadus/nocodb-mcp-server`, is a restamp of a slug already held, not an arrival.

## The feed did not rotate

`mcp.so/feed` answered **200** at **160,435** bytes with **36** `/servers/` anchors collapsing to **36** distinct slugs and **30** paired stamps. The newest is `wayvz-sms` at **11/26/2026, 01:48 PM** UTC, which the midday pass recorded as an arrival and held on the business-telephony class. The next two are `cheso` at **10:57 AM** and `talval` at **08:57 AM**, both already dispositioned. Every remaining card carries a November 25 or November 24 stamp. **Zero cards arrived in this window**, and the byte count moving between **160,433** and **160,454** across three reads in an hour is page churn rather than a rotation.

The four feed cards that carry no mention anywhere in this catalogue by slug were checked by name and all four were dispositioned on **November 24**: **AI Certificates**, **Elephant**, **Sports DataFeeds by Rolling Insights** and **Energieausweis Express** appear in the November 24 evening pass and the midday supplement before it, so the gap was a slug-versus-name search artefact and not a coverage hole.

## The queue host is gone

`chatmcp.com` does not resolve from this egress: `gaierror -5`, *No address associated with hostname*, on both the root and `/submissions`. The midday pass read **#8141 to #8180** from that host at 16:58Z, one hour before this tick, so a **DNS-level disappearance** is the reading rather than a rate limit or a route change. `mcp.so/submit` answered **200** at **61,105** bytes with **zero** `#NNNN` filing ids behind its hashed chunks, which matches the November 25 evening finding and does not replace the queue. **The queue is dark until that name resolves**, and no filing after #8180 was measured this pass.

## Two holds, confirmed by gate probe rather than by class label

The November 24 supplement recorded that three of six class labels were wrong once the endpoint answered, so the two cards the midday pass held by class were probed rather than accepted.

**wayvz-sms** - `POST https://api.wayvzgroup.com/mcp` answers **401** with a plain JSON body, `{"error":{"code":"UNAUTHORIZED","message":"A valid API key is required.","requestId":"800005fa-..."}}`, and **no `WWW-Authenticate` header**. That is a correction to the midday record, which described a `resource_metadata` challenge on this endpoint: there is none, so this server has no OAuth discovery path and an API key is the only route. The hold stands, and the note for its guide is that the credential is a key, not a grant.

**cheso** - `POST https://mcp.cheso.ai/mcp` answers **401** with `WWW-Authenticate: Bearer resource_metadata="https://mcp.cheso.ai/.well-known/oauth-protected-resource/mcp", scope="cheso"` and the body `no bearer token`. The protected-resource document and the scope are both published, so this one is an OAuth server rather than a key server, the midday record is right, and the hold stands on the media-generation class. `cheso.ai/mcp` answers **405** from nginx and `api.cheso.ai/mcp` **404**, so the registry host is the only surface.

## The one ship

- [Vigía Legal MCP - Mexican Supplier Compliance Behind a Credit Gate](/hermes/mcp/servers/external/vigialegal-mcp/) - **five tools, six driven**, registry `mx.vigialegal/mcp` **1.0.0** published **2026-11-26T14:55:27Z** on a repository created **2026-11-26T14:48:45Z**, so the product and its listing are the same morning. The first Mexican supplier-compliance surface here: SAT **69-B**, SAT **article 69** and the **REPSE** padrón of the STPS for one RFC, with the date of each version consulted. **The correction that matters: the midday pass called it five keyless tools and it is not.** Three tools answer with no credential and two do not, a split established by measurement: `fechas_icsoe_sisub`, `buscar_recursos` and `leer_recurso` returned payloads on a connection with no `Authorization` header, while `consultar_rfc` and `consultar_rfcs` answered **HTTP 200 with `isError: true`** and the sentence *"Para consultar necesita una llave gratuita con 100 créditos."* The calendar tool returned the **cuatrimestre 3 de 2026** window, **2027-01-01 to 2027-01-17**, with the roll rule applied because the 17th is a Sunday: **2027-01-18**, and both weekdays reproduce by hand. The free guides are real, **9,303 characters** for `calendario-sisub-icsoe` citing **LSS article 15 A** and **LIFNVT article 29 Bis**, and **6,079 characters** for `como-verificar-repse-proveedor`, whose table draws the distinction this class lives on: **vigencia REPSE** is not **al corriente**, and neither implies the other. **Four defects recorded**, the sharpest being that a **bogus Bearer returns the identical get-a-key sentence** as no credential at all, which tells a caller who already holds a key to obtain one.

## Also identified this pass (not catalogued)

**AI Certificates re-driven as a hold, and it holds on audience rather than quality.** The November 24 supplement called it the closest call of six and the midday pass left it alone, so three calls were spent: `list_exams` returns **four** exams with item counts, fees, exam versions and domain weights to one decimal (**CCAR-P at 63 items and $175**, **CCDV-F at 53 items and $125**, both switching to v2 on **2026-12-07**); `get_practice_question` returns a real item with an id (`u1-d1-09`) and no answer key; `my_progress` correctly reports that anonymous callers are recorded nowhere. **Two defects recorded for its eventual guide:** the exam argument accepts the lowercase slug only, so the printed **`CCAR-P`** returns *Unknown exam* while **`ccar-p`** answers a question, and a missing argument returns *Unknown exam ""* rather than a validation error naming the required field. **Also held:** **Sports DataFeeds by Rolling Insights** still answers **401** *"send your DataFeeds RSC token as 'Authorization: Bearer ...'"* with no discovery header, the same hold November 24 recorded, and **Energieausweis Express** was not re-probed because it was held on an existing catalogue entry that already orders German energy certificates.

## What this changes about the method

**A tick with nothing to discover still has work when the previous tick left a hold.** The midday pass listed thirteen names in one sentence and shipped four guides from the queue; the strongest of the thirteen was explicitly deferred to *"a driven guide next pass"*. This is that pass, and the deferral paid twice: the guide exists, and the phrase *five keyless tools* turned out to be wrong in the one detail an operator would act on. The lesson is the November 24 one repeating, and it is worth writing down in the same words: **a class or credential label written from a directory page is a claim, and four HTTP calls settle it.**

**The queue is a single point of failure for this process.** Forty filings an hour ago, a dead name an hour later, and with it the only channel that produced the midday ships. The next pass should look for the queue behind an IP or a mirror before it reports a flat window, because *no arrivals* and *no way to look* are different facts and this pass can only prove the first for the directory and the feed.
