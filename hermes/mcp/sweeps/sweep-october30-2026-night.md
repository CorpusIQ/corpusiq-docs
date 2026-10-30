---
title: "MCP Server Discovery - October 30, 2026 (Night)"
description: "Six hours after the evening pass: the directory counter moved for the first time in three reads, and one business-research corpus earns the entry."
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october30-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 30, 2026 (Night Sweep)

This pass fired at `03:00 MST` against an evening read whose newest feed card was stamped `2026-10-30T03:18:57Z`. Six hours is a short window, and for the first time in three reads the directory counter actually moved rather than churning in place. The queue was busy and the entry came from somewhere else.

## What Was Catalogued

One entry, and the reason it is in rather than held is that nothing in this catalogue carries a business-research corpus with published gaps.

[Sprouts Data MCP](/hermes/mcp/servers/external/sprouts-data-mcp/) sits at `https://dashboard.sproutsdata.ai/mcp` and answered a bare `initialize` with **HTTP 401** and the JSON-RPC error `-32000` reading `No credential. Send your Sprouts API key as an X-API-Key header (or Authorization: Bearer ...). Keys are issued in the dashboard; sk_dsp_test_ keys hit the same corpus at zero credit cost.` The test-key clause is the practical detail: the surface can be driven before anyone pays, which is how a catalogue entry can be evidence rather than a directory card. The corpus is **43M+ companies**, **200M+ people** and **470M affiliation edges**, searched across nine categories: companies, people, patents, news articles, trends, market reports, funding rounds, research papers and job openings. Twelve tools are documented on the vendor's tools page, with six prompts and eight resources beside them, and the scopes split the surface into `dsp.search.read`, `dsp.entities.read`, `dsp.agents.write` and `dsp.usage.read`. Two design lines earn the entry. Records carry per-field provenance and the vendor publishes its own gaps through `sprouts_coverage`, which returns a `not_in_index[]` array in plain language, and a lookup miss is charged at zero, so absence is a first-class answer. The research run is asynchronous and priced by effort from **1.02 to 85 credits**, charged only on success and resumed by `run_id`. The gap is recorded, not smoothed: `tools/list` needs a key, so the twelve is the vendor's published list and not one this pass drove, and the landing page still says nine tools against twelve on the tools page.

## What Was Read and Held

Sixteen issues arrived between `#6417` and `#6432` and none became an entry.

The substantive arrival is `Enhanciar` (`#6429`), and it is held on strategy rather than on class. It reads Slack, Gmail, Google Drive, Notion, Jira, Linear, GitHub, Zendesk and Postgres, answers with a link to every source, and drafts the reply, ticket, doc or calendar event for approval, over twelve tools with `https://enhanciar.in/enhanciar/mcp/` answering **401** on a Bearer contract. That is the closest external surface to this catalogue's own product, so it is recorded as a competitor to watch and not published as an install guide.

`PayStage Preflight` (`#6420`) checks a proposed x402 payment against a local policy and returns `pay`, `review` or `do_not_pay` before the agent signs, read-only with no custody, held on the x402 payment preflight class already ruled on at `SpendPreflight` beside Pink Wallet and Mekler. `RepoMemory` (`#6417`) is a per-repository ledger of decisions, lessons and guardrails with a task queue, held in the memory class this catalogue carries heavily. `ATS Jobs` (`#6425`) reads postings first hand from Greenhouse, Ashby and Lever across 7,479 verified boards, held on the careers class carried by Applystead, CareJobs.Now and Web Remote Jobs. `Fictura` (`#6421`) is an Expo and React Native growth platform with 44 hosted tools, held on the product-analytics and mobile-vertical class. The Alvin's Club trio (`#6422` Channel, `#6423` BrandPilot, `#6424` Studio) is social publishing and product-video production across six networks, held on the social-publishing class at saturation per Pith and PostPlanify. `Coronium mobile proxies` (`#6426`) and `Proxies.sx` (`#6427`) rent 4G, 5G and residential bandwidth with rotation controls, held on the proxy infrastructure class. `7702 Sweeper Check` (`#6418`) and `Crypto Link Check` (`#6419`) are free crypto-safety lookups with x402-priced paid reports, held on the crypto class. `Mac Organiser` (`#6430`) is a local stdio server over Apple Reminders, Calendar and Notes whose allowlist the model cannot widen, held as hardware-bound local tooling. `GhostPaw Telegram` (`#6431`) mirrors a bot's messages into SQLite with full-text search, held beside the catalogued GhostPaw Email. `Pouch.me and Inkable Label` (`#6432`) answers questions about printed pouches and labels with confirm-to-send quote requests and reads no customer data, held on the vendor sales surface ruling. `Agent Bounty Feed` (`#6428`) is an aggregator of funded agent bounty boards arriving as a bounty fix, which is a directory shape rather than a record set.

On the feed, two cards sat above the evening stamp: `kilobat` is a macOS network diagnostics CLI with an MCP wrapper, held as developer infrastructure, and `paystage-6d8a8f` is the hosted card for the PayStage disposition above.

## Surfaces This Pass

| Surface | Reading | Delta |
| --- | --- | --- |
| mcpservers.org `/all` p1 to p3 | counter **18,400** from **18,230**, 90 unique slugs | first growth in three reads, page one rotated |
| mcp.so `/feed` p1 | 30 cards, newest `2026-10-30T09:46:12Z` | two above the evening stamp |
| chatmcp/mcpso issues | `#6417` to `#6432` | 16 issues in eight hours |
| Live probes | two endpoints | both 401 with a published credential contract |

## Catalog Movement

Catalog **1059** to **1060** servers, guides **1207** to **1208**.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)
