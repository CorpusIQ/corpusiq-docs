---
title: "Waza - Engineering Habit Skills for Coding Agents"
description: "Tw93 Waza: 120.1K combined installs. Eight engineering habit skills for planning, debugging, review, UI and prose, driven from one dispatcher."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/waza-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-25"
tags: ["hermes skill", "agent skill", "skill setup", "engineering habits", "code review", "debugging"]
---

# Waza - Setup Guide

**Source:** [tw93/waza](https://www.skills.sh/tw93/waza) via skills.sh - 120.1K combined installs across 11 indexed listings; new to this catalog in the Oct 25, 2026 morning sweep

**GitHub:** [tw93/Waza](https://github.com/tw93/Waza) - 7,356 stars, MIT, last pushed 2026-10-25, branch main, eight skill directories under `skills/` mirrored under `plugins/waza/skills/` for the host plugin, plus four optional rule files under `rules/`

**Category:** Agent Workflow / Engineering Discipline

**Quality Tier:** 🟡 Beta - one author's deliberate, widely installed engineering discipline suite with permissive licensing, held back from production tier by two Gen Agent Trust Hub failures on credential handling and install scripts

Waza is Tw93's answer to a narrow question: which engineering habits make an agent's output usable, and what does each one look like as an instruction set. The repository ships eight skills, one per habit, and nothing else. There is no framework, no plugin runtime to learn and no opinion about which model you use.

The design decision worth understanding is restraint. Every skill states the outcome, the red lines and how the result gets verified, then stops. It does not script the model's path through the task. The author's argument is that a model improves faster than a prompt tree does, so a skill that describes a destination ages better than one that describes every step. The collection was built from real projects and refined through 300 or more sessions across seven of them.

The skills chain by intent rather than by configuration. You plan with `think`, implement, then review with `check`. You debug with `hunt`, fix, then `check` again. You fetch with `read`, synthesize with `learn`, polish with `write`. Nothing forces a workflow; the habits are separate so you can install the two you need.

## Installation

The README's recommended path installs into the shared `~/.agents/skills` directory, which Claude Code symlinks into and which Codex, Cursor, Gemini CLI, Copilot, Amp and other hosts read directly:

```bash
npx skills add tw93/Waza -a claude-code codex cursor -g -y
```

Update an installed copy with:

```bash
npx skills update -g -y
```

If you prefer the host's own package manager, the repository is also a plugin marketplace, which namespaces the skills as `/waza:check` and so on:

```text
/plugin marketplace add tw93/Waza
/plugin install waza@waza
```

```bash
codex plugin marketplace add tw93/Waza
codex plugin add waza@waza
```

For Claude Desktop, download `waza.zip` from the latest release, open Customize then Skills, create a skill and upload the ZIP. For Pi, `pi install npm:@tw93/waza`.

The four optional rules are separate from the skills and only apply when you paste one into your agent's persistent instructions. They are installed by `setup-rule.sh` from the latest release: `english` for a short correction when a prompt contains a mistake, `anti-patterns` for always-on guardrails against scope creep, `waza-routing` so non-Claude hosts prefer these skills when a request matches their triggers, and `clarity` for consistent terms and explicit conditions. Read the script before running it; the README says to review it first and shows you how.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| health | 18,538 | Auditing an agent's own setup: instruction drift, hooks and MCP wiring, verifier output, AI maintainability, and whether the host is quietly ignoring its instructions. |
| check | 15,820 | Reviewing a diff or pull request against project constraints, running the verification the repository defines, and handling an approved release, publish or push. |
| write | 15,346 | Rewriting prose in English or Chinese, technical instructions, product copy, release notes and launch posts, and cutting AI tone out of a draft. |
| think | 14,982 | Turning a rough idea into a decision-complete plan before code: pressure-testing the problem, judging whether to build at all, and writing a handoff another agent can execute. |
| hunt | 14,913 | Debugging to root cause before any fix, especially regressions and anything that used to work, including defects reported as a screenshot. |
| read | 14,064 | Fetching a URL or PDF and returning a summary or clean Markdown for quoting, citing, converting or saving, with a proxy and DeepSeek search fallback when built-in fetching is thin. |
| learn | 13,183 | A six-phase research workflow from source bundle to publishable output: collect, digest, outline, fill in, refine, and self-review. |
| design | 8,721 | Design work as a routed intent; indexed listing with no directory under `skills/` in the current tree. |
| ui | 4,264 | Building or restyling a page, component or type system, including screenshot-grounded aesthetic iteration on something that looks wrong. |

The remaining 2 indexed listings sit below the threshold: waza (208 installs), the dispatcher entry that routes an unprompted request to the right skill, and english (12 installs), the optional correction rule described above.

## Why This Matters for Hermes Agents

Most agent failures on real work are not capability failures. The model can write the code, run the command and read the documentation. What it skips is the work around the work: confirming the requirement before building, finding the root cause before patching, reviewing its own diff before declaring the task complete, and reading the primary source instead of paraphrasing from memory.

Those four habits are exactly what this repository encodes, one skill per habit, each with the failure that produced it written down. For a Hermes agent that runs unattended for long stretches, the highest value is in the pairing: `hunt` refuses to fix anything before naming a cause, and `check` refuses to call a change finished before running the project's own verification command. That combination is the difference between a session that ends with a tested change and one that ends with a confident report and a broken build.

The second reason is portability. Because every skill is a plain `SKILL.md` under a shared directory, the same discipline loads in Claude Code, Codex, Cursor and a Hermes profile without a second copy. Teams that run more than one agent host get one behaviour instead of several.

The caveat is not about the habits, it is about two of the implementations. `think` instructs the agent to open the project's config file, explicitly including `.env`, and lift live values into the plan, and it asks for every API key and token the plan requires. `check` runs the verification commands it discovers in the repository. Both are defensible in a trusted single-developer repository and both need a policy in a shared one. Read the Security section before you install this on a host that holds production credentials.

## Usage

| You say | What happens |
|---|---|
| "Should we build this at all, and if so how" | think challenges the requirement, prices the alternative of not building it, and returns a plan complete enough for another agent to implement. |
| "This used to work and now it does not" | hunt reproduces the regression, isolates the boundary that changed, and states a confirmed cause before proposing a patch. |
| "Review this before I merge" | check reads the project's own constraints and verification commands, reviews the diff against them, and reports what it actually ran. |
| "Ship it and close the issue" | check handles the release path it was authorised for: publish, push, and maintainer follow-through on the issue. |
| "Read this paper and give me the Markdown" | read fetches the PDF and returns clean Markdown, falling back to a proxy or a search backend if direct fetching fails. |
| "Research this market and give me one reference document" | learn runs the six phases and returns a single compiled document with its sources. |
| "This draft sounds like a machine wrote it" | write rewrites the prose in the author's register and removes formulaic phrasing, in English or Chinese. |
| "My agent keeps ignoring its own instructions" | health audits the configuration, instruction files, hooks and MCP wiring, and names the drift rather than the symptom. |

## Verification

Confirm the layout on main before installing; every in-tree skill uses `skills/<name>/SKILL.md`:

```bash
for s in think check hunt read; do
  curl -sL -o /dev/null -w "%{http_code} skills/$s/SKILL.md\n" \
    "https://raw.githubusercontent.com/tw93/Waza/main/skills/$s/SKILL.md"
done
```

Read the two skills that touch credentials and commands before you enable them:

- https://raw.githubusercontent.com/tw93/Waza/main/skills/think/SKILL.md
- https://raw.githubusercontent.com/tw93/Waza/main/skills/check/references/project-context.md

After install, the skills appear as one folder per skill in your agent's skills directory, and in Claude Code as `/think`, `/check`, `/hunt` and the rest. The `skills` CLI prompts before writing unless you pass `-y`, so a first install without `-y` is a safe way to see what the index resolves. The rule installers write into your instructions, so diff them before use.

## Security

skills.sh verdicts for sampled skills (verified October 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| health | Pass | Pass | Pass |
| check | Pass | Pass | Warn |
| write | Pass | Pass | Pass |
| think | Fail | Pass | Pass |
| hunt | Pass | Pass | Pass |
| read | Pass | Pass | Warn |
| learn | Pass | Pass | Warn |
| ui | Warn | Pass | Pass |
| design | Warn | Pass | Pass |
| waza | Fail | Warn | Warn |
| english | Pass | Pass | Pass |

Two failures need to be read, not skimmed.

`think` fails Gen Agent Trust Hub on `CREDENTIALS_UNSAFE` and `INDIRECT_PROMPT_INJECTION`. The evidence is a step that opens the project's actual config file, naming `.env` as an example, and lifts the live value into the plan, plus a requirement to list every API key, token and third-party account the plan needs. In a repository you own, that is a legitimate planning input. In a repository with production secrets, it is a credential read dressed as planning.

`waza`, the dispatcher entry, fails on `REMOTE_CODE_EXECUTION`, `DATA_EXFILTRATION`, `EXTERNAL_DOWNLOADS` and `COMMAND_EXECUTION`: the release scripts are fetched and piped to a shell, `health/scripts/collect-data.sh` reads `~/.claude/settings.local.json` and session logs, the read skill routes URLs through third-party proxies `defuddle.md` and `r.jina.ai`, and the check skill executes any test command it detects in the project. None of that is hidden, and the README tells you to review the scripts first. All of it still deserves a decision rather than a default.

Snyk records `W011` third-party content exposure on `check`, `read` and `learn`, which is structural: the skills intentionally ingest diff comments, web pages and source bundles. `read` also carries `W012` for its proxy and search endpoints as unverifiable runtime dependencies.

The practical posture: install the skills you need, keep the optional rules reviewed rather than auto-applied, exclude `.env` by policy if the host has production credentials, and point the read skill at providers you trust.

## Limitations

- Snapshot data, verified October 25, 2026: 120,051 combined installs across 11 indexed listings; 7,356 GitHub stars; MIT; last pushed 2026-10-25. Counts drift over time.
- The install index outruns the tree by three listings. `design` has no directory under `skills/`, and `waza` and `english` resolve to the dispatcher and the optional rule rather than standalone skills, which is why their rows read as they do.
- The README markets the collection against larger frameworks on size. Eight skills is the whole product, so if you need domain knowledge rather than working discipline, this repository has none.
- `think` reads project config by instruction and `check` executes discovered test commands. Both are the intended behaviour and both are what the auditors flagged.
- The rule installers pull a script from the latest release and run it. Their behaviour is reviewed only when you review them.
- Skill descriptions and trigger phrases are heavily bilingual (Chinese and English), which raises a prompt-matching surface on hosts that do not route on intent.

## Related

- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Ponytail Skills - Lazy Senior Dev Coding Setup](/hermes/skills/catalog/ponytail-skills-setup)
- [Masseater Skills - Engineering Judgment Suite](/hermes/skills/catalog/masseater-skills-setup)
- [Ultracite - Zero-Config Lint Preset Setup](/hermes/skills/catalog/ultracite-skills-setup)

## Pro Tips

- Install `hunt` and `check` first. Root-cause discipline and a review gate cover most of the real failure modes, and they are the two skills that survive a change of coding stack.
- Keep the optional rules out until a session shows you need one. They run on every turn, not only when a skill is invoked.
- Put an explicit `.env` exclusion in your project instructions before enabling `think` on anything that holds real credentials. The skill's own instruction is to read the value.
- Pair `check` with the repository's CI command rather than replacing it. The skill runs what the project defines; it does not define the project's standard.
- When a session ends with a green report and a red build, the missing habit is almost always `check`. Make it the last call rather than an optional one.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
