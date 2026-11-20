---
title: "Academic Research Skills - Citations, Reviews and Writing"
description: "KalarisLabs research-agent-skills: 12.2K combined installs across 93 listings that turn any agent into a research co-scientist."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kalarislabs-research-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "scientific writing", "citation verification", "literature review"]
---

# Academic Research Skills - Setup Guide

**Source:** [kalarislabs/research-agent-skills](https://www.skills.sh/kalarislabs/research-agent-skills) via skills.sh - 12.2K combined installs across 93 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)

**GitHub:** 171 stars, NOASSERTION licence (the repository README badge shows MIT), main branch, last pushed Nov 19, 2026. Skills live in `skills/<name>/SKILL.md` as plain folders with references and tested scripts, plus `catalog/skills.json`, docs and benchmark assets.

**Category:** Academic research and scientific writing

**Quality Tier:** 🟠 Orange - 1 Fail and 6 Warn among the 16 sampled skills.sh verdicts (literature-review fails the Gen Agent Trust Hub); NOASSERTION licence.

KalarisLabs maintains a free, open-source library of agent skills that give a general-purpose agent the methods of a careful scientist, from literature search and hypothesis generation through experimental design, data analysis, writing, citation checking and peer review. Each skill is a folder with a `SKILL.md` playbook, reference material and tested scripts, loaded only when the current job needs it.

The library is large, the README counts 280+ skills across AI, ML, biology, chemistry, medicine and physics, and it positions itself against the specific failure researchers hit with general agents: fabricated or wrong citations, slop-style prose, and irreproducible analysis. The skills.sh index surfaces 93 listings, a fraction of the full skill catalog.

## Installation

Install with the open skills.sh CLI (Node.js 18+, no account):

```bash
npx skills add KalarisLabs/research-agent-skills
```

That opens a picker. To skip it, use flags such as `--all`, `--skill citation-verification apa7`, `--list`, `--agent claude-code`, `--global` or `--yes`. Update installed skills later with `npx skills update`.

A Python route is also available:

```bash
uvx research-agent-skills install citation-verification
pip install research-agent-skills
research-agent-skills install --bundle research-essentials
```

Claude Code can install curated field bundles from the plugin marketplace:

```
/plugin marketplace add KalarisLabs/research-agent-skills
/plugin install biology-research@research-agent-skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| citation-verification | 420 | Verify every reference exists and matches its metadata before submission |
| unslop-academic-writing | 303 | Remove AI slop from papers, theses, grants and rebuttals |
| literature-review | 302 | Run systematic reviews with PRISMA flow diagrams and verified citations |
| scientific-writing | 291 | Draft and audit manuscripts with evidence provenance and reporting-guideline coverage |
| scientific-critical-thinking | 211 | Evaluate claims, biases, confounders and evidence quality |
| peer-review | 194 | Prepare constructive, evidence-bounded review drafts |
| experimental-design | 194 | Design experiments and studies before data is collected |
| scientific-visualization | 176 | Create and audit truthful, publication-ready figures |
| statistical-analysis | 175 | Test selection, effect sizes, power and APA-formatted reporting |
| paper-lookup | 170 | Search 18 scholarly APIs for papers, citations and open-access text |
| apa7 | 169 | Format papers and references in APA Style 7th edition |
| ml-paper-writing | 168 | Write ML and AI papers for NeurIPS, ICML, ICLR, ACL, AAAI and COLM |
| systematic-review-prisma | 163 | Plan and report systematic reviews to PRISMA 2020 standards |
| hypothesis-generation | 163 | Formulate evidence-bounded questions, hypotheses and analysis plans |
| reproducibility-statement | 160 | Prepare data and code availability statements and venue checklists |
| bibtex-hygiene | 155 | Clean, deduplicate and validate BibTeX bibliographies |
| rebuttal-and-response-to-reviewers | 143 | Write reviewer responses, conference rebuttals and appeals |
| abstract-and-title | 140 | Write and sharpen titles, abstracts, keywords and highlights |
| research-lookup | 140 | Compile scholarly evidence for a manuscript or evidence summary |

The remaining 74 indexed listings range from 99 to 137 installs.

## Why This Matters for Hermes Agents

This is the clearest large-scale example of a skill library aimed at one high-stakes job: turning an agent into a co-scientist whose output can be trusted. The citation-verification skill alone encodes a workflow every research-facing agent needs, checking each reference against Crossref, DataCite, OpenAlex and arXiv and flagging retractions before a claim reaches the draft.

The benchmarking stance is what sets it apart. The README commits benchmark results rather than claiming them, including a whole-brain study run end to end with the skills, so the capability claims are measured rather than asserted. For builders, that is a model for how a skill collection documents what its skills actually do.

The per-venue skills, apa7, ieee-transactions, springer-lncs, acm-sigconf, nature-portfolio and the rest, are a practical reminder that submission-ready output depends on format-specific knowledge an agent will not have by default.

## Usage

| You say | What happens |
|---|---|
| "Verify every reference in refs.bib" | citation-verification checks each entry against scholarly databases and flags mismatches |
| "Unslop this introduction without changing any claims" | unslop-academic-writing rewrites the prose while preserving the claims |
| "Run a systematic review of X" | literature-review searches, screens, synthesizes and draws a PRISMA diagram |
| "How should I set up this experiment?" | experimental-design chooses a design, randomization and blocking |
| "Write a rebuttal to these reviews" | rebuttal-and-response-to-reviewers drafts point-by-point replies under length limits |
| "Format my paper for NeurIPS" | ml-paper-writing applies venue templates and checks citations |

## Verification

After installing, confirm the skill folders are present under `skills/` in the repository checkout and that your harness discovers them. To review one skill before relying on it, fetch its definition directly:

```bash
curl -sL https://raw.githubusercontent.com/KalarisLabs/research-agent-skills/main/skills/citation-verification/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

One Fail sits in the sample: literature-review fails the Gen Agent Trust Hub. Six Warn cells sit in Snyk: citation-verification, literature-review, scientific-writing, paper-lookup, ml-paper-writing and systematic-review-prisma. Every sampled skill passes Socket.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| citation-verification | Pass | Pass | Warn |
| unslop-academic-writing | Pass | Pass | Pass |
| literature-review | Fail | Pass | Warn |
| scientific-writing | Pass | Pass | Warn |
| scientific-critical-thinking | Pass | Pass | Pass |
| peer-review | Pass | Pass | Pass |
| experimental-design | Pass | Pass | Pass |
| scientific-visualization | Pass | Pass | Pass |
| statistical-analysis | Pass | Pass | Pass |
| paper-lookup | Pass | Pass | Warn |
| apa7 | Pass | Pass | Pass |
| ml-paper-writing | Pass | Pass | Warn |
| systematic-review-prisma | Pass | Pass | Warn |
| hypothesis-generation | Pass | Pass | Pass |
| reproducibility-statement | Pass | Pass | Pass |
| bibtex-hygiene | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 19, 2026: 12,160 combined installs across 93 indexed listings; 171 GitHub stars; NOASSERTION licence; last pushed Nov 19, 2026. Counts drift over time.
- The skills.sh index carries 93 listings while the repository catalogs 283 skills, so install counts cover only the indexed slice.
- The GitHub metadata reports NOASSERTION while the repository README shows an MIT badge and a LICENSE file, so the two sources disagree and neither should be treated as settled.
- The literature-review skill carries a Gen Agent Trust Hub Fail in the sampled verdicts; review its behavior and any network calls before production use.
- Several skills require network access or API keys (research-lookup needs api.parallel.ai, paper-lookup queries many external scholarly APIs), so confirm the environment before relying on them.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup)
- [AlterLab Academic Skills - Research to Submission](/hermes/skills/catalog/alterlab-academic-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the field-specific picker rather than `--all`: a research agent rarely needs 283 skills at once.
- Install the citation-verification skill first; it is the highest-value guard against the most common AI research failure.
- Use `--global` only if you want every project to see the skills; the default is project-scoped.
- The Claude Code bundles, research-essentials, ml-research, biology-research and the rest, are curated entry points when you do not want to choose per skill.
- No npm package exists under this name; any `research-agent-skills` package on the npm registry is not from this project.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
