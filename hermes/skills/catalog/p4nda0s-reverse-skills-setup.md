---
title: "Reverse Engineering Skills - Frida and IDA Setup"
description: "P4nda0s/reverse-skills: 14.7K combined installs. Eight skills for Frida hooking, IDA symbol and struct recovery, DEX and IL2CPP dumps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/p4nda0s-reverse-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "reverse engineering", "frida", "ida", "malware analysis"]
---

# Reverse Engineering Skills - Setup Guide

**Source:** [P4nda0s/reverse-skills](https://www.skills.sh/P4nda0s/reverse-skills) via skills.sh - 14.7K combined installs across 8 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) - 2,344 stars, no license file in the repository, branch main, last pushed 2026-05-06; 8 folders under `skills/`, seven holding an uppercase `SKILL.md` and one (`rev-ios-dump`) holding a lowercase `skill.md`, plus a 1.7 MB `panda-dex-dumper` binary inside `rev-dex-dumper/`

**Category:** Binary reverse engineering for agents: Frida instrumentation, IDA and IDAPython symbol and structure recovery, Android DEX unpacking, Unity IL2CPP, Unicorn emulation

**Quality Tier:** 🟡 Yellow - two of the three sampled listings carry an auditor Warn, the repository has no license file, and one skill ships a prebuilt binary that gets pushed to a target device

This is an eight-skill reverse engineering suite from P4nda0s, the author of IDA-NO-MCP. The README is written in Chinese with an English mirror at `README_EN.md`, and it states the suite supports 40+ AI coding agents and is designed to work with IDA-NO-MCP: export the decompilation from IDA, then let the coding agent analyse it. There is no build step, no test suite and no server. The whole artifact is eight folders of Markdown, roughly 2,000 lines in total, of which `rev-idapython` is the largest at 799 lines, followed by `rev-frida` at 351, `rev-symbol` at 211, `rev-struct` at 200, `rev-u3d-dump` at 172, `rev-ios-dump` at 168, `rev-unicorn-debug` at 74 and `rev-dex-dumper` at 71.

The analysis skills share a contract, and it is the most interesting part of the design. Each one opens with a pre-check that looks for a connected IDA Pro MCP server first, then for a `decompile/` directory of `.c` files named by hex address, and if neither exists it stops and prints a two-option prompt telling the user to either connect the MCP server or install IDA-NO-MCP and export with Ctrl-Shift-E. The agent is told what its input looks like before it is allowed to guess, which is unusual in a space where most prompts assume the model can see a disassembler.

## Installation

The README documents the skills.sh CLI, and that is the shortest path:

```bash
npx skills add P4nda0s/reverse-skills
```

The same README documents the maintenance commands, which are worth having on hand because the suite changes per skill rather than as a monolith:

```bash
npx skills check
npx skills update
npx skills remove rev-symbol rev-struct
```

The manual route copies the eight folders. Note the trailing `/.` on the source and the mixed-case filename in `rev-ios-dump`, because both matter on a case-sensitive filesystem:

```bash
git clone --depth 1 https://github.com/P4nda0s/reverse-skills.git /tmp/reverse-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills/reverse-skills
cp -R /tmp/reverse-skills/skills/. ~/.hermes/profiles/corpusiq/skills/reverse-skills/
```

Nothing is installed by the skill itself. What the skills drive lives outside the repository: IDA Pro plus the optional IDA Pro MCP server, ADB and a rooted or debuggable Android target for `rev-dex-dumper`, a jailbroken device with `frida-ios-dump` for `rev-ios-dump`, and the Unicorn Python package for `rev-unicorn-debug`. Frida itself is a host install plus a `frida-server` on the target.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rev-frida | 2,215 | Writing Frida hook scripts against the modern API: module and export lookup with `Process.getModuleByName`, native and ObjC and Java method interception, argument and return value capture, memory and export dumping, and loader-aware instrumentation for Android. The skill also corrects a common stale habit: the modern CLI has no `--no-pause`, because a spawned process resumes once the script loads. |
| rev-struct | 1,928 | Reconstructing C structure definitions from memory access patterns across a function and its call chain, including field offsets, guessed field widths and the cross-references that justify each field. |
| rev-symbol | 1,911 | Recovering function names by correlating code patterns, string references, constants and cross-references, either from the export tables or from decompiled bodies, so `sub_401000` becomes a claim with evidence behind it. |
| rev-idapython | 1,911 | IDAPython and IDALib script reference: headless analysis without the GUI, IDB database operations, memory and register access, function and basic block and instruction traversal, Hex-Rays decompiler API calls, obfuscation helpers and batch processing across binaries. |
| rev-dex-dumper | 1,880 | Unpacking Android apps by pushing the bundled `panda-dex-dumper` to the device with ADB, dumping DEX from live process memory and pulling the decrypted files back, which is the workflow that defeats class-loading packers. |
| rev-unicorn-debug | 1,832 | Emulating one function or fragment in the Unicorn engine instead of running the whole binary: loading the file raw, mapping only the segments that matter, and hooking libc, JNI and syscalls with Python stubs so a decryption routine can run without its environment. |
| rev-u3d-dump | 1,820 | Extracting C# method names, addresses and type information from Unity IL2CPP builds by pairing the native binary with `global-metadata.dat`, then generating IDA or Ghidra import scripts so the recovered names land in the database. |
| rev-ios-dump | 1,172 | Decrypting App Store binaries on a jailbroken device with `frida-ios-dump` to get a decrypted Mach-O or IPA that static tools can open. This is the skill that ships as `skill.md` in lowercase. |

All 8 indexed listings clear the threshold and appear in the table above.

The eight skills are procedural manuals rather than reference dumps. `rev-frida` gives the working CLI invocations and then the API surface, `rev-unicorn-debug` states five core principles before any code (load the file raw, identify context dependencies, use callbacks, iterate on crashes, keep trace output minimal), and `rev-struct` documents the export layout it expects: one `.c` file per function, named by hexadecimal address, plus the tables IDA-NO-MCP writes alongside them.

## Why This Matters for Hermes Agents

Reverse engineering is the task category where an agent's confident wrong answer costs the most, because a plausible Frida script that hooks the wrong offset, or a Frida script that still passes `--no-pause`, fails silently on a device that is already spawned. `rev-frida` corrects the flag, names the modern API, and shows the loader timing problem for Android native modules, which is exactly the class of detail that training data from older Frida releases gets wrong.

Symbol and structure recovery is worse, because there is no compiler to complain. An agent asked "what does this function do" will invent a name from a string it half-reads. `rev-symbol` makes the answer evidence-based by requiring code patterns, constants and cross-references to agree before a name is proposed, and `rev-struct` does the same for field offsets across the call chain rather than a single function body.

The pre-check matters more than it looks. By insisting on either a live MCP connection or an exported `decompile/` tree, the skills convert an open-ended question into a bounded one, and an agent that cannot satisfy the pre-check stops instead of fabricating an analysis from the function name alone. That is the behaviour you want on a task where the source of truth is a binary.

Two design details are worth flagging to a builder. `rev-dex-dumper` ships a 1.7 MB prebuilt binary rather than source, which is what the Socket Warn on `rev-frida` sits next to in spirit and what makes the copy step heavier than a Markdown clone. And `rev-ios-dump` uses a lowercase `skill.md`, so on Linux a loader that looks for `SKILL.md` will not see the eighth skill at all, while the skills.sh listing still counts it.

## Usage

| You say | What happens |
|---|---|
| "Hook this Java method and log the arguments" | `rev-frida` writes the modern-API script, spawns with `frida -U -f <package> -l hook.js` and notes that the process resumes on load without `--no-pause`. |
| "This function is called sub_401000, what is it?" | `rev-symbol` reads the function body, its string references, constants and cross-references, then proposes a name with the evidence that supports it. |
| "What structure is passed into this function?" | `rev-struct` walks the access patterns across the caller and callee, emits a C struct with offsets and flags fields it could not resolve. |
| "Write an IDAPython script to rename every function" | `rev-idapython` switches to the IDALib headless path when the database is not open in the GUI, then writes the traversal and rename loop. |
| "Unpack this Android app so I can read the DEX" | `rev-dex-dumper` pushes `panda-dex-dumper` to `/data/local/tmp/`, dumps the running process memory and pulls the decrypted DEX files. |
| "Dump the C# names from this Unity build" | `rev-u3d-dump` pairs `libil2cpp.so` or `UnityFramework` with `global-metadata.dat` and writes the IDA or Ghidra import script. |
| "Run this decrypt routine without the app" | `rev-unicorn-debug` loads the binary raw into Unicorn, hooks JNI, libc and syscalls with Python stubs and traces at block level. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/P4nda0s/reverse-skills/main/skills/rev-frida/SKILL.md
```

After a clone, the count is the check that matters, because the repository mixes the two filename cases:

```bash
git clone --depth 1 https://github.com/P4nda0s/reverse-skills.git /tmp/reverse-skills
find /tmp/reverse-skills/skills -name SKILL.md | wc -l
ls /tmp/reverse-skills/skills/rev-ios-dump
head -3 /tmp/reverse-skills/skills/rev-frida/SKILL.md
```

The first command prints 7, the second shows `skill.md` in lowercase, and `head` shows `name: rev-frida` plus the description the runtime routes on. Confirm the installed copy:

```bash
find ~/.hermes/profiles/corpusiq/skills/reverse-skills -name SKILL.md | wc -l
ls ~/.hermes/profiles/corpusiq/skills/reverse-skills/rev-dex-dumper
```

If you want all eight skills routable, rename `rev-ios-dump/skill.md` to `SKILL.md` in the installed copy and the count becomes 8.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rev-frida | Pass | Warn | Pass |
| rev-struct | Pass | Pass | Pass |
| rev-symbol | Pass | Pass | Warn |

The Warns are unsurprising for this category. `rev-frida` is a script generator for runtime instrumentation, and generated hook scripts run inside another process with that process's privileges. `rev-symbol` carries a Snyk Warn, and its output is advisory text that you should treat as a hypothesis rather than a fact. Neither verdict is a Fail, and `rev-struct` passes all three.

There is no license file in the repository even though the README's license section says MIT. Public and indexed is not the same as licensed, so if you intend to mirror or republish the skill text rather than install it into a profile, you have no explicit grant.

Two operational points matter more than the badges. The suite contains exactly one executable artifact, the 1.7 MB `panda-dex-dumper` binary in `rev-dex-dumper/`, which the skill tells you to `adb push` to a device and `chmod +x`. It is a prebuilt binary with no source in the repository, so read it or hash it before it goes onto hardware you care about. Everything else is Markdown, and nothing runs when a skill is loaded.

## Limitations

- Snapshot data, verified 2026-11-02: 14,669 combined installs across 8 indexed listings; 2,344 GitHub stars; no license file; last pushed 2026-05-06. Counts drift over time.
- No license file exists despite the README declaring MIT, so there is no explicit grant to reuse the text even though it is publicly indexed.
- `rev-ios-dump` ships as `skill.md` in lowercase, so a case-sensitive loader sees seven skills where the index counts eight.
- The skills.sh listing for `rev-ios-dump` repeats the `rev-dex-dumper` description word for word ("Dump DEX files from a running Android app"), which describes Android unpacking rather than iOS decryption. The in-repo frontmatter is correct, so trust the file over the listing.
- The analysis skills assume an input you may not have: either a live IDA Pro MCP connection or an IDA-NO-MCP export tree with one `.c` file per function. Without one of those, six of the eight skills stop at their pre-check.
- Last push was 2026-05-06, and Frida's API moves quickly. Verify `rev-frida` snippets against the installed Frida version before running them, and treat the version claims in the text as dated.
- The README is Chinese-first with an English mirror, so the English documentation is the secondary copy and can lag the primary one.

## Related

- [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup)
- [Setup Guide: cantinaxyz/clawdstrike - Agent Red-Team Security Testing (486 Installs)](/hermes/skills/catalog/clawdstrike-setup)
- [Metamask Openclaw Security Analysis Setup](/hermes/skills/catalog/metamask-openclaw-security-analysis-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the pre-check conversation first. If the `decompile/` tree does not exist, the agent will offer to walk you through the IDA-NO-MCP export, and letting it do that is faster than arguing with a skill that has already decided it has no input.
- Ask for the evidence alongside the name. `rev-symbol` is instructed to justify a name with strings, constants and cross-references, so "which strings told you that" is a cheap way to catch a guess presented as a finding.
- Give `rev-struct` the call chain, not one function. Field recovery works by watching the same offset get read and written in different callers, and a single body rarely pins a layout.
- Use IDALib for anything loop-shaped. `rev-idapython` documents headless execution, which is the difference between scripting a rename pass over 400 functions and clicking through them.
- Check the filename case before you debug a missing skill. If only seven of eight skills load, the answer is almost certainly `rev-ios-dump/skill.md`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
