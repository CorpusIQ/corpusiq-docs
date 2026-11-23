---
title: "MapLibre Agent Skills - Mapping Code Guidance Setup"
description: "Community-maintained MapLibre GL JS agent skills that help AI coding assistants write better mapping code - 5.2K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/maplibre-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "mapping", "geospatial", "webgl"]
---

# MapLibre Agent Skills - Mapping Code Guidance Setup

**Source:** [maplibre/maplibre-agent-skills](https://www.skills.sh/maplibre/maplibre-agent-skills) via skills.sh - 5.2K combined installs across 13 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [maplibre/maplibre-agent-skills](https://github.com/maplibre/maplibre-agent-skills) - 165 stars, MIT, main branch, last pushed Nov 23, 2026; one SKILL.md per skill directory under skills/, with the eval harness and results under evals/.
**Category:** Geospatial Mapping and WebGL Development
**Quality Tier:** 🟡 Yellow - 2 Warn cells (Snyk on mapbox-migration and terrain-rendering) and no Fail cells across the 13-skill sample.

MapLibre Agent Skills is a community-maintained collection of curated guidance for AI assistants building MapLibre applications. Each skill is a markdown file an agent reads as context, and the suite exists to give an agent the judgment to avoid common API gotchas and to suggest patterns that work when it is asked to implement something with MapLibre GL JS. New skills are prioritized by reported AI failures, recent API and library changes, and long-standing issues documented in GitHub, Stack Overflow or the community Slack.

The distinguishing feature is the correctness guarantee. Every skill must be accurate, actionable, warranted and attributed, and each one carries a metadata.status field that records whether a Promptfoo eval proved it fixes a real failure (verified) or is still provisional. The README walks install through paste-into-chat, project copy, a Claude Code plugin and the skills CLI, and it states that installs copy skill directories only, so a wrong skill should be reported through the AI failure report form rather than patched in place.

## Installation

Install as a Claude Code plugin:

```text
/plugin install maplibre-agent-skills --marketplace maplibre/maplibre-agent-skills
```

The plugin carries every skill in skills/ except the maintainers' eval runbook. Through the skills CLI:

```bash
npx skills add maplibre/maplibre-agent-skills
```

For a single skill, a listing, a global install or a specific agent:

```bash
npx skills add maplibre/maplibre-agent-skills --list
npx skills add maplibre/maplibre-agent-skills --skill maplibre-tile-sources
npx skills add maplibre/maplibre-agent-skills -g
npx skills add maplibre/maplibre-agent-skills -a claude-code
```

Without the CLI the skills are plain markdown: paste a SKILL.md into chat, copy skills/<name>/ to .agents/skills/ or .claude/skills/, or symlink the skills directory into .claude/.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| maplibre-tile-sources | 1,201 | choosing GeoJSON versus vector or raster tiles for your data |
| maplibre-pmtiles-patterns | 905 | serverless tiles via single-file PMTiles and HTTP range requests |
| maplibre-cartography | 633 | styling maps so labels, markers and roads stay readable |
| maplibre-mapbox-migration | 536 | moving a Mapbox GL JS app to MapLibre |
| maplibre-source-wiring | 414 | getting a configured source to actually render |
| maplibre-fonts-glyphs | 339 | glyphs URLs, font PBFs and non-Latin scripts |
| maplibre-terrain-rendering | 311 | hillshade, color-relief, contours and 3D terrain |
| maplibre-v6-migration | 290 | fixing a v5 app that breaks after upgrading to v6 |
| maplibre-skill-authoring | 233 | capturing a MapLibre research task as a new skill |
| maplibre-sprites-icons | 141 | sprites, addImage and missing-icon diagnosis |
| maplibre-running-evals | 79 | running this repository's Promptfoo evals for a skill |
| maplibre-terrain-patterns | 50 | retired terrain skill, superseded by maplibre-terrain-rendering |

The remaining 1 indexed listing is maplibre-native-gl-js-parity at 47 installs.

## Why This Matters for Hermes Agents

An agent that writes MapLibre code without these skills trips over the specific primitives this suite encodes: a source that is configured but draws nothing, a raster endpoint named "hillshade" that is not raster-dem, a sprite or glyphs URL that leaves labels and icons missing, or a v5 app that silently breaks on v6. The highest-value skill is maplibre-tile-sources, the most-installed at 1,201, which decides whether a dataset needs GeoJSON, vector tiles or raster tiles before any code is written. maplibre-source-wiring and maplibre-fonts-glyphs cover the two blank-map failure modes an agent cannot diagnose from a stack trace, and maplibre-mapbox-migration turns a Mapbox-to-MapLibre port into a checked procedure. For a builder the metadata.status field is the trust signal: it tells you whether a skill is verified by an eval or still provisional, so an agent can weigh the guidance it reads rather than treat every skill as equally proven.

## Usage

| You say | What happens |
|---|---|
| Install MapLibre skills | Adds maplibre/maplibre-agent-skills through the CLI or plugin |
| Why is my map blank? | Uses maplibre-source-wiring to diagnose CORS, glyph and layer-order causes |
| Should I use GeoJSON or tiles? | Uses maplibre-tile-sources to pick the source type for the dataset |
| Host tiles without a server | Uses maplibre-pmtiles-patterns for single-file PMTiles hosting |
| Move my Mapbox app to MapLibre | Uses maplibre-mapbox-migration for the port procedure |
| My labels render in the wrong font | Uses maplibre-fonts-glyphs for glyphs URLs and local-font fallback |
| My v5 app broke on v6 | Uses maplibre-v6-migration for the upgrade changes |

## Verification

Confirm the repository README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/maplibre/maplibre-agent-skills/main/README.md | head -40
```

Confirm the most-installed skill body is present before relying on it for source decisions:

```bash
curl -sL https://raw.githubusercontent.com/maplibre/maplibre-agent-skills/main/skills/maplibre-tile-sources/SKILL.md | head -30
```

Confirm the source-wiring skill body is present before using it for blank-map diagnosis:

```bash
curl -sL https://raw.githubusercontent.com/maplibre/maplibre-agent-skills/main/skills/maplibre-source-wiring/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| maplibre-tile-sources | Pass | Pass | Pass |
| maplibre-pmtiles-patterns | Pass | Pass | Pass |
| maplibre-cartography | Pass | Pass | Pass |
| maplibre-mapbox-migration | Pass | Pass | Warn |
| maplibre-source-wiring | Pass | Pass | Pass |
| maplibre-fonts-glyphs | Pass | Pass | Pass |
| maplibre-terrain-rendering | Pass | Pass | Warn |
| maplibre-v6-migration | Pass | Pass | Pass |
| maplibre-skill-authoring | Pass | Pass | Pass |
| maplibre-sprites-icons | Pass | Pass | Pass |
| maplibre-running-evals | Pass | Pass | Pass |
| maplibre-terrain-patterns | Pass | Pass | Pass |
| maplibre-native-gl-js-parity | Pass | Pass | Pass |

Two Snyk Warns (mapbox-migration and terrain-rendering) and no Fail across the 13 sampled skills; all 13 listings carry a published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,179 combined installs across 13 indexed listings; 165 GitHub stars; MIT; last pushed Nov 23, 2026. Counts drift over time.
- The maplibre-terrain-patterns listing (50 installs) has no counterpart directory in the current tree: the repository commit history shows it was replaced by maplibre-terrain-rendering, so the indexed name is a retired one.
- The install index and the current tree otherwise agree, with maplibre-native-gl-js-parity at 47 installs the only listing not shown in the table above.
- Install counts fall steeply from the 1,201-install head to the 47-install tail, so the top few skills are far more battle-tested than the long tail.
- Several skills carry a provisional metadata.status rather than a verified one, so an eval has not proven every skill fixes a real failure.

## Related

- [Mapbox Agent Skills - Location Development Suite Setup](/hermes/skills/catalog/mapbox-agent-skills-setup)
- [Geo-Sleuth - Photo Geolocation for Agents](/hermes/skills/catalog/geo-sleuth-setup)
- [AntV Chart Visualization Skills - Data to Charts](/hermes/skills/catalog/antvis-chart-visualization-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with maplibre-tile-sources to settle the data question first; it is the most-installed skill and the one every later decision depends on.
- Trust the metadata.status field: verified skills have an eval backing them, while provisional skills are guidance without a proven gap.
- Fix a wrong skill by filing the AI failure report form, not by editing the installed copy, which the next update overwrites.
- Use the plugin for the full set and the CLI --skill flag to pull a single skill into a project without the eval runbook.
- For a Mapbox-to-MapLibre port, run maplibre-mapbox-migration and treat its Snyk Warn as a reason to review the skill body before relying on it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
