---
title: "Scientific Agent Skills - Research Workflow Setup"
description: "tondevrel/scientific-agent-skills - 5.8K combined installs: scientific Python skills for numerical computing, machine learning, and research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/scientific-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "scientific python", "machine learning", "data analysis"]
---

# Scientific Agent Skills - Setup Guide

**Source:** [tondevrel/scientific-agent-skills](https://www.skills.sh/tondevrel/scientific-agent-skills) via skills.sh - 5.8K combined installs across 62 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [tondevrel/scientific-agent-skills](https://github.com/tondevrel/scientific-agent-skills) - 25 stars, MIT license, last pushed Feb 1, 2026, main branch; skill folders under skills/<name>/SKILL.md, several listed with an uppercase SKILLS.MD filename or a space-and-ampersand name.
**Category:** Scientific Computing (Python Research Workflows)
**Quality Tier:** 🟢 Green - all 15 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk checks.

tondevrel/scientific-agent-skills publishes contextual knowledge modules that auto-load when an agent detects a relevant scientific topic, spanning the scientific Python ecosystem: numerical computing, data analysis and visualization, machine learning, geospatial work, optimization, quantum computing, bioinformatics, and specialized domains from neuroimaging to chemistry. Each skill documents a library or workflow with best practices, common patterns, and pitfalls, so an agent offers expert guidance instead of generic coding help.

The README tallies the collection at 72 skills, while the current tree holds 71 skill directories and the skills.sh index lists 62 listings. The nine directories that use an uppercase SKILLS.MD filename or a name with spaces and ampersands (for example "gmsh & meshio", "pymc & numpyro", "sktime & tsfresh", and "spacy & nltk") have no hyphenated listing in the index. The repository was last pushed Feb 1, 2026, so treat it as a stale but useful reference.

## Installation

The README documents a manual install: clone and copy the skills directory into your agent's skills folder, or symlink it for easy updates.

```bash
git clone https://github.com/tondevrel/scientific-agent-skills.git
cp -r scientific-agent-skills/skills/* ~/.cursor/skills/
```

For Claude Code, copy into ~/.claude/skills/ instead; other targets include ~/.config/opencode/skill/, ~/.codex/skills/, and ~/.pi/agent/skills/. A symlink keeps updates easy:

```bash
ln -s $(pwd)/scientific-agent-skills/skills ~/.cursor/skills/scientific-agent-skills
```

## What It Provides

skills.sh publishes per-skill install counts for 62 indexed listings. The 11 most-installed skills are listed below; the remaining 51 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| xgboost-lightgbm | 504 | gradient boosting (XGBoost, LightGBM) for tabular data, classification, and regression |
| matplotlib | 376 | 2D plotting and publication-quality figures: heatmaps, contours, vector fields, LaTeX |
| opencv | 336 | computer vision: object detection, edge detection, tracking, camera calibration |
| pyomo | 262 | optimization modeling: LP, MILP, and NLP with Gurobi, CPLEX, IPOPT, and SCIP |
| ortools | 225 | Google optimization: CP-SAT, vehicle routing, scheduling, and constraint programming |
| plotly | 213 | interactive charts, 3D plots, and Dash dashboards |
| seaborn | 167 | statistical visualization: distributions, relationships, and categorical comparisons |
| numpy | 126 | array operations, linear algebra, FFT, and high-performance numerical computing |
| scikit-learn | 123 | classification, regression, clustering, model selection, and preprocessing |
| scipy | 122 | integration, optimization, interpolation, linear algebra, signal processing, and ODEs |
| xarray | 113 | N-dimensional labeled arrays for NetCDF, GRIB, Zarr, and climate data |

The remaining 51 indexed listings range from 44 to 91 installs.

## Why This Matters for Hermes Agents

Scientific Python is dense with half-remembered APIs and silent performance traps: a naive loop where a vectorized NumPy call would do, a missing optimizer.zero_grad() in a PyTorch training loop, or a matplotlib figure that looks fine but fails publication typography. This suite packages that domain knowledge as auto-loading skills, so an agent working on numerical computing, machine learning, or visualization pulls the correct patterns instead of improvising. For a builder running Hermes agents on research or data work, these skills turn "optimize this NumPy operation" into concrete vectorization and broadcasting guidance and "structure a proper training loop" into device management and gradient handling. The coverage is broad, at 62 indexed listings across the ecosystem, and every sampled skill passes all three skills.sh checks. The trade-off is freshness: the repository has not been pushed since Feb 1, 2026, so it lags newer library releases and should be treated as reference material rather than current API documentation.

## Usage

| You say | What happens |
|---|---|
| Optimize this NumPy loop | Uses numpy for vectorization and broadcasting patterns |
| Plot this dataset for a paper | Uses matplotlib and seaborn for publication-quality figures |
| Train a gradient boosting model on this CSV | Uses xgboost-lightgbm for tabular classification and regression |
| Schedule a vehicle routing problem | Uses ortools for CP-SAT and routing constraints |
| Build an interactive dashboard | Uses plotly for interactive charts and Dash |
| Fit a mixed-integer optimization model | Uses pyomo with Gurobi, CPLEX, or open-source solvers |
| Read a NetCDF climate file | Uses xarray for labeled N-dimensional arrays |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/tondevrel/scientific-agent-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/tondevrel/scientific-agent-skills/main/skills/numpy/SKILL.md | head -40
```

Both URLs return 200. After installing, review skills/<name>/SKILL.md for any skill you rely on; note the repository has not been pushed since Feb 1, 2026.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| xgboost-lightgbm | Pass | Pass | Pass |
| matplotlib | Pass | Pass | Pass |
| opencv | Pass | Pass | Pass |
| pyomo | Pass | Pass | Pass |
| ortools | Pass | Pass | Pass |
| plotly | Pass | Pass | Pass |
| seaborn | Pass | Pass | Pass |
| numpy | Pass | Pass | Pass |
| scikit-learn | Pass | Pass | Pass |
| scipy | Pass | Pass | Pass |
| xarray | Pass | Pass | Pass |
| matplotlib-pro | Pass | Pass | Pass |
| numba | Pass | Pass | Pass |
| scikit-image | Pass | Pass | Pass |
| statsmodels | Pass | Pass | Pass |

All 15 sampled skills pass all three checks; 15 of 62 listings were sampled.

## Limitations

- Snapshot data, verified Nov 25, 2026: 5,760 combined installs across 62 indexed listings; 25 GitHub stars; MIT license; last pushed Feb 1, 2026. Counts drift over time.
- The repository has not been pushed since Feb 1, 2026, so the skills lag newer releases of NumPy, PyTorch, scikit-learn, and the rest of the ecosystem.
- The README tallies 72 skills, the current tree holds 71 skill directories, and the index lists 62; nine tree directories with uppercase SKILLS.MD filenames or space-and-ampersand names have no hyphenated listing.
- Only 15 of 62 listings were security-sampled.
- The README install commands reference your-username/scientific-agent-skills as a placeholder repository path.

## Related

[Scientific Skills - Literature Search Suite Setup](/hermes/skills/catalog/yorkeccak-scientific-skills-setup) | [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup) | [Qinyan Academic Skills - Research Library](/hermes/skills/catalog/qinyan-academic-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by symlinking skills into your agent's skills directory so future updates require only a git pull.
- Let skills auto-load from your problem description rather than invoking them manually; the semantic matching picks the right library.
- For missing data, performance, architecture, and debugging questions, the skills map to best practices, common patterns, and pitfalls for each library.
- Verify a skill loaded by watching for domain-specific guidance and warnings about common pitfalls in the agent's reply.
- Because the repo is stale, cross-check any API detail against the current library documentation before shipping.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
