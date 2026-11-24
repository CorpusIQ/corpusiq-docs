---
title: "Novel Writer Skills - Chinese Fiction Writing Suite Setup"
description: "wordflowlab/novel-writer-skills - 7.7K combined installs: Chinese long-form fiction writing skills and Claude Code slash commands."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/novel-writer-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "fiction writing", "novel", "claude code"]
---

# Novel Writer Skills - Chinese Fiction Writing Suite Setup

**Source:** [wordflowlab/novel-writer-skills](https://www.skills.sh/wordflowlab/novel-writer-skills) via skills.sh - 7.7K combined installs across 13 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [wordflowlab/novel-writer-skills](https://github.com/wordflowlab/novel-writer-skills) - 274 stars, MIT license, main branch, last pushed Oct 20, 2025; skills and slash commands live under templates/skills/ and templates/commands/ with a TypeScript CLI under src/ and plugins under plugins/.
**Category:** Creative Writing and Fiction
**Quality Tier:** 🟢 Green - all 13 sampled skills pass Gen Agent Trust Hub, Socket, and Snyk.

Novel Writer Skills is a Chinese-language toolset for long-form fiction writing built for Claude Code, published by wordflowlab. It combines a seven-step methodology (constitution, specify, clarify, plan, tasks, write, analyze) with Agent Skills that activate automatically, plus genre knowledge bases for romance, mystery, and fantasy. It is the Claude Code focused companion to the author's cross-platform novel-writer project.

The README and documentation are written in Chinese, and the repository has been inactive since October 2025. The 13 indexed listings map to skill directories under templates/skills/, but several canonical names differ from their on-disk directory names, for example novel-writer-workflow-guide lives at templates/skills/quality-assurance/workflow-guide and story-consistency-monitor at templates/skills/quality-assurance/consistency-checker.

## Installation

Install the npm CLI:

```bash
npm install -g novel-writer-skills
```

Initialize a new novel project:

```bash
novelwrite init my-novel
```

Initialize in the current directory, or with the authentic-voice plugin:

```bash
novelwrite init --here
novelwrite init my-novel --plugins authentic-voice
```

The README distributes through npm and generates Claude Code slash commands and Agent Skills into the project's .claude/ directory; it does not document a skills.sh installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| novel-writer-workflow-guide | 1,981 | guiding the seven-step novel writing methodology |
| story-consistency-monitor | 727 | checking character, world, and timeline consistency |
| fantasy-world-building | 642 | fantasy genre world-building conventions |
| natural-dialogue-techniques | 606 | natural dialogue and character voice |
| scene-structure-techniques | 548 | scene structure and pacing |
| romance-novel-conventions | 503 | romance genre conventions and emotional rhythm |
| mystery-novel-conventions | 473 | mystery genre techniques and clue management |
| style-detector | 398 | detecting writing style needs and loading the matching style guide |
| getting-started-guide | 387 | getting started with the tool |
| pre-write-checklist | 378 | enforcing the mandatory pre-chapter file checklist |
| forgotten-elements-reminder | 377 | surfacing forgotten story elements |
| setting-detector | 353 | detecting story settings and activating genre knowledge bases |
| requirement-detector | 350 | detecting writing requirement keywords and loading matching docs |

All 13 indexed listings clear the 300-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Novel Writer Skills is a worked example of how a creative domain can be encoded as a repeatable agent workflow. The seven-step methodology (constitution, specify, clarify, plan, tasks, write, analyze) turns a long-form fiction project into a sequence an agent can execute chapter by chapter, with tracking files for plot, timeline, characters, and relationships so context persists between sessions.

For Hermes builders, the interesting part is the detector-and-knowledge-base pattern. setting-detector, style-detector, and requirement-detector watch for keywords and activate the right genre or style guide, which is the same routing pattern a QA or coding skill library uses. The pre-write checklist shows a concrete guard against long-context drift: it forces the agent to reload the mandatory context files before each chapter.

The caveats are real: the repository is Chinese-first, has not been updated since October 2025, and depends on Claude Code slash commands for the full experience. Treat it as a proven template for fiction workflows more than a maintained dependency.

## Usage

| You say | What happens |
|---|---|
| Start a new novel project | Uses novelwrite init to scaffold the project structure |
| Define my story's constitution | Uses /constitution to create the creative constitution |
| Write chapter one | Uses /write with the pre-write checklist loaded first |
| Check my timeline for contradictions | Uses story-consistency-monitor for consistency checks |
| Make this dialogue sound more natural | Uses natural-dialogue-techniques for dialogue and voice |
| Write a fantasy setting | Uses fantasy-world-building for world-building conventions |
| Track my plot and character relationships | Uses /track and /relations to update the tracking files |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/wordflowlab/novel-writer-skills/main/README.md | head -40
```

Confirm the workflow guide skill body is present (the indexed name novel-writer-workflow-guide maps to the workflow-guide directory):

```bash
curl -sL https://raw.githubusercontent.com/wordflowlab/novel-writer-skills/main/templates/skills/quality-assurance/workflow-guide/SKILL.md | head -30
```

Initialized projects carry skills under .claude/skills/ and commands under .claude/commands/.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| novel-writer-workflow-guide | Pass | Pass | Pass |
| story-consistency-monitor | Pass | Pass | Pass |
| fantasy-world-building | Pass | Pass | Pass |
| natural-dialogue-techniques | Pass | Pass | Pass |
| scene-structure-techniques | Pass | Pass | Pass |
| romance-novel-conventions | Pass | Pass | Pass |
| mystery-novel-conventions | Pass | Pass | Pass |
| style-detector | Pass | Pass | Pass |
| getting-started-guide | Pass | Pass | Pass |
| pre-write-checklist | Pass | Pass | Pass |
| forgotten-elements-reminder | Pass | Pass | Pass |
| setting-detector | Pass | Pass | Pass |
| requirement-detector | Pass | Pass | Pass |

All 13 sampled skills pass Gen Agent Trust Hub, Socket, and Snyk.

## Limitations

- Snapshot data, verified Nov 24, 2026: 7,723 combined installs across 13 indexed listings; 274 GitHub stars; MIT license; last pushed Oct 20, 2025. Counts drift over time.
- The repository has not been pushed since October 2025, so the toolset is effectively unmaintained and may lag current Claude Code releases.
- The README and documentation are written in Chinese; there is no English README in the repository.
- The skills.sh canonical names differ from the on-disk directory names (for example novel-writer-workflow-guide is the workflow-guide directory and story-consistency-monitor is consistency-checker), so install-by-name requires the index mapping.
- The skills.sh index ships descriptions for only four listings (pre-write-checklist, requirement-detector, setting-detector, and style-detector); the rest are name-level.

## Related

- [Creative Writing Skills - Fiction Agent Suite Setup](/hermes/skills/catalog/creative-writing-skills-setup)
- [Screenwriting Skills - Screenwriting and Dramaturgy Suite](/hermes/skills/catalog/screenwriting-skills-setup)
- [Sepia - De-AI Writing Skills for Any Agent](/hermes/skills/catalog/sepia-writing-skills-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the getting-started skill and the novelwrite init scaffold rather than installing every skill.
- Run the /constitution to /analyze sequence in order; the methodology is designed as a pipeline.
- The pre-write checklist only works when the mandatory context files exist, so keep character, world, and timeline files up to date.
- Use the bash scripts under .specify/templates/scripts/ for automation or CI, since they mirror the slash commands.
- Expect Chinese-language prompts and documentation, and plan for translation if your agent works in English.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
