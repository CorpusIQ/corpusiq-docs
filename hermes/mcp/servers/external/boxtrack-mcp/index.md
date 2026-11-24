---
title: "BoxTrack MCP - Home Inventory From Photos"
description: "Seven tools, two of them keyless and fully driven: a photo-to-inventory builder that totals a move at $4,052, and the cleanest connect-gate in this catalogue."
category: "Productivity"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-23
source: "A canonical mcpservers.org arrival at /servers/box-track-com-chatgpt stamped 2026-11-24T00:18Z; keyless initialize and tools/list on https://box-track.com/mcp answering 200 as boxtrack 1.0.0 with seven tools; show_home_inventory driven with five entries and returning 5 entries, 135 pieces and $4,052; five account tools returning isError with structuredContent.view=connect and a per-tool mcp/www_authenticate hint; the protected-resource document at https://box-track.com/.well-known/oauth-protected-resource/mcp and the pricing page at https://box-track.com/pricing, both read 2026-11-24"
relevance: "★★"
tags: [home-inventory, insurance, moving, property, mcp-apps, oauth, remote-mcp, productivity]
last_updated: "2026-11-23"
---

# BoxTrack MCP

**The insurance claim that gets paid is the one with a list: each thing, its photo, what it cost to replace, and the box it came out of.** BoxTrack is a home inventory app built around QR labels on boxes, and its MCP server does two different jobs in one endpoint: it builds an inventory from what a person describes or photographs, keyless, and it reads back an inventory the person already keeps, behind a connect step.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://box-track.com/mcp
Server name: boxtrack 1.0.0
Auth:        OAuth against a Supabase authorization server, scope "email"
Tools:       7 - two keyless, five that require a connected account
Pricing:     free demo, then $1.58 to $8.25 a month billed yearly
```

## Two doors, and the difference is measured

`initialize` and `tools/list` answer **200** with no credential, and the tool inventory is public:

```
show_home_inventory        entry count, pieces, totals, a per-room breakdown, a widget
home_inventory_checklist   the room-by-room list of what to photograph and record
find_my_stuff              account - "where are my passports?"
show_my_box                account - what is in one box
my_boxes                   account - the box list
my_inventory_value         account - what the stuff is worth
list_my_items              account - items by tag, fragile, shipping, sell
```

The two keyless tools were driven. `home_inventory_checklist` returns a real, specific instruction set rather than a marketing page: photograph each thing and each room, closet and open drawer; record brand, model and **serial number** for electronics and appliances; note when it was bought, what was paid and what replacement costs today; keep receipts or appraisals for valuables. It then walks the house room by room, and the details are the kind that only come from someone who has filed a claim: *"Fridge, stove, dishwasher and microwave, with model and serial numbers, if they're yours and not the landlord's"*, *"Count them roughly: about 120 books"*, *"Count the sets: 12 dinner plates, 8 wine glasses"*.

## The arithmetic, driven and checked by hand

`show_home_inventory` takes a `rooms` array and returns `text` for the model plus `structuredContent` for the client. Driven with five entries across two rooms:

| Room | Items | Room total |
| --- | --- | --- |
| Living room | sofa at $1,400, LG C3 65 inch TV at $1,300, 120 books at $8 | **$3,660** |
| Kitchen | 12 dinner plates at $6, coffee machine at $320 | **$392** |
| **Total** | **5 entries, 135 pieces** | **$4,052** |

Every figure reproduces by hand: 1,400 + 1,300 + (120 x 8 = 960) = 3,660; (12 x 6 = 72) + 320 = 392; and 3,660 + 392 = 4,052, with pieces 1 + 1 + 120 + 12 + 1 = 135. **`value` is a per-unit price multiplied by `quantity`, not a line total**, which is the single thing to know before handing it a list: 120 books at $8 is $960, not $8. The prose answer also carries the hedge the product requires, *"The values are estimates"*, and the response ships a `link` with its own UTM parameters and a standing instruction for the model to offer the free account.

## The refusal this catalogue will copy

Every account tool answers **HTTP 200** with `isError: true` and a payload built to be acted on rather than parsed as a failure:

```json
"structuredContent": {
  "view": "connect",
  "signup": "https://box-track.com/?try&utm_source=ai_app...",
  "app": "https://box-track.com/?utm_source=ai_app...",
  "season": {"key": "holiday", "label": "Holiday season",
             "line": "Year-end is the best time to update your home inventory for insurance.",
             "search": "holiday decorations"}
},
"_meta": {"mcp/www_authenticate":
  ["Bearer resource_metadata=\"https://box-track.com/.well-known/oauth-protected-resource/mcp\",
    error=\"insufficient_scope\",
    error_description=\"Connect your BoxTrack account to see your own boxes\""]}
