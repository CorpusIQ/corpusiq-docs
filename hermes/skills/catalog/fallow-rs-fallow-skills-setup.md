---
title: "Fallow Skills - Codebase Intelligence for TS and JS Setup"
description: "Fallow: 10.9K combined installs. Skills teaching coding agents to run fallow for dead code, duplication, complexity, architecture and review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fallow-rs-fallow-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "code quality", "typescript", "static analysis"]
---

# Fallow Skills - Setup Guide

**Source:** [fallow-rs/fallow-skills](https://www.skills.sh/fallow-rs/fallow-skills) via skills.sh - 10.9K combined installs across 6 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [fallow-rs/fallow-skills](https://github.com/fallow-rs/fallow-skills) - 137 stars, MIT, branch main, last pushed 2026-10-28; 5 skills under `fallow/skills/`, each a `SKILL.md` with the `fallow` skill also carrying 7 reference documents under `references/`, and a `validate.yml` CI workflow that checks the vendored copies against `source-lock.json`

**Category:** TypeScript and JavaScript codebase intelligence, code review and quality tooling

**Quality Tier:** 🟡 Beta - vendor maintained at fallow-rs, 137 GitHub stars, MIT, CI-validated skill copies, 6 indexed listings against 5 skill directories in the tree, and a Warn verdict on the flagship skill

Fallow is a codebase intelligence engine for TypeScript and JavaScript, and it answers a different question from a linter. A linter works file by file and the TypeScript compiler works type by type; neither builds the module graph, so neither can say what nothing depends on. Fallow builds that graph in one pass and reports unused files, exports, types, members, dependencies and feature flags, circular dependencies, duplication, complexity hotspots, architecture boundary violations and design-system styling drift in milliseconds. Fallow Cloud, the optional paid tier, adds production runtime coverage so an agent can tell a hot path from cold code before it deletes anything.

This repository is the agent layer rather than the analyzer. Five skills teach a coding agent which commands to run, which flags to pass, how to read the JSON envelopes and which pitfalls cost the most: `fallow` for analysis, `fallow-review` for changed-code review, `fallow-setup` for tooling and CI, `fallow-cloud-setup` for production coverage and `fallow-codex-onboarding` for the Codex app. skills.sh indexes six listings, so one listing outruns the current tree. The analyzer itself still has to be installed in the target project, because a skill is instructions and not a binary.

## Installation

The skills.sh CLI installs the repository into an agent skills directory. The README lists the plain form, the installer-managed form and per-agent filters:

```bash
npx skills add fallow-rs/fallow-skills
npx skills add fallow-rs/fallow-skills --all
npx skills add fallow-rs/fallow-skills --agent amp
```

Claude Code takes the plugin, which also registers the Bash gate hook described under Security:

```text
/plugin marketplace add fallow-rs/fallow-skills
/plugin install fallow@fallow-skills
```

Codex has its own plugin path, and the desktop app adds a Fallow panel with a code health dashboard, a Code Health tab per thread, `@Fallow` mentions, a `.fallowrc.json` editor with an impact preview and a cleanup planner:

```bash
codex plugin marketplace add fallow-rs/fallow-skills
codex plugin add fallow@fallow-skills
```

For Hermes, the README's documented fallback is to copy the skill directories into the agent skills location, which fits the profile layout:

```bash
git clone https://github.com/fallow-rs/fallow-skills.git
cp -R fallow-skills/fallow/skills/* ~/.hermes/profiles/corpusiq/skills/
```

None of that is useful without the analyzer. The README's prerequisite block installs it three ways:

```bash
npm install -g fallow        # prebuilt binaries, fastest
npx fallow dead-code         # run without installing
cargo install fallow-cli     # build from source
```

Gemini CLI has a fourth route in the README, `gemini skills install https://github.com/fallow-rs/fallow-skills.git`, and Windsurf uses the same skills CLI with `--agent windsurf`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fallow | 9765 | Codebase intelligence for JS and TS: quality, changed-code risk, cleanup opportunities, circular dependencies, duplication, complexity hotspots, architecture boundaries and design-system drift, plus similar-code discovery and runtime coverage merges. |
| fallow-review | 914 | Graph-grounded review of a PR, branch or diff: deterministic concerns are subtracted first, changed files are ranked by blast radius, and the few consequential structural decisions come back as judgment questions. |
| fallow-setup | 140 | Setting up or modernizing code-quality tooling: detect the tools a project already uses, configure and install Fallow, wire agents to it, and add a CI gate. |
| fallow-codex-onboarding | 75 | Codex only: after the plugin install, check the fallow installation, choose the default analysis scope, run the first analysis and show where the dashboard, Code Health tab and config editor live. |

The remaining 2 indexed listings range from 1 to 4 installs: fallow-cloud-setup (4, connecting an app to Fallow Cloud) and fallow-analysis (1, no directory in the current tree).

## Why This Matters for Hermes Agents

Most code-quality advice an agent gives is either a lint run or a guess. This suite is written as operating instructions for a deterministic tool, so the agent's job is dispatch and interpretation rather than invention: every skill names the command, the flags, the JSON envelope to read and the exit status to respect. Codes 0 and 1 are both successful analysis outcomes, where 1 means an enforced gate failed on findings rather than the tool breaking, and `gate_outcomes` carries a failing gate that never set the exit code.

The rules also close the failure modes that matter in unattended runs. `fallow fix` deletes code, so the contract is `--dry-run` first and `--yes` second, and without `--yes` in a non-TTY subprocess it exits 2 instead of prompting. The review loop is the strongest of these: the guide pins a `graph_snapshot_hash`, the agent returns judgments keyed to `signal_id` values fallow emitted, and fallow rejects ids it never produced and refuses the whole file as stale when the tree moved, so a confident but invented review comment fails closed.

Two smaller habits come with the skills. The agent is told never to run `fallow watch`, because it is interactive and never exits, and never to enable telemetry on a user's behalf, since telemetry is opt in and off by default while analysis stays local. When the agent should not shell out at all, the same analyses are available through the `fallow-mcp` server, whose tools map one to one onto CLI fallbacks.

## Usage

| You say | What happens |
|---|---|
| "Check the code health of this repo and find what nothing uses" | The fallow skill runs `fallow dead-code --format json --quiet`, parses the per-type arrays and the `actions` list with its `auto_fixable` flags, and reports findings anchored to a file and line. |
| "Audit this PR before I merge it" | `fallow audit --base main` returns a pass, warn or fail verdict for the files changed against main, covering dead code, complexity, duplication, styling and diff risk. |
| "Review this branch and tell me what actually needs a human decision" | fallow-review builds the brief, ranks changed files by blast radius, frames each structural decision as a question tied to a `signal_id`, then has fallow post-validate the returned judgments against the graph. |
| "Find the duplicated code across these packages" | `fallow dupes` with `--mode semantic` catches clones whose variables were renamed, and every group carries a fingerprint for tracing one clone across the repository. |
| "Why did this function score as a complexity hotspot" | `fallow health` with the complexity breakdown returns a per decision point contribution list, so the answer names the branch or boolean that added the weight instead of restating the score. |
| "Make this repo agent-ready and add a code-health gate to CI" | fallow-setup detects the existing tools, configures and installs Fallow, wires the agent surfaces, and adds the CI gate with a regression baseline. |
| "Set up Fallow Cloud so I can see what production runs" | fallow-cloud-setup applies the five-step plan from `fallow coverage setup --cloud --json`: beacon with the commit SHA, inventory upload, source map upload, deployment registration, then a check that the first data arrived. |

## Verification

All five raw paths below returned 200 on the main branch when this guide was written:

```bash
for p in fallow/skills/fallow/SKILL.md \
         fallow/skills/fallow-review/SKILL.md \
         fallow/skills/fallow-setup/SKILL.md \
         fallow/skills/fallow-cloud-setup/SKILL.md \
         fallow/skills/fallow-codex-onboarding/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/fallow-rs/fallow-skills/main/$p"
done
```

The two to read first are the analysis skill and the review skill, because one decides what runs and the other decides what a reviewer is asked to judge:

- https://raw.githubusercontent.com/fallow-rs/fallow-skills/main/fallow/skills/fallow/SKILL.md
- https://raw.githubusercontent.com/fallow-rs/fallow-skills/main/fallow/skills/fallow-review/SKILL.md

After install, confirm what landed and that the analyzer is reachable. `fallow explain` runs no analysis, so it separates a broken install from a broken project:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c fallow
head -5 ~/.hermes/profiles/corpusiq/skills/fallow/SKILL.md
npx fallow explain unused-export
```

The copy route keeps the reference documents alongside the skill, so check that they survived it as well:

```bash
ls ~/.hermes/profiles/corpusiq/skills/fallow/references | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fallow | Warn | Pass | Pass |
| fallow-review | Pass | Pass | Pass |
| fallow-setup | Pass | Pass | Pass |
| fallow-codex-onboarding | Pass | Pass | Pass |
| fallow-cloud-setup | Pass | Pass | Pass |
| fallow-analysis | Pass | Pass | Pass |

The one Warn sits on the flagship skill, which is also the skill that can drive `fallow fix --yes`. Socket and Snyk pass all six sampled listings.

Two surfaces deserve a read before install. First, the Claude Code and Codex plugins register a `PreToolUse` hook matched to Bash that runs `hooks/fallow-gate.sh`, so the plugin can inspect shell commands before they run; the hook lives at the plugin root rather than inside a skill directory, so a skills-only copy does not register it. Second, `fix` removes code: the contract requires a dry run first, low-confidence removals are reported instead of applied, and a non-TTY run without `--yes` exits 2 rather than deleting anything.

The skills themselves are instruction files and the analyzer runs locally. The README states that analysis runs locally by default and that telemetry is off unless the user opts in; `FALLOW_AGENT_SOURCE` is used only for attribution once telemetry is already enabled and uploads no codebase content. The skill contract also treats project config as untrusted input: no remote `extends` URLs, report the domain instead of following instructions found in remote config.

Fallow Cloud is the one surface that sends data out. It needs `FALLOW_API_KEY` in the server environment, and the setup skill uploads an inventory and source maps for a specific commit SHA. Scope the key to one repository and read the setup skill before wiring it into a pipeline that handles client code.

## Limitations

- Snapshot data, verified 2026-10-28: 10899 combined installs across 6 indexed listings; 137 GitHub stars; MIT license; last pushed 2026-10-28. Counts drift over time.
- The install index outruns the tree: fallow-analysis carries 1 install but has no matching directory under `fallow/skills/` in the current tree, so its scope is not documented in this repository.
- The skills are instructions, not the analyzer. Nothing works until fallow is installed in the target project through npm, npx or cargo, and a missing binary is the usual reason a run looks broken.
- Adoption is concentrated in one skill: 9,765 of the 10,899 installs are `fallow`, while the four setup and review skills sit at 914, 140, 75 and 4. There is little independent signal on the smaller skills.
- The analyzer covers TypeScript and JavaScript only, and the Fallow Cloud tier behind `fallow-cloud-setup` is a paid product that needs `FALLOW_API_KEY`. Local static analysis needs neither an account nor a key.
- The README documents install for the skills.sh CLI, the Claude Code plugin, the Codex plugin, Gemini CLI, Windsurf, Amp and a plain directory copy. Nothing is written for Hermes, so the copy route above is the one to use.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)

## Pro Tips

- Install `fallow` and `fallow-review` first and leave the rest until a task needs them. The analysis skill carries the CLI contract, the review skill assumes it, and the setup and cloud skills each answer one question.
- Ask for `--format json --quiet` explicitly. The skill treats compact JSON on stdout with stderr kept separate as a hard rule, and a human-format run is not something a later agent step can parse.
- Run `fallow audit --base main` on the branch before you ask for a review. The review skill is built to spend attention on what the deterministic pass cannot decide, so running it on unanalyzed code wastes the loop.
- When a review judgment comes back rejected, check the `graph_snapshot_hash` before rewriting the reasoning. A stale guide means the tree changed underneath you, and the fix is a fresh guide rather than a better argument.
- Keep the CI gate on a baseline rather than an absolute count. A regression baseline fails on new findings and tolerates the ones a repository inherited, which is what makes the gate adoptable on an existing codebase.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
