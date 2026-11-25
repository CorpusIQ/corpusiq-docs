---
title: "New Skills - November 25, 2026 Morning"
description: "Skills.sh sweep (Nov 25 morning): 15 guides, 124,239 combined installs across 703 listings, led by Jess Agent Skills and the BMad test-architecture suite."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov25-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 25, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

The standing 20-query window returned 886 unique listings across 290 distinct sources with no failed queries. Its largest rows were 2,181 installs (`0xdesign/design-plugin`), 1,971 (`404kidwiz/claude-supercode-skills`) and 1,535 (`adamlipecz/esp32-firmware-engineer-skill`), but the uncovered side held only 100 sources with negligible install mass, so the window again carried no convertible cluster and a fresh probe did the discovery work.

This fire probed vendor and platform ecosystems and capability themes rather than industries: CRM, support and marketing platforms, developer tooling and CI, data and warehouse platforms, design and media tools, CMS and commerce platforms, mobile and game engines, and a parallel set of capability lanes (revenue operations, compliance, testing, scientific computing, content production). Every shortlisted publisher was sized through its own exact-source filter before ranking, because a probe row understates a large publisher by an order of magnitude.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 886 listings |
| Distinct sources in the standing window | 290 |
| Uncovered sources in the standing window | 100 |
| Failed standing-window queries | 0 |
| Top standing-window row | 2,181 (`0xdesign/design-plugin`) |
| Fresh probe lanes completed | 426 |
| Unique rows merged (window plus probe) | 26,046 |
| Distinct sources in the merge | 7,493 |
| Uncovered sources after cross-reference | 6,523 |
| Sources at or above 400 probed installs | 110 |
| Candidates reachable on the GitHub REST repository endpoint | 106 |
| Candidates sized by exact source | 105 |
| Publishers published | 15 |
| Indexed listings behind those guides | 703 |
| Combined installs behind those guides | 124,239 |

## Published Guides

| Publisher | Guides | Combined installs | Listings |
|---|---|---:|---:|
| [Jess Agent Skills - GitHub Workflow Suite Setup](/hermes/skills/catalog/jssblck-agents-setup) | 1 | 17,568 | 27 |
| [BMad Test Architecture - Enterprise QA Skills Setup](/hermes/skills/catalog/bmad-test-architecture-enterprise-setup) | 1 | 15,065 | 22 |
| [RTK CLI Proxy - Token Reduction Skills Setup](/hermes/skills/catalog/rtk-ai-setup) | 1 | 12,838 | 8 |
| [rnskill Content Suite - Chinese AI Skills Setup](/hermes/skills/catalog/rnskill-setup) | 1 | 12,134 | 62 |
| [NicePkg AI Workflow - Prebuilt Skill Library Setup](/hermes/skills/catalog/nicepkg-ai-workflow-setup) | 1 | 10,463 | 96 |
| [SendAI Skills - Solana Agent Skill Marketplace Setup](/hermes/skills/catalog/sendaifun-skills-setup) | 1 | 8,166 | 50 |
| [Claude SEO AI - GEO and AEO Audit Toolkit Setup](/hermes/skills/catalog/claude-seo-ai-setup) | 1 | 7,275 | 34 |
| [Unity Skills - Game Development Automation Setup](/hermes/skills/catalog/unity-skills-setup) | 1 | 6,981 | 92 |
| [Contentful Skills - Headless CMS Agent Setup](/hermes/skills/catalog/contentful-skills-setup) | 1 | 5,870 | 12 |
| [Scientific Agent Skills - Research Workflow Setup](/hermes/skills/catalog/scientific-agent-skills-setup) | 1 | 5,760 | 62 |
| [WordPress Agent Skills - Audit and Optimize Setup](/hermes/skills/catalog/agent-skills-wordpress-setup) | 1 | 5,523 | 56 |
| [tldraw Skills - Infinite Canvas SDK Setup](/hermes/skills/catalog/tldraw-skills-setup) | 1 | 5,085 | 28 |
| [Embedded Engineering Skills - Arduino Maker Setup](/hermes/skills/catalog/embedded-engineering-skills-setup) | 1 | 4,678 | 43 |
| [Swan GTM Skills - Go-to-Market Suite Setup](/hermes/skills/catalog/swan-gtm-skills-setup) | 1 | 3,452 | 96 |
| [Warp Oz Skills - Agent Skills Collection Setup](/hermes/skills/catalog/warpdotdev-oz-skills-setup) | 1 | 3,381 | 15 |

Tiers: 1 Green, 10 Yellow, 4 Orange. Tier is derived from the skills.sh security verdicts sampled for each publisher, where any Fail cell moves a publisher to Orange.

## What These Publishers Cover

Agent workflow engineering leads the batch. Jess Agent Skills packages a personal GitHub loop as skills: merging PRs, resolving conflicts, tagging releases, running parallel agents and keeping sops secrets out of plain text. BMad Test Architecture adds an enterprise QA layer to the BMad Method, and RTK ships the skills that accompany a Rust CLI proxy built to cut token spend on common dev commands, with 87,780 stars behind it.

Content and commerce account for five: rnskill is a Chinese-language content factory for short video, Xiaohongshu and Douyin with captions, covers, avatars and voice work; NicePkg AI Workflow bundles 96 workflow skills across content, marketing, video, trading and product management; SendAI Skills indexes the Solana ecosystem for agents; Unity Skills turns one Unity template into 85 module documents for scene, asset and build work; and tldraw Skills covers migrating, documenting and testing inside the infinite-canvas SDK.

Web platforms and CMS account for three: Contentful publishes its own headless CMS skills, WordPress Agent Skills pairs site audits with a 220-tool MCP plugin for fix and migration work, and Claude SEO AI scores both classic search and generative-answer visibility before an opt-in fixer runs.

Scientific, hardware and go-to-market work round out the batch: Scientific Agent Skills covers Python numeric, plotting and mesh tooling; Embedded Engineering Skills covers Arduino scaffolding, datasheets and sensor work; Swan GTM Skills organizes go-to-market skills per creator; and Warp Oz Skills is Warp's own 15-skill collection, led by webapp testing and SEO audits.

## Method

Each publisher was probed on skills.sh, sized with a strict source-equality filter over its full listing set, checked on the GitHub REST repository endpoint, and documented from its own README and SKILL.md files. The exact-source filter decided the ordering: the probe read 1,186 installs for `jssblck/agents` against 17,568 exact, 1,539 for `rtk-ai/rtk` against 12,838, and 1,681 for `pluviobyte/rnskill` against 12,132. Every guide states its install band, its licence, its sampled security verdicts and the drift between what skills.sh indexes and what the repository tree actually contains.

## Held Back

`BrianRWagner/ai-marketing-skills` is a rename of the publisher already documented as [AI Marketing Skills](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup), and `beltsh/superpowers` and `whytryharder/superpowers` are forks of the inference.sh corpus already covered through the existing superpowers guides. `shajith003/awesome-claude-skills`, `dengineproblem/agents-monorepo`, `endigo/claude-skills` and `eddiebe147/claude-settings` returned 404 on the GitHub REST repository endpoint.

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
