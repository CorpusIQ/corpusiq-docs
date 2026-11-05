---
title: "MCP Server Discovery - November 4, 2026 (Evening)"
description: "Evening pass: a 171-entry directory wave that is an ingestion echo, two driven entries (ProveCart, lookfirst), and one index held after measurement."
last_updated: 2026-11-04
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november4-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 4, 2026 (Evening)

## Summary

This pass fired on the **21:00 MST** tick, eleven hours after the **10:00 MST midday** read. The feeds were quiet and the directory was not: mcpservers.org moved from **19,344** to **19,515**, **171** entries, and its newest page shared no slug with the thirty the midday pass dispositioned. mcp.so produced **26** server objects with only **4** cards above the midday stamp, and the submission window carried **17** items, one of them an MCP client rather than a server.

Two entries were catalogued and both were driven rather than quoted. **ProveCart** is the first surface in this catalogue that compares an order an agent built against the customer's own structured instruction and returns a signed verdict before the payment. **lookfirst** is the first that stops a specific write until a named human approves the exact arguments, verifies the result by read-back, masks account data before the model sees it, and keeps a hash-chained log you can verify.

The most useful thing this pass learned is about crossref, not about servers. **A 171-entry wave read as 113 new slugs and as a handful of new products.** The slug form and the product-name form disagree, and only running both tells you that the directory is ingesting a backlog rather than the ecosystem producing a wave.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **45** issues fetched, **17** in this window `#6746` to `#6762`; `#6761 AGNT` is a client, so **16** server arrivals |
| mcpservers.org `/all` | pages 1 to 4 through the reader proxy, page 1 read twice | **19,515** on both reads; **120** slugs parsed; **113** unledgered on the first slug pass |
| mcp.so `/feed` | direct fetch with a browser UA, `createdAt` parsed | **26** server objects, newest `2026-11-04T23:13:21Z` (Actora MCP), **4** cards above the midday stamp |
| Endpoint probes | keyless `initialize` with a browser UA | ProveCart **200** (`provecart` **1.0.2**), three `antevo.ch` paths **405** |
| Local install | `pip install git+https://github.com/Aethelgard-Systems/lookfirst`, demo run twice | `lookfirst 0.2.1`, both runs exit **0** |

## The wave, and why it is not 113 discoveries

mcpservers.org counters had moved **+171** in eleven hours while the mcp.so feed moved by four cards. That alone says the movement is the directory's own ingestion rather than new publishing, and the slugs confirm it in three cohorts:

1. **Direct matches to the submission window and the one before it.** `1toolring-com-install`, `transformpipe-com-agents`, `scrape-ly-docs-mcp`, `mysouschef/sous-chef-mcp`, `www-pokeinvest-io-data-api`, `api-provecart-com-mcp` and their siblings are named submissions from `#6719` to `#6758`.
2. **Cohorts a prior pass already dispositioned under product name.** The `-docs-mcp` documentation fleet (Cartrelay, Hirelabs, Ziva.sh, Teddit.io, Echoly, Skael, Webclaw, Recl, Rainbrand), the `theluckystrike` calculator four (CPI inflation, IRS mileage, silver per gram, river level), the `antevo.ch` four, and the `tidybytetools` trio were all named in the November 4 night sweep's cohort list. Their slugs were never ledgered, so a slug-only crossref calls them new.
3. **Genuinely new listings whose class is already carried.** The rest: analytics, uptime, workspace memory, media generation, scraping, document extraction, agent email, collectibles, travel and one pixel wall.

The lesson is recorded because it will recur: **crossref the product name and the slug, and read the context of every hit.** The name form disposed roughly forty items that the slug form called new, and the direction of the error is always the expensive one, a re-catalogue of something already held.

## Catalogued

### ProveCart MCP - the cart is checked against the instruction before the money moves

Remote Streamable HTTP at `https://api.provecart.com/mcp`. A keyless `initialize` answered **200** as `provecart` **1.0.2** with all **10** tools listed. The evidence tier is stated rather than implied: `provecart_scoreboard` and `provecart_certification_info` were called live and returned real payloads, and the three check tools refused with a single sentence naming what they need, so the check payload is schema-read and not measured.

```
This tool requires an integrator API key: send it in the X-API-Key header
of the MCP request. Contact ProveCart (hello@provecart.com) for a key.
```

