---
title: "Qinyan Academic Skills - Research Library Setup"
description: "leonchaox/qinyan-academic-skills - 7.5K combined installs: 96 indexed skills from a 187-skill multilingual academic research library."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qinyan-academic-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "scientific writing", "bioinformatics"]
---

# Qinyan Academic Skills - Research Library Setup

**Source:** [leonchaox/qinyan-academic-skills](https://www.skills.sh/leonchaox/qinyan-academic-skills) via skills.sh - 7.5K combined installs across 96 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [leonchaox/qinyan-academic-skills](https://github.com/leonchaox/qinyan-academic-skills) - 1,065 stars, MIT, main branch, last pushed Jul 20, 2026; 187 skills across 18 domains under skills/, plus a first-party Qinyan suite and a Bash installer.
**Category:** Academic Research and Scientific Writing
**Quality Tier:** 🟠 Orange - one Fail cell (peer-review on Gen Agent Trust Hub) and eleven Warn cells (Snyk on nsfc-proposal, qinyan-paper-search, qinyan-paper-analysis, nssfc-proposal, qinyan-citation, qinyan-topic-analysis, research-proposal, literature-review, citation-management, research-lookup and hypothesis-generation).

Qinyan Academic Skills is a multilingual library of installable AI agent skills for end-to-end academic research, spanning literature discovery, scientific writing, grant development, bioinformatics, drug discovery, clinical research, machine learning and data analysis. The README catalogues 187 skills across 18 domains; skills.sh indexes 96 of them, and the repository's own "182 installable skills" line is a slightly stale count of the same library.

The standout is a first-party five-skill Nature-style writing suite (qinyan-nature-writing, qinyan-nature-polishing, qinyan-nature-review, qinyan-nature-figures and qinyan-nature-statistics) that moves from a defensible claim to a submission-ready manuscript. Most indexed installs are flat because the default installer pulls the whole library in one command, so per-skill counts cluster between 74 and 116 rather than ranking individual popularity.

## Installation

Install everything, which defaults to the global Claude Code skills directory:

```bash
curl -fsSL https://raw.githubusercontent.com/leonchaox/qinyan-academic-skills/main/install.sh | bash
```

For selective installs, clone and run the installer directly:

```bash
git clone https://github.com/leonchaox/qinyan-academic-skills
cd qinyan-academic-skills
bash install.sh --category 01
bash install.sh --skill scanpy
bash install.sh --project --skill scientific-writing
bash install.sh --tool codex
```

Discover and maintain skills with bash install.sh --list, --search, --status, --check-update and --update.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nsfc-proposal | 116 | Chinese NSFC grant proposals with the 2026 templates and a staged writing workflow |
| qinyan-paper-polish | 109 | polishing Chinese and English academic prose to academic norms |
| qinyan-paper-search | 108 | searching Google Scholar, Wanfang, PubMed and arXiv through the Qinyan OpenAPI |
| qinyan-paper-analysis | 99 | deep analysis of one paper: objective, methods, findings and limits |
| nssfc-proposal | 97 | Chinese NSSFC social-science proposals from the 2025 official template |
| qinyan-citation | 95 | citations via Qinyan OpenAPI in GB/T 7714, IEEE, APA, MLA, Chicago and Harvard |
| qinyan-topic-analysis | 91 | research topic suggestions and difficulty analysis from literature results |
| research-proposal | 90 | PhD research proposals for STEM, humanities and social sciences |
| scientific-writing | 88 | full-paragraph manuscripts, IMRAD structure and reporting guidelines |
| literature-review | 87 | systematic reviews across PubMed, arXiv and bioRxiv with verified citations |
| citation-management | 86 | metadata extraction, validation and BibTeX for academic references |
| research-lookup | 83 | current research lookup via Parallel Chat or Perplexity sonar-pro-search |
| peer-review | 83 | structured manuscript and grant review with checklist evaluation |
| paper-slide-deck | 81 | slide decks generated from papers with auto-detected figures |
| scientific-visualization | 80 | publication figures: multi-panel, significance annotations, colorblind-safe palettes |
| pptx-posters | 80 | research posters in HTML/CSS exported to PDF or PPTX |

The remaining 80 indexed listings range from 74 to 79 installs.

## Why This Matters for Hermes Agents

For an agent doing academic research, this library spans the whole pipeline from literature discovery to submission. The first-party Qinyan skills (paper search, analysis, polish, citation and topic analysis) handle the Chinese academic workflow, and the Nature-style five-skill suite handles the English manuscript path from claim to submission-ready text. The surrounding indexed skills fill in the tooling: databases (PubMed, OpenAlex, UniProt, PDB), bioinformatics (scanpy, scvi-tools, gget), machine learning (scikit-learn, transformers, pytorch-lightning) and document production (docx, pptx, pdf, xlsx).

The installer is the collection's strongest part for an operator. One command installs everything, and the --skill, --category and --tool flags install exactly the slice a specific task needs, target a specific agent, or keep skills inside a single project instead of globally. The flat install band is a consequence of that default: most users run the full-library install, so every skill climbs roughly together.

## Usage

| You say | What happens |
|---|---|
| Find papers for my literature review | Uses literature-review, qinyan-paper-search and database skills |
| Write the manuscript for my results | Uses scientific-writing and the Nature-style suite |
| Polish my Chinese paper | Uses qinyan-paper-polish |
| Write an NSFC proposal | Uses nsfc-proposal with the 2026 template |
| Format my citations in GB/T 7714 | Uses qinyan-citation |
| Make slides from my paper | Uses paper-slide-deck |
| Run a single-cell analysis | Uses scanpy and related bioinformatics skills |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/leonchaox/qinyan-academic-skills/main/README.md | head -40
```

Review the installer before piping it to bash:

```bash
curl -sL https://raw.githubusercontent.com/leonchaox/qinyan-academic-skills/main/install.sh | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nsfc-proposal | Pass | Pass | Warn |
| qinyan-paper-polish | Pass | Pass | Pass |
| qinyan-paper-search | Pass | Pass | Warn |
| qinyan-paper-analysis | Pass | Pass | Warn |
| nssfc-proposal | Pass | Pass | Warn |
| qinyan-citation | Pass | Pass | Warn |
| qinyan-topic-analysis | Pass | Pass | Warn |
| research-proposal | Pass | Pass | Warn |
| scientific-writing | Pass | Pass | Pass |
| literature-review | Pass | Pass | Warn |
| citation-management | Pass | Pass | Warn |
| research-lookup | Pass | Pass | Warn |
| peer-review | Fail | Pass | Pass |
| paper-slide-deck | Pass | Pass | Pass |
| scientific-visualization | Pass | Pass | Pass |
| pptx-posters | Pass | Pass | Pass |
| matlab | Pass | Pass | Pass |
| hypothesis-generation | Pass | Pass | Warn |
| research-grants | Pass | Pass | Pass |
| venue-templates | Pass | Pass | Pass |

peer-review is the single Fail cell, on Gen Agent Trust Hub. The eleven Warn cells are all on Snyk: nsfc-proposal, qinyan-paper-search, qinyan-paper-analysis, nssfc-proposal, qinyan-citation, qinyan-topic-analysis, research-proposal, literature-review, citation-management, research-lookup and hypothesis-generation. The 76 listings outside the sample carry no verdict cells in this guide.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,528 combined installs across 96 indexed listings; 1,065 GitHub stars; MIT licence; last pushed Jul 20, 2026. Counts drift over time.
- Index-versus-tree drift: the README catalogues 187 skills across 18 domains, while skills.sh indexes 96 of them; the repository's own "182 installable skills" line is a slightly stale count of the same library.
- The install band is flat, 74 to 116 installs, because the default installer pulls the whole library in one command, so per-skill install counts cluster instead of ranking individual popularity.
- Skill paths embed Chinese category directory names, so an agent guessing an ASCII path will read nothing; use the installer or the README links instead of hand-built paths.
- peer-review carries the only Fail in the sample (Gen Agent Trust Hub), and eleven listings carry a Snyk Warn, so review each skill's own security page before installing.

## Related

- [Academic Research Skills - Citations, Reviews and Writing](/hermes/skills/catalog/academic-research-skills-setup)
- [Kalarislabs Research Agent Skills - Research Workflows](/hermes/skills/catalog/kalarislabs-research-agent-skills-setup)
- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup)
- [Research Paper Writing - Academic Suite](/hermes/skills/catalog/research-paper-writing-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the Nature-style suite for a manuscript; it is the first-party differentiator and the README documents each stage.
- Install one skill at a time with --skill to keep context small; the full library is large.
- Review install.sh before piping it to bash in a locked-down environment.
- Use --tool codex or --tool cursor if Claude Code is not your agent.
- Trace a skill to its source paper via RESEARCH.md or NATURE-SKILLS.md when the guidance needs attribution.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
