---
title: "MCP Server Discovery - November 25, 2026 (Night)"
description: "A thirteenth sitemap minted and 869 listings restamped, with three ships from the queue: a CEE fund, UK planning records, a funder directory."
category: "MCP Ecosystem"
last_updated: "2026-11-25"
---

# MCP Server Discovery - November 25, 2026 (Night)

Fired on the **03:00 MST** tick, about sixteen hours after the evening pass stored its baseline and five hours after it finished deploying. The directory did not merely move, it was **re-sharded**: a thirteenth numbered sitemap appeared, every shard now holds exactly **2,000** distinct keys, and **869** listings carry a `lastmod` stamp inside the window. Reading that as 869 new products would be wrong for reasons this pass can prove arithmetically, and all three ships came from the submission queue instead.

## The window, measured

```text
mcpservers.org /sitemap.xml   SEVENTEEN maps named
  static.xml, priority-servers.xml, servers/1..13.xml, skills.xml, remote-mcp-servers.xml
raw <loc>, numbered server maps 1-13   37,806   against 37,599 on the twelve-map basis
  servers/1  ..... 4,129     servers/8  ..... 2,754
  servers/2  ..... 2,513     servers/9  ..... 2,594
  servers/3  ..... 2,953     servers/10 ..... 2,554
  servers/4  ..... 3,195     servers/11 ..... 2,447
  servers/5  ..... 3,270     servers/12 ..... 2,431
  servers/6  ..... 2,876     servers/13 .....   220   (new in this pass)
  servers/7  ..... 5,870     sum 37,806 exact
distinct keys per map                    1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 220
  the 2,000 ceiling is the tell           the shards fill to a cap and the next one opens
priority-servers.xml                     232 raw / 34 keys   (252 raw on the earlier basis)
remote-mcp-servers.xml                    15 raw /  1 key
union, raw                               38,053
union, distinct keys                     24,221   against 23,927 on the earlier basis
lastmod pairs, server maps               34,376
  at or after 2026-11-24T18:00Z          1,390 rows
  collapsing to                          869 distinct keys
  newest stamp anywhere                  2026-11-25T09:06:09Z
```

**A raw rise with a shard count that changed is a re-shard until proven otherwise.** Three measurements say so. Every shard from `servers/6` onward sits at exactly **2,000** distinct keys, which is a cap rather than a coincidence. `servers/13` exists and holds **220**, which is the overflow. And `priority-servers.xml` **fell** from 252 raw entries to 232 while the library grew, which a purge cannot produce on the same day the total rises. The union is **24,221** distinct keys against **23,927**, a net **+294** over sixteen hours, and the honest label for that is growth with a re-shard on top, not 294 arrivals and not 869.

## Why 869 stamps are not 869 products

The stamped cohort was cross-referenced against the catalog: **788 of the 869 slugs** have no guide directory, no catalog heading and no sweep mention. On a normal night that would be a reading of 788 new servers. Here the cohort contains `filesystem`, `sequentialthinking`, `github-mcp-server`, `ynab-mcp-server`, `dbt-mcp` and `firebase-mcp-server`, each of which has been in this catalog or long predates it. **A restamp of the index shows up as a stamp, not an arrival**, and the discriminator is the per-map key ceiling, not the `lastmod` column. The cohort is therefore recorded as a restamp wave with the arrival signal carried by the union delta (**+294**) and the two surfaces that do not depend on the sitemaps.

## The feed

`mcp.so/feed` answered **200 at 160,403 bytes**, **37 anchors** and **30 stamps**, newest `11/25/2026, 08:32 AM` UTC, which is within two hours of the capture. **Seven cards** sit above the 04:00Z cutoff of the previous pass:

| Card | Stamp (UTC) | Class |
| --- | --- | --- |
| unscramblex | 08:32 | word puzzle, consumer |
| voxoria | 07:40 | audio generation |
| vocallab | 07:28 | voice lab |
| kalanos-robotics-dataset-audits | 07:19 | robotics dataset QA, narrow |
| papergarden | 06:05 | writing tool |
| prooftask | 05:45 | delivery acceptance, public tier is 3 tools |
| adrasi | 05:18 | advertising, unnamed surface |

None of the seven shipped: six are consumer or single-purpose tools outside the operator catalog, and `prooftask` was probed and returns a **keyless 3-tool public surface** (`getAgentCapabilities`, `searchPublicSpecifications`, `getPublicSpecification`) with the delivery workflows behind a local adapter and a scoped key. It is held as a discovery-only tier rather than catalogued on three template-browsing tools.

## The queue and one directory slug, which carried all three ships

`#8036` through `#8054`, **nineteen filings** in the window. Two resolved to drivable endpoints from the queue and shipped with guides, and a third came from the sitemap cohort, resolved through the registry and absent from every prior sweep:

