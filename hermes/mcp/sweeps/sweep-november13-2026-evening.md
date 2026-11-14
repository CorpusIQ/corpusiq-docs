---
title: "MCP Server Discovery - November 13, 2026 (Evening)"
description: "A ten-hour window where one map grew by 234 entries while the key set fell 1,808, the feed carried five cards, and three guides shipped on what each one refuses"
category: "MCP Ecosystem"
last_updated: "2026-11-13"
---

# MCP Server Discovery - November 13, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement closed at 18:01Z. The canonical moved in both directions at once - **236** more raw entries, **1,808** fewer distinct keys - so the surface was read as a composition change rather than as arrivals. The delta that mattered came from the feed and the queue, and three servers ship: an invoice checker whose advertised line-item check never fires, a law firm that quotes fixed fees to an agent, and a UAE compliance platform that is the first of its class here.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
raw <loc> entries                65,059   against 64,823 stated at the 18:01Z capture (+236)
per-map counts                   priority 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
                                 6,756 / 9,351 / 6,589 / 4,030 / 2,607 / 1,677
per-map movement                 servers/9 +1, servers/10 +1, servers/11 +234, nine held
per-map sum                      65,059   matches the raw total exactly
distinct keys, locale-stripped   19,315   against 21,123 (-1,808, a slice not a purge)
URLs per surviving key           3.37     against 3.39 on the prior capture
newest lastmod                   2026-11-13T19:53:51Z
lastmod at or after 18:01Z       27 rows, 18:06Z to 19:53Z, all distinct listings
mcp.so /feed                     200 at 155,666 bytes, 37 anchors, 30 stamped cards
                                 5 above the cutoff: mandate-law 22:27Z, verity 20:50Z,
                                 verand 20:01Z, oneiq 19:45Z, agentdrive 19:12Z
