---
title: "Open Artifact - Agent-Native Artifacts Suite Setup"
description: "jimliu/open-artifact: agent-agnostic artifacts for slides, dashboards, design systems, whiteboards, docs, motion - 16.8K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/open-artifact-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "design", "slides", "artifacts"]
---

# Open Artifact - Agent-Native Artifacts Suite Setup

**Source:** [jimliu/open-artifact](https://www.skills.sh/jimliu/open-artifact) via skills.sh - 16.8K combined installs across 20 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [JimLiu/open-artifact](https://github.com/JimLiu/open-artifact) - 223 stars, Apache-2.0 license, main branch, last pushed Nov 22, 2026; eight artifact-type skills under `artifact-types/<type>/SKILL.md` plus a `/open-artifact` router skill and per-host plugins.
**Category:** Design and Creative Artifacts
**Quality Tier:** 🟠 Orange - 4 Fail cells across the 20 sampled skills (Socket Fail on baoyu-design, Gen Agent Trust Hub Fail on design-system, Snyk Fails on design and whiteboard), with seven claude-* names returning not parsed.

Open Artifact lets any coding agent turn a plain-text request into a real, editable artifact: a slide deck, a UI design canvas, a design system, a whiteboard, a spreadsheet, a data dashboard, a living document or a short animated film. The agent writes a plain folder of files, a local daemon serves them as a live page, and the person can edit, comment and export (PDF, PPTX, PNG, HTML, MP4 and more) before sending comments back to the agent session. Everything runs on the machine with no account, upload or vendor lock-in, and the suite is agent-agnostic with plugins for Claude Code, Codex, Cursor, Copilot, Antigravity, ChatGPT and DeepSeek Harness.

The project is the rebuild of an earlier one-skill-per-type effort: the README notes it was formerly baoyu-design, which brought claude.ai-style artifact types to local agents. The flagship listing baoyu-design (6,985 installs) is that former name, and it is a separate repository from jimliu/baoyu-skills, which is catalogued separately. The current tree ships eight artifact-types/ skills plus the /open-artifact router, while the index still carries the legacy baoyu-design and claude-* names with no directory of their own.

## Installation

The recommended install is a plugin bundle per agent app. Install Node.js 22.18 or newer, download open-artifact-plugins.zip from the Assets section of a GitHub Release, and extract it to a permanent location. Each app then installs from the extracted folder (Claude Code adds it as a marketplace, Codex via codex plugin marketplace add, Cursor by copying the folder to ~/.cursor/plugins/local/open-artifact).

For skills only, copy the router folder from the extracted bundle to the agent's skill directory:

```bash
cp -r codex/skills/open-artifact/ ~/.claude/skills/
```

From a source checkout, build the workspace and plugin folders:

```bash
npm ci
npm run build
node scripts/build-plugins.mjs
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| baoyu-design | 6,985 | flagship listing under the repo's former name, no directory in the current tree |
| release-skills | 3,052 | index-only listing, no directory in the current tree |
| claude-design | 1,276 | legacy claude.ai-style listing name, no directory in the current tree |
| claude-design-system | 1,228 | legacy claude.ai-style listing name, no directory in the current tree |
| claude-slides | 1,162 | legacy claude.ai-style listing name, no directory in the current tree |
| claude-dashboard | 1,088 | legacy claude.ai-style listing name, no directory in the current tree |
| dataviz | 875 | index-only listing, no directory in the current tree |
| claude-motion | 480 | legacy claude.ai-style listing name, no directory in the current tree |
| motion-director | 450 | index-only listing, no directory in the current tree |
| claude-whiteboard | 102 | legacy claude.ai-style listing name, no directory in the current tree |

The remaining 10 indexed listings range from 1 to 63 installs.

## Why This Matters for Hermes Agents

Open Artifact attacks a real gap: agents usually return files or chat answers, not things a person can open, edit and react to. The local daemon and page frame mean a slides or dashboard request produces a folder of plain files that opens in a browser editor, which is a stronger loop than an agent dumping HTML or JSON. The format is agent-agnostic and local-first, with no account, upload or vendor lock-in, so it fits a Hermes workflow that keeps everything on the machine. The eight artifact types share one design: a SKILL.md that tells the agent how to write the format, a reference folder documenting the file layout, and an artifact-type.json for hosts, which is a repeatable pattern worth borrowing when packaging a new artifact type. The counterweight is the security sample, which puts a Socket Fail on the baoyu-design flagship, a Gen Agent Trust Hub Fail on design-system and Snyk Fails on design and whiteboard, and leaves seven legacy listings unparsed, so the audit picture is not clean despite an Apache-2.0 licence and 223 stars.

## Usage

| You say | What happens |
|---|---|
| /open-artifact slides a 6-slide pitch for this repo | Writes a deck folder and opens it as an editable local page with a slide rail and export |
| /open-artifact design three landing page options | Creates a Design canvas with three artboards you can move, retype and comment on |
| /open-artifact whiteboard a retro board for last sprint | Builds a shared infinite board with stickies, shapes and arrows for the team |
| /open-artifact data a dashboard of signups by month from signups.csv | Produces a live dashboard from the uploaded data with sources for each number |
| /open-artifact docs a hiring plan for 2027 | Creates a living document with tabs you can edit, comment on and export as Word or PDF |
| /open-artifact motion a 20-second launch animation | Makes a short animated film from HTML, CSS and JavaScript scenes with a generated score |

## Verification

Confirm the router skill landed and inspect its artifact list:

```bash
curl -sL https://raw.githubusercontent.com/JimLiu/open-artifact/main/skills/open-artifact/SKILL.md | head -40
```

Review the Design type's file format before generating a canvas:

```bash
curl -sL https://raw.githubusercontent.com/JimLiu/open-artifact/main/artifact-types/design/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| baoyu-design | Pass | Fail | Pass |
| release-skills | Pass | Pass | Pass |
| claude-design | not parsed | not parsed | not parsed |
| claude-design-system | not parsed | not parsed | not parsed |
| claude-slides | not parsed | not parsed | not parsed |
| claude-dashboard | not parsed | not parsed | not parsed |
| dataviz | Pass | Pass | Pass |
| claude-motion | not parsed | not parsed | not parsed |
| motion-director | Pass | Pass | Pass |
| claude-whiteboard | not parsed | not parsed | not parsed |
| claude-data | not parsed | not parsed | not parsed |
| open-artifact | Pass | Pass | Warn |
| design | Pass | Pass | Fail |
| design-system | Fail | Pass | Warn |
| data | Pass | Pass | Warn |
| whiteboard | Pass | Pass | Fail |
| slides | Pass | Pass | Warn |
| sheets | Warn | Pass | Warn |
| docs | Pass | Pass | Warn |
| motion | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 21, 2026: 16,807 combined installs across 20 indexed listings; 223 GitHub stars; Apache-2.0 license; last pushed Nov 22, 2026. Counts drift over time.
- The install index carries legacy names from the baoyu-design era: eleven of the twenty listings (baoyu-design, release-skills, the six claude-* names, dataviz and motion-director) have no directory in the current tree, which ships eight artifact-types/ skills plus the /open-artifact router.
- The flagship baoyu-design listing is the repo's former name and is a separate repository from jimliu/baoyu-skills, which is catalogued separately.
- The security sample is mixed: four Fail cells (Socket on baoyu-design, Gen Agent Trust Hub on design-system, Snyk on design and whiteboard) and seven skills with not parsed verdicts.
- Install is heavier than a single CLI command: the recommended path is a Node.js 22.18+ runtime plus a downloaded plugin ZIP per app, or a full source build with npm ci and a Rust toolchain only when changing a crate.

## Related

- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Superdesign Skill - Canvas Design & Inspiration Setup](/hermes/skills/catalog/superdesign-skill-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the /open-artifact router skill; it dispatches any of the eight types from one prompt and keeps the agent from hand-rolling HTML or JSON.
- Install the plugin bundle rather than the skills-only copy if you want comments to flow back into the session; the skills-only path drives the daemon from the command line.
- For one-off experiments, run a single type without the daemon: `node artifact-types/design/scripts/cli.mjs open ./my-design --type design`.
- Keep the Rust toolchain out of the loop unless you change a crate; the compiled WASM output is committed, so most builds need only Node.
- Review the four Fail-flagged skills (baoyu-design, design-system, design, whiteboard) against the skills.sh pages before generating artifacts in a repo with secrets.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
