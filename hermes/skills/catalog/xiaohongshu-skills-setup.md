---
title: "Xiaohongshu Skills - RED Content Operations"
description: "vivy-yi/xiaohongshu-skills: 28.1K combined installs. A Chinese-language library of 139 RED content, account and commerce skills, with no LICENSE file."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/xiaohongshu-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "xiaohongshu", "red", "content operations"]
---

# Xiaohongshu Skills - Setup Guide

**Source:** [vivy-yi/xiaohongshu-skills](https://www.skills.sh/vivy-yi/xiaohongshu-skills) via skills.sh - 28.1K combined installs across 137 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [vivy-yi/xiaohongshu-skills](https://github.com/vivy-yi/xiaohongshu-skills) - 515 stars, no license file, branch main, last pushed 2026-01-23; 139 `SKILL.md` directories, one per skill, grouped into nine Chinese-named category folders under `skills/`, with docs and a Claude Code plugin manifest beside them

**Category:** Xiaohongshu (RED) content operations: short-video production, note writing and account workflows

**Quality Tier:** 🟡 Yellow - every sampled skill Passes all three auditors, but the repository ships no LICENSE file at all

This is a knowledge base rather than a toolkit. 139 `SKILL.md` files cover the operating manual of Xiaohongshu, the platform also called RED or Little Red Book: how to write a note that gets saved, how to shoot and cut a vertical video, how to pick products for live commerce, which metrics to read in which analytics tool, and what the platform's rules will penalise. Every file is prose. The clone holds markdown, one plugin manifest, a gitignore and nothing else, so nothing here executes and nothing here calls an API: the agent reads the skill and applies the method itself.

Read the language situation before deciding. The descriptions on skills.sh are English, which is how a query in English can route to the right file, but the bodies and most file names are Chinese, the README is Chinese, and the nine category folders are Chinese. An agent reading these files gets guidance written for a Chinese-market operator, with platform vocabulary that has no clean English equivalent. That is the point of the repository, and it is also why it does not overlap with an English social-media skill set.

## Installation

The README gives two routes, both starting from a clone. The first registers the repository as a Claude Code plugin marketplace and installs the single bundled plugin:

```bash
git clone https://github.com/vivy-yi/xiaohongshu-skills.git
cd xiaohongshu-skills
/plugin marketplace add vivy-yi/xiaohongshu-skills
/plugin install xiaohongshu-complete-skills@xiaohongshu-skills
```

The second is the development route: clone, and let Claude Code pick up `.claude-plugin/marketplace.json` from the checkout without registering it as a marketplace.

```bash
git clone https://github.com/vivy-yi/xiaohongshu-skills.git
cd xiaohongshu-skills
```

Neither route knows about Hermes. The complication for a profile install is depth: the skills sit two levels below `skills/`, one directory per skill inside a category directory, so a single recursive copy lands nine category folders rather than 139 skills. Copy the categories as they are, or pull named skills out flat:

```bash
git clone --depth 1 https://github.com/vivy-yi/xiaohongshu-skills.git /tmp/xiaohongshu-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
find /tmp/xiaohongshu-skills/skills -mindepth 2 -maxdepth 2 -type d \
  \( -name "short-video-production" -o -name "copywriting-skills" -o -name "cover-design" \
     -o -name "title-writing" -o -name "compliance" \) \
  -exec cp -r {} ~/.hermes/profiles/corpusiq/skills/ \;
```

That installs five skills flat, each with its own `SKILL.md`, which is what a Hermes router needs. Widen the `-name` list to take more, and keep the names in mind rather than the paths: the category folders are Chinese, so tab completion in a terminal is the only realistic way to browse them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| short-video-production | 777 | Shooting and cutting vertical video for RED: filming vlogs and tutorials, editing short-form clips and optimising for phone viewing. |
| copywriting-skills | 571 | The note body: captions that hold attention, brand voice for posts, product descriptions and recommendation copy. |
| image-editing | 436 | Preparing stills: filters and adjustments, image quality, carousel-ready frames and the visual consistency a photo post needs. |
| viral-creation | 349 | Building a post meant to break out of the existing follower base, and reverse-engineering the patterns behind posts that did. |
| jiaying-tool | 344 | Editing video in Jiaying: effects, transitions, subtitles and music, and the export settings for a RED upload. |
| traffic-acquisition | 342 | Pulling traffic in from outside the platform, recruiting followers beyond organic discovery and breaking a growth plateau. |
| content-performance-analysis | 336 | Reading one post's numbers to decide why it worked or failed, spotting underperformers and comparing formats against each other. |
| brand-operation | 334 | Running a brand account: official presence, brand community, and scaling engagement rather than just follower count. |
| product-selection | 324 | Choosing what to sell: items worth featuring in content, what to put in a live room, profitability and trending product research. |
| livestream-sales | 324 | Hosting a sales live stream: planning the session, product presentations for a live audience, viewer interaction and conversion rate. |
| graphic-content-creation | 318 | Image posts: carousel structure, visual tutorials and step guides, photos with text overlays and the storytelling order between frames. |
| meitu-xiuxiu | 301 | Photo retouching on mobile: enhancing visual quality, making product shots presentable and lifting image aesthetics with a phone editor. |
| compliance | 285 | Staying inside the platform rules: what counts as a violation and how to keep an account healthy while pushing reach. |
| photo-editing-tools | 284 | Comparing editing apps and choosing one for a given job, then improving the visual quality of the output. |
| cover-design | 281 | The thumbnail and first image: click-through rate, cover variants and A/B testing which one wins. |
| stable-design | 280 | Graphics from Chinese design templates: posters, banners, promotional material and business-oriented visuals. |
| excel-analytics | 276 | Manual analysis in a spreadsheet: tracking sheets, dashboards built by hand, and the spreadsheet skills a small operator needs. |
| private-domain | 274 | Moving followers off-platform to WeChat, building an offline community and keeping audience ownership when the algorithm changes. |
| topic-participation | 273 | Trending topics and hashtag challenges: joining conversations while they are live instead of after they cool. |
| xinhong-data | 272 | Deep account analytics: performance trends over time, influencer research, category growth and the strategic read on all three. |
| store-operations | 272 | Daily shop work: inventory, orders, fulfilment, shipping coordination and planning shop promotions. |

The remaining 116 indexed listings range from 153 to 269 installs.

## Why This Matters for Hermes Agents

General-purpose marketing advice fails on RED for a structural reason: the platform is a search and discovery engine where the cover image and the first line decide distribution, the note body carries the saved value, and the comment section is where reach compounds. A generic "post consistently and use hashtags" skill teaches none of that. These skills are written at the level of the actual mechanic, cover design and title writing and topic timing as separate files, each with the failure modes an operator hits.

The tool skills are the second useful layer. `jiaying-tool`, `meitu-xiuxiu`, `stable-design`, `xinhong-data`, `excel-analytics` and `photo-editing-tools` document specific Chinese-market tools rather than generic ones, which means an agent asked to plan a RED workflow can name the tool a Chinese operator would actually open instead of substituting whatever it knows from an English stack.

The commercial chain is covered end to end, and each link is its own skill: `product-selection` picks, `seeding-copywriting` seeds, `livestream-sales` sells live, `sales-funnel` maps the path, `store-operations` fulfils, `roi-analysis` checks whether it paid. That decomposition is why the suite is large; it is also why an agent can be pointed at one stage without loading a treatise on the whole business.

The caveat is freshness. This is a snapshot of platform practice frozen in January 2026, and RED's algorithm and rules move. Treat the skills as a structured method with a date on it, not as current policy.

## Usage

| You say | What happens |
|---|---|
| "Write me a RED note about a ceramic mug" | `copywriting-skills` drafts the body in note register, `title-writing` writes the opening line and `hashtag-optimization` picks the tags, in that order rather than as one blob. |
| "Why did this post get 200 views and that one 20,000" | `content-performance-analysis` compares the two against format, cover and timing, and `cover-design` checks whether the thumbnail is the variable. |
| "Plan a week of content for a skincare account" | `content-planning` and `content-calendar` lay out the week, `topic-participation` slots in anything trending, and `account-positioning` is checked first if the account has no clear lane. |
| "Is this product worth featuring in a live stream" | `product-selection` evaluates margin and demand, then `livestream-sales` structures the segment and the presentation order. |
| "How do I edit this clip for RED" | `short-video-production` sets the format and pacing and hands the edit to `jiaying-tool` for effects, subtitles and music. |
| "Can I say this in a note without getting flagged" | `compliance` checks the claim against the platform rules and `penalty-avoidance` covers the softer cases where wording, not the product, is the problem. |
| "Move my followers somewhere I control" | `private-domain` covers the WeChat handoff and the retention design that keeps the relationship after the follower leaves the app. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31. The category directory is Chinese, so the path is percent-encoded:

```bash
curl -sL -o /dev/null -w "%{http_code} short-video-production\n" \
  "https://raw.githubusercontent.com/vivy-yi/xiaohongshu-skills/main/skills/01-%E5%86%85%E5%AE%B9%E5%88%9B%E4%BD%9C/short-video-production/SKILL.md"
```

Expect `200`. After the copy lands, confirm the five named skills arrived flat and readable:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/short-video-production \
      ~/.hermes/profiles/corpusiq/skills/copywriting-skills \
      ~/.hermes/profiles/corpusiq/skills/cover-design | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/short-video-production/SKILL.md
```

The count should print 3, and the header should show `name: short-video-production` with an English `description:` that begins "Use when creating video content for Xiaohongshu". If the copy instead created nine Chinese-named category folders, the `find` above matched at the wrong depth and the router will not see the skills.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - all five Pass all three auditors, and the reason this guide is Yellow rather than Green is that the repository has no LICENSE file, so there is no stated grant to redistribute or embed the content - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| short-video-production | Pass | Pass | Pass |
| growth-hacking | Pass | Pass | Pass |
| content-matrix | Pass | Pass | Pass |
| crisis-management | Pass | Pass | Pass |
| account-weight | Pass | Pass | Pass |

The audit surface is as small as it gets. The tree holds 139 markdown files, one JSON plugin manifest and a gitignore; there is no script, no package manifest, no postinstall step and no network call anywhere in the checkout, so an install cannot execute anything. The manifest is worth one look because it is the only executable-looking file: it lists skill paths under `skills/` for the plugin loader and points at the repository root as its source, which is what makes the one-line plugin install work.

The real risk is not code, it is advice. Several skills describe platform-rule edges, penalty avoidance and traffic acquisition, and an agent following them will be optimising against a rule set it cannot verify. Keep a human on anything that touches account safety, and treat `compliance` as guidance that is nine months old rather than a current reading of platform policy.

## Limitations

- Snapshot data, verified 2026-10-31: 28,082 combined installs across 137 indexed listings; 515 GitHub stars; no license file; last pushed 2026-01-23. Counts drift over time.
- No LICENSE file, which is the one fact that should stop a commercial deployment. The repository is public and permissively indexed, but public is not licensed; embedding these skills in a product or redistributing the text has no stated grant.
- The index, the tree and the manifest disagree on size. 137 indexed listings, 139 directories in the clone, 139 stated in the README and 144 declared in `.claude-plugin/marketplace.json`. Nothing reconciles them, and the manifest number is the largest.
- The content is stale by design. Last pushed 2026-01-23, nine months before this snapshot, on a platform whose algorithm, rules and commerce features change faster than that. The method survives; specific thresholds and policy claims may not.
- The README's beginner path names skills that are not in the tree. `content-niche-selection`, `visual-storytelling`, `copywriting`, `basic-data-analysis` and `account-setup` all appear in the learning-path sections and none has a directory, so follow the file names, not the tutorial.
- The category folders are inconsistent. Two of the nine are both numbered `03`, one for engagement and one for analytics, and the folder names are Chinese, which breaks sorting, tab completion and any script that assumes ASCII paths.
- Install counts are not a ranking. The whole visible band runs from 777 down to 272, a factor of under three across 21 skills, which says more about how skills.sh aggregates a plugin install than about which skill is best.

## Related

- [WeRead Skills - Tencent WeChat Reading Agent Skill Setup](/hermes/skills/catalog/weread-skills-setup)
- [Ziniao Skills - ERP and Store Automation Setup](/hermes/skills/catalog/ziniao-open-skills-setup)
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install flat, not nested. Hermes routes on `SKILL.md` one level under the skills directory, so copy named skill folders up rather than the nine Chinese category folders down.
- Start with three files, not the catalog. `account-positioning` for the lane, `copywriting-skills` for the note, `cover-design` for the thumbnail; those three cover the loop a new account runs daily.
- Pair the content skills with the analytics ones. `content-performance-analysis` without `xinhong-data` is a post-mortem with no denominator, and `xinhong-data` without the analysis skill is a dashboard nobody reads.
- Read `compliance` before any monetisation work, not after. The commercial skills assume claims and formats that the platform rules constrain, and the ordering matters more than the depth.
- Keep your own copy provisioned through a normal distribution path. Since no license is declared, anything beyond internal use of these files needs a conversation with the maintainer first.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
