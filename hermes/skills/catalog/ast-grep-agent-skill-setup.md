---
title: "ast-grep Skill - Structural Code Search"
description: "ast-grep/agent-skill: 20.8K combined installs. Two skills for structural code search with AST patterns and a cheap outline map of a codebase."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ast-grep-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "ast-grep", "code search", "static analysis"]
---

# ast-grep Skill - Setup Guide

**Source:** [ast-grep/agent-skill](https://www.skills.sh/ast-grep/agent-skill) via skills.sh - 20.8K combined installs across 2 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [ast-grep/agent-skill](https://github.com/ast-grep/agent-skill) - 900 stars, no LICENSE file, branch main, last pushed 2026-09-13; 2 `SKILL.md` files under `ast-grep/skills/`, with `ast-grep/skills/ast-grep/references/rule_reference.md` as the only supporting document in the repo

**Category:** Structural code search and rewriting with ast-grep: AST patterns, rule files and safe codemods

**Quality Tier:** 🟡 Yellow - every sampled verdict is a Pass, but the repository has no LICENSE file at its root, so the licence position rests on a sentence in the README

Two skills, one plugin, and a very lopsided install count. `ast-grep` at 18,303 installs is the reason this repository is in the catalogue: it teaches an agent to write ast-grep rules and search a codebase by syntax tree rather than by text. `ast-grep-outline` at 2,491 is the companion, and it does something much smaller and arguably more useful per token: print a compact structural map of files, directories, imports, exports and direct members so the agent can decide what to read before reading it.

The repository is a Claude Code plugin marketplace rather than a plain skills folder. The root carries `.claude-plugin/marketplace.json`, the plugin lives at `ast-grep/` with its own `.claude-plugin/plugin.json`, and the two skills sit at `ast-grep/skills/ast-grep/` and `ast-grep/skills/outline/`. That last path is worth noting before any raw fetch: the listing and the skill's frontmatter name are both `ast-grep-outline`, but the directory is just `outline`, so URLs and `ls` output do not match the name people search for.

The prerequisite does most of the work. The skill teaches rule authoring, not the binary: ast-grep itself has to be installed on the machine, with `brew install ast-grep`, `npm install -g @ast-grep/cli` or `cargo install ast-grep`, verified with `ast-grep --version`. The README's own framing is honest about what follows from that: installing the skill makes it discovered, not preferred, and because the model is usually also holding a text search tool that needs no setup, it will often reach for grep instead unless structurally-aware search is named in the request.

## Installation

The README's recommended route is the skills CLI:

```bash
npx skills add ast-grep/agent-skill
```

The Claude Code marketplace route installs the whole plugin, and `/plugin install` activates it in the running session without a restart:

```bash
/plugin marketplace add ast-grep/agent-skill
/plugin install ast-grep
```

For local development the README points the marketplace at a clone instead:

```bash
git clone https://github.com/ast-grep/agent-skill.git /path/to/local-marketplace
/plugin marketplace add /path/to/local-marketplace
/plugin install ast-grep
```

The binary is a separate, mandatory install in every case:

```bash
brew install ast-grep
# or
npm install -g @ast-grep/cli
# or
cargo install ast-grep
ast-grep --version
```

For a Hermes profile, the clone-and-copy route keeps both skills and the reference document together:

```bash
git clone --depth 1 https://github.com/ast-grep/agent-skill.git /tmp/agent-skill
cp -r /tmp/agent-skill/ast-grep/skills/. ~/.hermes/profiles/corpusiq/skills/
```

One behaviour is worth adopting with the install. The README recommends stating the preference once in `AGENTS.md` or `CLAUDE.md` rather than repeating it per query, with a snippet that says ast-grep is installed, that structural searches should default to `ast-grep --lang [language] -p '<pattern>'`, and that text-only search should only be used when explicitly requested. Without that sentence the skill competes with grep and often loses.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ast-grep | 18,303 | Writing ast-grep rules for structural code search and analysis: metavariables such as `$VAR`, relational queries like "find X inside Y", composite AND, OR and NOT logic, with a test-first loop that validates the rule against example code before searching the repository. |
| ast-grep-outline | 2,491 | Producing a cheap structural map of a codebase, listing files, directories, imports, exports and direct members, so an agent can survey a project before reading full source. |

All 2 indexed listings appear above; the threshold for this guide is 0 installs, so there is no tail to summarise.

## Why This Matters for Hermes Agents

Text search answers a lexical question and structural search answers a semantic one, and the gap between them is where agent code exploration wastes its budget. "Find async functions that do not handle errors", "find React components using a specific hook", "find functions with more than three parameters", "find `setState` calls inside `useEffect` hooks": grep can approximate none of these, and an agent that tries produces either noise or a confident wrong answer.

The skill's method is the interesting part. It has the agent write the ast-grep rule against example code first, test the rule on that example, and only then run it across the repository. That ordering matters because a zero-match ast-grep run exits successfully, so "there are no matches" and "my pattern is wrong" are indistinguishable from the exit code alone. Testing against a known-positive snippet is the only way to tell those two apart.

The README also addresses the recovery path when a pattern is suspect. It points at `llms-full.txt`, the whole ast-grep documentation as a single file, so the agent can load the real rule syntax instead of guessing at it, and at `ast-grep-mcp`, which lets an agent dump the AST of a snippet and iterate on a pattern rather than committing to one attempt.

`ast-grep-outline` is the cheaper half and worth installing even if rule authoring never happens. A compact map of files, imports, exports and members is exactly the first read an agent should make in an unfamiliar repository, and it costs a fraction of what opening files costs.

## Usage

| You say | What happens |
|---|---|
| "Use ast-grep to find all async functions that lack error handling" | `ast-grep` writes a rule with a `kind` and a negative `has` clause, tests it on an example, then searches the repository and reports file and line numbers. |
| "Show me places we call console.log with more than one argument" | `ast-grep` builds a call pattern with a metavariable and a count constraint instead of a text match. |
| "Find all setState calls inside useEffect hooks" | `ast-grep` uses a relational query so the match is scoped to the enclosing hook. |
| "Give me a map of this repository before I start" | `ast-grep-outline` lists files, directories, imports, exports and direct members as a compact structural summary. |
| "This pattern returns nothing, is my rule wrong" | The agent shows the rule, inspects the AST of a sample and tests against known-positive code, since a zero-match run exits clean either way. |
| "Search for every function with more than 3 parameters" | `ast-grep` writes a parameter-count rule, then runs it across the tree in one pass rather than iterating with grep. |

## Verification

The raw path for the main skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} ast-grep\n" \
  https://raw.githubusercontent.com/ast-grep/agent-skill/main/ast-grep/skills/ast-grep/SKILL.md
