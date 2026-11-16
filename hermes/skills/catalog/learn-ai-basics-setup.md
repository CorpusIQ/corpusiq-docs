---
title: "Learn AI Basics - Devpost Learner Curriculum"
description: "challengepost/learn-ai-basics - 11.1K combined installs across 9 indexed listings: a six-step learner curriculum from idea to shipped hackathon demo."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/learn-ai-basics-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "curriculum", "learning", "hackathon"]
---

# Learn AI Basics - Setup Guide

**Source:** [challengepost/learn-ai-basics](https://www.skills.sh/challengepost/learn-ai-basics) via skills.sh - 11.1K combined installs across 9 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 84 stars, MIT license, `main` branch, last pushed 2026-10-05, six `SKILL.md` files under `skills/`, one per step
**Category:** Beginner AI curriculum and learner workflow
**Quality Tier:** 🟢 Green - every sampled skill passes all three auditors.

This is the Devpost Learn hackathon curriculum packaged as agent skills. The six skills form a single learner sequence, 1-start through 6-ship, that walks a beginner from an idea to a shipped hackathon demo. It works in any harness that reads `SKILL.md`, including Claude Code, Codex and Cursor.

The skills are not independent tools; they are stages that hand state to each other through a `devpost/` folder in the project. Each planning document carries a draft or approved status in its frontmatter, and every skill opens by inspecting that folder, saying back where the learner is, and routing forward or to the first unfinished step.

## Installation

```bash
npx skills add challengepost/learn-ai-basics --all -y
```

Prerequisites: node and git installed, and an empty folder set aside for the project. Invoke each skill by name; starting a fresh conversation between skills is fine because the `devpost/` files carry the context forward.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| 5-build | 1,844 | Verified, committed build steps with hands-on review, then a short personalized learning wrap-up. |
| 6-ship | 1,843 | Prepare the demo video and public GitHub repository, then write your own submission and exit-survey answers. |
| 4-spec | 1,843 | How it is built: clarify an unknown, weigh options, and agree on a technical plan. |
| 3-prd | 1,843 | A learner-led product interview grounded in scope: screens, layout, style, behavior, edge cases, now/later. |
| 2-scope | 1,843 | Find or sharpen the idea, identify its kernel, define done, and keep it proof-of-concept sized. |
| 1-start | 1,842 | Understand the six steps, check the workspace, and introduce the idea and experience. |

The remaining 3 indexed listings are 4-ship, 3-build and 2-plan at 1 install each, earlier names the index still carries.

## Why This Matters for Hermes Agents

The interesting thing here is not any single skill but the discipline the sequence enforces: plan before you build. A generic agent asked to build a hackathon project will reach for code immediately; this curriculum makes it interview the learner about scope, product and plan first, and only then build. That ordering is the actual lesson the learner takes away.

State is the second design choice worth copying. There is no separate progress file: the `devpost/` folder is the state, each document carrying a draft or approved status in its frontmatter. A fresh conversation at any point costs nothing, because every skill opens by reading that folder and routing to the first unfinished step. That is a portable pattern for any multi-skill agent workflow.

The pacing is adaptive. Onboarding separates plan-first experience from coding experience, and those preferences carry forward, so newcomers get guided support while familiar users get concise explanations. The agent interviews, probes and organizes; the learner supplies the ideas and decisions.

## Usage

| You say | What happens |
|---|---|
| "I have an idea for a hackathon project" | 1-start checks the workspace and records the idea and experience. |
| "Help me find my idea" | 2-scope sharpens the idea, names the kernel and keeps it proof-of-concept sized. |
| "Let's define the product" | 3-prd runs a learner-led interview for screens, layout, style and behavior. |
| "How should I build this?" | 4-spec clarifies the unknown and agrees on a technical plan. |
| "Let's build it" | 5-build runs verified, committed build steps with hands-on review. |
| "Help me ship my submission" | 6-ship prepares the demo video, public repo and learner-written submission. |

## Verification

Check the skill files and install:

```bash
curl -fsSL https://raw.githubusercontent.com/challengepost/learn-ai-basics/main/skills/1-start/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/challengepost/learn-ai-basics/main/skills/6-ship/SKILL.md | head -30
npx skills add challengepost/learn-ai-basics --all -y
```

Each skill opens by inspecting the project's `devpost/` folder, so after the first step the documents rather than the chat history carry the context forward.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 1-start | Pass | Pass | Pass |
| 2-scope | Pass | Pass | Pass |
| 3-prd | Pass | Pass | Pass |
| 4-spec | Pass | Pass | Pass |
| 5-build | Pass | Pass | Pass |
| 6-ship | Pass | Pass | Pass |

The skills are Markdown plus document templates, and every sampled verdict is a Pass. Setup excludes the learner profile and local credential files from commits by default, but that does not make AI conversations private or remove already-tracked content.

## Limitations

- Snapshot data, verified 2026-11-15: 11,061 combined installs across 9 indexed listings; 84 GitHub stars; MIT; last pushed 2026-10-05. Counts drift over time.
- The install index carries three earlier names, 4-ship, 3-build and 2-plan, that have no counterpart in the current `skills/` tree.
- The curriculum expects node, git and an empty project folder; it is not a drop-in for an existing repository.
- Shipping still requires a human: the agent can interview and identify gaps but only corrects spelling and grammar in your copy, never drafts or rewrites it.
- This is a beginner-oriented curriculum; the value is in following the sequence rather than jumping straight to the build step.

## Related

- [skill-creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [Dev Event Organizer Skills - Conferences and Meetups Setup](/hermes/skills/catalog/dev-event-organizer-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the sequence in order the first time; the later skills assume the earlier documents exist in `devpost/`.
- Keep the `devpost/` folder in version control but leave the learner profile out, which is the repository's own default.
- Use speech-to-text; the README notes it helps a lot for the interview-heavy skills.
- "Looks good" is a real approval: one clear sign-off flips a document from draft to approved, with no second confirmation.
- Let the agent ask questions rather than answer them: the learner supplies the ideas, and the flipped interaction is the value.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
