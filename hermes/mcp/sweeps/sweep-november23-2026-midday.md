---
title: "MCP Server Discovery - November 23, 2026 (Midday)"
description: "A flat directory and a moving queue: compliance work at the OAuth gate, WhatsApp leads tied to the ad, and four free fraud checks."
category: "MCP Ecosystem"
last_updated: "2026-11-23"
---

# MCP Server Discovery - November 23, 2026 (Midday)

Fired on the **10:00 MST** tick, **5.5 hours** after the night pass stored its baseline at **11:31Z** and shipped Avanciq, Climatch, MOA and Strata through PR #485. The directory did not move: every reading on the canonical came back flat, and no `lastmod` stamp anywhere on the surface is newer than **10:27Z**. All three products came from the push surfaces - a feed card and two queue arrivals - and all three are about money an operator cannot currently see: certification work, the ad behind a WhatsApp lead, and whether a link is already known bad.

## The window, measured

```text
Cutoff (baseline written)      2026-11-23T11:31:16Z
Capture                        2026-11-23T17:00:40Z
Elapsed                        5.5 hours
Sitemap index                  200, sixteen maps (static, priority, servers/1-12, skills, remote)
Twelve numbered server maps    37,519 raw <loc> entries
Per-map block                  4,156 / 2,526 / 2,941 / 3,231 / 3,342 / 2,939
                               5,857 / 2,739 / 2,617 / 2,616 / 2,515 / 2,040
priority-servers.xml           251 raw / 34 keys
remote-mcp-servers.xml         15 raw / 15 keys
Union raw                      37,785 (12 maps + priority + remote)
Twelve-map distinct keys       23,612
Union distinct keys            23,661 raw, 23,647 after %23 and locale normalisation
Like-for-like union diff       +1 addition, 0 removals
lastmod pairs (server maps)    34,200 rows, newest stamp 2026-11-23T10:27:37Z
lastmod at or after 11:31Z     0 rows
```

The one addition is not a product. Normalising both sides leaves **one** new key, `https://mcpservers.org/remote-mcp-servers/clockwise`, which is a route form for a slug already in the index. The raw count also moved in a direction that reads wrongly on its own: **37,519** against **37,555** at the night capture, because `servers/3` fell **24**, `servers/12` fell **21**, `servers/11` fell **20** and `servers/10` fell **3**, while `servers/6` held its count and six maps rose (by 7, 6, 5, 7, 5 and 3), with `servers/7` down a single entry. A **36-entry raw fall with a two-key rise** is a re-shard, and the **218** `lastmod` rows in the 07:04Z to 10:27Z range collapse to **84** keys, of which nine are stamped **fifteen times each inside one second** (`supabase-mcp-server`, `browserstack/mcp-server`, `keboola/keboola-mcp-server`, `windsormcp`, `mozilla/firefox-devtools-mcp`, `longbridge/longbridge-mcp`, `wavix/wavix-mcp-server`, `azure-mcp-server`, `last9/last9-mcp-server`). Those rows belong to the night pass's own window, not this one.

A twelve-map capture diffed against the stored union would have invented **34 removals** - every one a `priority-servers.xml` slug printed in `/servers/` form. Recorded, not counted.

## Feed

`mcp.so/feed` answered **200** at **159,050** bytes with **34** server anchors and **30** `M/D/YYYY, HH:MM AM/PM` stamps. Five cards sit above the cutoff:

| Card | Stamp (UTC) | Disposition |
| --- | --- | --- |
| `scrumpy` | 16:16 | held, project boards class |
| `koop` | 15:52 | **shipped** |
| `cartai` | 15:34 | held, agentic checkout class |
| `onlydns-mcp` | 15:13 | held, infrastructure provisioning |
| `patchwell` | 12:45 | prior catalogue, November 7 |

## Queue

**#7886 to #7911**, twenty-six arrivals, bodies read in one authenticated call. Three were shipped or driven; twenty-three held with the class or gate named.

## Shipped

### Koop - security compliance at the OAuth gate

