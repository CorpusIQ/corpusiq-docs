---
title: "Embedded Skills - Firmware and Debugger Setup"
description: "zhinkgit/embeddedskills: 8.2K combined installs, 12 Chinese-language skills for Keil and GCC builds, J-Link and OpenOCD flashing, serial, CAN and SSH"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/embeddedskills-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "embedded", "firmware", "debugging", "can bus"]
---

# Embedded Skills - Setup Guide

**Source:** [zhinkgit/embeddedskills](https://www.skills.sh/zhinkgit/embeddedskills) via skills.sh - 8.2K combined installs across 12 indexed listings (8,222 exact); first seen Apr 15, 2026 (Nov 10, 2026 sweep)
**GitHub:** 793 stars, MIT license, `main` branch, last pushed 2026-10-20, 12 `SKILL.md` files among 185 blobs, one flat directory per skill at the repository root (`keil/`, `jlink/`, `serial/`, `workflow/` and the rest) with no nested plugin layout
**Category:** Embedded systems: firmware toolchains, debug probes, CAN and serial buses, RTOS workflows
**Quality Tier:** 🟠 Experimental - the ssh skill fails Gen Agent Trust Hub, five other listings carry Socket or Snyk warnings, and every SKILL.md is written in Chinese.

Embedded work has a loop that general coding agents cannot close on their own: change the code, build it, flash it, watch what the hardware does, read the error, repeat. This repository exists to hand that loop to the agent. Each skill is a folder of Python scripts that wrap a real vendor tool (UV4.exe for Keil MDK, cmake with arm-none-eabi-gcc, JLink.exe, openocd, probe-rs, tshark) and expose the tool as structured subcommands, plus a `SKILL.md` that tells the agent which subcommand answers which request. There are 12 skills, 8,222 combined installs on skills.sh, 793 GitHub stars, and first listings dated Apr 15, 2026.

The language fact needs stating at the top. All 12 `SKILL.md` files, including the frontmatter descriptions and the trigger phrases, are written in Chinese. The subcommand names, flags and JSON keys are ASCII, so an agent that does not read Chinese will still run `jlink flash` correctly, but it will be reading mixed-language prose and its automatic trigger matching depends on phrases a non-Chinese user is unlikely to type.

The 12 listings divide into four jobs. Build skills drive a project: `keil` for MDK projects, `gcc` for CMake projects, `eide` for EIDE projects. Flash and debug skills drive hardware: `jlink`, `openocd` and `probe-rs`. Bus skills talk to the device and the network: `serial`, `can`, `net`, plus `ssh` and `terminal` for remote and interactive sessions. `workflow` sits above them and chains build, flash, debug and observe into one run.

## Installation

The README's primary route is the Skills CLI. `-g` installs globally and `-y` skips the prompt:

```bash
npx skills add https://github.com/zhinkgit/embeddedskills -g -y

# one skill only
npx skills add https://github.com/zhinkgit/embeddedskills --skill jlink -g -y

# manage the install
npx skills ls -g
npx skills update -g
npx skills remove -g
```

The clone route keeps the whole set under one directory:

```bash
# global
git clone https://github.com/zhinkgit/embeddedskills ~/.claude/skills/embeddedskills

# current project only
git clone https://github.com/zhinkgit/embeddedskills .claude/skills/embeddedskills
```

The two routes produce different layouts: the clone keeps all 12 folders under a single `embeddedskills` parent, while `npx skills add` installs from the repository's skill index. Check which shape your agent's skill loader scans before you pick one.

Nothing is bundled. The skills wrap binaries that must already be on the machine, and the README's support matrix names what they expect: Keil MDK and CMake build systems; J-Link (SEGGER) and CMSIS-DAP or DAPLink probes; OpenOCD and probe-rs flashing frameworks; UART, CAN and CAN-FD, and Ethernet for buses. The build systems and probe frameworks combine freely, and the README states that all six pairings work out of the box.

Configuration follows the three-layer setup the README documents, with CLI arguments above all of it and each file overriding the next: `skill/config.json` carries tool paths and hardware parameters, `.embeddedskills/config.json` carries the target chip, interface and log directory, and `.embeddedskills/state.json` holds the last build, flash and debug record. Set the tool paths once in the second layer so a missing `JLink.exe` on the PATH does not surface as a confusing subcommand failure.

## What It Provides

Eleven of the 12 indexed listings clear the 500-install threshold and appear below with their exact counts:

| Skill | Installs | Use For |
|---|---|---|
| keil | 903 | Scans Keil MDK `.uvprojx` projects, enumerates targets, runs build, rebuild and clean, and returns artifact paths the flashing skills can reuse. |
| serial | 848 | Scans serial ports, monitors output in real time, sends data, records logs and shows hex. |
| can | 753 | Scans CAN and CAN-FD interfaces, monitors frames, sends test frames, decodes DBC databases and reports bus statistics. |
| jlink | 713 | Finds probes, flashes firmware, reads and writes memory and registers, resets the target, pulls RTT and SWO logs and runs GDB sessions. |
| openocd | 708 | Probe discovery, firmware flash, flash erase, GDB server, Telnet control, semihosting and ITM capture. |
| gcc | 697 | Scans CMake projects, lists presets, configures, builds with arm-none-eabi-gcc, rebuilds, cleans and reports ELF size. |
| workflow | 691 | Thin orchestration layer: finds projects, picks build, flash, debug and observe backends, and chains them through `.embeddedskills/state.json`. |
| net | 665 | Interface discovery, packet capture, pcap and pcapng analysis, port scans, connectivity tests and traffic statistics through tshark. |
| probe-rs | 661 | probe-rs probe discovery, flashing, reset, memory access, GDB server and RTT logs. |
| ssh | 549 | Runs commands on remote hosts through Host aliases in `~/.ssh/config`, with upload, download, jump host and tunnel operations. |
| terminal | 542 | Two-way interactive sessions for serial ports, SSH shells and local shells that keep context between commands. |

The remaining 1 indexed listing is eide (492 installs), EIDE project scan, config enumeration, build and size analysis.

The table is also the dependency map. `keil`, `gcc` and `eide` produce the artifact; `jlink`, `openocd` and `probe-rs` consume it; `workflow` is the only skill that calls the others rather than a vendor binary. The bus skills (`serial`, `can`, `net`) observe the device instead of writing to it, which makes them the safest place to start on unfamiliar hardware.

## Why This Matters for Hermes Agents

The reason to install these rather than let an agent improvise is the output shape. Every script returns the same JSON envelope: `status`, `action`, `summary`, `details`, `artifacts` and `next_actions`. An agent can branch on `status` and read the hex path out of `artifacts` instead of scraping a human-oriented build log or guessing at `output.hex`. That is the difference between a run that stops when the compile fails and a run that retries with the reported error.

The second reason is state continuity. `.embeddedskills/state.json` records the last build, flash and debug operation, so `workflow` can hand the artifact from the build step to the flash step without the operator restating the path. In a multi-turn session that removes the most common embedded agent failure: flashing the previous build after a compile that silently did not run.

The third is coverage of the actual debugging surface. `jlink`, `openocd` and `probe-rs` expose registers, memory, reset, breakpoints, call stacks and RTT or SWO logs as subcommands, which means an agent asked "why did it hang after reset" can halt the core and read the fault registers itself rather than asking a human to copy output out of an IDE.

Two limits are worth internalising before you wire this into an autonomous loop. These commands act on physical hardware: a flash or erase has no dry run and no undo, and a wrong target in `.embeddedskills/config.json` writes to the wrong chip. And the Chinese skill bodies mean the agent's reasoning about when to use a skill is weaker than its ability to execute one, so name the skill in the prompt when the task matters.

## Usage

| You say | What happens |
|---|---|
| "Build the Keil project and tell me what broke" | The keil skill scans the `.uvprojx`, enumerates targets, builds and parses the log into errors and warnings under `details`. |
| "Flash it with J-Link and show me the RTT output" | The build artifact path from the previous step feeds jlink flash, then jlink rtt streams the target log. |
| "Build and flash in one go" | workflow runs its `build-flash` chain, selecting the build and flash backends and carrying the artifact through state.json. |
| "Watch the serial console while I send AT commands" | terminal opens an interactive session, then sends and reads in sequence so the reply is captured in context. |
| "Decode this CAN capture" | can decodes the log against a DBC file and reports bus statistics alongside the decoded frames. |
| "The board goes silent after reset, find out why" | jlink halts the core and reads registers and memory, or openocd exposes the same through its Telnet session. |
| "Capture what the device sends to our server" | net captures on the interface and analyzes the pcap; ssh covers the server side if the traffic terminates on a remote host. |

## Verification

Every listing resolves to a raw `SKILL.md` at the repository root, one directory per skill on `main`. This request returns 200 and is the file to read before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/zhinkgit/embeddedskills/main/jlink/SKILL.md | head -8
```

The frontmatter opens with `name: jlink` and a folded description whose first line names the J-Link download and online debugging tool, followed by the subcommand documentation in the body. The same path pattern holds for the others, for example `can/SKILL.md` and `workflow/SKILL.md`.

After an install, confirm the Skill CLI sees the set:

```bash
npx skills ls -g
```

For the clone route, confirm the folder landed with its `SKILL.md` intact:

```bash
test -f ~/.claude/skills/embeddedskills/jlink/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| keil | Pass | Pass | Pass |
| serial | Pass | Warn | Pass |
| can | Pass | Pass | Warn |
| jlink | Pass | Warn | Pass |
| openocd | Pass | Warn | Pass |
| gcc | Pass | Pass | Pass |
| workflow | Pass | Pass | Pass |
| net | Pass | Pass | Warn |
| probe-rs | Pass | Pass | Pass |
| ssh | Fail | Pass | Pass |
| terminal | Pass | Pass | Pass |

The ssh listing is the one that fails a scanner, and it fails on Gen Agent Trust Hub, which is the verdict that scores whether the skill can be trusted with what it claims to do. That matters more here than a Snyk warning would, because the skill's stated job is running commands on remote hosts through `~/.ssh/config` aliases. Approve its calls the way you would approve a shell command on a production server.

The warns cluster on the skills that touch raw hardware and packet data: Socket warns on `serial`, `jlink` and `openocd`, which drive vendor binaries and open device ports, and Snyk warns on `can` and `net`, which send frames and capture traffic. None of these is a red flag on its own, but they are all skills with side effects outside the repository, so review the script that runs before you let an unattended loop call them. Verdicts exist only for the 11 listings in the table; `eide` was not in the sampled set.

The scanner verdicts score the skill files, not the firmware you flash or the commands an agent composes from them. A pass means the instructions are not obviously malicious, not that the resulting operation is safe on your board.

## Limitations

- Snapshot data, verified 2026-11-10: 8,222 combined installs across 12 indexed listings; 793 GitHub stars; MIT license; last pushed 2026-10-20. Counts drift over time.
- All 12 `SKILL.md` files and their frontmatter descriptions are written in Chinese. An English-speaking agent can follow the subcommands and the JSON fields, but it reads mixed-language prose, and its automatic skill selection relies on Chinese trigger phrases.
- Nothing is vendored. Keil MDK, arm-none-eabi-gcc with CMake and Ninja, the SEGGER J-Link software, OpenOCD, probe-rs and tshark all have to be installed separately, and a missing one shows up as a failed subcommand rather than a setup error.
- The Keil backend drives UV4.exe, which is Windows-only tooling, so a Linux host can use the gcc, probe-rs and bus skills but not the keil path.
- The ssh listing fails Gen Agent Trust Hub. Treat remote execution through it as a reviewed action rather than an autonomous one.
- Flash and erase commands act on connected hardware with no dry run. A wrong chip or interface setting in `.embeddedskills/config.json` writes to the wrong device.

## Related

- [Terminal Skills - System Administration Pack Setup](/hermes/skills/catalog/terminal-skills-setup)
- [CMUX Skills - Agent Terminal Multiplexer Setup](/hermes/skills/catalog/cmux-skills-setup)
- [Herdr Skills - Terminal Workspace Orchestration Setup](/hermes/skills/catalog/herdr-skills-setup)

## Pro Tips

- Read `jlink/SKILL.md` or `serial/SKILL.md` before installing the set. The subcommand table at the top of each file is the entire API, and it is faster to read than to discover through failed calls.
- Set `.embeddedskills/config.json` first, with the target chip, interface and log directory. Every build, flash and debug call inherits it, so one wrong line is cheaper to fix there than in a prompt.
- Install `workflow` only after the leaf skills work. It composes the others, so a broken `openocd` path fails twice when reached through the orchestration layer.
- Read `artifacts.hex` from the JSON rather than hard-coding an output path. The path moves between Keil, GCC and EIDE projects, and the field is the only thing that tracks it.
- Pin the skill directory in the prompt when the task matters (`/jlink flash`), because the Chinese trigger phrases will not fire on an English request.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
