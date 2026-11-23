---
title: "LabelQueue MCP - Label Sheet Geometry Before the Print"
description: "Avery and thermal label geometry, pitch and margins with print-drift diagnosis; six codes only, and an unknown code silently returns 5160."
category: "Business Operations"
stars: n/a (keyless, vendor-hosted)
added: 2026-11-22
source: "mcpservers.org sitemap arrival at /servers/labelqueue-mcp on 2026-11-22; keyless initialize, tools/list and seven tools/call probes on 2026-11-22"
relevance: ★★★
tags: [labels, printing, shipping, barcode, avery, thermal, keyless, fulfilment]
last_updated: "2026-11-22"
---

# LabelQueue MCP

**Remote MCP server (Streamable HTTP, no authentication) that answers the geometry question behind every misaligned label: exactly how wide, how tall, what margin and what pitch a sheet expects, and what to change when the rows creep.** Four deterministic tools, no account, no key.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://labelqueue.com/api/mcp
Server:      com.labelqueue/mcp 1.0.1 reported, protocol 2025-06-18
Registry:    com.labelqueue/mcp 1.0.2, published 2026-11-10T06:16:24Z
Tools:       4
Repo:        https://github.com/AbigailDavised/labelqueue-mcp
```

## Why This Matters for Operators

A package that shifts half a centimetre down the sheet wastes the sheet, and the cause is almost never the printer. It is a viewer scaling a 279.4 mm page to a printable area, a template using the wrong margin, or an Avery code copied from a listing with a different regional layout. This server answers with the numbers rather than an explanation, and one of its four tools names the drift cause directly.

## Measured Behaviour

Seven calls were driven on 2026-11-22, all keyless. Every figure is quoted from the response, and the two sheets were reproduced by hand.

| Call | Arguments | Answer |
|---|---|---|
| `lookup_avery_label_specs` | `5160` | US Letter, 2.625 x 1 in, 3 x 10 = **30** per sheet |
| `lookup_avery_label_specs` | `L7160` | ISO A4, 63.5 x 38.1 mm, 3 x 7 = **21** per sheet |
| `check_barcode_symbology_requirements` | `code128` | full ASCII 128, modulo-103 check, quiet zone **10X / 2.54 mm** |
| `diagnose_browser_label_print_drift` | `0.35` mm, `chrome` | names Fit-to-Printable-Area as the cause, three fix steps |
| `lookup_thermal_roll_label_specs` | `4x6` | **101.6 x 152.4 mm**, **812 x 1218** px at 203 dpi, **1200 x 1800** at 300 dpi |
| `lookup_avery_label_specs` | `9999` | **no error** - `defaultSpec` Avery 5160 plus the six-code list |
| `check_barcode_symbology_requirements` | `qrcode-xyz` | **no error** - Code 128 requirements, with the request echoed back |

### The sheet arithmetic checks out

Avery 5160 returns `hPitchIn: 2.75`, `leftMarginIn: 0.1875` and `topMarginIn: 0.5`. Reproduced by hand on US Letter: three columns at a 2.75 in pitch is 8.25 in of travel from a 0.1875 in margin, which lands at 8.4375 in and leaves 0.0625 in on the right; ten rows at a 1 in pitch from a 0.5 in top margin take 10.5 in of an 11 in page. Avery L7160 on A4: three columns at 66 mm from a 7.2 mm margin is 205.2 mm of a 210 mm sheet, and seven rows at 38.1 mm from a 15.1 mm top is 281.8 mm of 297 mm. Both match the sheets the vendors publish.

The thermal numbers are pure arithmetic from the roll size: 4 in at 203 dpi is **812** dots and 6 in is **1218**; at 300 dpi the same roll is **1200** by **1800**. An agent sizing a raster for a Zebra, Rollo or Munbyn printer gets the pixel count directly instead of guessing.

### The drift tool is the one an operator keeps

Asked with a 0.35 mm observed drift in Chrome, it answers with the mechanism rather than a checklist:

> Fit-to-Printable-Area shrinks a 279.4mm US Letter page by ~4% (~11mm total), causing row 1 to look close while row 10 creeps upward by 8-11mm.

The three fix steps that follow are the literal settings: scale at 100% / actual size, margins none with the `@page` block in the PDF, and paper size matched to Letter versus A4.

## Defects Recorded

- **An unknown code is silently substituted.** `9999` and `22806` both return the Avery 5160 spec under a `defaultSpec` key with `availableCodes: ["5160","5163","5164","5167","22807","L7160"]`. Nothing in the payload is an error, so an agent that reads `defaultSpec` without checking `requestedCode` against `availableCodes` will size a label it was never asked about. `22806` is the real Avery code for a 1 x 2.625 in sheet and is **not** covered.
- **An unknown symbology is echoed back with the wrong data.** `qrcode-xyz` returned the Code 128 charset, modulo-103 check digit and 10X quiet zone, with `symbology: "qrcode-xyz"` in the same object. That is a silent substitution of the answer, not just of a default.
- **Coverage is six codes.** Four US Letter sheets, one A4 sheet and one 2.625 in sheet. Anything outside that list is not really served.
- **Version drift between the endpoint and the registry.** `initialize` reports **1.0.1**; the registry record published on 2026-11-10 is **1.0.2**.

## Setup

```bash
claude mcp add --transport http labelqueue https://labelqueue.com/api/mcp
```

No key, no sign-in, no session id issued at initialize.

## What It Cannot Do

- **No custom sheet geometry.** It looks up a fixed table; it does not take dimensions and compute a template.
- **No PDF, no template, no print call.** Every response is data with a link back to the vendor's generator.
- **No regional coverage beyond one A4 code.** A European operator with a different Avery code is served the US default unless their code is `L7160`.

## See Also

- [ZplFlow MCP - Thermal Label Streams for Agents](/hermes/mcp/servers/external/zplflow-mcp/) - the label stream this geometry feeds
- [Print and Mail Company MCP - Physical Mail From an Agent](/hermes/mcp/servers/external/print-and-mail-company-mcp/) - the mailing step after the label
