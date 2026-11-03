---
title: "MCP Server Discovery - October 31, 2026 (Night)"
description: "Four hours on: a WCAG scanner measured on our own homepage, a creator marketplace that quotes coverage without a key, and a labour-market exchange that reproduced its own published figure."
last_updated: 2026-11-01
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october31-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 31, 2026 (Night Sweep)

This pass fired at `21:00 MST`, four hours after the afternoon read. The mcp.so homepage `recentServers` block returned **132** parsed cards against **140** at the afternoon read, which is the same block-count variance recorded twice this week and not a change at the source. The newest `createdAt` was the reliable reading, as usual: `2026-11-01T00:15:52Z` against `2026-10-31T17:06:19Z` at the previous pass, so **six** cards sat above the afternoon stamp.

The submission window moved much further. The afternoon pass closed the window at `#6511`; tonight it ran to `#6530`, which is **eighteen** submissions between `19:06Z` and `03:53Z`, every one read with its body rather than triaged from a title.

Three shipped. All three answered a live endpoint, and two of them answered without any credential at all, which is the test this pass applies before a guide.

## New: the accessibility scan nobody runs until a form asks

[Lazynext Accessibility Checker MCP](/hermes/mcp/servers/external/lazynext-accessibility-checker-mcp/) is remote Streamable HTTP at `https://checker.lazynext.com/mcp`, keyless, `initialize` answering **HTTP 200** in 0.19 seconds with `serverInfo` `accessibility-checker` at **1.0.0** and `tools/list` returning all **four** tools. `list_rules` returned **75** WCAG criteria, each tagged `static` or rendered.

Two live scans were made on our own homepage, and the result is the argument for the entry. Mobile viewport: score **46** on `score_model` `weighted-v1`, **28** issues across **12** distinct criteria, section 508 non-conforming against WCAG 2.0 AA with **5** clauses implicated (302.1, 302.2, 302.3, 302.7, 302.9), a benchmark at the **54th** percentile of **26** sites, and a persisted report at `checker.lazynext.com/report/c036dcc1-4e6`. Desktop viewport: the first call timed out at a 60-second client limit and the retry returned in **61.1 seconds** with score **46** and **29** issues.

The findings are specific in a way most audit tools are not. Two `wcag-2.5.3` failures where an `aria-label` replaces the visible text instead of containing it, so voice control cannot address the control by what it says. One `wcag-1.4.10` on a `<div>` with a fixed 1000px width that cannot reflow at 320px. Seven `wcag-1.1.1` findings that are all filename `alt` text: "Shopify", "HubSpot", "eBay", "HighLevel", "Odoo", "ActiveCampaign". Those are content edits, not engineering projects, which is how an operator without an accessibility specialist gets from a procurement form to a work list.

**Gap recorded.** The vendor site lists API, MCP and A2A as Pro features at **$9 per month**, with the free tier at 3 rendered scans a day, and yet the MCP endpoint accepted no key and labelled both scans `plan: "free"`. Whether that is a launch window or a plan gate that is documented but not enforced is not stated where this pass could read, so it is recorded as an unresolved discrepancy. `scan_html`, `get_report` and the site crawl were not exercised, the benchmark cohort is unpublished, and the repository is source available rather than open source.

## New: what a creator post costs, before anyone answers an email

[distribution.tech MCP](/hermes/mcp/servers/external/distribution-tech-mcp/) is remote Streamable HTTP with a guest tier at `https://app.distribution.tech/api/mcp/guest` that needs no key: `initialize` **HTTP 200** in 0.34 seconds, `serverInfo` `distribution` at **1.37.0**, and **six** tools with full schemas.

The guest surface returns counts rather than names, and the counts are the reason to read it. `inventory` at `04:02:35Z` reported **1,005** approved X creators, **86** bookable now and **255** posts carrying a current price. `resolve_audience` on a described profile (a B2B AI data layer, ecommerce and SaaS operators, US) resolved to three segments and narrowed that to **792** creators, **63** bookable and **187** priced posts, `thin: false`. The 213-creator gap between the whole network and one audience is exactly the number a founder cannot get from a DM.

