---
title: "MCP Server Discovery - November 19, 2026 (Midday)"
description: "Nine raw entries that were form changes, three feed cards, eighteen queue arrivals, and the catalog's first proven-optimal solver."
category: "MCP Ecosystem"
last_updated: "2026-11-19"
---

# MCP Server Discovery - November 19, 2026 (Midday)

Fired on the **10:00 MST** tick, five and a half hours after the **11:35Z** capture the night pass left on disk. The directory moved by **nine raw entries** and the whole of that movement was slug form rather than arrivals, the feed carried three usable cards, the submission queue carried eighteen arrivals, and two of them answer question classes this catalog had no entry for.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,677  against 66,668 at the 11:35Z capture  = +9
  servers/1  ..... 7,588      servers/7  ..... 9,351      sums to 66,677 exactly
  servers/2  ..... 5,949      servers/8  ..... 6,590
  servers/3  ..... 6,518      servers/9  ..... 4,022   (-2)
  servers/4  ..... 6,746 (+2) servers/10 ..... 2,608
  servers/5  ..... 6,954      servers/11 ..... 2,637
  servers/6  ..... 6,756      servers/12 ..... 958     (+9)
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw,   1 distinct key (clockwise)
distinct keys, twelve maps    22,717 against 22,720   = -3
distinct keys, unioned        22,752 against 22,753   = -1
set diff on the union         +4 additions, -5 removals
lastmod at/after 11:00Z       114 rows, 38 distinct keys
```

The three per-map movements do not add up to nine discoveries, and the set diff is the reason to say so. **Four additions:** three server keys (`connecteurs-juridiques-mcp`, `magicshot-mcp`, `shiftlog-mcp`) and one remote route (`clockwise`). **Five removals**, three of which pair with a surviving form in the same capture - `data-stalkchain-com` to `stalkchain-com-docs`, `signal-lab-jet-vercel-app-mcp` to `signal-lab-mcp`, `docs-videodb-io-pages-mcp-connect` to `video-db/agent-toolkit` - and the two that do not (`meta-stamp-v3-onrender-com-mcp-manifest`, `skybuyfly-pitchai-net-mcp-docs`) are both documentation-mirror slugs of the kind the eleventh and twelfth shards publish by the dozen.

The `lastmod` reading dates the movement rather than counting it. **114** stamps at or after **11:00Z** collapse to **38** distinct keys, and the multi-form keys are the tell: `stalkchain-com-docs`, `video-db/agent-toolkit` and `aakarim/openlore` each appear **fifteen** times, one per locale prefix, all three re-stamped inside the same second at **13:00:16Z**. That is a re-shard, not an arrival.

## The feed

`mcp.so/feed` answered **200** at **156,566** bytes with **30** stamps and three cards above the **11:35Z** cutoff: **alyvenmusic.com** at **13:54Z**, **alphagrowth-mcp** at **12:54Z** and **proxylane** at **12:53Z**. All three are already dispositioned or class-covered, and the case of `alphagrowth` is a reminder that a prior disposition lives as prose rather than as a heading: the term has no guide directory and no `###` entry, and the index carries it inside the dense finance and market-data hold list from an earlier pass.

The feed's newest card also carried no resolvable `/servers/` anchor ahead of its stamp - the card body names `alyvenmusic.com` and the anchors above it belong to other cards. It is recorded by name rather than by slug.

## Ships

Two, both from the submission queue and both keyless, both driven to their arithmetic rather than to a handshake.

- [Optimatika MCP - Proven-Optimal Optimisation Solver](/hermes/mcp/servers/external/optimatika-mcp/) - remote Streamable HTTP at `https://service-api.optimatika.se/optimisation/mcp`, *optimatika-optimisation-service* build **a74468c** on protocol **2025-06-18**, **three** tools, no auth of any kind. **This is the first operations-research solver in the catalog**, and the class had no owner: `linear program`, `operations research` and `integer programming` returned zero hits across the index and every sweep ledger. **The answers reproduce by hand:** maximising `3x + 2y` under `x + y <= 4`, `x <= 2`, `y <= 3` returned `OPTIMAL` **10.0** at `x = 2`, `y = 2`; a two-resource production mix returned **2,200** at `A = 40`, `B = 20` with labour at **100** of **100** and machine at **80** of **80** both binding; a minimisation returned **44** at `x = 1`, `y = 4` where the naive corner costs **48**; and an integer problem returned whole numbers `desks = 2`, `chairs = 3` for **22** rather than a relaxed **2.14**. **The refusal is a first-class result:** a model whose constraints contradict returns `state: INFEASIBLE` with the note that no solution satisfies all constraints, *or, occasionally, unbounded* - the vendor naming the one ambiguity a solver status cannot resolve. **The limits are asked, not discovered:** `environment` reports a Polar shared instance with no licence key, ojAlgo solvers only, a ceiling of **1,000** variables or constraints, a **30**-second suffice after which a result returns `FEASIBLE` unless proven optimal, and a **60**-second abort.
- [Visamundi MCP - Visa and Entry Rules by Nationality](/hermes/mcp/servers/external/visamundi-mcp/) - remote Streamable HTTP at `https://mcp.visamundi.io/`, *visamundi-public-mcp* **2.0.0** on protocol **2025-06-18**, **eight** tools of which five are keyless reference reads, registry `io.visamundi/visa`. **The catalog's first global visa matrix** - [CheckChinaTransit](/hermes/mcp/servers/external/checkchinatransit-mcp/) answers one country's transit rule precisely, this answers the nationality-by-destination question as a table. **The rules are typed, which is the reason to integrate it:** yellow fever for Kenya came back `needed` with the certificate conditioned on arriving **from** a country with transmission risk, aged one and over, while malaria came back `recommended` with the altitude and city carve-outs stated. **Priced, not described:** Vietnam returns a single-entry e-Visa at **25 USD** for **90** days and a multiple-entry at **50 USD** whose own description carries the exception that a stay under **45** days needs no visa at all. **Two defects recorded rather than smoothed:** `get_vaccines` and `get_customs` reject the argument `destination` that their descriptions and the server's own instructions both name, requiring `country_code`; and an invalid country code returns **HTTP 200** with `success: true` beside `code: country_not_found`, so a caller checking the status flag reads a failure as a success. The requirement field itself has no unit: `FR` into `CN` returned **30** and `CA` into `MX` returned **180**, which mean days permitted without a visa, beside named statuses `visa required` and `e-visa` for other pairs.

