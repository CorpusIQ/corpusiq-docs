---
title: "SciAgent Skills - Bioinformatics & Life Science Suite Setup"
description: "jaechang-hits/sciagent-skills: 96 bioinformatics and life science skills for RNA-seq, single-cell, drug discovery and more - 7.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jaechang-hits-sciagent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "bioinformatics", "life science", "scientific computing"]
---

# SciAgent Skills - Bioinformatics & Life Science Suite Setup

**Source:** [jaechang-hits/sciagent-skills](https://www.skills.sh/jaechang-hits/sciagent-skills) via skills.sh - 7.5K combined installs across 96 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [jaechang-hits/sciagent-skills](https://github.com/jaechang-hits/sciagent-skills) - 395 stars, NOASSERTION license (README declares CC-BY-4.0), main branch, last pushed Nov 16, 2026; skills live under `skills/<category>/<name>/SKILL.md` across eleven domain folders, with a Claude plugin manifest, a `registry.yaml` index and `references/` deep-dives on the larger skills.
**Category:** Bioinformatics and Life Science Research
**Quality Tier:** 🟡 Yellow - every sampled skill passes Gen Agent Trust Hub and Socket, with Snyk Warn cells on 3 of the 20 sampled skills.

SciAgent-Skills is a large open-source skill library that turns a general coding agent into a life sciences specialist. The publisher ships skills as plain markdown files organized by domain: genomics and bioinformatics, structural biology and drug discovery, scientific computing, cell biology, biostatistics, scientific writing, systems biology, proteomics, lab automation, data visualization and molecular biology. The README anchors the suite on a benchmark claim: equipping Claude Code with the skills lifted BixBench-Verified-50 accuracy from 65.3% to 92.0% with no fine-tuning.

The install index lists 96 skills against a README that advertises 199, so the counts here reflect the counted subset rather than the full directory. Each skill is a self-contained SKILL.md with runnable examples, key parameters and troubleshooting tables, and the agent reads only the description field during planning, loading full content on demand.

## Installation

The skills are plain markdown files, not an npm package, so there is no runtime install. Clone the repository and point your agent at it:

```bash
git clone https://github.com/jaechang-hits/SciAgent-Skills.git
cd SciAgent-Skills
```

For Claude Code, load it as a plugin (the recommended route):

```bash
claude --plugin-dir /path/to/SciAgent-Skills
```

Then run `/plugin` and confirm `sciagent-skills` appears in the Installed tab. Skills become available as `/sciagent-skills:<skill-name>`. For a persistent install across sessions:

```text
/plugin marketplace add jaechang-hits/SciAgent-Skills
/plugin install sciagent-skills
```

For project-level use with any markdown-reading agent, clone into the project and wire discovery via `registry.yaml`:

```bash
cd your-project
git clone https://github.com/jaechang-hits/SciAgent-Skills.git .sciagent-skills
cp .sciagent-skills/integration-templates/AGENTS.md ./AGENTS.md
mkdir -p .cursor/rules
cp .sciagent-skills/integration-templates/cursor-rules.md .cursor/rules/sciagent-skills.md
```

Python dependencies for the validation scripts are managed with Pixi:

```bash
pixi install
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| matplotlib-scientific-plotting | 131 | publication-quality scientific figures with fine control of line, scatter, bar, heatmap and multi-panel layouts |
| scientific-schematics | 119 | scientific schematics, pathway diagrams, mechanism figures and journal graphical abstracts |
| pydicom-medical-imaging | 103 | read and write DICOM, edit tags, apply windowing and anonymize PHI for CT, MRI, X-ray and ultrasound |
| astropy-astronomy | 95 | astronomy workflows: units, coordinate transforms, FITS I/O, tables, cosmology and time |
| sympy-symbolic-math | 94 | exact symbolic math: algebra, calculus, equation solving, matrices and code generation |
| autodock-vina-docking | 92 | molecular docking with AutoDock Vina: receptor and ligand prep, docking, pose analysis and virtual screening |
| statistical-analysis | 91 | guided statistical analysis: test selection, assumption checks, effect sizes, power and APA reporting |

The remaining 89 indexed listings range from 70 to 87 installs.

## Why This Matters for Hermes Agents

Scientific analysis is where an agent's plausible-looking output is also quietly wrong: a mis-picked statistical test, a mislabeled DICOM tag or a badly prepared figure can invalidate a result without any obvious error. This suite encodes the domain judgment a general agent lacks. The statistical-analysis skill walks test choice, assumption checks, effect sizes and power before reporting, so the agent reaches for the right test instead of the first one that runs. Database-connector skills such as OpenAlex, PubMed, UniProt, ChEMBL and PDB give the agent structured, citable access to primary sources rather than a web search of whatever surfaces. The figure-guide skills carry each journal's own resolution, format and image-integrity rules, which is the difference between a chart and a submission-ready figure. Because skills are plain markdown read on demand, an agent can hold dozens of them available without loading all of them into context at once.

## Usage

| You say | What happens |
|---|---|
| Run differential expression analysis on this RNA-seq count matrix | Loads the DESeq2 and featurecounts skills and produces the analysis with a volcano plot |
| Which statistical test should I use for this experiment | Checks assumptions, computes effect size and power, and reports in APA format |
| Fetch the AlphaFold structure for UniProt P04637 | Queries the AlphaFold database and assesses confidence regions |
| Search ChEMBL for EGFR inhibitors under 100 nM | Queries the ChEMBL bioactivity database and returns matching compounds with filters |
| Dock these candidates against EGFR and rank them | Runs AutoDock Vina docking and reports binding energies per pose |
| Prepare this figure for Nature submission | Applies the journal's resolution, format and image-integrity rules |
| Visualize cell-cell communication in this scRNA-seq data | Runs the CellChat workflow to infer ligand-receptor signaling and produce chord and bubble plots |

## Verification

Confirm the skills landed in your agent's skill directory:

```bash
ls .sciagent-skills/skills 2>/dev/null || ls ~/.claude/skills
```

Review the statistical-analysis skill's instructions before trusting it with a publication result:

```bash
curl -sL https://raw.githubusercontent.com/jaechang-hits/sciagent-skills/main/skills/biostatistics/statistical-analysis/SKILL.md | head -40
```

The `registry.yaml` at the repository root indexes every skill by category and name, so grepping it is the fastest way to confirm which skills your agent can see.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| matplotlib-scientific-plotting | Pass | Pass | Pass |
| scientific-schematics | Pass | Pass | Pass |
| pydicom-medical-imaging | Pass | Pass | Pass |
| astropy-astronomy | Pass | Pass | Pass |
| sympy-symbolic-math | Pass | Pass | Pass |
| autodock-vina-docking | Pass | Pass | Pass |
| statistical-analysis | Pass | Pass | Pass |
| snakemake-workflow-engine | Pass | Pass | Pass |
| scientific-visualization | Pass | Pass | Pass |
| scientific-manuscript-writing | Pass | Pass | Pass |
| nature-figure-guide | Pass | Pass | Pass |
| scientific-slides | Pass | Pass | Pass |
| biopython-molecular-biology | Pass | Pass | Warn |
| rdkit-cheminformatics | Pass | Pass | Pass |
| cellchat-cell-communication | Pass | Pass | Pass |
| biopython-sequence-analysis | Pass | Pass | Warn |
| scikit-learn-machine-learning | Pass | Pass | Pass |
| scientific-brainstorming | Pass | Pass | Pass |
| openalex-database | Pass | Pass | Warn |
| nejm-figure-guide | Pass | Pass | Pass |

The sampled verdicts are clean apart from three Snyk Warn cells, all on connector and toolkit skills that reach live databases or molecular tooling.

## Limitations

- Snapshot data, verified Nov 21, 2026: 7,451 combined installs across 96 indexed listings; 395 GitHub stars; NOASSERTION license; last pushed Nov 16, 2026. Counts drift over time.
- The README advertises 199 skills while the skills.sh index carries 96 indexed listings, so the install counts cover a counted subset of the directory; the index lists leaf skill names while the repository nests them under eleven category folders.
- GitHub reports the license as NOASSERTION while the README and badge declare CC-BY-4.0 for original content, with individual skills noting the licenses of their underlying tools.
- Each skill's runnable examples depend on scientific Python packages the skill names in its own prerequisites, so the agent needs the relevant environment (the Pixi lockfile manages this for the repository's own tooling).
- The 92.0% BixBench figure is the publisher's own evaluation, not an independent audit, so treat it as a claim to verify on your own workloads.
- Many skills reach external databases (OpenAlex, PubMed, UniProt, ChEMBL, PDB, FDA), so review each connector skill before letting an agent push queries against live services.

## Related

- [EvoSkills - Scientific Research Skill Packs Setup](/hermes/skills/catalog/evoskills-setup)
- [Academic Research Skills - Citations, Reviews and Writing](/hermes/skills/catalog/kalarislabs-research-agent-skills-setup)
- [RigorPilot Skills - AI Research & Paper Reproduction Setup](/hermes/skills/catalog/rigorpilot-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for a skill by name (`/sciagent-skills:rdkit-cheminformatics`) when you know the exact tool; otherwise describe the task and let the planning pass pick from the description fields.
- Start read-only with a database-connector skill such as OpenAlex or PubMed to confirm the environment works before running a write-heavy pipeline like docking or a full RNA-seq run.
- For publication work, run statistical-analysis before generating the figure, so the test choice and the plot come from the same assumptions.
- Keep the Pixi environment as the single source of Python packages rather than pip-installing ad hoc, so a skill's prerequisites stay reproducible.
- Pin the repository at a known commit for reproducibility work; the suite updates frequently and a skill's examples can shift under a long-running project.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
