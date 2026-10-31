---
title: "Context Engineering Kit - Prompt and MCP Setup"
description: "neolabhq/context-engineering-kit: 110.4K combined installs. 68 agent skills for prompt engineering, reasoning, subagent development and MCP setup."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/context-engineering-kit-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "prompt engineering", "context engineering", "subagents", "mcp"]
---

# Context Engineering Kit - Setup Guide

**Source:** [neolabhq/context-engineering-kit](https://www.skills.sh/neolabhq/context-engineering-kit) via skills.sh - 110.4K combined installs across 138 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [neolabhq/context-engineering-kit](https://github.com/neolabhq/context-engineering-kit) - 1,795 stars, GPL-3.0, branch master, last pushed 2026-08-26; 204 `SKILL.md` files, the same 68 skills mirrored into `skills/`, `antigravity/skills/` and `plugins/<plugin>/skills/`, beside `agents/` (21 subagent prompts), `docs/`, `scripts/`, `justfile` and `plugin.json`

**Category:** Context engineering techniques, prompt craft and agent reliability workflows

**Quality Tier:** 🟡 Yellow - four of five sampled skills Pass on all three auditors and `reflect` carries one Warn from Gen Agent Trust Hub, on a GPL-3.0 copyleft repository with a large, actively mirrored skill tree

NeoLab publishes Context Engineering Kit as `neolabhq/context-engineering-kit`, a hand-crafted collection of context engineering techniques aimed at agent result quality and predictability, with a deliberate emphasis on small token footprint. The README states the marketplace grew out of prompts the company's own developers used daily, supplemented by plugins taken from benchmarked papers and high quality projects, and it names its main plugins as Subagent-Driven Development and Spec-Driven Development, which it recommends starting with.

The suite is organised as thirteen plugins rather than one flat bundle: `sadd` for subagent orchestration and judging, `sdd` for spec-driven development, `kaizen` for continuous improvement analysis, `reflexion` for reflect and critique loops, `customaize-agent` for writing skills and commands, `mcp` for wiring Context7, Serena, Codemap and arXiv, plus `git`, `tdd`, `ddd`, `docs`, `fpf`, `review` and `tech-stack`. Each plugin is meant to load only its own agents, commands and skills, so a profile can take the three or four behaviours it needs instead of the whole catalogue. Version 3.0.0 of the kit added support for AMP and Hermes agents, according to the release notes in the README.

## Installation

The README's Claude Code route adds the marketplace once and then installs individual plugins:

```bash
/plugin marketplace add NeoLabHQ/context-engineering-kit
/plugin install reflexion@NeoLabHQ/context-engineering-kit
```

The generic skills route is the one the README lists for Cursor, Codex, OpenCode and other clients, and it is the route a Hermes profile can use, since it writes plain `SKILL.md` directories:

```bash
npx skills add NeoLabHQ/context-engineering-kit
```

The README flags the tradeoff plainly: `npx skills` does not support subagents, so anything that depends on the bundled agent prompts under `agents/` will run at reduced capability through this route.

Other first-party routes are the Gemini CLI extension, the Antigravity plugin endpoint and OpenSkills:

```bash
gemini extensions install https://github.com/NeoLabHQ/context-engineering-kit
agy plugin install https://github.com/NeoLabHQ/context-engineering-kit/antigravity
npx openskills install NeoLabHQ/context-engineering-kit
npx openskills sync
```

The repository holds 204 `SKILL.md` files, which is 68 distinct skills copied into three trees: `skills/<name>/SKILL.md` for the portable route, `antigravity/skills/<name>/SKILL.md` for the Antigravity plugin, and `plugins/<plugin>/skills/<name>/SKILL.md` for per-plugin installs. A Hermes profile that wants a single plugin without a marketplace can copy that plugin's skill directories straight across:

```bash
cp -r plugins/sadd/skills/do-and-judge ~/.hermes/profiles/corpusiq/skills/do-and-judge
```

Two plugins need more than skills to work as designed. `sdd` drives its workflow through `agents/` and command files, and `fpf` loads a specification the README measures at roughly 600k tokens, which is why the README says it runs in a subagent on a large-context model.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prompt-engineering | 1,441 | Writing commands, hooks, skills and subagent prompts, including prompt optimisation and production template design. |
| context-engineering | 1,407 | Understanding context mechanics such as attention budget, progressive disclosure and the lost-in-the-middle effect before editing prompts, skills or commands. |
| thought-based-reasoning | 1,401 | Choosing a reasoning technique when simple prompting fails: Chain of Thought, self-consistency, Tree of Thoughts, least-to-most, ReAct, PAL, Reflexion. |
| reflect | 1,375 | A self-refinement pass over the previous response, with complexity triage and verification before the agent claims it is done. |
| write-concisely | 1,348 | Applying Elements of Style writing rules to documentation humans read, so prose gets clearer, stronger and shorter. |
| kaizen | 1,314 | Continuous improvement analysis for implementation, refactoring and process work, including how to avoid over-engineering. |
| brainstorm | 1,312 | Refining a rough idea into a designed plan through collaborative questioning and alternatives, before code or an implementation plan exists. |
| multi-agent-patterns | 1,310 | Designing supervisor, peer-to-peer or hierarchical agent architectures when one context window stops being enough. |
| critique | 1,309 | Multi-perspective review by specialised judges that debate to a consensus scoring. |
| root-cause-tracing | 1,304 | Tracing a bug backward through the call stack to the point where invalid data or behaviour first enters. |
| judge-with-debate | 1,298 | Scoring a solution through multi-round debate between independent judges until consensus or a recorded disagreement. |
| update-docs | 1,296 | Keeping docs, READMEs, JSDoc and API references in step with local code changes through a tech-writer agent workflow. |
| subagent-driven-development | 1,293 | Executing a plan of independent tasks by dispatching a fresh subagent per task with code review between tasks. |
| memorize | 1,293 | Curating insights from reflections and critiques into durable project memory so the same correction is not needed twice. |
| agent-evaluation | 1,279 | Evaluating commands, skills and agents with LLM-as-judge rubrics, bias mitigation and a measurement of whether a change actually helped. |
| test-driven-development | 1,276 | A red-green loop for features and bugfixes: write the failing test first, then the minimal code that passes it. |
| plan-task | 1,275 | Refining a draft task specification into acceptance criteria, architecture, per-step sub-task files and verifiable phases. |
| review-local-changes | 1,265 | Reviewing uncommitted working-tree changes plus untracked files before a commit exists. |
| why | 1,255 | Five Whys root cause analysis, drilling from the visible symptom down to the underlying process failure. |
| implement-task | 1,251 | Implementing a planned task step by step with LLM-as-judge verification at the end of every phase. |

The remaining 118 indexed listings range from 17 to 1,249 installs.

Sixty-seven of those 118 names carry a plugin prefix, such as `sdd:plan`, `reflexion:reflect`, `git:commit` or `kaizen:why`, and they index a second time because each plugin ships its own copy of the skill file. Of the 51 plain names, 48 match a directory under `skills/`, and three older entries, `software-architecture`, `worktrees` and `notes`, have no directory in the current tree. Treat the table above as the catalogue and the prefixed names as duplicates.

## Why This Matters for Hermes Agents

Most agent failures in a long session are context failures rather than model failures: the instruction that mattered got buried, the plan drifted, or a subagent inherited a polluted window. This kit is unusual in treating that as the primary engineering problem instead of an afterthought, and it gives an agent named techniques for each stage of the problem, from writing the prompt to verifying the output to remembering the correction.

The subagent programs are the part that maps most directly onto Hermes. `subagent-driven-development`, `do-and-judge` and `do-competitively` describe the dispatch patterns this profile already uses, with an explicit judge step and a retry loop, which makes them useful as written reference material even when the surrounding marketplace is not installed. `multi-agent-patterns` covers the architecture question that comes before that, including when to fan out and when a single agent is cheaper.

The writing-side skills address a different recurring cost. `prompt-engineering`, `context-engineering` and `write-concisely` encode rules about instruction structure and brevity that are otherwise relearned by inspection after each bad output, and `reflect` plus `memorize` give the agent a defined loop for turning a correction into something durable rather than a one-off fix.

Each skill is a self-contained markdown file with no runnable code, scripts or dependencies, which is the safest shape to take into a production profile: there is nothing to execute and nothing to keep in sync. That also means the kit buys process discipline rather than new capability, so the value shows up in output quality and fewer retries, not in a new set of tools.

## Usage

| You say | What happens |
|---|---|
| "This prompt keeps getting ignored, tighten it up" | The agent loads `prompt-engineering` for structure and best-practice patterns, then `context-engineering` to check what else is competing for attention in the window. |
| "Review what I have not committed yet" | `review-local-changes` reads `git diff` plus untracked files and returns actionable suggestions before anything is staged. |
| "It works but the code feels bloated" | `kaizen` applies Value Stream or Muda analysis and `critique` runs the change past specialised judges, which is the over-engineering pass the README describes. |
| "Break this task into something you can actually finish" | `plan-task` produces acceptance criteria, architecture notes, per-step sub-task files and phases, then `implement-task` executes a step at a time with a judge check per phase. |
| "Why does this keep breaking after every refactor?" | `why` walks Five Whys to the process cause, and `root-cause-tracing` follows the bad value back through the call stack when the cause is mechanical rather than procedural. |
| "Do these five fixes without the contexts bleeding" | `subagent-driven-development` dispatches a fresh subagent per task with code review between tasks, so each one starts from a clean window. |
| "Remember this so I do not have to say it twice" | `memorize` curates the insight from the preceding reflection into project memory rather than leaving it in the transcript. |

## Verification

All three raw paths below returned 200 on branch master when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} portable\n" \
  https://raw.githubusercontent.com/neolabhq/context-engineering-kit/master/skills/prompt-engineering/SKILL.md
