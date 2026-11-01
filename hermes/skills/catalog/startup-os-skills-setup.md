---
title: "Startup OS Skills - Sales, Product and Video Pack"
description: "ncklrs/startup-os-skills: 12.9K combined installs. 54 startup skills for sales, marketing, product, customer success and Remotion video."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/startup-os-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "startup gtm", "sales", "product management"]
---

# Startup OS Skills - Setup Guide

**Source:** [ncklrs/startup-os-skills](https://www.skills.sh/ncklrs/startup-os-skills) via skills.sh - 12.9K combined installs across 53 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [ncklrs/startup-os-skills](https://github.com/ncklrs/startup-os-skills) - 53 stars, no licence file at the repository root, branch main, last pushed 2026-02-26; 54 `SKILL.md` files, one per directory directly under `skills/` with no category nesting, and a README that is the only documentation

**Category:** Go-to-market and product work for startup operators: sales, marketing, product management, customer success, and Remotion video production

**Quality Tier:** 🟡 Yellow - all three sampled verdicts are a Pass on Gen Agent Trust Hub, Socket and Snyk, but the repository ships no LICENSE file at its root even though the README carries an MIT badge linking one

The README describes 54 skills in six groups: sales (9, parent `sales-leader`), marketing (14, parent `marketing-strategist`), product (9, parent `product-leader`), customer success (6, parent `cs-strategist`), video production (13, parent `remotion-asset-coordinator`) and engineering (3, no parent). Each skill is a role rather than a topic: `account-executive`, `pricing-strategist`, `qbr-facilitator`, `renewal-manager`. The bodies follow one shape throughout, a short philosophy, then named frameworks and comparison tables, so the value is in the artefact a skill hands back (a qualification scheme, a proposal structure, a storyboard) rather than in prose.

The video group is the exception to the role pattern, because it is a pipeline. `vsl-storyboard-writer` produces a storyboard written for `motion-designer`, which produces a scene-by-scene specification with frame timing and audio, and the `remotion-*` skills turn that specification into animation configuration, composition ordering, components, render settings and a structured review. `create-video-start` is the orchestrator that chains the whole set from a single brief. Each of those skills states what is in scope and what belongs to a sibling, which keeps an agent from rewriting components when it was asked to fix timing.

## Installation

The README documents the skills CLI and nothing else. It also shows the list form, which is worth running first on a pack this size:

```bash
npx skills add ncklrs/startup-os-skills --list
npx skills add ncklrs/startup-os-skills
```

The CLI drops the selected skills into the agent you name (the README mentions Claude Code, Cursor and Windsurf) and prompts for a selection. For a Hermes profile the equivalent is a clone and copy, which is our route rather than a documented one:

```bash
git clone --depth 1 https://github.com/ncklrs/startup-os-skills.git /tmp/startup-os-skills
cp -r /tmp/startup-os-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

There is no plugin manifest, no package file and nothing to build: the copy is the install. Selecting a subset is the sensible default, since 54 skills add a lot of trigger surface to a profile and the video pipeline alone accounts for a quarter of them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| community-builder | 655 | Community-led growth: platform choice, member onboarding, engagement rituals, ambassador programs, moderation and health metrics. |
| motion-designer | 599 | Scene-by-scene video specifications for Remotion, with frame timing, audio layers and sound effect placement. |
| proposal-writer | 596 | Sales proposals, executive summaries, ROI cases, pricing presentations, SOWs and RFP responses structured on the CLOSE framework. |
| website-copy-specialist | 559 | Homepage, feature, pricing, comparison and use case copy, organised by the clarity hierarchy and message-market match. |
| vsl-storyboard-writer | 478 | Video sales letter and product video storyboards, with a formula chosen by length (Hook-CTA, PAS, AIDA, VSL Classic, Explainer). |
| remotion-animation | 445 | Spring configs, interpolation ranges, easing curves and stagger timing for Remotion, with no component code. |
| seo-content-strategist | 350 | Keyword research, content clusters, pillar pages, on-page and technical SEO, link building, programmatic pages and content refresh. |
| sales-leader | 331 | Sales leadership across strategy, hiring, pipeline management, enterprise deals, demos, proposals and negotiation, as the parent for the sales group. |
| sales-strategist | 328 | Sales process design, qualification framework choice (MEDDIC, BANT, SPICED, SCOTSMAN, CHAMP), territory planning, quotas and comp design. |
| gtm-copywriter | 328 | Marketing email, sequences, newsletters, blog posts, LinkedIn and X content, with a voice spectrum per channel. |
| marketing-strategist | 327 | Marketing leadership across GTM, product marketing, content, demand generation, community, events, PR, partnerships and pricing. |
| sales-negotiator | 281 | Negotiation preparation, BATNA development, discount handling, multi-stakeholder procurement and closing. |
| growth-product-manager | 269 | Growth loops, activation and onboarding, retention systems, referral mechanics, PLG motion choice and north star metrics. |
| product-leader | 261 | Product leadership across vision, roadmap, discovery, growth, platform strategy, analytics and launch, as the parent for the product group. |
| product-manager | 254 | Day-to-day PM work: roadmaps, RICE and ICE prioritisation, stakeholder management, sprint and release planning, OKRs and technical debt. |
| sales-ops-analyst | 243 | CRM architecture, pipeline analytics, dashboards, lead routing, territory design, commission logic and forecasting models. |
| remotion-video-reviewer | 239 | Structured review of a Remotion implementation against its specification, returning a prioritised revision list with compliance scores. |
| demo-specialist | 227 | Demo structure, stakeholder-specific demo variants, objection handling during a live demo and post-demo follow-up. |
| product-strategist | 224 | Product vision, product-market fit assessment, TAM/SAM/SOM sizing, competitive positioning and build versus buy decisions. |
| customer-lifecycle-marketer | 224 | Onboarding programs, expansion and upsell, churn prevention, referral programs and lifecycle email segmentation. |

The remaining 33 indexed listings range from 138 to 223 installs.

## Why This Matters for Hermes Agents

A role inventory is more useful to an agent than a topic list, because the first decision on any request is which specialist should answer it. This pack makes that decision explicit: `sales-leader` names eight sales skills, `marketing-strategist` names thirteen, `product-leader` names eight, and each of those skills is written to be loaded on its own. An agent can therefore route to `discovery-caller` for a call script instead of improvising a generic sales answer, and the answer arrives with a named framework attached.

The frameworks are the part that survives review. MEDDIC, BANT and SPICED are compared in one table in `sales-strategist`, the CLOSE section structure sits in `proposal-writer`, the clarity hierarchy and specificity ladder sit in `website-copy-specialist`, and the 12 principles of animation head up `motion-designer`. When a deliverable is challenged, the agent can name the framework it followed rather than defending a preference.

The video pipeline shows what staged skills can do that one large skill cannot. Each stage declares its inputs and outputs, so the storyboard format, the specification format and the animation config are separate artefacts that can be reviewed and corrected at the boundary. That is the same decomposition a build pipeline uses, and it means a bad frame timing gets fixed in the spec instead of being patched in rendered code.

For an operator running a small team, the coverage is the argument: one pack covers a discovery call, a proposal, a pricing page, a launch sequence, a churn review and a product video, all of which are normally six different tools or six different prompts.

## Usage

| You say | What happens |
|---|---|
| "Help me write a discovery call script for a 40 seat prospect" | `discovery-caller` applies a discovery framework, builds the question set and names the pain to qualify on. |
| "Our mid-market win rate is falling" | `sales-strategist` picks the qualification framework that fits the ACV band, then `competitive-strategist` builds the battlecard for the deals being lost. |
| "Draft the proposal for this 60K annual deal" | `proposal-writer` lays out the pyramid, executive summary and pricing presentation, and `sales-negotiator` prepares the discount conversation. |
| "Write the launch post and the announcement email" | `gtm-copywriter` selects a voice per channel and drafts both, with `senior-product-marketer` supplying the positioning. |
| "Make a 45 second product teaser" | `vsl-storyboard-writer` writes the storyboard for that length, `motion-designer` turns it into a timed specification, and the `remotion-*` skills produce the config and composition. |
| "Churn is up and I do not know which accounts to call" | `customer-health-analyst` builds the health score and `cs-strategist` sets the tiering and the intervention for the at-risk segment. |
| "Review this PR before I merge it" | `codex-review` hands the diff to the OpenAI Codex CLI for a second opinion, then reports the findings back. |

## Verification

The raw path for `community-builder` returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} community-builder\n" \
  https://raw.githubusercontent.com/ncklrs/startup-os-skills/main/skills/community-builder/SKILL.md
```

Expect `200`. After the clone, confirm that all 54 directories arrived and that each one carries a skill file:

```bash
ls /tmp/startup-os-skills/skills | wc -l
find /tmp/startup-os-skills/skills -name SKILL.md | wc -l
head -4 /tmp/startup-os-skills/skills/community-builder/SKILL.md
```

Both counts should print 54. The header should show `name: community-builder` and a `description:` line before the closing frontmatter. Several skills tell the agent to apply guidance from a `rules/` directory, so list one skill directory in full before assuming the pack is self-contained.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| community-builder | Pass | Pass | Pass |
| motion-designer | Pass | Pass | Pass |
| proposal-writer | Pass | Pass | Pass |

All three sampled verdicts are clean and the pack carries no Snyk codes. The repository's visible top level is a README and a `skills/` directory, with no package manifest, no dependency lockfile and no build step, so the review question is what the agent is instructed to do rather than what executes on install.

Two behaviours extend the trust boundary past the markdown and are worth naming. `codex-review` delegates a code review to the OpenAI Codex CLI, which means the diff leaves the local context for a third-party tool, so decide per repository whether that is acceptable. The `remotion-*` skills generate TypeScript and render configuration that is later executed by Node and the Remotion renderer, which brings a dependency tree the pack does not pin; treat generated config as reviewable code rather than inert output.

The licence is a separate issue rather than a security one. The README carries an MIT badge pointing at a LICENSE file that is not in the repository, so the grant is unverifiable; keep the clone local and do not vendor these skills into a shipped product until that file appears.

## Limitations

- Snapshot data, verified 2026-11-01: 12,860 combined installs across 53 indexed listings; 53 GitHub stars; no LICENSE at the repository root; last pushed 2026-02-26. Counts drift over time.
- The index lists 53 skills while the tree holds 54 `SKILL.md` directories. The extra directory is `codex-review`, which has no indexed listing, so it installs from the clone but has no install count behind it.
- The entire pack sits between 138 and 655 installs. That is a narrow band for 54 skills, so index order says little about quality and the top row is only five times the bottom.
- Several skill bodies instruct the agent to apply guidance from a `rules/` directory, while the tree listing records only one `SKILL.md` per skill. Confirm those directories exist in the clone before relying on the referenced rules.
- Last pushed 2026-02-26, about eight months before this snapshot. The sales and marketing frameworks age slowly, but the Remotion skills describe a fast moving library and their command and config advice may be behind the current release.
- There is no licence file at the root despite an MIT badge in the README, which leaves redistribution rights unresolved.

## Related

- [Slavingia Skills - Minimalist Entrepreneur Business Suite](/hermes/skills/catalog/slavingia-skills-setup)
- [Agentix CEO Skill - AI Worker Team Orchestration Setup](/hermes/skills/catalog/agentix-ceo-skill-setup)
- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start at the parent skill and let it route. Asking `sales-leader` which specialist fits the deal is faster than guessing between `sales-strategist`, `account-executive` and `discovery-caller`.
- Run `npx skills add ... --list` before installing. Fifty four skills is a large trigger surface, and a profile that only sells should not be loading the Remotion pipeline.
- Ask for the artefact by name. "Give me the MEDDIC qualification for this account" or "show me the CLOSE structure" returns the framework rather than a summary of it.
- Use `create-video-start` for the video group instead of calling the stages by hand. The individual skills assume the previous stage's output format, and the orchestrator enforces that order.
- Keep `codex-review` out of profiles that handle private code unless you have decided the diff may leave the host, since that skill's whole job is handing code to an external CLI.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
