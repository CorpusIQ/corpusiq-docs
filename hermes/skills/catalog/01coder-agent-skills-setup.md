---
title: "01coder Agent Skills - Content, Publishing & Security Toolkit"
description: "VerySmallWoods' 01coder marketplace: Chinese content creation, multi-platform publishing, subtitle tooling, and security scanning. 21.5K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/01coder-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-02"
tags: ["hermes skill", "agent skill", "skill setup", "content", "publishing", "chinese", "security", "video"]
---

# 01coder Agent Skills - Setup Guide

**Source:** [sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills) (136⭐, MIT)
**Skill family:** `sugarforever/01coder-agent-skills` (23 SKILL.md files in-repo; 27 indexed listings)
**Combined Installs:** ~21,505 across indexed listings (Oct 2, 2026 snapshot)
**Category:** Content / Publishing / Media
**Quality Tier:** 🟡 Beta (author-tested, actively maintained; Chinese-first content workflows, some skills language-specific)

01coder Agent Skills is a marketplace by VerySmallWoods aimed at content creators who publish across X, Substack, 知识星球 (Zsxq), YouTube, and Bilibili. It combines Chinese-language writing and video production workflows with multi-platform publishing skills and a small security-scanning cluster. The install base is dominated by a single domain-specific outlier (`china-stock-analysis`, 12.6K) — treat the combined total as narrower than the headline number.

---

## Installation

```bash
npx skills@latest add sugarforever/01coder-agent-skills
```

Claude Code native marketplace:

```bash
/plugin marketplace add sugarforever/01coder-agent-skills
/plugin install 01coder-skills@01coder-agent-skills
```

## Roster - Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| china-stock-analysis | 12,619 | A-share / China market stock analysis workflows |
| publish-substack-article | 602 | Publish Markdown articles to Substack as drafts (MD → HTML) |
| Next.js Security Scan | 539 | Security scanning for Next.js projects |
| Python Security Scan | 535 | Security scanning for Python projects |
| subtitle-correction | 528 | Fix speech-recognition errors in `.srt` files (ZH + EN) while preserving timestamps |
| diagram-to-image | 506 | Convert diagrams into images |
| video-script | 487 | Video script drafting |
| publish-zsxq-article | 472 | Publish Markdown to Zsxq (知识星球) as drafts |
| add-feishu | 452 | Feishu (Lark) integration |
| publish-x-article | 448 | Publish Markdown articles to the X (Twitter) Articles editor |
| share-reading | 431 | Draft social posts recommending an article/paper across X, Substack, Zsxq |
| interactive-input | 431 | Interactive input handling for agent workflows |
| personal-chinese-writing-style | 375 | Personal ZH writing-style preferences (punctuation, structure, voice) |
| fpl-copilot | 284 | Fantasy Premier League copilot — local SQLite, HTML reports, captain picks |
| personal-writing-style | 283 | Personal EN writing-style preferences |
| cover-image | 282 | Hand-drawn article cover generator (17 styles, 10 layouts) |
| slides-video | 279 | Slide generation + script → slides-driven narration video |
| tweet-insight | 271 | Read a tweet + linked sources, write an original ZH share-post |
| promote-post | 268 | Teaser tweet for a published article that opens the story |
| video-planner | 229 | Plan videos: read-aloud scripts, titles, tags, YouTube chapters |
| codex-cli | 225 | Codex CLI workflows |
| cover-design | 217 | Cover design generation |
| claude-session-manager | 196 | Claude session management |
| codex-session-manager | 189 | Codex session management |
| mining-session-skills | 185 | Session-mining skill extraction |
| producing-video | 171 | Voiceover audio + SRT → narration-synced MP4 via HyperFrames |
| chinese-writing-style | 1 | ZH writing-style stub (minimal installs) |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Multi-platform publishing | `publish-x-article` + `publish-substack-article` + `publish-zsxq-article` for one-source-many-destinations distribution |
| Video pipeline | `producing-video` (HyperFrames HTML-to-video) + `subtitle-correction` + `video-planner` |
| Social repurposing | `share-reading` + `promote-post` + `tweet-insight` to turn long content into platform-native posts |
| Localization | `personal-chinese-writing-style` for ZH-market content that reads natively |

## Limitations / Verification

- skills.sh indexing verified Oct 2, 2026: 27 indexed listings; 23 SKILL.md files verified via the GitHub trees API on branch `main`.
- **Install concentration:** `china-stock-analysis` alone accounts for 12,619 of the 21,505 combined installs (~59%). The content/publishing skills sit in the 150–600 range.
- Several skills are Chinese-language-first (`personal-chinese-writing-style`, `publish-zsxq-article`, `tweet-insight`) — verify fit before adoption in EN-only workflows.
- No live install test performed; install counts are from the Oct 2, 2026 sweep snapshot.
