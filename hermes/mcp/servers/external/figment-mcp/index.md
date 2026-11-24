---
title: "Figment MCP - A Mac Rented by the Hour, Ordered by an Agent"
description: "Eight keyless tools that let an assistant rent real macOS by the minute: three plans priced in cents, a Stripe link the human pays, and a stop call that ends billing."
category: "DevOps"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "An mcp.so feed card at 2026-11-24T16:25Z for /servers/figment-mac-hostingfigment-mac-hosting; keyless initialize and tools/list on https://figment.so/api/mcp answering 200 with serverInfo figment-mac 1.0.0 and eight tools on 2026-11-24; figment_get_offer driven live the same day, returning offer_version mac-offer-2026-11-17 with three plans and every price in US cents; figment_get_mac and figment_stop_mac driven with a bogus id and refusing in band for a missing api_key; plan positioning and CI runner targets from https://figment.so/ on 2026-11-24"
relevance: "★★★"
tags: [macos, ios-ci, xcode, mac-hosting, cloud-vm, agent-payments, stripe, ssh, keyless, remote-mcp, devops]
last_updated: "2026-11-24"
---

# Figment MCP

**The job that needs a Mac is never the job anyone planned for: an iOS build, a Safari-only bug, a `.app` that has to be signed on real hardware.** Figment rents macOS by the hour, the day or the month and exposes the whole rental as eight keyless MCP tools, which makes it the first entry in this catalog written for the case where the **agent** is the customer and a **person** pays the bill.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://figment.so/api/mcp
Auth:        none for the offer; an agent account api_key for everything else
Tools:       8 - get_offer, create_account, get_account, buy_credit,
             start_mac, get_mac, get_mac_access, stop_mac
Pricing:     $0.15/hour Intel VM, $0.40/hour shared M4 Pro VM,
             $1.00/hour dedicated M4 Pro; prepaid credit, $25 minimum first buy
```

## The gate, measured

There is no gate. `initialize` with no credential answers **200** and names itself:

```json
{"protocolVersion":"2025-06-18",
 "capabilities":{"tools":{"listChanged":false}},
 "serverInfo":{"name":"figment-mac","title":"Figment Mac hosting","version":"1.0.0"}}
```

`tools/list` then returns **eight** tools with full schemas. That is rare enough in this catalog to state plainly: most servers here refuse keyless and the guide has to reason from an OAuth chain. This one lets a stranger read the price list and the tool descriptions before any account exists, which is the correct amount of openness for a product whose first useful answer is "what does this cost".

The server's `instructions` string is also worth quoting, because it is the vendor writing rules for a model rather than for a human:

> *Order: figment_get_offer, figment_create_account (once; keep the api_key), figment_buy_credit (your user pays the link), figment_start_mac, figment_get_mac until state is "ready", figment_get_mac_access, and figment_stop_mac when the task is done. Setup is not instant. Never promise a start time, and never show the Mac password in chat.*

Two of those sentences exist because of how the product fails: provisioning takes minutes and a model will happily promise "ready in 60 seconds", and a Mac password in a chat transcript is a credential leak with a screenshot attached.

## The three plans, driven live

`figment_get_offer` with no arguments returns the whole commercial offer as JSON. Measured **2026-11-24**, `offer_version mac-offer-2026-11-17`, currency USD, region US East:

| Plan | Hardware | Hour | Day | Month | Available now |
| --- | --- | --- | --- | --- | --- |
| `intel-vm` | 4 shared vCPUs, 4GB RAM, 80GB SSD, macOS Sequoia on KVM | $0.15 | $2.00 | $25.00 | **false** |
| `apple-silicon-vm` | Shared M4 Pro VM, 4 shared vCPUs, 4GiB RAM, 50GB SSD | $0.40 | $6.00 | $69.00 | **true** |
| `dedicated-m4-pro` | 12-core M4 Pro, 24GB RAM, 512GB SSD, iMessage available | $1.00 | $15.00 | $199.00 | **false** |

The Intel plan carries its own warning inside the payload and it is not marketing hedging: **no GPU, no Metal acceleration**, Apple-silicon-only workloads do not run, and **Xcode stops at the version that supports Sequoia (26.3)**. The vendor's site repeats the consequence: Xcode after 26.3 needs an Apple Silicon plan. An assistant that picks the cheapest plan for an iOS 18 simulator job will pick the one that cannot do it, so the plan choice is a decision to make explicitly rather than a default.

`available_now: false` is not a refusal, it is a statement about inventory: **an order is refused unless `allow_wait` is true**. At the time of this capture only the shared M4 Pro VM was free, so the two quieter plans were subject to a queue the agent cannot estimate. The instructions say never promise a start time; the payload is why.

## Money, and where the human stays in the loop

This is the part other agent-facing vendors have not solved, and Figment's answer is a design worth describing precisely.

- **Prepaid only.** `figment_buy_credit` does not charge a card. It **returns a Stripe Checkout link**, and the link is paid by a person, or by an agent holding a Link wallet. The first purchase is at least **2,500 cents ($25)** and the ceiling is **50,000 cents ($500)**.
- **`figment_create_account` needs no sign-in and no credit.** It returns an **`api_key` exactly once**, and the instructions tell the model to keep it rather than make a new account per task. So an agent can exist before it can spend.
- **Hourly is billed by the minute**, starting when the order is accepted and stopping **when the rental is ended through the stop endpoint or the credit runs out**. The payload is explicit: **"A guest shutdown alone does not stop charges."** A Mac shut down from inside its own guest keeps costing money, which is the single most expensive misunderstanding this product can have.
- **Daily means 24 hours from the order**, does not renew unless `renew_daily` is true, and **stopping early does not refund the day**.
- **Monthly is not sold through this API** at all; it is ordered on the website.
- **Unused credit does not expire and is not refunded.** If a Mac fails before it was ever delivered, that credit is returned to the account.

The ceiling on waste is structural: **two running Macs per account**, so the worst case for a runaway agent is two machines on a prepaid balance it cannot exceed. Combined with a $25 minimum, that is a budget an operator can authorise once and stop worrying about, which is the argument for prepaid credit over a stored card.

## What the access actually is

`figment_get_mac_access` returns the **SSH host and port**, optionally a **one-time link to the screen in a browser** (`console: true`) and login details (`login: true`). The plan includes **remote desktop over an encrypted connection, SSH, browser access and administrator rights**. The split of responsibility is stated plainly: the vendor runs the Mac, the network and the virtualisation and fixes infrastructure faults; the operator manages apps, code, agents and third-party accounts. Support is **dashboard tickets with email replies seven days a week, answered within 24 hours, usually sooner**, at `support@figment.so`.

On the site, the use cases are the ones a Mac is genuinely needed for: **building, signing and shipping iOS and Mac apps**, running the **iOS Simulator**, testing **Safari** the way Apple users see it, **AppleScript and Shortcuts** against apps with no API, and **iCloud data** under the user's own Apple account. It also names CI as a first-class target: adding the Mac as a runner to **GitHub Actions, GitLab, Jenkins or Buildkite**. That is the honest framing: Linux stays the right choice for backend work, and the Apple part of the job goes to a Mac.

## Error paths, driven

Two tools were called with a fabricated Mac id and both behaved the way a client needs them to. `figment_get_mac` and `figment_stop_mac` answered **HTTP 200** with a JSON-RPC result whose payload is:

```json
{"error":"unauthorized",
 "message":"Send the api_key from POST /accounts as \"Authorization: Bearer ***\"."}
