---
title: "Yuyile Skills - AI Content Creator Skill Suite Setup"
description: "ttfake92-lab/skills - 5.0K combined installs: 13 AI agent skills for content creators spanning video, thumbnails, Remotion and macOS tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ttfake92-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "content creation", "video", "thumbnails"]
---

# Yuyile Skills - AI Content Creator Skill Suite Setup

**Source:** [ttfake92-lab/skills](https://www.skills.sh/ttfake92-lab/skills) via skills.sh - 5.0K combined installs across 13 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [ttfake92-lab/skills](https://github.com/ttfake92-lab/skills) - 341 stars, main branch, last pushed Oct 30, 2026; no LICENSE file in the repository, though the README states MIT. One SKILL.md per skill under skills/, with scripts, references and templates alongside.
**Category:** Content Creation and Video Production
**Quality Tier:** 🟠 Orange - the sample carries Fail cells on yyl-remotion-video (Snyk), macos-migration (Gen Agent Trust Hub and Snyk) and mx-shell-prompt (Snyk), and Warn cells on yyl-benchmark-breakdown (Gen Agent Trust Hub, Socket and Snyk), college-application (Snyk), yyl-disk-cleaner-cat (Snyk), archival-fragments (Snyk), yyl-video-prompt (Snyk) and yyl-vertical-video (Gen Agent Trust Hub, Socket and Snyk).

Yuyile's skills are a bilingual collection of AI agent skills for content creators, video producers, prompt engineers and students making decisions. They install through the skills CLI with a single command and cover the creator pipeline end to end: competitive teardowns, video prompts, Remotion projects, thumbnails, a short-film pipeline in a fixed visual style, and three macOS and Claude Desktop system tools.

The collection spans two very different audiences. Seven skills target video and content production, one targets China gaokao college applications, and three are macOS and Claude system tools. The repository ships no LICENSE file, and the sampled security verdicts carry Fail cells on three skills and Warn cells on six more, both of which matter before you install the full set.

## Installation

Install the collection and pick the skills and agent when prompted:

```bash
npx skills@latest add ttfake92-lab/skills
```

To install a single skill, target it by name:

```bash
npx skills add ttfake92-lab/skills --skill claude-local-reset
```

The installer reads the repository skill manifest and places the selected skills into the supported agent environments.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| yyl-benchmark-breakdown | 617 | teardown of competitor content from a link: platform detection, transcription, frame extraction, reusable formula |
| yyl-video-thumbnail | 579 | high-CTR video covers for Bilibili, YouTube and Douyin/TikTok using the pop-out technique |
| yyl-remotion-video | 565 | building 16:9 Remotion projects from scripts, articles or outlines and exporting mp4 |
| college-application | 542 | China gaokao application decisions: personality assessment, major research and a sourced HTML report |
| yyl-disk-cleaner-cat | 533 | macOS disk cleanup with a pixel-art cat and a confirm-before-delete web page |
| macos-migration | 525 | two-phase macOS migration: scan the old Mac to a JSON manifest, restore on the new |
| mx-shell-prompt | 462 | former video-prompt skill, merged into yyl-video-prompt and removed from the repository |
| AI-video-prompt | 444 | former video-prompt skill, merged into yyl-video-prompt and removed from the repository |
| archival-fragments | 242 | end-to-end short films in the Archival Fragments style, from idea to assembled file |
| archival-fragments-lite | 218 | the same visual style and first-last-frame method with no tool lock-in |

The remaining 3 indexed listings range from 54 to 139 installs.

## Why This Matters for Hermes Agents

An agent asked to produce content usually stops at text; this collection pushes it into the assets around the text. yyl-benchmark-breakdown turns a competitor link into a reusable formula, a frame-by-frame breakdown and a persona read, which is the research step most creator workflows skip. yyl-video-prompt then turns a script into ready-to-submit segment prompts, yyl-remotion-video builds a deterministic Remotion project, and yyl-video-thumbnail produces the cover. Together they close the loop from research to publishable asset.

Three cautions apply. The sample carries Fail cells on yyl-remotion-video, macos-migration and mx-shell-prompt, and Warn cells on six more, detailed in the Security section, so install skills individually and review the flagged ones before trusting them. Two indexed listings, mx-shell-prompt and AI-video-prompt, are removed skills that yyl-video-prompt replaces, so a search that returns them should route to yyl-video-prompt instead. And the repository ships no LICENSE file, which matters if you plan to reuse or repackage the skills.

## Usage

| You say | What happens |
|---|---|
| Tear down this competitor's viral video | Uses yyl-benchmark-breakdown to extract formula, hooks and rhythm |
| Turn my script into video prompts for Seedance | Uses yyl-video-prompt to split segments by short-video or cinematic mode |
| Build a Remotion project from these notes and export mp4 | Uses yyl-remotion-video for a frame-driven React project |
| Make a high-CTR cover for this YouTube video | Uses yyl-video-thumbnail for the pop-out cover in three ratios |
| Help a student decide majors and universities | Uses college-application for assessment, research and a sourced report |
| Free up space on my Mac | Uses yyl-disk-cleaner-cat for a confirm-before-delete cleanup |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/ttfake92-lab/skills/main/README.md | head -40
```

Confirm the benchmark teardown skill body is present before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/ttfake92-lab/skills/main/skills/yyl-benchmark-breakdown/SKILL.md | head -30
```

Confirm the Remotion skill body before building video:

```bash
curl -sL https://raw.githubusercontent.com/ttfake92-lab/skills/main/skills/yyl-remotion-video/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| yyl-benchmark-breakdown | Warn | Warn | Warn |
| yyl-video-thumbnail | Pass | Pass | Pass |
| yyl-remotion-video | Pass | Pass | Fail |
| college-application | Pass | Pass | Warn |
| yyl-disk-cleaner-cat | Pass | Pass | Warn |
| macos-migration | Fail | Pass | Fail |
| mx-shell-prompt | Pass | Pass | Fail |
| AI-video-prompt | Pass | Pass | Pass |
| archival-fragments | Pass | Pass | Warn |
| archival-fragments-lite | Pass | Pass | Pass |
| yyl-video-prompt | Pass | Pass | Warn |
| claude-local-reset | Pass | Pass | Pass |
| yyl-vertical-video | Warn | Warn | Warn |

Every indexed listing is in this sample, so there are no unsampled rows. The Fail cells sit on yyl-remotion-video (Snyk), macos-migration (Gen Agent Trust Hub and Snyk) and mx-shell-prompt (Snyk). The Warn cells sit on yyl-benchmark-breakdown (Gen Agent Trust Hub, Socket and Snyk), college-application (Snyk), yyl-disk-cleaner-cat (Snyk), archival-fragments (Snyk), yyl-video-prompt (Snyk) and yyl-vertical-video (Gen Agent Trust Hub, Socket and Snyk). The four skills with clean verdicts are yyl-video-thumbnail, AI-video-prompt, archival-fragments-lite and claude-local-reset.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,022 combined installs across 13 indexed listings; 341 GitHub stars; no LICENSE file in the repository; last pushed Oct 30, 2026. Counts drift over time.
- The repository ships no LICENSE file, although the README License section states MIT; treat the reuse terms as unconfirmed until a license file is added.
- mx-shell-prompt and AI-video-prompt carry install counts but no longer exist in the repository tree; yyl-video-prompt merges and replaces both, so route lookups for them to yyl-video-prompt.
- yyl-vertical-video (54 installs) requires external video-agent workspace dependencies listed in the skill, including lighttrail and talking-head-reel, which are not bundled.
- Several skills are Chinese-first (yyl-video-prompt, yyl-vertical-video, yyl-benchmark-breakdown, archival-fragments and the system tools); the README is bilingual but the skill bodies lean Chinese.

## Related

- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Guizang Social Card Skill - Social Card Generation Setup](/hermes/skills/catalog/guizang-social-card-skill-setup)
- [Archive Creator Marketing Skills - Creator Program Setup](/hermes/skills/catalog/archive-dot-com-creator-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the video-prompt and thumbnail skills together; the benchmark teardown feeds the prompt skill which feeds the thumbnail skill.
- Route any request for mx-shell-prompt or AI-video-prompt to yyl-video-prompt, which replaces both.
- Start with archival-fragments-lite before the full archival-fragments pipeline; the lite version has no tool lock-in.
- Treat macos-migration and claude-local-reset as macOS or Windows tools; neither supports Linux.
- Review the three Fail-cell skills individually before trusting their output in production.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
