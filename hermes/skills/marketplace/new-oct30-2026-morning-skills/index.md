---
title: "New Skills - October 30, 2026 Morning"
description: "Skills.sh sweep (Oct 30 morning): 885 skills scanned, 19 queued publisher guides for 345.9K combined installs across 264 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct30-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 30, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 86 NEW, 266 PARTIAL.

This fire did not come from the standing window, and it did not need a new probe either. The window was silent above the 1,000-install trigger for the twenty-third consecutive fire, its top row reading 302 installs, and all 60 of its NEW sources sized under 2,000 combined once queried by publisher. The trending board served 600 entries across 68 sources with every one of them already in the tree.

So the fire drained the queue the previous probe left behind: 19 repository-scoped clusters that had already been sized above the 5,000-install floor and cross-checked against the catalog. Together they carry **345,882 combined installs across 264 indexed listings**.

Every guide was drafted against a pre-built pack holding the exact per-listing install figures, the cloned repository tree, branch and licence metadata and three-auditor verdicts sampled from skills.sh, then checked with three gates: the format gate, the pack cross-check at a per-guide threshold of 500 installs, and the frontmatter audit. All 57 gate runs passed, re-run by the orchestrator after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 885 (0 failed queries) |
| NEW (not in catalog) | 86 |
| PARTIAL (source known, skill not cataloged) | 266 |
| Trending board | 600 entries / 68 sources, 0 uncovered |
| Above-floor finds in the standing window | 0 (top row 302) |
| Queue carried from the Oct 29 probe | 19 clusters |
| Guides published this fire | 19 |

## Publisher Guides

| Guide | Repository | Installs | Listings | Stars | License |
|---|---|---|---|---|---|
| Remotion Framework Skills | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 47,489 | 73 | 69,018 | NOASSERTION while LICENSE.md carries the two-tier Remotion License |
| Auth0 Agent Skills | [auth0/agent-skills](https://github.com/auth0/agent-skills) | 28,077 | 47 | 55 | Apache-2.0 |
| Upstash Context7 | [upstash/context7](https://github.com/upstash/context7) | 25,472 | 8 | 63,945 | MIT |
| Svelte AI Tools | [sveltejs/ai-tools](https://github.com/sveltejs/ai-tools) | 24,570 | 2 | 335 | MIT |
| Prisma Next Skills | [prisma/prisma-next](https://github.com/prisma/prisma-next) | 23,921 | 40 | 411 | Apache-2.0 |
| Axiom Skills | [axiomhq/skills](https://github.com/axiomhq/skills) | 23,872 | 15 | 17 | MIT |
| Lavish AXI | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | 23,474 | 3 | 4,358 | MIT |
| Multi-Agent Review | [riekelt/multi-agent-review](https://github.com/riekelt/multi-agent-review) | 19,509 | 1 | 82 | no licence file |
| Pulumi Agent Skills | [pulumi/agent-skills](https://github.com/pulumi/agent-skills) | 16,370 | 17 | 78 | Apache-2.0 |
| components.build | [vercel/components.build](https://github.com/vercel/components.build) | 14,813 | 1 | 802 | NOASSERTION while the LICENSE file is Apache-2.0 and the README says MIT |
| Kapso Agent Skills | [gokapso/agent-skills](https://github.com/gokapso/agent-skills) | 13,788 | 9 | 195 | no licence file |
| Dotneet Claude Code Marketplace | [dotneet/claude-code-marketplace](https://github.com/dotneet/claude-code-marketplace) | 12,917 | 10 | 3 | no licence file |
| Swift Concurrency Skill | [twostraws/swift-concurrency-agent-skill](https://github.com/twostraws/swift-concurrency-agent-skill) | 12,209 | 1 | 578 | MIT |
| Vectorize Hindsight Skills | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 11,470 | 15 | 56,373 | MIT |
| Amazon Devices Agent Skills | [amazonappdev/devices-agent-skills](https://github.com/amazonappdev/devices-agent-skills) | 10,978 | 2 | 6 | MIT |
| Vinta Django AI Plugins | [vintasoftware/django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins) | 8,390 | 5 | 166 | no licence file |
| Vercel Chat SDK Skills | [vercel/chat](https://github.com/vercel/chat) | 6,118 | 3 | 2,434 | MIT |
| Better Icons | [better-auth/better-icons](https://github.com/better-auth/better-icons) | 6,047 | 1 | 1,445 | MIT |
| Google ADK Docs | [google/adk-docs](https://github.com/google/adk-docs) | 16,398 | 11 | 1,530 | Apache-2.0 |

## What Stood Out

- **Two licensing corrections.** The Remotion repository reports NOASSERTION to GitHub and carries a two-tier Remotion License in its LICENSE.md: free for individuals, non-profits and for-profit organizations up to three employees, with a company licence above that. The components.build repository gives three answers at once, Apache-2.0 in the LICENSE file, NOASSERTION from the API and MIT in its README. Both guides state every source rather than picking one.
- **Four repositories ship no licence at all** - multi-agent-review, gokapso/agent-skills, dotneet/claude-code-marketplace and vintasoftware/django-ai-plugins - and each guide carries that on the GitHub line, in the tier note, in the security section and in its limitations.
- **The largest install count is not the largest installable suite.** remotion-dev/remotion tops the batch at 47,489 installs, but 63 of its 88 SKILL.md files are internal maintainer skills for people working on Remotion itself, so the index measures a maintainer's daily habits rather than the video skills a builder would install.
- **A Hermes-native find.** vectorize-io/hindsight ships a first-class Hermes memory-provider plugin beside its 20 skills, so the guide documents both the skill route and the plugin route.
- **Index-versus-tree drift is the norm, not the exception.** Fifteen of the nineteen repositories index more names than exist as directories, from Auth0's 47 retired per-framework names against one consolidated skill to Google ADK's six above-threshold listings with no directory in the tree. Every guide names which rows have nothing to install rather than guessing what they do.

## Verification

Each guide carries its own verification block: raw SKILL.md URLs on the repository's real branch, probed before publication, plus a post-install check of the profile skills directory.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
