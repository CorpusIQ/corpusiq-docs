---
title: "Baoyu Skills - Content Generation & Publishing Suite Setup"
description: "Setup guide for jimliu/baoyu-skills - 594.5K combined installs. A 21-skill content suite for illustration, infographics, and multi-platform publishing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/baoyu-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "content generation", "publishing", "image generation", "wechat"]
---

# Baoyu Skills - Setup Guide

**Source:** [jimliu/baoyu-skills](https://www.skills.sh/jimliu/baoyu-skills) via skills.sh - 594.5K combined installs across 24 indexed listings; first seen Oct 9, 2026 (evening sweep)
**GitHub:** [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) (26,498 stars, MIT license; active through Sep 2026 - pushed Sep 10, 2026; `skills/` holds 21 skill directories, plus release tooling in `.claude/skills/`)
**Category:** Content Generation / Image Generation / Multi-Platform Publishing
**Quality Tier:** 🟡 Beta - 26,498-star MIT repo, active through Sep 2026; 594.5K combined installs across 24 indexed listings; mixed security verdicts on browser/publishing automation skills (see Security)

Baoyu (JimLiu) publishes a 21-skill content suite for coding agents, covering the path from draft to published post: article illustration, comics, infographics, cover images, image generation, markdown formatting and conversion, and multi-platform publishing to WeChat, Weibo, X, and Xiaohongshu. The suite sits at 594.5K combined installs across 24 indexed listings on skills.sh. The WeChat Official Account workflow is the flagship: `baoyu-cover-image` for header art, `baoyu-article-illustrator` for in-body visuals, and `baoyu-post-to-wechat` to publish - a three-step article line the README itself recommends as the minimal set.

The README organizes everything into three groups. Content Skills cover the visual and publishing layer: cover images, illustration, infographics, Xiaohongshu image cards, slide decks, comics, diagrams, and the WeChat, Weibo, and X publishing skills. AI Generation Skills cover `baoyu-image-gen`, a provider-agnostic image backend spanning OpenAI, Azure, Google, OpenRouter, DashScope, Z.AI, MiniMax, Jimeng, Seedream, and Replicate, plus `baoyu-danger-gemini-web`. Utility Skills handle translation, YouTube transcripts, URL-to-markdown capture, markdown formatting, and image compression. Shared configuration lives under `.baoyu-skills/`: `.env` for API keys and per-skill `EXTEND.md` files for customization.

---

## Installation

Prerequisites: a Node.js environment, since the skills run through `npx`.

```bash
# Skills CLI (recommended) - installs the suite
npx skills add jimliu/baoyu-skills
```

Claude Code plugin marketplace:

```text
/plugin marketplace add JimLiu/baoyu-skills
/plugin install baoyu-skills@baoyu-skills
```

The README recommends installing only the skills you actually need - bulk-installing all 20+ adds context overhead for the agent on every run. Codex users can copy or symlink individual skills into `<project>/.agents/skills/<skill>/`. Credentials go in `~/.baoyu-skills/.env` (user level) or `<project>/.baoyu-skills/.env` (project level), and should never be committed. Individual skills are also installable from ClawHub (for example `clawhub install baoyu-image-gen`); ClawHub releases are published under MIT-0.

## What It Provides

Install counts from the Oct 9, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| baoyu-post-to-wechat | 34,007 | Publish to WeChat Official Account: image-text posts and full articles, API/browser/remote-API methods, multi-account support |
| baoyu-image-gen | 33,046 | Provider-agnostic image generation with batch mode, reference images, and quality presets |
| baoyu-infographic | 32,250 | Publication-ready infographics with 21 layout types and 17 visual styles |
| baoyu-markdown-to-html | 31,819 | Markdown to styled, WeChat-compatible HTML with themes and citation footnotes |
| baoyu-cover-image | 31,634 | Article cover images with a five-dimension Type × Palette × Rendering × Text × Mood system |
| baoyu-article-illustrator | 31,457 | Place and generate article illustrations with Type × Style × Palette selection |
| baoyu-xhs-images | 30,902 | Xiaohongshu image card series (1-10 cards) with the Style × Layout system |
| baoyu-slide-deck | 30,628 | Slide deck images from content, merged into pptx and pdf |
| baoyu-url-to-markdown | 29,924 | Fetch any URL via Chrome CDP and convert to clean markdown |
| baoyu-comic | 29,420 | Educational comics with art style × tone combinations and panel layouts |
| baoyu-post-to-x | 28,536 | X posts with images and X Articles (long-form markdown), via a real Chrome session |
| baoyu-compress-image | 27,835 | Compress images while maintaining quality |
| baoyu-format-markdown | 27,728 | Turn drafts into structured markdown with frontmatter, headings, and a typography pass |
| baoyu-danger-x-to-markdown | 27,666 | Convert X tweets, threads, and Articles to markdown (reverse-engineered API - see Security) |
| baoyu-danger-gemini-web | 27,588 | Gemini Web text and image generation (reverse-engineered access - see Security) |
| release-skills | 25,317 | Release tooling for the suite itself (maintainer-facing, ships in `.claude/skills/`) |
| baoyu-translate | 25,137 | Article translation with quick, normal, and refined modes plus audience and style presets |
| baoyu-post-to-weibo | 21,280 | Weibo posts with text, images, videos, and headline articles |
| baoyu-youtube-transcript | 21,005 | YouTube transcripts with language selection, translation, chapters, and speaker ID |
| baoyu-diagram | 14,860 | Publication-ready SVG diagrams: flowchart, sequence, structural, illustrative, class |
| baoyu-wechat-summary | 9,503 | WeChat group chat digests with topics, quotes, and per-user profiles |
| baoyu-imagine | 9,286 | Image generation listing (not present as a directory in the current `skills/` tree) |
| baoyu-electron-extract | 7,505 | Extract resources and readable source from an Electron app's `app.asar` |
| baoyu-image-cards | 6,207 | Image card listing (not present as a directory in the current `skills/` tree) |

The suite's flagship workflow is visible in the install mix: `baoyu-post-to-wechat` is the most-installed skill at 34,007. The two listings without a directory in the current tree (`baoyu-imagine`, `baoyu-image-cards`) appear to be earlier or alternate image listings.

## Why This Matters for Hermes Agents

Coding agents have become strong at producing content and weak at shipping it: the last mile of an article - cover art, in-body illustration, platform-specific markup, the actual publish step - is usually manual work. This suite automates that last mile for platforms many Western toolchains ignore: WeChat Official Accounts, Weibo, and Xiaohongshu, where publishing is gated behind logins and browser sessions rather than clean APIs. The publishing skills drive a real Chrome session over CDP when no API path exists, with a human reviewing before the final publish. `baoyu-image-gen` is the reusable core: one interface over providers including OpenAI, Azure, Google, OpenRouter, DashScope, MiniMax, Jimeng, Seedream, and Replicate, with batch mode, reference images, and quality presets. The markdown toolchain (format, convert, translate, compress) works in any content workflow regardless of platform. Two skills are deliberately marked as danger - reverse-engineered APIs for Gemini Web and X - so treat them as opt-in experiments rather than foundations. Everything is plain markdown plus local scripts run through `npx`, so a Hermes agent adds it the same way it adds any other skill.

## Usage

| You say | What happens |
|---|---|
| "Illustrate this article and generate a cover image" | baoyu-cover-image picks a five-dimension combination, then baoyu-article-illustrator places and generates in-body visuals |
| "Publish this draft to my WeChat Official Account" | baoyu-post-to-wechat converts markdown to WeChat-ready HTML and publishes as an image-text post or full article, via API or browser |
| "Make a Xiaohongshu card series from this post" | baoyu-xhs-images breaks the content into 1-10 styled image cards using the Style × Layout system |
| "Turn these notes into an infographic" | baoyu-infographic recommends a layout × style combination and generates a publication-ready graphic |
| "Post this thread to X" | baoyu-post-to-x fills the composer in a real Chrome session (markdown input routes to X Articles); you review and publish |
| "Translate this article for a Chinese audience" | baoyu-translate runs normal or refined mode with audience and style presets, then the markdown toolchain cleans up the output |
| "Summarize my WeChat group chat from yesterday" | baoyu-wechat-summary produces a structured digest with topics, quotes, and per-user stats (requires wx-cli and macOS WeChat 4.x) |

## Verification

```bash
# Claude Code and skills-directory agents - check the suite landed
ls ~/.claude/skills/ | grep -i baoyu

# Codex project-level installs - run from the project root
ls .agents/skills/ | grep -i baoyu

# Review a skill's SKILL.md straight from GitHub before installing
curl -s https://raw.githubusercontent.com/JimLiu/baoyu-skills/main/skills/baoyu-post-to-wechat/SKILL.md | head -20
```

If your agent uses a different skills directory, check that path instead; the `npx skills add` flow installs into the directory your agent scans.

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| release-skills | Warn | Pass | Warn |
| baoyu-post-to-wechat | Pass | Warn | Pass |
| baoyu-danger-gemini-web | Warn | Warn | Pass |
| baoyu-cover-image | Warn | Pass | Pass |

No sampled skill is clean on all three engines. The README is candid about two of the risks: `baoyu-danger-gemini-web` uses a reverse-engineered Gemini Web API through browser cookies (use at your own risk, no stability guarantees), and `baoyu-danger-x-to-markdown` warns that account restrictions are possible if its reverse-engineered X API usage is detected. The publishing skills also automate a logged-in Chrome session, which carries the usual platform-automation risks.

## Limitations

- Mixed security profile: sampled verdicts include Warns on release-skills (two engines), baoyu-post-to-wechat, baoyu-danger-gemini-web, and baoyu-cover-image.
- The two danger skills depend on reverse-engineered APIs that can break without notice.
- External dependencies: Google Chrome for the CDP flows, wx-cli plus macOS WeChat 4.x for baoyu-wechat-summary, and WeChat API credentials (or an allowlisted IP) for the fast publishing method.
- Browser publishing is semi-manual by design: the scripts fill the composer and the user reviews and publishes.
- Bulk installs add context overhead; the README recommends installing only the skills you need.
- Snapshot data, verified Oct 9, 2026: 594.5K combined skills.sh installs across 24 indexed listings; 26,498 GitHub stars; MIT; last pushed Sep 10, 2026. Counts drift over time.

## Related

- [Proseify - Anti-Prose-Slop Book Writing Setup](/hermes/skills/catalog/proseify-setup) - prose-quality pass for the long-form drafts this suite publishes
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup) - design-quality gate for the web surfaces your content points at
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - motion and interface craft for product content and demos
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from the minimal WeChat line: cover-image, article-illustrator, post-to-wechat. post-to-wechat already includes the markdown-to-WeChat HTML conversion, so add format-markdown only for raw drafts and markdown-to-html only for custom themes.
- Keep API keys in `~/.baoyu-skills/.env`, project overrides in `<project>/.baoyu-skills/.env`, and add the project config to `.gitignore`.
- Customize per skill with `EXTEND.md` (project level beats user level): brand palettes, default themes, and multi-account WeChat configuration.
- Prefer the WeChat API publishing method when the machine's IP can be allowlisted; the browser method needs only a Chrome login, and the remote-API method exists for machines outside the allowlist.
- For batch image work use `baoyu-image-gen --batchfile batch.json --jobs 4`, and set `--provider` and `--model` explicitly for reproducible output.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