`https://mcp.koop.ai/client/mcp` answers **401** with an in-band JSON-RPC error that names both credential paths and points at Claude Code's `/mcp` flow. The protected-resource document is complete on both the bare and the resource-relative route, with three scopes: **koop:read**, **koop:write** and a separate **koop:draft**. The RFC 8414 document carries PKCE **S256**, dynamic registration at `/register`, a revocation endpoint, `token_endpoint_auth_methods_supported: none` and `authorization_response_iss_parameter_supported: true`.

The frameworks read off the vendor page: SOC 2, ISO 27001, ISO 42001, CMMC L1 and L2, NIST SP 800-171, DFARS 252.204-7012 and ISO 9001, priced **from $299 a month**. The tool list is **not readable without an account**, and the guide says so rather than listing tools nobody saw. First of class here: the catalog had legal compliance and MCP audit proxies, nothing that runs certification work.

### wapi.kz - WhatsApp leads priced back to the ad

**#7910**. `https://wapi.kz/api/mcp` serves **28** tools keyless at `tools/list` (server **wapi.kz 0.5.0**, protocol 2025-06-18) and refuses every `tools/call` in band with a Russian message naming the cabinet URL for the key. All 28 descriptions are in Russian. The registry record `kz.wapi/whatsapp` reads **0.5.1** against the endpoint's 0.5.0, recorded as drift.

The model is not the Cloud API: a number is attached as a **linked device** (pairing code `ABCD-EFGH`, four codes per ten minutes, or a QR that lives ~20 seconds). `get_analytics` rolls ad spend into leads into sales, grouped by campaign, ad set, ad, source, link, day or device; `list_leads` carries `ctwa` joins with `ad_id`, `adset_id` and `campaign_id`, link joins with utm, fbclid and gclid, and organic; `get_link_stats` returns conversion percent, revenue, median minutes from click to first message and a bot count; and `match_method` publishes its own weakest link as `time_window` with a **15-minute** window. Six Meta tools reach the ad account, and `set_ad_budget` carries the vendor's own warning that a budget change spends the client's money immediately. **330 KZT per connected number per day**, first day charged on add, with `add_number` refusing to change anything without `confirm=true`.

Second WhatsApp entry after Meta's Business MCP, and a different slice: attribution and tenge billing on a session model rather than the Cloud API contract.

### RelayShield Scam Checks - four keyless fraud checks

**#7908**. Four tools at `https://relayshieldadmin-relayshield-free-mcp.hf.space/mcp`, all driven keyless: `check_link`, `check_email`, `check_breach`, `check_wallet`. Every clean answer is `[UNKNOWN]` or a `LOW` risk with the qualifier that the verdict is unknown rather than safe, which is the behaviour worth cataloguing.

Measured, including the defects:

- `check_link` on our own domain prints `IOC corpus=False | threat feeds=False | domain age=Noned` - the null template appended a `d`, so an advertised signal is unreadable.
- The batch path disagrees with itself: two URLs returned "Checked 1 link(s): 0 flagged, 1 incomplete", with the lookalike printed as `[UNKNOWN]` and then again as `[NOT CHECKED - retry]`, while `example.com` was correctly skipped as an IANA-reserved name.
- `check_email` on a classic invoice-fraud pair of subject and body scored **Risk low, Score 0**, because it scores the fields supplied and a bare body is not a check. That is the single most useful fact in the guide and the vendor's own note says it.
- `check_breach` returned **275** breaches for `test@example.com` and **0** for a unique address on our own domain: a test address with a documented history, not a wildcard.
- Bad input is refused in band with the vendor's 400 body naming the rule.

The publisher runs three servers in the registry: the free one (**1.30.1**), an MCP proxy firewall (**0.3.0**, 50 free calls then **$49 a month**) and a subscription server (**0.2.11**). Only the free door is measured.

## Held, with the class or gate named

Twenty-three arrivals, each measured or class-named rather than dropped silently:

