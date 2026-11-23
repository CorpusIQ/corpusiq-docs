---
title: "wapi.kz MCP - WhatsApp Leads Priced Back to the Ad"
description: "A Kazakhstan WhatsApp business server that ties each chat to the ad or link that produced it, then rolls chats up into sales and cost per lead."
category: "Marketing & Customer Communication"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-23
source: "The mcp.so submission queue entry #7910 filed 2026-11-23T16:53:56Z and the registry record `kz.wapi/whatsapp`; a keyless initialize and tools/list on `https://wapi.kz/api/mcp` that answered 200 with 28 tools and an in-band credential refusal on tools/call; and the Russian-language tool descriptions read from the live tools/list"
relevance: "★★★★"
tags: [whatsapp, meta-ads, attribution, lead-tracking, crm, kazakhstan, marketing, remote-mcp, tenge]
last_updated: "2026-11-23"
---

# wapi.kz MCP

**Most businesses can name the ad that ran and the sale that closed, and cannot join the two.** wapi.kz is a Kazakhstan WhatsApp business service that puts the join in the protocol: every chat carries the ad id, the tracking link, the utm and the fbclid that produced it, and one analytics tool rolls the spend, the chats and the won deals into a single line per campaign.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://wapi.kz/api/mcp
Server:      wapi.kz 0.5.0, protocol 2025-06-18
Auth:        Bearer API key from the vendor cabinet, or the OAuth path for the app
Tools:       28 (listed keyless; every tools/call refused without a key)
Pricing:     330 KZT per connected number per day, first day charged on add
Registry:    kz.wapi/whatsapp 0.5.1 (endpoint serves 0.5.0)
Language:    all 28 tool descriptions are in Russian
```

## The gate is open for discovery and closed for execution

`initialize` and `tools/list` answer **200** with no credential, which is what makes this entry describable at all: 28 tools with full JSON schemas and long, unusually practical descriptions. Then `tools/call` refuses in band:

```json
{"jsonrpc":"2.0","id":100,"result":{"content":[{"type":"text",
 "text":"Нужен заголовок Authorization: Bearer *** ... ключ выдаётся в кабинете wapi.kz/app/api."}],
 "isError":true}}
