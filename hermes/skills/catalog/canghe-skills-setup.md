---
title: "Canghe Skills - AI Content Generation Suite Setup"
description: "freestylefly/canghe-skills: 30 skills for AI image, video and comic generation, infographics and WeChat/X/XHS publishing - 15.6K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/canghe-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "content generation", "image generation", "video generation", "chinese platforms"]
---

# Canghe Skills - Setup Guide

**Source:** [freestylefly/canghe-skills](https://www.skills.sh/freestylefly/canghe-skills) via skills.sh - 15.6K combined installs across 30 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [freestylefly/canghe-skills](https://github.com/freestylefly/canghe-skills) - 474 stars, no LICENSE file at the repo root (README states MIT), master branch, last pushed Jun 8, 2026. Skills live under skills/<name>/SKILL.md (555 files in the tree).
**Category:** AI Content Generation
**Quality Tier:** 🟠 Orange - 4 Fail among 20 sampled verdicts (Gen Agent Trust Hub: seedance-video, canghe-post-to-wechat, canghe-danger-gemini-web, canghe-danger-x-to-markdown; Snyk: seedance-video); no LICENSE file at the repo root.

Canghe (freestylefly) ships a Chinese-first suite of Claude Code skills for AI content generation and publishing, built to speed up daily content work. The indexed set spans image, video and comic generation (Seedance, manga drama, manga-style video, image-gen), visual content for articles and decks (cover-image, article-illustrator, infographic, slide-deck), and publishing to Chinese platforms (WeChat Official Account, Xiaohongshu, Douyin) alongside X (Twitter).

The repo also carries a utility layer: URL and X-to-markdown converters, image compression, markdown formatting and HTML rendering, plus Obsidian skills, a skill discovery helper, a skill-creator and Remotion best practices. Many skills are adapted from BaoYu's skill work (github.com/JimLiu/baoyu-skills) and refined for local workflows. The README is written in English with a Chinese companion (README.zh.md), and several skills are Chinese-first in naming and output.

## Installation

Prerequisites: Node.js installed, plus the ability to run npx bun commands.

Quick install (recommended):

```bash
npx skills add freestylefly/canghe-skills
```

Register as a plugin marketplace in Claude Code:

```text
/plugin marketplace add freestylefly/canghe-skills
```

Then install skills via the browse UI or directly by plugin:

```text
/plugin install content-skills@canghe-skills
/plugin install ai-generation-skills@canghe-skills
/plugin install business-intelligence-skills@canghe-skills
/plugin install utility-skills@canghe-skills
```

The four plugins group the skills by purpose: content-skills (content generation and publishing), ai-generation-skills (image, video and avatar backends), business-intelligence-skills (Tianyancha company research), and utility-skills (content processing and Obsidian tooling). Several skills need API keys set in .canghe-skills/.env (for example OPENAI_API_KEY, GOOGLE_API_KEY and DASHSCOPE_API_KEY); see the Environment Configuration section of the README.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| manga-drama | 875 | Comic-style short drama generation from Seedance with storyboard scripts |
| manga-style-video | 680 | Anime-style video generation with 8 manga style templates and image-to-video |
| seedance-video | 617 | ByteDance Seedance AI video generation (text-to-video and image-to-video) |
| canghe-image-gen | 606 | AI image generation via OpenAI, Google, DashScope and Canghe providers |
| canghe-comic | 594 | Knowledge comics with art style and tone combinations and panel layouts |
| volcengine-video-understanding | 586 | Video content analysis with the Volcengine Ark API (Q&A, recognition) |
| canghe-xhs-images | 581 | Xiaohongshu (RedNote) infographic series with style and layout presets |
| canghe-cover-image | 552 | Article cover images with a five-dimension type, palette, rendering system |
| canghe-markdown-to-html | 543 | Markdown to styled WeChat-compatible HTML with code, math and PlantUML |
| canghe-article-illustrator | 529 | Article illustrations with type and style selection and structural analysis |
| canghe-infographic | 523 | Professional infographics with 20 layouts and 17 visual styles |
| canghe-url-to-markdown | 517 | Fetch any URL to clean markdown via Chrome CDP |
| canghe-slide-deck | 513 | Slide deck images from content outlines, merged to pptx and pdf |
| canghe-format-markdown | 512 | Format markdown with frontmatter, headings, lists and typography fixes |
| remotion-best-practices | 510 | Best practices for Remotion video creation in React |
| canghe-post-to-wechat | 505 | Publish articles and image-text posts to WeChat Official Account |
| canghe-danger-gemini-web | 505 | Gemini Web text and image generation via a reverse-engineered API |
| find-skills | 504 | Discover and install agent skills with searchable keywords and commands |
| canghe-compress-image | 501 | Compress images to WebP or PNG with automatic tool selection |

The remaining 11 indexed listings range from 173 to 496 installs (canghe-danger-x-to-markdown 496; canghe-post-to-x 495; obsidian-markdown 495; douyin-downloader 495; skill-creator 490; canghe-tianyancha 173).

## Why This Matters for Hermes Agents

Content-generation agents usually stall on two things: producing platform-ready visuals, and publishing to the Chinese platforms where the audience actually is. This suite supplies both. The generation skills are opinionated end to end: they analyze an article, recommend a layout and style, and emit finished images or decks rather than leaving the agent to assemble prompts by hand. The publishing skills cover the awkward parts of Chinese distribution (WeChat Official Account articles and image-text posts, Xiaohongshu infographic series, Douyin download and transcript extraction) that generic tooling rarely touches. The utility layer (URL to markdown, X to markdown, image compression, markdown formatting and HTML rendering) forms a self-contained article pipeline from fetch to publish. Because the skills ship their own TypeScript and Python scripts with reference files, they stay deterministic instead of relying on the model to remember each platform's constraints. The trade-off is security posture: several listings carry Fail verdicts and two use reverse-engineered APIs, so install selectively and keep the danger- skills out of unattended workflows.

## Usage

| You say | What happens |
|---|---|
| Turn this article into Xiaohongshu images | canghe-xhs-images breaks the article into a 1-10 image infographic series with a chosen style and layout |
| Make an anime-style video from this picture | canghe-manga-style-video renders an image-to-video clip in one of 8 manga styles |
| Publish this draft to my WeChat account | canghe-post-to-wechat posts an article or image-text post via API or browser |
| Generate a cover image for this post | canghe-cover-image auto-selects type, palette, rendering, text and mood for a cover |
| Convert that tweet thread to markdown | canghe-danger-x-to-markdown fetches the thread and writes markdown with YAML frontmatter |
| Save that webpage as clean markdown | canghe-url-to-markdown captures the page via Chrome CDP to a markdown file |
| Build me a slide deck from this outline | canghe-slide-deck generates slide images and merges them into pptx and pdf |

## Verification

```bash
# after install, confirm the skill files landed
ls .skills/freestylefly/canghe-skills/
# review a SKILL.md before relying on it
curl -sL https://raw.githubusercontent.com/freestylefly/canghe-skills/master/skills/canghe-article-illustrator/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| manga-drama | Pass | Warn | Pass |
| manga-style-video | Pass | Warn | Pass |
| seedance-video | Fail | Warn | Fail |
| canghe-image-gen | Pass | Warn | Pass |
| canghe-comic | Pass | Pass | Pass |
| volcengine-video-understanding | Pass | Pass | Pass |
| canghe-xhs-images | Pass | Pass | Pass |
| canghe-cover-image | Pass | Pass | Pass |
| canghe-markdown-to-html | Warn | Warn | Warn |
| canghe-article-illustrator | Pass | Pass | Pass |
| canghe-infographic | Pass | Pass | Pass |
| canghe-url-to-markdown | Pass | Pass | Warn |
| canghe-slide-deck | Pass | Pass | Pass |
| canghe-format-markdown | Warn | Warn | Pass |
| remotion-best-practices | Pass | Pass | Pass |
| canghe-post-to-wechat | Fail | Warn | Pass |
| canghe-danger-gemini-web | Fail | Warn | Pass |
| find-skills | Pass | Pass | Warn |
| canghe-compress-image | Pass | Pass | Pass |
| canghe-danger-x-to-markdown | Fail | Warn | Warn |

## Limitations

- Snapshot data, verified Nov 20, 2026: 15,620 combined installs across 30 indexed listings; 474 GitHub stars; no LICENSE file at the repo root (README states MIT); last pushed Jun 8, 2026. Counts drift over time.
- Only 20 of 30 listings have skills.sh verdicts; the other 10 are unverified on that platform.
- Four sampled skills carry a Gen Agent Trust Hub Fail (seedance-video, canghe-post-to-wechat, canghe-danger-gemini-web, canghe-danger-x-to-markdown) and seedance-video also fails Snyk; the two danger- skills use reverse-engineered APIs (Gemini Web and X) that the README warns may break without notice or trigger account restrictions.
- Indexed names drift from tree directories: manga-drama, manga-style-video, seedance-video, volcengine-video-understanding and douyin-downloader are indexed without the canghe- prefix their directories carry, and flyworks-avatar-video maps to a versioned directory (flyworks-avatar-video-1.0.0).
- The README is written in English with a Chinese companion (README.zh.md); several skills are Chinese-first in naming, commands and output (WeChat, Xiaohongshu, Douyin).

## Related

- [Baoyu Skills - Content Generation & Publishing Suite Setup](/hermes/skills/catalog/baoyu-skills-setup)
- [find-skills - Skill Discovery Tool Setup](/hermes/skills/catalog/find-skills-setup)
- [skill-creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by plugin (content-skills, ai-generation-skills, utility-skills) rather than the whole marketplace, so you only pull the skills you actually use.
- Set API keys in ~/.canghe-skills/.env before first use; image-gen picks its provider from whichever of OPENAI_API_KEY, GOOGLE_API_KEY or DASHSCOPE_API_KEY is present.
- Treat the two danger- skills as opt-in: danger-gemini-web and danger-x-to-markdown use reverse-engineered APIs and require consent plus cookie-based authentication.
- Chain canghe-format-markdown then canghe-markdown-to-html for a WeChat-ready article pipeline (format first, then render with a WeChat-compatible theme).
- Customize any skill with an EXTEND.md at ~/.canghe-skills/<skill-name>/EXTEND.md to override defaults without editing the installed files.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
