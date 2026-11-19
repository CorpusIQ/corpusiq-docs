---
title: "iArt Ad Video Skills - Ad Creative and Launch Films Setup"
description: "iart-ai/ad-video-skills: 5.6K combined installs across 3 listings; motion-graphics skills for ad creative, launch films, and testimonial clips."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iart-ad-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "advertising video", "motion graphics", "video production"]
---

# iArt Ad Video Skills - Setup Guide

**Source:** [iart-ai/ad-video-skills](https://www.skills.sh/iart-ai/ad-video-skills) via skills.sh - 5.6K combined installs across 3 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 23 stars, MIT licence, `main` branch, last pushed 2026-11-11. Each of the three skills is a `SKILL.md` with references under `skills/<name>/`, plus helper scripts under `scripts/`.
**Category:** Advertising and marketing video
**Quality Tier:** 🟡 Yellow - 1 Warn among 3 sampled skills (ad-creative-video); MIT licence.

iArt Ad Video Skills is a small set of three Claude Code skills from iart.ai for producing advertising and marketing video from motion-graphics templates. Each skill turns a prompt, or a CSV of variants, into on-brand video: ad creative with A/B-testable variants, high-energy launch films, and animated testimonial clips.

The skills run in Claude Code, Cursor, Codex, and other agents, and are part of a larger 19-pack open-source motion-skills collection from iart.ai, so you can install only the ad-video set.

## Installation

Install the whole pack with npx skills:

```bash
npx skills add iart-ai/ad-video-skills
```

Or add it as a Claude Code plugin marketplace:

```bash
/plugin marketplace add iart-ai/ad-video-skills
/plugin install ad-video-skills
```

The skills run in Claude Code, Cursor, Codex, and 40+ agents.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ad-creative-video | 1,941 | Build performance/UGC-style video ads and batch-produce variants from one template plus a CSV, exporting to multiple aspect ratios for A/B testing. |
| launch-video | 1,878 | Build high-energy product launch and hype films with a hook, tease, reveal, feature montage, and end-card CTA, cut to the beat. |
| testimonial-video | 1,828 | Turn customer reviews into animated quote clips with staggered line reveals, kinetic emphasis, star ratings, and an author block. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

For an agent generating ad or marketing video, the hard part is not the render, it is the structure: the hook that stops the scroll, the message matched to the CTA, and the batch discipline that turns one template into many on-brand variants for A/B testing. These three skills encode exactly that structure, so the agent produces a coherent ad rather than a generic animation.

The data-driven variant pattern is the standout: one template plus a CSV produces N message-matched ads, exported to every placement aspect ratio for Meta, TikTok, and Reels. Because each skill is a plain SKILL.md file with references, they load in any harness that reads skill files, including Hermes.

## Usage

| You say | What happens |
|---|---|
| "Make a UGC-style video ad from this CSV" | ad-creative-video generates hook variants matched to each row and exports per placement. |
| "Build a 30 second product launch video" | launch-video produces a beat-synced hook, tease, reveal, montage, and end-card arc. |
| "Turn this review into an animated testimonial" | testimonial-video renders quote typography, staggered reveals, and a star rating. |
| "Export this ad for Meta and TikTok" | ad-creative-video outputs the aspect ratios each placement needs. |
| "Make one quote video per review in this list" | testimonial-video templates one card across many quotes. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/iart-ai/ad-video-skills/main/skills/ad-creative-video/SKILL.md
```

Then install the pack:

```bash
npx skills add iart-ai/ad-video-skills
```

After install, ask your agent to build an ad or a launch film and check the next response changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ad-creative-video | Warn | Pass | Pass |
| launch-video | Pass | Pass | Pass |
| testimonial-video | Pass | Pass | Pass |

The sample covers all 3 indexed listings; one carries a Warn (ad-creative-video).

## Limitations

- Snapshot data, verified Nov 18, 2026: 5,647 combined installs across 3 indexed listings; 23 GitHub stars; MIT licence; last pushed 2026-11-11. Counts drift over time.
- The pack is small: three skills, all motion-graphics prompts, with no general video editing or capture tooling.
- The skills assume you bring a motion-graphics template or a brand kit; they structure and batch, they do not render footage from nothing.
- They are one pack of a 19-pack iart.ai collection, so adjacent needs live in sibling repos rather than here.

## Related

- [Explainer Video Skills - Script to Render Setup](/hermes/skills/catalog/explainer-video-skills-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with ad-creative-video for A/B testing; its one-template-plus-CSV loop is the highest-leverage pattern here.
- Feed a brand kit or template along with the CSV so the variants stay on-brand rather than generic.
- Export each ad in the placement aspect ratios (9:16, 4:5, 1:1) up front to avoid a re-render pass.
- Use launch-video when you need a single hero film; it optimizes for the arc, not for batch variation.
- Only install this pack if ads are the goal; sibling iart.ai packs cover explainer, map, and motion-design video.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
