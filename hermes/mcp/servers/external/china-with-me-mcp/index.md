---
title: "China With Me MCP - Sourcing and AQL Inspections"
description: "A keyless China sourcing server with published fees, a trade-show directory of 143 upcoming shows, and an ISO 2859-1 sampling calculator."
category: "Procurement / Manufacturing"
stars: "0 (consultancy service; the MCP server is keyless and remote)"
added: 2026-11-14
source: "the mcp.so submission #7338 filed 2026-11-14T14:05:33Z, the official registry record com.chinawithme/b2b-mcp 2.1.2 active and published 2026-11-13, the published exhibition feed at https://chinawithme.com/data/exhibitions.json read the same day, and a live session on this host: initialize, tools/list and six tools/call requests against https://mcp.chinawithme.com/mcp"
relevance: ★★★
tags: [china, sourcing, manufacturing, prototyping, trade shows, canton fair, aql, quality inspection, iso 2859, procurement, supply chain, mcp, remote]
last_updated: "2026-11-14"
---

# China With Me MCP

**The last mile of hardware sourcing is a plane ticket.** An agent can find a supplier list, draft an RFQ and compare quotes, and then it stops, because somebody has to stand in a booth in Shenzhen, ask the factory engineer whether the quoted MOQ is real, and work out how many units to pull from a finished lot before accepting it. Those are the three steps that decide whether a hardware project ships, and they are all done by a person in a room.

China With Me is a one-consultant service built on exactly those three steps, and it publishes them as a keyless MCP server: a trade-show directory of upcoming Chinese exhibitions, a remote booth-visit service with published day rates, a prototyping scope tool with a phase-by-phase fee structure, and an **ISO 2859-1 sampling calculator** that returns the accept and reject numbers for an inspection before anyone books one.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, no session header issued
Endpoint:      https://mcp.chinawithme.com/mcp
Server:        chinawithme-b2b-mcp 2.1.2, protocol 2024-11-05, capabilities: tools
Registry:      com.chinawithme/b2b-mcp 2.1.2, streamable-http, same URL,
               status active, published 2026-11-13 (2.0.0 through 2.1.2 all active)
Auth:          none
Tools:         6
Exhibitions:   143 upcoming shows, expired shows excluded, as of 2026-11-15 CST
```

## The evidence tier

Keyless and drivable. `initialize` answered **200** with `serverInfo` **chinawithme-b2b-mcp 2.1.2** on protocol **2024-11-05** and **no `Mcp-Session-Id`**, and six `tools/call` requests were made across four tools. The two tools that open a human intake - `request_remote_exhibition_viewer` and `book_consultation_or_quote` - were deliberately **not** driven, and this guide says so rather than presenting their output as measured.

## The fees, read out of the tool

`get_services_and_pricing` returns the whole service catalog with USD prices, which is the part that makes this server worth a guide: a consultant's rate card is normally a conversation, and here it is a JSON object.

| Service | Price | What it covers |
|---|---|---|
| Feasibility and DFM review | 499 | Design-for-manufacture review before tooling |
| Turnkey prototype sprint | from 4,500 | EVT/DVT pilot run, 10 to 100+ units |
| Typical 4 to 6 week EVT/DVT sprint | 4,500 to 7,500 | The range the vendor quotes for that sprint |
| On-site engineering management | 450 per day | In-person factory work at a Shenzhen or Dongguan supplier |
| Post-visit 30-day execution support | 800 | Follow-through after the trip |
| Remote exhibition viewer, single day | 299 | A specialist walks one show on your behalf |
| Three-day full fair sprint | 799 | Same, across a full fair |
| Post-fair sample consolidation | 149 | Samples collected and shipped together |

The consultancy is disclosed in the tool output itself: a named independent consultant in Shenzhen and Singapore, with contact details, and a service catalog keyed on four pillars - prototyping, exhibition, sourcing and interpreting.

## The inspection calculator, reproduced by hand

`estimate_aql_inspection` takes a lot size and returns the sampling plan under **ISO 2859-1 / ANSI ASQ Z1.4, General Inspection Level II**, with AQL **2.5 Major** and **4.0 Minor**. Four lot sizes were driven and every one was checked against Table I and Table II-A by hand:

| Lot size | Code letter | Sample size | AQL 2.5 accept / reject | AQL 4.0 accept / reject | Man-days |
|---|---|---|---|---|---|
| 150 | F | 20 | 1 / 2 | 2 / 3 | 1 |
| 1,200 | J | 80 | 5 / 6 | 7 / 8 | 1 |
| 5,000 | L | 200 | 10 / 11 | 14 / 15 | 2 |
| 12,000 | M | 315 | 14 / 15 | 21 / 22 | 2 |

Every cell matched the standard: lot **5,000** sits in the **3,201 to 10,000** band, which is code **L** and **200** units, and at that sample size AQL 2.5 is **Ac 10 / Re 11** and AQL 4.0 is **Ac 14 / Re 15**. The service also states the execution model honestly - the inspection is fulfilled by accredited third-party QC partners, not by the consultant - and returns the booking URL rather than pretending the calculator is the service.

**The limit that matters:** the schema accepts **only `lot_size` and `city`**. There is no parameter for inspection level, AQL value or single versus double sampling, so this is one fixed plan rather than a calculator you can retune. For a 1.5 AQL critical-defect plan or a tightened inspection after a bad history, it will not answer.

## The exhibition directory

`search_china_exhibitions` returns **143** upcoming shows with expired ones excluded, stamped `as_of_date_cst: 2026-11-15`. The query is a keyword filter, not a full-text search: `electronics` narrowed 143 to **40**, and results carry `name_en`, `name_zh`, `abbreviation`, `category`, `subcategories`, `city`, `venue` and hall data, so an agent can tell a Canton Fair pavilion from a regional plastics expo before suggesting a flight.

The response also publishes the machine-readable feed it is built from, `https://chinawithme.com/data/exhibitions.json`, which answered **200** at **278,289** bytes with **146** records on the same day. The difference is explained by the tool's own `expired_shows_excluded` flag rather than by a stale cache, and it is the reason to read the tool's count and the feed's count as two different things.

