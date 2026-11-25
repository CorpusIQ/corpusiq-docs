---
title: "Fontier MCP - Font Licences Answered With the Quote"
description: "2,168 open-licence families, each with a sourced yes, no or conditional for commercial, web, app and logo use, plus measured sizes and pairings."
category: "Design"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8055 filed 2026-11-25T10:19:50Z; registry record ai.fontier/fontier 1.0.0 with the remote https://fontier.ai/mcp against serverInfo fontier.ai 0.3.0; keyless initialize and a five-tool tools/list read 2026-11-25; check_font_license, get_font, search_fonts, pair_fonts and best_fonts_for_use driven the same day"
relevance: "★★★"
tags: [fonts, typography, licensing, brand, design, woff2, remote-mcp]
last_updated: "2026-11-25"
---

# Fontier MCP

**"Can I use this font on the website" is a licensing question wearing a design question's clothes, and the licence is a text file nobody opens.** Fontier answers it per use, commercial, web, app, platform, modify or logo, with a verdict, a verbatim quote from the licence, the source URL, the licence version and a SHA-256 of the text it read. The same record carries facts measured from the font file itself: cap height, glyph coverage, and the WOFF2 bytes a phone and a Windows browser each download.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://fontier.ai/mcp
Auth:        none, no key and no account
Registry:    ai.fontier/fontier 1.0.0
Pricing:     not stated on the server; open-licence families only
Tools:       5, read from a keyless tools/list
```

The library is every open-licence family on Google Fonts, Fontsource and Fontshare, **2,168** of them by the server's own count. The `instructions` string ends with the constraint that keeps the tool honest and should be repeated to whoever reads the output: *"Quote the licence source and say the answer is a reading of the licence text, not legal advice."*

## The five tools

| Tool | What it needs | What it answers |
| --- | --- | --- |
| `search_fonts` | optional `uses`, `category`, `sort`, `text_only` | families filtered by licence use, mood or measured size |
| `get_font` | `font` | the full record: foundry, weights, measurements, CSS, download bytes |
| `check_font_license` | `font`, `use` | yes, no, conditional or unknown, with the quote and the source |
| `pair_fonts` | `font` | the fonts real sites load alongside it, and the size ratio that aligns them |
| `best_fonts_for_use` | `use` | ranked picks for a resume, tattoo, logo, wedding or handwriting job |

## A yes, a conditional, and the quote that decides it

`check_font_license` on **Inter** for `commercial` returned **yes**, under **SIL Open Font License 1.1**, with the sentence that settles it: *"The OFL allows the licensed fonts to be used, studied, modified and redistributed freely as long as they are not sold by themselves."* The record carries three conditions rather than one line of reassurance: do not sell the font files on their own, keep the copyright notice and licence with any files you hand out, and a modified font stays under the OFL and drops any Reserved Font Name. The source is the OFL text in the Google Fonts repository, with `licenseSha256` **5b9321a4298cfeb6b34354164a1c3afc3db114569984c502b9b35d988fd58c57** and a check date of **2026-11-19**.

`check_font_license` on **Satoshi** for `logo` is the more interesting answer, because it is the one family here whose licence text names logos and trademarks directly. Three quotes come back, and the third is the catch an operator usually discovers late:

- *"You may use the Font Software to create logos, wordmarks, graphic elements, images, vector files, scalable drawings and other creative works."*
- *"Logos and wordmarks created using the Font Software may be registered as trademarks."*
- *"You may not provide the Font Software directly to external designers, agencies, contractors, printers or other service providers."*

So a wordmark set in Satoshi can be registered as a trademark, and the same licence forbids handing the font files to the outside agency that will redraw it. **An outside designer has to get their own copy from Fontshare.** That is the kind of clause a procurement review needs in writing, and the tool returns it as a labelled `catch` quote rather than a footnote.

### Why the logo answer changes by licence

`best_fonts_for_use` for `logo` ranks four families and explains each on the licence line that matters for a logo: **Satoshi** because its licence is *"the one here that says a logo made with it can be registered as a trademark"*, **Space Grotesk** for the tech look at a measured **72%** width-to-cap-height ratio *"open enough to read in a small icon"*, **Playfair Display** for luxury and, by measurement, the one real sites load most at **562** top home pages, and **Archivo Black** *"when the logo has to work tiny"*. All four are free for a logo, and the reason is quoted rather than asserted: the OFL FAQ names logos first.

## What the page actually downloads

`get_font` on **Inter** returns the facts that usually get guessed. Popularity rank **5**, live version **v20**, npm package **5.3.0**, last modified **2025-09-10**, nine weights from 100 to 900, italic and variable both true, foundry The Inter Project Authors, designer Rasmus Andersson. Then the bytes:

- Phone, Regular **23,664** and Regular+Bold **48,432**.
- Windows, Regular **23,664** and Regular+Bold **48,256**.

And the adoption number with its source: **5,344 of the top 100,000 websites** (Tranco list `JZW4Y`) load Inter on their home page. Pair that with the 23.6 KB Regular and you can price a font swap in bytes before you ship it, which is the question a Core Web Vitals budget actually asks.

`pair_fonts` answers "what goes with this" with counts instead of taste. For Inter, the closest partners among sites that load both are **Poppins at 331 sites**, **JetBrains Mono at 192** and **Fragment Mono at 133**, and it hands over the alignment rule: *"Set Fragment Mono at 104% of Inter's size and their lowercase letters line up."* A pairing recommendation with a size ratio is a recommendation you can implement in one line of CSS.

### Which fonts are lightest for a fast page?

`search_fonts` with `uses: ["web"]`, `sort: "size"` and `text_only: true` returns **20 of 350** matching families, and the ordering needs one caveat read correctly. The head of the list is **Cuprum** (Regular 9,284 bytes, Bold 14,344), **Khand** (7,664 and 15,280) and **Poppins** (7,900 and 15,748). The Regular column is not ascending, because `sort: "size"` orders on the **Bold** WOFF2 size, which does rise monotonically down the page from 14,344 to 18,212. If you are picking a single weight, sort by the column you are shipping; if you ship Regular and Bold, the given order is already the one to read.

## Limits measured this pass

- The server reports **fontier.ai 0.3.0** in `serverInfo` while the registry record is **1.0.0**. The two version lines disagree, and the registry number is the one to quote to a procurement team.
- Written answers on a page come from check dates of **2026-11-19**, while the byte measurements carry **2026-11-23**. Two clocks, both stated in the payload, which is preferable to one undated number.
- The licence verdicts are readings of licence text by a machine and the server says so in every record (`not_legal_advice: true`). For a trademark registration, the quote is the evidence and a lawyer is still the decider.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
- [tld.expert MCP](/hermes/mcp/servers/external/tld-expert-mcp/) for the naming half of a brand: domain availability, prices and name collisions.
