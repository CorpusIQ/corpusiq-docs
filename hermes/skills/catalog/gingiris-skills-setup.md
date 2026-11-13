---
title: "Gingiris Skills - SEO, GEO and Growth Ops Setup"
description: "gingiris-1031/gingiris-skills: 9.6K combined installs across 64 listings, SEO, GEO, launch and open-source growth playbooks for operators"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gingiris-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "growth"]
---

# Gingiris Skills - Setup Guide

**Source:** [gingiris-1031/gingiris-skills](https://www.skills.sh/gingiris-1031/gingiris-skills) via skills.sh - 9.6K combined installs across 64 indexed listings; first seen Nov 13, 2026
**GitHub:** 91 stars, MIT license for the downloadable skills, `main` branch, last pushed 2026-11-12, 79 `SKILL.md` files under `skills/`, 485 files in total
**Category:** SEO and GEO, product launch, open-source marketing and B2B growth
**Quality Tier:** 🟡 Yellow - 64 listings over 79 in-tree skills and a four-language README, but a commercial tier upstream.

This is a growth operator's monorepo rather than a tidy skill pack. The README says the content is distilled from real operations and not compiled from secondary sources, and the two-layer structure backs that up: long-form `gingiris-*` playbooks that explain a GTM motion, and short `gr-*` execution skills that run it.

The routing skill is the interesting design decision. `gr` is the entry point: ask it how to grow, how to launch on Product Hunt, why organic traffic dropped, or to write a blog post, and it dispatches to the narrowest matching sub-skill. The author's `gingiris-growth-finder` does the same job at the strategy layer, diagnosing the growth model, the stage and the current constraint before routing.

Coverage is broad and operator-flavoured: SEO and GEO patrol and citation tracking, backlink building across five channel types, blog publishing, B2B lifecycle growth, App Store optimisation, KOL and UGC programs, Product Hunt launches, GitHub star growth, README writing, community ambassadors and DevRel. Several playbooks carry hardware and consumer case material alongside the software examples.

The README is published in English, Chinese, Japanese and Korean, and the skill files themselves mix languages, which is the single most practical thing to know before installing (see Limitations).

## Installation

```bash
# Install everything
npx skills add Gingiris-1031/gingiris-skills

# Or install one skill at a time
npx skills add Gingiris-1031/gr-readme
npx skills add Gingiris-1031/gr-oss-marketing

# Install a single skill by name from the monorepo
npx skills add Gingiris-1031/gingiris-skills --skill gr-wechat-editorial
```

The README's own heading says 65 skills install in one command, the tree holds 79 `SKILL.md` files, and the install index serves 64 listings. All three numbers are real; the repo has simply grown faster than its own marketing.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gr | 220 | The growth router: dispatches a growth question to the narrowest matching sub-skill. |
| gr-backlinks | 193 | Backlink building across five channel types ranked by GEO and SEO return. |
| gr-blog-post | 189 | Blog publishing pipeline that writes in a fixed house style with frontmatter and article structure. |
| gingiris-seo-geo-agent | 188 | SEO and GEO agent operations SOP rebuilt from live operations, including a Search Console incident. |
| gr-social-distill | 188 | Adapting a supplied article or draft into the requested social formats, with source attribution. |
| gr-b2b-growth | 188 | B2B SaaS lifecycle growth from PMF validation toward $10M ARR, covering PLG and sales-led selection. |
| gr-aso | 188 | App Store optimisation and app cold start: keyword research, metadata, creator matrix, localisation. |
| gr-seo-patrol | 187 | Daily SEO and GEO patrol: rank tracking, index counts and llms.txt checks. |
| gr-user-interview | 186 | User interview and requirement validation: recruitment, question design, synthesis, follow-up handoff. |
| gr-geo-cite | 186 | Weekly citation tracking and optimisation across four AI assistants. |
| gr-competitor | 185 | Competitor scanning on evidence: history, pricing, blog and channel history. |
| gr-oss-marketing | 184 | Open-source launch and topical marketing, including GitHub star growth and community distribution. |
| gr-ph-launch | 183 | Product Hunt launch script: T-14 warm-up, launch day and T+7 post-launch. |
| gingiris-kol-outreach | 162 | KOL and influencer marketing SOP from discovery to ROI tracking. |
| gingiris-b2b-growth | 162 | The long-form B2B growth playbook: is the constraint distribution, pricing or product-market fit. |
| growth-hacking-playbook | 162 | Designing, prioritising and running measurable growth experiments across the funnel. |
| go-to-market-playbook | 162 | A reusable go-to-market template for B2B and B2C launches: positioning, messaging, ICP. |
| competitor-research-playbook | 162 | Competitor research: choosing benchmarks, reconstructing positioning, feeding GTM. |
| gingiris-launch | 161 | Multi-channel launch timing and sequencing, T-14 warm-up through launch week. |
| viral-marketing-playbook | 160 | Designing referral programs, invite systems and share mechanics into the product. |

The remaining 44 indexed listings range from 1 to 159 installs.

## Why This Matters for Hermes Agents

Growth work fails on sequencing more than on ideas. A founder who runs a launch, a backlink campaign and a Product Hunt push in the same week learns nothing from any of them, and the agent gets blamed for the noise.

What this suite adds is the routing layer. `gr` and `gingiris-growth-finder` both exist to answer "which motion applies to my situation right now", and an agent that can pick the narrowest skill is far more useful than one holding 79 playbooks and no index.

The other useful property is that the playbooks are operational rather than inspirational. `gr-seo-patrol` names what a daily patrol checks. `gr-ph-launch` splits the launch into T-14, T-0 and T+7. `gr-geo-cite` runs weekly against four named assistants. Those are schedules an agent can hold, which is most of the value of putting them in an agent at all.

For a Hermes operator running a small product, the realistic pairing is two or three skills, not 64: one patrol, one launch motion, one content pipeline.

## Usage

| You say | What happens |
|---|---|
| "What should we do to grow this month?" | Runs `gr` or `gingiris-growth-finder`, diagnoses the constraint, and routes to the narrowest skill. |
| "Run today's SEO patrol on our domain" | Runs `gr-seo-patrol` and reports rank movement, index counts and llms.txt state. |
| "Plan our Product Hunt launch three weeks out" | Runs `gr-ph-launch` and returns the T-14 warm-up plan through the T+7 follow-up. |
| "Which AI assistants cite us for our main keyword?" | Runs `gr-geo-cite` and returns the weekly citation picture across the four assistants. |
| "Turn this blog post into five social posts" | Runs `gr-social-distill` and returns the formats with the source attributed. |
| "Rewrite our repo README so people star it" | Runs `gr-readme` and returns a conversion-oriented README structure. |
| "We are deciding between product-led and sales-led" | Runs `gr-b2b-growth` and returns the selection logic for the current stage. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/Gingiris-1031/gingiris-skills/main/skills/gr-readme/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Gingiris-1031/gingiris-skills/main/skills/gr-backlinks/SKILL.md
```

Read the head of both. These files are not all written in English, so the probe doubles as a language check before you install 79 of them into an agent's skill directory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gr | Pass | Pass | Pass |
| gr-backlinks | Fail | Pass | Warn |
| gr-blog-post | Pass | Pass | Pass |
| gingiris-seo-geo-agent | Pass | Warn | Pass |

`gr-backlinks` fails the Gen Agent Trust Hub check and carries a Snyk Warn, so read that SKILL.md in full before installing it, and treat anything it asks the agent to fetch or submit as untrusted until you have. Two of the three other sampled skills pass all three checks; the third carries a single Socket Warn. The remaining 60 listings publish no verdict at all, which is not a pass.

## Limitations

- Snapshot data, verified 2026-11-13: 9,614 combined installs across 64 indexed listings; 91 GitHub stars; MIT license for the downloadable skills; last pushed 2026-11-12. Counts drift over time.
- The licence covers the repository materials only. The README is explicit that hosted Gingiris Pro services, private datasets, managed execution, paid reports and brand assets are separate commercial products, and the repo carries a paid resource pack and community signup in WeChat.
- The tree carries more skills than the index serves: 79 `SKILL.md` files against 64 indexed listings, with the README claiming 65. Installing the repo gets you the larger set, and some of those skills have no install count to judge them by.
- The README is CJK-first in places and several skill files are written in Chinese. An English-only agent may load instructions it cannot follow cleanly, so check the language of the skills you actually install.
- One sampled skill fails its trust verdict. `gr-backlinks` is also one of the most installed listings in the pack, which is a combination worth pausing on.

## Related

- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [OpenSEO - Self-Hosted SEO Platform, MCP and Skills Setup](/hermes/skills/catalog/open-seo-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `gr` first and let it route. Installing a specific `gr-*` skill without the router is how you end up running a backlink campaign when the actual constraint was activation.
- Use `gingiris-growth-finder` at the start of a quarter, not the start of a week. It diagnoses stage and constraint, and that answer should not change weekly.
- Read `gr-backlinks` before installing it. The failing trust verdict is on that skill specifically, and backlink workflows are the ones that touch third-party sites.
- Check the language of each file you install. A Chinese-language skill is still usable if your operator reads Chinese and useless if the agent is asked to follow it for an English deliverable.
- Keep the free and paid surfaces separate in your notes. When a skill points at hosted Gingiris Pro or a paid resource pack, that is a commercial upsell inside an MIT repo, not a dependency.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
