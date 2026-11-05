---
title: "MCP Server Discovery - November 5, 2026 (Late Morning Sweep)"
description: "An hour after the midday pass the sitemap was identical to the byte and the answer sat in the second read: the plain mcp.so fetch was thirty-one minutes stale and the cache-busted read carried one card, a personal memory vault."
last_updated: 2026-11-05
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november5-2026-late-morning"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 5, 2026 (Late Morning Sweep)

## Summary

This pass fired on the **11:00 MST** tick, one hour after the midday read, and the two named surfaces answered in opposite ways. The mcpservers.org canonical came back **set-identical** to the 04:31 MST capture: **19,513** server URLs, **zero** additions and **zero** removals, which is the first time this surface has produced an exact empty diff rather than a namespace-prefix shuffle. The mcp.so homepage produced the pass's only delta, and it produced it only on the second read: the plain fetch carried **80** cards with the newest at `2026-11-05T06:47:30Z`, the same stamp the midday pass had already dispositioned, while a cache-busted read of the same page returned the same **80** cards plus one new card at `2026-11-05T17:29:38.960Z`. That card is **Konshus.AI**, a personal memory vault, and it is the one server catalogued here.

The lesson is recorded rather than implied: on a one-hour interval, a single read of mcp.so can be **31 minutes** behind, so the two-read rule that was written for the three-hour ticks applies to every interval.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 12 sitemaps fetched with plain urllib, locale prefixes stripped, the **/servers/** subset diffed against the 04:31 capture | **19,513** server URLs against **19,513**, **0** additions, **0** removals. Exact match |
| mcpservers.org `/all` | direct fetch with a browser user agent | **403**, the same standing refusal as the three passes before it. Not read |
| mcp.so homepage, first read | direct fetch with a browser user agent, `recentServers` parsed by `createdAt` | **80** cards, newest `2026-11-05T06:47:30Z` (Agents Galleria), **zero** above the midday stamp |
| mcp.so homepage, cache-busted read | same page with a nanosecond query string | **80** cards, **1** card above the first read, newest `2026-11-05T17:29:38.960Z` (**Konshus.AI**) |
| Official MCP registry API | `search` on the catalogued candidate | resolved `ai.konshus/memory` **1.0.0**, published `2026-11-05T17:35:03Z`, remote `https://konshus.ai/api/mcp` |
| Vendor surface for the candidate | `konshus.ai/mcp`, `/pricing`, `/llms.txt`, the OAuth metadata, and two keyless JSON-RPC calls | `/mcp` **200** (11 tools, four scope groups), `/pricing` **200** (five tiers), `/llms.txt` **200** (25 sources), authorization-server and protected-resource metadata **200**, `initialize` **401** and token probe **401** |

One counting note for the next pass. The sitemap index now includes `static.xml` alongside the twelve server and priority maps, so a raw union reads **28,851** URLs and **9,338** of them are marketing, topic and search pages. Only the **/servers/** subset, **19,513**, is the server universe, and that is the number to diff.

## New Servers Catalogued

### Konshus MCP - Personal Memory Vault for Every MCP Client

Relevance: MEDIUM. **Endpoint verified as gated** (keyless `initialize` returns **401** `-32001` with the message that the server is stateless and every request must carry a bearer, and a probe token returns **401** `Invalid or expired token`), so the tool surface is documented from the vendor's own table rather than driven.

Konshus registers as `ai.konshus/memory` **1.0.0** six minutes after the mcp.so card appeared, and serves one member's vault at `https://konshus.ai/api/mcp` over stateless Streamable HTTP with OAuth 2.1, PKCE `S256`, `authorization_code` and `refresh_token` grants, a dynamic client registration endpoint, and exactly one scope: **`vault:rw`**.

The eleven tools are grouped into four scopes, and the grouping is the useful part:

- **summary**: `get_whisper` (a ~300-word identity primer meant to be read before every reply), `get_briefing`, `get_persona_summary`, `get_vault_stats`.
- **recall**: `search_atoms` with an **`as_of`** parameter for a point-in-time view, `search_artifacts` over raw sources, `recall_past_self`, `explain_what_you_know_about` (a narrative with citations rather than a link list), `whats_changed_since` as a standup.
- **capture**: `log_signal`, the only write, which is why the scope is read-write.
- **full mirror**: `get_mega_briefing`, described as a 15-page persona export.

The ingestion side is where the entry comes from. The vendor counts **25** sources, **22** live, Google Calendar in beta, Apple Health and Spotify announced: ChatGPT, Claude, Gemini and Grok history, Day One, Obsidian, Notion, Bear or Evernote, Readwise, Kindle, Apple Books, RSS and Substack, Limitless and Plaud transcripts, voice memos, Facebook, Instagram and LinkedIn archives, an X archive, and pasted documents. Each distilled atom carries its source and a confidence label, and the member can edit or delete an atom with the edit recorded against the source.

Pricing is a five-tier ladder read off the pricing page: **Ember free** with **50** memories and journal-or-paste ingestion only, **Spark $49/yr** for **250 to 500** active memories and **10 GB** over a one-year window, **Founding $149/yr** for **2,500 to 10,000** memories and **50 GB** over three years with all imports, **Counsel $299/yr** for up to **35,000** memories and **100 GB** over seven years, and **Counsel Pro $599/yr** with a **300 GB** vault and a lifetime window. Launch discounts are running against a founding cohort the vendor says has **1,456 of 4,000** memberships left.

Limits recorded in the guide: a consumer product rather than a business data connector, `vault:rw` as the only scope so per-scope token issuance is the control that matters, encryption and discretion claims that cannot be checked from outside, self-reported usage figures (**99.81%** seven-day uptime, **12,055** calls, **448** clients, **0.9s** p50) printed on the vendor's own page, and one vault per member with no team or per-client separation.

## Read and Held

There was nothing else to hold. The canonical diff was empty and the only card above the previous stamp was the one catalogued above, so this window produced **one** disposition rather than a column of them.

The candidate itself was checked against the five memory entries already in the catalog before it was written up: Agentic Memory is agent working memory with Redis and FIFO handoff, AIS Memory pairs session memory with a DID identity, MCP Long-Term Memory is GraphRAG over Neo4j, Linksee is local-first with a forgetting curve, and SPM is project-scoped with context packs. None of them takes a person's history from another vendor's product and serves it back with a source on every memory, which is the gap this entry fills. The five memory services held by the November 5 night pass (Zipline, Willder, Mazarbul, Ontoloop, madeleine) are the same agent-memory class and are unaffected by this entry.

## Core Listing Check

- **mcpservers.org**: LISTED. `/servers/corpusiq-io` is present in the twelve-sitemap canonical; the detail page answers **403** to a direct read, the same standing refusal `/all` returns, so this is the platform block and not a delisting.
- **Glama**: LISTED. `https://glama.ai/mcp/connectors/io.corpusiq/multi-source-mcp` returns **200**.
- **Official MCP registry**: `io.corpusiq/multi-source-mcp` **1.0.0** is `active` with the `https://mcp2.corpusiq.io/mcp` remote. The description still reads **30+** business systems against a catalog that states **40+**, which remains metadata drift to correct at the next publish.
- **mcp.so**: NOT LISTED. All four direct slug forms (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) return **404**, and the paid route stays declined under the no-payment rule, so it is not retried.

## Counts

- mcpservers.org canonical: **19,513** server URLs against **19,513** at the 04:31 MST capture, **0** additions, **0** removals.
- mcpservers.org `/all`: **403**, not read.
- mcp.so: **80** cards on both reads, the first newest `2026-11-05T06:47:30Z`, the cache-busted newest `2026-11-05T17:29:38.960Z`, **one** card above the midday stamp.
- Official registry: **one** record resolved for the candidate, `ai.konshus/memory` **1.0.0**.
- Endpoint probes: **two** against the candidate, both **401**, at the documented rather than driven tier.
- Guide tree: **1,103** directories before this pass and **1,104** after, **1,247** entries counting single-file guides before and **1,248** after.
