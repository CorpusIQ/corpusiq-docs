---
title: Sellfy MCP - Store Operations Inside the Chat
description: "Hosted MCP for a Sellfy store: products, discounts, orders, sales and draft campaigns, with no delete, refund or buyer-email tool by design."
category: Commerce & E-Commerce
stars: n/a (included on every Sellfy plan and the 14-day trial; the store itself is paid)
added: "2026-11-06"
source: "The mcp.so homepage recentServers card sellfy-mcp stamped 2026-11-06T13:13:32.202Z and its detail page; the vendor page at sellfy.com/mcp and the machine readable contract at sellfy.com/mcp.md (last updated 2026-10-22); the agent setup file at api.sellfy.com/agent-setup.md; the protected resource document at api.sellfy.com/.well-known/oauth-protected-resource/mcp; and a keyless initialize probe of api.sellfy.com/mcp answering 401 with that document named in WWW-Authenticate"
relevance: ★★★★
tags: [commerce, ecommerce, sellfy, store, digital-products, orders, discounts, oauth, remote, streamable-http, claude, chatgpt, cursor]
last_updated: "2026-11-06"
---

# Sellfy MCP

**Every store owner has a question they answer by clicking around a dashboard for ten minutes, and an assistant that cannot get at the store can only guess at the answer.** A Sellfy store connected through MCP stops the guessing: the assistant reads the real numbers, and where it writes it writes the way a careful employee writes, into drafts that a human still has to approve. The interesting part of this server is not the product list. It is the envelope around the writes, because that envelope is the answer to the question every operator asks before letting an agent near their shop.

```
Server type:  Remote, Streamable HTTP
Endpoint:     https://api.sellfy.com/mcp
Auth:         OAuth browser sign-in with the seller's own Sellfy account,
              scopes mcp:read and mcp:write, no API keys to create
Plans:        every Sellfy plan, including the 14-day free trial at no extra cost
Rate limit:   120 requests a minute across all connected clients
Session:      expires after 30 days unused or 180 days total; a password
              change ends every connection at once
Launched:     14 October 2026
Vendor:       UAB Sellfy, Riga; the vendor states 75,000+ creators and
              businesses and $165M+ in creator earnings
First tool:   get_store_info, which returns the store name and currency
```

**Evidence tier: documented, not driven.** There is no Sellfy store on this machine, so nothing here was measured against live data. What was verified is the connection itself and the published contract: a keyless `initialize` against `api.sellfy.com/mcp` answers **401** with `WWW-Authenticate: Bearer resource_metadata="https://api.sellfy.com/.well-known/oauth-protected-resource/mcp"`, and that document names the authorization server, `bearer_methods_supported: header`, and the two scopes `mcp:read` and `mcp:write`. The behaviour below comes from the vendor's own machine readable page at `sellfy.com/mcp.md`, written for machines rather than for a sales pitch, plus `api.sellfy.com/agent-setup.md`, which is an instruction file addressed to the agent doing the setup. Claims about what the tools return are the vendor's, and are marked as such by the evidence label at the top of this page.

## What a connected assistant can do

| Area | What is exposed |
| --- | --- |
| Products | Create digital, physical, subscription and print-on-demand products; edit titles, descriptions and prices; upload and attach files; set variants; manage media; add or revoke license keys |
| Publishing | Publish a product on request, as a separate step from creating it |
| Discounts | Create and update a discount, list codes, expire a code |
| Orders and customers | Search orders by date, buyer address, payment status or shipping status; open one order by transaction id for line items and amounts; list customers; list reviews |
| Sales | Summaries, histograms and top stats answered from the store's own numbers |
| Email | Create and update campaigns, and send a test to the seller's own address |
| Storefront | Create a draft store version, edit pages and modules inside it, preview, then publish or discard |
| Shipping | Create and update shipping profiles and apply them to products |

A seller's real prompts, from the vendor page, are the useful scale here: create a 20 percent discount code called THANKYOU20 valid for seven days; how did last month compare to the month before and which product made the most; which products have no image or a description shorter than two sentences; find the orders for a buyer address and tell me whether payment went through. None of those need a dashboard, and each one is a question a small merchant answers by hand today.

## What it cannot do, and why that is the reason to trust it

The restrictions are properties of the build, not promises in a policy document, which is why they are worth reading as a design pattern:

- **It cannot email buyers.** Campaigns are only ever created as drafts, and a test email goes to the seller's own address. Sending to a list stays in the dashboard, done by the merchant.
- **It does not publish on its own.** New products are created unpublished, publishing is a separate request, and a digital product cannot go live at all until it has a file, text, link or license keys attached.
- **It cannot delete a product or a discount.** No such tools exist. A discount can only be expired, and the only deletions available are a license key and a store draft.
- **It cannot move money.** There is no refund tool and no payout tool.
- **It cannot overwrite a concurrent edit.** Storefront writes carry a revision check: if the page changed since the assistant last read it, the write is rejected and the assistant has to read again first.

That last one is the piece most agent integrations skip, and it is the one that matters in a shop with a second person in it. Two editors, one stale read, and the naive connector silently reverts somebody's work. A revision check turns that into an error message.

## The draft, preview, publish shape

