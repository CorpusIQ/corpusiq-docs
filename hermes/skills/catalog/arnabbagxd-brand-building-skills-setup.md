---
title: "Brand Building Skills - Brand Strategy Suite Setup"
description: "arnabbagxd/brand-building-skills: 48.6K combined installs. 29 MIT brand skills covering strategy, naming, identity, voice, messaging and launch."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/arnabbagxd-brand-building-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "brand strategy", "marketing"]
---

# Brand Building Skills - Setup Guide

**Source:** [arnabbagxd/brand-building-skills](https://www.skills.sh/arnabbagxd/brand-building-skills) via skills.sh - 48.6K combined installs across 29 indexed listings; first seen Jun 11, 2026
**GitHub:** [arnabbagxd/Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills) (787 stars; MIT, LICENSE file in repo; pushed 2026-06-13; layout `skills/<name>/SKILL.md` for all 29 skills, optional `evals/evals.json` in 4 of them, plus `validate-skills.sh`, `VERSIONS.md` and `.claude-plugin/marketplace.json`)
**Category:** Marketing / Brand Strategy
**Quality Tier:** 🟡 Trusted (MIT LICENSE in-repo and Gen Agent Trust Hub, Socket and Snyk all Pass on the four sampled skills; held below Production by single-maintainer activity, no push since 2026-06-13 and eval files on only 4 of 29 skills)

Brand Building Skills is a 29-skill suite from a single maintainer, Arnab Bag, aimed at the work an agency or in-house brand team does between the first client call and the launch post. It is pure markdown, MIT licensed, and organised as a dependency graph rather than a bag of prompts: `brand-context` captures the brand DNA into one file, and every other skill opens by checking that file before it asks a question.

The suite covers the full arc a brand project actually follows - strategy, naming, positioning, identity, voice, messaging, guidelines, audit, rebrand, launch - and then reaches into the channels that spend the money: Meta and Google ads, email, WhatsApp, influencer, UGC, ASO and two D2C and B2B marketing playbooks. That breadth is unusual for a repo this small, and it is the reason it holds 29 indexed listings at 1,517 to 2,216 installs each.

## Installation

```bash
npx skills add arnabbagxd/brand-building-skills
```

```bash
# Optional: run the repo's own skill auditor against a clone
git clone https://github.com/arnabbagxd/Brand-building-skills.git
cd Brand-building-skills
bash validate-skills.sh
```

There is no CLI, no API key and no runtime beyond the agent. The README states that skills install to `.agents/skills/` following the Agent Skills specification, and that the skill set is one plugin entry in the bundled `.claude-plugin/marketplace.json` if you prefer to wire it into Claude Code as a marketplace.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| brand-naming | 2,216 | Full naming workflow: generate names with strategic rationale, or evaluate, rank and score options you already have; auto-detects which mode to run |
| brand-identity | 2,059 | Visual identity brief for a designer: logo direction, colour palette, typography, imagery style and design system foundations |
| personal-brand | 1,796 | Personal brand strategy for founders, executives and creators: positioning, point of view, platform strategy, content pillars and a 90-day plan |
| brand-positioning | 1,790 | Market position: competitive landscape map, positioning territory, positioning statement and proof points |
| brand-voice | 1,763 | Verbal identity: tone, voice qualities, vocabulary, writing style rules and channel adaptations |
| brand-strategy | 1,746 | Agency strategy workflow: structured client questionnaire, then a full brand strategy report |
| brand-guidelines | 1,746 | Brand standards document: logo usage, colour, typography, voice, messaging and application rules |
| brand-context | 1,696 | Foundation file at `.agents/brand-context.md` holding identity, audience, positioning, values and voice; every other skill reads it first |
| brand-messaging | 1,688 | Messaging hierarchy: taglines, value proposition, key messages and proof points per audience |
| target-audience | 1,680 | ICP and personas: psychographics, behavioural patterns and audience language analysis |
| brand-packaging | 1,672 | Packaging design brief: structure, visual direction, hierarchy, materials and unboxing experience |
| competitor-branding | 1,668 | Competitor brand analysis across identity, messaging, positioning, voice and visual style, to find gaps |
| brand-audit | 1,655 | Six-dimension brand health check: positioning clarity, identity, messaging consistency, voice, audience alignment and differentiation |
| meta-ads | 1,652 | Facebook and Instagram advertising: campaign structure, core and lookalike audiences, creative, pixel, retargeting, budget scaling and ROAS |
| brand-story | 1,650 | Origin story, founder narrative and why-we-exist statement in long, short and one-liner versions |
| whatsapp-marketing | 1,633 | WhatsApp Business setup, broadcast campaigns, automated flows and conversational commerce, weighted to India and emerging markets |
| brand-architecture | 1,619 | Branded house, house of brands, endorsed and hybrid models, plus the sub-brand hierarchy and naming system |
| b2b-brand-marketing | 1,614 | B2B brand strategy: buying committee messaging, thought leadership, LinkedIn presence, trust signals and an ABM brand layer |
| brand-launch | 1,602 | Launch plan: pre-launch assets, launch day sequence, content plan and post-launch momentum |

The remaining 10 indexed listings range from 1,517 to 1,594 installs and sit just under the table threshold: ugc-strategy 1,594, rebranding 1,591, brand-manifesto 1,582, d2c-marketing 1,576, google-ads 1,560, brand-measurement 1,559, brand-partnerships 1,550, email-marketing 1,550, influencer-marketing 1,544 and aso 1,517. They are not filler - rebranding is the step after brand-audit, and d2c-marketing, google-ads, email-marketing and influencer-marketing are the channel playbooks the marketing half of the suite runs on.

## Why This Matters for Hermes Agents

Brand work fails in agent sessions in a specific way: the model invents a positioning statement and a palette in the first turn, then contradicts both four turns later because nothing was written down. This suite fixes the memory problem structurally. `brand-context` is a mandatory first read for the other 28 skills, and it persists to `.agents/brand-context.md`, so a long session stays anchored to one brief instead of drifting.

The second gain is that the output is briefed, not just descriptive. `brand-identity` produces a designer brief with logo direction, palette and typography rationale; `brand-packaging` produces a packaging brief with structure and materials; `brand-guidelines` assembles logo, colour, type, voice and messaging rules into one standards document. Those are the artefacts a human contractor can act on, which is a much better handoff than a chat transcript.

The third is sequencing. The repo ships the graph explicitly: brand-audit leads to rebranding leads to brand-launch; target-audience feeds brand-messaging, brand-voice and brand-positioning; competitor-branding feeds brand-positioning and brand-strategy. An agent that reads those edges can plan an eleven-step engagement and know which step is blocked on which input, rather than generating eleven unrelated documents.

Finally, the channel skills close the loop between brand and spend. Once positioning and messaging exist, meta-ads, google-ads, email-marketing and whatsapp-marketing write campaign structure against that messaging instead of inventing a second brand voice for ads. For a small team that is the difference between a brand document nobody uses and one that shows up in the ad account.

## Usage

| You say | What happens |
|---|---|
| "Set brand context for our new coffee subscription, urban commuters, premium" | brand-context collects the brief and writes `.agents/brand-context.md`; every later skill reads it instead of re-asking |
| "Help me name this brand, here is the brief" | brand-naming runs the generation workflow with strategic rationale per name; paste existing candidates instead and it switches to scoring mode |
| "Our brand feels outdated, where do we start?" | brand-audit scores the six dimensions first, then rebranding takes over with diagnosis, equity audit and rollout plan |
| "Write the About page and a one-line pitch" | brand-story produces the long, short and one-liner versions from one narrative spine |
| "We are adding a second product line under the master brand" | brand-architecture picks a branded house or house of brands model and defines the naming system for the sub-brand |
| "Which channel should we test first for a DTC launch?" | d2c-marketing frames unit economics and channel fit, then meta-ads or email-marketing writes the execution plan |
| "Brief our designer on the new identity" | brand-identity emits a visual identity brief with logo direction, palette, typography and imagery direction |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -i brand
```

Read the foundation skill and two of the load-bearing skills before installing. All four URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/arnabbagxd/Brand-building-skills/main/README.md
curl -sL https://raw.githubusercontent.com/arnabbagxd/Brand-building-skills/main/skills/brand-context/SKILL.md
curl -sL https://raw.githubusercontent.com/arnabbagxd/Brand-building-skills/main/skills/brand-naming/SKILL.md
curl -sL https://raw.githubusercontent.com/arnabbagxd/Brand-building-skills/main/skills/brand-strategy/SKILL.md
```

Check the context file actually lands after the first skill runs:

```bash
ls -l .agents/brand-context.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| brand-naming | Pass | Pass | Pass |
| brand-identity | Pass | Pass | Pass |
| brand-audit | Pass | Pass | Pass |
| brand-context | Pass | Pass | Pass |

No sampled verdict reports malware, injection or data exfiltration, and that is consistent with what is in the files: 29 SKILL.md documents, zero executable scripts, and no network calls. The only write the suite performs is `brand-context` creating `.agents/brand-context.md` (and reading `.claude/brand-context.md` if that is where an existing context lives); every other skill is a reader of that file plus a prompt. None of the 29 files declares an `allowed-tools` block, so the host agent's own tool policy governs what the skills can reach - which means the blast radius depends on how you have scoped the session, not on the repo. Nothing here touches credentials, and no skill shells out to a paid API.

## Limitations

- The suite is editable markdown with no test harness. Four skills carry `evals/evals.json` (brand-audit, brand-naming, brand-positioning, brand-strategy); the other 25 are unexercised prompt text, so quality varies by skill.
- Single maintainer, and the repo has not been pushed since 2026-06-13. `VERSIONS.md` stops at 1.2.0, dated 2026-06-11, so there is no release cadence to rely on for fixes.
- The shared state is project-local: `.agents/brand-context.md` in the working directory. Run the skills from a different directory and the foundation file is not found, and the questioning starts again.
- Six of the 29 skills (meta-ads, google-ads, email-marketing, whatsapp-marketing, influencer-marketing, aso) are channel playbooks rather than brand work. They are useful, but the install counts make them look like peers of brand-strategy when they solve a different problem.
- The channel skills overlap by design: d2c-marketing, meta-ads, google-ads and email-marketing each describe parts of the same acquisition plan, so an agent asked for "a launch plan" can produce three competing versions.
- Snapshot data, verified Oct 26, 2026: 48,568 combined installs across 29 indexed listings; 787 GitHub stars; MIT; last pushed 2026-06-13. Counts drift over time, and the live skills.sh listing already shows slightly different per-skill figures.

## Related

- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup) - the execution half of the same job: ad copy, SEO and paid channel craft once positioning exists.
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - turns the messaging hierarchy from brand-messaging into a publishing plan.
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup) - a broader marketing operating layer that can sit above these brand skills.
- [OPC Skills - Solopreneur Toolkit (SEO, Reddit, Branding, Launch) Setup](/hermes/skills/catalog/opc-skills-setup) - a lighter solo-operator alternative when a 29-skill suite is more than the job needs.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run brand-context in the first turn of every brand session. Without `.agents/brand-context.md` the other skills open with their own questionnaires and you will answer the same four questions repeatedly.
- Paste your shortlist into brand-naming rather than asking for ideas. The skill auto-detects the evaluation branch and scores the names you already like against criteria, which is faster than another round of generation.
- Ask for one deliverable per session: audit, then rebranding, then launch. Chaining all 29 skills in a single turn produces shallow documents because each one waits on the previous output.
- Run brand-strategy before brand-identity on client work, so the visual brief inherits a positioning instead of inventing one the strategy then has to contradict.
- Keep the generated documents in the repo next to `.agents/brand-context.md`. brand-guidelines and brand-audit both look for earlier work in the session, and a committed folder beats re-deriving it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
