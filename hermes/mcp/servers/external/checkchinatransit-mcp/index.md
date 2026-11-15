---
title: "CheckChinaTransit MCP - Visa-Free Transit Rules"
description: "A keyless MCP server for China's 240-hour visa-free transit rules, with eligibility, the routing test and the deadline arithmetic as tools."
category: "Travel / Compliance"
stars: "0 (thin front end over a documentation site; eight tools, keyless, seven substantive)"
added: 2026-11-14
source: "the mcp.so submission queue entry #7366 filed 2026-11-15T00:53Z, and a driven session against https://checkchinatransit.com/api/mcp on 2026-11-14 in which initialize answered 200 as com.checkchinatransit/mcp 1.0.0 and all eight tools were called"
relevance: ★★
tags: [travel, china, visa, transit, compliance, business-travel, keyless, remote-mcp]
last_updated: "2026-11-14"
---

# CheckChinaTransit MCP

**China's visa-free transit is a routing rule, not a permission, and the routing rule is the part travelers get wrong.** A 240 hour stay without a visa is available to a passport from one of the listed countries, and only if the traveler arrives from one country and leaves for a different one. Fly Singapore to Shanghai to Singapore and the same traveler who qualified on Tuesday is refused at the desk, because the itinerary was a round trip rather than a transit. The deadline has its own trap: the clock does not start at landing, it starts at midnight.

This server turns those rules into seven working tools and a stub. It is keyless, stateless and takes no account, so an assistant can answer the three questions a traveler actually asks (does my passport qualify, is my routing valid, when exactly must I leave) without a human reading a policy page between each one.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0, stateless, keyless
Endpoint:      https://checkchinatransit.com/api/mcp
Server:        com.checkchinatransit/mcp, version 1.0.0
Registry:      com.checkchinatransit/mcp (the server name echoes it)
Auth:          none
Tools:         8 (twov_nationality_eligibility, third_country_itinerary_rule,
               transit_stay_deadline, transit_port_zone, 24hour_direct_transit_rules,
               airline_checkin_boarding_checklist, visa_photo_specs,
               twov_vs_unilateral_30day_visa_free)