- **CartAI** (**feed**): agentic checkout infrastructure, npm `cartai-mcp-server`. First of the agentic-commerce class if it stands up; held for a local install this pass did not reach.
- **Scrumpy** (**feed**): scrum and kanban boards, remote MCP, `401 Unauthenticated` at initialize with no protected-resource document - project boards are carried by taskade, taskfolk and sprintcheckout.
- **OnlyDNS** (**feed**): Anycast DNS provisioning for agents, local repository package, infrastructure class.
- **SentriSend** (**#7897**): email validation plus sending with Ed25519-signed receipts; the email-verification class is already saturated by the MailTester trio, though the signed receipt is a new idea worth a second look.
- **AgentSDR** (**#7886**): sales reply-queue work per instance, OAuth as its own authorization server; nothing publicly probed without an instance address.
- **FlowFeed** (**#7892**): macro and market news, **$9 a month** key; the macro-data class is carried by Monitly and FXMacroData.
- **Agent Meets Agent** (**#7891**): an agent directory behind a Supabase function host, keyless initialize and sign-up tools only.
- **DoLoop** (**#7890**) and **Okokumo** (**#7889**): one author filing twice; tasks and project management, and monitoring and DevOps respectively - both tools/call gated behind OAuth or a key.
- **Oxynet** (**#7887**): closed-source, OAuth 2.1 with DCR plus an API key, documented in `llms.txt`.
- **HenryCrawl** (**#7888**): e-commerce data at **$19 a month for 3,000 credits**, one credit per result with a 20-credit minimum per Amazon or eBay call; tenant of the standing transport-and-pricing ruling.
- **Scrapemint** (**#7902** to **#7904**): three Apify-hosted fronts over the same publisher's actor set, one fleet.
- **Tintloom** (**#7900**), **Rainfrog** (**#7899**), **Musikalis** (**#7894**), **One Design** (**#7893**): media generation, image editing, music and local design tooling - all carried classes.
- **Edgegap** (**#7909**): not a new product, a listing correction request for an existing mcp.so entry (repository renamed from `edgegap-mcp` to `llm-mcp-server`).
- **Agent402 pay-mcp** (**#7898**) and **HelmSwap** (**#7901**): x402 payment tooling and unsigned swap quotes, both on the crypto-wallet class.
- **Solana Rent and Rug Shield** (**#7907**): token safety plus rent recovery, crypto class.
- **Agent Registrar** (**#7905**): OAuth 2.1 identity for agents, DCR and client metadata documents - a real surface, held on the identity class already held by Agent Warden and AgenticGeoMate's discovery tier.
- **OrchStep** (**#7896**): local stdio YAML workflow runner, developer tooling.
- **Palace** (**#7911**): local-first agent memory in Rust, memory class.
- **doubao-remote** (**#7895**): drives a local desktop app over Chromium DevTools, macOS-only, not a remote service.
- **#7906**: not a submission - a pull request closing issue #1 with a settlement address attached, recorded and ignored.

## Listing status, re-measured

| Surface | Status | Evidence |
| --- | --- | --- |
| mcpservers.org | **listed** | `corpusiq-io` in `servers/5.xml` of this pass's fresh capture, beside our own `/servers/corpusiq/corpusiq-docs` mirror |
| mcp.so | **not listed** | four slugs 404: `corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq` |
| Glama | **listed** | `200` at `/mcp/connectors/io.corpusiq/multi-source-mcp`, title *CorpusIQ - MCP Connector* |
| Smithery | **listed in the registry API, page route unresolved** | the registry API returns the Cprusiq record with `remote: true`, deployment `corpusiq.run.tools` and our MCP Apps resources; the public page 404s for namespaced servers generally - three other namespaced records were tested, one renders and two 404 - so the 404 is a route condition and not a delisting |
| Anthropic connector directory | **not listed** | `scripts/anthropic_directory_watch.py` exit 0, 1,207 pages scanned, 0 hits |

## What this window says about the directory

A 5.5-hour window in which the canonical did not move at all, and all three products arrived through the queue and the feed. That is the fourth consecutive pass where the sitemap was the quieter surface. The useful discipline is unchanged: capture, diff on one basis, print the per-map block, and treat the push surfaces as where the products actually appear.