```

with **`isError: true`** on the result. The credential error arrives **in band**, in a message that names the fix, rather than as an unexplained HTTP 401. For a client that renders tool errors badly this is the difference between a dead end and an instruction. It also confirms the account model: everything except `get_offer` and `create_account` needs the `api_key` from the account call.

## How to use it

1. Call `figment_get_offer` before anything else. It is free, keyless, and names which plans are actually free right now.
2. Call `figment_create_account` **once**, keep the `api_key`, and store it as a secret rather than in a conversation.
3. Call `figment_buy_credit` and hand the Stripe link to the person who pays. $25 is the first purchase and it buys roughly **166 hours** of shared M4 Pro or **25 hours** of the dedicated Mac, so the plan choice decides how far the credit goes.
4. Call `figment_start_mac` with the plan the **job** needs, not the cheapest one, and set `allow_wait` deliberately.
5. Poll `figment_get_mac` **no more often than every 30 seconds**, as the tool description instructs, until the state reads `ready`. Do not estimate the time in the meantime.
6. Take access with `figment_get_mac_access`, do the work, and **always** finish with `figment_stop_mac`. The rental does not end because the guest was shut down or the task finished.
7. On the way out, `figment_get_account` shows the balance, the Macs and their states, and a **claim link** that puts the account in a browser for the person who paid.

## Boundaries recorded

- **Provisioning time is unknown by design.** The payload says setup is not instant and the instructions forbid promising a start time. A workflow that needs a Mac in under two minutes is not a fit, and no measured provisioning duration exists in this pass.
- **The retention clock is the vendor's, not ours.** The offer states that when a rental ends, recoverable data is kept **seven days and then deleted**. Anything that must survive belongs somewhere else.
- **No public repository.** The API reference is an OpenAPI document (`/api/agent/v1/openapi.json`) and a guide for agents (`/agents.md`), and the MCP surface mirrors them.
- **Two of the three plans were out of stock at capture.** Availability moves; the offer call is the only honest source, and a guide that quotes `available_now` as fact would be wrong within the hour.
- **Agent-purchased compute is a new risk class.** The human stays in the money loop through Stripe, and the blast radius is capped at prepaid credit and two Macs, but an operator authorising this is authorising an agent to spend a balance unattended. Set the balance to the experiment, not to the quarter.
