---
title: "TouristPads MCP - Singapore Event Rental Quotes"
description: "Three tools that list Singapore event devices, price a rental to the dollar with timing surcharges, and issue a numbered quote"
category: "Business Operations"
stars: "n/a (hosted, keyless, no credential required)"
added: 2026-11-11
source: "the mcp.so submission #7130 for TouristPads, the official registry record com.touristpads/touristpads 1.0.0, and the endpoint itself at https://touristpads.com/mcp, where a keyless initialize answered 200 as touristpads 1.0.0, tools/list returned three tools, and list_rental_options plus price_rental were driven on a real six-device two-day order"
relevance: ★★★
tags: [event-rental, equipment-rental, singapore, quotes, pricing, surcharges, smb, events, keyless, streamable-http, remote-mcp]
last_updated: "2026-11-11"
---

# TouristPads MCP

**The rental industry quotes in two numbers and argues about the third.** The equipment total is easy to explain and easy to compare; the delivery window, the day of the week and the collection time are where the margin actually lives, and they are usually discovered when the invoice arrives. This server quotes both, itemises every surcharge, and then volunteers the cheaper date.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://touristpads.com/mcp
Auth:         none; keyless initialize, tools/list and tools/call all 200
Registry:     com.touristpads/touristpads 1.0.0
Tools:        list_rental_options (read), price_rental (read), request_quote (write)
Currency:     Singapore dollars, all dates Singapore time
Scope:        one city, one operator, delivered and collected by the vendor
```

Three tools is the whole surface, and the split is deliberate: two reads that price an estimate, one write that turns an estimate into a numbered quote and emails the PDF. The initialize instruction string spells out the workflow rather than leaving it to the model: call `list_rental_options` first, ask what the customer needs and for both delivery and collection windows, then call `price_rental` and show the total and the main lines, and if `price_rental` returns `cheaperTimingOptions` or `sparesOption`, tell the customer.

## The inventory is real, and it is finite

`list_rental_options` returned **16 rentable product ids** with a maximum quantity for each, which is the availability an event planner actually needs before promising a layout:

```text
ipad-102                      104        ipad-102-tablestand        55
iphone-xr                      35        ipad-102-floorstand        30
router (5G, 200Gb/month)       22        ipad-air11                 19
ipad-air11-tablestand          19        ipad-pro129                18
ipad-pro129-tablestand         18        iphone-15                  14
samsung-a33                    11        iphone-17                   3
```

plus four accessories with no stock ceiling (Lightning and USB-C cables, HDMI and VGA adapters) and three charged extras: steel cable locks per table stand, and pre-installed apps or files per iPad or per phone. Two rules sit next to the stock and change what the numbers mean: **floor stands fit only the iPad 10.2**, so an order for floor stands is an order for that specific tablet; and **the Wi-Fi-only iPad Air 11 comes with one free 5G router per unit instead of a SIM**, so the router count in a mixed order is not simply the router line.

## A priced order, with the fees separated

A six-device, two-router order for a three-day event was priced in one call:

```text
6 x iPad 10.2 (2021) + Floor Stand, 3 days @ 81.44     1,465.92
2 x Prolink DL-7211 5G router, 3 days @ 20.80            124.80
2 x 200Gb per router per calendar month @ 30.00           60.00
                                            equipment  1,650.72
delivery                                                 106.80
after hours                                              150.00
Sunday or public holiday                                 500.00
rounding down                                             -0.52
                                            timing       756.80
                                            TOTAL      2,407.00 SGD
