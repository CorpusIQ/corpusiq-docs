---
title: "Multi-Agent Review - Adversarial Code Review Setup"
description: "riekelt/multi-agent-review: 19.5K combined installs. Fail-closed six-agent panel reviews specs and plans before execution, juror on disagreement."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/multi-agent-review-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "multi-agent", "verification", "spec review"]
---

# Multi-Agent Review - Setup Guide

**Source:** [riekelt/multi-agent-review](https://www.skills.sh/riekelt/multi-agent-review) via skills.sh - 19.5K combined installs across 1 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [riekelt/multi-agent-review](https://github.com/riekelt/multi-agent-review) - 82 stars, no LICENSE file in the tree (the GitHub API reports no license and the README's own License section states MIT), branch main, last pushed 2026-08-22; one skill tree at `plugins/multi-agent-review/skills/multi-agent-review/` holding `SKILL.md`, `agents/` (four reviewer prompt files) and `assets/project-rules.example.md`, beside `evals/` (`evals.json`, `trigger-evals.json`, `fixtures/`) and three per-platform plugin manifests (`.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`)

**Category:** Multi-agent code review and adversarial verification workflows

**Quality Tier:** 🟡 1 sampled FAIL verdict(s) in the security table; review before install - one coordinator skill that drives six reviewer agents and a fail-closed verdict gate

`riekelt/multi-agent-review` is a single-skill repository with a narrow and unusual job: it reviews specs and plans, not code, and it does so before execution rather than after. The README states the intent plainly and the skill file backs it up. Six review agents run in parallel, a fast tier and a standard tier each covering completeness, alignment and risk, and a single reasoning-tier juror is convened only when the two tiers disagree on a finding. If they agree, no juror is dispatched and no reasoning-tier tokens are spent.

What makes it worth reading as a design rather than as another review prompt is the fail-closed contract. A dead juror does not soften a contested finding, it promotes every contested finding to BLOCKER. A panel with fewer than three valid reports halts instead of returning a verdict. An empty panel can never yield a clean result, and the skill says so twice, once in the failure table and once in the coordinator steps. Both fail-closed paths are recorded in the README as having run in operation on Claude Code and Codex, operator-verified on 2026-08-19.

The skill is built as a slot in the Superpowers workflow rather than as a standalone tool. `spec` mode fires after a spec is written and hands off to `writing-plans`; `plan` mode fires after a plan is written and hands off to `subagent-driven-development`. The verdict sorts findings into Blockers, Warnings and Observations, and an inline JSON block alongside each human-readable gate lets the next step consume the result without parsing prose.

## Installation

The README documents no `npx skills add` route and no skills.sh install command, and the skill files carry none either. Every documented path is a plugin install for Claude Code, Codex or Cursor. The Claude Code marketplace pair is the shortest:

```text
/plugin marketplace add riekelt/multi-agent-review
/plugin install multi-agent-review@multi-agent-review
```

The remaining routes clone and copy, because the plugin does not sit at the repository root:

```bash
git clone https://github.com/riekelt/multi-agent-review /tmp/multi-agent-review
cp -r /tmp/multi-agent-review/plugins/multi-agent-review ~/.claude/plugins/multi-agent-review
```

The Codex and Cursor sections repeat that shape against `<your-codex-plugins-dir>` and `<your-cursor-plugins-dir>`; each platform then reads the model tiers from its own `.codex-plugin/plugin.json` or `.cursor-plugin/plugin.json` inside the copied directory.

Hermes loads a skill directory, not a plugin manifest, so the route for this profile is a copy of the skill tree:

```bash
git clone https://github.com/riekelt/multi-agent-review /tmp/multi-agent-review
cp -r /tmp/multi-agent-review/plugins/multi-agent-review/skills/multi-agent-review \
  ~/.hermes/profiles/corpusiq/skills/multi-agent-review
```

Copy the directory and not the markdown alone. `agents/` holds the four prompt files the coordinator reads on every run, one per topic plus the juror, and `assets/project-rules.example.md` is the template the coordinator looks for in a project root. A lone `SKILL.md` leaves the panel with no reviewer prompts to dispatch.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| multi-agent-review | 19,509 | Coordinator for pre-execution review of a spec or plan: locates and validates the artifact, dispatches six reviewers across completeness, alignment and risk in two model tiers in one parallel message, convenes a reasoning-tier juror only on disagreement, then gates the next skill with a fail-closed Blockers, Warnings or Clean verdict plus a machine-readable JSON block. |

No indexed listings fall below the threshold; all 1 appear above.

## Why This Matters for Hermes Agents

An agent that plans before it builds has no independent check on its own plan, and a second opinion from the same model in the same context is not a check at all. This skill is the cheapest honest version of that check: two tiers review the same three topics with different prompts and different model weights, and only the disagreements cost reasoning-tier tokens. For a Hermes profile that already dispatches subagents, the panel is one more parallel dispatch rather than new machinery.

The failure semantics are the part worth copying even if you never install the skill. Quorum is explicit at three of six valid reports, a partial panel is reported as a panel-health warning rather than silently accepted, a juror timeout promotes contested findings to BLOCKER, and a third re-run stops the loop with the finding set you have. Those are the four places where a review pipeline usually degrades quietly, and each one has a stated behaviour instead of a hope.

The gate output is built for automation. Every verdict carries a fenced JSON block with `verdict`, `blockers`, `warnings`, `obs`, `panel_health` and `iteration`, so a cron or an orchestrator can branch on the result without reading prose, and the human-readable gate is emitted alongside it rather than instead of it. That shape is unusual in skills of this size and it is the reason the skill composes with a workflow rather than replacing one.

It is also honest about scope. It does not repair artifacts, does not review code, and does not search outside the Superpowers artifact directories without an explicit path. On a Hermes profile those limits are a feature: the skill refuses work it was not built for instead of producing a plausible verdict about the wrong thing.

## Usage

| You say | What happens |
|---|---|
| "Review my spec before I write the plan" | Spec mode: the coordinator takes the most recent artifact under `docs/superpowers/specs/`, validates it, reads it in full, dispatches completeness, alignment and risk reviewers in both tiers, and gates the handoff to `writing-plans` on the verdict. |
| "Is this plan ready to execute?" | Plan mode: it resolves the plan under `docs/superpowers/plans/`, loads the linked spec as supplementary context for the alignment reviewer, and gates the handoff to `subagent-driven-development`. |
| "Give this plan a cheap second opinion" | `--fast` runs the three fast-tier agents only, with no cross-model comparison and no juror; every finding is accepted at its emitted severity. If the artifact mentions authentication, payments, migrations, data deletion or production infrastructure, the skill refuses the flag and runs the full panel instead. |
| "The two tiers disagree about the risk finding" | The disagreement becomes a CONTESTED_LIST entry, a single reasoning-tier juror receives all six reports plus that list, and its rulings are folded into the accepted findings before bucketing. |
| "Only four reviewers came back, is the verdict usable?" | Quorum check: three to five valid reports carry on with a panel-health warning, fewer than three halt with no verdict at all, and a clean result is never produced from a broken panel. |
| "Override the blockers, I am shipping anyway" | The override is written to stdout and appended as a `git note` to the artifact's most recent commit, composed on stdin so finding titles cannot reach the shell as code, then the next skill is invoked. |
| "Third re-run and it still blocks" | The iteration cap stops at three, the header becomes REVIEW EXHAUSTED, and the operator's only choices are override with a logged note or abort the handoff. |

## Verification

All three raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} skill\n" \
  https://raw.githubusercontent.com/riekelt/multi-agent-review/main/plugins/multi-agent-review/skills/multi-agent-review/SKILL.md