```

Four details are worth taking from it. The refusal is **in band at the tool level**, not a transport error, so the conversation continues and the person is told what to do. It carries the **spec-shaped auth hint** in `_meta` with the protected-resource URL, the `insufficient_scope` error and a sentence in plain English. It carries a **machine-readable next step** (`view`, `signup`, `app`), which is what lets a client render a Connect button instead of a paragraph. And it is **seasonally personalised**: during this pass the payload offered a holiday-season line and a suggested search, which means the refusal text is a marketing surface the vendor can change without shipping a new tool.

The protected-resource document is one line and it is honest about what it grants:

```json
{"resource":"https://box-track.com/mcp",
 "authorization_servers":["https://fvxliyrbicskvrbejgtb.supabase.co/auth/v1"],
 "scopes_supported":["email"],
 "resource_name":"BoxTrack",
 "resource_documentation":"https://box-track.com/chatgpt"}
```

`email` is the only scope. There is no `inventory:read`, so as with Utleio in this catalogue, the token establishes identity and the authorisation boundary is the connection itself. An operator auditing what an assistant can reach here has to look at the app's own account model, not the token.

## MCP Apps, actually shipped

Both response shapes carry an app template in `_meta`: `ui://widget/boxtrack-inventory-v1.html` for a built inventory and `ui://widget/boxtrack-account-v1.html` for the connect prompt. That is the server-controlled UI layer - the assistant renders the vendor's HTML inside its own frame - and it is the clearest example in this catalogue of a refusal and a result both getting a designed surface rather than a wall of text. For anyone building a product surface today, this is worth reading as a pattern: the account gate is not a dead end, it is a screen.

## Pricing, as published

Read from `box-track.com` on 2026-11-24, billed yearly: **free demo** with 3 boxes of up to 20 items each and one sub-box of three, no card and no sign-up to try; **Starter $1.58 a month ($19 a year)** for up to 5 boxes with 10 AI photo scans a month; **Plus $4.08 a month ($49 a year)** for up to 49 boxes, unlimited AI scans including whole-box scans, the insurance report, Excel and CSV export, sharing and custom fields; **Unlimited $8.25 a month ($99 a year)** for unlimited boxes plus Pax, the AI assistant. Monthly billing is also offered. New accounts get a **72-hour trial** on any paid plan with no card, and a lapsed trial falls back to the free plan without deleting anything.

## How to use it

1. Add `https://box-track.com/mcp` as a remote server. The two keyless tools work immediately, which makes this one of the few servers here that a person can evaluate before creating an account.
2. For a claim or a move, ask for the checklist first, then give the inventory room by room in the assistant's own words or from photos of open boxes.
3. Connect the account only for the read-back tools (`find_my_stuff`, `show_my_box`, `my_boxes`), and expect the connect screen rather than an error.

## What this guide can and cannot certify

Measured: the endpoint, the handshake, all seven tool names and schemas with their annotations, two keyless responses in full, the arithmetic of a five-entry inventory, the connect-refusal payload and its auth hint, the protected-resource document, both app templates, and the published prices. Not measured: anything behind the account - whether `find_my_stuff` searches photo contents, voice notes or item names - and the accuracy of the AI photo scan the paid plans sell.

## Verdict

**Two stars as an operator tool, four as a design reference.** A home inventory is consumer work, and this catalogue does not pretend otherwise; what earns the entry is that the two keyless tools do real work, the totals reproduce to the dollar, and the connect gate is the best-built refusal measured here. If the pattern spreads - in-band, hinted, machine-readable and designed - agents will stop dead-ending at sign-in, which is worth more to this ecosystem than one more data connector.
