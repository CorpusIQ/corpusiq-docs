---
title: "Sweep Report - September 1, 2026 - CorpusIQ Docs"
description: "Midday MCP catalog sweep: chatmcp/mcpso issues #3873-#3876, cataloged ErzyCall with a verification guide."
date: 2026-09-01T11:02:00-07:00
sources: [chatmcp/mcpso, mcpservers.org]
status: complete
last_updated: "2026-10-19"
---

# Sweep Report - September 1, 2026 (Midday Cron Sweep)

- **Shift:** Midday (run ~11:02 MST, ~18:02 UTC)
- **Fresh window:** chatmcp/mcpso issues #3873-#3876 (all filed after the morning sweep cutoff of #3872)
- **Secondary surface:** mcpservers.org /all page 1 (30 broad slugs, cross-ref only)
- **Prior sweep cutoff:** issues through #3872 (morning sweep commit 1d87603bc, catalogued Gridar, Hive Intelligence, Ranki, StackScope)
- **Outcome:** 1 new server catalogued with a guide (ErzyCall); Docling MCP deduped against a sibling afternoon sweep; 2 issues already disposed by the sibling with matching conclusions

## Sibling race (resolved, zero duplicates)

A sibling "afternoon sweep" (commit 28776c137, "mcp: afternoon sweep Sep 1 - catalog Docling MCP; catalog 461 servers") landed between this sweep's fetch and rebase. Detection: `git pull --rebase` hit add/add conflict on docling-mcp/index.md (both sessions catalogued issue #3873). Resolution: `git rebase --abort`, `git reset --hard origin/main`, re-applied only the ErzyCall delta. The sibling's Docling guide is the live one; its diamond-mcp and Washlib skip dispositions match this sweep's conclusions, so no duplicate skip prose was written.

## Catalogued (1)

| Server | Source | Verification chain |
|--------|--------|--------------------|
| ErzyCall MCP | issue #3876 | Endpoint https://app.erzycall.com/api/mcp initialize probe returned 401 Unauthorized - liveness signal per the Jitsu class (OAuth 2.1 gate). Vendor /docs/mcp page documents the full connection flow: OAuth 2.1 PKCE + DCR (RFC 7591), POST-only Streamable HTTP (GET 405), no API key for MCP, scopes (calls, contacts, contact_groups, cases, assistants, phone_numbers, whatsapp, usage), confirmation-before-dial model, webhooks. No public adoption data - brand new submission. |

## Deduped to sibling sweep (not re-catalogued)

- **Docling MCP** (#3873) - sibling afternoon sweep catalogued it with its own guide at docling-mcp/ (verified live in main, frontmatter + body present). This sweep's independent verification (727 stars, MIT, PyPI v3.2.0, registry io.github.docling-project/docling-mcp) matched.
- **diamond-mcp** (#3875) - both sweeps skipped it (niche educational and consumer class).
- **Washlib** (#3874) - both sweeps skipped it (consumer local-services class).

## Skipped (/all page 1)

Zero new dispositions - all 30 slugs were morning/afternoon sweep dispositions (GridCarbon, Onchain Diary, CordFind, Vaanzari Commerce, Firefly III, SigVest, LinkUpAPI, GridNews, Perception, mlab.sh, urdigitalau family, Seedance re-listings).

## Notable dispositions

- **Sub-hour same-day sweep re-confirms the issues-only doctrine at the sibling level:** the entire unique yield was 1 issue (#3876, filed ~1 minute before the fetch); /all page 1 and the issue window #3873-#3875 were already owned by the sibling sweep.
- **Two sessions reached identical skip verdicts independently** (diamond-mcp, Washlib) - the skip-class doctrine is stable.
- **reset --hard after rebase --abort deletes files tracked only in the aborted local commit** - the ErzyCall guide and this report were rewritten from context. The sibling's docling-mcp/ (tracked in origin/main) survived.

## Commit

- Guides: erzycall-mcp
- Index: frontmatter date + last-updated line + top section + tail block (462 servers, +348 guides)
- Validation: erzycall-mcp guide PASS (YAML, lengths, em-dash, credential-guard, See Also dirs + labels)
