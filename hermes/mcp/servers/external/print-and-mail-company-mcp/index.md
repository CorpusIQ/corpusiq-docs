---
title: "Print and Mail Company MCP - Letters From an Agent"
description: "An MCP server that prices, composes and posts real paper letters from the EU to 236 destinations, with registered mail and a confirm gate."
category: "Business Operations / Physical Mail"
stars: "0 (hosted and closed source; the connector repository is public)"
added: 2026-11-14
source: "the mcpservers.org canonical arrival at 2026-11-14T06:02Z, the official registry record com.printandmailcompany/printandmailcompany 1.0.0, the vendor pages printandmailcompany.com/en/ai-assistants and /en/pricing read the same day, and a live session on this host: initialize, tools/list and nine tools/call requests against https://printandmailcompany.com/mcp"
relevance: ★★★
tags: [physical mail, letters, post, postage, registered mail, direct mail, eu, germany, france, invoicing, collections, mcp, remote]
last_updated: "2026-11-14"
---

# Print and Mail Company MCP

**Some things a business has to say still go on paper.** A cancellation, a formal notice, a collections letter, a contract termination, a letter to a customer who has stopped answering email. An agent can draft all of them in seconds and then stops dead at the last step, because a model cannot buy a stamp. Every operator in that position does the same thing: copy the text into a word processor, print it, find an envelope, look up the postage, and drive to a postbox.

Print and Mail Company is a German-facing service that puts both ends of that on an MCP server: it prices a letter to the exact destination before you write it, formats the document to a print standard, and posts it through a carrier after you confirm. The sender can be anywhere in the world, no postal account is needed, and the letters are printed in Germany, France, Belgium or Luxembourg.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, stateless (no Mcp-Session-Id issued)
Endpoint:      https://printandmailcompany.com/mcp
Server:        printandmailcompany 1.0.0, protocol 2025-06-18, capabilities: tools
Registry:      com.printandmailcompany/printandmailcompany 1.0.0, streamable-http, same URL,
               status active, published 2026-10-07
Auth:          none for the three read tools; a Print and Mail Company account for the
               eleven that compose, store, price a draft or spend money
