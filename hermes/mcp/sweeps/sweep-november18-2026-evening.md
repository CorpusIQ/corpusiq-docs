---
title: "MCP Server Discovery - November 18, 2026 (Evening)"
description: "A 326-entry ingestion wave that added one product, a feed of five consumer cards, and a small-business books server whose demo answers without a credential."
category: "MCP Ecosystem"
last_updated: "2026-11-18"
---

# MCP Server Discovery - November 18, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement closed. The directory moved by its largest raw count in a week and the movement was an ingestion wave rather than a burst of new products. The feed carried five consumer cards above the cutoff, the submission queue carried twenty-five arrivals, and one of them is a small-business books server whose public demo answers without a credential, which is how fourteen of its twenty-two tools were driven.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,668   against 66,342 at the 18:00Z midday capture (+326)
  servers/1  ..... 7,588   held    servers/7  ..... 9,351   held
  servers/2  ..... 5,949   held    servers/8  ..... 6,590   held
  servers/3  ..... 6,518   held    servers/9  ..... 4,024   held
  servers/4  ..... 6,744   held    servers/10 ..... 2,608   held
  servers/5  ..... 6,954   held    servers/11 ..... 2,637   held
  servers/6  ..... 6,756   held    servers/12 ..... 949     +326 (623 to 949)
                              the twelve counts sum to 66,668 exactly
priority-servers.xml          299 raw,  34 distinct keys, none of them in the twelve maps
remote-mcp-servers.xml         15 raw
distinct keys, twelve maps    22,720 against 22,440  = +280
distinct keys, union w priority 22,754 against 22,474  = +280
removals, after %23 normalisation   0
lastmod rows at or after 18:00Z     1,500 rows, 596 distinct keys
                                    276 of them new, 320 held and re-stamped
                                    forms per key: 33 keys at 15 forms, 182 at 3,
                                    373 at 1, 5 minor
                                    hour of newest stamp: 18Z 47 / 19Z 72 / 20Z 46 /
                                    21Z 39 / 22Z 45 / 23Z 31 / 00Z 295 / 01Z 10 /
                                    02Z 9 / 03Z 2
mcp.so /feed                  200, 156,861 bytes, 37 anchors (35 server cards,
                              1 agents card, 1 clients card), 30 stamps,
                              27 distinct stamped server slugs, 5 above the cutoff
submission queue              #7605 to #7629, twenty-five arrivals, bodies in one call
```

The whole raw rise sits inside `servers/12`, which has been the shard every arrival has landed in since it appeared on November 17. The key set rose by the same **280** on both the twelve-map basis and the union basis, so the priority map contributed nothing new and no reading of this window depends on which basis is used. Normalising `%23` on both sides of the comparison removes three phantom "removals" that are the same pages under a different fragment encoding.

The `lastmod` distribution is the shape of the wave: **295** of the 596 stamped keys carry their newest stamp inside the single hour beginning **00:00Z**, and **33** keys appear under fifteen locale forms each. That is one ingestion run, not 596 discoveries.

## The wave is an ingestion echo, and the slug census says so

Decomposing the **280** additions before triaging any of them:

```text
cotlet-dev-integrations-*    50   one integration-vendor fleet (17hats, odoo,
                                  pennylane, procore, recurly and 45 more)
