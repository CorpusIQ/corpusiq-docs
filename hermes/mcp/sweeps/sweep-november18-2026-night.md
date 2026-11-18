---
title: "MCP Server Discovery - November 18, 2026 (Night)"
description: "A six-hour window with both directory surfaces flat, one feed card and three servers catalogued from the submission queue."
category: "MCP Ecosystem"
last_updated: "2026-11-18"
---

# MCP Server Discovery - November 18, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed. The canonical did not move, the feed carried **one** server card, the queue carried **24** arrivals, and **three** servers ship: two from one author's Argentine suite, driven with a keyless trial key, and one keyless fraud-statistics server driven without any credential at all.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,338   identical map for map to the 66,338 read at 04:07Z
  per-map                     7,588 / 5,949 / 6,518 / 6,744 / 6,954 / 6,756
                              9,351 / 6,590 / 4,024 / 2,608 / 2,637 / 619
                              summing to 66,338 exactly
priority-servers.xml          299 entries, 34 distinct keys not already in the twelve maps
remote-mcp-servers.xml         15 raw entries, no new server route
distinct keys, twelve maps    22,440  against 22,440 at the evening capture
                              = 0 additions and 0 removals
lastmod >= 2026-11-18T04:07Z  ZERO rows (newest anywhere: 2026-11-18T01:37:43Z)
mcp.so /feed                  200, 156,858 bytes, 36 server anchors, 1 client anchor,
                              30 stamps, 29 distinct server slugs,
                              1 card above the cutoff (lake-meter, 06:51Z)
queue                         #7554 to #7577, 24 arrivals, no gaps
```

The flat reading is arithmetic rather than a count. The twelve numbered maps returned the same raw total and the same per-map block as the evening capture, the distinct locale-stripped key set was **22,440** on both reads, and a `lastmod` scan at or after the evening cutoff returned nothing at all, with the newest stamp anywhere in the twelve maps reading **01:37:43Z**, which predates the cutoff. Three of those numbers would be enough; all three agree.

One cross-reference trap is worth recording because it produced a phantom removal count on the first pass. The retained capture on disk held **22,474** keys, not 22,440, because it was a union that also carried the **34** keys that live only in `priority-servers.xml`. Differencing this pass's twelve-map set against that union returns exactly **34** "removals", and every one of the thirty-four is present in the priority map on this same read. The difference between 22,474 and 22,440 is the tell: a removal count that equals the known size of a map you did not fetch is a scope error, not a delisting.

## The feed

`mcp.so/feed` answered **200** at **156,858** bytes with **36** server anchors and **30** stamps, of which **29** distinct server slugs were parsed. Exactly one server card sits above the cutoff:

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 06:51 | `lake-meter` | held, agent cost infrastructure |

**The count that does not balance is the finding.** Thirty stamps against thirty-six anchors normally means seven featured rails plus cards, which is the pattern recorded across every pass since October. This read has **one** extra stamp attached to an anchor under `/clients/`, not `/servers/`: a company card for `rapidoddsapi.com` stamped **04:22Z**, carrying a sponsor blurb, an avatar and a `Submitted 6 hours ago` label. A stamp-to-slug pairing that walks the document and attaches each stamp to the nearest preceding `/servers/` anchor therefore loses one card, and a pairing that trusts the stamp count alone reports one more card than the feed actually carries. Read both anchor families and subtract the client rail.

`lake-meter` is a per-step model picker and a hard per-run cost cap for Claude Code, distributed as `npx lake-meter@latest mcp`, local only with no telemetry. Its own mcp.so page shows no tool list. It is agent cost infrastructure rather than a business data surface, and the nine stars-worthy entries in this catalogue that cover agent routing already carry that class, so it is held with the class named rather than catalogued from a card.

## The queue

Twenty-four arrivals, **#7554** to **#7577**, read with bodies in one authenticated call. The window opens with a two-item marketing pair from one author (`flypost`, a LinkedIn content studio) and closes with a **five-item** `mambalabsdev` Apify fleet that this catalogue documents as one line, plus a listing **correction** (`#7566`, AgentMsgr) rather than an arrival.

