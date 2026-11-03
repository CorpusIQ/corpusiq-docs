---
title: "New Skills - November 2, 2026 Evening"
description: "Skills.sh sweep (Nov 2 evening): 11 publisher guides for 94.1K combined installs across 71 indexed listings, drained from the queue."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov2-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 2, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills with 0 failed queries: 84 NEW, 261 PARTIAL, and no NEW source above the 1,000-install trigger, its top row reading 306 installs. That is the thirtieth consecutive fire on which the standing window was silent above the floor.

The November 2 morning fire had probed 68 topic queries and left eleven above-floor sources queued after documenting the thirteen largest. This fire drained those eleven remaining clusters. Each source was re-tested against the current tree first, because a stored queue goes stale: all eleven were still undocumented, and each was sized again by its own repository rather than by its best window row.

Every guide was built from a pre-verified pack holding exact per-listing install figures, a depth-1 clone with its branch, licence and skill directories, and three-auditor verdicts sampled across each index. Each draft was then checked with three gates: the format gate, the pack cross-check at the pack's own threshold and the frontmatter audit. All 33 gate runs passed on the orchestrator re-run after an md5 comparison of the three canonical scripts, with no fix cycles.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 84 |
| PARTIAL (source known, skill not cataloged) | 261 |
| Above-floor finds in the standing window | 0 (top row 306) |
| Queued sources re-tested | 11 |
| Queued sources still undocumented | 11 |
| Guides published this fire | 11 |
| Combined installs documented | 94,072 |
| Indexed listings covered | 71 |

## New Setup Guides

- [Reverse Engineering Skills - Frida and IDA Setup](/hermes/skills/catalog/p4nda0s-reverse-skills-setup) - P4nda0s/reverse-skills, 14,669 combined, 8 listings, 2344 stars, no LICENSE file, Eight skills for Frida hooking, IDA symbol and struct recovery, DEX and IL2CPP dumps, where rev-frida carries a Socket Warn and rev-symbol a Snyk Warn and the README claims MIT with no licence file in the tree
- [YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup) - zeropointrepo/youtube-skills, 11,176 combined, 12 listings, 1159 stars, MIT, Twelve skills over the TranscriptAPI: transcripts, search, channels, playlists and captions, mirrored in both skills/ and clawhub/ trees, with a Socket Fail on the search and transcript listings
- [Lynx Agent Skills - DevTool and ReactLynx Setup](/hermes/skills/catalog/lynx-community-skills-setup) - lynx-community/skills, 10,307 combined, 20 listings, 28 stars, Apache-2.0, The official Lynx suite: DevTool CDP debugging, ReactLynx best practices, trace recording and analysis, bundle-size checks and OpenUI, on a release branch with one Snyk Warn on lynx-devtool
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup) - supabase/server, 10,220 combined, 1 listings, 94 stars, MIT, One skill living inside the @supabase/server SDK monorepo: auth modes, Edge Function handlers, client creation and context injection, with a Snyk Warn on the single listing
- [TikTok Video Skills - Short-Form Video Suite Setup](/hermes/skills/catalog/tiktok-video-skills-setup) - iart-ai/tiktok-video-skills, 9,858 combined, 4 listings, 20 stars, MIT, Four vertical-video skills for retention hooks, karaoke captions, lower thirds and countdowns, every sampled verdict a Pass
- [Infisical AI Skills - Secrets Management Setup](/hermes/skills/catalog/infisical-ai-skills-setup) - Infisical/ai-skills, 7,488 combined, 18 listings, 37 stars, MIT, Seventeen Infisical skills for the CLI, SDK and API through secret syncs, dynamic secrets, PKI, KMS, PAM and the Kubernetes operator, with 34 directories split between a flat skills tree and a plugin tree
- [Stageshow - Faux Product UI Skill Setup](/hermes/skills/catalog/benjitaylor-skills-setup) - benjitaylor/skills, 7,243 combined, 1 listings, 996 stars, no LICENSE file at root, One skill and a small React kit for product illustrations, cursor stories and motion design, with nine visual styles and 69 example scenes, carrying a Socket Warn and no licence file at the repository root
- [Semgrep Skills - Secure Code and Static Analysis](/hermes/skills/catalog/semgrep-skills-setup) - semgrep/skills, 6,622 combined, 3 listings, 338 stars, NOASSERTION, Three generated skills: a 28-page secure coding rule index, Semgrep scanning and rule authoring, and OWASP Top 10 for LLM applications, under the Semgrep Rules License v1.0 rather than an open source licence
- [NotebookLM nblm Skill - Source-Grounded Answers](/hermes/skills/catalog/magicseek-nblm-setup) - magicseek/nblm, 6,322 combined, 1 listings, 34 stars, MIT, One browser-driven NotebookLM skill for cited answers plus podcasts, slides and folder sync, with a Socket Fail and a Snyk Warn on the only listing and the SKILL.md at the repository root
- [Cline SDK Skill - Build AI Agents on @cline/sdk](/hermes/skills/catalog/cline-sdk-skill-setup) - cline/sdk-skill, 5,104 combined, 1 listings, 8 stars, Apache-2.0, One skill on the Cline Agent runtime: ClineCore sessions, custom tools and plugins, every sampled verdict a Pass
- [Next.js Cache Architecture - Setup Guide](/hermes/skills/catalog/nextjs-cache-architecture-setup) - mohamed-hossam1/nextjs-skills, 5,063 combined, 2 listings, 10 stars, MIT, Two skills on Next.js 16 caching: the use cache directive, cache tag registries, invalidation wiring and Suspense boundaries, plus a next-safe-action handler, with a static audit script and all sampled verdicts a Pass

## What the Batch Shows

Three guides are Green and eight are Yellow, and the Warn, the Fail or the missing licence is named in the guide rather than footnoted. Two of the eleven ship no licence file at all, one releases under the Semgrep Rules License rather than an open source text, and two carry a Socket Fail on the sampled listings.

The batch closes a gap in the catalog's coverage of working domains rather than frameworks: reverse engineering, cloud secrets management, video transcripts and short-form video production, static analysis, NotebookLM research, and Next.js caching. Each of those sat in the skills.sh index with thousands of installs and no page here.

Index-versus-tree drift is stated factually wherever it appears: the YouTube suite mirrors the same twelve skills in two trees, Infisical carries 34 directories against 18 listings, Lynx indexes 20 names against 16 unique directories, and the reverse-engineering suite's rev-ios-dump listing counts 1,172 installs from a description copied from its Android sibling.