Three check tools, one shape. `provecart_check_order`, `provecart_check_booking` and `provecart_check_reservation` take the customer's **mandate** (or a `mandate_id`) plus what the agent assembled, and answer **MATCH**, **REVIEW** or **BLOCK**. A non-MATCH answer carries the Agent Correction Format: a `corrections` array of `dimension`, `action`, `expected`, `actual` and `reason`, a retry budget, and a sealed evidence pointer, so the agent fixes the named difference instead of guessing. The compared dimensions are the same seven on every check - item, name, date, time, party size, terms, price - with category rules on top.

The mandate is what separates this from a prompt. The order mandate is **18** structured fields including `max_total_price`, `merchant_allowlist`, `merchant_blocklist`, `max_quantity`, `variant_constraints`, `price_basis`, `expires_at` and a `period_budget` with its own window. The booking mandate is **26**, including `airport_substitution`, `date_flex_days`, `fare_terms`, `max_connections`, `min_connection_minutes`, `max_layover_minutes` and `allow_airport_change_connection`. The reservation mandate is **17**, including `time_tolerance_minutes`, `party_size_max`, `max_deposit` and `cancellation`. The cart, booking and reservation objects carry `previous_record_id` and `cart_changed`, so a resubmission is traceable to the check that rejected the earlier attempt.

The certification half is public and was measured. Sign-up needs only an `agent_name` and returns an `agent_id` and a scoped key; the live exam gives the agent customer instructions and real shelves and grades its own decisions. **80** or above certifies, a pass is CURRENT for **90 days** and then lapses, status is computed from the sealed record at read time, renewal is a newly generated exam, cohorts are never reissued, and a pass yields an Open Badges 3.0 / W3C Verifiable Credential under `did:web:api.provecart.com`. The scoreboard read live: two agents at **100.0** over **29** checks with certification CURRENT to **2027-02-02**, one external and one house, and two audit probes at **13.8** and **11.1** with no certification. The `origin` field separates external, house and audit runs, which is the difference between a scoreboard and a marketing page.

Limits, stated: it never holds or moves money; a verdict gates a payment only where the integrator's code calls the check first and honours the answer, and nothing in the protocol enforces that; the AI layer cannot overturn a block and its behavioural flags never change a verdict; business onboarding is a free **90-day** design-partner pilot with a small number of slots rather than a published price; the badge is proof of practice and never a gate; and `provecart.com` answers **401** to a plain reader-proxy fetch so the marketing pages were read directly with a browser user agent.

### lookfirst MCP - approval, read-back and a chain you can verify

A local stdio MCP proxy, Apache-2.0 at `github.com/Aethelgard-Systems/lookfirst`, installed here from the repository and reporting `lookfirst 0.2.1` against a README that still says 0.2.0 pre-1.0. The offline demo was run twice.

The approval run returned:

```
{"status": "executed", "id": "tw-30bbf0da56147705", "approved_by": "elicitation:mcp",
 "readback": "ok", "readback_detail": "read-back matches", "blocked": false}
```

and the fake bank balance moved **1,250.00 to 1,129.50 EUR** for a **120.50 EUR** transfer. The denial run returned `"status": "denied"` naming the failed channel, with the balance untouched. Both runs exited **0**.

Five behaviours earn the guide. The decision table fails closed: `readOnlyHint` allows, a `destructiveHint`, an unannotated write and an unknown tool all confirm, an explicit rule beats the annotation, and `deny` never executes. The approval is bound to the arguments: a webhook answer must carry the per-call HMAC token and echo the preview's `args_sha256` or it returns **403**, the web page binds its buttons the same way, and every channel shares one timeout where **a timeout is a denial**. The write is verified by **read-back** against `$args` and `$result` placeholders and reported `ok`, `unklar` or `fehlgeschlagen` in `structuredContent.lookfirst`, so a write is never reported as done on its own word. The audit log is an **Ed25519 hash chain**: `verify-log` walked the run to **OK, 20 signed and chained entries**, the demo then rewrote the decision entry, and the same command returned **TAMPERED, line 6, hash mismatch**. The result is **masked before the model sees it**: the agent received `[[IBAN_c30e2f3c...]]` and `[[NAME_5f082d93...]]`, passing the placeholder back works because the gate resolves it internally, and an invented one is refused with `Denied: unknown or expired placeholder`.

The limits are the vendor's own, and they are unusually specific: pre-1.0 with no field record and **0** stars; an autonomous client that auto-answers elicitation approves itself unless `confirm.elicitation` is off **and** the page is isolated at the network level, where a separate OS user is not enough because every local user reaches loopback; the web page has no login and is meant for `127.0.0.1`; an HTTP bearer token is authentication rather than encryption; Windows is untested; and the mask is a deterministic pattern filter that misses a split IBAN, zero-width text, a Base64-only secret and keys such as `db_password`, which is pinned as a known gap. The documented log weakness is end-truncation plus a deleted `.head` sidecar, closed by an external `--trusted-head` checkpoint.

