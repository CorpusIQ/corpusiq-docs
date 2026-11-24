---
title: "MCP Server Discovery - November 24, 2026 (Midday Supplement)"
description: "One hour after the midday pass, one new card and twelve new keys. Three of the four guides reverse a one-line hold the earlier pass took without probing."
category: "MCP Ecosystem"
last_updated: "2026-11-24"
---

# MCP Server Discovery - November 24, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, **one hour** after the midday pass closed its capture at **17:00Z** and shipped three from the queue. A one-hour window is a flat window, and this one was: **57** fewer raw entries, **twelve** more keys, **eighteen** restamped rows and **one** new feed card. The material came from somewhere else entirely. The midday pass read six products off the feed in a single line each and **held all six**; this pass drove four of them to their gates, found every one of them verifiable, and catalogued them. Three of the four guides below are **reversals of a hold taken an hour earlier**, and the reversal is the finding.

## The window, measured

```text
mcpservers.org /sitemap.xml   sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12         37,599   midday capture 37,656  (-57, composition)
  servers/1  ..... 4,129     servers/7  ..... 5,878
  servers/2  ..... 2,527     servers/8  ..... 2,739
  servers/3  ..... 2,945     servers/9  ..... 2,606
  servers/4  ..... 3,200     servers/10 ..... 2,575
  servers/5  ..... 3,290     servers/11 ..... 2,509
  servers/6  ..... 2,891     servers/12 ..... 2,310     sum 37,599 exact
distinct keys, maps 1-12     23,906   midday 23,894  (+12)
URLs per key                 1.573    midday 1.576
priority-servers.xml         252 raw, 34 distinct keys   (unchanged)
remote-mcp-servers.xml       15 raw, 1 key in fifteen locale forms  (unchanged)
lastmod, server maps         34,152 stamped rows; midday 34,203
  at or after 17:05Z         18 rows -> 18 distinct keys
  newest stamp anywhere      2026-11-24T17:53:49Z
mcp.so /feed                 200, 160,408 bytes, 36 anchors, 30 stamps
  above the 17:00Z cutoff    ONE (codixio-api, 17:12Z)
submission queue             #8002 - #8004, three filings 17:26Z to 17:46Z
```

**The composition moved again and the keys still rose.** The raw count fell **57** against the midday capture with a per-map block that sums exactly, the ratio fell from **1.576** to **1.573**, and the distinct key set rose by **twelve**. Eighteen keys were restamped inside the window, so the additions sit inside that set rather than arriving as a clean list. Sixteen of the eighteen have no counterpart in the guide tree or the catalogue index, and reading the names explains why none became a guide: `usezn/zn`, `asobeast/asobeast`, `leeswallow/stickypane`, `knaisoma/data-olympus`, `retyc/retyc-cli`, `frankshan001/cutvoke` and `akzar1el/god-prompt-mcp` are single-author repositories with no product page the sitemap points at, and `daniel3303/equibles` is already catalogued as `equibles-mcp`. The one recognisable name in the batch, `deephaven/deephaven-mcp`, arrives in the analytics-database class this catalogue already covers. A twelve-key rise in one hour is worth printing and does not have to be worth a page.

**One card, and it was the good one.** The feed came back **389 bytes smaller** than the midday read with the same **36** anchors and **30** stamps, and exactly **one** card sits above the window: **codixio-api at 17:12Z**. The midday pass read that card and put it in a held list. It is the only new arrival in this window that deserved a guide, and it got one.

