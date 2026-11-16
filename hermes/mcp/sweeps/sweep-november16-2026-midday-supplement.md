---
title: "MCP Server Discovery - November 16, 2026 (Midday Supplement)"
description: "An hour flat on both directory surfaces, six queue arrivals, and two servers that ship on two different evidence tiers."
category: "MCP Ecosystem"
last_updated: "2026-11-16"
---

# MCP Server Discovery - November 16, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed at 10:11 MST. The canonical returned the same raw count, the same eleven per-map counts and the same key set, the feed carried **no** card above the midday's newest, and the submission queue carried **six** arrivals. **Two** servers ship, and the pass is as much about what each one's evidence tier does and does not support as about the tools themselves.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, eleven numbered server maps
raw <loc>, maps 1-11 at 18:01Z   65,551   identical to the 17:05Z midday capture
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 2,466
sum of per-map counts            65,551   exact
distinct keys, eleven-map basis  21,807   unchanged
priority-servers.xml             200 with 299 entries and 34 distinct keys
skills.xml                       200 with 12,579 entries
remote-mcp-servers.xml           200 with 15 entries, all fourteen locales of clockwise
set diff, union basis            0 additions, 0 removals against 21,841 retained keys
lastmod rows at/after 17:05Z     0
mcp.so /feed                     200 at 157,281 bytes, 30 cards, newest salescloser 15:47:45
                                 cards above the 15:47:45 cutoff: 0
submission queue #7468 to #7473  6 arrivals, bodies in six authenticated calls
```

## The flat surface, proved rather than asserted

The eleven numbered maps returned **65,551** raw `<loc>` entries, map by map identical to the midday capture, and the per-map totals sum to 65,551 exactly. The distinct locale-stripped key set read **21,807** on the eleven-map basis and **21,841** with the priority and remote maps unioned in, and the set diff against the **21,841** keys retained on disk from the 04:31 MST capture returned **0 additions and 0 removals**, so the hour's arrivals had to come from the queue.

**One measuring note belongs in the record.** An ElementTree pass over the eleven maps put the newest `lastmod` on the whole surface at **2026-11-16T10:30:17Z** and returned **zero** rows at or after the 17:05Z cutoff, while a first regex pass over the same maps had printed a **17:29:43** stamp for `servers/5.xml`. Re-reading that map directly found no such row: the regex had picked up a clock time from a July `lastmod`, not a November one. The ElementTree read over parsed `<url>` elements is the authoritative one, and it agrees with the key-set diff: nothing was stamped inside the hour.

The feed is flat by the same measure. `mcp.so/feed` answered **200** at **157,281** bytes with **30** stamped cards, byte-identical in size to the midday read, and the newest card is still **salescloser** at **15:47:45**, so **zero** cards sit above the midday's own newest. The midday's four cards (`salescloser`, `url2pin-mcp`, `funding-sales-signals`, `enhancv-resume-builder-job-search-8bfdaf`) carry their dispositions from that report and are not reopened here.

## The queue, six arrivals

**#7468** to **#7473**, filed between 17:08Z and 17:48Z, with bodies in six authenticated calls:

- **Olbrain Alchemist** (**#7468**) lets a coding agent build, test and publish Olbrain agents, with the server holding the step map and the human holding the approvals. Registry `com.olbrain/alchemist`, MIT plugin repo, **1** star. It is an agent-builder platform, which is the agent-infrastructure class this catalog has held consistently: a skill-and-agent catalogue rather than a data surface.
- **Seedara** (**#7469**) generates video, image and audio across **140+** models with credits and prices quoted before every run. Registry `ai.seedara/mcp`; the registry description says **150+** models on **1.0.0** and **140+** on **1.0.1**, the count moving down between versions. Media-generation aggregator class, held.
- **Momentic** (**#7470**) runs a bug bash on a deployed app or a pull request through Mo, then lists test runs and quarantined tests. Registry `ai.momentic/momentic`. Quality-assurance tooling for engineering teams, which is developer tooling rather than operator data.
- **Build to Launch MCP** (**#7472**) connects an agent to **300+** methods, workflows and examples plus **100+** live tools for keywords, SEO, trends and social data, membership-gated. The primary surface is a resource library with `search_btl_resources` and `use_btl_resource`, and its live tools land in the SEO class this catalog already carries twenty deep.
- **Podseeker** (**#7471**) ships below.
- **Kote Charts** (**#7473**) ships below.

## What ships, and why the evidence tiers differ

**[Kote Charts](/hermes/mcp/servers/external/kote-charts-mcp/)** (**#7473**) is keyless and was driven: `initialize` answered **200** as `kote-analytics` **1.1.0** on protocol **2025-06-18**, `tools/list` returned **four** closed schemas, all four tools were called over **17** `tools/call` requests, both prompts were listed and the **116**-entry resource surface was read. It serves **114** Bitcoin on-chain charts whose category counts sum to 114 exactly, each arriving with its formula, fields and units, update cadence, known limitations, analysed block height and a ready-made citation string. `get_latest` and `get_chart` agree to the field on the same day (**0.335** MVRV Z at **64,119.34** on 2026-11-15, from **0.466** at **68,232.31** the day before, a **6.03%** price fall against a **0.131** z-score fall), and the ETF flow series reconciles by subtraction (**1,329,664.3** minus **587.1** is **1,329,077.2**). Three defects are recorded rather than smoothed: the required argument is `id` while the prose says "chart", `additionalProperties: false` is declared but unknown arguments are silently dropped so a `points` argument returns the **500**-row default, and the running instance reports **1.1.0** while the registry lists **1.1.1** as latest. Its data licence is **non-commercial** with attribution while its code is MIT, which is the limitation an operator needs before building a paid workflow on it.

**[Podseeker](/hermes/mcp/servers/external/podseeker-mcp/)** (**#7471**) is OAuth and API-key gated, and this pass could only prove liveness: the endpoint answered **401** with a body naming both routes in and the key page. It ships on a documented surface of **19** tools read from the vendor README, a database built for podcast guest booking (**booking difficulty**, expected credentials, recent guests and their topics, host and producer contacts with role and confidence, **Client Fit** recommendations, and media lists that are the same objects the team sees in the app), an MIT repository under the vendor's own organisation, and two published registry records. No response shape, argument name or credit cost in that guide was observed from a live call, and the guide says so in its own evidence tier rather than implying a driven session.

## Also identified this pass

The canonical and the feed were both flat to the checkable measure described above, so every disposition here comes from the queue. **Olbrain Alchemist**, **Seedara**, **Momentic** and **Build to Launch** are held on the agent-builder, media-generation, developer-testing and SEO-library classes with the class owners named in the sweep section of the catalog index. `/all` was not re-read: it has answered **403** by edge policy since 4 November, so page-1 membership is absent evidence rather than corroborating evidence, and this pass does not claim otherwise.
