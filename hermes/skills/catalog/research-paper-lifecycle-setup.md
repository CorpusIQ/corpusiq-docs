---
title: "Research Paper Lifecycle Skills - Academic Writing Setup"
description: "shaishavmaisuria/research-paper-lifecycle-skills - 4.5K combined installs: 42 skills for literature review, academic writing and submission."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/research-paper-lifecycle-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "research", "academic writing", "paper submission"]
---

# Research Paper Lifecycle Skills - Academic Writing Setup

**Source:** [shaishavmaisuria/research-paper-lifecycle-skills](https://www.skills.sh/shaishavmaisuria/research-paper-lifecycle-skills) via skills.sh - 4.5K combined installs across 42 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [shaishavmaisuria/research-paper-lifecycle-skills](https://github.com/shaishavmaisuria/research-paper-lifecycle-skills) - 63 stars, Apache-2.0 license, main branch, last pushed Oct 24, 2026; 42 skills under skills/<name>/SKILL.md with references/ and scripts/ subdirectories, plus docs/, assets/ and a .claude-plugin/marketplace.json.
**Category:** Academic Research and Writing
**Quality Tier:** 🟡 Yellow - nine sampled skills carry a Snyk Warn cell (literature-review, find-papers and verify-results among them); none carry a Fail.

Shaishav Maisuria's research-paper-lifecycle-skills is a 42-skill suite that spans the whole academic-paper lifecycle, from discovering and fetching papers through writing and polishing, to verifying citations and claims, submitting, responding to reviews and presenting. It is built as a copilot rather than an auto-writer: skills draft and check while the author stays responsible, and every writing workflow routes new references through citation verification instead of trusting plausible text.

The suite is field-agnostic and copyright-conscious. Paper content is fetched only from legal open-access sources on demand and never bundled, and venue rules are built or re-checked from live CFPs and author instructions. Its install band is flat: every one of the 42 listings sits between 95 and 146 installs because the whole suite installs as a single unit, so per-skill counts do not reflect individual popularity.

## Installation

Add the complete suite with the Agent Skills CLI:

```bash
npx skills add ShaishavMaisuria/research-paper-lifecycle-skills
```

List what is included, or install a single skill:

```bash
npx skills add ShaishavMaisuria/research-paper-lifecycle-skills --list
npx skills add ShaishavMaisuria/research-paper-lifecycle-skills --skill preflight-check
```

Install into a supported agent:

```bash
npx skills add ShaishavMaisuria/research-paper-lifecycle-skills --agent claude-code
```

Claude Code plugin bundles are exposed in .claude-plugin/marketplace.json:

```text
/plugin marketplace add ShaishavMaisuria/research-paper-lifecycle-skills
/plugin install paper-submission@research-paper-lifecycle-skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| verify-citations | 146 | checking BibTeX entries for fabricated or mismatched records |
| literature-review | 141 | building a structured, citation-grounded literature review |
| check-originality | 132 | checking for plagiarism, self-plagiarism and text recycling |
| find-papers | 124 | key-free scholarly search across DBLP, Crossref, Semantic Scholar and arXiv |
| verify-claims | 122 | auditing load-bearing claims against evidence and citations |
| polish-prose | 119 | de-AI-ifying and tightening prose without changing claims |
| fetch-paper | 117 | fetching a legal open-access copy from a DOI or arXiv ID |
| verify-results | 113 | checking reported metrics against local code outputs |
| draft-related-work | 112 | drafting a related-work section against verified references |
| study-exemplars | 111 | studying best papers from a target venue |
| write-talk-script | 111 | writing a timed, word-budgeted talk script |
| preflight-check | 110 | linting LaTeX for desk-reject risks before submission |
| simulate-reviewers | 109 | venue-calibrated mock peer review |
| match-style | 108 | aligning a draft to the author's voice or venue style |
| refactor-structure | 108 | repairing argument structure and narrative flow |
| fit-page-limit | 106 | compressing or expanding a paper to a target length |
| rehearse-qa | 104 | practicing hostile and curious Q&A |
| write-rebuttal | 103 | drafting rebuttals and author responses |
| polish-tables-figures | 102 | cleaning up figures, tables, captions and crossrefs |
| test-research-code | 102 | making research code runnable and repeatable |
| write-abstract | 101 | drafting, revising or linting a venue-aware abstract |
| triage-reviews | 101 | converting raw reviews into a response plan |
| draft-survey | 101 | producing a ranked reading list and survey draft |
| paper-profile | 100 | recording paper positioning and preferences |
| make-slides | 100 | turning a paper into a conference talk deck |
| assess-paper | 100 | one overall paper-health report |

The remaining 16 indexed listings range from 95 to 99 installs.

## Why This Matters for Hermes Agents

This suite is the closest thing to a complete, human-led pipeline for research support work, and its verification-first posture lines up with how Hermes agents are expected to operate. The verify-citations gate refuses to let new references ship without checking them against Crossref, DBLP, Semantic Scholar and arXiv, which is the academic equivalent of evidence-before-claims. preflight-check and parse-cfp build requirements from live venue sources and mark anything unsourced as unverified, matching the habit of verifying live before claiming a job is done. The bundled checks are deterministic stdlib-only Python scripts, so they are a clean model for shipping repeatable, reviewable verification steps rather than opaque prompt-only advice. The flat install band means popularity is not a signal here: judge the suite by its coverage of the lifecycle, from idea to camera-ready. For a Hermes agent asked to support a researcher, this is a high-value single install with an explicit boundary: it never submits a paper or predicts acceptance.

## Usage

| You say | What happens |
|---|---|
| Will this get desk-rejected at an IEEE conference? | preflight-check lints main.tex against the CFP for template, page-limit, anonymization and checklist risks |
| Verify my refs.bib | verify-citations checks entries against scholarly metadata and flags fabricated records |
| Find missing related work | find-papers searches the literature, then draft-related-work positions the paper |
| Write the abstract for SIGSPATIAL | write-abstract drafts a venue-aware abstract with keyword blocks |
| Simulate Reviewer 2 | simulate-reviewers runs a venue-calibrated mock review with a fix list |
| Turn these reviews into a rebuttal plan | triage-reviews builds a response matrix, then write-rebuttal drafts the response |
| Make slides for my talk | make-slides turns the paper into a conference deck |

## Verification

Confirm the suite is discoverable, then review one raw SKILL.md before installing:

```bash
curl -sL https://raw.githubusercontent.com/ShaishavMaisuria/research-paper-lifecycle-skills/main/skills/preflight-check/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| verify-citations | Pass | Pass | Pass |
| literature-review | Pass | Pass | Warn |
| check-originality | Pass | Pass | Warn |
| find-papers | Pass | Pass | Warn |
| verify-claims | Pass | Pass | Pass |
| polish-prose | Pass | Pass | Pass |
| fetch-paper | Pass | Pass | Warn |
| verify-results | Pass | Pass | Warn |
| draft-related-work | Pass | Pass | Warn |
| study-exemplars | Pass | Pass | Warn |
| write-talk-script | Pass | Pass | Pass |
| preflight-check | Pass | Pass | Pass |
| simulate-reviewers | Pass | Pass | Warn |
| match-style | Pass | Pass | Warn |
| refactor-structure | Pass | Pass | Pass |

Nine sampled skills carry a Snyk Warn cell; every sampled skill passes the Gen Agent Trust Hub and Socket checks.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,454 combined installs across 42 indexed listings; 63 GitHub stars; Apache-2.0 license; last pushed Oct 24, 2026. Counts drift over time.
- The install band is flat (95 to 146 installs) because the whole suite installs as one unit, so per-skill install counts do not reflect individual popularity.
- Venue rules and CFP facts can go stale; the suite itself instructs users to re-check them live before relying on them.
- Skills never submit a paper, predict acceptance, or invent citations or venue facts.
- The workflow is LaTeX and Overleaf centric, so Word-first workflows need adaptation.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)
- [Research Paper Writing Pipeline - Hermes Skill Setup Guide](/hermes/skills/catalog/research-paper-writing-setup)
- [Academic Research Skills - Citations, Reviews and Writing](/hermes/skills/catalog/kalarislabs-research-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start a new paper with paper-profile, then literature-review, write-abstract, draft-related-work and polish-prose.
- Run verify-citations before any draft, rebuttal or camera-ready leaves the machine.
- Install single skills with --skill <name> when you only need one stage of the pipeline.
- Keep generated reports in paper-workspace/ and preferences in .paper-memory/ so they stay with the paper.
- Re-check venue rules against the live CFP before submission, since profiles can go stale.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
