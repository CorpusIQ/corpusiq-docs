---
title: Research Paper Writing Pipeline — Hermes Skill Setup Guide
description: Install and configure research-paper-writing, the official Hermes Agent skill for end-to-end ML/AI research paper production targeting NeurIPS, ICML, ICLR, ACL, AAAI, and COLM — 396 installs.
---

# Research Paper Writing Pipeline — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/research-paper-writing) (396 installs)
**Originally from:** [master-cai/research-paper-writing-skills](https://skills.sh/master-cai/research-paper-writing-skills/research-paper-writing)
**Category:** Research / Academic
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Python 3.10+, LaTeX (optional)

End-to-end pipeline for producing publication-ready ML/AI research papers targeting top venues: **NeurIPS, ICML, ICLR, ACL, AAAI, and COLM**. Covers the full research lifecycle: experiment design, execution, monitoring, analysis, paper writing, review, revision, and submission.

⚠️ This is **not a linear pipeline** — it is an iterative loop. Results trigger new experiments. Reviews trigger new analysis. The agent must handle these feedback loops.

---

## What It Does

| Phase | Capability |
|-------|-----------|
| **Experiment design** | Hypothesis formulation, ablation planning, baseline selection |
| **Execution** | Run experiments, track metrics, log results |
| **Monitoring** | Track training curves, detect anomalies, early stopping |
| **Analysis** | Statistical tests, visualization, significance reporting |
| **Paper writing** | Structured LaTeX/PDF output with venue-specific templates |
| **Review response** | Draft rebuttals, revise based on reviewer feedback |
| **Submission** | Format check, supplementary material, camera-ready prep |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill research-paper-writing
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/research/research-paper-writing ~/.hermes/skills/
```

---

## Supported Venues

| Venue | Field | Template |
|-------|-------|----------|
| NeurIPS | ML/AI | NeurIPS LaTeX style |
| ICML | Machine Learning | ICML LaTeX style |
| ICLR | Learning Representations | ICLR LaTeX style |
| ACL | Computational Linguistics | ACL LaTeX style |
| AAAI | Artificial Intelligence | AAAI LaTeX style |
| COLM | Language Modeling | COLM LaTeX style |

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.20.0+ |
| Python | 3.10+ with numpy, scipy, matplotlib |
| LaTeX | texlive-full (recommended for PDF output) |
| GPU access | Optional — for experiment execution |

---

## Verification

After install, test with:

```
Hermes, help me design an ablation study for a transformer-based model comparing attention mechanisms.
```

The agent should walk through hypothesis formulation, experimental design, and suggest a structured approach following the research pipeline.

---

## Pitfalls

- **Iterative, not linear:** The pipeline loops. Don't expect a one-pass paper — expect rounds of experiment → analyze → revise.
- **LaTeX dependency:** PDF output requires a working LaTeX installation (`texlive` or `miktex`).
- **Venue-specific formatting:** Each venue has strict formatting requirements. Verify the template version before submission.
- **Snyk warning:** The skill carries a SnykWarn security audit. Review before use in sensitive research environments.

---

**Installed via:** `npx skills add nousresearch/hermes-agent --skill research-paper-writing`
