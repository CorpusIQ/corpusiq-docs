---
title: "PaintColorMatcher MCP - Paint Color Matching"
description: "A keyless MCP server that matches any HEX to 11,249 Sherwin-Williams, Benjamin Moore and Behr paints with CIEDE2000, LRV and trim."
category: "Retail / Design"
stars: "0 (hosted, closed source; eight tools, keyless, all eight driven)"
added: 2026-11-14
source: "the mcp.so submission queue entry #7367 filed 2026-11-15T00:53Z, and a driven session against https://paintcolormatcher.com/api/mcp on 2026-11-14 in which initialize answered 200 as com.paintcolormatcher/mcp and all eight tools were called"
relevance: ★★
tags: [paint, color-matching, retail, interior-design, ciede2000, lrv, keyless, remote-mcp]
last_updated: "2026-11-14"
---

# PaintColorMatcher MCP

**A customer holds up a phone with a photo of a wall and says "this one", and the color on that screen is not the color on the wall.** Screen photos shift with white balance, paint chips shift under a shop's fluorescent tubes, and the same swatch looks different in a north facing room than a south facing one. Getting from a photograph to a purchasable can of paint is a colorimetry problem, and the industry answer has a standard: CIEDE2000 distance in a perceptual color space.

This server is a color engine rather than a product browser. It carries **11,249 official colors** across Sherwin-Williams, Benjamin Moore and Behr, matches any HEX to the closest of them by CIEDE2000, and exposes the intermediate arithmetic (Lab coordinates, LRV, undertone family) in the response, which is what makes it checkable rather than merely confident. For an operator running a design studio, a paint retailer or a home services business, the useful tools are the ones that answer a quantity question: how many gallons, which sheen, what trim.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0, stateless, public, keyless
Endpoint:      https://paintcolormatcher.com/api/mcp
Server:        com.paintcolormatcher/mcp,
               title "PaintColorMatcher Scientific CIEDE2000 Engine"
Website:       https://paintcolormatcher.com
Source:        https://github.com/AbigailDavised/paintcolormatcher-mcp
Registry:      com.paintcolormatcher/mcp
Auth:          none
Tools:         8, all driven
Listed on:     mcp.so queue #7367
```

## The evidence tier

Driven. `initialize` answers **200** with no credential, `tools/list` returns eight schemas, and every one of the eight was called on 2026-11-14. The color arithmetic was then reproduced independently in Python from the hex codes rather than accepted from the response, which is the control that matters for a server whose entire claim is a formula.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `match_hex_to_paint_colors` | `hex`, `brand`, `limit` (1 to 15) | The input color's LRV and Lab coordinates, then the closest official colors across brands with code, name, hex, LRV, undertone family and CIEDE2000 delta. |
| `find_cross_brand_paint_equivalent` | `query` (name or manufacturer code), `target_brand` | The source paint's record, then its closest equivalents in the other brands, ranked by delta. |
| `calculate_ciede2000_swatch_distance` | `hexA`, `hexB` | Lab for both colors, the CIEDE2000 distance, the LRV difference, and a verdict band such as imperceptible or visible. |
| `analyze_paint_lrv_and_room_exposure` | `lrv`, `roomExposure` | The LRV category band and how that room's light will treat the color. |
| `calculate_room_paint_gallons_estimator` | `wallPerimeterFeet`, `ceilingHeightFeet`, `coats`, `doorsCount`, `windowsCount` | Net paintable area, coat area, exact gallons at a stated coverage rate, and a recommended purchase with a touch up buffer. |
| `recommend_paint_sheen_finish` | `surfaceOrRoom` | A sheen recommendation with a reason. |
| `simulate_kelvin_lighting_undertone_shift` | `undertone`, `kelvin` | How a bulb temperature treats that undertone family. |
| `generate_coordinating_trim_and_accent_palette` | `wallHex` | Wall color record, detected temperature, and named trim and ceiling whites across the three brands. |

## What the calls returned

**A photograph's color, matched three ways.** `#EAE6DF`, a warm off-white, returned its own LRV as **79.4** and Lab as **91.42, 0.13, 3.88**, then three matches: Benjamin Moore **2108-70 Lacey Pearl** at `#e8e5df` with delta **0.62**, Behr **MQ3-32 Cameo White** at `#ebe8e2` with delta **0.70**, and Behr **BWC-06 Solid Opal** at `#eeeae2` with delta **0.97**. All three sit under a delta of 1.0, which the distance tool calls *imperceptible to the human eye*, and all three are labelled with the same undertone family, Warm Yellow-Cream. That is the answer a paint desk needs: not one match, but three purchasable alternatives within a tolerance nobody can see.

**An official color across brands.** Queried with `Agreeable Gray`, the server recognised it as Sherwin-Williams **SW 7029**, hex `#d1cbc1`, LRV **60.23**, and returned Behr **HDC-NT-20 Cotton Grey** at delta **0.60** and Behr **DC-007 Tranquil Gray** at delta **0.80** as its cross brand equivalents, then Benjamin Moore **859 Collingwood**. A customer who wants the look in a brand the shop stocks gets three codes rather than a shrug.

