---
title: "Research-Claw Research Plugins - Academic Skills Setup Guide"
description: "wentorai/research-plugins: 350+ academic research skills, MCP configs and plugins for Research-Claw and AI agents - 8.2K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wentorai-research-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "research tools"]
---

# Research-Claw Research Plugins - Setup Guide

**Source:** [wentorai/research-plugins](https://www.skills.sh/wentorai/research-plugins) via skills.sh - 8.2K combined installs across 96 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** [wentorai/research-plugins](https://github.com/wentorai/research-plugins) - 320 stars, MIT licence, main branch, last pushed Jun 19, 2026. Skills live under `skills/<category>/<subcategory>/SKILL.md` across six top-level categories (524 files in the tree).
**Category:** Academic Research
**Quality Tier:** 🟡 Yellow - 5 Warn among 16 sampled verdicts (Snyk: paper-review, deep-research, social-science, geoscience; Socket: ocr-translate); MIT licence.

The research-plugins package is the built-in skill library for Research-Claw (Wentor AI's academic research agent) and works with 40+ agent frameworks through the skills protocol. The README counts 433 academic skills, 34 TypeScript API tools wired to 18 free scholarly databases (OpenAlex, CrossRef, PubMed, arXiv and others), and six curated resource lists. Skills load progressively: six category entries point to 40 subcategory indexes, which point to the individual guides, so an agent never loads the whole library into context at once.

The indexed listings on skills.sh show 96 rows because the marketplace API caps at 96, so the listing count and combined-install figure are floors rather than exact totals. The repository itself documents the fuller 433-skill corpus.

## Installation

For Research-Claw or OpenClaw users, install as a plugin (loads all skills plus the 34 API tools):

```bash
openclaw plugins install @wentorai/research-plugins
```

The plugin installs to `~/.openclaw/extensions/` and auto-loads after a gateway restart.

For Claude Code, Cursor, Windsurf, OpenCode and other skills-protocol frameworks (SKILL.md files only, no API tools):

```bash
npx skills add wentorai/research-plugins
```

Uninstall:

```bash
# OpenClaw / Research-Claw
rm -rf ~/.openclaw/extensions/research-plugins

# npx skills
rm -rf .skills/wentorai/research-plugins
```

Do not load the package as a pnpm dependency through `plugins.load.paths`: pnpm's hard links trip the OpenClaw safety check with an "unsafe plugin manifest path" error. Always use `openclaw plugins install`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| polish-skills | 419 | Writing polish: tone, translation, refining, humanizing, grammar and plagiarism checks |
| dataviz-skills | 297 | Data visualization: bokeh, d3, plotly, echarts and publication figures |
| latex-skills | 268 | LaTeX writing: typesetting, bibliography management, templates and TikZ diagrams |
| citation-skills | 263 | Citation management: Zotero, BibTeX, Mendeley and reference-manager workflows |
| econometrics-skills | 248 | Econometrics: causal inference, panel data, IV regression and Stata workflows |
| paper-review-skills | 225 | Peer review: critique frameworks, rebuttal writing and review responses |
| deep-research-skills | 212 | Deep research: systematic reviews, meta-synthesis and scoping reviews |
| statistics-skills | 208 | Statistics: hypothesis testing, power analysis, survival analysis and SEM |
| social-science-skills | 199 | Social science: psychology, sociology, survey research and network analysis |
| ocr-translate-skills | 195 | OCR and translation: handwriting recognition, LaTeX OCR and PDF translation |
| chemistry-skills | 191 | Chemistry: cheminformatics, molecular dynamics and PubChem |
| finance-skills | 190 | Finance: quantitative finance, portfolio optimization and risk modeling |
| diagram-skills | 188 | Diagrams: Mermaid, PlantUML, Kroki and scientific illustration |
| composition-skills | 185 | Writing composition: abstracts, methods sections, discussions and literature reviews |
| ai-ml-skills | 185 | AI/ML: PyTorch, TensorFlow, transformers and LLM evaluation |
| geoscience-skills | 181 | Geoscience: climate modeling, GIS and remote sensing |
| document-skills | 181 | Documents: PDF parsing, Grobid, Zotero add-ons and large-document reading |
| pharma-skills | 180 | Pharma: drug discovery, clinical trial design and pharmacovigilance |

The remaining 78 indexed listings range from 5 to 175 installs.

## Why This Matters for Hermes Agents

Academic research agents usually stall at the same two points: they can talk about a paper but cannot query the databases behind it, and they do not know the field-specific method for each task. This package supplies both: 34 API tools that actually retrieve, parse DOIs, chase citations and find open-access full text, and a large library of structured guides covering the full research lifecycle. The progressive-loading layout matters for agents because it keeps a 433-skill corpus usable without exhausting context: load one category index, then the specific guide. Guides cover real workflows such as PRISMA systematic reviews, fixed-effects regressions with robustness checks, and reviewer rebuttals, which are exactly the tasks where a generic model hallucinates method instead of applying it. Everything runs on free scholarly APIs with no account or API key, and the code is MIT licensed.

## Usage

| You say | What happens |
|---|---|
| Find high-citation papers on causal inference from the last three years | The OpenAlex tool sorts by citations and the Unpaywall tool locates open-access PDFs |
| Run my systematic review workflow | The systematic-review-guide drives a PRISMA flow with multi-database search and dedup |
| Run a fixed-effects regression on this panel data | The econometrics guides produce Stata or Python code with placebo and clustered-error checks |
| Draft a point-by-point reply to these reviewer comments | The rebuttal-writing guide classifies each point as changed, clarified or politely disputed |
| Turn my Zotero library into a cited draft | The citation tools resolve DOIs and the composition guides structure the manuscript |
| Build an NSF proposal with a budget | The grant-writing and budget guides scaffold sections and a budget table |

## Verification

```bash
# after install, confirm the skill files landed
ls .skills/wentorai/research-plugins/
# review one category index before relying on it
curl -sL https://raw.githubusercontent.com/wentorai/research-plugins/main/skills/analysis/dataviz/SKILL.md
```

The raw SKILL.md URL above was probed Nov 19, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| polish-skills | Pass | Pass | Pass |
| dataviz-skills | Pass | Pass | Pass |
| latex-skills | Pass | Pass | Pass |
| citation-skills | Pass | Pass | Pass |
| econometrics-skills | Pass | Pass | Pass |
| paper-review-skills | Pass | Pass | Warn |
| deep-research-skills | Pass | Pass | Warn |
| statistics-skills | Pass | Pass | Pass |
| social-science-skills | Pass | Pass | Warn |
| ocr-translate-skills | Pass | Warn | Pass |
| chemistry-skills | Pass | Pass | Pass |
| finance-skills | Pass | Pass | Pass |
| diagram-skills | Pass | Pass | Pass |
| composition-skills | Pass | Pass | Pass |
| ai-ml-skills | Pass | Pass | Pass |
| geoscience-skills | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 19, 2026: 8,238 combined installs across 96 indexed listings; 320 GitHub stars; MIT licence; last pushed Jun 19, 2026. Counts drift over time.
- The 96-listing count is the skills.sh API cap, so both the listing count and the combined-install total are floors; the repository documents a larger 433-skill corpus plus 34 API tools.
- The top-level category skills carry a `-skills` suffix on the marketplace (polish-skills, dataviz-skills) while the matching tree directories drop it (writing/polish, analysis/dataviz); these listings are the category indexes, one per research domain.
- Only 16 of 96 listings have skills.sh verdicts; the other 80 are unverified on that platform.
- The README is written in Chinese; the English guidance lives in README.en.md, and the API tools assume a Research-Claw or OpenClaw host to register as a plugin.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)
- [Arxiv Setup](/hermes/skills/catalog/arxiv-setup)
- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `openclaw plugins install` for the full plugin (skills plus 34 API tools); use `npx skills add` when you only want the SKILL.md guides.
- Lean on the 34 free API tools first: they cover OpenAlex, CrossRef, PubMed, arXiv and Unpaywall with no API key.
- Read `polish-skills` before finalizing any draft: it covers tone, grammar, plagiarism and the humanization guides.
- Avoid loading the package through pnpm or `plugins.load.paths`; OpenClaw rejects the hard-linked manifest path.
- For systematic or scoping reviews, start at `research/deep-research` rather than a single paper tool so the whole PRISMA flow stays consistent.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
