---
title: "Agentara Skills - AI Builder Skill Suite Setup"
description: "agentara/skills - 5.7K combined installs: 24 skills for AI builders covering AIGC, engineering review, health and productivity workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentara-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "ai builders", "code review", "aigc"]
---

# Agentara Skills - AI Builder Skill Suite Setup

**Source:** [agentara/skills](https://www.skills.sh/agentara/skills) via skills.sh - 5.7K combined installs across 24 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [agentara/skills](https://github.com/agentara/skills) - 635 stars, MIT, main branch, last pushed Sep 29, 2026; one SKILL.md per skill, grouped into aigc/, engineering/, health/, productivity/ and entertainment/ directories with reference files alongside.
**Category:** AI Builder Workflows and Creative Generation
**Quality Tier:** 🟡 Yellow - the 20-skill sample has Warn cells but no Fail cells: article-to-html (Socket), doctor-strange (Snyk), feature-dev-loop (Gen Agent Trust Hub), publish-research-site (Socket and Snyk) and engineering-code-review (Snyk).

Agentara Skills is a personal library of Claude Code skills, packaged as installable prompt extensions, that gives a coding agent practical capabilities across five areas: AIGC (image stylization, video planning, storyboards, key art), engineering (code review and small-change workflow), health (triage, lab interpretation, parenting), productivity (feature orchestration, article-to-HTML, scenario simulation) and entertainment (a World Cup predictor). Each skill is a single SKILL.md with reference files kept alongside, so it installs into Claude Code, Codex and other agents that read the Agent Skills format.

Two groups stand out for builders. The engineering skills adapt Google Engineering Practices under CC-BY 3.0 into a review-and-change workflow of six skills, and the productivity group carries feature-dev-loop, an end-to-end orchestration for PR-sized features. The health skills are Chinese-language and answer a different audience than the code-oriented majority, which is worth knowing before you surface them to a team.

## Installation

The README installs one skill at a time via that skill's directory URL. To install the doctor-strange skill:

```bash
npx skills add https://github.com/agentara/skills/blob/main/skills/productivity/doctor-strange/ -y -g
```

Replace the path with the directory URL of any other skill. To install manually, clone and symlink or copy the skill directory into the agent skill folders:

```bash
git clone https://github.com/agentara/skills.git
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.agents/skills/doctor-strange
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.claude/skills/doctor-strange
```

Copy or symlink any skill directory into ~/.agents/skills/<skill-name>/ and ~/.claude/skills/<skill-name>/ so Claude Code and other agents can discover it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| video-storyboard | 1,062 | storyboard image boards and video-generation prompt scripts for specific scenes |
| super-daddy | 623 | family-doctor-style parenting and child health management in Chinese |
| video-character-design | 410 | character design specs and sheets for video, animation and AI video workflows |
| video-plan | 325 | planning short-form video scripts by duration, story arc and timed scenes |
| lab-interpreter | 287 | interpreting medical lab reports uploaded as images, PDFs or text |
| video-poster-design | 273 | cinematic movie poster concepts and final key art images |
| presentation-design | 251 | generating a 6-slide presentation design board as one composite image |
| article-to-html | 221 | rendering markdown into a single-file paper-style HTML page |
| emergency-triage | 213 | triaging urgent or semi-urgent symptoms and preparing hospital questions |
| doctor-strange | 213 | causal sand-table simulations of future scenarios via parallel subagents |
| mega-goal-prompt | 196 | generating a /goal mega prompt for Claude Code or Codex CLI |
| soviet-storybook-grotesque | 192 | transforming photos into vintage Eastern European children's book illustrations |
| feature-dev-loop | 188 | end-to-end orchestration for PR-sized feature development |

The remaining 11 indexed listings range from 35 to 143 installs.

## Why This Matters for Hermes Agents

An agent doing real engineering work spends most of its time on code review, change description and PR hygiene, and the engineering group here is built for exactly that: engineering-code-review judges a change for code health and approval risk, engineering-small-prs splits a large change into reviewable chunks, and engineering-review-feedback handles reviewer pushback as the author. Together they encode Google's own engineering practices in a form the agent can apply, which is a stronger starting point than general instructions.

The AIGC group is the other half: video-storyboard, video-character-design, video-plan and video-poster-design form a pipeline from a loose theme to a storyboard to a finished poster, each holding continuity constraints (character, wardrobe, prop and location) that a single prompt tends to drop. For builders who need output that looks designed rather than generated, presentation-design and article-to-html turn prose into a slide board or a self-contained HTML page.

Two cautions apply. The health skills (super-daddy, lab-interpreter and emergency-triage) are Chinese-language and deal with medical and parenting decisions, so an English-only operator should not surface them to end users without review. And the security sample carries Warn cells on five skills, detailed below, which matters if you install the whole set rather than one file at a time.

## Usage

| You say | What happens |
|---|---|
| Review this PR before we merge | Uses engineering-code-review for code health and approval risk |
| Split this 2,000-line change into reviewable parts | Uses engineering-small-prs to sequence small PRs |
| Turn this markdown into a pretty single-page document | Uses article-to-html to render a paper-style HTML file |
| Storyboard my 60-second product video | Uses video-plan and video-storyboard to time scenes and boards |
| Write a /goal so Claude keeps working on this migration | Uses mega-goal-prompt to interview and emit the mega prompt |
| What should I do about this pain before the doctor | Uses emergency-triage to narrow causes and suggest a department |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/agentara/skills/main/README.md | head -40
```

Confirm the top skill body is present before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/agentara/skills/main/skills/aigc/video-storyboard/SKILL.md | head -30
```

Confirm the doctor-strange skill body before simulation work:

```bash
curl -sL https://raw.githubusercontent.com/agentara/skills/main/skills/productivity/doctor-strange/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-storyboard | Pass | Pass | Pass |
| super-daddy | Pass | Pass | Pass |
| video-character-design | Pass | Pass | Pass |
| video-plan | Pass | Pass | Pass |
| lab-interpreter | Pass | Pass | Pass |
| video-poster-design | Pass | Pass | Pass |
| presentation-design | Pass | Pass | Pass |
| article-to-html | Pass | Warn | Pass |
| emergency-triage | Pass | Pass | Pass |
| doctor-strange | Pass | Pass | Warn |
| mega-goal-prompt | Pass | Pass | Pass |
| soviet-storybook-grotesque | Pass | Pass | Pass |
| feature-dev-loop | Warn | Pass | Pass |
| publish-research-site | Pass | Warn | Warn |
| torn-paper-collage-poster | Pass | Pass | Pass |
| engineering-small-prs | Pass | Pass | Pass |
| engineering-code-review | Pass | Pass | Warn |
| engineering-review-comments | Pass | Pass | Pass |
| engineering-review-feedback | Pass | Pass | Pass |
| engineering-change-descriptions | Pass | Pass | Pass |

The Warn cells sit on article-to-html (Socket), doctor-strange (Snyk), feature-dev-loop (Gen Agent Trust Hub), publish-research-site (Socket and Snyk) and engineering-code-review (Snyk); there are no Fail cells. The four listings outside the sample, engineering-emergency-changes, world-cup-predictor, gunpla-poster and portrait-clone, carry no verdict cells here, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,666 combined installs across 24 indexed listings; 635 GitHub stars; MIT license; last pushed Sep 29, 2026. Counts drift over time.
- The engineering skills are adapted from Google Engineering Practices under CC-BY 3.0, not MIT, and carry source attribution in each SKILL.md; the rest of the repository is MIT.
- The health skills (super-daddy, lab-interpreter and emergency-triage) are Chinese-language, which limits them to Chinese-speaking users and teams.
- Four of the 24 listings were outside the verdict sample and carry no security cells in this guide.
- The README installs one skill at a time via a directory URL; there is no single-command whole-collection install documented.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup](/hermes/skills/catalog/dot-skills-setup)
- [AI Dev Standards Skills - Design Setup](/hermes/skills/catalog/ai-dev-standards-skills-setup)
- [Skill From Masters - Domain Expert Methodology Suite Setup](/hermes/skills/catalog/skill-from-masters-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time; the engineering set is the highest-value group for a builder, and feature-dev-loop plus engineering-code-review covers most code-review incidents.
- Ask the video-plan skill for the story arc before any character or storyboard work; it fixes duration and visual style first.
- Keep article-to-html and presentation-design separate in intent: one renders a paper-style document, the other produces a six-slide visual board.
- The doctor-strange simulations store projections as persistent memory, so treat its RECALL mode as a soft prior rather than a prediction.
- If you surface the health skills, tell users up front they are Chinese-language and not a substitute for medical advice.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
