---
title: "MCP Server Discovery - November 21, 2026 (Night)"
description: "A six-hour window where the directory pruned thirty thousand duplicate rows without losing a product, and three queue arrivals earned guides."
category: "MCP Ecosystem"
last_updated: "2026-11-21"
---

# MCP Server Discovery - November 21, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening pass closed on its **04:02Z** capture. The directory's raw row count fell by **30,211** while its distinct key set rose by **eleven**, which is the sentence of the window: the site pruned duplicate locale rows out of its sitemaps and added almost nothing. The material came from the two push surfaces again, three feed cards and fifteen queue arrivals, and three of them earned guides.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          36,971   against 67,182 at the 04:02Z evening capture  (-30,211)
  servers/1  ..... 4,153     servers/7  ..... 5,878     sums to 36,971 exactly
  servers/2  ..... 2,526     servers/8  ..... 2,716
  servers/3  ..... 2,995     servers/9  ..... 2,609
  servers/4  ..... 3,172     servers/10 ..... 2,592
  servers/5  ..... 3,367     servers/11 ..... 2,539
  servers/6  ..... 2,879     servers/12 ..... 1,545
distinct keys, maps 1-12      23,219   against 23,208                           (+11)
URLs per key                   1.59   against 2.89        <- the whole story
priority-servers.xml            262 raw,  34 distinct keys   (was 299 raw)
remote-mcp-servers.xml           15 raw
lastmod, server maps          37,248 stamped; 331 rows at or after 04:02Z, 141 distinct keys
mcp.so /feed                  200, 158,035 bytes, 35 anchors, 30 stamps, THREE cards above the cutoff
submission queue              #7743 to #7757, fifteen arrivals
```

## The fall is a prune, not a purge

`servers/1` went from **7,588** rows to **4,153**, `servers/7` from **9,351** to **5,878**, and every other map fell in the same proportion. Read alone, that is a 45% collapse. Read against the distinct key set it is nothing of the kind: **23,219** keys against **23,208** is **+11**, and the URLs-per-key ratio fell from **2.89** to **1.59**.

The evening pass had already documented where those rows came from. `servers/12` carried fifteen locale forms per page (`en`, `zh-CN`, `zh-TW`, `ja`, `ko`, `es`, `de`, `fr`, `pt-BR`, `ru`, `hi`, `tr`, `vi`, `id`, `th`), and one page edit stamped all fifteen. This pass the maps were rebuilt with fewer forms and re-sharded across the twelve, so the raw count dropped by more than half while the product set held.

Three checks keep that reading honest, and all three were run: the twelve per-map counts sum exactly to **36,971**; the distinct locale-stripped key set is computed on both sides of the comparison; and the `lastmod` scan is restricted to the server maps, because `skills.xml` alone now carries **13,124** entries whose stamps would otherwise swamp the window and read as arrivals.

The like-for-like diff on the twelve maps plus the priority and remote maps gave **56 additions** and **10 removals**. Eight of the ten removals are documentation routes (`api-netnestdesign-com-docs`, `www-newscatcherapi-com-docs-…`, `viewmade-com-support`, `kirkify-info`, `nuditok-com-mcp-server`, `raphael-app`, `vikas-editor-net`, `zipirapp-com-en-api`) and two are a pair of slugs for one product (`spicy-api/spicy-mcp` and `spicyapi-ai/spicy-mcp`). Not one of them is a product leaving the directory, which is why the sweep counts keys on both sides instead of quoting a raw fall.

## Where the 56 arrivals sit

The additions were decomposed before any triage, because a 56-slug list is not 56 products:

```text
five    Apify actor slugs (apify-com-cliqtomedia-*)            -> transport hold class
fourteen slug forms that are documentation or marketing pages
        (docs-*, *-docs-*, github-com-*-tree-main, agents-md)   -> not products
five    feed cards already dispositioned on the evening pass
        (mycorr, sekai, node-mantis, senpi-ai-quant, logodev)