```

Translated: the Authorization header is required, and the key is issued in the vendor cabinet at wapi.kz/app/api. So this is the **discovery-open, execution-gated** tier - a measured tool list, a measured refusal, and no invented tool behaviour. The registry record reads **0.5.1** while the endpoint identifies itself as **0.5.0**, which is recorded as drift rather than reconciled.

## The model is not the Cloud API

This is the second WhatsApp entry in the catalog after Meta's own Business MCP, and the difference is structural rather than commercial. Meta's entry drives the **WhatsApp Business Cloud API**. wapi.kz connects a number as a **linked device**, which is the same path a phone uses: the server calls it подключается как «связанное устройство», and `connect_number` takes either a pairing code in the form `ABCD-EFGH` (open WhatsApp, Linked devices, Link with phone number, enter the code; at most four codes per ten minutes) or a QR image that lives about 20 seconds.

That matters to an operator for one reason: a linked-device connection keeps the number usable in the WhatsApp app itself, at the price of being a session rather than an API contract. The tools confirm the trade - `get_limits` returns the day's send allowance and a **trust index from 0 to 100**, `check_number` is capped at **200 checks a day per number**, and `add_number` is refused until a human confirms.

## Attribution is the product

Four tools do the thing most operators cannot do by hand:

| Tool | What it answers |
| --- | --- |
| `get_analytics` | Ad spend, then leads, then sales for a period, grouped by `campaign`, `adset`, `ad`, `source`, `link`, `day` or `device` |
| `list_leads` | First-time contacts with their source: `ctwa` carries Meta click-to-WhatsApp with `ad_id`, `adset_id`, `campaign_id` and the ad's own text and link; `link` carries the tracking link with utm, fbclid and gclid; `organic` is someone who simply wrote in |
| `get_link_stats` | Clicks, uniques, returning visitors, how many reached a chat, conversion percent, sales and revenue, clicks with no lead, median minutes from click to first message, and a bot count |
| `get_link_clicks` | Click-level rows with time, IP, country, region and city, device, OS, browser or app (Instagram, TikTok), utm, and which lead the click joined |

The join method is stated rather than implied: `match_method` is `hidden_code` when an invisible marker in the prefilled message survived, `visible_code` when a readable code did, and `time_window` when the person erased the text and a new chat inside **15 minutes** of the click is assumed to be the same person. `create_link` builds that prefilled text, and returns a `snippet` that reroutes a website's WhatsApp buttons through the tracking link with utm and fbclid attached.

## Meta ad control, with the vendor's own warning

Six tools reach into Meta: `list_ad_accounts` (with `capi_enabled`, so conversion feedback is visible), `list_ad_objects` (campaign, ad set and ad with both `status` and `effective_status`, the second being what is actually running), `set_ad_status`, `set_ad_budget`, `sync_ads` and `list_ad_changes`.

Two details argue for the vendor's seriousness. `set_ad_budget` carries this in its own description: **ВНИМАНИЕ: это тратит деньги клиента** - a budget increase immediately spends the client's money, change it only if the person asked or agreed, and the amount is in the account currency in normal units. And `add_number` without `confirm=true` changes nothing and returns the price and the balance, so the agent is instructed to ask the human first. A tool that refuses until confirmed is a better default than a confirm dialog in a UI the agent cannot see.

The money side is tenge: **330 KZT per day per active number**, charged from the first day and continuing until the number is deleted, with `get_balance` returning the balance, the daily debit and how many days it covers. A number that runs out of balance reads `paused`.

## Operational edges worth knowing

- **Message media links expire.** `get_messages` returns `media` with a URL that lives **15 minutes**; `get_media` issues a fresh one. An agent that logs a URL instead of the media loses it.
- **Exports are rate-limited.** `create_export` builds a ZIP in the background, no more than **2 at once and 10 a day**, and the finished archive lives **24 hours**.
- **Refusals are in Russian.** An English-speaking operator gets correct behaviour and a Russian error string; that is a usability fact, not a defect.
- **Webhooks are signed.** `set_webhook` delivers `message`, `message.out`, `message.ack`, `session.status`, `lead.created` and `lead.updated`, signed with `X-Wapi-Signature`.
- **A connected number is a session.** Reconnection is a first-class tool (`connect_number` doubles as reconnect) because linked devices drop.

## FAQ

### Is wapi.kz the same product as the Meta WhatsApp Business API?

No. Meta's Business MCP drives the Cloud API; wapi.kz attaches a number as a linked device and adds the attribution layer - ad and link joins, lead stages, sales values and cost per lead - on top of the WhatsApp session.

### Can I try it without paying?

The tool surface is readable with no credential, but every `tools/call` needs a key from the vendor cabinet. The product is priced per number per day in tenge, and `add_number` returns the price without changing anything unless `confirm=true` is passed, so a first look costs nothing and a connected number costs 330 KZT a day.

### Does it write to my Meta ad account?

Yes, and deliberately narrowly: pause or launch a campaign, ad set or ad, and change a daily or lifetime budget. Every change lands in `list_ad_changes` with the actor recorded, and the vendor's own description warns that a budget increase spends the client's money immediately.

### What happens when the agent is unsure which lead a click belongs to?

It says so. `match_method` distinguishes a hidden marker, a visible code and a bare 15-minute time window, so a `time_window` join is visibly weaker evidence than a `hidden_code` one, and the analytics can be read with that in mind.

## Verdict

**The attribution slice of the WhatsApp story, and the first Kazakhstan-specific marketing surface here.** Four stars on substance: 28 measurable tools, a priced unit an operator can compute against, and an attribution model that publishes its own weakest link instead of hiding it. The missing star is access - nothing executes without a vendor key, so the behaviour described here is the schema and the refusal, not a driven sale. Test the free cabinet key against `list_leads` for a week and compare its cost per lead with whatever the team currently reports by hand.
