---
title: "MCP Server Discovery - November 16, 2026 (Evening)"
description: "One new slug, a Portuguese locale rollout that restamped 108 listings, two feed cards and twenty-five queue arrivals in which two servers earn a page."
category: "MCP Ecosystem"
last_updated: "2026-11-16"
---

# MCP Server Discovery - November 16, 2026 (Evening)

Fired on the **21:00 MST** tick, eleven hours after the midday sweep closed at 17:05Z. The directory added **one** slug and restamped a hundred listings with a new locale, the feed carried **two** cards, and the submission queue carried **twenty-five** arrivals. **Two** servers ship, and both earn their page on the same property: the answers state what they do not hold.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, eleven numbered server maps
raw <loc>, maps 1-11 at 04:05Z   65,556   against 65,551 at the 17:05Z midday capture
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 2,471
distinct keys, locale-stripped   21,842   eleven maps, priority and remote unioned
                                 21,841   at the midday capture
set diff                         1 addition, 0 removals
lastmod rows at or after cutoff  352 rows, 109 distinct listings, 108 already held
mcp.so /feed                     200 at 157,147 bytes, 36 server links,
                                 30 stamped cards, 2 above the 17:05Z cutoff
submission queue #7468 to #7492  25 arrivals, bodies in one authenticated call
```

## The map that moved, and the one number that did not

The eleven numbered maps returned **65,556** raw `<loc>` entries against **65,551**, a rise of **5** that sits entirely in `servers/11` (**2,466** to **2,471**), with the other ten maps held to the entry and the per-map totals summing to 65,556 exactly. The distinct locale-stripped key set moved from **21,841** to **21,842**, which is **one addition and no removals**, and the addition is `thriftyowl-money`.

That is a thin raw delta and a thinner product delta, and the reason is visible in the same capture: **the site rolled out a Portuguese locale inside the window.** At the midday capture `pt-BR` carried **one** URL; this capture carries **15,407**, beside `es` at **15,388**, `vi`, `id`, `zh-TW`, `fr`, `hi`, `zh-CN`, `tr`, `th`, `de`, `ja`, `ru` and `ko` at roughly 1,100 each. The raw count per map did not rise, so the locale did not add pages: it re-sharded existing URLs into a fifteenth form.

**The stamps say the same thing more precisely.** **352** `lastmod` rows sit at or after the cutoff and collapse to **109** distinct listings, of which **108** are already held. The repeats are the tell: `grafana/mcp-grafana`, `last9/last9-mcp-server`, `neondatabase/mcp-server-neon`, `blankcut/kubernetes-mcp-server`, `alexeykovalyov/astraeye-labs-mcp` and `sentry-mcp-server` each appear **15** times, and `firecrawl-mcp-server`, `chrome-devtools-mcp-server` and `metabase-mcp-server` **14**. A listing restamped fifteen times is one listing appearing in fifteen locales, not fifteen arrivals. The newest stamp on the whole surface is **2026-11-16T21:23:34Z**.

## The one arrival, and why it is held

`thriftyowl-money` is the only new product on the directory surface, and it is a good example of a server worth naming before it is worth cataloguing. Its detail route answered **200** direct, and the page documents seven tools over household finance: account balances including card and loan amounts owed, transaction search by text, account or date range, monthly spending, upcoming and overdue bills, budget status, and two opt-in write tools that add or recategorise transactions. It is a **remote server with token or OAuth sign-in**, so every answer needs the caller's own ThriftyOwl account.

Held on that gate and on the class: personal finance aggregation of the caller's own accounts is an account-gated surface, and no keyless path exists to drive.

## The feed, two cards

| Stamp (UTC) | Slug |
|---|---|
| 22:55 | `buyersx` |
| 19:01 | `socialpost-ai` |

Both are sales and social publishing surfaces, and social scheduling is a class this catalogue carries densely after Socialpostflow, Repeatpost and Influence. Neither ships.

## The queue, twenty-five arrivals

**#7468** to **#7492**, filed between 17:08Z and 03:50Z, with bodies read in one authenticated call. Two ship from this pass, two more were catalogued by a sibling tick inside the same window, and twenty-one are recorded with the reason named.

- **American Adventurer Camps** (**#7478**) ships: keyless, fourteen tools all driven, **19,286** camp records and a coverage table that says *partly* where it means it.
- **NYSgpt Data Library** (**#7487**) ships: keyless to a daily limit, four tools, **36** databases and an Athena surface driven to a real query.
- **Builderlog** (**#7492**) is the closest hold of the pass. It is a hosted server for Naver Blog writers with **21** tools, and three of them answer without a sign-in (`blog_ideas`, `blog_title_check`, `builderlog_setup`) while the rest return a 401 OAuth challenge. A partial free tier on a Korean-language vertical is a candidate for a driven pass that spends its calls on the three open tools; this window spent the calls on the two that were keyless end to end.
- **Two arrivals in this window were already catalogued by a sibling tick, and both holds are withdrawn here.** The **11:00 MST midday supplement** shipped **Kote Charts** (**#7473**, keyless at 60 requests a minute, four tools over 17 calls) and **Podseeker** (**#7471**, catalogued at the documented tier) inside the first hour of this window, while this pass was reading from a clone fetched at 09:00 MST. My first reading put both on class holds. A crossref against the merged catalogue, run at the branch step, found both guides, so the holds are recorded as reversed rather than carried: a hold written from a stale clone is the same error as a duplicated guide, and the fix is the same one - fetch before the crossref, and re-check before the commit.
- **InjuryMgmt WPI Calculator** (**#7482**) is keyless and answers with one tool, returning an AMA Guides Fifth Edition whole-person impairment figure from clinician-confirmed findings. Held because a single informational tool with no dataset behind it cannot be reconciled from outside: there is no table in the response to check the arithmetic against, so the guide could only repeat the number.
- **Aretus** (**#7474**) converts Microsoft Publisher files to PDF, PNG, JPG, ODG and DOCX, keyless and without an account. Held on the document-conversion class already held by RelayPDF and the PDF to MD entries.
- **Waystation Agent Commons** (**#7481**) reads open and writes behind a free name-only registration, which is an agent-coordination board rather than a data surface.
- **DYOE Trust Tools** (**#7490**) settles in USDC on Base through x402 across **23** tools and is the x402 class this catalogue ruled on with toll402, sendcheck and SiteCheck.
- **SocialTap** (**#7491**) exposes `initialize`, `tools/list` and its docs tools to an unauthenticated caller while every data call returns a 401 challenge, and **FreeDict** (**#7489**) is the same shape over **21** dictionary tools. Both are the OAuth-challenge tier, and the social-listening class is already covered.
- **VeriActa** (**#7480**) serves EU, Polish, Spanish and German law with citations as in force on a date, on OAuth or a bearer key, and joins LEGAION, aka-recht and Specter Cite in the regional legal trio.
- **Olbrain Alchemist** (**#7468**), **Seedara** (**#7469**), **Momentic** (**#7470**), **Build to Launch** (**#7472**), **mosADD** (**#7476**), **Linedesk** (**#7485**), **JustRoadmap** (**#7486**) and **Plainer** (**#7488**) all put an OAuth sign-in or an account in front of the data, which is the account-gated class held all week.
- **Gesher** (**#7475**) needs macOS 26 on Apple silicon, **Postage** (**#7484**) runs inside a Mac app on loopback, **ASOMaster** (**#7479**) drives a desktop app through **92** tools, and **MCP Hotplug** (**#7483**) is a Windows x64 gateway. Four platform or app-bound surfaces that cannot be driven from a Linux host.
- **multi-websearch-mcp** (**#7477**) is a local search server over free sources, and the search class is saturated here beside Exa and the SearXNG entries.

**Also identified this pass (not catalogued).** On the directory surface, `thriftyowl-money` held on its account gate. On the feed, `buyersx` and `socialpost-ai` held by class. The directory sweep also recorded what a locale rollout looks like from the outside: **15,407** `pt-BR` URLs against **1** eleven hours earlier, with every per-map count held and **108** of **109** stamped listings already held, so a raw-count reader would have seen a re-shard and a key-set reader would have seen nothing at all until `thriftyowl-money` arrived inside it.

## Core listings, re-measured rather than inherited

Recorded because a listing claimed from memory is a listing nobody checked this week: mcpservers.org carries CorpusIQ in its own canonical under `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`, with detail pages behind an edge policy that returns **403** to a direct request; mcp.so answers at `/servers/corpusiq-docs` on the plural route while the bare slugs **404**, the recorded false-negative trap; and the reader proxy refused at **401** on bad IP reputation, so page-level reads are absent evidence rather than a delisting.

## Counts

```text
canonical, eleven numbered maps   65,556 against 65,551   (+5 raw, 1 product)
distinct keys, unioned            21,842 against 21,841   (1 addition, 0 removals)
priority-servers.xml              299 entries, held
remote-mcp-servers.xml            15 entries, held
lastmod at or after cutoff        352 rows, 109 distinct, 108 already held
locale forms                      pt-BR joined at 15,407 URLs, raw totals flat
mcp.so feed                       30 stamped cards, 2 above the cutoff
submission queue                  25 arrivals, 2 catalogued
guides                            2 new guide directories
```
