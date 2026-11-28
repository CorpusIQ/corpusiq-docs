---
title: "K-Dense Scientific Agent Skills - Setup Guide"
description: "k-dense-ai/scientific-agent-skills: 221.6K combined installs. 177 scientific skills and 100+ databases that turn any agent into an AI scientist."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/k-dense-scientific-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "scientific", "research", "drug discovery"]
---

# K-Dense Scientific Agent Skills - Setup Guide

**Source:** [k-dense-ai/scientific-agent-skills](https://www.skills.sh/k-dense-ai/scientific-agent-skills) via skills.sh - 221.6K combined installs across 96 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [k-dense-ai/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 58,714 stars, MIT, branch main, last pushed 2026-11-23; 177 skills live under `skills/<name>/SKILL.md` as a 2.72.0 Agent Skills collection with per-skill references and scripts.

**Category:** Scientific research agent skills: bioinformatics, cheminformatics, clinical research, machine learning, data analysis and scientific communication

**Quality Tier:** 🟡 Yellow - three of the twenty sampled listings (literature-review, paper-lookup, citation-management) carry a Snyk Warn; the other seventeen pass all three auditors, with no Fail cells in the sample.

Scientific Agent Skills is a 177-skill collection from K-Dense that teaches an agent how scientific work actually gets done: which Python package or database to reach for, what conventions and validation checks apply, and where the safety boundary sits. The skills span biology, chemistry, medicine, physics, engineering, Earth science, data analysis and scientific communication, and they follow the open Agent Skills standard, so they load on Cursor, Claude Code, Codex, Google Antigravity and other compatible hosts.

The README counts 177 validated skills plus 100+ scientific databases, but skills.sh indexes 96 of those 177 listings, and this guide does not reconcile that gap. The 96 indexed listings sit in a flat install band between 2,177 and 2,839, which is a shape of this corpus rather than a popularity ranking: the suite installs as one validated set, and a single install pulls the whole collection.

## Installation

The README offers four install paths. The standards-based installer covers the supported hosts:

```text
npx skills add K-Dense-AI/scientific-agent-skills
```

GitHub CLI (v2.90.0+) users can install interactively, pick one skill, or target a host:

```bash
gh skill install K-Dense-AI/scientific-agent-skills
gh skill install K-Dense-AI/scientific-agent-skills scanpy
gh skill install K-Dense-AI/scientific-agent-skills --agent cursor
```

Pin to a release tag or commit SHA for reproducible installs, and update with `gh skill update --all`.

The repo is also a valid Agent Plugins package (plugin.json plus skills/). Cursor users symlink the checkout into the local plugins directory; Codex installs from a checkout with `codex plugins install .`. For hosts that scan `~/.agents/skills/`, clone the repo there directly. Hermes versions with skill taps use:

```bash
hermes skills tap add K-Dense-AI/scientific-agent-skills
```

Every SKILL.md uses YAML frontmatter with a quoted `metadata.version`. Installing the files does not install their Python dependencies: follow each skill's `compatibility` field and use uv for its packages, in a separate environment per workflow.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scientific-writing | 2,839 | Drafts and audits evidence-traceable manuscripts with provenance, reporting-guideline coverage and consistency checks. |
| scientific-visualization | 2,800 | Publication-ready figures in Matplotlib, Seaborn or Plotly with accessibility and export planning. |
| literature-review | 2,748 | Systematic, scoping and narrative reviews across PubMed, arXiv, bioRxiv and Semantic Scholar. |
| scientific-critical-thinking | 2,744 | Evaluates claim and evidence quality: bias, confounders, statistics, GRADE and Cochrane grading. |
| statistical-analysis | 2,658 | Test selection, assumption checks, effect sizes, power analysis and APA-formatted reporting. |
| scientific-brainstorming | 2,629 | Evidence-aware ideation with structured discussion, adversarial review and decision logs. |
| paper-lookup | 2,621 | Searches 18 scholarly APIs for papers, citations, full text and open-access status. |
| citation-management | 2,608 | Searches OpenAlex, PubMed and Google Scholar, validates citations and formats BibTeX. |
| peer-review | 2,552 | Evidence-bounded peer-review drafts with claim-evidence, statistics and ethics critique. |
| matplotlib | 2,538 | Fine-grained Matplotlib plots exported to PNG, PDF or SVG for publication. |
| scikit-learn | 2,528 | Supervised and unsupervised learning, evaluation, tuning and pipelines with scikit-learn. |
| scientific-slides | 2,526 | PowerPoint and Beamer slide decks for talks, seminars and defenses. |
| scientific-schematics | 2,511 | AI-assisted diagram drafts for architectures, pathways and flowcharts. |
| exploratory-data-analysis | 2,496 | Bounded local EDA of supported scientific files with missingness and leakage audits. |
| statsmodels | 2,449 | OLS, GLM, mixed models and ARIMA/SARIMAX with design and uncertainty checks. |
| markitdown | 2,434 | Converts documents and URIs to Markdown with Microsoft MarkItDown. |
| hypothesis-generation | 2,428 | Evidence-bounded hypotheses, rival explanations and preregistration-ready plans. |
| markdown-mermaid-writing | 2,407 | Scientific Markdown and Mermaid diagrams with templates and rendering checks. |
| seaborn | 2,403 | Statistical plots with pandas integration: distributions, relationships, heatmaps. |
| database-lookup | 2,375 | Documented public database APIs (80 databases) with endpoints, pagination and provenance. |
| scholar-evaluation | 2,367 | Qualitative, low-stakes evaluation of scholarly works; never ranks people. |
| polars | 2,358 | Fast Polars DataFrame operations for scientific data processing. |
| latex-posters | 2,340 | LaTeX poster generation from templates for conferences. |
| pptx-posters | 2,338 | Macro-free PPTX posters generated from author-approved local manifests. |
| sympy | 2,334 | Symbolic mathematics with SymPy. |
| bgpt-paper-search | 2,334 | Advanced paper search with 25+ structured fields read from full text. |
| research-grants | 2,325 | Grant writing workflows and research proposals. |
| pytorch-lightning | 2,325 | Deep-learning training with PyTorch Lightning. |
| networkx | 2,317 | Network analysis and visualization with NetworkX. |
| aeon | 2,316 | Time-series forecasting, classification and clustering with aeon. |
| transformers | 2,311 | Hugging Face Transformers models and pipelines. |
| shap | 2,311 | Model interpretability with SHAP. |
| pyzotero | 2,305 | Zotero library access and citation workflows via pyzotero. |
| generate-image | 2,299 | Image generation, editing and compositing via the OpenRouter Image API. |
| infographics | 2,296 | AI-powered infographics across 10 types and 8 styles. |
| matlab | 2,295 | MATLAB and GNU Octave planning and review workflows. |
| dask | 2,293 | Scalable parallel computing with Dask arrays and dataframes. |
| market-research-reports | 2,291 | Evidence-traceable market research with assumption-led sizing and forecast sensitivity. |
| get-available-resources | 2,280 | Detects available compute resources before resource-sensitive workloads. |
| optimize-for-gpu | 2,275 | GPU acceleration with CuPy, Numba CUDA, cuDF, cuML and the RAPIDS stack. |
| pymc | 2,274 | Bayesian modeling and inference with PyMC. |
| venue-templates | 2,271 | Publishing and paper venue templates for submission workflows. |
| research-lookup | 2,265 | Research discovery and lookup workflows. |
| umap-learn | 2,264 | UMAP dimensionality reduction for high-dimensional data. |
| parallel-web | 2,262 | Web search, URL and PDF extraction, deep research and recurring monitoring. |
| scikit-survival | 2,261 | Survival analysis with scikit-survival. |
| biopython | 2,258 | Sequence analysis, BLAST, alignments and phylogenetics with BioPython. |
| open-notebook | 2,256 | Self-hosted NotebookLM-style research notebooks over PDFs, video and web pages. |
| torch-geometric | 2,255 | Graph machine learning with Torch Geometric. |
| timesfm-forecasting | 2,248 | Google TimesFM zero-shot univariate forecasting. |
| geopandas | 2,246 | Geospatial analysis and CRS management with GeoPandas. |
| stable-baselines3 | 2,242 | Reinforcement learning with Stable Baselines3. |
| pymoo | 2,239 | Multi-objective optimization with PyMOO. |
| geomaster | 2,239 | Remote sensing, GIS, satellite imagery and spatial ML with GeoMaster. |
| simpy | 2,236 | Discrete-event simulation with SimPy. |
| consciousness-council | 2,236 | Multi-perspective deliberation and devil's advocate analysis. |
| scikit-bio | 2,234 | Bioinformatics algorithms with scikit-bio. |
| what-if-oracle | 2,232 | Branch possibility exploration, contingency planning and decision stress-testing. |
| hypogenic | 2,224 | HypoGeniC candidate text-pattern generation for datasets; not validated hypotheses. |
| bioservices | 2,224 | Multi-database access via BioServices. |
| anndata | 2,221 | AnnData single-cell data structures and manipulation. |
| clinical-reports | 2,216 | Source-bound clinical report drafts from verified facts, visibly marked for review. |
| rdkit | 2,213 | Cheminformatics with RDKit: molecules, descriptors and structure analysis. |
| clinical-decision-support | 2,211 | Aggregate or synthetic decision-support evaluation and governance artifacts. |
| modal | 2,210 | Cloud compute and scheduled jobs with Modal. |
| astropy | 2,208 | Astronomy data analysis, coordinates and cosmology with Astropy. |
| gget | 2,207 | gget bioinformatics database queries. |
| scanpy | 2,206 | Single-cell RNA-seq analysis with Scanpy. |
| pydicom | 2,203 | DICOM processing with privacy-first local preflight. |
| cellxgene-census | 2,203 | Cellxgene Census single-cell data access. |
| datamol | 2,201 | Molecular manipulation and descriptors with Datamol. |
| deeptools | 2,200 | deepTools sequencing-data normalization and workflows. |
| pufferlib | 2,199 | PufferLib reinforcement-learning environment workflows. |
| deepchem | 2,198 | DeepChem molecular deep learning. |
| vaex | 2,196 | Vaex out-of-core dataframe processing. |
| benchling-integration | 2,196 | Benchling LIMS and ELN integration. |
| arboreto | 2,194 | Gene regulatory network inference with Arboreto. |
| pydeseq2 | 2,193 | Differential expression analysis with PyDESeq2. |
| molecular-dynamics | 2,193 | OpenMM plus MDAnalysis molecular dynamics and trajectory analysis. |
| adaptyv | 2,192 | Automated protein testing and validation via the Adaptyv cloud lab platform. |
| torchdrug | 2,191 | TorchDrug molecular deep learning. |
| pymatgen | 2,191 | Materials analysis with pymatgen and Materials Project queries. |
| fluidsim | 2,190 | FluidSim computational fluid dynamics with validity checks. |
| esm | 2,190 | ESM protein language models. |
| zarr-python | 2,189 | Zarr compressed array storage. |
| scvi-tools | 2,188 | scvi-tools probabilistic single-cell models. |
| pyhealth | 2,187 | PyHealth healthcare AI and EHR research. |
| imaging-data-commons | 2,187 | NCI radiology and pathology datasets via idc-index. |
| neurokit2 | 2,186 | NeuroKit2 physiological signal analysis. |
| medchem | 2,185 | MedChem drug-likeness filters. |
| molfeat | 2,182 | Molfeat molecular featurization. |
| dhdna-profiler | 2,182 | DHDNA cognitive profiling and thinking patterns from text. |
| pysam | 2,178 | pysam alignment and variant file processing. |
| pathml | 2,177 | PathML research-only whole-slide image analysis. |
| diffdock | 2,177 | DiffDock molecular docking. |
| depmap | 2,177 | DepMap cancer dependency scores and drug sensitivity. |

All 96 indexed listings appear in the table above. The installs form a flat band from 2,177 to 2,839 rather than a popularity curve, which is a shape of this corpus: the suite installs as one validated set, so a single install pulls the whole collection.

## Why This Matters for Hermes Agents

Scientific Agent Skills is the largest single science-domain library on the index, and its value is scope: an agent that can route procedural knowledge across packages, databases and workflows. The skills encode the boundaries generic agents get wrong: clinical reports are visibly marked drafts built from verified source facts and never a diagnosis; DICOM processing is privacy-first; ISO and analytical-method skills explicitly stop short of certification decisions. That discipline, written into the SKILL.md files rather than left to the model, is the pattern a Hermes-style builder should copy.

The multi-skill workflow prompts are the second thing worth copying. The README's Quick Examples chain five or six skills into one research task, each scoped to a narrow step (query ChEMBL, filter with RDKit, dock with DiffDock, search resistance mechanisms, visualize). That is a worked model of routing a general agent into specialized skills without letting any one skill overreach.

The database-lookup skill is the backbone: it documents 80 databases with endpoints, pagination and provenance, and the dedicated data-access skills (DepMap, Imaging Data Commons, PrimeKG) hang off it. For a builder, that separation of a unified retrieval contract from domain-specific accessors is the right layering.

Finally, the security posture is explicit rather than implied: the README says do not install everything at once, read each SKILL.md, and run the Cisco AI Skill Scanner locally. Combined with the flat-band install shape, the practical guidance is to install the set once and then review the skills your agent actually touches.

## Usage

| You say | What happens |
|---|---|
| "Prioritize EGFR inhibitor candidates for preclinical research" | database-lookup queries ChEMBL, rdkit filters compounds, diffdock docks them, and scientific-visualization renders the report. |
| "Analyze this 10X single-cell dataset" | scanpy loads and QC-checks the data, cellxgene-census integrates public data, pydeseq2 runs differential expression, and arboreto infers regulatory networks. |
| "Draft a systematic review on this topic" | literature-review searches PubMed, arXiv and bioRxiv, and citation-management validates and formats the references. |
| "Help me write this manuscript" | scientific-writing drafts evidence-traced sections, and peer-review produces a claim-by-claim critique. |
| "Make a publication figure for this result" | scientific-visualization builds the figure with Matplotlib or Seaborn and audits color, uncertainty and export settings. |
| "Turn this VCF into an evidence-traceable summary" | pysam parses the file, database-lookup pulls ClinVar and COSMIC evidence, and scientific-writing writes the summary. |
| "Forecast this time series" | timesfm-forecasting runs Google TimesFM zero-shot forecasting, or statsmodels fits ARIMA with design checks. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/scientific-writing/SKILL.md
```

After a clone, confirm the layout and count:

```bash
git clone --depth 1 https://github.com/K-Dense-AI/scientific-agent-skills.git /tmp/sci-skills
ls /tmp/sci-skills/skills/ | wc -l
head -3 /tmp/sci-skills/skills/scientific-writing/SKILL.md
```

The count prints the in-tree skill directories (177 per the README; the index tracks 96), and head shows the scientific-writing frontmatter. Skill names in the table above are directory names under `skills/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scientific-writing | Pass | Pass | Pass |
| scientific-visualization | Pass | Pass | Pass |
| literature-review | Pass | Pass | Warn |
| scientific-critical-thinking | Pass | Pass | Pass |
| statistical-analysis | Pass | Pass | Pass |
| scientific-brainstorming | Pass | Pass | Pass |
| paper-lookup | Pass | Pass | Warn |
| citation-management | Pass | Pass | Warn |
| peer-review | Pass | Pass | Pass |
| matplotlib | Pass | Pass | Pass |
| scikit-learn | Pass | Pass | Pass |
| scientific-slides | Pass | Pass | Pass |
| scientific-schematics | Pass | Pass | Pass |
| exploratory-data-analysis | Pass | Pass | Pass |
| statsmodels | Pass | Pass | Pass |
| markitdown | Pass | Pass | Pass |
| hypothesis-generation | Pass | Pass | Pass |
| markdown-mermaid-writing | Pass | Pass | Pass |
| seaborn | Pass | Pass | Pass |
| database-lookup | Pass | Pass | Pass |

This guide is Yellow because three of the twenty sampled listings (literature-review, paper-lookup, citation-management) carry a Snyk Warn, while Socket and the Gen Agent Trust Hub pass every sampled listing and no Fail appears in the sample. The repository runs weekly LLM-based security scans via the Cisco AI Skill Scanner and publishes results to docs/security-report.md. Skills can execute code and make network requests, so follow the README's own guidance: install only what you need and read each SKILL.md first.

## Limitations

- Snapshot data, verified 2026-11-27: 221,587 combined installs across 96 indexed listings; 58,714 GitHub stars; MIT; last pushed 2026-11-23. Counts drift over time.
- The README counts 177 validated skills plus 100+ scientific databases, but skills.sh indexes only 96 listings; this guide lists the 96 and does not reconcile the gap.
- Installing the skill files does not install their Python dependencies; each skill declares its own compatibility field, and some require different Python versions or incompatible package pins, so use separate environments per workflow.
- Several skills carry clinical or regulatory scope limits: clinical-reports and clinical-decision-support produce drafts or aggregate artifacts, never diagnoses or treatment decisions; ISO and analytical-method skills stop short of certification or method-release decisions.
- Since 2.72.0 the repo no longer bundles the docx, pdf, pptx and xlsx document skills vendored from anthropics/skills; the README points there for those four.
- Three of the twenty sampled listings carry a Snyk Warn; the failure reasons are not published beside the verdicts, so check the security pages on skills.sh before installing into a production profile.

## Related

- [Scientific Agent Skills - Research Workflow Setup](/hermes/skills/catalog/scientific-agent-skills-setup) - note: that is tondevrel/scientific-agent-skills, a different publisher from the k-dense-ai collection covered here.
- [Scientific Skills - Literature Search Suite Setup](/hermes/skills/catalog/yorkeccak-scientific-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole set once rather than cherry-picking: the README installs the collection as one validated unit, and the flat install band reflects that all-at-once usage pattern.
- Pair that with the README's own caution and review only the SKILL.md files your agent actually opens, instead of auditing all 177 up front.
- Load database-lookup early: it documents 80 databases and is the shared retrieval layer most workflow prompts depend on.
- Keep the clinical and regulatory boundaries verbatim in your own prompts: these skills produce drafts and research artifacts, never diagnoses or certification decisions.
- Pin to a release tag with `gh skill install K-Dense-AI/scientific-agent-skills --pin v2.71.0` for reproducible lab installs, and re-read a skill's compatibility field before upgrading Python or packages.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
