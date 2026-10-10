---
title: "MiniMax AI Skills - Official Dev & Document Suite Setup"
description: "Setup guide for minimax-ai/skills - 48.3K combined installs. Official MiniMax dev suite: web scaffolds plus pptx, docx, pdf, and xlsx generators."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/minimax-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "minimax", "document generation", "frontend development"]
---

# MiniMax AI Skills - Setup Guide

**Source:** [minimax-ai/skills](https://www.skills.sh/minimax-ai/skills) via skills.sh - 48.3K combined installs across 24 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [minimax-ai/skills](https://github.com/minimax-ai/skills) (13,683 stars, MIT; pushed 2026-04-18; layout `skills/<name>/SKILL.md`)
**Category:** Development / Documents / Multimodal
**Quality Tier:** 🟡 Beta - official MiniMax; README marks Beta; last pushed Apr 2026; mixed sampled verdicts - see Security

MiniMax AI Skills is the official skill suite from MiniMax, aimed at AI coding agents. It covers structured, production-quality guidance for frontend, fullstack, Android, iOS, Flutter, React Native, and shader development, plus a document and media family: PowerPoint, Word, PDF, and Excel generators alongside image, voice, music, and video workflows that call MiniMax APIs.

The suite is distinct from its video-focused sibling: minimax-ai/minimax-h3 is a separate, documented repo for AI video prompt writing and generation, while this repo is the development and document suite. Across the 24 indexed listings, the document generators dominate the install chart, followed by the web and mobile development skills.

---

## Installation

### Claude Code

```bash
claude plugin marketplace add https://github.com/MiniMax-AI/skills
claude plugin install minimax-skills
```

### Cursor

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.cursor/minimax-skills
```

Then point the skills path in your Cursor settings at `~/.cursor/minimax-skills/skills/`. Windows setup details live in the repo's `.cursor-plugin/INSTALL.md`.

### Codex

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.codex/minimax-skills

mkdir -p ~/.agents/skills
ln -s ~/.codex/minimax-skills/skills ~/.agents/skills/minimax-skills
```

Restart Codex to discover the skills; see `.codex/INSTALL.md` for Windows instructions and details.

### OpenCode

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.minimax-skills

mkdir -p ~/.config/opencode/skills
ln -s ~/.minimax-skills/skills/* ~/.config/opencode/skills/
```

Restart OpenCode to discover the skills; `.opencode/INSTALL.md` has the details.

### VS Code

No standalone VS Code extension is shipped. Run Claude Code, Codex, or OpenCode in the integrated terminal, or use Cursor for native local-skills configuration.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pptx-generator | 5,814 | Generating, editing, and reading PowerPoint decks: PptxGenJS creation, XML edits, markitdown text extraction |
| minimax-docx | 4,444 | DOCX creation, editing, and formatting via OpenXML SDK; three pipelines with an XSD validation gate |
| minimax-pdf | 3,742 | Creating, filling, and reformatting PDFs with a token-based design system and 15 cover styles |
| minimax-xlsx | 3,721 | Spreadsheets end to end: XML-template creation, pandas analysis, zero-format-loss editing, formula recalculation |
| fullstack-dev | 3,340 | Backend architecture and frontend-backend integration: REST, auth, real-time, databases, release checklist |
| frontend-dev | 3,118 | Premium UI with cinematic animation (Framer Motion, GSAP) and AI-generated media on React/Next.js plus Tailwind |
| vision-analysis | 2,624 | Image analysis: describe, OCR, UI mockup review, chart extraction (Community; MiniMax VL API with GPT-4V fallback) |
| android-native-dev | 2,615 | Native Android with Kotlin/Jetpack Compose, Material Design 3, accessibility, and performance work |
| shader-dev | 2,375 | GLSL effects: ray marching, SDF modeling, fluid simulation, particles, post-processing (ShaderToy-compatible) |
| ios-application-dev | 2,102 | iOS apps with UIKit, SnapKit, and SwiftUI; Dynamic Type, Dark Mode, and HIG compliance |
| gif-sticker-maker | 2,002 | Turning photos into 4 animated GIF stickers with captions via MiniMax image and video APIs |
| flutter-dev | 1,948 | Cross-platform Flutter: widgets, Riverpod/Bloc, GoRouter, and testing strategies |
| react-native-dev | 1,888 | React Native and Expo: components, navigation, state, networking, deployment, and SDK upgrades |
| pr-review | 1,726 | Automated validation checks and quality review criteria for pull requests |
| mmx-cli | 1,606 | MiniMax command-line workflows |
| minimax-music-gen | 1,566 | Vocal songs, instrumentals, and covers via the MiniMax Music API, with basic and advanced-control modes |

The remaining 8 indexed listings range from 71 to 1,332 installs.

## Why This Matters for Hermes Agents

Most agent skill libraries stop at software scaffolding; this one ships a content factory too. Seven development skills span web, fullstack, native mobile (Android and iOS), cross-platform (Flutter and React Native), and GLSL shaders - targets that many libraries skip entirely - with performance, accessibility, and testing guidance. The document skills follow real pipelines rather than loose prompting: PPTX built through PptxGenJS and XML workflows, DOCX through OpenXML with an XSD validation gate, XLSX with zero-format-loss editing and formula recalculation. That structure is what agent builders need for output that survives contact with a stakeholder: deterministic steps, validation, and format fidelity. Media skills then round out the suite by calling MiniMax APIs for images, voice, music, and video, so one install can generate the assets a build needs, not just the code around them.

## Usage

| You say | What happens |
|---|---|
| Build the deck for our board update | pptx-generator creates a full deck from scratch: cover, table of contents, content, section dividers, summary |
| Turn this CSV export into a formatted report | minimax-xlsx analyzes with pandas and applies financial formatting without losing the original file's format |
| Fill in this PDF form and restyle it | minimax-pdf fills form fields, then reformats the document with print-ready typography |
| Scaffold a landing page with cinematic animation | frontend-dev pairs React/Next.js and Tailwind patterns with Framer Motion and GSAP |
| Review this GLSL fragment shader | shader-dev covers techniques from ray marching through post-processing |
| Turn my pet photos into chat stickers | gif-sticker-maker returns 4 animated GIF stickers with captions |
| Write a launch song for our product | minimax-music-gen generates a vocal track or instrumental from a one-line prompt |

## Verification

In Claude Code, confirm `minimax-skills` appears in the `/plugin` list after installing. For Codex and OpenCode, check that the symlink resolves (`~/.agents/skills/minimax-skills` and `~/.config/opencode/skills/`); for Cursor, confirm the configured skills path points at `~/.cursor/minimax-skills/skills/`. Before installing, review the exact instructions the agent will read - skills live at `skills/<name>/SKILL.md`. For example, fetch the PowerPoint generator skill file at `https://raw.githubusercontent.com/minimax-ai/skills/main/skills/pptx-generator/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pptx-generator | Warn | Pass | Warn |
| minimax-docx | Pass | Pass | Warn |
| minimax-pdf | Pass | Warn | Pass |

## Limitations

- Sampled verdicts are mixed: Gen Agent Trust Hub Warn and Snyk Warn on pptx-generator, Snyk Warn on minimax-docx; only three skills were sampled.
- Beta status is explicit in the README: skills, APIs, and configuration formats may change without notice.
- Last pushed 2026-04-18, so parts of the suite may lag current MiniMax model and API versions.
- Media-generation skills call MiniMax APIs at runtime and are not self-contained.
- vision-analysis is marked Community (not Official) in the README's source column.
- VS Code gets no standalone extension; the README routes VS Code users through Claude Code, Codex, or OpenCode in the integrated terminal.
- Snapshot data, verified Oct 10, 2026: 48,257 combined installs across 24 indexed listings; 13,683 GitHub stars; MIT; last pushed 2026-04-18. Counts drift over time.

## Related

- [MiniMax H3 Skills - AI Video Prompt Writing & Generation Setup](/hermes/skills/catalog/minimax-h3-skills-setup) - the separate, video-focused sibling suite from the same publisher
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) - official vendor skills for the React/Next.js stack used by frontend-dev
- [Media Use Setup - Agent Media OS for HyperFrames (182.7K installs)](/hermes/skills/catalog/media-use-setup) - media assembly pipelines that complement the MiniMax generators
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Claude Code users do not need a clone: `claude plugin marketplace add https://github.com/MiniMax-AI/skills` then `claude plugin install minimax-skills`.
- Install the four document generators (pptx, docx, pdf, xlsx) as a group; they share conventions and cover adjacent handoffs.
- pr-review doubles as the repo's own contribution gate: run `python .claude/skills/pr-review/scripts/validate_skills.py` to see the checks it enforces.
- For Cursor, Codex, and OpenCode the path is clone plus symlink; follow the per-tool INSTALL.md files, especially for Windows.
- Try gif-sticker-maker or minimax-music-gen first if you want to see the MiniMax API workflows in action before wiring them into a pipeline.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
