---
title: "Vizbl MCP - AR Try-On Widgets for Store Products"
description: "OAuth remote MCP for ecommerce AR: convert 3D models, build try-on widgets for Shopify, WooCommerce and Wix, get AR links and embed code."
category: "Commerce / AR"
stars: "n/a (hosted, OAuth 2.0 with dynamic client registration; 40+ tools documented)"
added: 2026-11-17
source: "the mcp.so feed card stamped 2026-11-17T07:12:56Z and the vendor's own connector documentation at developer.vizbl.com/docs/mcp, read 2026-11-17; the endpoint refused an anonymous handshake with HTTP 403"
relevance: ★★
tags: [ecommerce, shopify, woocommerce, ar, virtual-try-on, 3d, widgets, oauth, remote, mcp]
last_updated: "2026-11-17"
---

# Vizbl MCP

**The product photo is the last unmeasured step in online retail.** A shopper cannot put a rug in their room, hold a poster at its real print size, or see how a jacket hangs, so the return is often the first time the product meets the buyer. Vizbl's connector exists to close that gap from inside an assistant: upload or convert a model, place it on a product, and get back the widget code the storefront needs.

What makes it a catalogued surface rather than another ecommerce listing is the shape of the write path. **Read and write are separate tools, and destructive tools ask for confirmation first**, and a connection approved for reading only does not list the write tools at all. Several tools work with no account, so the cost side of the decision can be priced before anything is installed.

```
Server type:   remote Streamable HTTP
Endpoint:      https://mcp.vizbl.com/mcp
Docs:          https://developer.vizbl.com/docs/mcp
Transport:     Streamable HTTP
Auth:          OAuth 2.0 with dynamic client registration; an optional Developer API key adds analytics, usage and team tools
Tools:         40+ documented, split read / write / destructive
Platforms:     Shopify, WooCommerce, BigCommerce, Wix, custom sites
Listed on:     mcp.so feed, stamped 2026-11-17T07:12:56Z
```

## The evidence tier

**Documented surface, gated endpoint.** An anonymous `initialize` to `https://mcp.vizbl.com/mcp` answered **403** from the edge, so no tool schema was read directly, and this page says so rather than presenting the vendor's documentation as a measured schema. What was read is the vendor's own connector documentation, which names the endpoint, the transport, the OAuth flow with dynamic client registration, and the tool list by area with each tool's access class.

The tier is still useful because the documentation is unusually specific about the boundary between free and keyed work: `get_guide`, `estimate_costs` and the conversion tools answer without an account, and everything that touches a store or a catalog needs a secret key with the matching access chosen on the consent screen.

## Tools & Capabilities

| Area | Tools | What they answer |
|---|---|---|
| No account needed | `get_guide`, `estimate_costs`, `convert_3d_model`, `get_job_status`, `create_public_upload_url`, `get_ar_link`, `get_qr`, `get_widget_snippet`, `generate_wallart_buttons`, `get_install_instructions`, `list_tryon_types` | The guide for a topic, an expected monthly token budget from traffic and catalog size, a 3D or CAD file converted to GLB, USDZ or FBX, AR links and QR codes, and per-platform install code |
| Library and models (key) | `list_models`, `get_model`, `create_upload_url`, `upload_model`, `update_model`, `publish_model`, `set_model_activation`, `get_model_links`, `delete_model` | Catalog search, imports, edits, publishing a draft, and linking a model to the products that show it |
| Rugs, flooring and rooms (key) | `list_rugs`, `list_floorings`, `create_rug_from_photo`, `add_rug_size`, `update_rug`, `list_rooms`, `add_room`, `remove_room` | Kits and size or colour variants, a 3D rug built from a flat photo at real dimensions, and the preview rooms in the viewer |
| AI Try-On (key) | `get_tryon_widget`, `set_shopify_tryon` | The try-on embed code for a product type, and per-product try-on toggles on a linked Shopify store |
| Account, analytics, keys, team (key) | `get_account`, `get_pricing`, `get_usage`, `create_checkout_link`, `list_invoices`, `get_analytics`, `list_api_keys`, `create_public_key`, `revoke_key`, `get_domains`, `set_domains`, `list_members`, `invite_member`, `revoke_invite` | Balance and plan features, token spend by action, invoices, widget analytics, publishable keys, allow-listed storefront domains, team invitations |
| Shopify (key) | `list_shopify_products`, `link_model_to_product`, `unlink_model`, `list_shopify_posters`, `set_poster_active`, `submit_request` | The linked store's products and variants, and which ones show a model or a wall-art poster |

**A limit worth knowing before the trial.** Generating try-on images inside the chat is not exposed. The tools install the widget; shoppers run try-on on the storefront, and that is what spends tokens. An assistant cannot be used as a bulk image generator through this connector.

## Installation

Add `https://mcp.vizbl.com/mcp` as a remote MCP server and complete the OAuth consent screen, choosing what the connection may do. Any client with remote MCP plus OAuth works, including Claude and Claude Code. Clients that cannot complete OAuth can use a Developer API key instead, which also unlocks the analytics, usage and team tools.

## Why This Matters for Operators

Return rate is where ecommerce margin quietly disappears, and the fix has always been a rendering project. The connector turns that project into a sequence of tool calls: convert the model once, publish it, link it to variants, and take the embed code for the platform the store actually runs on. Pricing is also answerable before commitment, because `estimate_costs` turns traffic and catalog size into a token range with its assumptions attached.

## Questions operators ask

### What does a read-only connection actually prevent?

According to the vendor's documentation, a connection approved for reading only does not list the write tools at all, so the tool surface itself shrinks rather than each write being refused at call time. That is the stronger of the two designs.

### Can an assistant delete things?

`delete_model` is marked destructive and requires confirmation before it runs. `set_model_activation` is the reversible alternative that takes a product off its widgets without deleting the object.

### Where does the token spend come from?

Two places: the conversion and generation work done on the vendor's servers, and shopper-side try-on impressions on the storefront. `get_usage` reports token transactions and spend by action, and `estimate_costs` forecasts the monthly range.

## Related

- [Shopify Speed Check MCP](/hermes/mcp/servers/external/shopify-speed-check-mcp) - the performance side of the same storefront
- [MCP Apps - Interactive UI in the Client](/hermes/mcp/mcp-apps-interactive-ui) - why an in-conversation widget is a different surface from a link