- **[BADideas.fund](/hermes/mcp/servers/external/badideas-fund-mcp/)** (registry `fund.badideas/mcp` 1.0.0, `https://badideas.fund/mcp`): keyless `initialize` and a keyless **8-tool** `tools/list`, with three tools driven. `list_portfolio` returned **40 companies** newest first, from Tapaya in Czechia at Apr 2026 to Juo in Poland at Sep 2025, and the headquarters list runs past the CEE line to Sweden, Denmark and the USA. `search_website` returned the fund's own medians for January to September 2026: **€380,000 at pre-seed, €2 million at seed, €7.1 million at Series A**, with Estonia at **€2.8 million** and Lithuania at **€1.9 million** at seed. `ask_question` answered a real founder question with numbered sources and an honest negative: first check **€200K to €1.5M**, one deal lead per investment, and in Latvia **4 rounds joined and none led** since January 2025. The same answers give the runway shift (**18 months in 2026 against 12 in 2025**), the use of funds (**34% product, 30% sales, 17% people**) and the finding that **86%** of the fund's founder calls raised finding customers.
- **[PlanningLedger](/hermes/mcp/servers/external/planningledger-mcp/)** (registry `com.planningledger/planningledger` **1.0.2**, `https://mcp.planningledger.com/mcp`): the **discovery-open, execution-gated** tier measured in four calls. Keyless `initialize` **200** and a keyless **14-tool** `tools/list`, then every `tools/call` returns **401** with `WWW-Authenticate: Bearer resource_metadata="https://mcp.planningledger.com/.well-known/oauth-protected-resource/mcp"` and a plain JSON body naming the sign-in. The protected-resource document answers **200** at both the bare and the suffixed route with **one scope, `read`**, and the RFC 8414 document on the same host is complete: dynamic registration, `authorization_code` plus `refresh_token`, PKCE **S256** only, response mode `query`, and `authorization_response_iss_parameter_supported`. The vendor states the allowance as **20 document searches and 100 quotes a day** per person, **20 calls a minute and 300 a day**, reset at midnight UK time, free. Fourteen read-only tools cover applications, their documents, decision counts, appeals from PINS, PEDW, DPEA and PAC, and Local Plan policies.
- **[Investor Shelf](/hermes/mcp/servers/external/investorshelf-mcp/)** (registry `com.investorshelf/investor-shelf` 1.0.0, `https://investorshelf.com/api/mcp`): keyless `initialize` **200** and then **`-32001`** on `tools/list`, *a valid API key of an active Pro subscription is required*, returned at **HTTP 200**, so a client that reports connection success is reporting reachability and not access. **Three well-known routes answer 404 with 25 KB of application HTML**, which makes this the static-key tier with no discovery document at all. The vendor publishes the **8 tools** on its own MCP page and the library size: **5,853 funders, 27,013 funding rounds, 6,289 reports, 86,492 records including 55,534 SEC filings**, contacts for **4,801 funders**, MCP on Pro at **$29 a month or $290 a year**.

## Held, with the class named

Nineteen filings minus three ships leaves sixteen, and the pass spent its probe budget on the three above rather than on partial reads:

| Held | Reason |
| --- | --- |
| `mepmail`, `draftlab`, `privatools`, `logtriage`, `nemus`, `agy-memory`, `CollieTax`, `HostMT5`, `Business-Wrap` | filed inside the last three hours of the window with **no registry record yet**; no endpoint to drive |
| `NJ-Burrito` Business-Wrap, QA-Wrap and Profile-Wrap | one publisher, three wrappers; the fleet is dispositioned together once one endpoint proves a surface |
| `mambalabsdev` five (SEC filings search, Keepa price history, Telegram channels, YouTube keywords, Wayback snapshots) | repeat publisher already held as a class in the Nov 24 night pass; the SEC and Keepa items are the two that deserve a probe when the class is next opened |
| `financetoolkit` (`io.github.JerBouma/financetoolkit` 2.3.5) | **401** on initialize naming an FMP key or OAuth; the package ships an MCP entry point, so the next pass drives it locally over stdio rather than stopping at the gate |
| `taxtrace` (`io.github.vinayvobbili/taxtrace` 0.2.1) | local stdio package, masked read-only tax workspace; install-and-drive next pass |
| `formationlane` / `llc-fees` 1.1.1 | same vendor as the **Formation Lane** entry recorded unreachable from this egress (TLS `ACCESS_DENIED`); retry class, not a new discovery |
| `cernion-energy-tools`, `quant-b2b-intel-hub`, `settlegrid` | registry-resolved remotes not reached this pass; the Apify-backed hub and the discovery-only SettleGrid entry are low priority on the operator lane |

## Listings, re-measured

Nothing changed on the surfaces that matter to us: `mcpservers.org` still carries `corpusiq-io` in its server maps, `mcp.so` still answers its `/servers/` route, and the GitHub and Smithery records stand as recorded in `GEO_CHECKLIST`. No listing work was attempted in this pass.

## What the pass says about the platform

A directory that re-shards without restating its count will make every naive diff lie in both directions: the raw count rose by 207 while the shard count rose by one, the priority map fell by 20 while the library grew by 294 keys, and 869 stamps named mostly servers that have been there for months. The two surfaces that cannot be re-sharded, the feed and the submission queue, carried all three ships. The pattern to keep: **count distinct keys per map before calling a rise an arrival**, and work the queue first when the sitemaps are reorganizing.