apify-com-*                   9   the Apify actor fleet, held as a class since October
documentation mirrors        23   slugs ending in -docs-mcp or -docs
agents pages                 14   slugs ending in -agents or -for-agents
llms.txt pages                3
api pages                     4
developers pages              5
mcp endpoint slugs           70   product-shaped slugs, triaged individually
other                       102   product-shaped slugs, triaged individually
```

Twenty-one of the individually triaged slugs match a submission filed in the same window by name rather than by coincidence: `flystopover`, `thunderbirdmcp`, `vbtnl-com`, `human-use`, `metri-diary-com`, `dank-meme-sounds`, `lumman-co-mcp-multi-books`, `antevo-ch-mcp-companies`, `antevo-ch-mcp-mandates`, `signbuddy-eu`, `supplywise-com-au`, `simonjamescarroll-thunderbirdmcp`, `xmevans10-dealhound`, `alertviz-com-eurokyb`, `hitl-sh`, `jig-clawhard-com`, `notary-clawhard-com`, `vouch-clawhard-com`, `mcp-mint-gg`, `testbay-dev` and `run-peerfoundry-ai-quickstart`. The submission queue and the sitemap are two views of the same ingest, which is why the queue is triaged first and the wave second.

Two fleet rules apply unchanged. `cotlet-dev-integrations-*` is one vendor's API wrapper set under fifty names, evaluated once, and the class it serves (hosted SaaS API wrappers per platform) is already carried. `apify-com-*` remains a hold class on the Apify distribution ground recorded in October.

## The feed's five cards did not survive a class check

`mcp.so/feed` answered **200** at **156,861** bytes. The anchor count is **37**: **35** server cards, one `/agents/` card (`vindaris`, 19:40Z) and the `/clients/` sponsor card. **30** stamps against **35** server anchors is the shape every recent pass records, and pairing each stamp to the nearest preceding anchor of any family keeps the sequence readable through the two non-server cards.

Five server cards sit above the 18:00Z cutoff and all five are held by class:

```text
shiftlog-it            20:26Z   shift and time logging, workforce utility class
moodlight              20:39Z   ambient consumer device
spooky-particles       20:46Z   creative and game effects
wals-pro-ai-4-weclapp  20:47Z   consumer app connector
openshorts-io          00:42Z   short-video generation, consumer media class
```

None of the five is an operator data surface, and the media-generation class has been saturated since the Varosity and Superpowers rulings.

## The queue: one ship, twenty-four holds

Twenty-five arrivals between **#7605** and **#7629**, read with bodies in one authenticated call.

**Catalogued, with a guide:**

- [Contha MCP - Small-Business Books Read by an Agent](/hermes/mcp/servers/external/contha-mcp/) - **#7627**, remote Streamable HTTP at `https://demo.contha.com/api/mcp` for the demo and `https://app.contha.com/api/mcp` for production, `contha-demo` **0.4.0** on protocol **2025-06-18**. **Twenty-two** tools listed keyless and **fourteen driven**, all read-only on the demo, against **six** write tools on the production service that file transactions, add cash entries and maintain rules, budgets, bills and goals, and that the vendor says can never move money. **The arithmetic closes:** free-to-use **$40,380.70** reconciles from cash **$45,509.84** less cards **$1,878.27**, goals set aside **$1,595.50**, bills due in thirty days **$296.38** and tax due on the return **$1,358.99**; the 2026 Schedule C reads gross receipts **$71,500.00** and expenses **$11,213.65** across four lines that sum exactly (car and truck **$91.20**, contract labor **$7,258.99**, office **$166.32**, other **$3,697.14**) for tentative profit **$60,286.35**; self-employment tax reproduces at **$8,518.19** on **$55,674.44** of taxable earnings. `audit_misfiled_business` returns **five** business charges filed on the personal side totalling **$115.98**, which is the tool that makes the two-book split worth having. **Recorded rather than reconciled:** the headline tax figure of **$1,358.99** appears in both `get_overview` and `get_tax_estimate` and does not reproduce from the fields published beside it (balance due **−$1,668.32**, projected full-year **$16,791.48** less **$16,200.00** paid at **$591.48**, all four installments at `toPay` **0**), and `get_budget`'s `leftToSpend` of **$1,869.27** includes **$1,050.00** of carried-in budget that a reader checking `planned − spent` will read as an error. Production is OAuth with PKCE S256, open dynamic registration and separate `read` and `write` scopes, both documents on the same host.

**Held with the gate or class named:**