curl -sL -o /dev/null -w "%{http_code} antigravity\n" \
  https://raw.githubusercontent.com/neolabhq/context-engineering-kit/master/antigravity/skills/prompt-engineering/SKILL.md
curl -sL -o /dev/null -w "%{http_code} plugin\n" \
  https://raw.githubusercontent.com/neolabhq/context-engineering-kit/master/plugins/customaize-agent/skills/prompt-engineering/SKILL.md
```

Expect `200` three times. Fetch the portable one before installing to confirm the frontmatter still carries a `description:` that names trigger situations, because that line is what routing reads.

After a copy lands in the profile, confirm the directory and the file:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/*/ | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/prompt-engineering/SKILL.md
find ~/.hermes/profiles/corpusiq/skills -name SKILL.md | wc -l
```

A good copy shows `name: prompt-engineering`, a one-line description and a single markdown file per skill, with no `scripts/` or `assets/` required beside it. Count the installed files against the 68 you intended to take; the repository's 204 is three mirrored trees, not 204 distinct skills, so a copy that reports 204 has been duplicated.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - one of the five samples, `reflect`, carries a Warn from Gen Agent Trust Hub while the other four Pass on all three auditors. The warn reflects a review of one markdown file and no code was found to execute; re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prompt-engineering | Pass | Pass | Pass |
| context-engineering | Pass | Pass | Pass |
| thought-based-reasoning | Pass | Pass | Pass |
| reflect | Warn | Pass | Pass |
| notes | Pass | Pass | Pass |