`guest_status` states its own limits: **60** calls per 10 minutes per client address and **3** `plan_quote_guest` calls per **7 days**, which makes this a coverage tool rather than a price research tool unless you are careful with your three quotes.

The buying half is documented at `/docs/agents` as **22** tools, and the design is what earns the guide: a key carries a spend **mandate**, signing a plan produces a payment link inside that mandate, brands are reviewed before their agent can buy, creator names and two alternates arrive before signing, swaps are allowed before signing, and every placement returns `evidence`. An agent that can propose a plan and stop at an approval is a procurement process a founder can audit.

**Gap recorded.** `plan_quote_guest` failed with `unavailable: The network could not be read just now. Try again.` so no all-in price was obtained, and that failure consumed one of the three weekly guest quotes. Nothing was purchased and no brand approval was sought, so `create_campaign`, `approve_plan`, `evidence` and the mandate enforcement are read rather than driven, and the creator side of the payout split was not read at all.

## New: pay data that reproduces its own published number

[GWIX MCP](/hermes/mcp/servers/external/gwix-mcp/) is remote Streamable HTTP at `https://api.gwix.ai/mcp`, and the live server answered a keyless `initialize` with **HTTP 401**, JSON-RPC `-32001`, `Authentication required: sign in with OAuth or send a GWIX API key as a Bearer token.` A probe on `/v1/mcp` returned a different 401 shape, an RFC 7807 problem body with a `request_id`, which tells you the public API and the MCP server sit on different routers and both are closed.

The vendor publishes a keyless sample at `https://api.gwix.ai/mcp/sample`, and that is where this pass measured. `initialize` **HTTP 200**, `tools/list` returning **27** tools in 37,580 bytes. `get_data_status` for the US reported `release: "2026-W41"`, `last_complete_week: "2026-04-12"`, and a sample that covers the US, UK and Germany at **6 months** of lag with history from `2024-10-14`, market level only, no company or industry splits.

Then the verification that matters. `get_pay` for SOC **47-2111** in metro `mtr_midland_tx` for 2026-Q1, the exact example GWIX publishes in its own free sample, returned **74** ads with pay and percentiles of **38,215 / 48,368 / 66,781 / 76,526 / 94,694** USD per year. The median matches the vendor's published figure to the dollar. A data product that reproduces its own advertised sample on a third-party call is a data product whose other rows can be trusted to be consistent, which is a stronger signal than any marketing page.

The metadata is where the argument lives: 13-week quarters of whole Monday to Sunday weeks ending on the last Sunday on or before the quarter's last day; each country's currency converted at the period average with `fx_rate` returned per row; occupation codes crosswalked to US SOC 2018 with the rule that each SOC is a separate row set and never pooled. That is the machinery that makes a pay figure checkable by somebody who was not in the room.

**Gap recorded.** `job_offer_check`, the tool closest to a decision, returned a CloudFront **504** after 30.07 seconds while the row tools answered in 0.26 seconds, so the written-analysis path is unverified and the cheap path is fast. No credential exists, so the credit accounting, the report tools and `get_account_usage` were not driven. The **247**-country coverage claim is the vendor's; the sample proves three. The credit cost of a typical question is the number an operator needs and this pass could not produce it.

## Read and held

The mcpservers.org `/all` page came back through the r.jina.ai reader proxy with **23** unique slugs and the counter at **18,577** against **18,402** at the afternoon read. Every slug matched at least one existing file in the tree, so the page carried no delta; the counter moved because the catalogue is growing, not because the newest page changed. Slugs read: `ravenwallet-pro-docs-ai`, `cymetica-com-mcp-v1-stock-vectors`, `theluckystrike`, `reason-machines`, `auscaster`, `www-reslyce-com-flow-mcp`, `yir-ai-mcp-server`, `kinti`, `screenifystudio`, `liyupi`, `gmapscrawl-com-google-maps-scraper-mcp`, `www-repeatpost-com-mcp`, `compi-ai`, `secfeedapi`, `anantharajuc`, `aiimage-com`, `asms-ai`, `reinventa-es-asistentes-ia`, `apex-byte-technologies`, `renewroster-com-docs-mcp`, `whiteboardanimation-ai-mcp`, `nitrozenio` and `docs-safeprompt-dev-mcp`.

