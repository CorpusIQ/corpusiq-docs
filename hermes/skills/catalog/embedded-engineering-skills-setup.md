---
title: "Embedded Engineering Skills - Arduino Maker Setup"
description: "wedsamuel1230/embedded-engineering-skills - 4.7K combined installs: Arduino and embedded skills for code generation, debugging, and maker workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/embedded-engineering-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "arduino", "embedded systems", "maker"]
---

# Embedded Engineering Skills - Setup Guide

**Source:** [wedsamuel1230/embedded-engineering-skills](https://www.skills.sh/wedsamuel1230/embedded-engineering-skills) via skills.sh - 4.7K combined installs across 43 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [wedsamuel1230/embedded-engineering-skills](https://github.com/wedsamuel1230/embedded-engineering-skills) - 35 stars, MIT license, last pushed Oct 15, 2026, main branch; 43 skill directories under skills/<name>/SKILL.md plus three repo tooling skills under .agents/skills/ and thin adapters for Codex, Claude Code, and Cursor.
**Category:** Embedded Systems (Arduino / Maker Tools)
**Quality Tier:** 🟡 Yellow - 15 sampled skills: arduino-project-builder (Socket) and datasheet-interpreter (Snyk) carry Warnings; the other 13 sampled skills pass all three checks.

wedsamuel1230/embedded-engineering-skills publishes Arduino and embedded-systems skills plus maker tools, packaged for the Agent Skills format. The 43 indexed listings span code generation, hardware debugging, serial monitoring, power planning, BOM and enclosure work, and board support, all toolchain-neutral across Arduino IDE, Arduino CLI, PlatformIO, and vendor tools. Each skill is a folder with a SKILL.md plus scripts/ (Python tools with PEP 723 inline dependencies), references/, and assets/, loaded by progressive disclosure: name and description first, then the full SKILL.md, then references and scripts only when needed.

The README frames the suite around explicit multi-framework routing, board-aware Arduino skills, and physical-world evidence gates that keep build, upload, hardware, system, and deployment proof separate. The skills.sh index lists 43 listings, matching the 43 skill directories in the current tree; the repository also ships three repo tooling skills under .agents/skills/ (cli-creator, plugin-creator, skill-creator) that have no indexed listing.

## Installation

The quick path installs the whole collection through the Agent Skills CLI:

```bash
npx skills add wedsamuel1230/embedded-engineering-skills
```

The repository keeps one shared skills/ directory of truth with thin adapters per host: Codex (codex plugin marketplace add /path/to/embedded-engineering-skills, then codex plugin add embedded-engineering-skills@embedded-engineering-skills), Claude Code (claude --plugin-dir /path/to/embedded-engineering-skills), and Cursor (install the repository as a plugin). Manual setup clones and copies the skills directory:

```bash
git clone --branch codex/universal-embedded-skills https://github.com/wedsamuel1230/embedded-engineering-skills.git
cd embedded-engineering-skills
mkdir -p ~/.codex/skills
cp -r skills/* ~/.codex/skills/
```

## What It Provides

skills.sh publishes per-skill install counts for all 43 indexed listings. The 16 most-installed skills are listed below; the remaining 27 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| arduino-project-builder | 618 | complete Arduino/embedded projects across Arduino IDE, CLI, PlatformIO, and vendor toolchains |
| arduino-code-generator | 480 | Arduino and embedded C++ snippets for sensors, buses, state machines, and timing |
| circuit-debugger | 314 | multimeter hardware debugging: power checks, continuity, and signal tracing |
| arduino-serial-monitor | 280 | read and analyze serial output for structured runtime debugging |
| error-message-explainer | 180 | explain compiler, upload, boot, power, and runtime errors in plain English |
| arduino-cli-skill | 180 | Arduino CLI commands for board discovery, library install, compile, upload, and serial troubleshooting |
| enclosure-designer | 166 | 3D-printable enclosures with measurements, cutouts, and print settings |
| power-budget-calculator | 152 | total power draw and battery life with sleep-mode and sizing analysis |
| datasheet-interpreter | 150 | extract specs from datasheet PDFs: pins, I2C addresses, timing, register maps |
| bom-generator | 141 | bill of materials with part numbers, quantities, suppliers, and compatibility warnings |
| battery-selector | 140 | battery chemistry, safety, voltage regulation, and charging for Arduino/ESP32/RP2040 |
| code-review-facilitator | 132 | automated code review for best practices, memory safety, and common pitfalls |
| readme-generator | 128 | auto-generate professional README files following open-source best practices |
| sensor-calibration-workbench | 114 | calibration workflows for CO2, load cell, magnetometer, color, and analog sensors |
| i2c-bringup-diagnostician | 110 | diagnose I2C bring-up failures: addresses, pull-ups, and board-family bus quirks |
| wiring-safety-check | 103 | check logic levels, current, pull-ups, drivers, rails, and safe defaults |

The remaining 27 indexed listings range from 28 to 97 installs.

## Why This Matters for Hermes Agents

Embedded work is where agent overconfidence is most costly: a wrong pin assignment, a blocking delay() loop, or an unverified "it compiles" claim all look plausible in text but fail on real hardware. This suite encodes the discipline directly into skills: board-aware code generation, toolchain neutrality, and physical-world evidence gates that require measured output before a claim is accepted. For a builder running Hermes agents on Arduino, ESP32, or RP2040 projects, the router and project-loop skills provide a durable multi-session workflow with rollback and a user-owned physical gate, so an agent does not silently declare success on a broken circuit. The skills separate build, upload, hardware, system, and deployment evidence, and ship Python tools with PEP 723 inline dependencies you can run directly with uv. Adoption is trivial through npx skills, the Codex, Claude Code, and Cursor adapters, or a plain copy into the agent's skills directory. The main caveat is scope: executable support is limited to recorded framework, target, and host fixtures, so a generic family match is not a variant confirmation.

## Usage

| You say | What happens |
|---|---|
| Build me an environmental monitor project | Uses arduino-project-builder to scaffold a project across Arduino IDE, CLI, or PlatformIO |
| Generate I2C scanner code for ESP32 | Uses arduino-code-generator to emit a board-aware I2C snippet |
| My circuit gets hot and stops working | Uses circuit-debugger for multimeter power checks, continuity, and signal tracing |
| What parts do I need for this build | Uses bom-generator to produce a bill of materials with suppliers and warnings |
| What battery should I use | Uses battery-selector for chemistry, safety, and charging guidance |
| My I2C sensor is not detected | Uses i2c-bringup-diagnostician to isolate address, pull-up, and library failures |
| Explain this compiler error | Uses error-message-explainer to separate build, upload, and hardware evidence |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/wedsamuel1230/embedded-engineering-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/wedsamuel1230/embedded-engineering-skills/main/skills/arduino-project-builder/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and run the repo's own validators (scripts/validate_agent_skills.py and siblings) against a checkout.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| arduino-project-builder | Pass | Warn | Pass |
| arduino-code-generator | Pass | Pass | Pass |
| circuit-debugger | Pass | Pass | Pass |
| arduino-serial-monitor | Pass | Pass | Pass |
| error-message-explainer | Pass | Pass | Pass |
| arduino-cli-skill | Pass | Pass | Pass |
| enclosure-designer | Pass | Pass | Pass |
| power-budget-calculator | Pass | Pass | Pass |
| datasheet-interpreter | Pass | Pass | Warn |
| bom-generator | Pass | Pass | Pass |
| battery-selector | Pass | Pass | Pass |
| code-review-facilitator | Pass | Pass | Pass |
| readme-generator | Pass | Pass | Pass |
| sensor-calibration-workbench | Pass | Pass | Pass |
| i2c-bringup-diagnostician | Pass | Pass | Pass |

15 of 43 listings were sampled; two carry a Warning (arduino-project-builder Socket, datasheet-interpreter Snyk) and the rest pass all three checks.

## Limitations

- Snapshot data, verified Nov 25, 2026: 4,678 combined installs across 43 indexed listings; 35 GitHub stars; MIT license; last pushed Oct 15, 2026. Counts drift over time.
- Only 15 of 43 listings were security-sampled; the other 28 carry no sampled verdicts in the index.
- Executable support is scoped to recorded framework, target, and host fixtures; a board profile is documentation support, not proof the current checkout was built or measured on that board.
- The README manual clone command targets the codex/universal-embedded-skills branch, while the skills.sh index and raw URLs resolve on main.
- Version 2.0.0 is marked for review; publication and tags require a separate authorized release.

## Related

[Embedded Skills - Firmware and Debugger Setup](/hermes/skills/catalog/embeddedskills-setup) | [KiCad Happy - Electronics Design Review Skills Setup](/hermes/skills/catalog/kicad-happy-setup) | [Blender Agent Skills - 3D Production Workflows](/hermes/skills/catalog/blender-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- For a complete request, start with arduino-workflow-router; for anything spanning physical hardware or multiple sessions, load embedded-project-loop first.
- Run tool scripts with uv (uv run skills/<name>/scripts/...); they carry PEP 723 inline dependencies.
- Name the exact board, framework, toolchain, pins, voltage, memory, and library versions before asking for code so the generator does not guess.
- Use references/boards/index.json and scripts/resolve_board_profile.py for exact board lookup before assigning pins or making electrical claims.
- Validate a checkout with the repo's own scripts before relying on a release.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