```

Expect `200`. After the copy lands, confirm both directories arrived and that the reference file came with the main skill, then check the binary, because a skill without the CLI can only talk about searches it cannot run:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^(ast-grep|outline)$'
ls ~/.hermes/profiles/corpusiq/skills/ast-grep/references
ast-grep --version
head -4 ~/.hermes/profiles/corpusiq/skills/outline/SKILL.md
```

The filter should list `ast-grep` and `outline`, the references listing should show `rule_reference.md`, the version command should print a release, and the header should show `name: ast-grep-outline` inside a directory called `outline`.

## Security

Both skills in this repository were sampled and both are clean across all three auditors.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ast-grep | Pass | Pass | Pass |
| ast-grep-outline | Pass | Pass | Pass |

The content surface is two markdown files and one reference document: no package, no build step, no postinstall hook and no bundled scripts. The real executable surface is the `ast-grep` binary itself, which is installed separately and is not audited by these verdicts, so its distribution channel is the thing to trust: the Homebrew formula, the `@ast-grep/cli` npm package or the crates.io release.

Licensing, not safety, is the reason this guide is Yellow. There is no LICENSE file in the repository root, and the README's License section states only that "this skill follows ast-grep's MIT license for any included documentation or examples". That is a statement of intent rather than a licence grant, so treat redistribution of the skill text as requiring the author's confirmation even though ast-grep itself is MIT.

## Limitations

- Snapshot data, verified 2026-10-31: 20,794 combined installs across 2 indexed listings; 900 GitHub stars; no LICENSE file; last pushed 2026-09-13. Counts drift over time.
- The repository has no LICENSE file at its root. The README says the skill follows ast-grep's MIT license, so the permissive position is asserted in prose rather than granted in a licence file.
- Only two skills are indexed, and one of them accounts for 18,303 of the 20,794 installs, so the combined figure says more about the main skill than about the suite.
- The listing name and the directory name disagree: `ast-grep-outline` lives at `ast-grep/skills/outline/`, so raw URLs and filesystem lookups must use `outline`.
- Nothing works without the `ast-grep` binary. The skill teaches rule authoring and assumes the CLI is installed and on `PATH`.
- Install makes the skill discoverable, not preferred. Without the README's `AGENTS.md` snippet, an agent holding a no-setup text search tool will often use that instead.

## Related

- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Add the README's `AGENTS.md` sentence to the profile's guidance file. Naming ast-grep as the default for structural search is the difference between the skill being loaded and the skill being used.
- Test every rule against an example before running it. A zero-match ast-grep run exits successfully, so an untested pattern and a genuine absence look identical.
- Load `llms-full.txt` from the ast-grep documentation when rule syntax starts getting invented, and use `ast-grep-mcp` when the agent needs to inspect an AST and iterate rather than commit to a guess.
- Install `ast-grep-outline` first in unfamiliar repositories. It is the cheapest first read and it makes the follow-up file reads far more targeted.
- Keep the rule reference open: `references/rule_reference.md` ships with the skill and is the local answer for pattern, `has` and `inside` syntax when the network is not available.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