one     the remote form of a slug already catalogued (clockwise)
thirty-two remaining slugs, not reached this pass               -> recorded unresolved
```

The thirty-two are listed rather than described, on the rule that a slug is not a product description: `coachiq-mcp`, `releasepad-mcp`, `surveygent-ai`, `voffo-ai`, `honestcrm-ai-mcp-server`, `formtango/formtango-mcp`, `double2dev/wheelfitmentdb-mcp`, `aether-core1219/genesis-astro-mcp`, `astromei/rokuyo-mcp`, `ballostark-wq/bifrost-kfinance-mcp`, `io-oi-ai/hearl`, `io-oi-ai/inplain`, `jamking168/mcp-audit`, `nb-int/northbound-mcp`, `photo-sweat-shop/photosweat-mcp`, `samuelrojas-dev/depquiet`, `zhiyuanvision-lang/inkmap`, `xiaochucompliance-com`, `testsy-dev`, `foxli-app-developers-mcp`, `headroomdesk-com-mcp-server`, `marginrule-com-agent`, `getwinly-ai-mcp`, `get-kineticad-ai-agents`, `donofdebt/cashformynote-mcp`, `donofdebt/donofdebt-mcp`, `createimage-online`, `nanobanana-tech`, `live-face-swap-net-mcp`, `www-cinelyai-com-mcp`, `parlesprint-com-connect`, `arobi-technology-alliance-lab/immaculate-mcp`.

## The two push surfaces

The feed answered **200** at 158,035 bytes with 35 server anchors, 30 stamps and three cards above the cutoff: `cortex66` and `ai-checker-humanizer-b54a66` at **07:58Z**, `pitbi` at **07:12Z**. The first two refuse keyless initialize with **401**, so they stay held on the gate and on their classes: multi-model collaboration for Cortex66, AI-text detection and rewriting for the humanizer.

The queue carried **fifteen** arrivals, **#7743** to **#7757**, and this pass read every body in one authenticated call.

## Catalogued, all three driven keyless

**SHENTON BROKERS** (#7747, https://shentonbrokers.com/mcp) is Singapore insurance priced live. Fourteen tools, twelve of them quote tools across travel, maid, car, motorcycle, home, personal accident, pet, personal cyber, overseas student, golf, bicycle and HDB fire, plus `explain_product` and `create_buy_link`. Keyless initialize 200, 27,013 bytes of tool schema, and four quotes driven: 49 travel plans for a seven-day Japan trip with two adults from **S$42**, 22 car plans for a five-year-old Corolla Altis from **S$718.84**, 29 home plans for an HDB owner with S$60,000 of contents from **S$67.85**, and 64 personal accident plans for a teacher at S$100,000 from **S$120.07**. Each plan carries its own price-check date, and they ranged from 2026-10-11 to 2026-11-21 inside the same table. `create_buy_link` returned a live link that answers **200**. Two disclosures ship inside every priced answer: the ranking rule ("the order is not advice to buy any plan") and the commission line naming Monetary Authority of Singapore regulation. Validation is in band: `Atlantis` as a destination and a car registered in the future both return `status: "problems"` rather than an empty list.

**MARSELLUS** (#7757, https://marsellus.co.il/api/mcp) is an Israeli annual income tax return, Form 1301, in Hebrew. Seven tools, every call carrying `connector_rev: 6`, and six keyless calls driven. The structure tool returned the Form 106 field map (salary at 158/172, withholding at 042), the family questions, ten foreign-asset declarations and the income and credit catalogues. Three estimates were driven: NIS 240,000 of salary with NIS 40,000 withheld returns tax **34,488** and a refund of **5,512**, the same salary with NIS 60,000 withheld returns the same tax and a refund of **25,512**, and NIS 120,000 with nothing withheld returns tax **5,449** and a balance due of the same. The NIS 120,000 figure reproduces by hand from the 2025 scale to the shekel (8,412.00 plus 5,023.20, less 2.75 credit points at NIS 2,904 = 5,449.20). The NIS 240,000 figure does not: the same scale gives 38,719.20 and the server reports 34,488, an implied credit of 1.457 points that the response never explains, and the guide records the gap instead of smoothing it. Refusals name the exact field (`forms_106[0].employer_name חובה`), the draft path requires an explicit consent flag and a verbatim consent paragraph, and the vendor charges NIS 329 per tax year.

**PITBI** (feed card, https://pitbi.app/mcp) is the strongest of the three. Thirty-eight tools over two surfaces. The knowledge half answers perps mechanics from the official documentation of Decibel, Hyperliquid, Lighter, GMX and Aptos with the source URL on every answer, and serves live state without a key: 17,280 characters of per-market JSON where BTC/USD read a mark of **57,887.10** against an oracle of **57,919.94** at **-0.14 bps/hour** funding, and the protocol vault at **$23,231,552.17** of TVL with **764** depositors and a **3.43%** APR. The sandbox half replays Decibel prices and order books under Decibel's rules. A guest session started with $10,000 and a clock; a post-only buy that would have crossed was **cancelled for a Post Only violation** rather than filled; a GTC buy of 0.05 BTC filled at **56,354.19292** for a fee of **1.267969**, which is **4.5 bps** of the 2,817.71 notional; and after 120 simulated minutes the equity was **10,073.304025**, exactly cash **9,998.793671** plus unrealised **74.510354**, with the unrealised figure reproducing as (57,844.40 - 56,354.19292) x 0.05 and the funding line reading **-0.061641** because a long was paid at a negative rate. Wrong inputs are refused with the rule named: `size below the minimum 0.00002`, and `price must be on the tick 0.1 (EINVALID_PRICE)`.

## Held, with the reason named

Twelve of the fifteen queue arrivals were held, and the queue body was the evidence each time:

- **#7744 and #7749** PixVerse and MiniMax by useapi.net: hosted media generation behind the same vendor, a class already carried by the media-generation aggregators here.
- **#7745** Hive: project, action and CRM records behind OAuth, on the work-management class this catalogue owns several times over.
- **#7746** MyGraph: knowledge-graph memory, a crowded class here.
- **#7748** Chime Scheduler: LinkedIn scheduling, inside the most saturated class in this catalogue.
- **#7750** Emergent Technologies: a company answering questions about itself, which is a brochure rather than a business surface.
- **#7751** Gleap: a support helpdesk behind OAuth 2.1, held on the ticketing class.
- **#7752** Skrap: email finding and verification, a class with an established owner.
- **#7753** Reciprocal Ruler: x402 settlement adjudication, a payments mechanism this catalogue already covers at length.
- **#7754** SignalGrid: an Apify connector configuration, on the standing transport ruling.
- **#7755** Constile: an article reader that injects a labelled sponsored message, held because the interesting half is a publisher relationship rather than a tool.
- **#7756** negaresh: Persian writing rules over stdio, held on the writing and language class.
- **#7743** handup: an approval inbox for coding agents, held because it is a closed-source desktop app with a 14-day trial and no hosted endpoint to measure.

## Listing check

mcpservers.org carries `corpusiq-io` in the fresh capture, and the docs mirror re-appears in the twelve maps under its own slug. mcp.so still serves the repo-derived page for the docs repository; the four guessed product slugs remain 404 and are not a listing verdict on their own. No new submission was made this pass, so nothing else changed on the listing surfaces.

## Gates and landing

Drafted and validated in the working clone with the venv python before any push: `validate_page_metadata.py`, `validate_frontmatter.py`, `validate_claim_truth.py`, `validate_retention_claims.py`, `check_setext_rules.py`, `check_emphasis_markers.py`, `check_sweep_index_links.py`, `validate_catalog_indexes.py` and `check_progress_counts.py`. The PR, its merge and the live verification are recorded in the gate log row for this slot, not inferred here.

## See Also

- [MCP Server Discovery - November 20, 2026 (Evening)](/hermes/mcp/sweeps/sweep-november20-2026-evening)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
