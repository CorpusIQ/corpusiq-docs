---
title: "New Skills - November 13, 2026 Evening"
description: "Skills.sh sweep (Nov 13 evening): 12 publisher guides for 285,717 combined installs across 439 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov13-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 13, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 883 unique skills across 0 failed queries: 82 NEW rows and 249 PARTIAL, with the top NEW row at 350 installs (`sjy051/music-composition`). That is the fifty-second consecutive silent window on the standing board, and nothing in it came within a factor of three of the 1,000-install trigger.

The morning fire had widened the probe lanes from 87 to 174 queries and the band recovered, so this fire widened again rather than touching the floor. The probe ran 250 queries across business process, vertical industry, product, communications, developer and personal-productivity lanes: 20,778 rows across 5,391 distinct sources, one failed query (`dropship fulfillment`). Uncovered sources came back at 4,605, with 63 above 3,000 combined installs against 8 in the morning fire.

The queue carried two jobs. The eight candidates the morning note left sized were drafted as measured, and four fresh finds from the probe were added once their exact-source sizes came back. The largest find of the fire, `codewithmukesh/dotnet-claude-kit`, is also the reason for the headline pitfall below.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 883 (0 failed queries) |
| NEW (not in catalog) | 82 rows |
| PARTIAL (source known, skill not cataloged) | 249 |
| Above-floor finds in the standing window | 0 (top row 350) |
| Fresh topic probe | 250 queries, 20,778 rows, 5,391 sources, 1 failed |
| Uncovered sources from the probe | 4,605 |
| Uncovered above 3,000 combined | 63 |
| Uncovered above 2,000 combined | 104 |
| Uncovered above 1,500 combined | 154 |
| Uncovered above 1,000 combined | 255 |
| Candidates sized from source | 10 pre-sized, 6 fresh |
| Guides published this fire | 12 |
| Combined installs documented | 285,717 |
| Indexed listings covered | 439 |
| Tier mix | 3 Green, 8 Yellow, 1 Orange |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|--:|--:|---|
| DotNet Claude Kit - .NET 10 Engineering Setup | codewithmukesh/dotnet-claude-kit | 176,295 | 65 | Green |
| Plinth - Java Enterprise SDLC Toolkit Setup | jabrena/plinth | 31,263 | 96 | Green |
| Stock Checker - Ticker Analysis for Agents Setup | gracefullight/stock-checker | 28,638 | 69 | Yellow |
| Claude Bughunter - Red Team Skill Bundle Setup | elementalsouls/claude-bughunter | 25,418 | 83 | Yellow |
| AWS Skills - CDK, Serverless and Cost Ops Setup | zxkane/aws-skills | 4,620 | 6 | Yellow |
| EventCatalog Skills - Architecture Docs for Agents | event-catalog/skills | 3,955 | 6 | Green |
| LinkedIn Skills - 13-Skill Content Engine Setup | sergebulaev/linkedin-skills | 3,815 | 13 | Yellow |
| Day1Global Finance Skills - 5-Skill Market Setup | star23/day1global-skills | 2,970 | 5 | Yellow |
| Israeli Tax and Finance Skills - 50-Skill Setup | skills-il/tax-and-finance | 2,426 | 50 | Yellow |
| BibiGPT Skill - Video Summary for Agents Setup | jimmylv/bibigpt-skill | 2,129 | 4 | Orange |
| Giulioco Skills - Social Growth and Sales Setup | giulioco/skills | 2,121 | 8 | Yellow |
| Creator Marketing Skills - 34-Skill Program Setup | archive-dot-com/creator-marketing-skills | 2,067 | 34 | Yellow |

All 48 gate invocations were green on the orchestrator re-run: `qa_guide.py`, `verify_guide_draft.py` at a per-guide threshold, and `guide_frontmatter_check.py` for each of the 12 drafts, plus `validate_page_metadata.py`. One metadata failure and one prose defect were fixed by hand, both described below.

## The probe undercounts big publishers by an order of magnitude

This is the lesson of the fire. The probe is a semantic search over skills.sh: it returns the rows that match a query, up to 96, not every listing a source owns. A publisher whose skills cluster under one query reads at roughly its real size, and a publisher whose 65 skills spread across 65 different query lanes reads at a fraction of it.

| Source | Probe rows | Exact-source rows | Understatement |
|---|--:|--:|--:|
| codewithmukesh/dotnet-claude-kit | 3 rows, 11,069 | 65 listings, 176,295 | 16x |
| jabrena/plinth | 14 rows, 4,255 | 96 listings, 31,263 | 7x |
| gracefullight/stock-checker | 4 rows, 16,221 | 69 listings, 28,638 | 1.8x |
| elementalsouls/claude-bughunter | 18 rows, 5,161 | 83 listings, 25,418 | 5x |