## Held, with the measurement

| Candidate | Measurement | Ruling |
| --- | --- | --- |
| `xusteve/mailers-scan-api` | one keyless `scan_domain` at `mcp.mailers.email/mcp`: score, `maxScore` **80**, grade, MX, SPF, DKIM, DMARC, rDNS, domain age; **60**/hour per IP, **24**-hour cache, DNSBL excluded from the public API | held on class: [how.is MCP](/hermes/mcp/servers/external/how-is-mcp/) runs SPF, DKIM, DMARC and blocklists among **17** checks, [Mamba](/hermes/mcp/servers/external/mamba-outbound-infrastructure-fingerprint/) returns the same fields beside the outbound stack, Leadgen MCP carries the Romanian version |
| Antevo Tremor Watch | **35** of **176** volatility and equity pairs broken against a normal Friday's **9**, **3.1×**, the **184th** most unsettled of **1,348** Fridays since 2001, Feb 2020 **22×**, Oct 2008 **14×**, **697** pairs tracked | held: portfolio-specific risk is [PairBook](/hermes/mcp/servers/external/pairbook-mcp/) (Euler contributions, ETF overlap) and openInvest (VaR, tail risk); this is the vendor's weekly breadth index. A per-portfolio exposure call would reverse the ruling |
| Antevo Trademark | company, domain and trademark checks across **50+** registers with opposition windows, no account | held: [Goalie](/hermes/mcp/servers/external/goalie-trademark-search-mcp/) searches **14M+** USPTO records, [IP Defender](/hermes/mcp/servers/external/ipdefender-mcp/) monitors filings across **40+** countries |
| Antevo Wealth, The 07:00 Brief | OAuth household holdings that never trades; a pre-market read | held on the wealth and macro classes, dispositioned together with the fleet under the single-author rule |
| `1toolring-com-install` | pay-per-call search, SEO, maps, price and FX data on a prepaid balance | held on the data-aggregator class |
| `workbook-tools-mcp` | XLSX formula inspection and what-if comparison | held: the spreadsheet-workbook slice is carried by the SheetsFinance surfaces |
| `uptrack-app/uptrack-mcp`, `invisit-dev`, `veduis/pdf-a11y-audit` | uptime, cookieless analytics, PDF accessibility audit | held on [Cronitor](/hermes/mcp/servers/external/cronitor-mcp/) and Runheed, the analytics class, and `kinti/a11y-toolkit` |
| `actora-mcp`, `arsen-mcp`, `circles-personal-whatsapp-for-ai-agents`, `airport-pickups-london` | the four feed cards above the midday stamp | held as one vertical each: ERC-8004 agent manifests, phishing simulation, personal WhatsApp reading, London transfers |

Held without a probe because the class is settled: `withnym-com`, `agentlair-dev` and `inboxfamily-...` on agent email; `thread-page-...`, `worktable/worktable-dev` and `withnative/native` on workspace and memory engines; `ocr-ai-com` and `transformpipe-com-agents` on document extraction; `scrape-ly-docs-mcp`, `brainfish-ai/webcrawl-anything`, `fetchlayer-dev-mcp` and `scrappy-gg-integrations-mcp` on scraping; `animatecaptions-com-developers`, `www-gridbulk-com-api`, `chartpng/chartpng`, `imgtoimageai-com` and `www-versely-studio-mcp` on media; `kennmarq-com-docs-guides-ai-coding-agents` on C2PA marking; and outside operator scope `cellionaire-com`, `superhero-pw`, `soundiiz-com`, `pocketplanner-fr`, `blindspotjournal-com-mcp`, `gecici-email`, `thechesscoach-netlify-app-docs-html`, `testagent-space-llms-txt`, `tourscanner-org/tourscanner-ai` and `thecharterdesk-com-mcp`.

## Counts

Guide tree **1,099** directories before this pass, **1,101** after. Entries counting single-file guides **1,243** before, **1,245** after. mcp.so **26** server objects with the newest at `2026-11-04T23:13:21Z`. mcpservers.org `/all` at **19,515** on both reads, **+171** since the midday **19,344**. Submission window `#6746` to `#6762`, **17** items, **16** server arrivals. Seven endpoint probes and one local install.