submission queue #7293 to #7318  26 arrivals, no gaps, read with bodies
```

## The canonical moved both ways, and neither direction was an arrival

The raw count rose by **236** and the distinct locale-stripped key set fell by **1,808**. Both readings are correct and they describe one thing: the index re-sharded.

**234** of the 236 raw entries arrived in `servers/11`, the map that has carried every bulk publish for a week; `servers/9` and `servers/10` each moved by one. The twelve per-map counts sum to **65,059** exactly, which is the raw total, so no entry is double-counted inside this capture. Alongside that, the surviving keys now carry **3.37** URLs each against **3.39**, which is the arithmetic of more pages under fewer keys rather than of 1,808 products leaving.

Set-diffing against the capture retained from the 04:32Z night read gives **8** additions and **1,816** absent keys, and the eight additions are all one product: `google-ads-mcp-server-by-adkit`, `linkedin-…`, `meta-…`, `microsoft-…`, `pinterest-…`, `reddit-…`, `tiktok-…` and `x-ads-mcp-server-by-adkit`. Those are the nine AdKit cards the night pass resolved to a single registry namespace (`io.github.adkit/ads`) and held on a documentless static token gate. **Zero new products arrived through mcpservers.org in this window.**

The **27** stamped rows were read by slug and, where the slug was not self-describing, resolved through the official registry. Fifteen resolved to identifiable products and every one sits in a covered class or a consumer vertical: CloudGPU billing (**GPU class**, owner gpufinder), ClickHouse official (**data warehouse**), Goose (**agent runtime**), `2kw` EU LLM gateway, SchemaGate (**identity-scoped schema selection for text-to-SQL**), Designesy (**design scoring**, 40 checks), VolatiAI (signed sector signals with Ed25519 attestation), Agent402 (**prepaid agent payments**, 1,338 tools), Browser MCP and Oh My Android (**developer tooling**), RLHF Feedback Loop (**memory class**). Ten did not resolve - `flisk`, `wenlan`, `sv-number`, `terminal-tax-integrations`, `viafrei`, `cutvoke`, `kernelcad`, `marcellosso/localhost`, `dczhub`, `capacity-attest` - and are recorded as **unidentified** rather than catalogued or dismissed; a slug is not a product.

## The feed, five cards

Read at 155,666 bytes with 37 card anchors and 30 stamps in the `M/D/YYYY, HH:MM AM/PM` UTC form. Five sat above the 18:01Z cutoff, and the two that matter were both readable in full.

**Mandate Law** (`mandate-law`) - keyless, **eight** tools, a District of Columbia attorney taking agent-filed matters with published fixed fees. Shipped, with the fee table quoted by the tool rather than scraped.

**Verity** (`verity-5374e3` on the card, `app.ask-verity.com/api/mcp`) - a warehouse-native customer data platform for ecommerce: managed pipelines into the customer's own BigQuery, ROAS attribution, segments pushed to Meta, Google, Klaviyo, MCP reference published. Held on the **Adrails class** - [Adrails](/hermes/mcp/servers/external/adrails-mcp/) owns ad spend reconciled to real revenue with 69 tools and a formal proposal-and-approval write path, and Verity's claim ("AI agents that answer questions and take action across the platform") lands inside that owner. Its OAuth handshake is real and was measured: **401** `Missing Bearer token`, a protected-resource document at **200** with `mcp:read` and `mcp:write` and `resource_name: Verity`.

**Verand** (`verand`, OAuth) - content, daily Google rankings, AI-citation tracking and pre-publish compliance checks. Held on the **visibility class** carried by geolint, LogNorm and the saturated rank-tracking owners.

**OneIQ** (`oneiq`, OAuth) - read-only governed infrastructure context across VMware, Nutanix, Kubernetes and cloud. Developer and infrastructure class; no operator data slice.

**agentdrive** (`agentdrive`, OAuth) - a listing whose entire description is *"agentdrive is a remote MCP server available at https://useagentdrive.com"*. Prior disposition (the `AgentDrives` tool-directory entry) and self-disqualified by carrying no product statement at all.

## The queue, twenty-six arrivals

Read from #7293 to #7318 in one authenticated call, with bodies.

**Shipped, three.**

**Invoices to Spreadsheets** (`com.invoicestospreadsheets/invoice-spreadsheets` **1.0.0**) - keyless remote, **three** tools, six `tools/call` requests driven, the workbook downloaded and every cell read by reference. The finding is a check that never fires: the description promises to report "whether line items add up", and two targeted invoices - net **250.00** against line items of **100.00 + 100.00**, and net **100.00** against a line of **3 x 40.00** - both came back *"No arithmetic, completeness or duplicate problems found."* Two smaller defects beside it: a `null` VAT is compared as **0.00** instead of being flagged missing, and the `Line Items` sheet never fills its own `Net` and `VAT` columns.

**Auditro** (`co.auditro/auditro` **0.5.0**) - the first entry here for **In-Country Value and MoHRE Emiratisation**. Shipped at the OAuth tier with the handshake measured end to end: **401** `invalid_token`, `www-authenticate` naming the protected-resource document, that document **200** with **seven** scopes separating `auditro:read` from `auditro:write`, `auditro:files` and `auditro:sync`. The 99 tools and 47 read-only are the vendor's figures and the guide says so.

**Mandate Law** - from the feed rather than the queue, described above.

**Held, with the owner named.**

**Habits Guard** (`com.darmousseh/habits-guard`, filed twice - #7298 at 19:17Z and #7308 at 21:44Z) holds on the prompt-guard class owned by `glc PromptGuard` and `docs-safeprompt`. It is the more interesting entry of the two dozen (`0.8%` false alarms after 100 labels against `39.8%` for the model alone, with a published benchmark that admits it loses on injections hidden in tool output), and the reason it is held rather than shipped is class density, not quality. **Jobiba Hiring** and **Jobiba Jobs** hold on the jobs and ATS class carried by ATS Job Board Feeds and CareJobs.Now. **ASOMap** holds on the ASO class saturated after ASOgenic and Sonar ASO. **QRdx** holds on the QR and short-link class owned by Rus.sh and useClick. **TCGdetect** holds on the collectibles class (TickerMint, HobbyCardIndex, Valo.IA) and cannot be verified anyway: its primary host is still completing SSL and only the Supabase fallback answers. **AIfa Memory** and **PADAM NOCTURNE** hold on the memory class (PLUR, Azquo, MemoryBrain, Dawnmere, oortmem). **WACrew** holds on the unofficial-WhatsApp class: it is built on Baileys, the WhatsApp Web library, and its own submission says it is not the Business API. **HIPAA Studio** holds on the X12 EDI class (SignalEDI, FluentEDI) and is a licensed Windows binary with no driveable path from this host. **Rivervo** (`com.rivervo/mcp`) holds on the hosting-panel class; **Sonilo** on the saturated media-generation class; **Jot** is a proprietary paid Mac app; **mcp-conform** is a CLI rather than a server; **agentdomains**, **Dropify**, **unslop** and **vibe-shield** are prior dispositions, and `ghost-qa` joins the same author's fleet as developer tooling; **Ikoi** is an invitation-only gated preview of a game; **Hammer-MCP** edits Source engine maps. Both **Apify-scoped** submissions (#7295 China Social Data over WeChat, Weibo, Bilibili and Douban; #7296 WooCommerce and AliExpress product data) hold under the standing Apify-actor ruling, with the China surface the more interesting of the two and still distribution rather than a data product.

## What the window says

Two of the three ships were decided by a **refusal** or a **gap**: an invoice tool whose advertised check does not run, and a compliance server that answers nothing until an account exists and says so in a correct OAuth challenge. The third, a law firm selling fixed-fee review to agents, is a genuinely new shape in this catalog - the first professional service here that takes instructions rather than returning documents.

The directory surface itself contributed nothing new for the second pass running, and the map that keeps growing (`servers/11`) is a re-sharding rather than a source of arrival. On a ten-hour window the queue and the feed are the only surfaces that carry a delta, and the key-set drop is a reminder that a count without a set is a rumour.

## 🆕 November 13, 2026 - Midday Supplement (2 New, 2 Guides)

An hour where the sitemap and the feed were both flat, the queue carried nine arrivals, and two tools shipped on what they refuse.

## 🆕 November 13, 2026 - Midday Sweep (1 New, 1 Guide)

A window flat to the raw count, every per-map count and the lastmod cutoff, where the one guide shipped on a Bulgarian deadline chain reproduced by hand.

## 🆕 November 13, 2026 - Night Sweep (2 New, 2 Guides)

The pass that overturned the evening before it: the 1,817 keys read as absent came back, and the per-map counts were established as the only reliable arrival signal on this index.