Listed on:     the mcp.so submission queue as #7366
Website:       https://checkchinatransit.com/
```

## The evidence tier

Driven. Eight tools, eight `tools/call` requests and six extra calls across the eligibility, routing and deadline tools, all answering 200 on 2026-11-14 with no credential. Everything below is quoted from a live response or reproduced from one by hand; no policy figure here is taken from a marketing page.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `check_china_twov_nationality_eligibility` | `nationality` | Two booleans and a sentence: whether the passport qualifies for the 240 hour transit rule, whether it qualifies for the 24 hour rule, and what to do if it does not. |
| `validate_third_country_itinerary_rule` | `inboundFrom`, `outboundTo` | Whether A to China to C is a valid third region routing, with the note that immigration checks only the immediate inbound origin and immediate outbound destination. |
| `calculate_transit_stay_deadline` | `arrivalDateIso`, `policyHours` (240, 144 or 24) | When the clock starts and the exact local date and time by which the traveler must depart. |
| `lookup_china_transit_port_zone` | `cityOrAirportCode` | Documented as returning permitted stay regions and approved entry and exit ports. See the defect below. |
| `check_24hour_direct_transit_rules` | `totalLayoverHours`, `hasDomesticTransfer` | Whether a layover fits the 24 hour rule, and the line to use at the border desk. |
| `get_airline_checkin_boarding_checklist` | `stayingInHotel` | The document list an airline desk will ask for, plus the TIMATIC phrase to give the agent. |
| `lookup_china_visa_photo_specs` | `usageType` | Physical and digital photo dimensions for a Chinese visa application. |
| `compare_twov_vs_unilateral_30day_visa_free` | `nationality` | Which of the two visa-free paths applies to that nationality and what each one allows. |

## What the calls returned

**Eligibility, two passports.** A United States passport returned `twov240HourEligible: true` and `direct24HourEligible: true`, with the sentence *ELIGIBLE: Passport qualifies for China 240-hour (10-day, upgraded from 144h) Visa-Free Transit with confirmed onward ticket to a third country/region (HK/Macau/Taiwan count as third regions)*. An Indian passport returned `twov240HourEligible: false` beside `direct24HourEligible: true` and *Not on the 54-country 240h TWOV list; check 24-hour direct transit or apply for an L/G visa prior to travel*. The asymmetry is the useful part: the refusal names the alternative instead of ending the conversation.

**Routing, both directions of the same test.** Singapore to China to Japan returned `validThirdRegionRouting: true` with the note that immigration checks only the immediate inbound flight origin and the immediate outbound destination. Singapore to China to Singapore returned **false** and *INVALID FOR TWOV: Origin A and Destination C cannot be the same country/region (round-trip A -> China -> A is strictly disqualified under TWOV)*. A traveler holding a confirmed round trip home from Shanghai is relying on a rule that does not exist, and this is the call that says so.

**The deadline, three tiers, one arrival date.** Arriving 2026-11-15:

| Policy | Clock starts | Must depart before |
|---|---|---|
| 240 hours | 2026-11-16 00:00 Beijing | 2026-11-25 23:59 Beijing |
| 144 hours | 2026-11-16 00:00 Beijing | 2026-11-21 23:59 Beijing |
| 24 hours | 2026-11-16 00:00 Beijing | 2026-11-16 23:59 Beijing |

**The 24 hour rule, both sides of its edge.** An 18 hour layover with a domestic transfer returned `eligibleUnder24hRule: true` and the instruction to apply for a 24 hour temporary entry permit at the border desk if changing terminals or collecting baggage. A 30 hour layover returned `false` and *Exceeds 24 hours; must qualify for 240-hour TWOV (54 countries) or hold a valid Chinese visa.* The boundary sits where an operator would expect and the message names the two paths forward.

**The document list.** The checklist tool returned four mandatory documents: a passport valid three months from arrival with two blank pages, a printed onward ticket with a confirmed seat and e-ticket number to a third country, a hotel booking (or a police accommodation registration plan within 24 hours at a private address), and an arrival card. It also returned the phrase to give the airline agent: *Ask the agent to look up TIMATIC under "TWOV (Transit Without Visa) - 240-hour Visa-Free Transit", NOT standard tourist visa*. That line is the single most practically useful string in the server, because the failure it prevents happens at check-in rather than at immigration.

**Photo specifications.** 33 mm by 48 mm physical, head 15 to 22 mm wide and 28 to 33 mm chin to crown, digital between 354 by 472 and 420 by 560 pixels, JPEG 40 KB to 120 KB, pure white background, no glasses or jewelry.

## The arithmetic control

The deadline tool is the one place a wrong answer gets someone detained, so the three tiers were reproduced by hand against the rule as stated in the response itself.

The clock starts at 00:00 on the day after arrival, and the policy is expressed in hours. For a 240 hour window starting 2026-11-16 00:00, ten days is 2026-11-26 00:00, and a departure that must happen before that instant is *2026-11-25 23:59*: the returned value. For 144 hours, six days from the same start is 2026-11-22 00:00, so the departure deadline is the previous minute, *2026-11-21 23:59*: the returned value. For 24 hours, one day is 2026-11-17 00:00, so the deadline is *2026-11-16 23:59*: the returned value. All three cells match, and the bonus day the server points out is real: hours spent on the arrival day before midnight sit outside the window, which is why a late evening arrival buys almost a full extra day.

## The defect this pass is recording

**`lookup_china_transit_port_zone` is a stub.** Its description promises *permitted stay regions and approved entry/exit airports, seaports, and rail ports*. Called with `PVG`, with `PEK`, and with the deliberately invalid `ZZZZ`, it returned **the same three fields every time**: the query echoed back, a general sentence that *60 approved ports across 24 provinces allow cross-provincial travel within the designated permitted zones*, and a link to the ports directory. No zone, no port list, no indication that `ZZZZ` is not a port. A tool that answers the same text for a valid airport and for nonsense is a link, and an assistant that reports "PVG permits the Yangtze River Delta zone" from this call would be inventing it.

Two smaller marks belong beside it. The server's `instructions` field is not a description at all: it is the 36 character string `mcprush.com-eec7a370865b13a747c4179c`, a builder token with no product text, which is the first thing an MCP client reads and it says nothing about the product. And the policy counts are the vendor's own: **54 countries** for the 240 hour list and **60 ports across 24 provinces**. This catalog has not independently verified either count against an immigration authority, and published counts for both have moved as the policy expanded, so a figure that decides someone's trip should be confirmed at the airline desk or an embassy page on the day rather than taken from a tool response.

## Frequently asked

### Does the traveler need a visa for a 240 hour transit?

Only if the passport is not on the 54 country list. The eligibility tool answers that in one call and returns two booleans, one for the 240 hour rule and one for the 24 hour rule, with a sentence saying what to do when neither applies.

### What happens if the itinerary is a round trip?

It is refused, and the server says so plainly: origin and destination cannot be the same country or region. A traveler flying home from China to the country they arrived from does not qualify for transit without a visa, whatever the length of the stay.

### Which countries count as a third region?

Hong Kong, Macau and Taiwan count as distinct regions from mainland China, which is stated in both the eligibility and the routing responses. That is what makes a Shanghai trip routed through Hong Kong a valid transit and a Shanghai trip routed back to Singapore not.

### Can I use it to plan a multi-city trip inside China?

Partly. The 240 hour policy allows cross-provincial travel within designated permitted zones, and the server states that 60 ports across 24 provinces participate, but the tool that is supposed to name the zone for a given airport does not return one. Plan the port and zone detail from the ports directory the tool links to, not from the tool.

### Is it free and does it need an account?

Yes to free, no to an account. `initialize` and every call in this pass returned 200 over plain HTTPS with no credential and no session header.

## What to check before you rely on it

1. Run the eligibility call for the exact passport, then the routing call for the exact itinerary. The two questions have different answers and both must pass.
2. Use the deadline tool rather than counting days, and remember the clock starts at midnight after arrival rather than at landing.
3. Give the airline desk the TIMATIC phrase from the checklist response. The refusal that ruins a trip usually happens at check-in.
4. Do not quote a port zone from `lookup_china_transit_port_zone`. It returned the same payload for PVG, PEK and ZZZZ.
5. Confirm the country and port counts against an official page on the day of travel. The server's figures are its own and this catalog has not verified them.
