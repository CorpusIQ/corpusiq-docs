---
title: "MiniMax H3 Skills - AI Video Prompt Writing & Generation"
description: Setup guide for the MiniMax H3 skill bundle from the official MiniMax org - portable h3-prompt-writing (agent-agnostic, 7,857 installs) plus 8 MiniMax Hub canvas video generators. 15.6K+ combined installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/minimax-h3-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-14"
tags: ["hermes skill", "agent skill", "video generation", "skill setup"]
---

# MiniMax H3 Skills - Setup Guide

**Source:** [minimax-ai/minimax-h3](https://github.com/minimax-ai/minimax-h3) (15,683+ combined installs on skills.sh)
**Category:** Video Generation / AI Content
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published)

MiniMax H3 is MiniMax's flagship video generation model ([Hailuo](https://hailuoai.video)). The official MiniMax org publishes this repo (8,630★, 599 forks, created Jul 30 2026) with nine bundled agent skills: one portable prompt-writing skill (`h3-prompt-writing`) and eight style-specific generators built for the MiniMax Hub canvas workflow.

---

## Installation

```bash
# Portable prompt-writing skill (recommended - works in any agent harness)
npx skills add minimax-ai/minimax-h3 --skill h3-prompt-writing

# Alternative URL form used in the README
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing

# MiniMax Hub canvas skills (require the MiniMax Hub runtime)
npx skills add minimax-ai/minimax-h3 --skill brand-promo-video-generator
npx skills add minimax-ai/minimax-h3 --skill music-video-subtitle-generator
npx skills add minimax-ai/minimax-h3 --skill handdrawn-live-video-generator
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Nothing for h3-prompt-writing** | Pure Markdown + local reference files - no API calls, no keys, no runtime |
| **MiniMax account** | [platform.minimax.io](https://platform.minimax.io) for H3 API access (generation only) |
| **MiniMax Hub** | The 8 canvas skills target the Hub's `hub_generate_video` / `hub_generate_image` canvas workflow |
| **Hermes Agent** | Any version that reads SKILL.md and local files |

## Capabilities

### h3-prompt-writing (portable - 7,857 installs)

Agent Skills format (name/description/compatibility frontmatter). Explicitly portable: "no external API calls, MiniMax Hub tools, or proprietary runtime required." Ships two prompt guides under `references/`: `base-en.txt` (text/keyframe modes) and `ref-en.txt` (full-reference Ref2VA mode).

| Mode | What it does |
|---|---|
| T2VA | Builds the full audiovisual timeline from text |
| I2VA | Starts from a first frame, develops forward |
| FL2VA | Describes the continuous path between first and last frames |
| L2VA | Infers an opening that converges on the supplied last frame |
| Ref2VA | Full-reference rewrites with `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music` |

Key fields: `integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music` - exact field names, section order, and timing notation matter.

### MiniMax Hub canvas skills (platform-bound)

| Skill | Installs | Notes |
|---|---|---|
| brand-promo-video-generator | 2,629 | Hub canvas workflow |
| music-video-subtitle-generator | 2,609 | Hub canvas workflow |
| handdrawn-live-video-generator | 2,588 | Hub canvas workflow |
| minimalist-product-ad-generator, 3d-animation-short-generator, papercraft-stop-motion-explainer, paper-collage-explainer-generator, co-op-game-intro-generator | - | Hub-bound; per README "not portable to generic agent harnesses" |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC video prompt engineering** | Apply H3 T2VA/I2VA prompt structures when scripting CorpusIQ UGC videos - the field ordering and timing notation are reusable outside MiniMax |
| **Brand promo video briefs** | brand-promo-video-generator for CorpusIQ product-ad briefs (requires MiniMax Hub) |
| **Prompt-pattern research** | base-en.txt / ref-en.txt are portable multimodal prompt-structure references - feed into the CorpusIQ UGC pipeline regardless of model |
| **Multimodal answer enrichment** | H3's audio-visual timeline format (integrated_multimodal_description + overall_soundscape) is a reusable structure for CorpusIQ visual answers |

## Troubleshooting

| Issue | Fix |
|---|---|
| Hub skills fail outside MiniMax Hub | Expected - the 8 canvas skills call `hub_generate_video` etc. Use only `h3-prompt-writing` in generic agent harnesses |
| `npx skills add` lists 9 skills but installs none | Install per-skill with `--skill h3-prompt-writing` |
| Missing license | The repo has no LICENSE file (GitHub API reports none) - internal review recommended before commercial reuse of the prompt guides |

## Verification

```bash
# List what the bundle provides
npx skills add minimax-ai/minimax-h3 --list

# After install, confirm the portable skill is present
ls ~/.hermes/skills/h3-prompt-writing/SKILL.md
```

## Security

No skills.sh security audits are published for this publisher (Trust Hub / Socket / Snyk verdicts all absent as of Sep 14, 2026).

| Audit | Status |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

`h3-prompt-writing` itself performs no network calls and ships only local Markdown reference files. The Hub-bound skills require a MiniMax account and the Hub runtime. Review the repo before adopting the Hub workflow into production pipelines.

## Related

- [RunComfy Agent Skills - Setup Guide](/hermes/skills/catalog/runcomfy-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