Of the six new mcp.so cards above the afternoon stamp, five are recorded here with the reason, because a card that is not dispositioned becomes work for the next pass:

- `corridome` (`2026-11-01T00:15:52Z`) is a US private-equity and M&A register, firms, funds, deals, advisers and people, each answer with the record behind it, and its own card states it requires a Corridome membership. Held on access rather than quality: `corridome.com` answered **200**, no keyless surface is offered, and the deal and fund entries here already cover the class from the filings side.
- `gwix` (`18:49:44Z`) shipped, above.
- `browse-bridge` (`23:07:27Z`) shares selected Chrome tabs with an agent at `https://mcp.browsebridge.com`, held in the browser automation class this catalogue carries heavily.
- `listing-698e96` (`19:17:31Z`) is Tabulya, a Russian-language spreadsheet with AI, Python and SQL, held as a localised product rather than an operator surface this catalogue can apply.
- `coinvello` (`19:10:08Z`) is the same arrival as `#6513`, dispositioned below.
- `myimage2life-8891ac` (`18:02:28Z`) turns a chat image into a printed product and is consumer retail.

## The issue window, dispositioned

Eighteen submissions between `#6513` at `19:06:26Z` and `#6530` at `03:53:43Z`. Three shipped, fifteen recorded so the next pass cannot read them as fresh.

`CoinVello` (`#6513`) is non-custodial crypto payments for agents: checkout sessions and invoices priced in fiat or crypto, webhooks, prepaid credits, test payments, across Bitcoin, Ethereum, Base, Arbitrum, Optimism, Polygon, BNB Chain, Avalanche, Solana and Tron, MIT licensed, `npx @coinvello/mcp` local stdio, keys refused unless `COINVELLO_ALLOW_LIVE=1`, and the card says nothing in the server can move funds. Held on saturation: the agent payments class here already carries wallets, x402 readers, USDC rails and Solana transfers, and this one needs a key before it answers anything.

`ILens` (`#6514`) decompiles .NET assemblies one member at a time, Windows x64 via `winget`, held as developer tooling outside the operator surface.

`Clearcote MCP` (`#6515`) drives a Chromium fork with about **20** tools and hands the same browser to Playwright, Puppeteer, browser-use or Crawl4AI through `get_cdp_endpoint`, with the fingerprint set in C++ rather than by a stealth plugin. It is the strongest hold of the window on capability and it is held on class: browser automation is one of the deepest slices in this catalogue, and the CDP handoff is the specific feature to test if that ever changes.

`Fittest` (`#6516`) is materials science, three foundation interatomic potentials producing a trust verdict against a DFT threshold on non-periodic molecules of seven heavy atoms or fewer. Remote, keyless and genuinely novel, and it answers a question no business operator asks.

`CSI MCP` (`#6517`) drives SAP2000 and ETABS through their COM API on Windows only, with **67 of 67** rebuilt verification examples matching published values, which is unusually rigorous evidence for a submission. Held on platform and vertical: structural engineering on Windows, and the catalogue carries no construction slice for it to join.

`recall` (`#6518`) serves Claude Code's own markdown memory files to other agents with `[[wiki-links]]`, breadth-first recall trimmed to a token budget, secret redaction and a `--read-only` mode. Zero dependencies, MIT. Held on saturation in the agent memory class.

`conductor` (`#6519`) is **23** tools where every one has an input schema, an output schema and a mandatory verifier that checks the result in code before the client sees it, with deterministic jobs run as plain code and model-backed jobs run hermetically with retry and visible failure. It is the most interesting reliability entry of the window and it is developer tooling; the verification contract is the part to revisit if this catalogue grows a reliability slice.

`Betterloop` (`#6520`) ranks fixes from real users, rage clicks, dead buttons, JavaScript errors and slow pages, with a free plan and a Bearer key. Not measured because the key is required, and the analytics class is deep.

`Wordy Page` (`#6521`) publishes a page or a multi-site to `wordy.page/your-name/` in one call, free, with OAuth 2.1 and PKCE or a personal key, and an agent mode that takes custom HTML and CSS with outgoing links only. Held on saturation: publishing entries here number in double figures.

