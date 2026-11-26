---
title: "Beautiful Rust - Idiomatic Rust Skills Setup"
description: "morganlinton/beautifulrust - 3.8K combined installs: three Rust skills to write, review, and port idiomatic Rust, plus a tested clippy config."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/beautifulrust-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "rust", "clippy", "code review"]
---

# Beautiful Rust - Setup Guide

**Source:** [morganlinton/beautifulrust](https://www.skills.sh/morganlinton/beautifulrust) via skills.sh - 3.8K combined installs across 3 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [morganlinton/BeautifulRust](https://github.com/morganlinton/BeautifulRust) - 2,143 stars, MIT license, last pushed Nov 8, 2026, main branch; three skills under skills/<name>/SKILL.md plus a lints/ clippy config.
**Category:** Rust Engineering
**Quality Tier:** 🟢 Green - all 3 listings sampled and every cell is Pass.

Beautiful Rust teaches a coding agent to write, review, and port idiomatic Rust, and backs the guidance with a tested clippy configuration. The three skills are rust-best-practices (writing), rust-review (critiquing existing code), and rust-port (moving C, C++, Python, Go, or JavaScript into idiomatic Rust). Each skill ships eval cases in the layout Claude Code's plugin evaluator reads, and every code example compiles on stable Rust.

The lints/ directory is a drop-in clippy config that enforces the machine-checkable rules in CI, with a check crate containing one deliberate violation per lint to prove each lint fires. All 3 indexed listings have a matching skills/<name>/SKILL.md in the current tree on the main branch.

## Installation

The skills installer supports most agents (Node 22.20 or later):

```bash
npx skills add morganlinton/BeautifulRust
```

Add -g for a user-level install or -a <agent> to target one agent. Claude Code installs it as a plugin:

```bash
claude plugin install beautiful-rust --marketplace morganlinton/BeautifulRust
```

Codex, Copilot, and Gemini CLI installs are documented in the README, and Cursor or anything else can copy the three folders into the agent's skills directory. The clippy config is separate: copy lints/clippy.toml next to your Cargo.toml and paste the [lints] block from lints/lints.toml into it, then deny warnings in CI:

```bash
cargo clippy --all-targets --all-features \
  -D warnings
```

## What It Provides

skills.sh publishes per-skill install counts for all 3 indexed listings.

| Skill | Installs | Use For |
|---|---|---|
| rust-best-practices | 1,374 | write idiomatic, robust, maintainable Rust, triggered on any Rust code: new crates, modules, traits, error types, async, unsafe, or FFI |
| rust-review | 1,296 | review existing Rust code for idiom, API design, error handling, and safety, producing a prioritized report that cites the rule and shows a fix |
| rust-port | 1,091 | port C, C++, Python, Go, JavaScript, or TypeScript into idiomatic Rust, porting the tests first to prove behavior matches |

All 3 indexed listings clear the 1,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Rust's borrow checker and API conventions punish an agent that writes working-but-unidiomatic code, and this skill set turns style guidance into something an agent can apply deterministically. rust-best-practices synthesizes the Google Rust Style Guide, the Rust API Guidelines, Effective Rust, Rust Design Patterns, and Microsoft's Pragmatic Rust Guidelines into one digest, and where the sources disagree it picks a side and says why, so the agent is not stuck arbitrating. rust-review makes every finding cite the rule it breaks and show the smallest fix, which produces reviews a human can act on rather than vibes. rust-port maps each source language's habits to Rust equivalents, so a port keeps semantics instead of transliterating. The clippy config then enforces the machine-checkable subset in CI, which is what keeps the rules from slipping back after the agent hands the code off.

## Usage

| You say | What happens |
|---|---|
| Write a Rust crate for this | Uses rust-best-practices for idioms, error types, API design, and a pre-handback checklist |
| Review my Rust code | Uses rust-review to run fmt, clippy, and tests, then write a three-tier report with cited fixes |
| Port this Python service to Rust | Uses rust-port to port the tests first, design a Rust API, and verify with cargo test and clippy |
| Add clippy enforcement to CI | Uses lints/clippy.toml and lints/lints.toml to deny the machine-checkable rules |
| Check this Bevy code | Uses the bevy reference so general Rust advice does not break Bevy conventions |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/morganlinton/BeautifulRust/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/morganlinton/BeautifulRust/main/skills/rust-best-practices/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/morganlinton/BeautifulRust/main/skills/rust-review/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/morganlinton/BeautifulRust/main/skills/rust-port/SKILL.md | head -40
```

All four URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rust-best-practices | Pass | Pass | Pass |
| rust-review | Pass | Pass | Pass |
| rust-port | Pass | Pass | Pass |

Across the 3 sampled skills there are 9 Pass, 0 Warn, and 0 Fail cells; all three listings pass all three checks.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,761 combined installs across 3 indexed listings; 2,143 GitHub stars; MIT license; last pushed Nov 8, 2026. Counts drift over time.
- The repo name is BeautifulRust (capital B and R); skills.sh indexes it as morganlinton/beautifulrust, and the README install commands use the BeautifulRust casing.
- The skills are guidance plus evals, not enforced constraints; the clippy config is what enforces the machine-checkable rules in CI.
- The eval cases are real model runs and are billed; running claude plugin eval consumes model credits.
- The reference digests are paraphrased summaries of their five sources; read the originals for the full reasoning.

## Related

[Rust Skills - 265 Rules Across 26 Categories](/hermes/skills/catalog/rust-skills-setup) | [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup) | [Rust Skills - Rust Engineering Skills](/hermes/skills/catalog/full-stack-skills-rust-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all three skills together; rust-review and rust-port lean on rust-best-practices for target-code style.
- Run lints/check with scripts/check-lints.sh to prove every lint in the table still fires after a clippy upgrade.
- For Bevy crates, read skills/rust-best-practices/references/bevy.md first; several general rules are wrong for Bevy systems.
- Add the four Bevy-specific allows when a crate depends on bevy or bevy_ecs, or clippy flags every idiomatic system signature.
- Set rust-version = "1.81" or later in Cargo.toml for the allow_attributes lints, which need #[expect] support.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
