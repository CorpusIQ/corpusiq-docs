---
title: "MCP Server Discovery - November 5, 2026 (Night Sweep)"
description: "Night pass where both directory surfaces refused to be read, the sitemap caught up with a backlog, and the registry resolved 67 slugs into products."
last_updated: 2026-11-05
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november5-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 5, 2026 (Night Sweep)

## Summary

This pass fired on the **03:00 MST** tick, six hours after the **21:00 MST evening** read, on the night both named directory surfaces stopped answering: mcpservers.org returned **403** to a direct `/all` fetch, the reader proxy answered **401 03** bad IP reputation, two open proxies answered **408** and **522**, and mcp.so returned **zero bytes** to a direct fetch before an open proxy returned the homepage. The sitemap carried the pass: **19,513** server URLs against **19,344** at the evening capture, **194** additions and **25** removals, with **24** of the additions being the same servers reappearing after a namespace prefix was dropped. **One** server was catalogued and it was driven with **nine** live calls.

The mechanic this pass adds is about resolution rather than discovery. Of the **194** added slugs, **134** had no prior disposition under slug, heading, guide directory or spaced product name, and the official MCP registry answered for **67** of them with a title, a description, a website and a version. That turned a bare slug list into a product list, which is the only way a night pass at this gap ends with one honest ship instead of a page of guesses.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 14 sitemaps fetched directly (65.5 MB), locale prefixes stripped, set difference against the 21:05 MST capture | **19,513** server URLs against **19,344**, **194** additions, **25** removals, **24** of the removals matching an addition with the namespace prefix dropped |
| mcpservers.org `/all` | direct fetch, reader proxy, two open proxies | **403** direct Cloudflare block, **401 03** bad IP reputation on the reader, **408** and **522** on the proxies. Not read |
| mcp.so homepage | direct fetch then an open proxy | direct returned **0 bytes**; the proxy returned the page, **65** card objects collapsing to **53** distinct, newest `2026-11-05T06:47:30Z`, **one** card above the evening stamp |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **40** issues fetched, **10** in this window `#6763` to `#6772`, two of them listing updates |
| Official MCP registry API | `search` query per unresolved slug, 94 queries | **67** resolved with title, description, website and version |

## New Servers Catalogued

### SmartRetry Payment Tools MCP - Card Reference Data for Agents

Relevance: HIGH. **Endpoint verified** (HTTP 200 keyless `initialize` as `smartretry-tools` 1.0.0, four tools, nine calls made).

Published in the official registry as `com.smartretry/payment-tools` on **2026-11-03** and listed at `https://tools.mcp.smartretry.com/mcp` with no authentication, no sign-up and no API key. The four tools are `lookup_bin`, `lookup_issuer`, `lookup_mcc` and `lookup_decline_code`, all declaring `readOnlyHint`, `idempotentHint` and `openWorldHint` true, and the server is stateless so no session header is needed after `initialize`.

What was measured rather than quoted:

- `lookup_bin` `414709` returned **VISA CREDIT (TRADITIONAL)** issued by **CAPITAL ONE, NATIONAL ASSOCIATION**, United States.
- `lookup_bin` `519256` returned **MASTERCARD DEBIT (BUSINESS)** issued by **STATE BANK OF INDIA**, India, with the bank website and phone.
- `lookup_issuer` `chase` returned separate legal entities by jurisdiction, JPMorgan Chase in Singapore and the US Virgin Islands, Chase Manhattan in Thailand, Chase Bank USA in Puerto Rico and Disney Rewards issued by Chase in the United States.
- `lookup_mcc` `5411` returned Grocery Stores and Supermarkets, group Retail outlets, high risk no, with the Visa **45 percent** perishables rule and the Mastercard definition; `7995` returned betting with high risk **yes**; `coffee shop` returned **5814 Fast Food Restaurants**.
- `lookup_decline_code` `51` returned Visa 51 Not sufficient funds; `05` narrowed with `provider: Visa` returned Visa 05 Do not honor; `do_not_honor` returned the Stripe answer with its related statuses.

Three weaknesses are recorded because the calls produced them: the nonsense BIN `123456` returned a plausible record with no not-found state, the misspelling `chse` returned a German savings bank instead of Chase, and the related-code lists under a single number mix issuer response, ECI and 3DS namespaces. The `lookup_mcc` parameter is named `query`, so a call using `mcc` is refused with `-32602`.

## Also Identified (Not Catalogued)

The 194 added slugs were resolved in three ways before any disposition: **60** were already read on the evening pass over `/all` pages one to four, **40** more matched a prior disposition by distinctive token in the sweep corpus, and **94** had no mention anywhere and were sent to the official registry, which answered for **67**.

Held on carried classes, with the neighbour named in the catalog index: Pohoda Czech accounting workflows, EdgarStack on the EDGAR surfaces, MapleStats on Canadian open data, Asonix beside ASOgenic, Krawlup, SeoAiX, Grandranker and Crawlinx on the SEO class, CheckMyApp on site quality, BootLeads, Ecommerce Leads and Reuily on lead generation, Pixelary on ad conversion tracking beside PaidSync, Zipline, Willder, Mazarbul, Ontoloop and madeleine on agent memory, Time of Meeting on calendar utilities, Posteady on social scheduling, ArtifactSend on tracked shares and data rooms, Shiptrail on the AIS vessel entries already carried, HoneyLabs on threat intelligence, Kingy AI Facts on the model pricing index, PacketStream on scraping, LiveContext on workflow automation and UniOne on transactional email.

Outside operator scope and named so the next pass does not re-triage them: Agents Galleria on the feed, Viral Agent, MakerRadar, AppTierList, 99tests, Anywayr, Doorfarer, OffWeGoSIM, Symphony, Raploom, aithon telecom procurement, Ringback contractor missed-call text-back, Basemodo, Verifyum, 369 Meter and tshark-mcp from the submission window, plus 27 slugs the registry could not resolve and that carry no operator surface by name.

Axiom Works AgentReader from the window is the closest miss: UK Companies House due diligence with red flags and ECB FX rates are two real operator questions, but both legs are already carried by the registry entries and the FX surfaces, and the rest of the tool set is web reading and conversion.

## Core Listing Verification

- Official registry: `io.corpusiq/multi-source-mcp` present at versions **1.0.0** through **1.0.3**, remote `https://mcp2.corpusiq.io/mcp`. The **1.0.3** record is newer than the 1.0.1 this catalogue last recorded.
- mcpservers.org listing page answered **403** to a direct fetch, the same Cloudflare block that refused `/all`, so the listing could not be re-read this pass. The prior verified state stands.
- mcp.so remains not listed, unchanged from every pass since the delisting, and no re-probe was run on the four direct slugs this pass.

## Verification

- `gates.py docs` on the new guide: **pass**, zero findings.
- `gates.py docs` on the catalog index: **warn** only, the historical `aeo_faq` warning that fires on the index body.
- Guide frontmatter parsed with PyYAML, title **52** characters, description **151** characters, no em dash, no redacted token.
- See Also targets stat the directory tree before commit: stripe-mcp, pagofix-mcp and invoice-parser-pro-mcp all exist and the labels were read from each target's own frontmatter.

## Counts

Guide tree **1,101** directories before this pass and **1,102** after. Entries counting single-file guides **1,245** before and **1,246** after. Sources: twelve-sitemap canonical **19,513** against **19,344**; mcp.so **53** distinct cards with the newest at `2026-11-05T06:47:30Z`; submission window `#6763` to `#6772`, **10** items; **67** registry resolutions across **94** unknown slugs; **1** endpoint probed and **nine** live tool calls.
