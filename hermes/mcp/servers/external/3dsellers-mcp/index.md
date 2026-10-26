---
title: "3Dsellers MCP - Six Marketplaces, 150+ Tools"
description: "One hosted endpoint for eBay, Amazon, Walmart, Etsy, Shopify and TikTok Shop: listings, inventory, orders and buyer messages."
category: Commerce & E-Commerce
stars: n/a (vendor-hosted; official registry entry com.3dsellers/mcp v1.0.0)
added: 2026-10-23
source: "mcp.so /feed page 1 card (posted 2026-10-23T13:27:33Z, submitted by 3dsellers, verified and featured) plus the vendor README and the official MCP registry"
relevance: ★★★
tags: [ecommerce, ebay, amazon, walmart, etsy, shopify, tiktok-shop, multichannel, listings, inventory, orders, helpdesk, automations, remote-mcp, oauth]
last_updated: "2026-10-24"
---

# 3Dsellers MCP

**A seller who runs six storefronts does not have six businesses. They have one catalog and six places it has to agree with itself. This is the first MCP entry in this catalog that treats the catalog as the unit and the marketplaces as outputs.**

```
Server type: Remote (Streamable HTTP) at https://api.3dsellers.com/mcp
Auth: OAuth 2.1 authorization code with PKCE S256, client_secret_post at the token endpoint, or a bearer token minted on the 3Dsellers API / MCP page
Live check: POST initialize without a token returned HTTP 401 {"statusCode":401,"error":"Unauthorized","message":"This MCP server requires a bearer token. Discover the authorization server at https://api.3dsellers.com/.well-known/oauth-protected-resource/mcp"}
Discovery: that advertised path returns 200 with resource https://api.3dsellers.com/mcp, 14 scopes and client_id_metadata_document_supported true; /.well-known/oauth-authorization-server returns authorize and token endpoints, code and refresh grants, S256
Tools: 150+ across products and catalog, listings and publishing, inventory, orders, bulk actions, CSV import, export and reports, categories and field mapping, helpdesk and messages, automations, offers, listing designer and selling accounts
Pricing: MCP included in every 3Dsellers plan including the free trial; data reads free; AI actions sold in advance at $9 for 2,000 a month, $20 for 5,000, $29 for 10,000
Vendor: 3Dsellers (3dsellers.com), registry entry com.3dsellers/mcp
```

## Why This Matters for Operators

Multichannel selling fails in one specific place: the space between channels. A price changed on Amazon does not travel to eBay, a product created in the catalog does not carry the item specifics Walmart demands, and an inventory count that is right in Shopify is wrong in TikTok Shop by the end of the day. Every seller knows this, and the standard fix is a person copying numbers between six tabs, which is why the same SKU appears at three prices.

The catalog entries already here read one marketplace each. Amazon Seller Central and Amazon Ads, Datrace, Pangolinfo, Webotee, AMZ Vault, Nova, SellerMate: all Amazon, all depth. Nexscope reads twelve marketplaces but for research, not for changing your own listings. 3Dsellers is the first entry built around the seller's own catalog as the source of truth, with the marketplaces as publishing targets.

That distinction decides what an operator can ask. A research tool answers what the market is doing. This answers what my catalog says, where it is published, what is out of stock, and which buyer is still waiting for a reply, in one place and from one connection.

## What It Actually Does

The tool inventory is published in full in the vendor README, grouped by area and marked read or write, which makes it auditable before you connect anything.

Products and catalog: `get-products`, `get-product`, `create-product`, `update-product`, `patch-product`, `get-product-listings`, `sync-new-skus` and `link-skus-cross-account`. That last pair is the multichannel core. `sync-new-skus` pulls SKUs that exist on a channel into the catalog, and `link-skus-cross-account` ties the same SKU across selling accounts so stock moves together.

Listings and publishing: `publish-products-to-channel` pushes a product to eBay, Amazon, Walmart, Etsy, Shopify or TikTok Shop, with `set-draft-details`, `set-item-specifics`, `apply-policies` and `get-seller-policies` shaping the listing before it goes out. `dismiss-listing-errors` and store category tools clean up afterwards.

Inventory: `set-listing-inventory`, `set-variation-inventory` and `set-inventory-sync`, so a quantity change can be scoped to one listing, one variation, or a whole selling account's sync setting.

Orders: `get-orders` filters by status, channel, date or SKU; `set-order-tracking` pushes carrier and tracking to the marketplace; `generate-order-invoice` and `get-order-invoice` handle paperwork.

Bulk and data movement: `get-action-catalog`, `get-action-schema`, `create-action` and `get-action` run price, item-specific, policy and tag changes across hundreds of listings with a tracked job. The CSV side is a full pipeline of its own, with `create-import-csv` (dry run first), `get-import-csv-errors` row by row, `retry-import-rows`, and scheduled imports that pull a supplier file from a link on a fixed timetable.

Helpdesk and messages: ticket search, ticket conversations, `reply-to-helpdesk-ticket`, internal notes, ticket status, plus automatic post-sale messages.

