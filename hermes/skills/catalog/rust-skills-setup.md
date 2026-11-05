---
title: "Rust Skills - 265 Rules Across 26 Categories"
description: "leonardomso/rust-skills on skills.sh: 6.8K combined installs across 1 listing; 265 Rust rules in 26 categories for writing and review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rust-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "rust", "code review", "best practices"]
---

# Rust Skills - Setup Guide

**Source:** [leonardomso/rust-skills](https://www.skills.sh/leonardomso/rust-skills) via skills.sh - 6.8K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 670 stars, MIT licence, last pushed 2026-06-14, one SKILL.md at the repository root with a rules/ directory beside it
**Category:** Rust engineering standards: ownership, error handling, async, unsafe, API design, performance and testing
**Quality Tier:** 🟢 Production - every sampled audit Pass; MIT; 670 stars.

Rust Skills is a single skill holding 265 rules across 26 categories, current for Rust 1.96 and the 2024 edition. It targets the shape of code agents default to: cloning to dodge the borrow checker, unwrapping everywhere, reaching for `Box<dyn Trait>` where `impl Trait` would do. Each rule states why it matters, shows a bad example, shows a good example, and links related rules and sources.

The design is built for low token cost. `SKILL.md` is a lightweight index, every rule reduced to a one-line summary grouped by category with a link to its file. The `rules/` directory holds one markdown file per rule, named `<prefix>-<name>.md`, and the prefixes (`own-`, `err-`, `unsafe-`, `async-`, `mem-`, `anti-`) map directly to categories, so a review of async code pulls the async, concurrency and ownership files and leaves the rest alone.

## Installation

The README installs with the `add-skill` CLI, which detects the agents on the machine and places the skill for each:

```bash
npx add-skill leonardomso/rust-skills
```

For Claude Code the README's manual route is a clone, globally or per project:

```bash
git clone https://github.com/leonardomso/rust-skills.git ~/.claude/skills/rust-skills
```

```bash
git clone https://github.com/leonardomso/rust-skills.git .claude/skills/rust-skills
```

Single-file harnesses take the index directly. Cursor, for example, can use the whole skill directory or just the SKILL.md as a rules file:

```bash
curl -o .cursorrules https://raw.githubusercontent.com/leonardomso/rust-skills/master/SKILL.md
```

Codex and Zed use the AGENTS.md standard the same way, and the repository's `CLAUDE.md` and `AGENTS.md` are symlinks to `SKILL.md`, so all three conventions resolve to one file. Note the branch: this repository uses `master`, and every raw URL above depends on it.

## What It Provides

One listing, far above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| rust-skills | 6,765 | Reviewing, writing and refactoring Rust against 265 rules, loaded by prefix so only the relevant categories enter context |

No indexed listings fall below the 500-install threshold; the single listing appears above.

## Why This Matters for Hermes Agents

An agent writing Rust without guidance produces code that compiles and is still wrong: a `&String` parameter where `&str` would do, a `clone()` on every path to silence the borrow checker, an `unwrap()` in library code, a `Box<dyn Trait>` where a generic would inline. The README's own example is the pattern in miniature. Given a function that clones a string, splits it and unwraps the first word, the rules turn it into a signature that borrows and returns an `Option`, citing own-slice-over-vec, own-borrow-over-clone and anti-unwrap-abuse by name.

The rule catalogue is what makes the advice checkable rather than stylistic. Memory has 17 rules, async 18, API design 17, testing 15, anti-patterns 15, and each one is a file an agent can cite instead of an opinion it invented.

Progressive disclosure is the part that makes it usable in a real context window. The agent reads the index, picks the prefixes the code in front of it needs, and opens a handful of rule files. That keeps a 265 rule corpus from becoming a 265 rule prompt.

It also gives a Hermes agent something to be graded against. A review that says "rule async-cancel-safety is violated" is auditable in a way that "this looks non-idiomatic" is not, and the bad and good examples in each file show the fix rather than describing it.

## Usage

| You say | What happens |
|---|---|
| "/rust-skills review this function" | The agent loads the relevant rule files and reviews the code against them |
| "/rust-skills is my error handling idiomatic?" | Applies the error handling rules: thiserror for libraries, anyhow for applications, the question mark operator |
| "/rust-skills check for memory issues" | Pulls the memory rules: SmallVec, arenas, avoiding allocations, `mem::take`, drop order |
| "/rust-skills is this unsafe block sound?" | Applies the unsafe rules: SAFETY comments, Miri, MaybeUninit, 2024 edition unsafe |
| "Why is this cloning so much?" | Ownership and borrowing rules find the unnecessary clones and the signature that removes them |
| "Review this tokio task for cancel safety" | Async rules cover channels, async fn in traits and cancellation |
| "Set up clippy and CI for this crate" | Linting rules cover clippy configuration, CI setup and unexpected_cfgs |

## Verification

Confirm the index the installer pulls:

```bash
curl -fsSL https://raw.githubusercontent.com/leonardomso/rust-skills/master/SKILL.md | head -5
```

It should open with `name: rust-skills` and a description naming 265 rules across 26 categories. Then confirm the rule corpus landed beside it and that the count matches the claim:

```bash
ls ~/.claude/skills/rust-skills
ls ~/.claude/skills/rust-skills/rules | wc -l
```

The first command should list `SKILL.md`, `CLAUDE.md`, `AGENTS.md` and `rules/`; the second should print 265. A smaller number means a partial clone or a copy that took only the index file.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rust-skills | Pass | Pass | Pass |

Everything this skill installs is markdown. There are no scripts to execute, no hooks and no network calls in the rule corpus, which is why the audit surface is small.

## Limitations

- Snapshot data, verified 2026-11-05: 6,765 combined installs across 1 indexed listing; 670 GitHub stars; MIT; last pushed 2026-06-14. Counts drift over time.
- The default branch is `master`, not `main`. Every raw URL in the README and in this guide depends on it, so a future rename breaks the single-file installs.
- The README's how-it-works section says the agent avoids loading "all 218" rules while the badges, the category table and the `rules/` directory all count 265. The directory holds 265 files, so treat 265 as current and 218 as stale prose.
- The rules target Rust 1.96 and the 2024 edition. Some of them assume edition features that older toolchains do not have, so a legacy crate will collect advice it cannot apply.
- It is one skill with one index. The context stays small only while the agent follows the read-the-index-then-open-files pattern; pasting the whole `rules/` directory into a prompt defeats the design.
- The install CLI is `add-skill`, not the `skills` CLI most other repositories in this catalog document. Check which binary your harness has before scripting an install.

## Related

- [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)
- [Apollo GraphQL Skills - GraphQL and Rust Setup](/hermes/skills/catalog/apollographql-skills-setup)
- [Cargo Skills - GTM Engineering Suite for Agents Setup](/hermes/skills/catalog/cargo-skills-setup)

## Pro Tips

- Scope the request by prefix. Asking for an async review loads far fewer rules than asking for a general review, and the narrower answer is usually the more useful one.
- Run it on new code before review, not after. The rules are cheaper as a writing constraint than as a rework list.
- Cite the rule name in your own review comments. The rule files carry a stable identifier, which makes a disagreement about style resolvable by reading one file.
- Keep `rules/` out of the prompt and in the filesystem. The index is the interface; the files are the reference.
- Pair it with a compiler and clippy pass. The rules cover design and idiom, and neither replaces the borrow checker or a lint run.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
