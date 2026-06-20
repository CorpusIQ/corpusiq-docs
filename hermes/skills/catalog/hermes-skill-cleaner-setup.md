---
title: Hermes Skill Cleaner — Setup Guide
description: Zero-dependency TypeScript CLI to audit Hermes agent skills — token budget analysis, duplicate detection, unused skill scanning, description compression.
author: FavorPan
repo: https://github.com/FavorPan/hermes-skill-cleaner
license: MIT
---

# Hermes Skill Cleaner Setup

**A zero-dependency TypeScript CLI that audits your Hermes agent skill collection.** Identifies wasted context-window tokens, duplicate skills, unused skills, and overly verbose descriptions — with concrete cleanup recommendations.

## Quick Install

```bash
git clone https://github.com/FavorPan/hermes-skill-cleaner.git
cd hermes-skill-cleaner

# Quick budget check (fastest — skips log scanning)
node --experimental-strip-types scripts/hermes-skill-cleaner.ts --no-logs

# Full report with usage stats
node --experimental-strip-types scripts/hermes-skill-cleaner.ts
```

**Requirements:** Node.js 22+ (for `--experimental-strip-types`), zero npm dependencies.

## What It Audits

### 1. Skill Budget
Calculates what % of your context window's 2% skill budget is consumed by loaded skills, and reports remaining headroom.

```
## Skill Budget
context_window: 200,000 tokens
skill_budget:   4,000 tokens (2%)
skills_loaded:  156
skills_used:    2,850 tokens (71% of budget)
remaining:      1,150 tokens (29% of budget)
```

### 2. Duplicate Detection
Finds duplicate skills across three strategies:
- **By name** — same skill name in different directories
- **By body hash** — identical content under different names
- **By Jaccard similarity** — near-identical skills (copy-paste variants)

### 3. Usage Scanning
Parses Hermes session JSONL logs to find which skills are actually invoked. Skills with zero usage traces across recent sessions are flagged as removal candidates.

### 4. Description Bloat
Identifies skills where the YAML frontmatter description exceeds 200+ characters, with compact alternatives suggested.

## CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--no-logs` | Skip session log scanning (fastest) | off |
| `--deep-logs` | Include archived sessions in scan | off |
| `--months N` | Lookback window for log files | 3 |
| `--max-log-mb N` | Max total log bytes to scan | 300 |
| `--context-tokens N` | Override context window size | from config |
| `--budget-percent N` | Budget as % of context window | 2 |
| `--root <path>` | Add extra skill root directory | none |
| `--json` | Output JSON instead of markdown | off |
| `--model <name>` | Override model name | from config |

## Common Recipes

```bash
SCRIPT=scripts/hermes-skill-cleaner.ts

# Quick budget check
node --experimental-strip-types $SCRIPT --no-logs 2>&1 | grep -A5 "## Skill Budget"

# Full report
node --experimental-strip-types $SCRIPT

# Deep scan including archived sessions
node --experimental-strip-types $SCRIPT --months 6 --max-log-mb 800 --deep-logs

# Custom context window (e.g., 272K tokens)
node --experimental-strip-types $SCRIPT --context-tokens 272000 --budget-percent 2 --no-logs

# JSON output for scripting
node --experimental-strip-types $SCRIPT --json --no-logs

# Find unused skills
node --experimental-strip-types $SCRIPT --deep-logs --months 6 --max-log-mb 800 2>&1 | \
  grep "usage=\$0, reads=0, text=0"
```

## Recommended Cleanup Workflow

### Phase 1: Remove Duplicates
Delete 100% body-hash matched skills, keeping the shorter-path copy. Re-run after to verify.

### Phase 2: Remove Truly Unused Skills
Run with `--deep-logs` for accurate usage data. Delete skills showing `usage=$0, reads=0, text=0`.

### Phase 3: Compress Long Descriptions
Target descriptions >200 chars. Fold multi-line YAML blocks to single-line, remove redundant trigger word lists, drop duplicate translations.

Re-run after each phase to measure progress.

## Installing as a Hermes Skill

```bash
# Symlink into your skills directory
ln -s "$(pwd)" ~/.hermes/skills/hermes-skill-cleaner

# Or copy directly
cp -r . ~/.hermes/skills/hermes-skill-cleaner
```

Restart Hermes or `/reset` for the skill to be discovered. Invoke with: "audit my skills" or "clean up unused skills".

## Disabling Skill Groups

Hermes has no built-in skill disable mechanism. Move directories out:

```bash
mkdir -p ~/.hermes/skills-disabled
mv ~/.hermes/skills/<category-or-name> ~/.hermes/skills-disabled/
```

To restore: `mv ~/.hermes/skills-disabled/<name> ~/.hermes/skills/`

## Context Window Detection

The script reads Hermes context window size from (highest priority first):
1. `--context-tokens` CLI argument
2. `model.context_length` in `~/.hermes/config.yaml`
3. Fallback: **272,000 tokens**

---

*← [Session Maintenance Setup](/hermes/skills/catalog/hermes-session-maintenance-setup/) | [Skills Catalog →](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