Tools:         14, no annotations in the schema
Destinations:  236, in five postage zones Z1 to Z5
Origin:        printed and posted in Germany, France, Belgium or Luxembourg
```

## The evidence tier

Discovery-open, execution-gated, measured end to end. `initialize` answered **200** with `serverInfo` **printandmailcompany 1.0.0** on protocol **2025-06-18** and **no session header**, and a keyless `tools/list` returned all **fourteen** tools with full descriptions and input schemas. Nine `tools/call` requests were driven.

The split is deliberate and it is the part worth copying. The three tools that only read - `get_price_quote`, `list_destinations`, `check_pdf_margins` - answer with no account at all, which is why the pricing in this guide is measured rather than quoted from a page. Everything that touches an account answers **401** `invalid_token`: `get_balance` and `list_letters` were both refused, and the vendor's own tool table marks the compose, upload, create and send tools as requiring sign-in.

The server's `instructions` string describes the service in its own words: letters are printed and posted in Germany, France, Belgium or Luxembourg and delivered by postal carriers, the sender can be anywhere in the world, and no local address or postal account is needed.

## What the fourteen tools do

| Tool | Required arguments | Account | What it returns or does |
|---|---|---|---|
| `get_price_quote` | `pages`, `country` | no | exact total including VAT, with a line per component, the zone, post format, weight and delivery window |
| `list_destinations` | none | no | **236** countries with their zone, or one country with its one-page and registered price |
| `check_pdf_margins` | `pdf_url` or `pdf_base64` | no | whether the PDF is A4 or US Letter and keeps the required 9 mm margin |
| `compose_letter` | `sender`, `recipient`, `subject`, `body` | yes | text into an A4 letter in DIN 5008 layout that passes the print check |
| `upload_document` | `pdf_url` or `pdf_base64` | yes | stores an existing PDF as a document |
| `fix_document_margins` | `document_id` | yes | shrinks pages or crops margins so the print check passes |
| `create_upload_link` | none | yes | a private link to upload a PDF from a device |
| `create_letter` | `recipient` | yes | a draft with the exact price; nothing is charged |
| `send_letter` | `letter_id`, `confirm`, `user_accepted_terms` | yes | posts a confirmed draft |
| `get_letter` | `letter_id` or `reference` | yes | status: draft, paid, in production, printed, posted |
| `list_letters` | none | yes | recent letters, filtered by status |
| `cancel_letter` | `letter_id` | yes | cancels a draft, or a paid letter that has not been printed |
| `get_balance` | none | yes | prepaid credit and whether it covers a draft |
| `create_topup_link` | none | yes | a link to add credit, or to pay one specific draft by card |

Two argument shapes are stricter than they look, and both were measured by sending the natural wrong form first. `country` must be a two-letter code - `"France"` is rejected with *Too big: expected string to have exactly 2 characters* - and `color` is an enum of `bw` or `color`, not a boolean.

## What came back when it was driven

| Request | Total incl. 17% VAT | Net | Postage | Zone | Delivery |
|---|---|---|---|---|---|
| 2 pages to France | **€4.20** | €3.59 | €2.78 | Z1 | 2-4 business days |
| 2 pages to France, registered | **€23.95** | €20.47 | €2.78 | Z1 | 2-4 business days |
| 1 page to Germany | **€3.86** | €3.30 | €2.78 | Z1 | 2-4 business days |
| 4 pages to the United States | **€6.11** | €5.22 | €3.83 | Z4 | 5-15 business days |
| 1 page to the United States, from `list_destinations` | €5.09 | - | - | Z4 | 5-15 business days |

The line items are returned individually, which is what makes the number checkable. For two pages to France the components are envelope **€0.23**, paper **€0.28** (two sheets), printing **€0.30** (two sheets) and postage **€2.78** - net **€3.59**, VAT at 17% **€0.61**, total **€4.20**. The arithmetic reconciles by hand to the cent on every quote measured.

The second page costs **€0.34** more than the first (€3.86 for one page against €4.20 for two), which is paper and printing with no extra postage, and the quote states the weight it priced (10 g for one sheet, 15 g for two).

**Registered mail is a flat €19.75 surcharge, not a percentage.** Two pages to France went from €4.20 to €23.95, and the one-page United States price went from €5.09 to €24.84 - the same €19.75 both times, on two different zones. An agent asked to "send it registered" can state that number before it does anything.

The zone is the whole of the price model outside registered mail: Germany and France are **Z1** at €2.78 postage for a letter, the United States is **Z4** at €3.83, and `list_destinations` assigns every one of the 236 countries to Z1 through Z5. `list_destinations` with a country returns that country's one-page and registered price directly, which is the cheaper call when the question is "can I and what does it cost" rather than a full quote.

## The confirm gate, and why it is the right shape

`send_letter` requires three arguments: `letter_id`, `confirm`, and `user_accepted_terms`. A draft is created first - `create_letter` returns the exact price and charges nothing - and the money is only spent when the caller passes the confirmation flags against that specific draft.

That is the pattern a physical, irreversible, money-spending action needs, and it is rarer in this catalog than it should be. The failure it prevents is the one that matters: an agent that misreads "cancel my subscription" and posts a letter to the wrong address cannot un-post it. The vendor's own description of the product makes the same promise - *every letter is shown to you and only sent after you confirm* - and the tool schema is where that promise is enforced.

Payment is prepaid: credit sits on the account, `get_balance` reports it, `create_topup_link` adds credit or pays one draft by card, and the published pricing page states there is **no subscription and no setup fee**, one price per letter covering envelope, paper, printing and postage plus 17% VAT.

## Limits worth knowing before you connect

- **Two-letter country codes only.** A model that writes "United Kingdom" instead of `GB` gets a validation error, not a suggestion.
- **A4 and US Letter, with a 9 mm margin.** `check_pdf_margins` will refuse a PDF that does not fit, and `fix_document_margins` will shrink or crop it - which changes the document rather than rejecting it, so review what it produced.
- **The paper is European.** DIN 5008 layout, European envelope sizes DL, C5 and C4, printed in Germany, France, Belgium or Luxembourg. A US-format letter will be reformatted.
- **No delivery confirmation on the standard tier.** `get_letter` reports status through `posted`; registered mail is the only trackable option and it costs €19.75.
- **The service name is on the envelope.** This is a mailing house, not a discreet one; a letter arrives in a printed envelope from a print and mail provider.
- **Eleven of fourteen tools need an account**, so a fully driven session on this host was not possible and the compose and send behaviour is documented from the tool schema and the vendor's pages, not measured.

## Connecting it

```bash
claude mcp add --transport http printandmailcompany https://printandmailcompany.com/mcp
```

Claude (desktop and mobile) takes it as a custom connector at the same URL with OAuth; ChatGPT takes it under `chatgpt.com/plugins` as an MCP server with OAuth; any other client uses the plain URL:

```json
{"mcpServers": {"printandmailcompany": {"url": "https://printandmailcompany.com/mcp"}}}
```

Quotes work before you sign in, which makes the pricing worth testing first: ask for a two-page letter to your own country and compare the total with what the pricing page states.

## Questions this answers that a chat window alone cannot

### What does it cost to post a two-page letter to France?

**€4.20 including 17% VAT**, delivered in **2-4 business days**, itemised as envelope €0.23, paper €0.28, printing €0.30 and postage €2.78, from a live `get_price_quote` call. Registered, the same letter is **€23.95** - the €19.75 flat surcharge, not a percentage.

### Can my agent post a letter without me reading it first?

Not through this surface as designed: `send_letter` requires `confirm` and `user_accepted_terms` against a specific `letter_id`, and the draft step returns the exact price with nothing charged. The gate is in the schema, not only in the prompt.

### Which countries can it reach?

**236**, in five postage zones. `list_destinations` with no arguments returns the full list with each country's zone; with a country code it returns that country's one-page and registered price and its delivery window.

### Does it need a subscription?

No. Prepaid credit per letter - envelope, paper, printing and postage plus 17% VAT - with no subscription and no setup fee, per the vendor's published pricing.

## Verdict

A three-star entry on a gap that the catalog could describe and could not act on. The first physical-mail server here was US-centric - MailStream for postcards and letters, PostAgent for USPS paid per call in USDC - and this one is the European counterpart: printed in Germany, France, Belgium or Luxembourg, priced in euros, posted to 236 countries, with registered mail as a real option and a sender who can be anywhere.

The measured surface is unusually good for a first release: pricing is keyless and itemised, the arithmetic reconciles to the cent, the confirm gate is enforced in the tool schema, and the registered surcharge is disclosed by the tool rather than buried in a price list. What holds it back is the account wall - eleven of fourteen tools need sign-in, so the compose, upload and send paths are documented rather than driven - and the European paper format, which makes it the wrong tool for a US-format mailing.

For an operator who needs a cancellation, a collections letter or a formal notice to arrive on paper and cannot be bothered with a printer, this is the shortest path from a sentence to a postbox.

See also: [MailStream MCP](/hermes/mcp/servers/external/mailstream-mcp/) for US postcards, letters and campaigns, and [Zip-Codes.com MCP](/hermes/mcp/servers/external/zip-codes-mcp/) for validating the address before anything is printed.
