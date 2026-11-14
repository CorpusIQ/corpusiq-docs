---
title: "Reverse Skill - Security Research Router Pack"
description: "zhaoxuya520/reverse-skill: 65.1K combined installs across 88 listings, a security research skill router for reverse engineering and pentesting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reverse-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "security", "reverse engineering", "pentesting"]
---

# Reverse Skill - Setup Guide

**Source:** [zhaoxuya520/reverse-skill](https://www.skills.sh/zhaoxuya520/reverse-skill) via skills.sh - 65.1K combined installs across 88 indexed listings; first seen Nov 14, 2026
**GitHub:** 44,635 stars, MIT license, `main` branch, last pushed 2026-11-14, 89 `SKILL.md` files in `skills/<name>/` folders plus a `plugins/reverse-skill/` adapter
**Category:** Reverse engineering, authorized penetration testing and security research skills
**Quality Tier:** 🟠 Orange - security research tooling with multiple Fail verdicts in the sampled set; needs an isolated environment and authorization.

Reverse Skill is a security research skill router: when an agent meets an APK, a binary, frontend JavaScript encryption, a CTF challenge or a pentest target, it routes to the right methodology and toolchain instead of guessing commands. The routing core is driven by one configuration (`skills/config/routing.json`, 44 routes R0-R45), validated by a 200-case regression benchmark on Windows and Ubuntu, and kept client-neutral so Claude Code, Codex, Cursor, Cline and OpenCode all load the same ladder.

Treat it as offensive-security tooling, and read the verdicts before anything else. The sampled set on skills.sh is mixed: pentest-tools, reverse-engineering, reverse-skill-router and ida-reverse fail the Gen Agent Trust Hub, and pentest-tools and reverse-skill-router also fail Socket. The README restricts use to systems you own or are explicitly authorized to assess, and the workflow gates every engagement on a scope file before any target action. Run the skills in an isolated environment, not in a production agent with arbitrary tool access.

## Installation

The README installs the repository as a whole-repo clone, then refreshes the local tool index:

```bash
git clone https://github.com/zhaoxuya520/reverse-skill.git
bash skills/scripts/refresh-tool-index.sh
```

On Windows use `powershell -File skills/scripts/refresh-tool-index.ps1`; on Kali use `bash kali/scripts/refresh-tool-index.sh`. An all-in-one Docker option is documented as `docker compose -f docker/docker-compose.yml run --rm reverse-skill`. Prerequisites per the README are Java/JDK, Node.js 22.12+, Python 3.x and a compatible AI client. The README does not document a per-skill `npx skills add` command; the 88 skills are indexed on skills.sh but install as the whole repo.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pentest-tools | 2,210 | Active pentest toolchain: recon, port and vuln scanning, web pentest, SQL injection, directory brute force, password cracking, 20+ tools surfaced through pentestMCP and mcp-security-hub. |
| reverse-engineering | 2,080 | Reverse engineering techniques for understanding compiled, obfuscated binaries. |
| apk-reverse | 1,871 | Android APK reverse in the CLI: unpacking, Java decompile, smali edits, repackaging, Frida hooking, and so/native analysis. |
| reverse-skill-router | 1,732 | Routes the reverse-skill repository from Codex for authorized reverse engineering, security analysis, and CTF. |
| ghidra-reverse | 1,659 | Free/open reverse engineering with Ghidra headless or GUI: decompile, cross-references, and scripting. |
| ida-reverse | 1,621 | IDA Pro reverse analysis for PE/ELF/APK/DLL/SO binaries, password recovery, vuln and malware analysis, and firmware. |
| radare2 | 1,531 | Analyze binaries with radare2/r2 from the command line. |
| binary-diff | 1,468 | Cross-version symbol migration and binary diffing: move old-version symbols and reverse results to new versions. |
| firmware-pentest | 1,460 | Firmware and IoT pentest chain from a .bin/.img: reverse, extract, emulate, exploit, following OWASP FSTM stages with a binwalk toolchain. |
| dotnet-reverse | 1,449 | .NET/C# binary reverse for assemblies, C# output including NativeAOT, and red-team Sharp* tools. |
| js-reverse | 1,448 | Frontend JavaScript reverse via js-reverse-mcp: signature-chain location, page forensics, runtime sampling, and local environment replay. |
| mobile-reverse | 1,447 | Authorized Android and iOS reverse engineering and security testing, including APK and IPA analysis. |
| diagram-generator | 1,436 | Generate, refine, validate, and render diagrams from natural language, notes, code, schemas, and tables. |
| edr-bypass-re | 1,419 | Reverse EDR/Defender/AV hooks, ETW providers, and AMSI to write targeted unhook, indirect syscall, and ETW bypasses. |
| patch-diff-exploit | 1,414 | N-day patch diffing to exploitation: reverse vuln points from vendor patches, write PoCs, and build attack modules. |
| pwn-chain | 1,408 | Full-chain engineering from reversing a binary to a stable, working exploit. |

The remaining 72 indexed listings range from 83 to 1,369 installs.

## Why This Matters for Hermes Agents

The routing core is the point. Reverse Skill turns a vague "analyze this APK" into a routed pipeline: RULES.md, then the master route, then a case init that gates on authorization and scope before any target action, then the scenario skill and its toolchain. An agent gets a repeatable methodology instead of guessing between jadx, apktool, Frida, IDA and BurpSuite.

The coverage is broad. The 88 listings span APK, ELF, JavaScript and PCAP reverse engineering, malware analysis, firmware and IoT, patch diffing, exploit development, and a 42-skill CTF sandbox. The tree holds 89 `SKILL.md` files, so the index and the repository nearly align.

The authorization gate matters most for agent safety. The workflow requires a scope file with authorization and a network profile before it acts on a target, and the README's disclaimer restricts use to owned or explicitly authorized systems. That is the right default for an agent that could otherwise act on arbitrary targets.

The trade-off is the verdict mix. Several sampled skills fail skills.sh's Gen Agent Trust Hub, so a Hermes agent should treat this as a toolchain to run isolated and reviewed rather than drop into a production agent.

## Usage

| You say | What happens |
|---|---|
| "Analyze this APK" | Routes to apk-reverse for unpacking, decompile, smali edits, repackaging and Frida hooking. |
| "Reverse this ELF binary" | Routes to ida-reverse or radare2 for decompile, cross-references and symbol recovery. |
| "What is this malware doing?" | Routes to malware-analysis for static, dynamic and behavioral analysis with IOC extraction. |
| "Diff this patch for the CVE" | Runs patch-diff-exploit to reverse the vuln point and draft a PoC. |
| "Set up a CTF challenge" | Hands off to CTF-Sandbox-Orchestrator, which dispatches one of 42 sub-skills. |
| "Review this case evidence" | Runs case-review for scope readiness and Evidence to Finding to Path traceability. |
| "Are we authorized for this target?" | The case-init gate requires scope.md with authorization and a network profile before any target action. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/zhaoxuya520/reverse-skill/main/skills/pentest-tools/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zhaoxuya520/reverse-skill/main/skills/reverse-engineering/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zhaoxuya520/reverse-skill/main/plugins/reverse-skill/skills/reverse-skill-router/SKILL.md
```

Most skills live at `skills/<name>/SKILL.md`; the router is the exception at `plugins/reverse-skill/skills/reverse-skill-router/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pentest-tools | Fail | Fail | Pass |
| reverse-engineering | Fail | Warn | Pass |
| apk-reverse | Pass | Fail | Warn |
| reverse-skill-router | Fail | Fail | Pass |
| ghidra-reverse | Pass | Warn | Pass |
| ida-reverse | Fail | Warn | Pass |

Four of the six sampled skills fail the Gen Agent Trust Hub (pentest-tools, reverse-engineering, reverse-skill-router and ida-reverse), and three fail Socket (pentest-tools, apk-reverse and reverse-skill-router). Only ghidra-reverse passes all three auditors. The sample covers 6 of the 88 indexed listings, so it says little about the remaining 82. The repo is MIT-licensed but bundles a GPLv3 CTF-Sandbox-Orchestrator submodule and invokes third-party tools (jadx, frida, nmap, burpsuite-mcp) under their own licenses; the skill-level verdicts do not cover those artifacts.

## Limitations

- Snapshot data, verified 2026-11-14: 65,070 combined installs across 88 indexed listings; 44,635 GitHub stars; MIT; last pushed 2026-11-14. Counts drift over time.
- Four of six sampled skills fail the Gen Agent Trust Hub, and the sample covers only 6 of 88 listings; the rest publish no verdict on skills.sh.
- This is offensive-security tooling: the README restricts use to systems you own or are explicitly authorized to assess, and the skills should run in an isolated environment.
- The CTF-Sandbox-Orchestrator submodule is GPLv3, not MIT, and the bundled third-party tools ship under their own licenses.
- Several Use For cells are condensed translations of Chinese-language SKILL.md frontmatter, not verbatim English descriptions.
- The tree holds 89 `SKILL.md` files across 88 indexed listings; the extra file is the master `skills/SKILL.md` routing entry point.

## Related

- [Cybersecurity Skills - 42 Audit and Pentest Skills](/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup)
- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the routing self-test after any routing or config change: the README ships a 200-case regression benchmark that fails CI on mismatch.
- Gate every engagement with case-init first: it creates scope.md with authorization and a network profile before any target action.
- Treat the Fail-verdict skills (pentest-tools, reverse-skill-router, ida-reverse) as isolated-environment tooling, never as drop-in production skills.
- Use `skills/MASTER-ROUTING.md` as the PRIMARY fast ladder when you only want the routing core without client adapters.
- Keep the tool index current: run refresh-tool-index after installing or moving tools, then check `skills/tool-index.md`.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
