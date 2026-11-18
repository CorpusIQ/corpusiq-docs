---
title: "Materials Simulation Skills - Numerical Methods and HPC"
description: "heshamfs/materials-simulation-skills: 4.8K combined installs across 24 listings; skills for numerical methods, solvers, meshing, convergence and HPC."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/materials-simulation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "materials science", "numerical methods", "HPC", "simulation"]
---

# Materials Simulation Skills - Setup Guide

**Source:** [heshamfs/materials-simulation-skills](https://www.skills.sh/heshamfs/materials-simulation-skills) via skills.sh - 4.8K combined installs across 24 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 94 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-15, 24 skills in eight categories under `skills/`, plus a `mss` command-line tool and a Python library
**Category:** Computational materials science / scientific computing
**Quality Tier:** 🟡 Yellow - 58 Pass and 2 Warn across the 20 sampled listings; no Fail.

Materials Simulation Skills gives an agent instructions plus tested Python scripts for the numerical and workflow decisions that surround a computational materials simulation, so it checks a CFL number or picks a preconditioner instead of guessing. The 24 skills span eight categories: core numerical methods, simulation workflow, materials ontologies, HPC deployment, verification and validation, FAIR data management, robustness, and a meta evaluator.

The core numerical set covers stability, time-stepping, meshing, convergence, integration, differentiation, and linear and nonlinear solvers. The workflow set handles validation, design of experiments, orchestration, post-processing, profiling, workflow mapping, and molecular dynamics analysis. Each skill ships a tested script the agent runs with your numbers, and the repository's eval gate asserts exact script output, so the documented numbers cannot drift from the code. These skills plan and check a simulation; they do not run a solver, and a passing check is not evidence about a physical simulation.

## Installation

The README's primary install hands the suite to a skills-aware agent:

```text
npx skills add HeshamFS/materials-simulation-skills
```

Alternative installs are documented in `docs/INSTALL.md`: pin to a release, add it as a Claude Code plugin, or install the curated `mss` CLI:

```bash
gh skill install HeshamFS/materials-simulation-skills --pin v1.0.0
pip install materials-simulation-skills
mss install --agent claude --bundle verification-and-validation
```

Then ask the agent a simulation question; it picks the matching skill and runs its script.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| numerical-stability | 240 | Check CFL and von Neumann stability, detect stiffness, and pick explicit or implicit stepping. |
| nonlinear-solvers | 233 | Choose Newton, quasi-Newton, or Anderson methods and set line-search or trust-region globalization. |
| simulation-orchestrator | 232 | Generate parameter sweeps, track batch campaigns, and aggregate results across runs. |
| mesh-generation | 224 | Estimate grid resolution from physics scales and check aspect ratio and skewness. |
| simulation-validator | 220 | Pre-flight config checks, runtime log monitoring, and post-flight validation of results. |
| convergence-study | 220 | Compute observed convergence orders and Grid Convergence Index per ASME V&V 20. |
| numerical-integration | 216 | Pick Runge-Kutta, BDF, or Rosenbrock integrators, set tolerances, and plan IMEX splitting. |
| parameter-optimization | 214 | Run DOE and sensitivity analysis, pick an optimizer, and fit surrogates for expensive runs. |
| post-processing | 213 | Extract fields, time series, and profiles and compare against analytics or data. |
| time-stepping | 211 | Plan time-step policies, ramp transients, and schedule output and checkpoint cadence. |
| slurm-job-script-generator | 211 | Generate sbatch scripts and sanity-check MPI, memory, GPU, and walltime requests. |
| linear-solvers | 210 | Choose direct or Krylov methods, analyze conditioning, and pick preconditioners. |
| performance-profiling | 205 | Parse timing logs, evaluate strong and weak scaling, and profile memory. |
| differentiation-schemes | 204 | Generate finite-difference stencils and pick central, upwind, compact, or spectral schemes. |
| ontology-mapper | 200 | Map materials terms and crystal structures to CMSO/ASMO classes and FAIR metadata. |

The remaining 9 indexed listings range from 108 to 198 installs.

## Why This Matters for Hermes Agents

Most simulation failures surface as vague symptoms: a solver stalls, a run blows up, a step is rejected. These skills give a Hermes agent a structured way to act on those symptoms instead of asserting a guess. Each skill is a folder of instructions plus a small, tested script the agent runs with the numbers from the problem, then explains the output.

For an engineer the value is reproducibility: every script also runs by hand through the `mss` CLI, so any answer the agent gives can be checked at a terminal. The convergence and verification skills route the agent to formal standards such as ASME V&V 20 and the Grid Convergence Index rather than ad hoc error estimates. The HPC skills make cluster requests concrete: a SLURM script generator that catches conflicting directives, and a runtime doctor for launch failures.

The scope caveat is real. These skills are decision support around a solver, not the solver itself. If the underlying toolchain is not installed and configured, the agent can plan and check but cannot run the simulation.

## Usage

| You say | What happens |
|---|---|
| "Is dt=0.001 stable for advection with v=2.0 m/s and dx=0.01?" | The agent runs the numerical-stability CFL check and reports the CFL number with a recommended maximum step. |
| "My GMRES solve stalls. Which preconditioner should I try?" | The agent runs linear-solvers diagnostics and recommends a preconditioner for the matrix type. |
| "Use convergence-study to check if my mesh is in the asymptotic range: h = 0.4, 0.2, 0.1 gave stress = 98.5, 99.6, 99.9 MPa." | The agent computes the observed convergence order and estimates the error on the finest mesh. |
| "My simulation crashed." | The agent runs simulation-failure-triage to classify the failure signature and propose a one-change-at-a-time retry ladder with stop conditions. |
| "I need to try many parameter combinations." | The agent uses simulation-orchestrator to generate the sweep, track jobs, and aggregate results. |
| "I need to run this on the cluster." | The agent generates a SLURM sbatch script and sanity-checks the resource request. |

## Verification

Probe two skills on the `main` branch before installing, then run the CLI check. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/HeshamFS/materials-simulation-skills/main/skills/core-numerical/numerical-stability/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/HeshamFS/materials-simulation-skills/main/skills/core-numerical/convergence-study/SKILL.md
```

```bash
pip install materials-simulation-skills
mss list
mss bundles
```

Skills live under `skills/<category>/<name>/SKILL.md`, with per-skill `references/`, `scripts/`, and `evals/` directories.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| numerical-stability | Pass | Pass | Pass |
| nonlinear-solvers | Pass | Pass | Pass |
| simulation-orchestrator | Pass | Pass | Pass |
| mesh-generation | Pass | Pass | Pass |
| simulation-validator | Pass | Pass | Pass |
| convergence-study | Pass | Pass | Pass |
| numerical-integration | Pass | Pass | Pass |
| parameter-optimization | Pass | Pass | Pass |
| post-processing | Pass | Pass | Pass |
| time-stepping | Pass | Pass | Pass |
| slurm-job-script-generator | Pass | Pass | Pass |
| linear-solvers | Pass | Pass | Pass |
| performance-profiling | Pass | Pass | Pass |
| differentiation-schemes | Pass | Pass | Pass |
| ontology-mapper | Pass | Pass | Pass |
| ontology-validator | Pass | Pass | Pass |
| ontology-explorer | Pass | Pass | Warn |
| simulation-failure-triage | Warn | Pass | Pass |
| benchmark-and-mms-planner | Pass | Pass | Pass |
| md-analysis-planner | Pass | Pass | Pass |

The sample covers 20 of the 24 indexed listings; the four unsampled listings carry no verdicts in this snapshot.

## Limitations

- Snapshot data, verified 2026-11-17: 4,765 combined installs across 24 indexed listings; 94 GitHub stars; Apache-2.0; last pushed 2026-11-15. Counts drift over time.
- The 15 tabled skills span 200 to 240 installs, a 40-install spread, so the counts are flat rather than a ranked popularity signal.
- These skills are decision and check tooling that wraps an existing solver. They do not install or run LAMMPS, VASP, QE, or MOOSE, and the repository's validation scope states that a passing check is not evidence about a physical simulation.
- skills.sh security verdicts cover 20 of the 24 listings; the remaining four have no published verdicts in this snapshot.
- The repository has not yet published a live-agent comparison showing better scientific answers with the skills than without; that measurement is tracked as open work.

## Related

- [Math Via Code Setup](/hermes/skills/catalog/math-via-code-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)
- [RigorPilot Skills - AI Research & Paper Reproduction Setup](/hermes/skills/catalog/rigorpilot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the `mss` CLI even if you use one skill; `mss run <skill> <script>` reproduces any agent answer by hand.
- Give the agent the physics numbers (velocity, dx, dt), not a yes-or-no question, so a skill computes the CFL number instead of guessing stability.
- Name a skill explicitly, as in "use convergence-study", to bypass the agent's own skill selection when you want a specific check.
- Pair slurm-job-script-generator with performance-profiling so the resource request matches a measured scaling profile.
- Keep the three-stage habit: pre-flight checks, runtime monitoring, and post-flight validation before trusting a result.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
