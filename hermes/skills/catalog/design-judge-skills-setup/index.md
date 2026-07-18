---
title: "Design Judge Skills — Full Setup Guide for Hermes Agent"
description: "Install and configure SeanJ1ang/design-judge-skills — 5 evidence-driven agent skills for design award research, evaluation, matching, entry writing, and submission readiness. Works across Hermes Agent, Claude Code, Codex, OpenClaw, and OpenCode."
---

# Design Judge Skills — Setup Guide

**Repo:** [SeanJ1ang/design-judge-skills](https://github.com/SeanJ1ang/design-judge-skills)
**Stars:** 25 · **Forks:** 6 · **License:** Apache 2.0
**Language:** Python · **Skills:** 5 + 1 shared support package
**Agent Support:** Hermes Agent, Claude Code, Codex, OpenClaw, OpenCode

## Overview

Design Judge Skills decomposes the end-to-end design award submission process into five modular, evidence-driven agent skills. Each skill operates independently with well-defined boundaries — you can use one, several, or all five as your workflow demands.

The skills are configured for 11 major design awards: iF DESIGN AWARD, iF DESIGN STUDENT AWARD, Red Dot Product Design, Red Dot Design Concept, IDEA, DIA, K-Design, GOOD DESIGN AWARD Japan, Core77, James Dyson, and EPDA. Award rules, deadlines, fees, eligibility, and categories are verified against official pages at runtime.

## The 5 Skills

### 1. design-award-search — Find Winning Precedents

Retrieve and verify winning entries in the same category from official award archives.

**Use when:** You need examples of what won in your category, or want to understand what juries reward.

**Trigger phrase:** "Find winning cases for [product type] in [award/category]"

**Example prompt:**
```
Use design-award-search to find verified winning entries for a rehabilitation training device
in the iF DESIGN AWARD product category. Verify each case against the official iF archive.
```

### 2. design-evaluation — Score Design Quality

Evaluate design quality and presentation expression using evidence-based rubrics with transparent scoring.

**Use when:** You need an objective assessment of a design before submitting it to awards.

**Trigger phrase:** "Evaluate this design for [award] submission"

**Example prompt:**
```
Use design-evaluation to assess the attached design. Maturity level is "student concept."
Output design quality score, presentation expression score, evidence confidence, and critical issues.
```

**Output structure:**
- Design quality score (with rubric alignment)
- Presentation expression score
- Evidence confidence (what's verified vs. assumed)
- Critical issues (blockers before submission)

### 3. design-award-match — Compare Award Fit

Compare awards, tracks, and submission categories against project characteristics to find the best fit.

**Use when:** You have multiple award options and need to decide where to submit.

**Trigger phrase:** "Compare award fit for [project]"

**Example prompt:**
```
Use design-award-match to compare iF Student, Red Dot Design Concept, DIA, Core77,
and James Dyson for this project. Output fit scores with explanations for each.
```

### 4. design-information-prep — Prepare Submission Text

Prepare award submission text constrained to source materials, with field-by-field drafting and word-count validation.

**Use when:** You have design materials and need to write submission copy.

**Trigger phrase:** "Prepare submission text for [award]"

**Example prompt:**
```
Use design-information-prep to prepare IDEA award submission text from the attached materials.
First list missing facts, then output English draft per field with word count verification.
```

### 5. design-submission-check — Final Readiness

Check a submission package against the current official rules of the target award. Outputs a go / conditional go / no-go verdict.

**Use when:** Your submission package is complete and needs a final compliance review.

**Trigger phrase:** "Check submission readiness for [award]"

**Example prompt:**
```
Use design-submission-check to verify this submission package against the current iF DESIGN AWARD
official rules. Output go / conditional go / no-go with itemized issues.
```

## Shared Support Package

`design-judge-shared` is a shared support package used by the other five skills. It's automatically included when any skill is installed. You don't invoke it directly.

## Design Principles (from the repo)

These principles govern all five skills. They're worth understanding before you rely on the output:

1. **Primary sources first.** Award rules and cases verified against official pages. Search summaries and third-party pages are for discovery only.
2. **Facts vs. inference separated.** User materials, model inferences, and items requiring user confirmation are labeled distinctly.
3. **Transparent scoring.** Fit and evaluation scores aid decisions but don't simulate judging panels or predict outcomes.
4. **Single-responsibility modules.** Search, evaluation, matching, text prep, and submission check don't cross boundaries.
5. **No fake judging.** Skills align with public criteria but don't simulate undisclosed judge preferences.

## Installation

### Option 1: npx skills (Recommended — works with any agent)

Install individual skills:

```bash
npx skills add SeanJ1ang/design-judge-skills --skill design-award-search -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-evaluation -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-award-match -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-information-prep -g -y
npx skills add SeanJ1ang/design-judge-skills --skill design-submission-check -g -y
```

The `-g` flag installs at global/user scope. The `-y` flag skips confirmation prompts. Remove `-y` for interactive installation.

### Option 2: Hermes Agent — Manual Skill Installation

Copy the skill directories to your Hermes profile:

```bash
# Clone the repo
git clone https://github.com/SeanJ1ang/design-judge-skills.git /tmp/design-judge-skills

# Copy skills to Hermes profile
cp -r /tmp/design-judge-skills/skills/* ~/.hermes/profiles/corpusiq/skills/

# Clean up
rm -rf /tmp/design-judge-skills
```

Then reload skills in your Hermes session or restart.

### Option 3: Claude Code

```bash
# In Claude Code session
/install-skill SeanJ1ang/design-judge-skills/design-award-search
```

Replace `design-award-search` with any of the five skill names.

### Option 4: Codex

```bash
codex skills install SeanJ1ang/design-judge-skills --skill design-award-search
```

## Verification

After installation, verify skills are loaded:

**Hermes Agent:**
```bash
ls ~/.hermes/profiles/corpusiq/skills/design-*/
```

**npx skills:**
```bash
npx skills list | grep design-
```

**Quick test:** Describe a design and ask the agent which award to target. The agent should invoke `design-award-match`:

```
I have a wearable health monitor for elderly users. It tracks heart rate, fall detection,
and medication reminders. Which design awards should I target?
```

## Workflow

The five skills form a pipeline but can be used independently:

```
Design Materials
  ├─ Find winning precedents ──────> design-award-search
  ├─ Evaluate design quality ──────> design-evaluation
  └─ Match awards & categories ───> design-award-match
                                         │
                                         v
                                design-information-prep
                                         │
                                         v
                                design-submission-check
```

A complete submission flow typically starts with evaluation or matching, moves to text preparation once the target award is selected, and ends with a submission check.

## Supported Awards

| Award | Category Coverage | Source Verification |
|-------|------------------|-------------------|
| iF DESIGN AWARD | Product, Communication, Packaging, Service Design, UX, Professional Concept | Official iF archive |
| iF DESIGN STUDENT AWARD | Student concepts across all categories | Official iF archive |
| Red Dot Product Design | 51 product categories | Official Red Dot archive |
| Red Dot Design Concept | Concepts, prototypes, student work | Official Red Dot archive |
| IDEA | Professional + Student | IDSA official site |
| DIA (Design Intelligence Award) | Product, Concept, Digital | DIA official site |
| K-Design Award | Product, Space/Architecture, Communication, Service, Fashion | K-Design official site |
| GOOD DESIGN AWARD Japan | All categories | G-Mark official archive |
| Core77 Design Awards | 23 categories | Core77 official site |
| James Dyson Award | Student design + engineering | James Dyson Foundation |
| EPDA (European Product Design Award) | Product, Packaging, Interface | EPDA official site |

Award rules, deadlines, and fees are verified at runtime. Do not cache these — they change annually.

## Limitations

- **Runtime verification required.** Award rules, deadlines, and fees must be re-verified against official pages at runtime. The skills don't cache this data.
- **Language.** Primary documentation is Chinese with English translation. Skills accept materials in either language.
- **Not a judging simulation.** Evaluation scores are heuristic aids, not predictions of jury outcomes.
- **11 awards configured.** Additional awards require adding configuration to the shared support package.

## Security

- The skills read design materials you provide and search official award websites. No data is sent to third-party services.
- All source code is in Python and the shared support package. Review `skills/design-judge-shared/` before using with confidential designs.
- License: Apache 2.0 — safe for commercial use.

## Troubleshooting

### "Skill not found" after npx install

The `npx skills` CLI caches skills. Try:
```bash
npx skills list --refresh | grep design-
```

### Award rules mismatch

Awards update annually. If the skill references outdated rules, specify the year in your prompt:
```
Use design-submission-check for iF DESIGN AWARD 2027 rules.
```

### Language issues

The repo is primarily Chinese with English README. If outputs appear in Chinese, specify language in your prompt:
```
Output all results in English.
```

---

*Setup guide by CorpusIQ. Skill repo by [SeanJ1ang](https://github.com/SeanJ1ang). Licensed Apache 2.0.*
