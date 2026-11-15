---
title: "Jobsite Math MCP - Eleven US Construction Calculators"
description: "A local MCP server with eleven US construction calculators that asks for the bag label instead of inventing a waste allowance."
category: "Construction / Estimating"
stars: "0 (npm package jobsite-math-mcp, MIT, local stdio; eleven tools, all eleven driven)"
added: 2026-11-15
source: "the mcp.so submission queue entry #7394 filed 2026-11-15T14:30:52Z, and a driven session on 2026-11-15 in which the package was installed from npm and eighteen tools/call requests were run against it over stdio"
relevance: ★★★
tags: [construction, estimating, contractors, calculators, trades, markup, local, stdio, keyless, mcp]
last_updated: "2026-11-15"
---

# Jobsite Math MCP

**A contractor who confuses markup with margin loses money on every job, and the mistake is invisible in the quote.** Cost a job at 1,000 and add 20 percent, and the selling price is 1,200 with a margin of 16.7 percent. Aim for a 20 percent margin on the same job and the price has to be 1,250. Both numbers look like "twenty percent" on the page. One of them leaves 50 dollars of profit behind, on every job, for as long as the habit lasts.

The second half of the problem is the arithmetic itself: bag yields, sheet counts, board rows, and the waste factor somebody remembers from a supply house. An assistant asked to size a slab will answer confidently with a number it invented, because the bag label is not in its context.

Jobsite Math is eleven calculators that answer those two problems instead of approximating them, and its design stance is the reason it is worth a page: where the answer depends on a product figure, it asks for the figure rather than assuming one.

```
Server type:   local stdio (npm package jobsite-math-mcp)
Install:       npx -y jobsite-math-mcp
Server:        jobsite-math, version 0.1.0
Protocol:      2025-06-18
Repository:    https://github.com/johnski9000/jobsite-math
Licence:       MIT
Auth:          none
Tools:         11 (roof_pitch, hip_roof, markup, hourly_rate, concrete,
               gravel, bricks, mortar, paint, drywall, deck_boards)
Listed on:     the mcp.so submission queue as #7394
```

## The evidence tier

Installed and driven, not documented. The package was installed from npm on this host, the binary was started over stdio, `initialize` answered as `jobsite-math` **0.1.0** on protocol **2025-06-18**, `tools/list` returned **eleven** schemas, and **eighteen** `tools/call` requests were run against it. Every figure below is the server's own output, and every arithmetic check beside it is mine, worked independently.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `roof_pitch` | `riseIn`, `runIn`, optional `planAreaSqFt` | Pitch as x-in-12, angle in degrees, percent grade, slope factor, sloped length, and sloped area with squares when a plan area is given. |
| `hip_roof` | `lengthFt`, `widthFt`, `risePer12`, optional `overhangIn` | Plan area, roof area, squares, ridge, plate-to-ridge and eave-to-ridge heights, common and hip rafter lengths for a simple rectangular hip at equal pitch. |
| `markup` | `costUsd`, `percent`, `mode` (markup or margin) | Selling price, profit, margin and markup, with the mode declared. |
| `hourly_rate` | `targetPayUsd`, `overheadUsd`, `workingWeeks`, `billableHoursPerWeek`, optional `reserveUsd`, `profitMarginPercent` | The revenue the business must bill and the hourly rate that produces it. |
| `concrete` | `shape` (slab, round, tube), dimensions in feet and inches, optional `allowancePercent`, `bagYieldCuFt` | Cubic feet, cubic yards, and a bag count when a bag yield is supplied. |
| `gravel` | `shape` (rectangle, circle), `depthIn`, optional `densityLbPerCuFt` | Cubic feet and yards, plus pounds and short tons when the supplier density is supplied. |
| `bricks` | wall length and height, `openingsSqFt`, brick face length and height, `jointIn` | Net wall area, bricks per square foot and the brick count for one wythe. |
| `mortar` | `bricks`, `bricksPerBag` | Bags, from the bag label rather than a default. |
| `paint` | `surface`, `coats`, `coverageSqFtPerGallon` | Net area, coat area, gallons, quarts and the whole gallons to buy. |
| `drywall` | `surface`, `sheetWidthFt`, `sheetLengthFt` | Net area, sheet area, base sheets and whole sheets. |
| `deck_boards` | `lengthFt`, `widthFt`, `boardWidthIn`, `gapIn`, `boardLengthFt` | Rows, pieces per row, boards and purchased linear feet. |

## What the calls returned

**The markup and margin pair, on a 1,000 dollar job.** `mode` is a required argument, so the caller has to say which percentage it means, and both answers came back with the other figure attached:

| Call | Price | Profit | Margin | Markup |
|---|---|---|---|---|
| `costUsd` 1,000, `percent` 20, `mode` markup | 1,200 | 200 | 16.667% | 20% |
| `costUsd` 1,000, `percent` 20, `mode` margin | 1,250 | 250 | 20% | 25% |

Both reproduced by hand: 1,000 x 1.2 = 1,200, and 200 / 1,200 = 16.667 percent. Then 1,000 / 0.8 = 1,250, and 250 / 1,000 = 25 percent. The 50 dollar gap is the whole argument for the tool.

**The hourly rate divides by the margin, it does not add it.** Asked for 80,000 of pay, 30,000 of overhead and a 10 percent profit margin over 46 weeks at 25 billable hours, it answered required revenue **135,555.56**, billable hours **1,150**, hourly rate **117.87**, profit **13,555.56**. The check: pay plus overhead is 110,000, and 110,000 / 0.9 = 122,222, plus the 12,000 reserve booked in that call gives 122,000 / 0.9 = 135,555.56, divided by 1,150 = 117.874. A tool that added 10 percent instead would have quoted about **105.22** an hour and buried the margin.