Nothing here is a Fail, and the sample is small: five of 68 skills carry a verdict, which is the top four rows of the table plus `notes`. The risk that matters for this kit is therefore not malicious code but instruction quality, since every file is markdown that shapes what an agent believes it should do next. `reflect` prompting the model to revise its own output is exactly the kind of instruction worth reading in full before it runs unattended.

Two behaviours are worth checking before this goes near client work. The `fpf` plugin pulls a large specification into a subagent and the README warns it can consume a token budget quickly, which is a cost control issue rather than a security one but it lands on the same bill. And the `mcp` plugin's setup commands write MCP server configuration into project or user level files, so those commands should be reviewed before they touch a profile that holds credentials.

## Limitations

- Snapshot data, verified 2026-10-30: 110,374 combined installs across 138 indexed listings; 1,795 GitHub stars; GPL-3.0; last pushed 2026-08-26. Counts drift over time.
- GPL-3.0 is copyleft. Copying skill files into a profile is ordinary use, but redistributing a modified version of the kit, or bundling it into something shipped, carries obligations that permissive licences do not.
- The index outruns the tree. skills.sh carries 138 listings while the checkout holds 68 distinct skills in three mirrored trees, so most listing names are plugin-prefixed duplicates of the same file rather than separate installs. Counted exactly: 67 of the 118 below-threshold names carry a plugin prefix, and `software-architecture`, `worktrees` and `notes` have no directory at all.
- The counts are not a ranking, and the spread is narrow. All twenty table rows sit between 1,251 and 1,441 installs, so ordering by install volume tells you almost nothing about which skill is strongest.
- The subagent plugins are designed around Claude Code's agent format. The README states that `npx skills` does not support subagents, so through that route the orchestration skills lose the agents they delegate to and become guidance for building the pattern by hand.
- `fpf` is expensive by design. The README puts its specification at roughly 600k tokens loaded into a subagent and warns it can burn a token budget quickly, so it is not a casual install.

## Related

- [Deep Agents - Batteries-Included Agent Harness Setup](/hermes/skills/catalog/deepagents-setup)
- [PStack Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/pstack-setup)
- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by plugin, not by bundle. The kit is built so each plugin loads only its own agents and skills, and taking `sadd` plus `reflexion` covers most of what a working profile needs at a fraction of the context cost.
- Read `context-engineering` first and `prompt-engineering` second. The mechanics skill explains why the prompt rules exist, which makes the rules stick in actual edits instead of being paraphrased badly later.
- Pair `reflect` with `memorize`. Reflection alone fixes one output; memorizing the finding is what stops the same correction from coming back the next session.
- Take the `skills/<name>/` path when copying into Hermes. It is the portable tree, it matches the raw URL in this guide, and it does not carry the Antigravity or per-plugin metadata.
- Skip `fpf` unless you have a large context budget and an auditable decision to make. It is the one plugin in the kit whose token cost can dominate a session on its own.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