curl -sL -o /dev/null -w "%{http_code} juror\n" \
  https://raw.githubusercontent.com/riekelt/multi-agent-review/main/plugins/multi-agent-review/skills/multi-agent-review/agents/synthesis-agent.md
curl -sL -o /dev/null -w "%{http_code} rules\n" \
  https://raw.githubusercontent.com/riekelt/multi-agent-review/main/plugins/multi-agent-review/skills/multi-agent-review/assets/project-rules.example.md
```

Expect `200` three times. Read the coordinator before installing it: its description is the routing contract, listing the trigger phrases ("review my spec", "is this plan ready to execute", "second opinion on this plan") and naming the two skills it hands off to. `/multi-agent-review spec` and `/multi-agent-review plan` are the two documented entry points, and the optional path argument plus `--fast` are the only modifiers.

After the copy lands in the profile, confirm the tree and the frontmatter:

```bash
ls ~/.hermes/profiles/corpusiq/skills/multi-agent-review/
head -3 ~/.hermes/profiles/corpusiq/skills/multi-agent-review/SKILL.md
```

The listing should show `SKILL.md`, `agents/` and `assets/`, and the frontmatter should carry `name: multi-agent-review` with a description naming the trigger phrases and the fail-closed verdict. A copy without `agents/` has the coordinator but not the panel, which fails at the first dispatch rather than at install time.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| multi-agent-review | Pass | Pass | Fail |

Two trust verdicts pass and the Snyk scan failed, and the pack records the verdict rather than the finding behind it, so read that Snyk entry on skills.sh before installing. The behaviour worth reviewing by hand is in the coordinator itself: it reads files from the project root and from the artifact paths, writes an override record with `git notes append` against the artifact's most recent commit, and dispatches subagents whose prompts are built from repository files under `agents/`. An override path that appends to git history is the one write this skill performs by design, and Step 9's heredoc rule exists because finding titles are model output that must never be interpolated into a shell command line.

Two details reduce the risk surface. Reviewers receive the artifact between explicit BEGIN and END markers and are told that text inside them is data rather than instructions, with an artifact that tries to instruct its reviewers recorded as a BLOCKER. And the skill cannot repair what it reviews, so a compromised artifact cannot be silently rewritten by the panel.

There is no license file in the repository, which matters more than the verdicts if you plan to redistribute the prompts. The README's License section states MIT, while the GitHub API reports no license, so treat the grant as stated rather than detected until a LICENSE file appears.

## Limitations

- Snapshot data, verified 2026-10-30: 19,509 combined installs across 1 indexed listings; 82 GitHub stars; no LICENSE file (README states MIT); last pushed 2026-08-22. Counts drift over time.
- The combined figure is one number, not a suite. skills.sh indexes a single listing for this repository, and the tree carries a single `SKILL.md`, so there is no per-skill install ranking to read and no dispatcher to hold separately.
- No LICENSE file ships in the tree. The README's License section states MIT and the GitHub API reports none, so a redistribution or vendoring decision rests on the README statement rather than on a detected license.
- There is no skills.sh or `npx skills add` install path in the README, so a Hermes install is a directory copy. The copy also breaks the coordinator's plugin-manifest lookup, which walks up from the skill directory to a `.claude-plugin/`, `.codex-plugin/` or `.cursor-plugin/` manifest and otherwise falls back to the hardcoded `haiku` / `sonnet` / `opus` tiers, so check Step 3's resolved tiers if you point the copy at a non-Claude model provider.
- The dispatch assumes a host with a parallel Agent tool, which is how Claude Code, Codex and Cursor run the six-way single-message panel. A host without one can still read the skill and its prompts, but the panel degrades to sequential work or does not run.
- Artifact discovery assumes the Superpowers layout (`docs/superpowers/specs/`, `docs/superpowers/plans/`) and the two named handoff skills. Outside that workflow, pass an explicit path argument on every invocation. The skill also reviews text only: it never reviews code, despite the install-index framing, and it never repairs the artifact it reviews.

## Related

- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)
- [Oh My Hermes (OMH) Suite - Multi-Agent Orchestration Skills Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup)
- [Claw Multi-Agent Skill Setup](/hermes/skills/catalog/claw-multi-agent-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pass an explicit artifact path outside the Superpowers layout. Discovery defaults to the two `docs/superpowers/` directories, and a wrong guess reviews the wrong file with no error.
- Copy `assets/project-rules.example.md` to the project root as `project-rules.md` before the first run. Without it the coordinator falls back to `CLAUDE.md` or `AGENTS.md` and applies only the lines that read as standing constraints, which is a weaker alignment check.
- Keep the full panel for anything touching authentication, payments, migrations or data deletion. `--fast` refuses those artifacts anyway, and a fast-tier-only verdict carries no cross-model adjudication.
- Branch on the JSON block, not the prose. `verdict`, `blockers`, `panel_health` and `iteration` are emitted on every run, which is what makes the gate usable from an orchestrator or a cron.
- Read Step 9 before granting the skill write access to a repository. The override path appends a git note to the artifact's most recent commit, and that is the only mutation the skill performs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
