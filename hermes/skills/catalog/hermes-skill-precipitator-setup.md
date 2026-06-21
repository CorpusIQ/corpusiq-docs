---
title: Hermes Skill Precipitator Setup Guide
description: Install and run the automatic workflow-pattern discovery engine — watches Hermes Agent sessions and precipitates reusable skills from repeated patterns
---

# Skill Precipitator — Setup Guide

**Repo:** [luxuguang-leo/hermes-skill-precipitator](https://github.com/luxuguang-leo/hermes-skill-precipitator)
**Created:** June 20, 2026 | **Stars:** 1 | **License:** MIT (assumed)

A self-improving capability for Hermes Agent. Watches your session history, identifies repeated multi-step workflow patterns, and "precipitates" them into new SKILL.md files. Think of it as: if you do something 3+ times across sessions, the precipitator notices and creates a skill for it.

---

## Installation

```bash
git clone https://github.com/luxuguang-leo/hermes-skill-precipitator.git /tmp/hermes-skill-precipitator
cd /tmp/hermes-skill-precipitator
python3 install.py
```

The installer:
1. Copies the skill to `~/.hermes/skills/hermes-skill-precipitator/`
2. Installs Python dependencies
3. Creates `~/.hermes/skills/hermes-skill-precipitator/config.yaml`

**Manual install:**
```bash
cp -r . ~/.hermes/skills/hermes-skill-precipitator/
pip install -r requirements.txt
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| Python | 3.10+ |
| Python packages | numpy, scikit-learn (for clustering), pyyaml |
| Session history | Honcho session DB or `~/.hermes/sessions/` directory |
| Disk | ~50MB for pattern database |

---

## Capabilities

### Core Pipeline

| Phase | What Happens |
|-------|-------------|
| **Observe** | Reads Hermes session history (Honcho or file-based) |
| **Cluster** | Groups similar multi-step interaction patterns using TF-IDF + clustering |
| **Extract** | Identifies the invariant steps vs variable parameters |
| **Template** | Generates a SKILL.md with the workflow pattern |
| **Validate** | Checks the generated skill against the SKILL.md schema |

### Discovery Controls

| Capability | Command |
|-----------|---------|
| Run discovery | `hermes-skill-precipitator run` |
| Dry-run (preview only) | `hermes-skill-precipitator run --dry-run` |
| Set minimum occurrences | `hermes-skill-precipitator run --min-occurrences 3` |
| Target specific sessions | `hermes-skill-precipitator run --sessions recent_7d` |
| Exclude patterns | `hermes-skill-precipitator run --exclude "git,terminal"` |

---

## CLI Reference

```bash
# Full discovery pass — watches all sessions, precipitates patterns
hermes-skill-precipitator run

# Dry-run: see what WOULD be created without writing files
hermes-skill-precipitator run --dry-run

# Only consider patterns that appear 5+ times
hermes-skill-precipitator run --min-occurrences 5

# Target last 30 days of sessions
hermes-skill-precipitator run --sessions recent_30d

# Exclude certain tool categories from pattern matching
hermes-skill-precipitator run --exclude "read_file,search_files"

# Show discovered patterns without generating skills
hermes-skill-precipitator patterns

# Review a specific pattern before precipitation
hermes-skill-precipitator inspect <pattern-id>

# Manually precipitate a single pattern
hermes-skill-precipitator precipitate <pattern-id>
```

---

## CorpusIQ Use Cases

### 1. Automate Growth Workflow Discovery
CorpusIQ agents follow repeatable patterns — the precipitator captures them:
```bash
hermes-skill-precipitator run --sessions corpusiq
# Discovers: "social-mining → lead-capture → email-response" pattern
# Precipitates: corpusiq-inbound-lead-workflow skill
```

### 2. Codify Tribal Knowledge
Patterns that operators do reflexively but haven't documented:
```bash
hermes-skill-precipitator patterns --status undocumented
# Surfaces: "if API fails, switch to browser" → becomes api-fallback-pattern skill
```

### 3. Skill Gap Detection
Compare discovered patterns against existing skills to find gaps:
```bash
hermes-skill-precipitator gaps
# Returns: 3 patterns with no corresponding skill — candidates for new skill creation
```

### 4. Agent Consistency Enforcement
Ensure all CorpusIQ agents follow the same discovered best practices:
```bash
hermes-skill-precipitator run --sessions all_corpusiq --min-occurrences 2
# Lower threshold across all agents → finds common patterns worth standardizing
```

### 5. Continuous Improvement Loop
Schedule as a weekly cron job:
```bash
# crontab entry
0 2 * * 1 hermes-skill-precipitator run --sessions recent_7d --min-occurrences 3
```
Every Monday at 2 AM, review and precipitate new patterns.

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `install.py` fails with import error | Missing Python packages | `pip install numpy scikit-learn pyyaml` |
| No patterns found | Not enough session history | Accumulate 7+ days of sessions before running |
| Generated skills have empty bodies | Patterns too generic | Raise `--min-occurrences` or exclude common tool calls |
| Honcho connection fails | Honcho not running | Configure `config.yaml` with correct Honcho endpoint |
| Overlapping patterns flood output | Too many similar sessions | Use `--exclude` to filter noisy tool patterns |

### Verification

```bash
# Confirm installation
ls ~/.hermes/skills/hermes-skill-precipitator/SKILL.md && echo "✓ Skill installed"

# Check config
cat ~/.hermes/skills/hermes-skill-precipitator/config.yaml

# Dry-run discovery
hermes-skill-precipitator run --dry-run 2>&1 | head -20

# Check pattern count
hermes-skill-precipitator patterns 2>&1 | wc -l
```

---

*← [Hermes Bible Skill Setup](/hermes/skills/catalog/hermes-bible-skill-setup/) | [Next: Skills Catalog →](/hermes/skills/catalog/)*
*↑ [Skills Home](/hermes/skills/)*
