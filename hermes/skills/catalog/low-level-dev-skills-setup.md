---
title: "Low-Level Dev Skills Setup Guide for Hermes Agents"
description: "mohitmishra786/low-level-dev-skills - 41.5K installs across 142 skills: systems programming guidance for agents - CMake, LLVM, GDB, eBPF, Rust unsafe, assembly, kernel modules, and performance analysis."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/low-level-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "systems", "c", "cpp", "rust", "linux", "debugging", "ebpf"]
---

# Low-Level Dev Skills - Setup Guide

**Source:** [mohitmishra786/low-level-dev-skills](https://skills.sh/mohitmishra786/low-level-dev-skills) (41.5K installs across 142 skills)
**GitHub:** [mohitmishra786/low-level-dev-skills](https://github.com/mohitmishra786/low-level-dev-skills) (188 stars)
**Skills:** 142 skills; top skills: `cmake` (1.4K), `static-analysis` (894), `llvm` (710)
**Category:** Development / Systems & Low-Level
**First Seen:** skills.sh Feb 20, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟡 Trusted - Gen Agent Trust Hub and Socket Pass, but Snyk carries a warning on the top skill (see Security Audit Status)

A 142-skill suite of procedural guidance for low-level and systems programming, packaged for agents. The catalog is genuinely deep: build systems (CMake, Make, Ninja, Meson), compilers and toolchains (GCC, Clang, LLVM, cross-GCC, MSVC), debuggers (GDB, LLDB), dynamic analysis (Valgrind, sanitizers, heaptrack, fuzzing), performance (linux-perf, flamegraphs, CPU cache optimization, PGO, hardware counters), kernel-adjacent work (Linux kernel modules, eBPF, io-uring, AF_XDP, RDMA, DPDK), assembly (x86, ARM), Rust systems work (unsafe, FFI, sanitizers/Miri, cross-compilation, security), plus Zig, wasm, GPU (CUDA, HIP/ROCm, Triton), embedded (FreeRTOS, OpenOCD/JTAG), and language internals (interpreters, compilers, memory model, branch prediction).

The skills follow a uniform shape: purpose, triggers (example questions that should load the skill), and a numbered workflow - the same trigger-driven pattern Hermes skills use. Hot momentum is current: six skills (`rust-cross`, `linux-perf`, `clang`, `compiler-optimizations-deep`, `zig-debugging`, `ebpf-rust`) were on the skills.sh hot leaderboard during the Aug 31 sweep.

---

## Installation

```bash
npx skills add mohitmishra786/low-level-dev-skills
```

Or per-skill:

```bash
npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill cmake
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Native toolchain** | The relevant compiler/build tool for the target skill (gcc, clang, cargo, zig, cmake, etc.) |
| **Linux** | Most debugging and profiling skills assume Linux (perf, eBPF, Valgrind) |
| **Node.js** | Recent LTS for the `npx skills` installer |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| cmake | 1.4K | Modern target-first CMake: out-of-source builds, dependencies, generators, presets, CI/IDE integration |
| static-analysis | 894 | Running and interpreting static analyzers across languages |
| llvm | 710 | LLVM tooling: passes, IR, optimization pipeline |
| gdb | 621 | Interactive and scripted debugging with GDB |
| linux-perf | 517 | Perf profiling, counters, and flamegraph data collection |
| sanitizers | 513 | ASan, TSan, UBSan setup and triage |
| core-dumps | 512 | Core dump analysis and post-mortem debugging |
| clang | 495 | Clang-specific flags, diagnostics, and workflows |
| freertos | 483 | FreeRTOS tasks, scheduling, and embedded patterns |
| linux-kernel-modules | 467 | Building, loading, and debugging kernel modules |
| memory-hierarchy-and-caches | 238 | CPU cache and memory hierarchy optimization (added Sep 29, 2026 sweep) |

Plus `assembly-x86`, `assembly-arm`, `simd-intrinsics`, `cpu-cache-opt`, `memory-model`, `fuzzing`, `valgrind`, `flamegraphs`, `linkers-lto`, `binutils`, `strace-ltrace`, `dynamic-linking`, `ebpf`, `rust-unsafe`, `rust-ffi`, `rust-sanitizers-miri`, `zig-debugging`, `wasm-emscripten`, `cuda-debugging`, `io-uring`, `riscv-privileged`, `llvm-passes`, `mlir`, `dpdk`, `triton-lang`, and 90+ more.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cmake | Pass | Pass | Warn |

Gen Agent Trust Hub and Socket Pass; Snyk carries a warning - the reason this suite ships 🟡 Trusted rather than 🟢 Production.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Worker-node debugging** | The DGX Spark and worker nodes run native binaries, podman, and kernel-adjacent tooling - core dumps, perf, and eBPF skills map directly to that debugging surface |
| **Rust and Zig tooling** | CorpusIQ's Go/Rust/Python CLI tools get systems-level guidance (unsafe audits, FFI, cross-compilation) when performance work arises |
| **Agent-build correctness** | CMake, linkers, and sanitizer skills stop agents from guessing build flags when scaffolding native projects |
| **Infrastructure forensics** | strace-ltrace, flamegraphs, and cpu-cache-opt skills support real diagnosis on degraded nodes |

## Limitations / Verification

- The top skill sits at 1.4K installs with a long tail below 500; the suite's value is breadth and structure rather than any single blockbuster skill.
- Snyk warning is named in the tier above.
- Skills are guidance, not binaries: the agent must have the underlying toolchain installed.

Verification after install:

```bash
npx skills add mohitmishra786/low-level-dev-skills --list    # 142 skills discovered
```

## Related

- [Dart Language Skills Setup](/hermes/skills/catalog/dart-lang-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) - full quality-tiered directory

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
