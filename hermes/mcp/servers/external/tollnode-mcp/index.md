---
title: "TollNode MCP - 155 Paid Calls and Their Published Prices"
description: "A metered gateway that lists a price for every one of 155 tools, then asks for that exact price in USDC base units before it answers, so a workflow can."

category: "AI Gateway / Metered Data"
stars: "0 (remote Streamable HTTP; 156 tools listed, 155 of them priced, 1 free catalogue tool; three paid tools measured to their x402 challenge)"
added: 2026-11-16
source: "the mcp.so submission queue entry #7395 filed 2026-11-15T14:33:00Z, and a driven session on 2026-11-16 in which initialize, tools/list and the free list_models tool were run and three separate paid tools were measured to their payment challenge"
relevance: ★★★
tags: [gateway, x402, pay-per-call, pricing, sanctions-screening, sec-filings, email-verification, keyless, remote, mcp]
last_updated: "2026-11-16"
---

# TollNode MCP

**The missing number in most AI stacks is the price of a call.** A business owner can see what a model costs per million tokens and still have no idea what a sales list, an email verification pass or a sanctions screen costs to produce. Every tool arrives with a claim and no invoice, and the invoice is the thing the operator actually has to sign.

TollNode is a gateway that puts **155 tools behind one endpoint with a price printed on each of them**, charged in USDC on Base, per call. What earns it a page here is not the count. It is that the price list is a **free, machine-readable tool**, the payment challenge **carries the same number in base units**, and the two agree to the cent on every line measured.

```
Server type:   remote Streamable HTTP, stateless
Endpoint:      https://tollnode.com/mcp
Server:        tollnode, version 1.0.0, title TollNode
Protocol:      2025-06-18
Payment:       x402 version 2 on eip155:8453 (Base), asset USDC
               at 0x833589fCD6..., or an account API key
Tools:         156 listed; 155 priced; 1 free (list_models)
Website:       https://tollnode.com
Listed on:     the mcp.so submission queue as #7395
```

## The evidence tier

**Measured to the payment gate, and stated as such.** `initialize` answered **200** as `tollnode` **1.0.0** on protocol **2025-06-18** with a full instructions field and `capabilities.tools` carrying `listChanged: false`. `tools/list` returned **156** schemas. The free `list_models` tool was called and returned all **155** priced tools with price, parameters and category. Three paid tools were then called without any payment and each returned an **x402 version 2** challenge, which is the evidence recorded below.

**No paid call was executed.** Nothing in this guide was purchased. The price claims are checked against the challenge the server itself issues, and the one claim that cannot be checked without paying is named as such in its own section.

## The catalogue tool is the free one

The arithmetic of the count closes exactly:

| Measurement | Value |
|---|---|
| `tools/list` schemas | 156 |
| `list_models` count field | 155 |
| Tools in `list_models` missing from `tools/list` | 0 |
| Tools in `tools/list` missing from `list_models` | 1 (`list_models` itself) |

**155 priced tools plus the free index tool is 156.** A caller counting only what it can pay for gets 155, and the difference is the one tool that costs nothing, which is also the one tool a caller should run first.

## What the 155 actually are

`list_models` returns a category on every tool, and the categories sum to the count:

| Category | Tools | Category | Tools |
|---|---|---|---|
| Image | 56 | Lookup | 5 |
| Video | 30 | Shopping | 5 |
| Social | 18 | Travel | 4 |
| Audio | 12 | Document | 2 |
| **Business** | **10** | Jobs | 2 |
| Search | 8 | Text | 2 |
| | | Property | 1 |

56 + 30 + 18 + 12 + 10 + 8 + 5 + 5 + 4 + 2 + 2 + 2 + 1 = **155**. The largest share is generation, which is not what this catalog is for. The **ten Business tools** are, and they are priced individually rather than bundled.

## The ten business tools and what each costs

| Tool | Price as published | What it returns |
|---|---|---|
| `company-contacts` | $0.020 per website | Emails, phones and addresses a company publishes |
| `company-registry` | from $0.003 per lookup | SEC financials, filings, insider trades |
| `email-verify` | $0.003 per email | Status, score, MX, mailbox, catch-all, disposable |
| `maps-business-search` | $0.042 per search | 10 Google Maps businesses with address and category |
| `google-reviews` | $0.014 per search | 20 newest Google reviews with owner replies |
| `linkedin-company` | $0.007 per company | One company page as JSON |
| `linkedin-company-search` | $0.030 per search | 10 companies by keyword and location |
| `linkedin` | from $0.007 per call | Company profiles, employees, posts, people |
| `sanctions-screen` | $0.010 per name | OFAC SDN and non-SDN, UK, EU and UN lists |
| `trustpilot-reviews` | $0.022 per search | 20 newest Trustpilot reviews |

The rest of the surface is priced with the same granularity, and a few lines are worth knowing before a workflow is designed around them:

- **Search:** `web-search` $0.008, `url-to-markdown` $0.006, `news-search` $0.035, `search-trends` $0.037, `webpage-screenshot` $0.008, `website-reader` $0.042 for up to 10 pages, `web-search-markdown` $0.017, `google` from $0.014.
- **Jobs:** `indeed-jobs` $0.006 for up to 25 listings against `linkedin-jobs` $0.016 for the same cap. The same question costs **2.7 times** more on one source than the other.
- **Lookup:** `qr-code` $0.002, `weather` from $0.002, `domain` from $0.003, `base-wallet-balance` $0.003, `vin-decode` $0.005.
- **Travel:** `tripadvisor-reviews` and `booking` from $0.053, `hotel-search` $0.054, `airbnb-search` $0.056. Travel is the most expensive vertical after generation.
- **Document:** `data-file` from $0.003 to check a CSV or Excel file before import, `document-to-markdown` from $0.007.