**A slab, then a column, then a tube, all three shapes.** Ten feet by ten feet at four inches returned **33.333** cubic feet and **1.2346** cubic yards (100 square feet x 4/12, divided by 27). A 24 inch column four feet high returned **12.566** cubic feet, which is pi/4 x 2 squared x 4. A 24 inch tube with an 18 inch core at the same height returned **5.498** cubic feet, the annulus, pi/4 x (4 - 2.25) x 4. Adding a 10 percent allowance and a 0.6 cubic foot bag yield moved the slab to **36.667** cubic feet and **62** bags, which is 36.667 / 0.6 rounded up from 61.1.

**Gravel, with the supplier's own density.** Ten by twenty feet at four inches returned **66.667** cubic feet and **2.469** cubic yards. Given a density of 105 pounds per cubic foot it returned **7,000** pounds and **3.5** short tons, which is 66.667 x 105 and that divided by 2,000.

**Brick, wall by wall.** A 20 by 8 foot wall with 20 square feet of openings, US modular brick at 7.625 by 2.25 inches and a 0.375 inch joint returned a net **140** square feet, **6.857** bricks per square foot and **960** bricks. The check is the joint: brick plus joint is 8.0 by 2.625 inches, 21 square inches, and 144 / 21 = 6.857. Mortar at 25 bricks per bag returned **39** bags from a base of 38.4, rounded up.

**Rooms, in paint and in board.** A 12 by 10 foot room with 8 foot walls and the ceiling included returned **472** square feet net, **944** coat square feet at two coats, **2.697** gallons and **3** whole gallons. The walls alone are 2 x (12 + 10) x 8 = 352, plus the 120 square foot ceiling is 472. The same room in drywall at 4 by 8 sheets returned **15** sheets from 14.75.

**Deck boards, and what board length does to the count.** A 16 by 12 foot deck with 5.5 inch boards and a 0.125 inch gap returned **26** rows from 144 / 5.625 = 25.6, one piece per row on 16 foot stock, and **26** boards. Asking for 12 foot stock instead returned **2** pieces per row, **52** boards and **624** purchased linear feet, because the second piece in every row is a cut.

**The hip roof, checked line by line.** A 40 by 24 foot building at 6-in-12 with a one foot overhang returned a plan area of **1,092** square feet (42 x 26), a roof area of **1,220.9**, **12.21** squares, a ridge of **16** feet, plate-to-ridge **6** feet, eave-to-ridge **6.5** feet, a common rafter of **14.534** feet and a hip rafter of **19.5** feet. Each one reproduces: the ridge of an equal-pitch hip is length minus width, the plate-to-ridge is a 12 foot run at half the pitch, the eave-to-ridge adds the overhang, the common rafter is 156 inches x 1.11803 = 174.4 inches, and the hip rafter is the diagonal run of 18.384 feet against a 6.5 foot rise, which is 19.499 feet.

## The stance that makes it usable

**It will not invent a waste factor.** Every volumetric and sheet tool carries an `allowancePercent` argument whose own description reads: "Extra percentage for waste or overage. Omit for none; this is not a recommended". A general assistant asked for concrete will add 10 percent because 10 percent sounds prudent, and that number is a guess wearing a hard hat. Here the default is zero, and the caller has to bring the number.

**It refuses an argument it does not know, by name.** A round column asked for `heightFt` came back `isError true` with `Unrecognized key: "heightFt"`, and the schema prints `heightIn` instead. The same happened to a gravel call using `bulkDensityLbPerCuFt` where the schema says `densityLbPerCuFt`. Both were my errors and both were answered with the key that was wrong rather than with a silently filtered result, which is how a caller finds out their units were skipped. The brick tool takes inches for the brick and feet for the wall in the same argument list, and that refusal is the only thing standing between the two.

**The pricing tools carry their own caveat.** The server's own instructions field opens with "Deterministic US-unit construction and pricing calculators. Use them instead of doing the arithmetic yourself", then asks for any missing dimension or product figure rather than guessing it, and closes by naming what it is not: "planning estimates, not structural design, code compliance, HVAC load calculations or tax advice."

## Limits

US units only. Rafters and hip lengths are for a simple rectangular hip at equal pitch, not a complex roof. Drywall does not select a rated assembly. Deck boards assume a straight rectangle with no offcut reuse. Brick is one wythe of a wall face. Nothing here replaces a stamped drawing, a permit review, or a local code check, and the server says so first.

## FAQ

### Does it need an API key or an account?

No. It runs locally over stdio from the npm package, with no credential and no network calls.

### Why not just ask the assistant for the estimate?

Because the assistant will supply the missing figures, and the missing figures are the estimate. Bag yield, paint coverage, supplier density and waste factor are the four numbers that decide whether the job makes money, and each one belongs on a bag or a data sheet rather than in a guess.

### What is the difference between markup and margin here?

Markup adds to cost; margin is measured against price. The tool requires you to choose, and returns both figures so the gap is visible in the answer.

### Is the allowance added by default?

No. It is omitted unless the caller passes `allowancePercent`, and the schema description states that the omission means none rather than a recommended value.

## Related reading

- [External MCP server catalog](/hermes/mcp/servers/external/) for the rest of the servers evaluted and catalogued here
- [CorpusIQ connectors](https://corpusiq.io/connectors) for the read-only business systems this catalog is built around
