---
title: "Allium Skills - Specification Language Setup"
description: "juxt/allium - 17.9K combined installs: a specification language and skill set that keeps specs, tests, and code in agreement."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/juxt-allium-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "specification", "bdd", "testing"]
---

# Allium Skills - Setup Guide

**Source:** [juxt/allium](https://www.skills.sh/juxt/allium) via skills.sh - 17.9K combined installs across 7 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [juxt/allium](https://github.com/juxt/allium) - 544 stars, MIT license, last pushed Nov 19, 2026, main branch; 7 skill folders under skills/<name>/SKILL.md plus 5 autonomous agents under agents/<name>.md.
**Category:** Specification / Behavior-Driven Development (Agent Skills)
**Quality Tier:** 🟡 Yellow - 7 of 7 listings sampled: one carries a Warning and six pass all three checks; no Fails.

juxt/allium is a behavioural specification language and skill set that "talks back": an agent maintains a .allium specification alongside the code, capturing what the system should do in a form that persists across sessions. Six skills plus the /allium router drive a loop - elicit works forward from intent, distill works backward from existing code, tend edits the spec, weed reconciles spec and code, propagate generates tests, and witness independently certifies convergence.

The language is purely descriptive (no compiler or runtime) but pairs with a separate CLI that validates syntax and draws semantic inferences, catching data-flow and lifecycle problems language models miss. All 7 indexed listings map to the current tree, and tend and weed also ship as autonomous agents for Claude Code and Copilot. MIT-licensed and measured at 544 GitHub stars.

## Installation

Install the Allium CLI first (optional but recommended, via Homebrew or crates.io):

```bash
brew tap juxt/allium && brew install allium
```

```bash
cargo install allium-cli
```

Then install the skills. Claude Code via the JUXT plugin marketplace:

```bash
/plugin marketplace add juxt/claude-plugins
/plugin install allium
```

Codex via the JUXT plugin marketplace:

```bash
codex plugin marketplace add juxt/claude-plugins
codex plugin add allium@juxt-plugins
```

Cursor, Windsurf, Aider, Continue, and other skills-compatible tools:

```bash
npx skills add juxt/allium
```

GitHub Copilot reads skills and agents from the repository automatically; no installation needed.

## What It Provides

skills.sh publishes per-skill install counts for all 7 indexed listings. The 6 most-installed skills are listed below; the remaining 1 is summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| allium | 3,745 | entry point that drives the whole loop to convergence, routing to the right skill |
| elicit | 2,777 | structured discovery session to build a spec from intent through conversation |
| propagate | 2,751 | generate tests from a spec, including property-based and state machine tests |
| distill | 2,749 | extract an Allium spec from an existing codebase |
| tend | 2,736 | targeted edits to specs as requirements change, pushing back on vague requests |
| weed | 2,719 | find and fix divergences between spec and code |

The remaining 1 indexed listing is witness (412 installs), which independently verifies that a loop's convergence claim is true and was reached honestly.

## Why This Matters for Hermes Agents

For agentic coding, the verification phase is what decides quality, and Allium supplies the two things loops most often lack: a verification signal at the level of behaviour and context that does not drift between sessions. The .allium spec persists, so meaning carries across sessions instead of being re-read from code each time, directly addressing the context-drift failure a long Hermes session hits by prompt ten or twenty. Because behaviour is written as structure rather than prose, contradictions (two rules with incompatible preconditions) surface on their own instead of requiring a powerful model to notice them. The propagate skill turns the spec into tests, and the witness skill gives CI a trustworthy convergence signal by checking that no generated test was weakened. For a builder running Hermes agents on real repos, this means green means behaviour is right, not just that unit tests pass.

## Usage

| You say | What happens |
|---|---|
| Add gift cards to checkout | Uses elicit to build the spec, propagate to generate tests, then weed to reconcile |
| Extract a spec from this existing codebase | Uses distill to reverse-engineer behaviour into an Allium specification |
| Generate tests for this spec | Uses propagate to turn the spec into tests |
| Update the spec for this new requirement | Uses tend to make targeted edits as requirements change |
| Check whether code still matches the spec | Uses weed to find spec-code divergences and reconcile them |
| Verify this loop actually converged | Uses witness to independently certify the convergence claim |

## Verification

Confirm the README and the entry-point skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/juxt/allium/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/juxt/allium/main/skills/allium/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warning noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| allium | Pass | Pass | Warn |
| elicit | Pass | Pass | Pass |
| propagate | Pass | Pass | Pass |
| distill | Pass | Pass | Pass |
| tend | Pass | Pass | Pass |
| weed | Pass | Pass | Pass |
| witness | Pass | Pass | Pass |

All 7 listings were sampled; one carries a Warning (allium, on Snyk) and six pass all three checks, with no Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 17,889 combined installs across 7 indexed listings; 544 GitHub stars; MIT license; last pushed Nov 19, 2026. Counts drift over time.
- Allium has no compiler and no runtime; it is purely descriptive, defined entirely by its documentation, so enforcement relies on the CLI's structural checks and the agent's diligence.
- The Allium CLI lives in a separate repository (juxt/allium-tools); the skills run without it but fall back to the language reference with no formal checks.
- The allium-lsp language server is not bundled with the Claude Code plugin; install it separately and place the binary on PATH or Claude Code reports Executable not found in $PATH.
- Only the Claude Code plugin wires every layer (skills, autonomous agents, auto-verification, and LSP); other harnesses get a subset and need git hooks or manual allium check runs.

## Related

[Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup) | [Specsfy Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/specsfy-setup) | [Walden - Spec-Driven Development with Executable Proofs](/hermes/skills/catalog/walden-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the Allium CLI so every spec edit is formally checked; the skills fall back to the language reference without it.
- Use the spec-first loop (elicit, propagate, implement, weed) for new features and distill for existing code.
- Confirm generated tests fail first; a generated test that is already green is either already covered or vacuous.
- Wire allium check into a pre-commit hook or edit hook for harnesses that lack live verification.
- Use witness to gate CI on a trustworthy convergence signal rather than a self-reported green.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