## What shipped

### Índices AR MCP

Keyless handshake, keyed calls, at `https://indices-ar-api-103907796853.us-east1.run.app/mcp`, *indices-ar* **0.1.0** on protocol **2025-06-18**, **twelve** tools of which **ten** were driven. A `POST /v1/keys` with an empty body issued a **50**-credit trial key with no registration, shared across the author's three APIs.

The arithmetic is the argument. `ajustar_monto` restated **500,000** pesos from 2026-05-01 to 2026-11-01 at ICL with factor **1.158108**, and it published both levels it divided (**32.13** and **37.21**), so 37.21 over 32.13 reproduces the factor to six decimals by hand. `actualizar_alquiler` produced a quarterly schedule of **531,133.04**, **582,511.06** and **621,640.01** whose three printed factors multiply to 24.32 percent against a stated 24.33, which is the signature of full precision kept internally and rounded only for display. `plazo_fijo` on **1,000,000** for 30 days returned simple interest of **19,726.03** at a 24 percent TNA chosen from **33** reporting banks, and compared it against measured inflation at **2.2** percent to report a real return of **-0.22** percent. `intereses_judiciales` computed Ley 27.802 art. 55 interest at **21.0883** percent, which is the ratio of two published BCRA series values (**97,654.4823** over **80,629.9143**), and returned the ceiling and the floor as amounts.

Two argument defects are recorded in the guide: the index enum is lowercase while the tool's own description writes the names in uppercase, and `calendario_fiscal` refuses a CUIT ending sent as a string with `expected number, received string`.

### AR Tools MCP

Same suite, same trial key, at `https://ar-tools-api-103907796853.us-east1.run.app/mcp`, **thirteen** tools with **eight** driven. The validators are the product: CUIT **20-12345678-6** validated to **20123456786** as a *persona_fisica*, and the check digit reproduces by hand from the 5-4-3-2-7-6-5-4-3-2 weighting (sum 148, mod 11 is 5, eleven minus 5 is 6). CBU **0170099220000067797370** validated with the bank resolved to **BBVA Argentina**. An Argentine mobile written `011 15 3456-7890` normalised to E.164, international, national and WhatsApp forms with the mobile `9` preserved.

Payroll reconciles to the cent: **1,500,000** gross to **1,245,000** net on **255,000** of statutory deductions (11 plus 3 plus 3), against an ANSES ceiling of **4,861,685.38** for 2026-11; the half-year bonus on the same salary is **750,000** gross and **622,500** net due **2026-12-18**; and an annual revenue of **18,000,000** in services lands in monotributo category **C** at **66,020.12** a month, whose three components sum exactly. `cotizacion_dolar` returned all **seven** dollar houses with a per-house update stamp.

### Scamstats MCP

Keyless end to end at `https://scamstats.org/mcp`, *scamstats* **1.0.0**, **seven** tools with **five** driven and no credential of any kind. The world estimate for 2025 reads **593.1 million** people scammed, **10.2** percent of adults, **US$208.14 billion** lost and **US$20.48 billion** returned. The United States alone carries **US$103.93 billion** of that loss, **49.9** percent of the world figure, with **9.95** billion returned at **9.6** percent of the loss, **1,008,597** cases recorded, and only **8.2** percent of victims reporting to police.

The methodological layer is why it earned a page rather than a mention: rows where a country does not publish a scam-type split say *Borrowed from* and name the countries whose average shape was applied, so a modelled share can never be read as a measurement. The error tier is a model of its kind, refusing `money_lost` with the exact enum (`people_scammed`, `share_of_adults`, `money_lost_usd`, `cases_recorded`) named in the response.

## Holds, with the gate named