## Also identified this pass (not catalogued)

Held with the gate or class named.

**From the queue.** **SparkLayer** (**#7664**), **37** tools over a B2B wholesale platform with bulk SKU pricing, customer groups and annotated write tools, answers **401** at `initialize` with no keyless surface to enumerate, held on the commerce-platform class and on that gate. **Writ Cloud** (**#7662**), **41** tools turning a website into an API with crawling, monitors and schedules, held on the scraping and web-to-API class already dense with extraction entries. **Vendo AI** (**#7657**), a **405**-tool sales platform with signal searches and outreach, held on sales intelligence beside Hilead, StackScope, Leadbay and Vibe Prospecting. **lafo.trade** (**#7649**), read-and-brake access to a member's trading robots behind a `lafo_` API key, held on the trading class and because nothing of it is measurable without a member account. **mebius.design** (**#7659**) held on the design-system and component class carried by Shadcn; **gomami-mcp** (**#7661**), **29** VPS-management tools with three access tiers and a protected-server list, held as single-provider infrastructure control beside the VPS pricing entry; **Klakix** (**#7660**), **19** media-generation tools, held on the media-gen aggregator class carried by Varosity and Superpowers; **arancelmx-mcp** (**#7663**) held on the customs class this catalog closed twice in two days with [Tariff Monitor](/hermes/mcp/servers/external/tariff-monitor-mcp/) and [htsapi.dev](/hermes/mcp/servers/external/htsapi-mcp/); **Paletoo** (**#7651**) on social-design generation; and the **mambalabsdev** five (**#7650**, **#7652**, **#7653**, **#7655**, **#7656**) continuing the standing Apify-actor ruling, one tool per actor.

**Vargov®Design**, filed twice (**#7665** stdio and **#7666** remote) for one product: a made-to-order lighting catalogue whose five keyless tools drive well - `get_composition` on `LC0413` returns the brand's own description, the rooms it is calculated for, Art Nouveau and romantic classicism as its style, and `no_elements_in_stock`; `dealers_and_showroom` returns a Moscow showroom and dealers in Dubai and Hanoi. It is held on the single-brand design-catalogue class already carried by Aalto, Louis Studios and House AI rather than on its own evidence, and the keyless surface that Aalto lacked does not by itself turn a product lookup into a business-operations question.

**From the canonical.** **connecteurs-juridiques-mcp** answers the French and EU legal corpus - Légifrance, Judilibre, BOFiP, EUR-Lex - which is the class [Casus MCP](/hermes/mcp/servers/external/casus-mcp/) owns with **230,419** articles of **77** codes and **3.4** million decisions, beside the LEGAION, aka-recht, Specter Cite and VeriActa quartet, so it is held on that owner. **shiftlog-mcp** is the `it.shiftlog/mcp` billable-hours product whose feed card this catalog held yesterday on the consumer class, and a canonical arrival does not re-open a disposition. **magicshot-mcp** returns no registry record and no readable detail route, and is recorded as an unidentified slug rather than inferred into a product. **clockwise**, the one remote route, was dispositioned on an earlier pass as one route published under fourteen locale forms.

**From the feed.** **AlphaGrowth** was held on the finance and market-data class; **proxylane** is proxy infrastructure; **alyvenmusic.com** is consumer music generation.

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

## Counts

```text
canonical raw        66,677  against 66,668   (+9)
canonical keys       22,717  against 22,720   (-3)
union keys           22,752  against 22,753   (-1)
set diff             +4 additions, -5 removals (three removals pair to a new form)
lastmod >= 11:00Z    114 rows, 38 distinct keys, three keys at 15 forms each
feed                 156,566 bytes, 30 stamps, 3 cards above the cutoff, 0 shipped
queue                #7649 to #7666, 18 arrivals
catalogued           2 with 2 guides
held                 16 with the gate or class named
guide tree           1,213 to 1,215
hermes/mcp Markdown  1,664 to 1,667
```
