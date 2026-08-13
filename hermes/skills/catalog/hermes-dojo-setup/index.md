---
title: Hermes Dojo — Self-Improvement System Setup Guide
description: Install and configure the Hermes Dojo self-improvement system that monitors agent performance, finds weak skills, fixes them via self-evolution, and reports results.
publisher: yonkoo11/hermes-dojo
stars: 138
installs: 27
quality_tier: 🔵 Community
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-dojo-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Dojo — Self-Improvement System Setup Guide

The Hermes Dojo is a self-improvement system for Hermes Agent. It monitors agent performance, identifies weak skills, applies fixes through self-evolution, and generates detailed improvement reports. Think of it as a personal trainer for your Hermes agent — constantly watching, evaluating, and strengthening.

**Publisher:** [yonkoo11/hermes-dojo](https://github.com/yonkoo11/hermes-dojo) — 138⭐  
**Source:** skills.sh  
**Quality Tier:** 🔵 Community (untested by CorpusIQ)

---

## What It Does

- **Performance Monitoring:** Continuously evaluates Hermes Agent performance across tasks
- **Skill Gap Detection:** Identifies weak or underperforming skills in the agent's repertoire
- **Self-Evolution:** Automatically patches and improves skills that show deficiencies
- **Improvement Reports:** Generates detailed reports on what was fixed and how performance changed
- **Training Loop:** Runs in a continuous improvement cycle — monitor → detect → fix → report

---

## Prerequisites

| Requirement | Check |
|-------------|-------|
| Hermes Agent installed | `hermes --version` |
| `npx` available | `npx --version` |
| GitHub access | Required for skill installation |
| Agent profile configured | `hermes profile list` |

---

## Installation

### Step 1: Install from skills.sh

```bash
npx skills add https://github.com/yonkoo11/hermes-dojo --skill hermes-dojo
```

### Step 2: Verify Installation

```bash
hermes skills list | grep hermes-dojo
```

Expected output:
```
hermes-dojo    🔵 Community    yonkoo11/hermes-dojo    Self-improvement system
```

### Step 3: Configure the Dojo

The Dojo needs to know which Hermes profile to monitor and what improvement thresholds to use. Create a configuration:

```bash
mkdir -p ~/.hermes/dojo
```

Create `~/.hermes/dojo/config.yaml`:

```yaml
# Hermes Dojo Configuration
profile: corpusiq                    # Profile to monitor and improve
check_interval: 3600                 # How often to check (seconds) — hourly
improvement_threshold: 0.7          # Skill score below this triggers improvement
max_auto_fixes_per_cycle: 3         # Limit automatic changes per cycle
report_detail: full                 # full | summary | metrics
notify_on_improvement: true         # Send notification when skills are improved
```

---

## Usage

### Run a Manual Improvement Cycle

```bash
hermes skill invoke hermes-dojo --action audit
```

This performs a one-time audit of all skills in the configured profile, scores them, and identifies the weakest ones.

### Run Continuous Monitoring

```bash
hermes skill invoke hermes-dojo --action watch
```

Runs the Dojo in continuous mode — it monitors, detects weaknesses, applies fixes, and reports on the configured interval.

### Generate a Report

```bash
hermes skill invoke hermes-dojo --action report
```

Generates a summary report of the last improvement cycle.

---

## What to Expect

When the Dojo runs an improvement cycle, it:

1. **Audits** all installed skills for performance metrics
2. **Scores** each skill on a 0.0–1.0 scale based on error rates, completion times, and success patterns
3. **Identifies** skills below the configured threshold
4. **Attemts fixes** — reads the skill's SKILL.md, identifies gaps, and proposes improvements
5. **Applies changes** if confidence is high enough
6. **Reports** what was changed and the before/after scores

**Sample output:**
```
[Dojo Audit] Profile: corpusiq | Time: 2026-07-31T14:00:00Z
  Scanned: 96 skills
  Healthy: 89 (92.7%)
  Needs Improvement: 7
  
  Fixing: corpusiq-email-send-checklist (score: 0.62 → 0.84)
    → Added rate limit handling for Gmail API
    → Updated OAuth token refresh logic
  Fixing: corpusiq-preflight-post (score: 0.58 → 0.79)
    → Added content validation for image alt-text
    → Patched URL verification step
```

---

## Integration with CorpusIQ

For CorpusIQ agent workflows, the Hermes Dojo can:

- **Skill Auditing:** Run weekly audits of all CorpusIQ growth skills
- **Self-Healing:** Auto-patch skills that start failing after API changes
- **Performance Tracking:** Monitor improvement trends over time
- **Continuous Optimization:** Keep the agent's 96+ skills at peak performance

### Recommended Cron Setup

```bash
# Weekly skill audit — Monday 6 AM
0 6 * * 1 hermes skill invoke hermes-dojo --action audit --profile corpusiq

# Daily improvement report — 6 PM
0 18 * * * hermes skill invoke hermes-dojo --action report --profile corpusiq
```

---

## Verification

After installation, verify the Dojo is working:

```bash
# 1. Check skill is installed
hermes skills inspect hermes-dojo

# 2. Run a dry-run audit (no changes)
hermes skill invoke hermes-dojo --action audit --dry-run

# 3. Check the report directory
ls ~/.hermes/dojo/reports/
```

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "Profile not found" | Wrong profile name in config | Check with `hermes profile list` and update `config.yaml` |
| "No skills to audit" | Profile path incorrect | Verify `profile` in config points to an active Hermes profile |
| "Permission denied" | Dojo can't write to skill directory | Ensure Hermes has write access to `~/.hermes/profiles/<name>/skills/` |
| Improvements not applying | Confidence threshold too high | Lower `improvement_threshold` or run with `--force` flag |

---

## Related Skills

- [hermes-agent-self-evolution](/hermes/skills/catalog/hermes-agent-self-evolution-setup/) — Auto-learning framework
- [skill-vetter](/hermes/skills/catalog/skill-vetter-setup/) — Security audit for skills
- [skill-creator](/hermes/skills/catalog/skill-creator-setup) — Anthropic's skill creation framework

---

*Discovered July 31, 2026 · Published by yonkoo11 · 138 GitHub stars*
