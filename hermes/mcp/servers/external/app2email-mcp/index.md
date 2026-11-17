---
title: "app2email MCP - WhatsApp Business From an Agent"
description: "One endpoint, 20 tool sets and an approval gate: WhatsApp templates, flows, bookings and payments from an assistant, plus a quiet sandbox."
category: "Messaging / WhatsApp Business"
stars: "n/a (hosted, OAuth or bearer key; 20 tool sets, 211 documented tool slots)"
added: 2026-11-17
source: "the mcpservers.org sitemap shard servers/12.xml (slug app2email/mcp) and the vendor's own MCP reference read 2026-11-17; the endpoint answered HTTP 401 to an anonymous handshake"
relevance: ★★★
tags: [whatsapp, business-messaging, templates, flows, bookings, payments, approvals, oauth, remote, mcp]
last_updated: "2026-11-17"
---

# app2email MCP

**A WhatsApp number is where a small business actually talks to customers, and it is the last surface an assistant can reach.** Email has an API and a thousand wrappers; a WhatsApp Business number needs a template library, an opt-in record, a do-not-call list and an approval trail before anything may be sent. That is why most agent email work stops at email.

app2email exposes the whole WhatsApp Business surface over one endpoint and splits it into **twenty tool sets** that can be connected individually or combined, which matters for clients with a tool cap. Two properties make it worth cataloguing rather than filing under messaging: a **sandbox key that sends nothing to WhatsApp**, and a dedicated **Approvals** set whose `approve_send` tool is a gate inside the surface rather than a promise in the documentation.

```
Server type:   remote Streamable HTTP
Endpoint:      https://api.app2email.com/mcp
Auth:          OAuth (sign in, choose the number and the scope) or Authorization: Bearer <API key>
Protocols:     2026-07-28, 2025-11-25, 2025-06-18, 2025-03-26, 2024-11-05
Tool sets:     20, from 2 tools (account) to 43 (submit-info)
Sandbox:       a sandbox key sends nothing to WhatsApp
Listed on:     mcpservers.org, sitemap shard servers/12.xml
```

## The evidence tier

**Gated endpoint, documented surface with an enumerated tool map.** An anonymous `initialize` to `https://api.app2email.com/mcp` answered HTTP **401**, so the route exists and refuses unauthenticated callers; no tool schema was read directly. What was measured is the protocol claim and the tool map: the vendor's MCP reference lists the five protocol revisions the server speaks, which is the widest version span seen in this catalogue, and enumerates every tool set with its tool count and the names inside it.

The counts are worth recording because they are the sizing decision: **`messaging` 16**, **`messages` 12**, **`media` 4**, **`conversations` 5**, **`templates` 15**, **`broadcasts` 4**, **`account` 2**, **`do-not-call` 4**, **`contacts` 8**, **`approvals` 3**, **`webhooks` 10**, **`analytics` 4**, **`book-and-pay` 13**, **`calendar` 12**, **`calling` 3**, **`flows` 12**, **`number` 14**, **`payments` 7**, **`order-and-pay` 20**, **`submit-info` 43**. Every set carries `check_key` as its first tool, so the per-set counts include one shared diagnostic.

## Tools & Capabilities

| Set | Count | Representative tools |
|---|---|---|
| `messaging` | 16 | `send_text`, `send_template`, `send_media`, `send_interactive`, `list_messages`, `list_conversations`, `wait_for_message`, `upload_media` |
| `messages` | 12 | `send_message`, `send_reaction`, `send_location`, `mark_read`, `get_marketing_status` |
| `templates` | 15 | `list_templates`, `create_template`, `edit_template`, `compare_templates`, `upsert_auth_template`, `get_template_insights` |
| `approvals` | 3 | `list_approvals`, `approve_send` |
| `do-not-call` | 4 | `list_donotcall`, `add_donotcall`, `remove_donotcall` |
| `contacts` | 8 | `list_contacts`, `upsert_contact`, `block_users`, `check_contact_book` |
| `book-and-pay` | 13 | `get_booking_availability`, `create_booking`, `cancel_booking`, `send_flow`, `list_waitlist` |
| `order-and-pay` | 20 | `get_shop`, `search_shop_items`, `create_shop_order`, `quote_shop_order`, `refund_shop_order` |
| `payments` | 7 | `request_payment`, `refund_payment`, `create_meeting_poll`, `erase_customer_data` |
| `flows` | 12 | `list_flows`, `create_flow`, `publish_flow`, `get_flow_preview` |
| `number` | 14 | `get_number_health`, `set_profile_photo`, `set_conversation_starters`, `create_qr_code` |
| `submit-info` | 43 | The largest set, for structured intake over chat |

The vendor's documented smoke test is `check_key`, then `list_templates`, which is a good first call for any new connection.

## Installation

```json
{
  "mcpServers": {
    "app2email": {
      "type": "http",
      "url": "https://api.app2email.com/mcp",
      "headers": { "Authorization": "Bearer ${APP2EMAIL_API_KEY}" }
    }
  }
}
```

Clients that can complete OAuth need no key: connect the URL, sign in, then choose the WhatsApp number, what the app may do, and whether it is a sandbox. The resulting key appears on the API key page as `OAuth: <app>` and is revoked there. Clients with a tool cap can connect a subset, either as `https://api.app2email.com/mcp/<set>` or as `?tools=<set>,<set>`; every tool remains callable by name.

## Why This Matters for Operators

The dangerous part of agent messaging is not the send, it is the send that should not have happened: to someone who opted out, to a number on the do-not-call list, or outside the approved template. This surface puts the three relevant controls inside the tool list, with **`approve_send`** as a separate step, `add_donotcall` as a first-class operation, and a sandbox mode that exercises the whole path without touching WhatsApp. That combination is what makes it safe to let an agent draft in production.

## Questions operators ask

### Can an agent send to anyone?

Only through the paths the surface exposes: templates, text, media and interactive messages, with the do-not-call and opt-in sets beside them. The approvals set exists precisely so a send can be queued and released by a human rather than by the model that drafted it.

### How does the sandbox differ from production?

A sandbox key sends nothing to WhatsApp, per the vendor's documentation, so a full workflow can be rehearsed against real templates and flows without a customer receiving anything. That is the correct place to run the first week of any agent-driven outreach.

### Which protocol version will it negotiate?

The server advertises five revisions, from **2024-11-05** to **2026-07-28**, and a client negotiates upward from what it supports. That span is unusually wide and means older clients stay usable.

## Related

- [WhatsApp Business Tools MCP](/hermes/mcp/servers/external/whatsapp-business-tools-mcp) - Meta's own WhatsApp Business surface
- [1Lookup MCP](/hermes/mcp/servers/external/1lookup-mcp) - phone and email verification before a send
- [MCP Specification 2026-07-28](/hermes/mcp/mcp-spec-2026-07-28) - the newest revision this server speaks