The first pass of this fire ranked candidates by probe rows and put `codewithmukesh/dotnet-claude-kit` seventh, at 11,069 installs. The exact-source filter, which queries `q=<owner>/<repo>` and keeps only rows whose `source` matches the string exactly, puts it first at 176,295 across 65 listings. Ranking the queue by probe rows would have drafted a 25K pack and skipped the largest one available. Every candidate in the top band now goes through the exact-source filter before it is sized.

## Held, with the reason measured

- **vasilyu1983/ai-agents-public** (14,147 in the probe, 19,636 across 96 exact rows, a 96-row API cap): a broad multi-domain library that needs a domain pass per skill rather than a size pass.
- **kimny1143/claude-code-template** (14,076 / 3 listings, one at 4,692): a template repository whose skills are configuration rather than workflow.
- **andreadellacorte/groove** (12,365 / 23): consistent 600-install rows across 23 skills, queued for the next fire with a tree check pending.
- **hexiaochun/seedance2-api** (11,983 / 2, one listing at 11,962): a single-listing four-figure skill. A note, not a guide.
- **arkdocs.tos-cn-beijing.volces.com**, **apifox.com**, **senclaw-cdn.italent.cn**: CDN and product domains with no repository behind them, so nothing to verify.
- **tinyfish-io/tinyfish-cookbook** (10,709 / 4): queued, not size-checked.
- **colosseumorg/colosseum-copilot** (8,984 / 2), **emblemcompany/emblemai-agentwallet** (8,709 / 1), **astro-han/karpathy-llm-wiki** (8,690 / 1): single-purpose finds held for a second listing before they earn a page.
- **oracle/netsuite-suitecloud-sdk** (8,164 / 11): a vendor SDK reference set, queued.
- **alterlab-ieu/alterlab-academic-skills** (6,788 / 96, 243 `SKILL.md`) and **mohitagw15856/pm-claude-skills** (5,384 / 96, 3,097 `SKILL.md`): still need a domain pass rather than a size pass.
- **wix/skills** (8,754 / 37): still waiting on index-versus-tree drift.

## New pitfalls found this fire

- **Rank candidates by exact-source size, never by probe rows.** The table above is the evidence: a 16x understatement on the largest find of the fire. The probe discovers sources; the exact-source filter sizes them.
- **A tail sentence with a grammar defect passes every gate.** The EventCatalog guide shipped "The remaining 1 indexed listings range from 85 to 85 installs" through all three gates and the metadata gate. No gate reads prose, so the tail arithmetic needs a human reading for singular and plural, not just for the integers.
- **`validate_page_metadata.py` caught a description that the drafting gates passed.** The Bughunter guide's description ended on "bug bounty and red-team work", and the same phrase appeared in the body's authorised-use sentence, so the metadata gate read the description as a truncated quote (DESC CUT IN BODY). Rewording the description tail to "authorised red team and bounty work" cleared it. Run the metadata gate on every new guide before staging, not after.
- **The search API caps a source at 96 rows, and three of this fire's guides hit the cap.** Plinth serves 96 rows against 126 `SKILL.md` files, so both its listing count and its install total are floors. Say so in the guide rather than presenting a capped figure as complete.
- **A repository can bundle an unrelated framework.** `gracefullight/stock-checker` indexes five finance skills and about forty `oma-*` agent-framework skills from the same tree. The guide names both groups rather than folding the framework into the finance story.

## Live verification

Deploy run after the merge. Every new guide page returns 200 with its own title on `docs.corpusiq.io` and through the `www.corpusiq.io/docs` proxy, the batch page returns 200, the catalog index renders the new sweep heading with all 12 links, the marketplace index carries the updated stamp and links this page, and all 12 new URLs appear in `sitemap.xml`.

## Integration

Twelve guides into `hermes/skills/catalog/`, one `### New - November 13, 2026 Evening Sweep (12 publisher guides)` block appended to `catalog/index.md`, this batch page, a Recent Sweeps entry at the top of `marketplace/index.md`, the stamp moved from 1,598+ to 1,610+, and PROGRESS counts resynced from the staged tree.

## Next-fire note

Queue, all in the measured band and none of them sized: `andreadellacorte/groove` (12,365 / 23), `tinyfish-io/tinyfish-cookbook` (10,709 / 4), `vasilyu1983/ai-agents-public` (96 rows capped, 126-plus skills), `oracle/netsuite-suitecloud-sdk` (8,164 / 11), plus the 63 uncovered sources above 3,000 in `/tmp` cache from this fire. Keep the 250-query lane list, and run the exact-source filter on every candidate before drafting anything.