## The challenge, and the arithmetic that matches it

Calling a paid tool with no payment returns `isError` and a JSON body, not a refusal to price it. The body names the resource, the method, a description of the call and an `accepts` array:

```
sanctions-screen   network eip155:8453   amount 10000   -> 10000 / 1e6 = $0.010
email-verify       network eip155:8453   amount  3000   ->  3000 / 1e6 = $0.003
company-registry   network eip155:8453   amount  5000   ->  5000 / 1e6 = $0.005
```

USDC carries six decimals, so base units divided by **1,000,000** is the dollar figure, and all three reproduce the published price: `sanctions-screen` at **$0.010** a name and `email-verify` at **$0.003** an email are exact, and the asset is USDC at `0x833589fCD6...` on Base with a single `payTo` address. **The quote and the charge are the same number**, which is the property that makes a metered gateway usable by an agent: the price is discoverable before the call, not after it.

The instructions state the flow plainly rather than hiding it behind a client library: call the tool, read the payment requirements in the error result, then call again with the signed payment in `params._meta["x402/payment"]`. The alternative is an account API key on the same endpoint.

## The default action costs more than the headline

`company-registry` publishes **from $0.003 per lookup** and carries a `priceOptions` block that explains what "from" means:

| Action | Price |
|---|---|
| `us_filings` | $0.003 |
| `us_financials` (default) | $0.005 |
| `us_insider_trades` | $0.008 |

The default action is `us_financials` at **$0.005**, which is **67% more** than the headline figure a reader will quote. That is not a bait price: the range is printed, and the default is printed. It is the reason a cost estimate should be built from the `priceOptions` block rather than from the summary line, and it is exactly why the free `list_models` tool exists.

## The gate fires before the arguments are checked

This is the finding that a reader should weigh, because it is the one claim on the surface that cannot be verified without money.

`sanctions-screen` was called three ways: with a real 12 character name, with **no arguments at all**, and with a **400 character** name. All three returned the **identical** x402 challenge. A malformed call is priced the same as a valid one.

The server's own sentence is *You are charged only when a call delivers a usable result*, and the challenge body repeats it per tool as *Charged only when the call succeeds*. **That promise is enforced after payment, on the server, and is therefore not observable from an unpaid session.** An agent that signs first and validates later pays for the privilege of learning its argument was wrong. The practical rule for a caller is to take the JSON Schema from `tools/list`, validate locally, and only then sign, because the payment gate will not do it.

Two smaller notes from the same probe: the instructions describe a free `list_models` filter by category or search word, so the catalogue is queryable rather than a 155 row dump, and the server advertises `websiteUrl` in `serverInfo`, which the docs can be checked against.

## What a real workflow costs

The useful property of a printed price list is that a workflow can be costed before it runs. Enriching **10 companies** from a keyword search to a verified email:

```
linkedin-company-search   $0.030  x 1  (up to 10 companies)   = $0.030
company-contacts          $0.020  x 10 (one per website)      = $0.200
email-verify              $0.003  x 10 (one per email)        = $0.030
                                                    total      = $0.260
```

**$0.026 per company**, which is the sort of number an operator can compare against a data vendor's per-record fee without asking a salesperson. The same arithmetic on a sanctions pass over 500 counterparty names is **$5.00** at $0.010 a name, and over 50 names is $0.50, which is a screening run priced in advance rather than discovered on an invoice.

## Where it is thin, measured rather than assumed

- **One vendor, many products.** The tool descriptions name ElevenLabs, Google's Lyria, MiniMax, Stability and others, so a defect in one line is not a defect in the gateway, and a price change on one line is not a gateway price change. Read the per-tool price, never a blended one.
- **Generation dominates the catalogue.** 98 of 155 tools are image, video, audio or social generation. A reader looking for business data should go straight to the Business, Search, Lookup and Jobs categories, which together are 27 tools.
- **No free tier beyond the catalogue.** Every data tool is metered. There is no anonymous sample call to test a tool's usefulness with, which is why this guide records the challenge rather than a result.
- **USDC on Base only for the payment path.** An operator without a wallet needs the account key, and the account path is not specified in the instructions beyond the bearer header.

## FAQ

### Does it need a key?

No key is needed to connect, list tools or receive a price quote. Every paid call returns a price challenge instead of a result, so an unpaid session is a price enquiry and not a trial.

### Can I see the whole price list without paying?

Yes. `list_models` is free, returns all 155 tools with `price`, `priceOptions`, `parameters` and `category`, and takes a category or a search word. It is the one call to make first.

### Is the price I see the price I pay?

On the three tools measured, yes: the challenge amount in USDC base units divided by 1,000,000 reproduced the published price exactly. Where a tool publishes "from" a price, check `priceOptions`, because the default action is not always the cheapest one.

### What happens if my call is malformed?

You are asked to pay anyway. The challenge fired on empty arguments and on a 400 character name, so validate against the schema before signing rather than expecting the gate to catch a bad argument.

### Where does this fit a business?

Counterparty screening, company enrichment with email verification, and priced data lookups inside an agent workflow are the three places this beats a subscription whose per-call cost nobody can state. It is the first entry in this catalog for a **per-call priced gateway**, which makes it the reference for what a metered MCP surface should publish.

## Related reading

- [External MCP server catalog](/hermes/mcp/servers/external/) for the rest of the servers evaluated and catalogued here
- [mcp-sanctions](/hermes/mcp/servers/external/mcp-sanctions/) and [Sanctions Screening](/hermes/mcp/servers/external/sanctions-screening-mcp/) for the single purpose sanctions surfaces this gateway prices as one tool among 155
- [CorpusIQ connectors](https://corpusiq.io/connectors) for the read-only business systems this catalog is built around