**The gallon count, with the arithmetic visible.** A room with a 52 foot perimeter and 9 foot ceilings, two coats, two doors and two windows came back as **396 square feet** net, **792 square feet** across two coats, **2.11 gallons** exact at a stated **375 square feet per gallon** coverage, and a recommended purchase of **3 gallons** with a 10% touch up buffer. Every one of those numbers is reproducible from the inputs: 52 times 9 is 468 gross, minus two doors at 21 square feet and two windows at 15 gives 396, times two coats is 792, divided by 375 is 2.112, and 10% on top rounds up to 3.

**Trim and ceiling from a wall color.** `#D1CBC1` returned a detected temperature of *Warm / Greige-Cream Undertone (b* >= 4)*, with Sherwin-Williams **SW 7005 Pure White (LRV 84)**, Benjamin Moore **OC-17 White Dove (LRV 83.2)** and a Behr pair as trim, plus the instruction to use an untinted flat ceiling white or the wall color at 25% strength.

**Lighting and exposure.** LRV 60 classified as *Light Neutral / Balanced Mid-Light (LRV 55-74)*, with a north facing note that cool indirect light mutes warm colors and pulls out cool, green and violet undertones. A 3000K bulb was described as the residential soft white standard that flatters greige and warm whites.

## The arithmetic control, and it passes

The claim under test is CIEDE2000, so the distance was computed independently in Python: sRGB to CIE Lab through D65, then the full CIEDE2000 formula with the G compensation term, the hue averaging rules, the weighting functions S_L, S_C, S_H and the rotation term R_T.

| Pair | Server Lab | My Lab | Server delta | My delta |
|---|---|---|---|---|
| `#D1CBC1` against `#CFC9BF` | 81.9 / 0.33 / 5.72 and 81.18 / 0.33 / 5.73 | 81.90 / 0.34 / 5.71 and 81.18 / 0.34 / 5.72 | **0.49** | **0.491** |
| `#EAE6DF` against `#e8e5df` | 91.42 / 0.13 / 3.88 | 91.42 / 0.14 / 3.87 | **0.62** | **0.627** |

Lab agrees to within 0.01 and the distance agrees to within 0.007, which is rounding on both sides. **This engine is computing the standard correctly**, and that is worth stating plainly because most color tools in this space compare RGB channels, which is the wrong metric for a question about what a human will see.

## The limits worth knowing

- **Color matching is exact; everything after it is a rule of thumb.** The delta is a formula. The sheen, exposure and lighting tools return prose guidance with no numeric input beyond the one you supply.
- **The sheen recommendation answers a different question than the room asks.** `kitchen` returned *Matte or Eggshell (5-15% gloss)* with a reason about velvety depth and minimal roller stipple. A working kitchen argues for a scrubbable finish, and the response carries no washability or durability field to weigh against appearance. Treat the sheen tool as a starting point for a conversation, not a specification.
- **The gallon figure assumes 375 square feet per gallon, one porosity, one paint line and one application style.** Rough surfaces, a deep base color over a light wall, or a sprayer all move that number, and none of those inputs exist in the schema.
- **The lighting tool returns a description rather than a measurement.** No shifted Lab value comes back for the 3000K case, so the effect cannot be compared across bulb temperatures numerically.
- **No as-of date on the catalogue.** The count is stated as 11,249 official colors in the server's own instruction block; when a manufacturer retires a color, the delta arithmetic stays right and the purchasable code may not.
- **Brand filter values were not enumerated.** `brand` accepts a brand name or `all`; the response ignores an unknown value rather than erroring, so a typo silently searches everything.

## Frequently asked

### How accurate is the paint match?

It returns CIEDE2000 deltas, and 1.0 is the usual threshold for imperceptible. In this pass a warm off-white found three matches between 0.62 and 0.97, all purchasable codes, and an independent Python implementation of the same formula reproduced both sampled distances to within 0.007.

### What is LRV and why does the server return it on every line?

Light Reflectance Value, 0 to 100, the share of visible light a color reflects. It is the number that predicts how a color will behave in a room, so it travels with every match. An LRV of 79.4 for an off-white and 60.23 for a greige is the difference between a room that lifts and one that settles.

### Can it tell me how much paint to buy?

Yes, with a stated coverage rate. A 52 by 9 room, two coats, two doors and two windows returns 396 net square feet, 2.11 gallons exact and 3 gallons recommended with a touch up buffer, all of which reconcile by hand at 375 square feet per gallon.

### Does it work with a photo?

Indirectly. The match tool takes a hex code, so the chain is photo to hex by some other means, then hex to paint here. The vendor links a separate photo calibration tool on its own site for the first step, which is outside this MCP surface.

### Is it free, and does it need a key?

Yes and no. `initialize`, `tools/list` and all eight tool calls returned 200 over plain HTTPS with no credential, and the submission describes the server as public and stateless.

## What to check before you put a color in a spec

1. Ask for at least three matches and read the deltas. Anything under 1.0 is a defensible substitute, and the brand you can actually buy decides between them.
2. Confirm the code with the manufacturer before ordering. The engine matches color, not stock.
3. Take the sheen recommendation as an opening position, not a specification, especially for wet rooms and kitchens.
4. Recompute the gallon figure if the surface is rough or the paint line differs, and add a room's worth for a two-coat deep base change.
5. Record the date. The catalogue count is the vendor's and manufacturer lines retire colors without notice.
