---
title: "SmartRetry Payment Tools MCP - BIN, MCC and Declines"
description: "Free keyless card payment reference data for agents: BIN and issuer lookups, merchant category code definitions and what a decline code actually means."
category: Finance
stars: n/a (free, no authentication)
added: 2026-11-05
source: "The mcpservers.org sitemap addition www-smartretry-com-mcp in the November 5 2026 night window; the official MCP registry record com.smartretry/payment-tools published 2026-11-03T11:38:52Z; a keyless initialize and tools list against https://tools.mcp.smartretry.com/mcp returning HTTP 200 as smartretry-tools 1.0.0 with four tools and full input schemas; nine live calls across all four tools (two BINs resolved, one nonsense BIN, two issuer searches including a misspelling, three MCC queries and four decline codes); and HTTP reads on smartretry.com/mcp for the vendor's own privacy and scope statements"
relevance: ★★★
tags: [payments, fintech, bin-lookup, mcc, decline-codes, card-networks, merchant-operations, keyless, free, read-only]
last_updated: "2026-11-05"
---

# SmartRetry Payment Tools MCP

**Every operator who takes cards eventually asks four small questions that no amount of reasoning answers: which bank issued this card, what is this four digit code on my statement, who is this issuer I have never heard of, and what does this decline actually mean. All four are reference data, all four are answered confidently by a model that does not have them, and all four decide whether the next action is retry, refund, contact the customer or contact the bank.** SmartRetry publishes them as four free read-only MCP tools.

```
Server type: Remote, Streamable HTTP
Endpoint:    https://tools.mcp.smartretry.com/mcp
Auth:        none (no sign-up, no API key, no account)
Version:     1.0.0 (serverInfo smartretry-tools)
Registry:    com.smartretry/payment-tools, published 2026-11-03
Tools:       4, all readOnlyHint true, idempotentHint true
Vendor:      SmartRetry (payments recovery), smartretry.com
Data:        public card, issuer and network reference data, not your transactions
```

The tier is measured rather than implied: a keyless `initialize` returned **HTTP 200** as `smartretry-tools` **1.0.0**, `tools/list` returned all **four** tools with complete input schemas, and **nine calls** were made across all four tools with real arguments. The server is stateless, so no session header is needed after `initialize`.

## What the four tools answer

| Tool | Argument | What comes back |
| --- | --- | --- |
| `lookup_bin` | `bin`, six to eight digits matching `^\d{6,8}$` | card network, card type and level, issuing bank, country, and the bank website and phone when known |
| `lookup_issuer` | `name`, two to one hundred characters, partial names accepted | matching banks with country and contact details |
| `lookup_mcc` | `query`, a four digit MCC or a business description | category name, group, high risk flag, and the Visa plus Mastercard definitions |
| `lookup_decline_code` | `code`, one to one hundred characters, plus optional `provider` | the code meaning, its namespace and level, and a list of related codes |

All four declare `readOnlyHint: true`, `destructiveHint: false` and `idempotentHint: true`, so a client that gates writes on annotations passes them straight through.

## What the calls actually returned

**BIN.** `414709` came back as **VISA CREDIT (TRADITIONAL)** issued by **CAPITAL ONE, NATIONAL ASSOCIATION**, United States. `519256` came back as **MASTERCARD DEBIT (BUSINESS)** issued by **STATE BANK OF INDIA**, India, with the bank website and phone number attached. The distinction matters to an operator: a business debit card and a consumer credit card behave differently on authorisation, on interchange and on a dispute.

**Issuer.** `chase` returned a set of separate legal entities rather than one bank: **JPMORGAN CHASE BANK, N.A.** in Singapore and in the US Virgin Islands, **CHASE MANHATTAN BANK** in Thailand, **CHASE BANK USA, N.A.** in Puerto Rico, and **DISNEY REWARDS (ISSUED BY CHASE)** in the United States, each with its own country and contact path. That is the right shape for a dispute, because a chargeback goes to the issuing entity, not to the brand.

**MCC.** `5411` returned **Grocery Stores and Supermarkets**, group **Retail outlets**, high risk **no**, followed by the two network definitions. The Visa definition is the one worth reading: the merchant must sell a full line of food for home consumption, and perishables must be at least **45 percent** of monthly sales volume. `7995` returned **Betting, including Lottery Tickets, Casino Gaming Chips, Off-Track Betting** with high risk **yes** and group **Amusement and entertainment**. A description instead of a code works too: `coffee shop` returned **5814, Fast Food Restaurants**.

