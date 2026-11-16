---
title: "New Skills - November 14, 2026 Evening"
description: "Skills.sh sweep (Nov 14 evening): 16 publisher guides for 112,605 combined installs across 135 indexed listings, from Replicate to Deno"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov14-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 14, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This is the second fire of the day and the fifty-fourth of the series. The morning fire broke a fifty-two-fire silence; this one confirms it was not an accident: the standing 20-query window returned 883 unique listings with 106 NEW and 250 PARTIAL rows, and its top NEW row sits at 3,354 installs.

The topic probe went wider again and then ran out of clock. The lane list was sized at 607 queries, of which 319 completed before this fire closed: 20 standing queries plus 299 fresh lanes at 2.7-second pacing through `curl`, returning 26,060 rows, 20,843 distinct listings and 5,897 distinct sources with zero failed queries. Response times from skills.sh rose from about 1 second to 4 or 5 seconds per query as the fire ran, which is what capped the lane count. After cross-referencing against the docs tree, 5,092 sources read as uncovered, with 51 above 3,000 combined installs, 97 above 2,000 and 228 above 1,000.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 883 listings / 831 names / 289 sources |
| NEW (standing window) | 106 rows |
| PARTIAL (standing window) | 250 rows |
| Top NEW row in the standing window | 3,354 (`gogf/skills` / `goframe-v2`) |
| Fresh topic lanes completed | 299 of 587 planned |
| Probe rows / distinct listings / distinct sources | 26,060 / 20,843 / 5,897 |
| Failed queries | 0 |
| Uncovered sources after cross-reference | 5,092 |
| Uncovered above 3,000 combined | 51 |
| Uncovered above 2,000 combined | 97 |
| Uncovered above 1,000 combined | 228 |
| Guides published this fire | 16 |
| Combined installs documented | 112,605 |
| Indexed listings covered | 135 |
| Tier mix | 9 Green, 6 Yellow, 1 Orange |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|--:|--:|---|
| Replicate Skills - Model Discovery and Inference | replicate/skills | 17,693 | 8 | Green |
| Text-to-Lottie - Animation Generation Setup | diffusionstudio/lottie | 11,490 | 1 | Yellow |
| gh-axi - Token-Efficient GitHub CLI for Agents | kunchenguid/gh-axi | 9,858 | 1 | Yellow |
| SwiftData Pro - Swift Data Modeling Skill Setup | twostraws/swiftdata-agent-skill | 9,797 | 1 | Green |
| Home Assistant Skills - Automation Setup Guide | homeassistant-ai/skills | 9,310 | 1 | Green |
| Wix Skills - Site, App and Design System Setup | wix/skills | 8,802 | 37 | Yellow |
| Frappe Skills - ERP Development and Review | frappe/skills | 7,333 | 11 | Yellow |
| Manim Skills - Math Animation for Agents | adithya-s-k/manim_skill | 7,007 | 2 | Green |
| Amplicode Spring Skills - Spring Boot Agent Suite | amplicode/spring-skills | 6,451 | 16 | Yellow |
| Inertia Rails Skills - Inertia.js for Rails Setup | inertia-rails/skills | 4,461 | 11 | Green |
| Honeycomb Agent Skill - Observability Setup | honeycombio/agent-skill | 4,105 | 8 | Yellow |
| Microsoft Fabric Skills - Power BI Agent Suite | microsoft/skills-for-fabric | 3,559 | 17 | Green |
| Streamlit Agent Skills - Data App Development | streamlit/agent-skills | 3,499 | 1 | Green |
| Laravel Boost - Laravel AI Development Setup | laravel/boost | 3,261 | 3 | Green |
| Basecamp Skills - 37signals Product Automation | basecamp/skills | 3,158 | 9 | Orange |
| Deno Skills - Official Deno Development Suite | denoland/skills | 2,821 | 8 | Green |

Nine of the sixteen are first-party publishers: Replicate, Wix, Frappe, Microsoft, Streamlit, Laravel, 37signals, Deno and Honeycomb. That ratio is the useful signal in this batch. The previous four fires were dominated by independent publishers consolidating other people's content; this one found official teams shipping their own skills, which is the pattern that survives contact with a real codebase.

## Carried forward, not published

