---
title: "Geo-Sleuth - Photo Geolocation for Agents"
description: "oldcircle/geo-sleuth: 4.9K combined installs across 1 listing; finds where a photo was taken via OSM geometry, skylines and satellite imagery."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/geo-sleuth-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "geolocation", "OSINT", "photo analysis"]
---

# Geo-Sleuth - Setup Guide

**Source:** [oldcircle/geo-sleuth](https://www.skills.sh/oldcircle/geo-sleuth) via skills.sh - 4.9K combined installs across 1 indexed listing; first seen Nov 17, 2026 (this sweep)
**GitHub:** 7,225 stars, MIT license, `main` branch, last pushed 2026-11-16; one skill folder at `skills/geo-sleuth/` with `SKILL.md`, `scripts/`, `references/`, `regions/` and `data/` (147 files)
**Category:** OSINT / photo geolocation agent skill
**Quality Tier:** 🟡 Yellow - 2 Pass and 1 Warn (Snyk) on the single listed skill.

geo-sleuth is a single Agent Skill that finds where a photo was taken, and when, and shows its work. It is built for frames that have nothing to read: no sign, no plate, no landmark. OpenStreetMap geometry, elevation skylines, satellite tiles and street view carry the search, and every conclusion has to point at the command that ran and the file it produced.

The workflow is split into three layers. `intake.py` reads EXIF, runs OCR and reverse image search on Baidu and Yandex in one command; `board.py` keeps a candidate board with clues, likelihood ratios and the next step; then the skill branches into sun and shadow math, skyline fitting against elevation data and OSM corridor searches, or CLIP-ranked satellite tiles and DINOv2-plus-SIFT street view matching. The output is coordinates plus an error radius, a camera heading, an evidence image and a tiered confidence.

## Installation

Install with the `skills` CLI, or copy the folder by hand. One command covers all six agents user-wide:

```bash
npx skills add Oldcircle/geo-sleuth -g -a claude-code -a codex -a cursor -a gemini-cli -a opencode -a github-copilot -y
```

By hand:

```bash
git clone https://github.com/Oldcircle/geo-sleuth
mkdir -p ~/.agents/skills ~/.claude/skills
cp -r geo-sleuth/skills/geo-sleuth ~/.agents/skills/
ln -s ~/.agents/skills/geo-sleuth ~/.claude/skills/geo-sleuth
```

Requirements are Python 3.10+, `uv`, `curl`, and an agent that can run shell commands. Reverse image search needs Google Chrome or Playwright Chromium; install the latter with `uvx playwright install chromium`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| geo-sleuth | 4,877 | Geolocate or chronolocate a photo with tool-verified reasoning: EXIF, OCR, reverse image search, skyline fitting, satellite and street view, sun and shadow math. |

No indexed listings fall below the threshold; the single listing appears above.

## Why This Matters for Hermes Agents

geo-sleuth replaces guessing with a checkable chain of evidence. Instead of the model eyeballing a photo and proposing a plausible city, each candidate has to survive a scored filter: intake reads EXIF and runs OCR and reverse image search, the candidate board ranks clues and names the next step, and the model only judges among the top few survivors. That division of labor is the interesting part for agent work: twenty-odd single-purpose scripts do the perception and ranking, and the model's judgment is reserved for the few decisions that need it. Every conclusion must name the command that ran and the file it produced, so a wrong answer fails loudly instead of silently. For Hermes agents the same pattern transfers to any task where an agent should not trust a guess: make the tool rank first and have the model judge last.

## Usage

| You say | What happens |
|---|---|
| "find where this photo was taken" | Runs intake.py (EXIF, OCR, reverse image search), builds a candidate board, narrows via skyline, satellite or street view, and returns coordinates plus an error radius and evidence image. |
| "when was this photo taken" | Sun and shadow math estimates time of day, latitude band and heading from shadows and lit faces. |
| "there is no text, plate or landmark" | Falls back to OSM geometry, elevation skylines and terrain scans instead of reading the frame. |
| "run doctor.py" | Checks Python, uv, curl, lookup tables, a writable working directory and a browser launch; `--network` probes services without uploading photos. |
| "compare this photo against street view" | match.py ranks candidate ground-level images with DINOv2 similarity plus SIFT inliers and returns the top few for a human look. |

## Verification

Confirm the skill exists on `main`, then run the environment check:

```bash
curl -fsSL https://raw.githubusercontent.com/Oldcircle/geo-sleuth/main/skills/geo-sleuth/SKILL.md | head -20
uv run skills/geo-sleuth/scripts/doctor.py
```

On first use, ask the agent to run `doctor.py` from the installed skill's `scripts/` folder and fix any failed checks before a real search.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| geo-sleuth | Pass | Pass | Warn |

The sample is a full census of the one listed skill: Gen Agent Trust Hub and Socket pass, Snyk warns.

## Limitations

- Snapshot data, verified 2026-11-17: 4,877 combined installs across 1 indexed listing; 7,225 GitHub stars; MIT; last pushed 2026-11-16. Counts drift over time.
- Reverse image search runs on Baidu and Yandex only; Google Lens is on the roadmap. Both need Chrome or Playwright Chromium, and services can return 403 or CAPTCHA.
- The two documented blind re-runs land 3 m and 87 m from ground truth, but the README states these are regression checks on photos the skill has seen before, not an accuracy figure on unseen photos; a public blind-test set is still on the roadmap.
- First use downloads roughly 2.4 GB (torch plus model weights), and model downloads need network access even when a later step runs locally.
- OSM data is queried live under ODbL; none ships in the repository, and you must credit OpenStreetMap contributors when publishing query results.
- Responsible-use limit from the README: run it on your own photos or ones you have permission to analyze, never to find people who have not agreed to be found.

## Related

- [OSINT Skills - Open-Source Intelligence Suite Setup](/hermes/skills/catalog/osint-skills-setup)
- [Apify Awesome Skills - Lead and Market Intelligence](/hermes/skills/catalog/apify-awesome-skills-setup)
- [GEO SEO Claude - Generative Engine Optimisation](/hermes/skills/catalog/geo-seo-claude-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- On first use, have the agent run `doctor.py` from the installed skill's `scripts/` folder and fix any failed checks before a real search.
- Reverse image search needs Chrome or Playwright Chromium; run `uvx playwright install chromium` if the browser launch check fails.
- Keep the complete skill folder, including `data/` and the helper modules in `scripts/`, or lookups and scripts will break.
- Runs are slow: the documented cases took 32 to 72 minutes and dozens of tool calls; a long run is normal rather than a failure.
- Run it only on your own photos or ones you have permission to analyze; never use it to find people who have not agreed to be found.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