```

The equipment is **68.6 percent** of the bill. The other **31.4 percent** is the calendar: a collection at 18:00 on **Sunday 22 November** carries both an after-hours charge (150, being two 30-minute blocks at 75) and the **500 SGD Sunday leg fee**. Nothing was hidden and nothing was added at the end; the fees are four named lines above the total.

Then the server did the thing that makes this entry worth a guide. It returned a `cheaperTimingOptions` array whose first entry moved the collection to **Monday 23 November at 10:30** and re-priced the identical order at **1,907.00 SGD**, exactly **500 SGD** less, with the after-hours charge still standing. The assistant is instructed to tell the customer that option exists. A quote tool that computes a cheaper alternative and surfaces it without being asked is arguing against its own invoice, and that is the behaviour an operator can build a process on.

### Who has to agree to the extra charges?

The response carries `afterHoursChargeNeedsAgreement: true`, and the published rules say the customer **must agree to any after-hours charge before a quote is issued**. The distinction matters because an estimate and a quote are different instruments here: the price response ends with

```text
"note": "An estimate only: no quote has been issued. A credit note held against the
 customer's email, if any, comes off when the quote is issued."
```

so an assistant that reports a price as a booking has misrepresented the state. `request_quote` is the only tool that issues the numbered quote and emails it with its PDF, and it is the only tool annotated as a write.

## The rules that decide the invoice

The published rule list is short and specific, and every line is a lever an operator can pull before signing:

- **Minimum order 280 SGD of equipment** before delivery. A smaller order is topped up to it, or the vendor offers extra spare units at the same total.
- **Delivery and collection run 6am to 11pm.** Outside **9am to 6pm** each leg costs **75 SGD per 30 minutes**. A **Sunday or public-holiday leg costs 500 SGD** and covers 9am to 9pm. **Saturday collections are free until 9pm.**
- **Rush.** Next-working-day or sooner carries a rush fee. **30 or more devices need five working days notice** to avoid it, which is the constraint that should drive a large-event booking date.
- **Volume.** **8 percent off at 2,000 SGD** of equipment and **10 percent at 3,000 SGD**, applied automatically. The order above stopped at 1,650.72 and therefore earned none of it, which is the other finding in this quote: adding roughly **350 SGD** of equipment would have crossed the 2,000 threshold.
- **Location surcharges are added at signing, not in the quote**: Sentosa, Tuas and Jurong Island 25 SGD per trip, Changi Exhibition Centre 60. A quote for an event at any of those venues is low by construction, and the tool says so in its own rules rather than after the fact.
- **Someone from the customer's team must be at the venue** to receive and sign for the devices.

## Verified surface

```text
initialize          200, touristpads 1.0.0, protocol 2025-06-18, no session id issued
tools/list          200, three tools; list_rental_options and price_rental readOnlyHint true,
                    request_quote false
list_rental_options 200, 16 products with max quantities, three extras, ten rules
price_rental        200, three equipment lines and four fee lines, total 2,407.00 SGD,
                    one cheaperTimingOptions entry at 1,907.00, agreement flag set
```

Not tested this pass: `request_quote`, because it issues a real numbered quote and emails a PDF to a real address. The write path is therefore described from its schema and its annotation, not from a message this pass sent.

## Good for

An event organiser or agency in Singapore that rents tablets, phones, routers or stands and needs the **all-in** number for a specific date window, including the day-of-week cost, before it commits to a layout and a schedule. An ops team comparing two event dates, which is exactly the question the cheaper-timing output answers. A venue or exhibitor budgeting device hire across several days where the collection time decides the fee.

Not for: any city other than Singapore; buying equipment, since the vendor only rents; or a team that needs availability calendars rather than quantity ceilings, because the max quantity is a stock limit and not a hold.

## Related in this catalog

- [WeGravel MCP](/hermes/mcp/servers/external/wegravel-mcp/) - the same shape of answer in materials: a delivered quantity and a price that states its own safety margin and its truck-load break.
- [PackIndex MCP](/hermes/mcp/servers/external/packindex-mcp/) - RFQ pricing where the order quantity decides the unit cost.
- [NuaSense MCP](/hermes/mcp/servers/external/nuasense-mcp/) - a market data surface that prices a delivery against a caller-supplied transport cost, the same net-of-logistics logic this quote applies to a Sunday leg.
