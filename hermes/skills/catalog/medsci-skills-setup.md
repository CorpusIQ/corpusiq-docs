---
title: "MedSci Skills - Medical Research Agent Skills Setup"
description: "aperivue/medsci-skills: medical research agent skills for references, statistics, manuscripts and reporting-guideline checks - 6.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/medsci-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "medical research", "statistics", "manuscript"]
---

# MedSci Skills - Medical Research Agent Skills Setup

**Source:** [aperivue/medsci-skills](https://www.skills.sh/aperivue/medsci-skills) via skills.sh - 6.9K combined installs across 62 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [aperivue/medsci-skills](https://github.com/aperivue/medsci-skills) - 397 stars, MIT license, main branch, last pushed Nov 23, 2026; one SKILL.md per skill under skills/<name>/SKILL.md, with docs, demos and per-skill reference pages alongside.
**Category:** Medical and Clinical Research
**Quality Tier:** 🟡 Yellow - no Fail cells and 6 Warn cells across the 20-skill sample: Snyk Warns on meta-analysis, search-lit and revise; Socket Warns on analyze-stats, find-journal and deidentify.

MedSci Skills is a set of Agent Skills for clinical research built by a physician-researcher, covering literature and references, study design, statistics, figures, manuscript drafting, reporting-guideline checks and journal submission, plus a lane for building and validating medical-imaging AI models. It targets physicians and biomedical researchers working in Claude Code, Codex, Cursor or GitHub Copilot, and the README states plainly that every output still needs review by a qualified researcher.

The suite is anchored by check-reporting, which audits a manuscript item by item against 49 reporting guidelines and risk-of-bias tools, and by 93 deterministic detectors that recompute or cross-check specific things such as reference metadata, arithmetic, checklist items and data leakage. Install runs through npx medsci-skills install, and the README documents plugin, GitHub CLI, git clone and fixed-version install paths.

## Installation

Install every skill with the package CLI, which copies them into ~/.claude/skills/ and ~/.agents/skills/:

```bash
npx medsci-skills install
```

Claude Code users can register the plugin marketplace, then enable the plugins they want:

```bash
/plugin marketplace add Aperivue/medsci-skills
```

A GitHub CLI 2.90+ path (gh skill install Aperivue/medsci-skills --all --agent claude-code --scope user), a fixed-version pin (npx medsci-skills@6.4.0 install) and a git clone plus skills/* copy are all documented in docs/install.md. After install, restart the agent and type /orchestrate to route a plain-language request to the right skill.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| check-reporting | 181 | auditing a manuscript item by item against one of 49 reporting guidelines and risk-of-bias tools |
| meta-analysis | 177 | running a systematic review and meta-analysis from PROSPERO protocol to pooling and PRISMA reporting |
| make-figures | 155 | publication-ready figures and visual abstracts: ROC, forest, Kaplan-Meier and flow diagrams |
| analyze-stats | 154 | reproducible Python/R statistical analysis with publication tables for regression, survival and agreement |
| verify-refs | 152 | auditing references against PubMed and CrossRef and flagging fabricated or mismatched citations |
| search-lit | 151 | searching PubMed, Semantic Scholar and bioRxiv/medRxiv and generating BibTeX |

The remaining 56 indexed listings range from 20 to 145 installs.

## Why This Matters for Hermes Agents

A general agent that helps with medical writing will fabricate references, quote stale statistics and skip the reporting guidelines a journal actually enforces. MedSci Skills closes those gaps with skills that look references up in PubMed, CrossRef and OpenAlex, and with 93 deterministic detectors that recompute what can be recomputed instead of trusting the model. The highest-value skills are check-reporting, which walks a manuscript item by item against the relevant guideline, and verify-refs, which flags fabricated or mismatched citations before submission. analyze-stats and make-figures turn a de-identified data file into reproducible analysis code and publication-ready figures, and search-lit builds a verified reference list with BibTeX. For an operator the safety model is the point: deidentify runs locally with no network calls before any patient data reaches a model, and the README is explicit that a qualified researcher must review every output. The suite is not a diagnostic tool or an autonomous author, and that boundary is what makes it usable in clinical work.

## Usage

| You say | What happens |
|---|---|
| Route this research goal to the right skill | Runs orchestrate, which classifies the request and dispatches to the right skill |
| Audit my manuscript against STROBE | Runs check-reporting and marks each item PRESENT, PARTIAL or MISSING |
| Verify my references are real | Runs verify-refs against PubMed and CrossRef and writes qc/reference_audit.json |
| Analyze this de-identified dataset | Runs analyze-stats, proposes a plan, then produces reproducible Python/R and tables |
| Make a Kaplan-Meier figure | Runs make-figures for a publication-ready plot after checking the journal AI-image policy |
| Run a meta-analysis | Runs meta-analysis from PROSPERO protocol through pooling and PRISMA reporting |
| Draft the study protocol | Runs write-protocol for full-prose Background, Design, Sample Size and Statistical Plan |

## Verification

Confirm the reporting-guideline skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/aperivue/medsci-skills/main/skills/check-reporting/SKILL.md | head -40
```

Spot-check the reference and statistics skills to confirm the flat skills/ layout:

```bash
curl -sL https://raw.githubusercontent.com/aperivue/medsci-skills/main/skills/verify-refs/SKILL.md | head -30
```

```bash
curl -sL https://raw.githubusercontent.com/aperivue/medsci-skills/main/skills/analyze-stats/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| check-reporting | Pass | Pass | Pass |
| meta-analysis | Pass | Pass | Warn |
| make-figures | Pass | Pass | Pass |
| analyze-stats | Pass | Warn | Pass |
| verify-refs | Pass | Pass | Pass |
| search-lit | Pass | Pass | Warn |
| write-paper | Pass | Pass | Pass |
| find-journal | Pass | Warn | Pass |
| design-study | Pass | Pass | Pass |
| present-paper | Pass | Pass | Pass |
| fulltext-retrieval | Pass | Pass | Pass |
| self-review | Pass | Pass | Pass |
| calc-sample-size | Pass | Pass | Pass |
| manage-refs | Pass | Pass | Pass |
| write-protocol | Pass | Pass | Pass |
| deidentify | Pass | Warn | Pass |
| humanize | Pass | Pass | Pass |
| revise | Pass | Pass | Warn |
| clean-data | Pass | Pass | Pass |
| orchestrate | Pass | Pass | Pass |

The 20-skill sample has no Fail cells and six Warn cells - Snyk Warns on meta-analysis, search-lit and revise, and Socket Warns on analyze-stats, find-journal and deidentify - while 42 of the 62 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 6,888 combined installs across 62 indexed listings; 397 GitHub stars; MIT license; last pushed Nov 23, 2026. Counts drift over time.
- Only 20 of the 62 indexed listings carry a published skills.sh security verdict; the other 42 have no published verdict in the sampled set.
- The README counts 54 skills while the index carries 62 listings: eight pre-v6 names (preprocess-imaging, profile-imaging, explainability, model-evaluation, model-validation, uncertainty-imaging, architecture-zoo and model-sourcing) remain indexed as their own listings until v7.
- Several bundled materials are not MIT: guideline templates, CSL citation styles and some checklist summaries carry their own terms including CC BY-NC, per THIRD-PARTY-NOTICES.md.
- The optional pdf_to_md.py dependency uses pymupdf4llm (AGPL-3.0), installed separately by the user.
- These are research productivity tools, not clinically validated decision support, and a qualified researcher must review every output.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)
- [AlterLab Academic Skills - Research to Submission](/hermes/skills/catalog/alterlab-academic-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with /orchestrate: it routes a plain-language goal to the right skill instead of forcing you to memorize 54 skill names.
- Run /verify-refs before submission and treat a FABRICATED or MISMATCHED result as a blocker; the skill reports and never edits references.
- De-identify patient data with /deidentify (local, no network) before any other skill touches the file.
- Pin a version for reproducibility when a paper will cite the tool: npx medsci-skills@6.4.0 install.
- Use the demo projects in the repository as worked examples for diagnostic accuracy, meta-analysis and survey epidemiology pipelines.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
