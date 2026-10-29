---
title: "Autopilot Skill - End-to-End Build Orchestration Setup"
description: "nick-vels/skills: 5.5K combined. Autopilot takes a dictated idea through spec, tickets and subagent builds to blind acceptance, with a live dashboard."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nick-vels-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "build orchestration", "subagents", "spec driven development"]
---

# Autopilot - Setup Guide

**Source:** [nick-vels/skills](https://www.skills.sh/nick-vels/skills) via skills.sh - 5.5K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [nick-vels/skills](https://github.com/nick-vels/skills) - 564 stars, MIT License, branch main, last pushed 2026-10-29; the tree carries one skill directory, `skills/autopilot/`, holding `SKILL.md` (133 lines), 16 phase files plus `dashboard-template.html` under `phases/`, two subagent prompts under `prompts/`, and a single 1,105 line stdlib Python bookkeeping script at `tools/ap.py`, roughly 340 KB of skill text in total

**Category:** Spec-driven build orchestration, subagent execution and acceptance gating

**Quality Tier:** 🟡 Beta - individual publisher with 564 stars, a real MIT LICENSE, a 489 line unittest suite for `ap.py` and all three sampled auditors passing, but no CI workflow in the tree and a fair amount of Russian-only prose in the runtime files

Nick Vels ships one skill, Autopilot, as a complete development framework. The README calls it "a development framework packaged as a skill" and promises: describe what you want built, get a finished project. The premise is a specific user, not a pair-programming partner: someone who will not read the spec, size the tasks or review the code, and who therefore needs the agent to be explicit about what it committed to on their behalf.

The architecture is the interesting part. `SKILL.md` is a thin orchestrator that assigns phase order, four gates and the rules that never lose, and it is careful about context: each phase's rules live in their own file under `phases/` and are read when that phase starts and not before, so a run does not pay for repair, resume and stress-test instructions until one of those cases fires. The user's original words become a numbered manifest before anything else happens, and that manifest is what every later gate measures against: G1 checks every requirement has a status, G2 checks an independent reader given only the brief and the spec finds nothing missing, G3 runs `ap.py check-plan` to prove every in-spec requirement traces to a ticket, and G4 runs blind acceptance from a clean clone with the spec withheld. Code is written in the second to last phase, one executor subagent per ticket and one commit per ticket, with a fresh reviewer rather than a long-lived one.

Around that sit the operational details that make it more than a prompt: four modes (`full`, `semi` as the default, `interview`, `manual`) and three depth settings (`strict`, normal, `deep`); task sizing by volume of code rather than by caution, roughly 3,000 changed lines per executor with a hard ceiling of twelve tasks before the work is split into two runs; a secrets policy that forbids ever requesting a key and redacts at ingest; and a dashboard that is a single HTML file carrying a snapshot of `state.js`, served on localhost, with colour standing for build state.

## Installation

The README documents the install explicitly. From a terminal:

```bash
npx skills add nick-vels/skills
```

The installer asks which skills to install and for which agents. The non-interactive form, and the one the README tells a non-technical user to paste into their agent, is:

```bash
npx skills add nick-vels/skills --skill autopilot -a claude-code -g -y
```

`--skill autopilot` selects the single skill, `-a claude-code` picks the agent, `-g` installs globally so it is available in every project, `-y` skips questions. Without `-g` it lands in the current project folder only. The README states the requirements plainly: Node.js for `npx`, and any supported agent, with a link to the 70 plus agents the underlying CLI supports. Nothing else.

Updating is a different command, and the README is emphatic that reinstalling is not how you update:

```bash
npx skills update autopilot -g
```

Hermes reads skills from directories, so the CLI route puts the files somewhere Hermes will not look. Clone the repository and copy the one skill directory across:

```bash
git clone --depth 1 https://github.com/nick-vels/skills.git /tmp/nick-vels-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r /tmp/nick-vels-skills/skills/autopilot ~/.hermes/profiles/corpusiq/skills/autopilot
```

Copy the whole directory, not just `SKILL.md`. A lone `SKILL.md` will load and then have nothing to work with, because every phase, both subagent prompts and `ap.py` are referenced by relative path from inside that directory. If you only want to read the skill before deciding, fetch the one file and skip the install:

```bash
curl -sL -o /tmp/autopilot-SKILL.md \
  https://raw.githubusercontent.com/nick-vels/skills/main/skills/autopilot/SKILL.md
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| autopilot | 5521 | One orchestrator skill that flies a dictated idea through eight stages: numbered requirement manifest with verbatim quotes, question rounds only on real forks, spec, ticket plan laid out in waves, one executor subagent per ticket with one commit each, targeted plus whole-branch review, and blind acceptance from a clean clone. Ships four modes and three depth settings, the G1 to G4 manifest gates, a local dashboard driven by `ap.py`, and a secrets policy that never requests or stores a key. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Most build-oriented skills are a style guide with a checklist bolted on. This one is closer to a state machine, and the pieces transfer even if you never run its slash command. The requirement manifest is the strongest idea: the user's words are quoted before they are interpreted, so an agent cannot quietly retire a requirement during the third rewrite, and the only entity allowed to drop one is the user, in their own words, appended to the brief. Any Hermes workflow that starts from a request in natural language can copy that discipline without copying the framework.

The gate design is worth studying too, because G2 and G4 deliberately withhold context. A subagent that gets only the brief and the spec, and not the manifest, cannot see what its author did not write, which is a cleaner test than asking the agent to check its own homework. The orchestrator rule is the other half: the main conversation writes no code at all, only `.autopilot/`, the memory files, `.gitignore`, `.env.example` and git, because its context never refreshes and a diff read on ticket two is still sitting there on ticket eight.

There is also a cost argument with numbers behind it. The repository's own audit measured a startup context of roughly 45,500 tokens and a later refactor cut the orchestrator's starting context from 188 KB to about 75 KB; `tools/measure-run.py` exists to check per-role spend from real logs. For Hermes, where a long session pays for its context on every step, the volume rule (about 3,000 changed lines per executor, twelve tasks maximum) is a useful default to steal.

Two caveats matter before adopting it. The skill is written for Claude Code, Cursor and Codex: the entry point is a `/autopilot` slash command with `disable-model-invocation: true`, so it never starts by itself, and a Hermes agent has to be told to load and follow the skill by name instead. And its runtime prose is partly Russian, which shows up in the dashboard and in the phase files, so an English-only team will be reading mixed labels.

## Usage

| You say | What happens |
|---|---|
| "/autopilot I want a Telegram bot that takes repair requests for appliances and puts them into a Google Sheet" | Phase 0 opens: the agent announces mode and depth, configures the repository, opens the dashboard on localhost, and moves to the manifest. Code is not written until the spec and the ticket plan exist. |
| "/autopilot brief.md" | The file is read as the task, copied into `.autopilot/` as the record the result is checked against, and the original is left untouched. Anything you type after the path is appended to the same task. |
| "/autopilot deep docs/idea.md but no card payments" | Depth is set to `deep`, so empty states, failure paths and limits are worked out further than the brief states, while the exclusion you added stays a requirement that cannot be dropped. |
| "fully automatic" or "interview me" or "approve every step" | The mode switches: `full` asks nothing, `interview` runs the adversarial pass and takes every fork as a question, `manual` does the same plus a spec gate and a plan gate that wait for your approval. |
| "ok" or "2 - a spreadsheet, the rest ok" | Question rounds are answered in bulk: accept all with "ok", or number the one you disagree with and let the rest stand. Answers are recorded into the manifest. |
| "why did ticket 04 come back?" | Repair is recorded as an event: the reviewer's BLOCKING lines go to the same executor that wrote the code, and a plan that turned out wrong is amended with a D row saying what the code demonstrated, never by retiring a requirement. |
| "what do I still need to fill in?" | The final report lists the environment variable names still empty, by name and without values, alongside blind acceptance mismatches and open questions. |

## Verification

The raw path below returned 200 on branch main when this guide was written, and it is the file the install actually loads:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/nick-vels/skills/main/skills/autopilot/SKILL.md
```

Confirm the copy landed completely, since the skill is useless without its phase files:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/autopilot/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/autopilot/phases | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/autopilot/SKILL.md
```

Expect `metadata.version: 2.2.1`, `disable-model-invocation: true`, and 17 entries under `phases/` (16 markdown files plus `dashboard-template.html`). The repository's own test suite exercises `ap.py` and needs nothing beyond the Python standard library:

```bash
python3 -m unittest discover -s tests
```

`skills-lock.json` pins the skill by content hash, `918d6306d3c6e445a21ec52ffc48598816ff71c0972b24b0a16a053d7588aa3c`, which is a quick way to tell whether a copy on disk is the version the repository expects.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| autopilot | Pass | Pass | Pass |

This is the cleanest verdict set in the batch: one listing sampled, three auditors, three passes, no FAIL and no WARN to explain away. What installs is markdown plus one Python script. `ap.py` imports only the standard library (`json`, `os`, `re`, `socket`, `subprocess`, `sys`, `time`, `urllib`), so there is no dependency tree and no postinstall step, and the repository ships no installer that pipes curl into bash. The install path is the `npx skills` CLI, which is itself third-party npm code, so that CLI is the supply chain to trust or vendor around rather than this repository.

The behaviour worth reviewing is what the script does locally rather than what it downloads. `ap.py` runs `git` in your project, starts and stops a `python -m http.server` bound to `127.0.0.1` to serve the dashboard, and makes exactly one outbound request, an HTTPS fetch of `SKILL.md` from `raw.githubusercontent.com` for the version check, which the README says sends no data and which `AUTOPILOT_NO_UPDATE_CHECK=1` turns off. The repository's design notes admit that an early server detection check was broad enough to kill a user's own dev server, and the check is now narrowed to `-m http.server` with an exact `--directory`; if you run other local servers in the same project, that is the paragraph to read before trusting the dashboard lifecycle.

The skill's own rules are unusually strict in the right direction, and they are worth copying even if you never install it: a secret is never requested, echoed or written; anything resembling a key is redacted at ingest before it reaches a file; a leaked key is a stop condition that halts the run; irreversible or outward-facing actions (deploy, publish, pay, message a third party, delete data, rewrite history) are questions rather than steps; and facts about the user are never invented, with prices, texts and addresses left as visible placeholders.

## Limitations

- Snapshot data, verified 2026-10-29: 5521 combined installs across 1 indexed listing; 564 GitHub stars; MIT License; last pushed 2026-10-29. Counts drift over time.
- Index against tree: the single indexed listing is the whole of it. The repository contains exactly one `SKILL.md`, at `skills/autopilot/SKILL.md`, and the two other paths that look like skill directories, `.agents/skills/autopilot` and `.claude/skills/autopilot`, are symlinks to that same directory. There is no second skill to discover, and the index number and the tree agree for once.
- One maintainer, no CI. There is no `.github` directory and no workflow file in the tree, so the 489 line unittest suite runs only when someone runs it. The changelog shows fast iteration on the runtime script (version 2.2.1 is dated the same day as this snapshot), which is good for fixes and bad for surprise behaviour changes.
- Language drift inside the repository. `SKILL.md` still specifies exactly one Russian word per stage and states that phase names are never shown to the user, while the 2.2.0 changelog says the dashboard is now in English. `ap.py` and the phase files carry a large amount of Russian string content, so an English-only team sees a mix, and anyone maintaining a fork has two languages to read.
- It is a product repository with a skill attached. `README.md` is 27 KB of marketing and usage prose, `README.ru.md` is 43 KB, and `assets/`, `docs/`, `CHANGELOG.md` and `tools/measure-run.py` exist for the product. Only `skills/autopilot/` is the installable surface, which is why the copy step above targets that directory alone.
- The entry point is Claude Code shaped. `disable-model-invocation: true` and the `/autopilot` command mean the skill never starts by itself, by design, and `tools/measure-run.py` parses Claude Code session logs specifically. Neither transfers to Hermes as is.

## Related

- [BuilderOS - Product Builder Workflow Suite Setup](/hermes/skills/catalog/builder-os-setup)
- [Wayne Sutton Builder Skills - Convex App Development Setup](/hermes/skills/catalog/waynesutton-builder-skills-setup)
- [Customware Skills - Low-Code App Builder Suite Setup](/hermes/skills/catalog/customware-ai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `phases/0-modes.md` before your first run. Mode and depth are decided once in Phase 0 and they set how much the agent asks and how far past the happy path it works; picking `manual` when you wanted speed is the most common way to be annoyed by this skill.
- Keep the run in its own git repository and let it commit. One commit per ticket is the rollback story, and the `Autopilot-Run` and `Requirements` trailers on those commits are what make `git log --grep` a usable index of what a requirement ever caused.
- Do not edit `state.js`. `ap.py` is the only writer, and the repository's tests exist precisely because hand edits and missing counts used to pass gates silently; the 2.2.1 fixes are all about commands that wrote state they should have refused to write.
- Take the volume rule, not the mode names. About 3,000 changed lines per executor with a twelve task ceiling is the transferable part, and it comes with measurements in `docs/autopilot/design.md` that explain why a long executor is more expensive than a fresh one.
- Copy the four gates into your own Hermes workflows even if you skip the skill. A quoted requirement table plus one acceptance check run by an agent that cannot see your manifest catches the failure this whole framework exists to prevent.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
