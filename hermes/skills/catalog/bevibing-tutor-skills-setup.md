---
title: "Bevibing Tutor Skills - Obsidian Study Vault and Quiz Setup"
description: "bevibing/tutor-skills: 4.8K combined installs across 2 listings; turns PDFs, docs, and codebases into Obsidian study vaults plus a quiz tutor."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bevibing-tutor-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "obsidian", "study vault", "quiz tutor"]
---

# Bevibing Tutor Skills - Setup Guide

**Source:** [bevibing/tutor-skills](https://www.skills.sh/bevibing/tutor-skills) via skills.sh - 4.8K combined installs across 2 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 1,413 stars, MIT licence, `main` branch, last pushed 2026-02-28. Two skills under `skills/` (`tutor-setup`, `tutor`), each a `SKILL.md` with references, plus `install.sh` and `uninstall.sh`.
**Category:** Learning and study
**Quality Tier:** 🟡 Yellow - 1 Warn among 2 sampled skills (tutor-setup); MIT licence.

Bevibing Tutor Skills turns PDFs, documents, and source-code projects into an Obsidian StudyVault, then quizzes you on the result with concept-level progress tracking. The two Claude Code skills close the loop from content to comprehension: `tutor-setup` builds the vault, and `tutor` drills it with four-question rounds graded against a per-concept proficiency badge.

The repository README still names its former owner RoundTable02 in its install commands; the repo now lives under bevibing/tutor-skills, which is the name skills.sh indexes.

## Installation

The README documents a one-line install, but it still writes the former owner. Install from the current owner:

```bash
npx skills add bevibing/tutor-skills
```

Or clone and run the bundled installer:

```bash
git clone https://github.com/bevibing/tutor-skills.git
cd tutor-skills
./install.sh
```

Then start Claude Code, generate a vault with `/tutor-setup`, and quiz it with `/tutor`. Uninstall with `./uninstall.sh` (or remove `~/.claude/skills/tutor-setup` and `~/.claude/skills/tutor` manually).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tutor | 2,604 | Quiz an Obsidian StudyVault: diagnostic assessment, section review, weak-area drills, and concept-level progress tracking with emoji badges. |
| tutor-setup | 2,191 | Turn PDFs, text, web pages, or a source-code project into an Obsidian StudyVault of notes, dashboards, and practice questions, in Document or Codebase mode. |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

For an agent asked to study or onboard a person, the useful output is not a pile of notes, it is a structured vault plus a way to prove the material was absorbed. `tutor-setup` gives the agent a deterministic pipeline from raw sources to interlinked concept notes with practice questions, and `tutor` closes the loop by quizzing and tracking mastery per concept.

The two skills are plain `SKILL.md` files with references, so any harness that reads skill files can load them, including Hermes. The StudyVault output is plain Obsidian Markdown with wiki-links, so the result is portable and inspectable rather than locked inside a chat transcript.

## Usage

| You say | What happens |
|---|---|
| "Turn this PDF folder into study notes" | tutor-setup scans the directory, builds topic notes, a dashboard, and practice questions, then writes an Obsidian vault. |
| "Quiz me on the vault" | tutor detects the StudyVault, reads the dashboard, and offers a diagnostic, drill, or section session. |
| "Onboard me to this codebase" | tutor-setup detects project markers and generates a Codebase Mode onboarding vault with module notes and exercises. |
| "Drill my weak areas" | tutor targets concepts flagged weak in prior sessions and rephrases missed questions. |
| "Where am I stuck?" | tutor reports concept-level proficiency with weak, fair, good, and mastered badges. |

## Verification

Probe one skill on the `main` branch before installing. Both return 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/bevibing/tutor-skills/main/skills/tutor/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/bevibing/tutor-skills/main/skills/tutor-setup/SKILL.md
```

Then install the pack and ask your agent to generate a StudyVault from a folder of PDFs.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tutor | Pass | Pass | Pass |
| tutor-setup | Pass | Pass | Warn |

The sample covers both indexed listings; tutor-setup carries a single Warn.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,795 combined installs across 2 indexed listings; 1,413 GitHub stars; MIT licence; last pushed 2026-02-28. Counts drift over time.
- The README still references the former RoundTable02 owner in its install and clone commands; the repository has moved to bevibing/tutor-skills.
- The output is an Obsidian vault, so it expects Obsidian (recommended) to open and navigate the generated notes.
- The skills require Claude Code (or an npx-skills-compatible agent) and are built for study and onboarding, not for general document processing.

## Related

- [Obsidian Agent Skills - Markdown, Bases and Canvas](/hermes/skills/catalog/obsidian-skills-setup)
- [Obsidian Visual Skills - Canvas, Excalidraw and Mermaid](/hermes/skills/catalog/axton-obsidian-visual-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/tutor-setup` first, then `/tutor`; the quiz skill only works against a vault that setup generated.
- Point it at a folder with real source files (PDF, MD, HTML, EPUB) so the dashboard has content to map.
- Use Codebase Mode for onboarding a new developer: it traces request and data flows into per-module notes and exercises.
- Check the per-concept badges before a review session so the drill targets actual gaps rather than known material.
- If the install picks up the wrong agent, install to a specific one with `-a` (for example `-a claude-code`).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
