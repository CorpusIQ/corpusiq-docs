---
title: "Huashu Skills - 22-Skill Content Production Pack"
description: "alchaincyf/huashu-skills: 16.0K combined installs. 22 content-production skills for Chinese publishing platforms, from topic to PDF to artwork."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/huashu-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "content production", "publishing", "editorial"]
---

# Huashu Skills - Setup Guide

**Source:** [alchaincyf/huashu-skills](https://www.skills.sh/alchaincyf/huashu-skills) via skills.sh - 16.0K combined installs across 37 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [alchaincyf/huashu-skills](https://github.com/alchaincyf/huashu-skills) - 2,147 stars, MIT, branch master, last pushed 2026-10-26; 22 `SKILL.md` files, one per `huashu-` prefixed directory at the repository root, most a single workflow document with a few pointing at a `references/` folder

**Category:** Content production for Chinese publishing platforms: articles, decks, video scripts, platform artwork and the editorial passes around them

**Quality Tier:** 🟡 Yellow - two of the three sampled skills are clean on all scanners, but huashu-douyin-script fails Gen Agent Trust Hub and warns on both Socket and Snyk

This repository is a catalogue as much as a pack. The README describes three layers: 21 flagship skills that live in their own repositories, 14 person-perspective skills also in separate repositories, and 22 built-in skills that live here. This guide covers only the built-in layer, the 22 directories in the tree. The README also ships a machine-readable `skills.json` and asks agents to read that file first, which is a better entry point than the prose table if you are automating the install.

The built-ins are a production line for one author's publishing workflow. It starts at topic selection and outline, moves through drafting, editorial passes and image generation for WeChat and Xiaohongshu, and ends at Markdown to PDF for whitepapers and at slide assembly for talks. Several skills encode a method rather than a task: the proofreading skill carries a six-category taxonomy of machine phrasing, the speech coach is built on the MIT How to Speak lecture, and the research skill exists to keep findings on disk when a session is cut short. The instructions are written in Chinese and assume a Chinese-language audience, so the method travels better than the wording.

## Installation

The README documents two routes, and neither is a skills CLI. The fastest is an instruction to the agent: point it at the repository README and `skills.json` and ask it to install what you need. The self-service route for the standalone repositories is a clone into the agent's skills directory:

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/skills/huashu-design
```

Built-in skills, which is everything in this guide, are installed by copying the subdirectory, and the README notes that a session restart is needed before the skills load. For Hermes that is:

```bash
git clone --depth 1 https://github.com/alchaincyf/huashu-skills.git /tmp/huashu-skills
cp -r /tmp/huashu-skills/huashu-*/ ~/.hermes/profiles/corpusiq/skills/
```

The wildcard is safe here in a way it is not in most repositories: every `huashu-` prefixed directory at the root is a skill, and everything else at the root is documentation, a licence, an assets folder or CI configuration.

Dependencies are documented per skill rather than once. The PDF skill states its own install (`pip3 install markdown2 weasyprint`, plus `brew install pango` on macOS), the image skills expect an image-generation model and Playwright for screenshots, and the Douyin script skill expects `yt-dlp`, `uv`, a Gemini API key and a Chrome session already logged in to the platform. Read the environment section of a skill before installing its dependencies, because several assume macOS tools.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| huashu-md-to-pdf | 1,049 | Markdown to a print-grade PDF whitepaper: cover, two-column contents, chapter pagination, code blocks and long tables handled. |
| huashu-douyin-script | 1,001 | Short-video scripts for Douyin: competitor download, video analysis, formula extraction, script and storyboard, tone pass. |
| huashu-proofreading | 879 | Three-pass editorial review aimed at machine-sounding prose: content, style and rhythm, with a six-category list of tells. |
| huashu-slides | 841 | Content to PPTX end to end with two assembly paths, checkpoints between stages and 18 design directions. |
| huashu-design | 775 | Design direction consulting: three differentiated philosophies from a library of 20, visual demos, prompts and a scored critique. |
| huashu-research | 750 | Structured web research that appends findings to a file as it goes, so a truncated session does not lose the work. |
| huashu-data-pro | 745 | Excel reads, campaign and ROI reviews, HTML reports, chart building and deck assembly from the same data. |
| huashu-wechat-image | 739 | WeChat article artwork: 2.35:1 covers, 16:9 and 4:3 body images and infographics, proposal before generation. |
| huashu-xhs-image | 738 | Xiaohongshu note artwork at 3:4, model-generated by default with HTML capture as the fallback for exact tables. |
| huashu-script-polish | 737 | Spoken-language pass on video scripts: removes written register, shortens sentences, marks where to cut to screen. |
| huashu-topic-gen | 729 | Three or four article directions with headline, outline, effort estimate and a real list of weaknesses. |
| huashu-speech-coach | 726 | Talk and training preparation from the MIT How to Speak method: promise openings, cycling, fences, verbal punctuation. |
| huashu-article-edit | 696 | Scoped article editing with a change log, written so a truncated session does not lose the edits. |
| huashu-video-outline | 691 | Two or three video outlines with titles, cover suggestions and structure, ready to pick from. |
| huashu-info-search | 691 | Multi-channel search on new products and technology, cross-checked against each other, then filed into a knowledge base. |
| huashu-article-to-x | 686 | Condenses a long article into 200 to 500 characters for X while keeping the author's voice. |
| huashu-image-upload | 677 | Generates article artwork, uploads it to an image host and inserts the markdown links in place. |
| huashu-video-check | 672 | Title, cover and opening-hook review against retention tactics, aimed at click-through and watch time. |
| huashu-material-search | 672 | Searches a personal library of 1,800+ real anecdotes and opinions so an article is grounded in specifics. |
| huashu-agent-swarm | 671 | Parallel multi-agent development over git with no master agent: eight workers, small commits, explicit stop conditions. |

The remaining 17 indexed listings range from 1 to 661 installs. Two different things are in that tail. Most of it is older listing names for skills already counted above (`markdown-to-pdf` at 61, `ai-taste-proofreading` at 13, `douyin-viral-script` at 7), which is why the index carries 37 listings against 22 directories. The rest is a real skill that simply sits below the cut: `huashu-skill-updater` at 39 installs is one of the 22 directories and is the pack's own update checker.

## Why This Matters for Hermes Agents

Content work is where agents most often produce text that is fluent and unusable. This pack takes the opposite approach to most writing skills: it decomposes publishing into stages, gives each stage its own skill, and puts a checkpoint between them. The topic skill waits for a choice, the slide skill asks for collaboration mode and assembly path before it starts, the artwork skills present two or three directions and refuse to generate until one is picked.

The proofreading skill is the most transferable document in the pack. Its six categories of machine phrasing, empty framing clauses, repeated rhetorical contrasts, written-register verbs where a plain verb exists, mechanical list structure, false balance and a lack of specifics, are a checklist any agent can apply to its own output in any language. The instruction to replace "significantly improved" with a number is the whole method in one line.

Two operational patterns also transfer beyond content. The research skill creates the output file before the first search and appends after every search, which is the cheapest defence against context loss in a long session. And the deck skill forces an assertion-and-evidence outline before design, which stops the common failure where a deck is styled before anyone decided what each slide claims.

## Usage

| You say | What happens |
|---|---|
| "Turn this markdown draft into a whitepaper PDF" | `huashu-md-to-pdf` runs its converter, which builds a cover, a two-column contents page from the heading numbers and paginated chapters, then reports any missing images by path. |
| "This article reads like a machine wrote it" | `huashu-proofreading` works in three passes: facts and logic first, then the six-category style sweep, then rhythm and paragraph length. |
| "I need a deck for Thursday, guided mode" | `huashu-slides` builds an assertion-led outline, waits for approval, offers three design systems, then assembles an editable PPTX. |
| "Make me three cover options for this note" | `huashu-xhs-image` proposes three differentiated directions at 3:4, then generates each one and shows them side by side. |
| "Research the new model releases this week and keep notes" | `huashu-research` creates a dated file first, appends findings with source and date after each search, and writes a source table with a confidence column at the end. |
| "Write me a video script from these three competitor clips" | `huashu-douyin-script` downloads the clips, analyses them, extracts the shared formula and drafts a script with a shot-by-shot storyboard. |
| "Check this title and cover before I publish" | `huashu-video-check` scores the hook and the cover against retention tactics and names the specific weakness rather than offering taste. |

## Verification

The raw path for the PDF skill returned HTTP 200 on branch master when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} md-to-pdf\n" \
  https://raw.githubusercontent.com/alchaincyf/huashu-skills/master/huashu-md-to-pdf/SKILL.md
```

Expect `200`. After the clone, confirm the tree matches the 22 directories this guide claims and that the catalogue file came down with it:

```bash
find /tmp/huashu-skills -name SKILL.md | wc -l
ls -d /tmp/huashu-skills/huashu-*/ | wc -l
head -3 /tmp/huashu-skills/huashu-research/SKILL.md
```

Both counts should print 22. The header should show `name: huashu-research` and a `description:` line, and the file should contain the instruction to create the research file before searching, which is the rule the skill exists for.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| huashu-md-to-pdf | Pass | Pass | Pass |
| huashu-douyin-script | Fail | Warn | Warn |
| huashu-proofreading | Pass | Pass | Pass |

The Snyk entry for `huashu-douyin-script` carries codes W011 and W012. The pack records the codes without explaining them, so treat them as a prompt to read that skill yourself rather than as a diagnosis.

Reading the skill explains the verdict. It downloads video from Douyin with `yt-dlp` using cookies pulled from a logged-in Chrome profile, sends the file to a Gemini endpoint with `GEMINI_API_KEY`, and accepts an optional `GEMINI_BASE_URL` so the calls can be routed through a proxy or relay. Browser credential reuse plus outbound upload plus a user-supplied base URL is the exact combination that trips a scanner, and it is also the combination that deserves a manual read before it runs on a machine holding real sessions. The other two sampled skills are far quieter: one converts local Markdown through WeasyPrint, the other edits prose.

Two pack-wide issues belong here rather than in limitations. Several skills reference absolute paths on the author's own machine (`/Users/alchain/...`) for a personal materials library and for a font or subtitle folder, so a request that triggers those lookups fails or, worse, reads whatever happens to sit at that path on another host. And the pack is MIT at the repository root, which is the clearest licensing position in this catalogue batch.

## Limitations

- Snapshot data, verified 2026-11-01: 16,023 combined installs across 37 indexed listings; 2,147 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- The index lists 37 skills but the tree holds 22 directories, so 15 listings are older names for skills already covered. One real skill, `huashu-skill-updater` at 39 installs, sits below this guide's threshold and is therefore missing from the table.
- The README counts 57 skills in three layers (21 flagship, 14 person-perspective, 22 built-in) while the repository's GitHub description says 52 (16, 14 and 22). Neither figure is checkable from this repository, so treat both as claims.
- The instructions, prompts and style rules are written in Chinese for Chinese publishing platforms. The workflow transfers, the wording does not, and an agent that does not read Chinese will follow the structure while missing the editorial intent.
- Several skills hardcode absolute macOS paths and expect a personal materials library of roughly 1,800 entries. Without that data, `huashu-proofreading` and `huashu-material-search` lose the specifics they were built to force.
- `huashu-md-to-pdf` documents an unresolved rendering fault where some PDFs open garbled in macOS Preview and fine in a browser, with no fix. The skill also warns against the obvious workaround, since the full-fonts option inflates a 10 KB file to 43 MB and leaves it garbled.

## Related

- [Huashu Design Skill - HTML-First Agent Design Setup](/hermes/skills/catalog/huashu-design-setup)
- [01coder Agent Skills - Content, Publishing & Security Toolkit Setup](/hermes/skills/catalog/01coder-agent-skills-setup)
- [Xiaohongshu Skills - RED Content Operations](/hermes/skills/catalog/xiaohongshu-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the four skills you will actually use, not the 22. The pipeline skills assume each other's outputs, and a paragraph is easier to audit than a directory of prompts that each expect a different environment.
- Start with `huashu-topic-gen` and `huashu-article-edit` if you write in English. They are the two least language-bound skills here and both are built around waiting for a human choice, which is the useful part.
- Read `huashu-proofreading` even if you never install it. The six-category list of machine phrasing is a compact editing checklist, and the rule about replacing vague intensifiers with numbers is worth adopting as a house style.
- Do not run `huashu-douyin-script` on a machine where Chrome holds sessions you care about. It extracts cookies from the browser profile by design, and that behaviour is why its scanner row is a fail rather than a pass.
- Expect macOS assumptions. Where a skill names a font, a subtitle folder or a materials library, substitute your own path before the first run rather than after the first confusing failure.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
