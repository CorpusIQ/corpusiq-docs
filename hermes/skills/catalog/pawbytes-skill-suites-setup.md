---
title: "Pawbytes Skill Suites - Marketing and Creative Agents"
description: "pawbytes/skill-suites: 10.1K combined installs across 76 listings for marketing strategy, video repurposing and growth execution"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pawbytes-skill-suites-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "social media", "video"]
---

# Pawbytes Skill Suites - Setup Guide

**Source:** [pawbytes/skill-suites](https://www.skills.sh/pawbytes/skill-suites) via skills.sh - 10.1K combined installs across 76 indexed listings; first seen Apr 2, 2026 (Nov 12, 2026 sweep)
**GitHub:** 118 stars, MIT license, `main` branch, last pushed 2026-11-10, 79 `SKILL.md` files under `src/<suite>/`, with a unified `marketplace.json` manifest
**Category:** Marketing and creative operations: strategy frameworks, social and content production, video repurposing, product development and webinar production
**Quality Tier:** 🟡 Established - a well-organised multi-suite pack with a router design and a manual install path, held back by a small star count and Snyk Warns on the social and planning skills.

This pack is organised as suites rather than as a flat list of skills, and each suite ships a coordinator agent that routes work to its specialists. The marketing suite is the largest at 23 skills, led by a master router that decides which specialist handles a request so the user does not have to name one. The creative suite adds persistent personas with memory across sessions, including a creative director who coordinates a designer, a strategist and a video producer. A product development suite covers discovery through roadmap, a webinar suite covers research to production, and a small utility suite adds HTML decks and release automation.

The practical difference between this and a folder of prompts is the routing. A request like "plan next quarter's campaign" lands on the marketing router, which then pulls the strategy framework, the channel plan and the measurement approach in a defined order. Whether the routing works is visible in the trace: the agent names the specialist it chose, and the wrong choice is easy to spot.

The video skills are the ones drawing the most installs. Clip extraction for a multi-platform repurpose, short-form pipelines for Reels and TikTok, and a long-form pipeline for YouTube are the top three listings in the pack, each between 177 and 193 installs. Content, email, SEO, influencer and behavioural-science skills sit just behind them.

Installation offers both an interactive CLI path and a manual one, and both end in the same place: folders inside the agent's skills directory, with a setup skill to configure each suite.

## Installation

The README's primary route is the skills CLI, which lets you select modules:

```bash
npx skills add pawbytes/skill-suites
```

For a manual install, clone the repository and copy the suite prefixes you want:

```bash
git clone https://github.com/pawbytes/skill-suites.git
cd skill-suites
cp -r src/marketing/paw-mkt-* ~/.claude/skills/
cp -r src/creative/paw-cra-* ~/.claude/skills/
cp -r src/prodig/paw-ps-* ~/.claude/skills/
cp -r src/webinar/paw-wbc-* ~/.claude/skills/
```

Each suite carries its own setup skill for one-time configuration, and the README's manual guide lists the setup step for each module. Copying folders without running setup leaves the coordinator without the configuration it expects.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| paw-cra-video-clips | 193 | Video repurposing: extracting clips from long footage for multi-platform use. |
| paw-cra-video-shortform | 186 | Short-form pipelines for Reels, TikTok and Shorts, from concept to export. |
| paw-mkt-social | 182 | Organic social strategy, calendars, hashtag research and posting plans. |
| paw-mkt-sostac | 179 | The six-phase SOSTAC planning framework, from situation analysis to control. |
| paw-mkt-dashboard | 179 | SvelteKit and sql.js marketing dashboards with a generated interface. |
| paw-mkt-seo | 178 | Technical SEO audits, keyword strategy, schema markup and generative engine visibility. |
| paw-mkt-psychology | 178 | Behavioural science applied to copy: cognitive bias, loss aversion, social proof. |
| paw-mkt-influencer | 178 | Creator partnerships, ambassadors, UGC programs and sponsorship terms. |
| paw-cra-video-longform | 177 | Long-form and episodic video production for YouTube and web. |
| paw-mkt-video | 176 | Video strategy, scripting and optimisation across YouTube, TikTok and Reels. |
| paw-mkt-guerrilla | 176 | Unconventional growth tactics and viral campaign design. |
| paw-mkt-product-context | 175 | Positioning documents: audience, differentiation and message hierarchy. |
| paw-mkt-email | 175 | Email sequences, newsletters, automation and deliverability. |
| paw-mkt-content | 175 | Blog posts, whitepapers, case studies and editorial calendars. |

The remaining 62 indexed listings range from 3 to 174 installs.

The pack ships 59 skills across five suites in the README's own count, and the index lists 76 listings, so the two do not match one to one. The extra listings carry names that are not in the current `src/` tree, which is the usual sign of modules that were renamed or split after the first publish.

## Why This Matters for Hermes Agents

Marketing work is where agents produce the most volume and the least judgment. A model asked for a content calendar will produce one, and it will be generic, because nothing in the prompt says which market, which stage or which constraint applies. A framework forces the missing questions to be asked first. SOSTAC does that for a plan, a positioning document does it for messaging, and a behavioural-science pass does it for the copy itself.

The video skills matter for a different reason. Repurposing one recording into clips, shorts and a long-form edit is mechanical work with specific tools attached, and it is the kind of task where an agent with a written pipeline finishes and an agent without one produces a script that describes the work instead of doing it.

The router design is the part worth copying into your own stack. One coordinator that knows which specialist exists and what each one needs is more reliable than asking the user to pick the right skill from a list of twenty. It also degrades better: when the router picks wrong, the trace shows it, and the fix is a line in the router rather than a rewrite.

For an operator, the honest measure is whether the output saves a step or adds a review. Copy that needs a rewrite has negative value. A plan that arrives with its assumptions named gets edited instead of regenerated, and that is the difference these frameworks buy.

## Usage

| You say | What happens |
|---|---|
| "Plan next quarter's marketing" | Runs the SOSTAC sequence and returns a plan with situation, objectives, strategy, tactics, action and control. |
| "Turn this webinar recording into clips and shorts" | Applies the clip extraction pipeline, then the short-form pipeline for each platform. |
| "Write the positioning doc for this product" | Produces audience, differentiation and message hierarchy before any copy is drafted. |
| "Audit the site's SEO and tell me what to fix first" | Runs the technical audit plus the keyword and schema pass, ordered by impact. |
| "Build a campaign dashboard" | Generates a SvelteKit and sql.js dashboard wired to the campaign data. |
| "Draft the email welcome sequence" | Writes the sequence, then applies the deliverability rules before returning it. |
| "Which creator should we sponsor?" | Applies the influencer skill's fit and terms framework rather than a popularity ranking. |

## Verification

The marketing skills live under `src/marketing/` and the creative skills under `src/creative/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/pawbytes/skill-suites/main/src/marketing/paw-mkt-seo/SKILL.md | head -6
```

Check the creative side too, since the two trees are installed by different copies:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/pawbytes/skill-suites/main/src/creative/paw-cra-video-clips/SKILL.md
```

After installing, confirm the router arrived with its specialists. A lone `paw-mkt-agent-agency` folder with no `paw-mkt-*` siblings installs cleanly and cannot route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| paw-cra-video-clips | Pass | Pass | Pass |
| paw-cra-video-shortform | Pass | Pass | Pass |
| paw-mkt-social | Pass | Pass | Warn |
| paw-mkt-sostac | Pass | Pass | Warn |

The two Warns sit on skills that produce posts and plans, which is where an agent can act publicly on your behalf. The scanners flag the pattern of tools that post, schedule or call platform APIs. The control is the account: a social skill wired to a personal account can publish, and nothing in the skill stops it.

The video and dashboard skills call local tooling plus a model. They pass clean, and the main risk with them is cost: rendering and model calls in a loop add up quietly.

## Limitations

- Snapshot data, verified 2026-11-12: 10,105 combined installs across 76 indexed listings; 118 GitHub stars; MIT license; last pushed 2026-11-10. Counts drift over time.
- The README counts 59 skills across five suites while the index lists 76 listings. Some indexed names have no matching folder in the current `src/` tree.
- Every suite needs its setup skill to run before the coordinator works. Copying folders alone is the most common partial install.
- The creative suite's personas carry memory across sessions, which means behaviour depends on state that accumulates rather than only on the current prompt.
- Social and email skills can publish and send. Nothing in the pack enforces an approval step, so gate it in the agent or in the account.
- The pack is a product-development project as much as a skill library, and the 14-skill product suite is less exercised than the marketing suite: its listings sit well below the top rows in install count.

## Related

- [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the router and its specialists together. The router is the entry point, and a partial install gives you an agent that describes the right process and then cannot run it.
- Ask for the framework by name when you want a plan rather than ideas: "run SOSTAC" produces a different output from "plan the quarter", and you want the first.
- Keep the positioning skill ahead of the copy skills. Every content skill produces better output when the audience and message hierarchy have already been written down.
- Run the video pipelines on one recording end to end before batch processing. The clip extraction stage is where the timing conventions get set, and a batch run repeats a wrong choice at scale.
- Put a human approval step between the social skill and the publishing account. The pack is good at drafting and has no opinion about whether today is the right day to post.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