`nana800` (`#6522`) is a no-code automation builder positioned against Zapier, Make and n8n with **44** tools and ruble payments, keyed. Held on locale.

`Frank` (`#6524`) runs AI-moderated voice and chat interviews with your customers and returns themes with verbatim evidence, **14** tools, OAuth 2.0, publishing gated on the account owner's separate approval because it is the only action that spends credits. The endpoint answered **401** with `Authentication required` in 0.27 seconds, which is a measured refusal rather than an absent surface. Held on saturation: four customer-research entries already sit here, and the promotion test is whether themes come back as quotable evidence per interview rather than as a summary.

`ytranscript` (`#6525`) returns YouTube transcripts through one tool, including on auto-dubbed videos, with AI speech-to-text for videos without captions, free at **50** units a month. Held on saturation in the transcript class.

`SKV` (`#6526`) answered a keyless `initialize` at `https://skv.network/mcp` with `serverInfo` `skv-memory` at **1.30.0** and returned more than **20** tools, including a per-turn `turn(user_message, draft)` duty, a paged constitution, a shared "cube" library with voting, a court for cube version disputes and an isolated `sandbox_run` with 10 runs a minute. It is memory plus governance, which is a rarer combination than plain memory, and it is held for one pass rather than dropped: the promotion test is whether the verification seal and the court are enforceable or self-reported, and whether `turn` can be driven without first installing a constitution.

`Shipvo` (`#6527`) opens a React Native app in a simulated phone with **18** tools and a hosted endpoint at `https://sim.shipvo.dev/mcp` that answered **HTTP 200** with `serverInfo` `shipvo` **0.0.6**; the tools that open or act need a key. Held as developer mobile testing.

`NexusBro` (`#6528`) is a free keyless website audit at `https://nexusbro.com/api/agents/mcp`, `initialize` **HTTP 200** with `serverInfo` `nexusbro` **1.1.0** and **two** tools, `audit_website` (crawl up to five pages, a 0 to 100 health score, top issues, a fix prompt and a report link) and `audit_checks`. Held on saturation: eight SEO audit entries already here, and this one adds breadth rather than a new question.

`VocaLingo` (`#6530`) summarises and dubs short video, clones voices and translates on-screen text across **15** tools. Held in the saturated media generation class.

## Count

The guide tree held **1,073** server entries before this pass and holds **1,076** after it, across **1,466** files under `hermes/mcp`. Sources: the mcp.so homepage `recentServers` block read directly (**132** parsed cards, newest `2026-11-01T00:15:52Z`), mcpservers.org `/all` through the r.jina.ai reader proxy with `X-Return-Format: html` (**23** unique slugs, counter **18,577**), the chatmcp/mcpso issue window **#6513** to **#6530** read with bodies in eighteen authenticated calls, a keyless `initialize`, `tools/list`, `list_rules` and two rendered `scan_url` calls on `https://checker.lazynext.com/mcp` (**200**, **4** tools, **75** rules, scans of 12.97s and 61.1s), a keyless `initialize`, `tools/list`, `guest_status`, `inventory`, `resolve_audience` and one failed `plan_quote_guest` on `https://app.distribution.tech/api/mcp/guest` (**200**, **6** tools), a keyless `initialize` on `https://api.gwix.ai/mcp` (**401**) and on `/v1/mcp` (**401**), a keyless `initialize`, `tools/list`, `get_data_status` and `get_pay` on `https://api.gwix.ai/mcp/sample` (**200**, **27** tools) with one `job_offer_check` failing at a CloudFront **504**, a keyless `initialize` on `https://skv.network/mcp` (**200**) and on `https://sim.shipvo.dev/mcp` (**200**), a keyless `initialize` and `tools/list` on `https://nexusbro.com/api/agents/mcp` (**200**, **2** tools), a **401** on `https://api.hifrank.ai/mcp`, a **404** on `https://api.gwix.ai` root, and HTTP reads on `gwix.ai`, `gwix.ai/mcp`, `gwix.ai/pricing`, `corridome.com`, `coinvello.com/ai`, `checker.lazynext.com`, `distribution.tech`, `distribution.tech/docs`, `distribution.tech/docs/agents` and `distribution.tech/pricing`, all **200**.
