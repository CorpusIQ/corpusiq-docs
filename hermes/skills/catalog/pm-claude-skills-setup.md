---
title: "PM Claude Skills - Product Management Skill Library"
description: "mohitagw15856/pm-claude-skills: 5.4K combined installs across 96 listings; plain-markdown agent skills for product management and professional work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pm-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "product management", "PRD", "SOP"]
---

# PM Claude Skills - Setup Guide

**Source:** [mohitagw15856/pm-claude-skills](https://www.skills.sh/mohitagw15856/pm-claude-skills) via skills.sh - 5.4K combined installs across 96 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 1,572 stars, MIT license, `main` branch, last pushed 2026-11-17; 8,740 files in the tree, with each skill held in several copies (see below)
**Category:** Product management / professional writing agent skills
**Quality Tier:** 🟡 Yellow - 59 Pass and 1 Warn across the 20 sampled listings; no Fail.

pm-claude-skills is a library of plain-markdown Agent Skills, each a single `SKILL.md` file that teaches an agent to produce one professional deliverable: a PRD, a stakeholder update, a postmortem, a lease decode. The README describes the collection in its own words as "an open-source library of 1374 Agent Skills", organized across 167 bundles and 35 professions. skills.sh indexes 96 of them, totalling 5,402 combined installs.

The 96 indexed listings are a sample of a much larger tree. The repository holds 8,740 files, and one skill appears many times: as a canonical copy under `skills/`, as a bundle-organized copy under `plugins/<bundle>/skills/`, as translations under `i18n/` and `skills-i18n/`, as versioned releases under `skill-releases/`, as Cursor `.mdc` exports under `exports/cursor/`, and inside agent templates under `templates/`. So the install figures below count one listing per canonical skill name, not one folder per topic.

## Installation

The installer copies markdown files into the tool's config folder; uninstalling deletes them.

```bash
npx pm-claude-skills add
```

In Claude Code, open `/plugin`, search `pm-skills`, and install from the Anthropic directory. To install one bundle instead of the whole library, use `npx pm-claude-skills add --bundle pm-essentials`; all 167 bundles are listed in `docs/catalogue.md`. `npx pm-claude-skills doctor` lists what is installed and what is stale.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| teaching-lesson-plan | 170 | Design a structured lesson plan for any subject, with objectives, activities, timing and assessment. |
| team-offsite-planner | 99 | Plan a team offsite with a weighted purpose split, agenda, logistics runbook and follow-through. |
| sop-writer | 82 | Write a Standard Operating Procedure with purpose, scope, procedure steps, quality checks and version control. |
| youtube-script-writer | 80 | Write a high-retention YouTube script with hooks, a beat-by-beat body and retention devices. |
| user-research-synthesis | 70 | Synthesize user research into themed insights with prevalence data, quotes and prioritized feature requests. |
| competitive-analysis | 69 | Build competitive landscape docs with feature matrices, positioning maps and strategic recommendations. |
| patient-communication | 68 | Write plain-English patient letters, leaflets and test-result communications for healthcare contexts. |
| meeting-notes | 68 | Structure meeting notes with decisions, action items, open questions and next steps. |
| financial-due-diligence | 68 | Generate a financial due diligence checklist and analysis framework for investments and acquisitions. |
| project-status-report | 66 | Write a project status report with RAG ratings, milestone progress, risks and decisions needed. |
| prd-template | 66 | Create a Product Requirements Document with problem statement, user stories, requirements and success metrics. |
| executive-summary | 64 | Write an executive summary for any document, report or proposal, readable in under 3 minutes. |
| pricing-strategy | 63 | Structure pricing, tier design and rollout decisions for SaaS and digital products. |
| job-application | 63 | Tailor a CV and cover letter to a job description, optimized for ATS. |
| incident-postmortem | 63 | Write a blameless incident postmortem with timeline, root cause and action items. |
| stakeholder-update | 62 | Write a BLUF-led stakeholder update with status, metrics, risks and decisions needed. |

The remaining 80 indexed listings range from 48 to 61 installs.

## Why This Matters for Hermes Agents

Each skill is a plain-markdown `SKILL.md`: a description that tells the agent when to load it, plus a framework, an output template and quality checks. The operator payoff is that a request in plain words ("turn these call notes into a PRD, a risk register and a stakeholder update") resolves to three skills that return finished documents, not advice about writing them. The library is MIT-licensed and local: skills are inert markdown, telemetry is off unless opted in, and the only thing that leaves the machine is the prompt to your model provider. Breadth is the trade-off to weigh: the README reports that none of the 183 skills it rates high-stakes currently carries a review by a qualified professional, so read a `SKILL.md` before trusting it on a high-stakes decision. For Hermes agents the practical move is to install by bundle, scope the loaded skills to the work, and treat the unverified long tail as exactly that.

## Usage

| You say | What happens |
|---|---|
| "Turn these six call notes into a PRD, risk register and stakeholder update" | Loads user-research-synthesis, prd-template and stakeholder-update and returns the three documents. |
| "Decode this job ad and tell me where I am weak" | Loads job-application to tailor a CV and cover letter against the description. |
| "Write a blameless postmortem for last night's outage" | Loads incident-postmortem and produces a timeline, root cause, impact summary and action items. |
| "Write a patient letter about these test results" | Loads patient-communication and produces a plain-English letter with clear next steps. |
| "Make me a content calendar for next month" | Loads content-calendar and produces topics, formats, channels and copy hooks. |

## Verification

Confirm the canonical English skills exist on `main` before installing. The PRD skill returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/skills/prd-template/SKILL.md | head -20
```

Skills live under several folders: canonical copies in `skills/`, bundle copies in `plugins/<bundle>/skills/`, and translations in `i18n/` and `skills-i18n/`. After installing, `npx pm-claude-skills doctor` lists what is installed and what is stale.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| teaching-lesson-plan | Pass | Pass | Pass |
| team-offsite-planner | Pass | Pass | Pass |
| sop-writer | Pass | Pass | Pass |
| youtube-script-writer | Pass | Pass | Pass |
| user-research-synthesis | Pass | Pass | Pass |
| competitive-analysis | Pass | Pass | Pass |
| patient-communication | Pass | Pass | Pass |
| meeting-notes | Pass | Pass | Pass |
| financial-due-diligence | Pass | Pass | Pass |
| project-status-report | Pass | Pass | Pass |
| prd-template | Warn | Pass | Pass |
| executive-summary | Pass | Pass | Pass |
| pricing-strategy | Pass | Pass | Pass |
| job-application | Pass | Pass | Pass |
| incident-postmortem | Pass | Pass | Pass |
| stakeholder-update | Pass | Pass | Pass |
| investor-pitch-deck | Pass | Pass | Pass |
| design-critique | Pass | Pass | Pass |
| budget-variance-analysis | Pass | Pass | Pass |
| content-calendar | Pass | Pass | Pass |

The sample covers 20 of the 96 indexed listings. prd-template carries the single Warn, from Gen Agent Trust Hub; every other sampled cell passes all three auditors. The remaining 76 listings are unverified on skills.sh.

## Limitations

- Snapshot data, verified 2026-11-17: 5,402 combined installs across 96 indexed listings; 1,572 GitHub stars; MIT; last pushed 2026-11-17. Counts drift over time.
- The README's own count (1,374 skills across 167 bundles and 35 professions) is far larger than the 96 skills.sh listings; the index samples a subset, and the 8,740-file tree holds many copies of each skill across translations, bundles, Cursor exports, releases and templates.
- skills.sh security verdicts cover 20 of the 96 listings; the other 76 are not verified there.
- The 21 Duet-ready skills are built for unattended agents but, per the README, none has been tested on Duet because it is a waitlisted preview.
- The README reports that none of the 183 skills it rates high-stakes currently has a review by a qualified professional.

## Related

- [Claude Office Skills](/hermes/skills/catalog/claude-office)
- [n8n Skills - Workflow Automation for Business Operators Setup](/hermes/skills/catalog/n8n-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by bundle (`npx pm-claude-skills add --bundle pm-essentials`) rather than the whole library; scope what the agent loads to the work.
- Read one `SKILL.md` before trusting it; `skills/lease-decoder/SKILL.md` is a representative first read.
- Re-run `npx pm-claude-skills doctor` to find stale installs; the same add command updates them.
- Verify a single skill against its published SHA-256 (`shasum -a 256` versus the hashes in `.well-known/agent-skills.json`).
- The Duet watchers draft and always ask before acting, but none has been tested on Duet; test the approval gate before unattended use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
