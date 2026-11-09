---
title: "Cotlet MCP - The Apps That Have No API"
description: "A hosted Chrome a business signs into itself, exposed as 719 tools across roughly 340 apps, with writes held for the owner's approval."
category: Commerce & Marketplace Operations
stars: "n/a (hosted; free workspace tools, credits for browser time)"
added: 2026-11-08
source: "the mcpservers.org thirteen-map canonical, which carried 19 cotlet-connect slugs as new in the eight-hour window; the official MCP registry records under dev.cotlet; and the endpoints themselves, where a keyless initialize answered 200 on the generic surface with 719 tool schemas and on the Fresha surface with 42"
relevance: ★★★★
tags: [browser-automation, no-api, field-service, booking, salons, hosted-chrome, credits, approval, remote-mcp]
last_updated: "2026-11-08"
---

# Cotlet MCP

**The systems a service business actually runs on mostly have no API.** The salon on Fresha, the cleaner on ZenMaid, the contractor on Contractor Foreman, the photographer on ShootProof, the auto shop on Tekmetric: each is a web application with a login, and none of them is going to hand a small business an API key. Cotlet answers that with a different architecture. It hosts a real Chrome per workspace, the owner signs into their own apps inside it, and the agent drives that browser through MCP, with typed tools for the apps where Cotlet has written them.

```text
Server type: Remote (Streamable HTTP)
Endpoints:   https://cotlet.dev/mcp/v1            generic surface, 719 tools
             https://cotlet.dev/mcp/v1/<app>      per-app surface, e.g. fresha (42 tools), skool, substack
Auth:        none to read the tool list; the user's own sign-in inside the Cloud Browser
Registry:    dev.cotlet/<app> records, e.g. dev.cotlet/fresha, dev.cotlet/bookingkoala
Charge:      credits, with a per-minute charge while a browser session is open
```

## What the endpoint says about itself

A keyless `initialize` on either surface answers **200** with the tool list and an instruction block that is unusually specific about safety. The generic surface returns **719** tools. The Fresha surface returns **42**. The instructions state the architecture in one line: Cotlet runs the user's own Chrome in the cloud, the user signs in there themselves, and **Cotlet does not store their passwords**. They go further than most vendors will: on a sign-in page, a two-factor prompt or a step that needs a person, the agent must **stop and give the user the browser link**, and must never ask for a password or type one. Ask before a step that sends, publishes, deletes or pays. Close the browser when the task is done, because each started minute costs credits.

## Two layers: typed operations, and a browser as the fallback

The per-app tools are the readable half. Every integration appears as a `_read` and a `_write` pair, with the operation named in `operation` and its inputs in `arguments`:

```text
fresha: list_appointments, get_appointment, list_clients, get_client, list_services,
        list_team_members, find_available_slots, get_sales_summary, list_sales,
        list_reviews, create_appointment, reschedule_appointment, cancel_appointment,
        add_client, add_client_note, add_blocked_time, reply_to_review
```

That is a working salon front desk, not a wrapper around five endpoints. The same shape repeats across the catalogue: `skool` carries 30 read and 41 write operations, `tradify` 11 and 12, `spyfu` 11 and 3, `woocommerce` 6 and 5, `zendesk` 7 and 5. The apps cover the operational core of small business: booking and field service (Fresha, Booksy, ZenMaid, Squire, Appointy, Setmore, FieldEdge, RazorSync, Contractor Foreman, Workiz, Service Autopilot, Service Fusion, Simpro, Tradify, AroFlo, ServiceTrade, Yardbook), photography studios (Pixieset, ShootProof, SmugMug, Studio Ninja), auto shops (Tekmetric, AutoLeap), restaurants (Toast), property management (AppFolio, Yardi Breeze, VaultRE), plus CRM, HR, e-signature and social publishing surfaces.

Where no typed tool exists, the browser layer takes over, and it is a real one: **25 tools** for open, navigate, read, find, screenshot, scroll, click, hover, drag, type, fill form, select, press, upload, download, evaluate, wait, tabs and close. Pages are read as numbered elements, so the agent acts on a number rather than a guessed selector. That combination is the interesting part: a typed operation where Cotlet has done the work, a browser where nobody has.

## The governance decisions that make it usable

Four are stated by the server, and all four are the kind of thing an operator should test before trusting any browser-based connector:

- **Writes that reach other people wait for approval in the Cotlet console.** The call returns `pending` with a `call_id`, and `cotlet_get_call` reports when the owner approved it. That is a proper human checkpoint, not a warning in a prompt.
- **The user signs in, not the platform.** Passwords are never asked for and never typed by the agent, and a two-factor prompt is a stop-and-hand-over, not a workaround.
- **Free identity and inventory tools.** `cotlet_whoami`, `cotlet_apps`, `cotlet_balance` and `cotlet_app_guide` cost nothing, so an assistant can report the account, the connected apps, the credit balance and the app-specific instructions before spending anything.
- **Automations that run without a model.** `cotlet_automation_guide`, `_test`, `_save`, `_list`, `_rows` and `_control` turn a tested browser flow into a scheduled job, tested with **every write skipped**, and the instructions require the rows and the cost to be shown to the user before saving. A job that runs on a schedule with no model in the loop is the honest answer to "make this repeat".

## The class it enters, and what is new about it

This catalogue has connectors to individual business systems and a few browser tools, but this is the first entry built on the premise that most small-business software has no API at all and never will. It is not a scraper: the browser is the user's own session, with the user's own rights, and the agent is a very fast operator sitting at their desk. It is also not a general automation platform, because the operations are typed per app rather than clicks recorded once.

For a business operator the practical value is the long tail: the salon software, the cleaning rota, the trades scheduling system and the photography gallery are usually the four systems a service business cannot get data out of, and they are exactly the four with no developer in the room.

## Limits, stated as limits

Cost model is credits and per-minute browser time, so a long conversation that keeps a session open is a meter running, and `cotlet_balance` is the tool to call first. The typed operations cover what Cotlet has written: a missing operation is missing, and the vendor says so directly, since a catalog description or a guide screenshot **proves no feature**. The browser path inherits the fragility of every web UI: a redesign breaks a step, and the server's own remedy is to report the issue rather than to guess. Acting inside a signed-in session means the agent holds the person's full rights in that app, which is why the approval checkpoint on outward writes is not optional in practice.

## Frequently asked questions

### How does it reach an app that has no API?

Through the Cloud Browser: a real Chrome hosted by Cotlet, signed in by the user, driven by 25 browser tools that read a page as numbered elements. Where Cotlet has written typed operations for an app, those are used instead, and they are faster and more reliable.

### Are passwords stored?

The server states that Cotlet does not store the user's passwords, and its instructions forbid the agent from asking for one or typing one. A sign-in prompt or a two-factor challenge is handed back to the person as a browser link.

### Who approves a write that reaches a customer?

The owner, in the Cotlet console. The tool call returns `pending` with a `call_id`, and nothing goes out until it is approved. The agent can poll the status through `cotlet_get_call`.

### Can a recurring job run without a chat window open?

Yes. An automation is a tested script saved on a schedule, and runs need no model and no open chat. The test run executes with writes skipped, and the cost and rows are supposed to be shown before the automation is saved.

### Why is the tool count so different between the two endpoints?

`https://cotlet.dev/mcp/v1` is the whole workspace in one place, **719** tools. `https://cotlet.dev/mcp/v1/<app>` is one app, for example **42** on Fresha. A busy assistant benefits from the narrow surface, since a shorter tool list is a smaller mistake to make.