The whole write surface follows one pattern, and it is the pattern to copy when wiring an agent into anything that is publicly visible: write into a draft, produce a preview the operator can open on a phone, and leave the final click with the human. On Sellfy this shows up twice, in the storefront (a draft store version with a preview link, the live store untouched until published) and in email (a campaign waiting in the dashboard, plus a test in the seller's own inbox). Products follow the same logic in a cheaper form: created unpublished, published only when asked.

For an assistant, the practical consequence is that a failed experiment costs nothing. The merchant can ask for a rewritten About page, look at the preview link the assistant returns, and discard it.

## Connecting it

One URL for every client, and a sign-in instead of a key: `https://api.sellfy.com/mcp`.

- **Claude.** There is a directory listing, so this is a Connect button rather than a pasted URL. The step people miss is the second one: after authorising, the connector has to be switched on inside each conversation.
- **ChatGPT.** Custom MCP server, paste the URL, leave authentication as detected, accept the trust prompt, then mention it with an at sign in the chat. The vendor notes that developer mode is not required, which is worth saying because older guides still tell you to turn it on.
- **Claude Code.** `claude mcp add --transport http sellfy https://api.sellfy.com/mcp`, then authenticate from the MCP menu.
- **Cursor, VS Code, Codex CLI, Gemini CLI, Perplexity, Lovable, Replit, Mistral Le Chat.** Same URL, OAuth in every case; the vendor's setup contract carries the exact command or click path per client.

The setup file tells an agent to call `get_store_info` first and to report the store name and currency as proof of connection. It also carries the error translations an operator ends up needing: "invalid or missing access token" means the sign-in never finished or was revoked, a permission error names `mcp:read` or `mcp:write`, and a stale authorization page has to be restarted.

## Where it stops, and the details that bite

- **Money arrives in minor units.** A price of 1999 is 19.99 in the store's currency. Any assistant that reports order totals without a currency conversion is off by a factor of 100, and the vendor warns about exactly this in its agent setup file.
- **Read tools see buyer data.** Orders, customers and reviews carry buyer names and email addresses, and whatever a tool returns is sent onward to whichever model provider the merchant connected, under that provider's terms. That is a data-processing decision the merchant is making when they connect, not a footnote.
- **It runs the store you already have.** The vendor is explicit that it does not find customers.
- **Connection lifetime is bounded.** Thirty days unused or 180 days total, then a fresh sign-in. A password change revokes everything at once, which is also the fastest way out if a connection is misbehaving.
- **The rate limit is generous but shared.** 120 requests a minute across all connected clients, so a broad audit of hundreds of products is cheap rather than free.

## Business relevance

The merchant this fits is the one-person shop that sells digital products, print-on-demand or subscriptions and lives in a dashboard between other jobs. The measurable work it removes is the monthly check-in: last month against the month before, which product carried it, which orders are unpaid, which listings are thin or missing images. Those are four questions and about twenty dashboard minutes each, and they are the questions that get skipped in a good month and hurt in a bad one.

The write side is where the discipline shows. Draft a product, attach the file, match the description to the rest of the catalogue, leave it unpublished; draft a campaign and send the test; rewrite a page into a preview link. The merchant reviews and publishes. That is a working assistant rather than a demo.

## Integration with CorpusIQ

The value of a connector like this inside a governed retrieval layer is narrow and real: sales and order questions that today live behind a login become one more read source next to Shopify, Stripe and QuickBooks, and the operator gets a single answer that cites which system it came from instead of three numbers that disagree. CorpusIQ's direct MCP requests fetch live and do not retain raw customer files or full connector response payloads; operational logs can retain query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days, while optional indexed search and compliance receipts carry their own separate lifecycles. On that basis the read tools are the part that fits, while the write tools belong in the vendor's own approval flow.

## Limitations

- No live account was driven for this entry; tool names beyond `get_store_info` are the vendor's published capability groups rather than observed responses.
- No refund, payout or money-movement tool exists, by design, so financial corrections stay manual.
- No buyer email send, by design; campaign sending is dashboard work.
- Buyer names and addresses reach the connected model provider when read tools run.
- The vendor's own page carries release claims (75,000+ creators, $165M+ earned) that this pass could not verify independently.
- Permissions are two coarse scopes, read and write, with no finer per-object scoping published.

## FAQ

### Can an AI assistant accidentally delete products or email customers in a Sellfy store?
No. There are no delete tools for products or discounts and no tool that sends to a buyer list. Campaigns are drafts, test emails go to the seller, and a discount can only be expired. The blast radius is limited by the build rather than by prompt instructions.

### Does the Sellfy MCP server cost extra?
No. It is included on every plan and works during the 14-day trial, with no add-on and no usage fee. The rate limit is 120 requests a minute across all connected clients.

### Which assistants can connect to Sellfy over MCP?
Anything that speaks Streamable HTTP with OAuth, which today includes Claude, ChatGPT, Claude Code, Cursor, VS Code, Codex CLI, Gemini CLI, Perplexity, Lovable, Replit and Mistral Le Chat. Each uses the same URL and a browser sign-in.

### What happens if two people edit the same store page?
Storefront writes carry a revision check. If the page changed since the assistant last read it, the write is rejected and the assistant re-reads before retrying, so a stale draft cannot quietly overwrite a colleague's edit.

## See Also

- [GumroadDNA MCP - Gumroad Store Operations](/hermes/mcp/servers/external/gumroad-dna-mcp/)
- [ShopSynch MCP - E-Commerce Operations for AI Agents](/hermes/mcp/servers/external/shopsynch-mcp/)
- [Shop MCP - Read-Only Shopify Catalogue and Stock](/hermes/mcp/servers/external/shop-mcp/)
- [MarketPrint MCP - Print on Demand to Your Store](/hermes/mcp/servers/external/marketprint-print-on-demand/)
- [Ozon Seller MCP](/hermes/mcp/servers/external/ozon-seller-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
