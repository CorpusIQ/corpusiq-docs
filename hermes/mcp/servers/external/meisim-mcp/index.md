---
title: "MeiSIM MCP - Phone Lines an Agent Can Own"
description: "A hosted MCP server that rents real US mobile numbers to agents, reads their inbound texts, sends replies, and sells travel eSIM plans."
category: "Communication / Telecom"
stars: "0 (hosted Streamable HTTP at https://mcp.meisimusa.com/mcp, keyless handshake, sixteen tools of which six were driven with real data; account tools answer an in-band 401)"
added: 2026-11-17
source: "the mcp.so feed card meisim stamped 2026-11-17T17:27Z, the registry record io.github.Shauliko/meisimusa-mcp 0.3.5, and a driven session on 2026-11-17 in which twelve tools/call requests were run against the live endpoint with no credential"
relevance: ★★★
tags: [telecom, sms, phone-numbers, esim, agents, identity, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# MeiSIM MCP

**An agent that needs a phone number hits the same wall every time: the sign-up form wants a mobile number, and the number it can find is a virtual one that the site already blocks.** The other direction is worse. A business wants its agent to receive a text from a real customer, and a shared inbox is not a line.

MeiSIM is a US telecom reseller that put its catalogue behind an MCP server. The catalogue is two things at once: real US mobile lines on a national carrier, and travel eSIM data plans from several vendors. The part worth a page is not the price list. It is that this one states its own gate plainly, in the same response that sells the product: **a person opens the account, and the server says an agent cannot open one by itself.**

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://mcp.meisimusa.com/mcp
Server:        meisimusa-mcp 0.3.5, protocol 2025-06-18
Auth:          none for the catalogue; Bearer API key for the account tools
Tools:         16 (12 read only, 4 that spend money or send a text)
Listed on:     mcp.so feed, registry io.github.Shauliko/meisimusa-mcp
Local route:   npx -y meisimusa-mcp with MEISIMUSA_API_KEY
```

## The evidence tier

Keyless and driven, with the boundary measured rather than assumed.

`initialize` answered **200** with no credential, no session id issued, and serverInfo **meisimusa-mcp 0.3.5** on protocol **2025-06-18**. `tools/list` returned sixteen schemas. Twelve `tools/call` requests were then run: six returned live data without a key, and six returned the server's own refusal text.

That split is the useful finding of the pass. The catalogue is public. The account is not.

## The tool surface

Every tool carries a title, an output schema, annotations and an `execution.taskSupport` field, which is more of the current spec than most entries here declare.

| Tool | Argument | What it returns |
|---|---|---|
| `get_ai_line_offer` | none | The current offer for lines sold to agents: monthly price for texts, for texts plus voice, volume tiers, minimum term, delivery times |
| `search_us_numbers` | `max_price_usd` | Prepaid plans that come with a real US number: carrier, voice allowance, SMS allowance, price, term |
| `search_plans` | `country_code`, `duration_days`, `data_gb`, `sort_by` | Travel eSIM plans for a country: data, days, price, vendor, coverage |
| `get_quote` | `plan_id` | The plan plus a price breakdown and a short lived quote |
| `purchase` | `plan_id`, `customer_email`, `payment_method`, `billing_country`, `idempotency_key` | A hosted Stripe payment link, then the eSIM and its QR emailed to the buyer |
| `get_activation` | `order_id` | Install QR, activation (LPA) string, status |
| `topup_lookup` | `line_type`, `phone` or `carrier`, or `iccid` or `email` | Existing lines and the top-up products available for them |
| `topup_start` | `line_type`, `product_id`, `customer_email` | Order id and a payment URL for a recharge |
| `get_account` | none | Company, status, prepaid wallet balance, how many numbers may be activated today |
| `get_number_pricing` | none | What a new number costs on this account: daily rate, minimum days, activation fee, headroom |
| `buy_numbers` | `count` (1 to 50), `billing`, `days` or `months`, `voice`, `line_history`, `area_code`, `zip_code` | Numbers ordered from the prepaid wallet |
| `get_order` | `order` | Provisioning status and the numbers delivered |
| `list_my_numbers` | `search`, `limit`, `offset` | The numbers on the account with status, voice, billing and paid through date |
| `read_messages` | `number`, `since`, `limit` | Inbound texts, newest first |
| `wait_for_message` | `number`, `since`, `timeout_seconds` (max 50) | Blocks until the next text arrives and returns it |
| `send_message` | `from`, `to`, `message` (max 800 characters) | Sends a text from one of the account's numbers |

`wait_for_message` is the connective tissue an agent actually needs. A verification flow is not a read, it is a wait: send, then hold the line for the code. Every other tool here is a lookup or a purchase.

## What the offer is, in numbers

`get_ai_line_offer` answered without a key and priced the product in one response:

```text
texts only          35 USD per line per month
texts and voice     45 USD per line per month
10 lines            32 or 42
50 lines            29 or 39
200 lines           25 or 35
minimum term        2 months, paid up front, then monthly from the balance
```

The notes attached to that figure are the ones that matter for an integration:

- A **real US mobile number on a national carrier, not a VoIP number**. That distinction is the whole product. A VoIP number fails the verification step this is bought to pass.
- Inbound texts arrive at a webhook or over the API. Voice runs over SIP with the number as caller ID, **one call at a time per line**, and outbound calls to US numbers only.
- From stock, a number is delivered in **seconds**; a new number takes **minutes**.
- **An AI agent cannot open the account by itself.** The sign-up form carries a robot check, and the ID step needs a government ID plus a phone camera, or a review by a person at the vendor.

That last line is not a defect. It is the compliance posture of a telecom regulator being passed through to the client, and it is stated in the refusal text of every account tool rather than buried in a policy page. A team planning to let an agent buy its own identity should read the sentence before it builds the flow.

## The catalogue, measured

`search_us_numbers` with a price ceiling of 1000 returned **28 plans** across five carriers (AT&T Prepaid, LinkUp Mobile, MobileX, Moxee 2, T-Mobile), from **7.50** for a 30 day plan with 100 SMS and no data, through **10.00** for 100 minutes and 100 SMS, to **288**. Every row carried `includes_us_number: true`, which is the field that makes the list relevant here.

The price ceiling works, which is not universal in this category:

```text
max_price_usd 10    2 plans, highest price 10.00
max_price_usd 25    9 plans, highest price 21.00
max_price_usd 1000  28 plans
```

No duplicate `plan_id` values, no duplicate carrier and title pairs. The filter is ascending by price and it holds.

`get_quote` on the cheapest plan returned its own arithmetic, clean and addable:

```text
subtotal 7.50   taxes 0   fees 0   final 7.50 USD
quote_expires_at  2026-11-17T18:17:36.155Z
```

The quote window is **15 minutes**, measured twice. A plan bought from a stale quote is the failure this field prevents, so a purchase flow should re-quote rather than reuse an id from a previous turn.

## The eSIM side is an aggregator

`search_plans` for the same country returns plans from several suppliers, not only the house brand. Sampling Japan, France and the United States at 30 days and 5 GB gave **58**, **80** and **86** plans, with vendors including Airalo, Sparks, 3, Bouygues, NextLink, RoamVault, IIJ and MeiSIM itself. Cheapest Japan plan **5.99**, cheapest France **4.70**, cheapest US **5.99**.

A country with no plans answers an empty list and no error: a request for `AQ` (Antarctica) returned zero plans, which is a coverage statement rather than a failure. That is the right shape, and it is worth noting because a silent empty is often indistinguishable from a broken call.

## What it refuses, and how the refusal reads

Six account tools answered without a key, all at HTTP **200** with `isError: true` and the same readable body:

```json
{"error": "unauthorized",
 "message": "This tool needs a MeiSIM API key. Remote: send it as an Authorization: Bearer header on the connection. Local: set MEISIMUSA_API_KEY. No key yet? Sign up at ...",
 "status": 401}
```

Three properties are worth copying here. The message names **both** routes in, remote header and local environment variable. It states that a person must open the account. And it masks the credential in its own example rather than printing a token shape an agent might echo.

`topup_lookup` is the exception: it answered without a key, returned an empty `lines` array with a hint naming the three fields that would find an order. That inconsistency is a small design choice, harmless in practice, and welcome because it lets a flow check a number before asking for a credential.

## Three defects, recorded rather than smoothed

**1. A required field the description says is unused.** `purchase` declares `payment_method` as a required object with a `type` enum (`stored_card`, `stripe_payment_method`) and a `token`, while its own description reads *Not used: payment happens on the hosted Stripe page via payment_url. Reserved for a future direct-charge path.*

A caller reading the description will omit it and be refused. A caller reading the schema will send a fake token to satisfy a field nobody reads. Measured: `purchase` with `payment_method` as the string `"card"` and a non-GUID `idempotency_key` returned

```text
MCP error -32602: Input validation error: Invalid arguments for tool purchase:
Invalid input: expected object, received string at payment_method Invalid GUID at idempotency_key
```

Two failures concatenated in one sentence, the second with no `at` separator. Both were real, both were ours, and one message per failure would have made the retry a single edit instead of two.

**2. A search that requires a filter it presents as optional.** `search_plans` lists `data_gb` with the note *Omit to return all sizes*, and `duration_days` as a plain integer. Calling it with a country code alone returns

```text
MCP error -32602: Input validation error: Invalid arguments for tool search_plans:
Invalid input: expected number, received undefined at duration_days
```

So the one filter a caller is invited to omit is not `data_gb`, it is the term. The guide records it because the first call of a session will hit it.

**3. A zero ceiling is a validation error, not a query.** `max_price_usd` must be greater than zero, so *show me the cheapest* has to be asked with a number the caller guesses. The refusal names the bound, which is the difference between a one minute fix and a support thread.

## What this replaces in an operator's stack

The class exists without MCP: Twilio provisions numbers, a carrier API sends texts, and a spreadsheet tracks renewals. What changes with this surface is that an agent can hold the whole loop in one place, because the three operations that normally live in a dashboard are tool calls: read inbound, wait for the next one, send a reply.

Two limits are stated by the server and should be quoted to anyone planning on it. A number is billed in a **two month minimum term** paid up front, and **there are no refunds once a number is delivered**. An agent with purchase authority over this tool can spend real money on a line it will keep for sixty days.

## Why it earns a page

This catalogue carries several ways to send a message and no way to own the number the message arrives on. `Mobile Text Alerts` covers broadcast texting to a subscriber list; `WhatsApp Business` covers the Meta messaging platform on a business number that Meta verifies. Neither gives an agent a US mobile line with inbound texts and a SIP voice channel on a per-line price, and neither sells the number at all.

The find is not that the telecom API is now an MCP server. It is that the vendor wrote its own gate into the refusal text: the agent buys, provisions, reads and replies, and a human opens the account with an identity document. That is a workable shape for giving an autonomous process a real phone line, and it is the first entry here that draws that line explicitly.