Automations and offers: trigger and action catalogs, automations such as tagging every order over $100, and rules that send automatic offers to buyers watching a listing.

Categories and field mapping are the part that decides whether a publish succeeds: `get-category-mappings`, `set-category-mappings`, `get-unmapped-categories`, `get-category-specifics` and `get-channel-category-fields` expose the mapping between a catalog category and what each channel actually requires.

## Installation

```bash
claude mcp add --transport http 3dsellers https://api.3dsellers.com/mcp
```

For Hermes:

```bash
hermes mcp add 3dsellers --url https://api.3dsellers.com/mcp
hermes mcp auth 3dsellers
```

The vendor documents four connect paths: Claude with a sign-in and no token to copy, ChatGPT, Grok, and developer tools such as Cursor, VS Code and Claude Code with a bearer token from Settings > Profile > API / MCP.

## Configuration

```json
{
  "mcpServers": {
    "3dsellers": {
      "type": "http",
      "url": "https://api.3dsellers.com/mcp"
    }
  }
}
```

A bearer token replaces the OAuth block for headless clients: add `"headers": {"Authorization": "Bearer <token>"}`. Tokens are shown once at creation and carry a scope, from `product:read` up to full access.

## What It Costs

The MCP server itself is included in every plan, including the free trial. The metered part is the work the agent performs, not the reading:

| Meter | Price | What it buys |
|---|---|---|
| AI Lite | $9 / month | 2,000 AI actions |
| AI Pro | $20 / month | 5,000 AI actions |
| AI Elite | $29 / month | 10,000 AI actions |
| Rate limits | included | 600 calls a minute and 50,000 a day on paid plans, shared by REST and MCP |

Reading your own data is free. Anything the assistant changes consumes an action, which is the right meter for this surface: an operator reading a catalog all day costs nothing, and a bulk repricing run is what actually has to be budgeted.

## Integration with CorpusIQ

The sequencing that earns its place: CorpusIQ already answers what the operator's own systems recorded, with orders and inventory from Shopify or Amazon Seller Central, spend from the ad connectors and cash movement from the accounting connector. This adds the marketplace edge of the same question, meaning what is published where, at what price, at what stock, and what a buyer asked that nobody answered.

Two uses that fit the product's own thesis: reconciling the catalog against what the marketplaces actually serve (the same SKU at three prices is a data disagreement an assistant can find in one pass), and drafting buyer replies from the ticket conversation while a person approves the send. The write surface is real and broad, so the safe shape is read-heavy by default and a small token scope for the write tools, rather than one full-access token wired into every session.

## Limitations

- **No tool call was made in this entry.** Every tool requires a 3Dsellers account with a connected selling account, and this sweep does not create accounts. The liveness claim rests on the live 401, the RFC 9728 document, the authorization-server metadata and the published tool tables.
- **The write surface is large and immediate.** Publishing, bulk edits, repricing, order tracking and buyer messages all change live marketplace state. The vendor mitigates with scoped tokens and an approval step before write tools, but the operator still chooses the scope.
- **It is eBay-shaped underneath.** The account policies, store categories and many listing fields are eBay concepts, with other channels mapped onto them. A Shopify-only seller gets a working but eBay-shaped data model.
- **AI actions are the real constraint.** Reads are free, but a month of agent-driven bulk work is limited by the action pack, not by the tool count.
- **Requires a paid or trial 3Dsellers plan.** The vendor documents `403 subscription_required` for accounts without an active plan or trial.

## FAQ

### Is there a free way to test it?

The free trial includes MCP access and free data reads, so a search over the catalog and a read of published listings can be done before paying for AI actions. There is no anonymous endpoint: an unauthenticated call returns 401.

### How is this different from the Amazon entries already here?

Those entries read Amazon deeply, and several of them read the seller's own Seller Central and Amazon Ads. This one is not a single-marketplace reader. It keeps one catalog and publishes it to eBay, Amazon, Walmart, Etsy, Shopify and TikTok Shop, which is a different question: not what Amazon says, but whether all six channels say the same thing.

### Can an agent change live listings with it?

Yes, and that is the point of the entry: publish, bulk repricing, inventory, order tracking and buyer replies are all write tools. Whether that is safe is a scope decision. The vendor supports narrow scopes such as `product:read`, logs every call with secret-looking values redacted, and allows revoking one token or all of them.

### What happens when a marketplace changes its API?

The vendor keeps the hosted server current, which is the stated reason for hosting rather than shipping a local package. The trade is that the integration is a vendor dependency, not something an operator can self-host.

## See Also

- [Nexscope MCP](/hermes/mcp/servers/external/nexscope-mcp)
- [AMZ Vault MCP](/hermes/mcp/servers/external/amz-vault-mcp)
- [Nova Amazon MCP](/hermes/mcp/servers/external/nova-amazon-mcp)
- [SellerMate MCP](/hermes/mcp/servers/external/sellermate-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
