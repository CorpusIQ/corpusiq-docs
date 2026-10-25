---
title: "New Skills - October 25, 2026 Morning"
description: "Skills.sh sweep (Oct 25 morning): 93 new skills, three publisher clusters from the trending board and the NEW lane totalling 155,652 combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct25-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-25"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 25, 2026 Morning Sweep

Morning sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 885 unique skills with 0 failed queries: 93 NEW, 270 PARTIAL.

The NEW lane stayed silent above the 1,000-install trigger for the thirteenth consecutive fire, its top row amirtaherkhani/nestjs-skills nestjs-oop-design-patterns at 379. The lane still produced one convert, because the publisher query is not gated on the row size: tw93/Waza showed as a 208-install row and sized at 120,051 combined across 11 listings once queried by publisher, a 577x multiple and the largest in this catalog's recorded history. The trending board served 527 entries across 53 sources, 51 of them already covered, and both uncovered sources cleared the floor.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 885 (0 failed queries) |
| NEW (not in catalog) | 93 |
| PARTIAL (source known, skill not cataloged) | 270 |
| New publisher guides | 3 (18 indexed listings, 155,652 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 45 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (737 markdown files); 0 converts |
| Board | Trending 527 entries / 53 sources; 51 covered, 2 uncovered, 2 converts |
| Marketplace count | 1,157+ to 1,160+ |

## New Publisher Guides

### 1. Waza (120,051 combined)

**Source:** [tw93/waza](https://www.skills.sh/tw93/waza), 11 indexed listings, top skill `health` at 18,538; 7,356 stars; MIT; pushed 2026-10-25.

Eight engineering habits, one skill each, behind a dispatcher that routes an unprompted request to the right one. Plan with `think`, debug to root cause with `hunt`, review the diff and ship with `check`, audit the agent's own configuration with `health`, and cover reading, research, prose and UI with `read`, `learn`, `write` and `ui`. Every skill states its outcome, its red lines and how the result is verified, and then stops rather than scripting the model's path.

Beta tier, and the reservation is security rather than quality. Gen Agent Trust Hub fails `think` on credential handling, because it opens the project config including `.env` and lifts live values into the plan, and fails the `waza` dispatcher entry on install scripts, session-log collection and third-party fetch proxies. Snyk adds `W011` and `W012` on `check`, `read` and `learn`. None of it is hidden, the README tells you to review the scripts, and the guide states each finding with its evidence.

### 2. Diagram Design (18,846 combined)

**Source:** [cathrynlavery/diagram-design](https://www.skills.sh/cathrynlavery/diagram-design), 1 indexed listing at 18,846; 60,868 stars; MIT; pushed 2026-10-24.

Forty-five diagram types rendered as one self-contained HTML file with inline SVG, in the reader's brand. The style is a written contract rather than a theme: one accent for the one or two things that matter, 1px hairlines, no shadows, a 4px grid and a density target of four out of ten. Onboarding pulls the palette and font stack from a site, maps them onto semantic tokens, verifies WCAG AA contrast and writes the result. Imports redraw `.drawio`, Mermaid and `.excalidraw` sources into the same system, and every SVG ships with an accessible name and description.

Production tier. One focused skill, a pinned motion controller, no network request beyond a fonts load that can be turned off, and all three auditors passing on its only listing. The honest limit, stated in the guide, is that the output is not a source format: there is nothing to diff in review, so Mermaid remains right for diagrams that change every sprint.

### 3. REA (16,755 combined)

**Source:** [morluto/rea](https://www.skills.sh/morluto/rea), 6 indexed listings, top skill `reverse-engineer-anything` at 10,508; 381,166 stars; MIT; pushed 2026-10-25.

One MCP server for reverse engineering: native binaries through an existing Hopper, Ghidra or IDA install, JavaScript and Electron applications, .NET assemblies, Android APKs, firmware images, model artifacts, GPU code objects, packet captures and live websites. The static paths need no provider at all, and every finding comes back with the evidence behind it and an explicit statement of what could not be determined.

Beta tier. Gen Agent Trust Hub records a MEDIUM warning: runtime execution of an unpinned `npx` package, a setup step that can rewrite the client's MCP configuration and replace the bundled skill, and an injection surface that is structural to reading adversary-controlled artefacts. The guide draws the line the tool draws: static inspection reads without executing, and runtime capture of a target is a licensing decision as much as a technical one.

## Why This Fire Matters

The three converts are all discipline skills rather than API skills, and that is now the third fire in a row where the interesting finds came from that lane: an audit that writes plans instead of patches, a set of rules that forbid guessing, a lint preset that defines the standard. This fire adds the habit layer from a single widely installed author, the brand layer for the one artefact agents most often produce badly, and the evidence layer for software an agent cannot read as source.

The Waza find is also the strongest argument yet for sizing every NEW-lane source by publisher rather than by row. A 208-install row became 120,051 combined, a 577x multiple that no threshold on the row itself would ever have surfaced. The board's two finds ran 32x (REA, 519 to 16,755) and 40x (Diagram Design, 465 to 18,846). Nothing that looked small was small.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (737 markdown files) and found 0 of the 45 PARTIAL sources at 100 or more installs without a page. `/popular` returned HTTP 404 again and `/skills` remains a shell with no embedded skill JSON, so the trending board is still the only board that returns data.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