**Decline.** `51` returned **Visa 51: Not sufficient funds** tagged as an issuer response code. `05` with `provider: Visa` returned **Visa 05: Do not honor**. `do_not_honor` returned the Stripe namespace answer, **the card was declined for an unknown reason, the customer must contact their card issuer**, beside the related Stripe statuses such as `requires_payment_method` and `requires_confirmation`.

## Where it is thin, measured rather than assumed

Three weaknesses showed up in the calls themselves and belong in the guide because an operator will hit them.

**There is no not-found state on a BIN.** `123456` is not a plausible issued BIN and the tool answered `LOCAL BRAND CREDIT (UATP)` with no confidence field, no null and no warning. Treat a BIN answer as the vendor's best record rather than a confirmation that the card exists.

**The fuzzy issuer match is weak on short strings.** `chse` was meant to be a misspelling of Chase and returned **SPARKASSE MITTELSACHSEN** in Germany instead. Pass the full name, or the answer is a different bank in a different country.

**Related codes cross namespaces.** The related list under `51` and `05` mixes issuer response codes, ECI codes and 3DS transaction status reasons under the same numeric label, so the same number appears three times with three meanings. Read the bracketed namespace, never the number alone.

Two smaller notes. The `lookup_mcc` parameter is named `query` even though the description says to pass a four digit MCC, so a call using `mcc` is refused with `-32602 Required at query`. And a pasted processor message such as `Your card was declined.` returns **no decline code found**, so the message has to be reduced to the code or the canonical token first.

## Why an operator should have this in the client

The payment stack answers what happened to a specific charge. This answers what the surrounding words mean, which is the part that decides the next step.

- **Statement and payout reconciliation.** A line reading `5411` or `7995` is unreadable until it is expanded, and the high risk flag is the difference between a normal cost line and a chargeback exposure line.
- **Failed payment triage.** `51` is not sufficient funds, which is a retry on a date, where `05` do not honor is a contact the issuer, and a generic processor decline is neither. The three get different actions and the guide is the only place that distinction is written down.
- **Dispute preparation.** A chargeback needs the issuing legal entity and its country, which is what `lookup_issuer` returns and what a plausible guess about the brand does not.
- **Card mix arithmetic.** Debit against credit, business against consumer, domestic against cross border: the BIN answer is the input to fee and routing questions that otherwise get answered from memory.

## Wiring it into CorpusIQ

The server takes no credential and holds no client state, so it can be added beside the payment connectors rather than instead of them. In Claude, add a custom connector with the URL. In ChatGPT, turn on developer mode under Settings then Apps and Connectors and create a connector with no authentication.

The useful pattern is a two source answer in one turn. A Stripe or QuickBooks connector says a charge of a given amount failed on a given date with a given code; this server says what that code means and who issued the card. The operator gets one answer with one number instead of a code, a guess and a support ticket.

## Limitations

- It reads public payment reference data only. It cannot see a client's transactions, and the vendor states plainly that the customer-only Platform MCP carrying live transaction data is requested through an account manager.
- It never accepts a full card number. The BIN schema is six to eight digits, and the vendor states a full number is rejected before anything runs.
- The vendor logs which tool ran and how long it took, never the query itself, and publishes fair use rate limits without a numeric ceiling.
- Coverage is what the vendor's dataset holds. The nonsense BIN answer is the evidence that a miss returns a plausible looking record rather than an error.
- The vendor is a payments recovery company selling retries. The tool descriptions keep the pitch in one closing line rather than in the payload.

## FAQ

### Does this MCP server need an API key?

No. It answers keyless on `https://tools.mcp.smartretry.com/mcp`, publishes no sign-up, and the four tools are read-only by design.

### Can it look up a specific transaction or a full card number?

No. It holds public reference data only, and the BIN tool accepts six to eight digits, so a sixteen digit number is refused before it runs.

### What does MCC 5411 mean and is it high risk?

Grocery Stores and Supermarkets, in the Retail outlets group, not high risk. MCC 7995 for betting is the one that returns high risk yes.

### Is a decline code answer provider specific?

Sometimes. The `provider` argument narrows it, and the bracketed namespace on every answer says whether the code came from an issuer response set, an ECI set, a 3DS status reason or a processor such as Stripe or Adyen.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Stripe MCP Server - Official Stripe Data](/hermes/mcp/servers/external/stripe-mcp/)
- [PagoFix MCP - EU Late-Payment Interest Drafts](/hermes/mcp/servers/external/pagofix-mcp/)
- [InvoiceParser Pro MCP - Invoice to Excel from Chat](/hermes/mcp/servers/external/invoice-parser-pro-mcp/)