**Three queue filings, none probed.** **ClaimTrace** (#8002, 17:26Z), **Graspful** (#8003, 17:28Z) and **Geo Govoy** (#8004, 17:46Z) arrived after the midday pass closed. All three are recorded as carried rather than evaluated: two local-package filings with no remote endpoint to probe inside the hour, and one Spanish municipal data surface adjacent to the public-records class this catalogue already carries.

## Shipped (4 guides: one arrival, three reversals)

**Codixio** is the arrival. **ZeroBounce**, **Persado** and **Figment** are the reversals, and the midday pass's own words are the record of what was held:

> *From the feed: **figment-mac-hosting** on mac hosting, **zerobounce** on the **MailTester** email-verification trio, **vibecode** (and its queue twin **#7993**) on app builders, **fatesign-bazi** as an astrology vertical, **ai-certificates** as exam preparation and **persado-mcp** on marketing copy generation.*

Four class labels, four products, no probe. This pass probed.

- [Codixio MCP - E-Invoices, Tariff Codes, Localization](/hermes/mcp/servers/external/codixio-mcp/) - the window's one card, **17:12Z**. Keyless `initialize` refuses **401** on `/mcp` **and** on all three per-service routes with `{"error":"unauthorized"}` and **no `WWW-Authenticate`**, so no discovery document exists to read; the documented path is OAuth 2.1 with the client registering itself. The tool list comes from the vendor's `llms.txt`: `localize_listing`, `suggest_tariff_code`, `get_job_result`, `validate_einvoice`, `create_einvoice`, `get_balance_and_quota`, split across four endpoints so the permission boundary is an **address chosen at connect time**. Per-call pricing from prepaid credit: **0.10 EUR** for an e-invoice checked by the official **KoSIT** validator, **1.50 EUR** for a CN/TARIC code, **9.90 EUR** for a marketplace listing rewrite, **10.00 EUR** minimum top-up, Polar as merchant of record, no subscription. The published ceiling is the reason to trust the rest: tariff confidence is **`high` only for German descriptions** and caps at `medium` with `confidence_capped_language` everywhere else, and every localization response states the marketplace rules it applied **with source and date**.
- [ZeroBounce MCP - Email Validation Inside the Assistant](/hermes/mcp/servers/external/zerobounce-mcp/) - held by the midday pass on "the MailTester email-verification trio". The class was real and the verdict was wrong: this is the **vendor's own server**, not a wrapper, and it ships as **`@zerobounce/mcp` on npm under MIT** with names and annotations held identical to the hosted endpoint. Keyless `initialize` is **401 invalid_token** with no `WWW-Authenticate`; the hosted path is an account sign-in with **no API key in the client config**, and the self-hosted path is the escape for clients that cannot open a browser. Every tool carries `readOnlyHint`/`destructiveHint` and states whether it **spends credits** or **changes the account**, and the README names the two endpoints the vendor **deliberately does not expose**: the Inbox Placement webhook, because it applies to the whole API key, and the Warmup SMTP test, because it takes the mailbox password. Pricing read the same day: **$39 for 2,000 addresses** as the minimum purchase, **ONE at $99 a month with 10,000 credits**, **one credit per validation**, **20 per successful Email Finder query**.
- [Persado MCP - Score Marketing Copy Before You Send](/hermes/mcp/servers/external/persado-mcp/) - held on "marketing copy generation", which undersells it: it does not generate, it **scores**, 0 to 100, with the elements moving the score named, then ranks rewrites by predicted lift. The chain is the most complete of the four: **401** with `resource_metadata` and `scope="openid offline_access mcp:tools"`, one permission scope on the protected-resource document, and an RFC 8414 document from a **Keycloak** realm (`myaccount.persado.com/realms/persado-portal`) with authorization code plus refresh, **PKCE S256**, a registration endpoint at `api.persado.com/register` and **`none`** client auth. Two hosts, one chain, and the issuer is not the host a client connects to, which is the detail that costs an integrator an afternoon. **14-day trial, no card**; brand voice and the **20+ regulatory frameworks** are labelled **Enterprise**, so the trial is not an evaluation of the compliance controls, and the tool schema is unreadable without an account.
- [Figment MCP - A Mac Rented by the Hour, Ordered by an Agent](/hermes/mcp/servers/external/figment-mcp/) - held on two words, "mac hosting", for the least classifiable entry of the day. It is the only **keyless 200** in this window: `initialize` names `figment-mac` **1.0.0**, `tools/list` returns **eight** tools, and `figment_get_offer` was driven live to `offer_version mac-offer-2026-11-17` with three plans priced in cents, **$0.15/hour Intel VM**, **$0.40/hour shared M4 Pro**, **$1.00/hour dedicated M4 Pro**. The reason it belongs in this catalogue is not the hardware, it is the **money loop**: `create_account` is keyless and returns an `api_key` once, `buy_credit` returns a **Stripe Checkout link a person pays**, the first purchase is **$25**, hourly billing runs **by the minute** and stops **only on the stop call** because *"a guest shutdown alone does not stop charges"*, and the structural ceiling is **two running Macs per account** on prepaid credit. Two error paths driven with a fabricated id both refused **in band** with `isError: true` and a message naming the missing header.

## Why a hold from an hour ago was overturned

The catalogue's own rule is that a name in an "also identified" list with no heading and no guide directory is a **prior disposition**, and the default is to skip it rather than catalogue it. That rule exists to stop a pass re-litigating yesterday's decisions. It does not make a one-line hold **evidence**, and the difference showed up four times in one hour.

Every hold in that sentence was a **class claim** made without a probe: "on mac hosting", "on the MailTester trio", "on app builders", "on marketing copy generation". Three of them were also the wrong class once the endpoint answered. Figment is not hosting in the shared-server sense, it is an agent-purchasable machine with a prepaid balance and a Stripe link a human pays. ZeroBounce is not a third wrapper in a trio, it is the official server with its own npm package and a published list of endpoints it refuses to expose. Persado does not generate copy, it predicts response to copy you already wrote. A class label is cheap; a gate probe is four HTTP calls.

What this pass did **not** overturn is as important. **Vibecode** still holds: `{"error":"Sign in to Vibecode to continue."}` with no `WWW-Authenticate` and no discovery document, an app-builder class this catalogue already carries, and nothing measurable before an account. **FateSign BaZi** still holds as a single-tool novelty vertical, even though it answered keyless and refused two malformed calls correctly with `place_required` and `invalid_gender`. **AI Certificates** still holds, and it is the closest call of the six: five keyless tools, a real dataset (**CCAR-P at 63 items and $175**, **CCDV-F at 53 items and $125**, exam versions switching on **2026-12-07**, domain weights to one decimal) and a named author with a stated score. It holds on **audience**, not quality: exam preparation for certification candidates is adjacent to the operator this catalogue is written for, and the listing monetises through Udemy referral links. A hold with a stated reason is a decision; a hold without one is a deferral, and only the second kind deserves another pass.

## What this changes about the method

**A one-hour window cannot produce four arrivals, so a supplement that ships four has to say what it is shipping.** One of these is new in the window. Three are old material verified properly. Presenting all four as discoveries would be the easiest lie in this process to tell and the hardest to catch, because every guide is real and every endpoint answered.

**The supplement tick's job is to verify, not to discover.** The midday pass spent its hour on the queue and got three solid ships; the feed's six cards went into a sentence. The 11:00 tick has no queue to clear and no directory movement to measure, which leaves exactly one useful thing to do: take the names the previous pass waved through and drive them. Four of six reversed, which is a rate worth reporting to whoever writes the class labels.