## What the prototyping scope tool returns

`scope_hardware_prototyping_china` is a structured intake rather than a quote. For a CNC-machined aluminium enclosure with PCBA and IP67 sealing at a 500-unit pilot it returned a manufacturing-tier strategy - ISO 9001 and ISO 13485 contract manufacturers in Shenzhen and Dongguan with in-house tooling, DFM and automated PCBA SMT lines - and a two-phase engagement:

- **Phase 1, remote screening at 800**: verify 5 to 10 candidate factories, check small-batch MOQ flexibility, rank the shortlist.
- **Phase 2, on-site at 450 per working day**: factory audits, engineering reviews and prototyping management, with **40% deposit to reserve dates and 60% at the end of the trip**.

That deposit split is the kind of term an agent should surface to the person before anyone commits, and it comes out of the tool rather than a proposal PDF.

## What does not work

- **Two tools open a human intake** and were not driven: `request_remote_exhibition_viewer` and `book_consultation_or_quote` both collect a name, an email and a phone number, which is a booking form rather than a query.
- **The AQL plan is fixed** at General Level II, 2.5 Major and 4.0 Minor. No parameter changes it.
- **No session header** is issued, so a client that expects one must not require it; the server is stateless between calls.
- **The exhibition count differs between surfaces**: 143 from the tool with expired shows excluded, 146 in the published feed. Both are dated, and neither is wrong - they answer different questions.
- **The pricing carries no validity date.** A rate card read from a tool has no expiry field, so a quote from it should be confirmed before it is repeated to a customer.

## Frequently asked questions

### Does China With Me MCP need an API key?

No. The handshake and all six calls in this pass answered without a credential, and the server issues no session header.

### Is the inspection calculator a substitute for a QC provider?

No, and the tool says so itself: it returns the sampling plan and the man-day estimate, then states that the inspection is fulfilled by accredited third-party partners and offers a booking URL.

### Can it book a booth visit for me?

It can prepare the request. `request_remote_exhibition_viewer` collects the client details and the show, which starts a human booking rather than completing one.

### Which shows does it cover?

Chinese exhibitions, currently 143 upcoming after expired shows are excluded, across categories that include electronics, medical, printing and industrial equipment, with Canton Fair and the Shenzhen high-tech fairs among them.

## Limits recorded

One consultancy, one country, USD pricing with no validity date. The inspection calculator implements a single ISO 2859-1 plan. The tools that matter most commercially - booth visits and quotes - end in a human intake by design, so the server is a well-priced front door rather than an automated sourcing pipeline. The sourcing-quote class here already carries [CNC Compass](/hermes/mcp/servers/external/cnc-compass-mcp/) for part quoting and Next Everything for BOM pricing; what this entry adds is the trade-show and inspection halves that neither of them covers.
