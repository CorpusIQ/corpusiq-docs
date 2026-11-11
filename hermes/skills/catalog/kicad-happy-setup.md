---
title: "KiCad Happy - Electronics Design Review Skills Setup"
description: "KiCad design review: 8.2K combined installs across 12 listings, schematic and layout analysis, EMC pre-checks, SPICE and BOM sourcing"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kicad-happy-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "kicad", "pcb design", "hardware engineering", "emc"]
---

# KiCad Happy - Setup Guide

**Source:** [aklofas/kicad-happy](https://www.skills.sh/aklofas/kicad-happy) via skills.sh - 8.2K combined installs across 12 indexed listings (8,216 exact); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 1,644 stars, MIT license, `main` branch, last pushed 2026-11-08, 11 `SKILL.md` files under `skills/<name>/` plus a `tools/` directory of Python helpers
**Category:** Hardware design: schematic and PCB analysis, design review, EMC pre-compliance, SPICE simulation, component sourcing and fabrication prep
**Quality Tier:** 🟡 Mixed - MIT licensed, actively maintained and unusually concrete in its outputs, with four Snyk Warns and one Socket Warn across twelve sampled skills and one indexed listing that has no skill directory in the current tree.

Hardware is the domain where an agent's confident wrong answer costs money in copper rather than in tokens. KiCad Happy is built around that asymmetry: it parses an actual project into structured data, computes real values from the component network, and reports what it found rather than what a board usually looks like. The README's own framing is blunt about the payoff, catching real bugs before you order boards.

It works on the open format. KiCad projects are S-expression files, so schematics, PCB layouts and Gerbers can be read directly without an EDA licence or a GUI. The repository ships Python tooling in `tools/` alongside the skill files, which is why the skills can compute a feedback divider ratio or an RC cutoff frequency instead of describing what one would be.

The output shown in the README is the reason this belongs in a catalog. On an open-source robot controller board it builds a power tree with computed rail voltages and dissipation, identifies functional subcircuits such as motor drive, input filtering and an addressable LED chain, audits nineteen connectors for ESD protection and reports that all nineteen have coverage gaps, validates passive networks against their marked values, and suggests applicable certifications from what it detected, in that case FCC Part 15 Subpart B and CISPR 32 for the EU market.

## Installation

The Claude Code plugin path is the documented default:

```bash
/plugin marketplace add aklofas/kicad-happy
/plugin install kicad-happy@kicad-happy
```

The README flags a known Claude Code issue where `/plugin update` may not detect new versions, and gives the workaround: clear the plugin cache and reinstall.

```bash
rm -rf ~/.claude/plugins/cache/kicad-happy ~/.claude/plugins/marketplaces/kicad-happy
/plugin marketplace add aklofas/kicad-happy
/plugin install kicad-happy@kicad-happy
```

The README lists support beyond Claude Code: OpenAI Codex, GitHub Copilot CLI, Google Antigravity and opencode, plus a GitHub Action for automated pull request reviews and the standalone Python scripts for anything else. It also points at `install-guidance.md` specifically for an agent to read, covering platform quirks, known bugs, workarounds and OS-specific issues, which is a useful pattern in its own right for a repository whose install surface varies by agent.

Python 3.10 or later is required for the tooling. The repository carries the usual multi-agent scaffolding directories (`.claude-plugin`, `.codex-plugin`, `.cursor`, `.opencode`, `.agents`), so the skills are plain markdown with helper scripts and can be copied into a Hermes profile skills directory if the plugin marketplace is not your path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| kicad | 1,205 | Parsing a KiCad project into structured data, tracing nets and running the main design review |
| jlcpcb | 889 | Preparing and checking a board for JLCPCB fabrication |
| bom | 804 | Bill of materials handling, MPN assignment and BOM lock status |
| lcsc | 738 | LCSC component lookup and part selection |
| spice | 722 | SPICE simulation of extracted circuits |
| emc | 716 | EMC pre-compliance checks and applicable certification suggestions |
| datasheets | 697 | Downloading and cross-referencing component datasheets against design values |
| digikey | 592 | Digi-Key component sourcing |
| pcbway | 572 | Preparing and checking a board for PCBWay fabrication |
| mouser | 572 | Mouser component sourcing |
| element14 | 542 | Element14 component sourcing |
| kidoc | 167 | KiCad documentation handling |

All twelve indexed listings clear the 150-install threshold and appear in the table above, so there is no tail to summarise. One row needs a caveat: `kidoc` is indexed with 167 installs but has no matching directory in the current `skills/` tree, which carries eleven `SKILL.md` files, so the twelve listing names do not map one to one onto eleven directories.

## Why This Matters for Hermes Agents

Design review is a task where the value comes from computation rather than prose. An agent that says "check your decoupling" adds nothing; an agent that reports five rails and thirty-four capacitors totalling 132 microfarads on the motor rail and 10.8 microfarads on the 3.3 volt rail has given a reviewer something to argue with. KiCad Happy is built to produce the second kind of answer, and the README's published example report shows the shape: tables of computed values, named components, and flags.

The connector audit is the clearest illustration of what an agent with project access can do that a checklist cannot. It enumerated nineteen connectors, reported ESD clamp status per connector, flagged the six-pin header, motor outputs, servo connectors and sensor port as unprotected, and then reported that all nineteen have coverage gaps. That is a finding, not a suggestion, and it came from reading the schematic.

Computed values also catch a class of bug that review prose misses. A feedback divider with a ratio of 0.155 setting a buck output to 3.87 volts, and a crystal load capacitance of 14 picofarads against an 18 picofarad target, are arithmetic claims that can be checked against the datasheet and against the intended design. Whether the tool is right is testable, which is not true of general design advice.

The certification suggestion step is where it stops being a linter. Detecting USB, switching regulators and external connectors and concluding that unintentional radiator rules and EMC directive compliance apply is the beginning of a compliance conversation, not a compliance decision, and the guide should be read that way.

The sourcing skills extend the loop to the order. Having a BOM with MPNs assigned, a distributor price, and a fabrication house check attached to the same review means the gap between "the design is good" and "the boards are on order" is covered by one workflow instead of three browser tabs.

## Usage

| You say | What happens |
|---|---|
| "Analyze my KiCad project at hardware/rev2" | Parses the schematic and layout, builds the power tree, identifies subcircuits and reports findings across the review sections |
| "Check the ESD protection on every connector" | Walks the connectors, reports clamp status per connector and lists the exposed ones |
| "Does my decoupling look adequate" | Totals capacitance per rail, counts capacitors and flags rails that fall short |
| "Compute the cutoff for my RC filters" | Reads resistor and capacitor values from the schematic and reports the cutoff frequency for each network it finds |
| "Which certifications do I need for this board" | Suggests applicable regimes from what it detects in the design, such as FCC Part 15 and CISPR 32 |
| "Check this BOM against the board" | Compares the BOM to the schematic, reports missing MPNs and BOM lock status |
| "Is this board ready for JLCPCB" | Runs the fabrication house checks for that service and lists what still has to be resolved |

## Verification

The skill files sit at `skills/<name>/SKILL.md`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/aklofas/kicad-happy/main/skills/kicad/SKILL.md | head -6
```

It should open with YAML frontmatter naming the skill and describing its trigger. The practical verification is a real project, and the README's own example is the template: point the agent at a KiCad directory and ask for the analysis, then check that the power tree it produces matches the regulators you know are on the board.

```text
Analyze my KiCad project at hardware/rev2/
```

If the response describes generic design advice with no component references, the parse failed and the skill is running on the model rather than on your files. Confirm the project directory contains the `.kicad_sch` and `.kicad_pcb` files, since the skills read those rather than a rendered PDF.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| kicad | Pass | Warn | Warn |
| jlcpcb | Pass | Pass | Pass |
| bom | Pass | Pass | Warn |
| lcsc | Pass | Pass | Warn |
| spice | Pass | Pass | Pass |
| emc | Pass | Pass | Pass |
| datasheets | Pass | Pass | Pass |
| digikey | Pass | Pass | Pass |
| pcbway | Pass | Pass | Warn |
| mouser | Pass | Pass | Warn |
| element14 | Pass | Pass | Pass |
| kidoc | Pass | Pass | Pass |

Every sampled skill passes the trust-hub check, which is the strongest of the three signals. Five carry a Snyk Warn and the main `kicad` skill also carries a Socket Warn, which is consistent with a skill that ships Python tooling and reaches the network for datasheets and distributor lookups. Read those pages before running the sourcing skills against a corporate network.

The data consideration is different from most skills in this catalog. A KiCad project is intellectual property, and the datasheet and sourcing skills fetch from third-party sites. Treat a design under NDA as you would any file you would not paste into a chat window, and check whether the datasheet retrieval path is acceptable under your agreements before pointing it at a confidential board.

## Limitations

- Snapshot data, verified 2026-11-11: 8,216 combined installs across 12 indexed listings; 1,644 GitHub stars; MIT; last pushed 2026-11-08. Counts drift over time.
- KiCad only. This reads KiCad's file formats, and a design in Altium, Orcad or Eagle has no path through it without an export that preserves connectivity and component data.
- Index and tree do not fully reconcile. Twelve listing names against eleven `SKILL.md` directories, with `kidoc` carrying installs but no current skill directory.
- The review is heuristic, not sign-off. Computed values such as a feedback ratio or a filter cutoff are arithmetic and checkable, but the certification suggestions and the coverage-gap flags are starting points for an engineer, not an approval.
- Network access is required for the datasheet and distributor skills. Digi-Key, Mouser, LCSC, Element14, JLCPCB and PCBWay lookups all involve third parties, and offline use loses those paths.
- Python 3.10 or later is required for the tooling in `tools/`, and the plugin path manages that for you while a manual copy does not.
- The README's known-issue note applies. `/plugin update` may not detect new versions in Claude Code, so a stale install can persist until the cache is cleared.

## Related

- [Text to CAD Skills - 3D Model and URDF Setup](/hermes/skills/catalog/text-to-cad-skills-setup)
- [Frames Engineering Skills - Agent Tools Setup](/hermes/skills/catalog/frames-engineering-skills-setup)
- [EvoSkills - Scientific Research Skill Packs Setup](/hermes/skills/catalog/evoskills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the power tree. It is the section that proves the parse worked, because rail voltages computed from feedback dividers cannot be produced without reading the schematic.
- Point it at the project directory, not at a PDF. The skills parse the source files, and a printed schematic gives them nothing to compute from.
- Ask for the connector ESD audit on any board with external interfaces. It is the highest-yield check in the set and the one whose gaps are most often missed by hand review.
- Use the datasheet skill to settle arguments. When a computed value and a datasheet disagree, the disagreement is the finding.
- Run the fabrication check last, after the electrical review. A JLCPCB or PCBWay pass on a board with an unprotected motor output is a false sense of readiness.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