- **Mindcase** (**#7564**) returns **401** to an anonymous handshake. 249 web-data APIs across LinkedIn, Instagram, TikTok, Maps, Amazon, reviews and jobs, which is the lead-generation and scraping class this catalogue already carries densely.
- **PDF Craft** (**#7562**) returns **401 Unauthorized** with no challenge document, so the tier is documented rather than driven, and document conversion is covered by Basis, SumOffice and the OCR entries.
- **Fontes** (**#7572**) is the strongest hold of the window: a PyPI stdio server with an adapter per jurisdiction for **124** jurisdictions of case law and legislation. It is held pending a driven local install, because a legal-corpus server with no measured tool surface is a listing.
- **joinfor.me** (**#7561**) sends a bot into Meet, Zoom and Teams. That class is covered and the value is in the bot, not in the record it leaves behind.
- **Dock Space** (**#7574**) needs a Dock Plus plan and offers **120+** presentation tools; the deck-editing class is covered and the plan gate is a credential promise.
- **Kove Journal** (**#7577**), **Laudanza** (**#7576**) and **Lykke** (**#7573**) are consumer verticals for health logging, choir songbooks and coursework. None carries a business data surface.
- **Inkmap** (**#7575**) and **HeurChain** (**#7563**) are a Mermaid mind-map app and an agent-memory server. Agent memory is infrastructure this catalogue documents as one class.
- **Browser.lol** (**#7559**), **e2e** (**#7571**) and **SEO Page to AI** (**#7560**) sit on browser automation, test tooling and SEO, three of the densest classes in the tree.
- **Flypost** (**#7554**) is a LinkedIn content studio; social scheduling is covered and the publishing lane is not the point of this catalogue.
- **Direcciones AR** (**#7557**) is the third API of the Argentine suite and normalises and geocodes addresses against INDEC data. It is keyless to the handshake and shares the trial key, held on the geocoding class, and its two siblings document the suite's shared credential.
- **mambalabsdev fleet** (**#7565**, **#7567**, **#7568**, **#7569**, **#7570**) is five one-tool Apify actor wrappers under a single author. Recorded as one line, per the standing rule that a publisher fleet is one entry and not five.

## Core listing check

Measured this pass rather than inherited. The fresh canonical still carries both `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`, the mcpservers.org detail pages remain **403** by edge policy, and mcp.so remains unlisted with all four of our slugs at **404**.

## FAQ

### Did anything new arrive on mcpservers.org?

No. The twelve numbered maps returned **66,338** raw entries on both captures, the distinct key set was **22,440** on both, and a `lastmod` scan at or after the cutoff returned zero rows. All three numbers are reported because a raw count alone is not a diff.

### Where did the three servers come from?

The submission queue. Two of the three are one author's Argentine suite (`indices-ar` and `ar-tools`, sharing one trial key) and the third is a keyless fraud-statistics server. The feed supplied one card and it was held on the agent cost class.

### Why is 22,474 recorded as a removal count anywhere?

Because the retained canonical capture was a union that included the **34** keys living only in `priority-servers.xml`. Differencing this pass's twelve-map set against that union returns 34 "removals" that are all present in the priority map on the same read, which is a scope error rather than a delisting.

## Counts

Canonical **66,338** against **66,338**, per-map identical and summing exactly, **0 additions** and **0 removals** on the twelve-map basis and on the twelve-plus-priority basis (**22,474** union, **22,440** twelve-only), **0** `lastmod` rows at or after the cutoff with the newest anywhere at **01:37:43Z**, priority **299** with **34** priority-only keys, remote **15** raw entries, feed **156,858** bytes with **36** server anchors, **1** client anchor, **30** stamps and **1** card above the cutoff, queue **#7554** to **#7577** with **24** arrivals, **3** candidates catalogued and **3** guides, **11** held with the class or gate named, guide tree **1,204** directories before this pass and **1,207** after, `hermes/mcp` Markdown **1,650** before and **1,654** after.