- **Querya** (**#7624**, `io.querya/querya`), Google Ads with **59** tools including Keyword Planner forecasting, validated change previews and undo, is the strongest hold of the pass. `tools/call` gate first: `POST` returns **401** with `scope="ads.read"` and a protected-resource document, so nothing was measurable without an account. The class is covered by AdRails (Google Ads with plan, validate-only, commit and spending caps), AdsCove (323 tools over Shopify, Meta, Google and TikTok with approval-gated writes) and the AdKit fleet, and the differentiator Querya offers, a validated preview with a plan id and undo, is the same one AdRails was catalogued on.
- **Spica Post** (**#7628**, `com.spicapost/spica-post`), OAuth with dynamic registration and a `studio` scope, held on the social-scheduling class already carried; the endpoint answers **401** with a sentence that names the gate rather than hiding it.
- **DirectCase Legal Search** (**#7614**, `ai.directcase/directcase`), legal research over national and EU law with the wording in force on a given date, held on the legal trio (LEGAION, aka-recht, Specter Cite) already carried, with its **401** and protected-resource document recorded.
- **gaents** (**#7629**, `com.gaents/api`), keyless `initialize` **200** with **14** tools over a pay-per-call module marketplace, held on the agent-marketplace and x402 rail classes carried since the inference-indexer and PZERO rulings.
- **Search402** (**#7625**), x402 web search, on the same payment-rail and search class.
- **volatiai** (**#7607**), already dispositioned on November 13 as signed sector signals.
- **Stopover** (**#7617**) and **Seatac Co** (**#7611**), travel planners, one travel vertical each.
- **Better Llama** (**#7616**), Chilean public data over eleven tools, held on the donniertf open-data expansion and the regional reference-data class.
- **thunderbirdmcp** (**#7615**), **56** tools over Thunderbird, IMAP, Gmail and Graph, held on the inbox class carried by Ficiel, Mailroom and Kaption and on the local-profile install gate.
- **Voicedex** (**#7608**), a speech-model pricing catalogue, held on the voice and TTS class carried by DialNexa and KaiCalls.
- **OpenLandscape** (**#7612**), drug pipelines, a pharma research vertical outside operator scope.
- **x402 Tool Shop** (**#7613**), weather, wallet risk and sanctions screening per call, on the x402 class with its OFAC leg noted as the one slice to revisit if a compliance section opens.
- **vbtnl** (**#7619**), agent-deployed hosting; **Sempera** (**#7618**), phone plans not yet purchasable; **Importly** (**#7620**), media download and transcription; **SignOff Studio** (**#7609**), local API verification for coding agents; **Osmanth Agent Marketplace** (**#7610**), marketplace class; **AimYear** (**#7605**), **LeadWebia** (**#7606**), **CT** (**#7626**), a vendor documentation server over a C/C++ test tool; **iphone-mcp** (**#7623**), local stdio device control; **ShortSpec** (**#7622**), barcode facts; **Rephrase AI** (**#7621**), writing utility.

The wave's individually triaged slugs follow the same dispositions: `paceads`, `misiki-in/gocommerce`, the `mambalabsdev` five and the `sitesy.ca` family are prior or class holds, `alertviz-com-eurokyb` lands on the company-data class carried by HirePulse and the aVenture family, `antevo-ch-mcp-companies` and `-mandates` continue the `antevo.ch` fleet dispositioned on November 4, and `lumman-co-mcp-multi-books` and `xmevans10/dealhound` did not answer a keyless handshake, so they are recorded as endpoints that refused rather than as products.

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

**Counts.** Canonical **66,668** against **66,342** (+**326**), key set **22,720** against **22,440** (+**280**), **0** removals, **1,500** `lastmod` rows collapsing to **596** keys of which **276** are new, feed **156,861** bytes with **5** cards above the cutoff and **0** shipped, **25** queue arrivals, **1** catalogued and **24** held with the class or gate named.
