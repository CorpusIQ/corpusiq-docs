---
title: "Garden Skills - ConardLi's Web Video & Design Suite Setup"
description: "Setup guide for conardli/garden-skills: 5 agent skills for web video, web design, image generation, and article design - 26.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/garden-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "web design", "video presentation", "image generation", "content production"]
---

# Garden Skills - Setup Guide

**Source:** [conardli/garden-skills](https://www.skills.sh/conardli/garden-skills) via skills.sh - 26,317 combined installs across 5 indexed listings (web-design-engineer 7,836; web-video-presentation 5,396; gpt-image-2 5,262; kb-retriever 4,589; beautiful-article 3,234); first seen Oct 9, 2026 (evening sweep)
**GitHub:** [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) (12,796 stars, MIT license; active - pushed Jul 12, 2026; five skills under `skills/`: web-video-presentation, web-design-engineer, gpt-image-2, kb-retriever, and beautiful-article)
**Category:** Design / Frontend / Image Generation / Content Production
**Quality Tier:** 🟡 Beta - 12,796-star MIT repo (ConardLi), active; 26.3K combined installs across 5 indexed listings; mostly-Pass verdicts with two single-Warns

Garden Skills is ConardLi's MIT-licensed collection of production-ready Agent Skills for Claude Code, Cursor, Codex, and other AI coding agents. The suite spans an unusually wide range for a single repository: record-ready web video presentations, web design engineering, GPT Image 2 generation and editing workflows, local knowledge-base retrieval, and an editorial pipeline that turns any source into a polished article. It carries 26.3K combined installs across five indexed skills.sh listings and 12,796 GitHub stars.

Every skill follows the standard Agent Skills contract - a SKILL.md with YAML frontmatter plus reference docs and scripts the agent loads on demand - and the install story is thorough: the `npx skills` CLI, a Claude Code plugin marketplace with four plugin packs, pinned release `.zip` files with SHA-256 checksums for CI and air-gapped environments, manual copy, and git submodule. Tested compatibility covers Claude Code, Claude.ai, Cursor, Codex CLI, Gemini CLI, and OpenCode, and the SKILL.md format stays portable by design.

---

## Installation

```bash
# Skills CLI - full suite (latest commit on main)
npx skills add ConardLi/garden-skills

# Or install a single skill
npx skills add ConardLi/garden-skills -s web-design-engineer

# Pin to a release for CI / reproducible installs (tag-scoped tree URL)
npx skills add ConardLi/garden-skills/tree/web-design-engineer-v1.0.0/skills/web-design-engineer
```

Claude Code plugin marketplace:

```text
/plugin marketplace add ConardLi/garden-skills
/plugin install presentation-skills@garden-skills
/plugin install web-design-skills@garden-skills
/plugin install knowledge-base-skills@garden-skills
/plugin install image-generation-skills@garden-skills
```

The four plugin packs bundle web-video-presentation, web-design-engineer, kb-retriever, and gpt-image-2 respectively; beautiful-article ships through the skills CLI or a pinned `.zip`. Every formal release publishes an immutable zip with a SHA-256 checksum to GitHub Releases, which is the recommended path for unattended installs.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| web-design-engineer | 7,836 | Polished frontend work: design-read step, six design schools plus 25 anchored style recipes (Linear, Aesop, Stripe Press, Bloomberg), anti-cliché rules |
| web-video-presentation | 5,396 | Turn scripts and articles into click-driven 16:9 web presentations recordable as cinematic videos; 23 themes; pluggable TTS narration |
| gpt-image-2 | 5,262 | Image generation and editing with GPT Image 2 / OpenAI-compatible APIs; 18 visual categories, 79 prompt templates, three runtime modes |
| kb-retriever | 4,589 | Local knowledge-base retrieval across Markdown, text, PDF, and Excel with bounded search rounds and source-aware answers |
| beautiful-article | 3,234 | Turn URLs, PDFs, DOCX, Markdown, or notes into a polished, share-ready article; 11 authoring theme profiles |

The skills are versioned and released independently, with immutable `.zip` artifacts and SHA-256 checksums on GitHub Releases. Reference material ships inside the skill folders: web-design-engineer bundles its style recipes and an advanced-patterns reference, gpt-image-2 packs 18 categories and 79 templates under `references/`, and kb-retriever includes extraction references for PDF and Excel work.

## Why This Matters for Hermes Agents

Hermes agents add skills by placing SKILL.md folders in the skills directory or via the skills CLI, and every Garden skill follows that exact contract: plain Markdown, no runtime service, no lock-in. The suite covers ground most single-purpose packs skip - a Hermes agent can take a research document, turn it into a designed web presentation, synthesize narration audio, produce supporting imagery, and package a polished article, all within the skill layer. The presentation skill targets a workflow agents usually hand to humans: record-ready 1920x1080 stages with a click-driven chapter/step cursor built for screen capture. web-design-engineer supplies the visual judgment layer - the five-dial design read, style recipes, and anti-cliché blocklist - that keeps generated frontends from looking generic. Because reference docs and scripts ship inside each skill folder, the agent loads only what a task needs and keeps context bounded. The caveats are the usual ones for an agent builder: skills that call external TTS or image APIs need credentials you control, and the newest skill, beautiful-article, is still early at v0.1.0.

## Usage

| You say | What happens |
|---|---|
| "Turn this blog post into a video presentation" | web-video-presentation maps the article into narration beats and full-screen scenes on a fixed 1920x1080 stage, pausing at script, theme, outline, and audio checkpoints |
| "Build a landing page that does not look AI-generated" | web-design-engineer runs the design read, declares a design system, shows an early v0, then builds and verifies the full experience |
| "Generate a product poster from this description" | gpt-image-2 picks a category prompt template and generates the image (Mode A or B) or returns a ready-to-use prompt when no image tool is available (Mode C) |
| "Answer questions from our knowledge folder" | kb-retriever navigates the layered index files, narrows candidates, and answers with sources without flooding the context window |
| "Turn this PDF into a share-ready article" | beautiful-article plans, double-confirms, builds a self-contained article with a chosen theme, then reviews and repairs |
| "Record a cinematic video from this talk script" | The Vite + React stage renders scene by scene; narration audio is synthesized after the visual outline is approved |

## Verification

```bash
# Confirm the skills are installed
npx skills list | grep -E "web-video-presentation|web-design-engineer|gpt-image-2|kb-retriever|beautiful-article"

# Claude Code / skills-directory agents: check the skills directory
ls .claude/skills/ | grep -E "web-video-presentation|web-design-engineer|gpt-image-2|kb-retriever|beautiful-article"

# Review a SKILL.md directly before installing
curl -fsSL https://raw.githubusercontent.com/ConardLi/garden-skills/main/skills/web-design-engineer/SKILL.md | head -40
```

The raw fetch hits `main`, which is what the CLI installs by default; to review a pinned release instead, fetch the same path inside the release tag you plan to use (for example the `web-design-engineer-v1.0.0` tag).

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-video-presentation | Pass | Warn | Pass |
| web-design-engineer | Pass | Pass | Pass |
| beautiful-article | Pass | Pass | Warn |
| gpt-image-2 | Pass | Pass | Pass |

Two skills carry a single Warn each (Socket on web-video-presentation, Snyk on beautiful-article); the other sampled skills are Pass across all three scanners. The suite mixes plain Markdown with skills that shell out to local tools and APIs - kb-retriever runs grep, pdftotext, pdfplumber, and pandas locally, web-video-presentation can call external TTS providers you configure, and gpt-image-2 talks to an image API when a key is present - so normal supply-chain and credential-hygiene practice applies. The repository itself is MIT-licensed and actively maintained.

## Limitations

- web-video-presentation produces a web presentation designed for screen recording; it does not render an MP4 itself, and narration audio is optional and provider-dependent (two built-in TTS providers plus recipes for others).
- gpt-image-2 without a configured image tool drops to advisor mode: useful prompts, but no images until a Garden-mode setup or a host-native image tool is available.
- kb-retriever expects a prepared local `knowledge/` directory with layered index files, so it needs curation before it pays off.
- beautiful-article is the newest skill in the suite (v0.1.0) and carries the one Snyk Warn among sampled verdicts; review it before production use.
- Skills are released independently with pinned zips, so installs that track `main` (the CLI default) can drift between versions; pin releases when reproducibility matters.
- Snapshot data, verified Oct 9, 2026: 26,317 combined skills.sh installs across 5 indexed listings; 12,796 GitHub stars; MIT; last pushed Jul 12, 2026. Counts drift over time.

## Related

- [Hyperframes Setup](/hermes/skills/catalog/hyperframes-setup) - HTML-based video composition pipeline, a rendered-video counterpart to recorded presentations
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup) - modern web platform guidance for the frontend work these skills produce
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - interaction and motion craft for the UI layer
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the skill you need with `-s <name>` - the five skills serve different jobs, and keeping the list lean keeps the agent's context lean too.
- In web-video-presentation, approve the hard checkpoints in order (script, theme, outline, implementation mode); narration audio is synthesized only after the visual outline is approved.
- Let gpt-image-2 run its mode detection instead of assuming; advisor mode works without any API key and still saves you a production-ready prompt.
- beautiful-article pays off most when you bring the cleanest source you have and settle the article type early - its bundled retention ratios are tuned per type.
- For CI or air-gapped machines, pin the immutable release `.zip` and verify its SHA-256 checksum; never track main in an unattended pipeline.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