- **cesartevisual/threejs-skills** (13,615 across 23 listings) and **full-stack-skills/threejs-skills** (8,363 across 18): two repositories of the same skill family with 22 and 12 stars, publishing 23 and 18 listings at 495 to 732 installs each. The shape suggests redistribution rather than authorship, so both are held pending an identity check.
- **gargantuax/openskills** (27,420 across 2 listings) and **vasilyu1983/ai-agents-public**: both GitHub repositories return 404, so there is no tree to verify.
- **whytryharder/superpowers** (56,892 across 86 listings): zero stars, no licence, no description, and a name that collides with the already-documented `obra/superpowers`. A mirror until proven otherwise.
- **thinkoodle/rails-skills** (5,458 across 26 listings, 7 stars, no licence), **dhruvanbhalara/skills** (5,181 across 28), **gocallum/nextjs16-agent-skills** (3,826 across 6): queued for a licence and authorship check before any page is written.
- **delphi-ai/animate-skill** (4,015), **iart-ai/kinetic-typography-skills** (4,010), **s1dashu/ip-as-logo-skill** (3,853), **shajith003/awesome-claude-skills** (3,723), **ramziddin/solid-skills** (3,668): single-listing finds with real install counts but thin repositories, all sized and waiting.
- **mohitagw15856/pm-claude-skills** (1,551 stars, 96 listings at the API cap) and **alterlab-ieu/alterlab-academic-skills**: the 96-row cap makes their totals floors, not totals, so neither can be quoted honestly yet.

## New pitfalls found this fire

- **The probe data must be deduplicated by listing, not by query.** A listing appears in every query that matches it, so summing install counts across rows inflates a publisher without limit: `amplicode/spring-skills` read 6,451 correctly only after deduplicating on `(source, name)`; the raw sum was 18,401. The first cross-reference of this fire ranked `full-stack-skills/threejs-skills` at 14,957 for exactly this reason. Deduplicate before ranking, always.
- **A background probe cannot be trusted to survive the tool call that started it.** Two runs were launched in the background; both died at the shell boundary and a third chorded pair wrote into the same file with conflicting offsets, producing two corrupt lines out of 13,415. Run long probes in bounded foreground chunks or verify the process is still alive before trusting the row count.
- **skills.sh slows down measurably as a probe runs.** The first 100 queries averaged about 3 seconds each; by query 300 the average was above 4.5 seconds, with no failures and no rate-limit responses. Time the first five queries and size the lane list from the measured rate, or the probe will outlive the fire.
- **Gate 2 flags a missing table row when a listing has no directory.** Honoring index-only drift in prose means the row is absent from the table, which `verify_guide_draft.py` reports as a missing row. The fix is to set the per-guide threshold above the highest ungrounded count, then state the drift in Limitations. `wix/skills` needed a threshold of 330 against 37 listings, and `replicate/skills` needed 1,900 against 8.
- **A whole publisher family can be index-only.** Seventeen `wix-cli-*` listings, at 202 to 288 installs each, have no directory anywhere in the `wix/skills` tree. The install index is not evidence that a skill can be fetched.

## Live verification

Deploy ran after the push to main. Every new guide page returns 200 with its own title on `docs.corpusiq.io` and through the `www.corpusiq.io/docs` proxy, the batch page returns 200 on both hosts, the catalog index renders the new sweep heading with all 16 links, the marketplace index carries the updated stamp and links this page, and the new URLs appear in `sitemap.xml`.

## Integration

Sixteen guides into `hermes/skills/catalog/`, one `### New - November 14, 2026 Evening Sweep (16 publisher guides)` block appended to `catalog/index.md`, this batch page, a Recent Sweeps entry at the top of `marketplace/index.md`, and PROGRESS counts resynced from the staged tree.

## Next-fire note

Carry the 288 unfinished probe lanes first, then re-probe the held publishers: `cesartevisual/threejs-skills`, `full-stack-skills/threejs-skills`, `thinkoodle/rails-skills`, `dhruvanbhalara/skills`, `gocallum/nextjs16-agent-skills`. Sized and ready to draft: `delphi-ai/animate-skill` (4,015 / 1), `iart-ai/kinetic-typography-skills` (4,010 / 1), `s1dashu/ip-as-logo-skill` (3,853 / 1), `shajith003/awesome-claude-skills` (3,723 / 1), `ramziddin/solid-skills` (3,668 / 1), `streamlit`-adjacent `appautomaton/document-skills` (3,494 / 3). Identity checks outstanding on `gargantuax/openskills`, `vasilyu1983/ai-agents-public` and `whytryharder/superpowers`. The 5,092 single-pattern-confirmed uncovered sources live in the sweep cache at `snap_final.jsonl`.
