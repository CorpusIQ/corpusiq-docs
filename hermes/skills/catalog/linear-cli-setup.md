---
title: "Linear CLI - Issue Tracking from the Terminal"
description: "schpet/linear-cli: 19.1K combined installs. A Rust CLI plus its agent skill for listing, starting and shipping Linear issues from the shell."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linear-cli-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "linear", "issue tracking", "developer workflow"]
---

# Linear CLI - Setup Guide

**Source:** [schpet/linear-cli](https://www.skills.sh/schpet/linear-cli) via skills.sh - 19.1K combined installs across 2 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [schpet/linear-cli](https://github.com/schpet/linear-cli) - 1,033 stars, ISC with `LICENSE` in the root and a `licenses/` folder, branch main, last pushed 2026-10-23; 2 `SKILL.md` files, the shipped skill at `skills/linear-cli/SKILL.md` and the maintainer's own release workflow at `.claude/skills/release/SKILL.md`

**Category:** Linear from the terminal for agents: list, start, link and close issues and open PRs without leaving the shell

**Quality Tier:** 🟡 Yellow - 1,033 stars under ISC and a genuinely agent-first CLI, but the `linear-cli` listing carries a Snyk warning and one of the two indexed listings is the maintainer's own release workflow

The CLI is a Rust binary that puts Linear's issue tracker where `gh` puts GitHub: `linear issue list` shows the unstarted issues assigned to you, `linear issue start` picks one and creates the branch, `linear issue view` prints the current branch's issue as Markdown, and `linear issue pr` opens a pull request with the title and body preset through the `gh` CLI. It is git and jj aware, so it can tell which issue a branch or a `Linear-issue` commit trailer belongs to, and it can jump to the web app or the desktop app the way `gh` jumps to a repository. Commands cover issues, projects, initiatives, cycles, milestones, documents, templates, teams and users, most with a `--json` form, and a documented exit status lets a script branch on the result.

The skill is the reason it belongs in this catalog. `skills/linear-cli/SKILL.md` is written for an agent that has the CLI on `PATH`: it declares `allowed-tools: Bash(linear:*)` and `Bash(curl:*)`, carries copy-pasteable recipes for the common flows, and falls back to Linear's GraphQL API through `linear api` when no dedicated command covers the operation, which is why the repository also ships `graphql/schema.graphql` for type-checking. Nineteen files in `skills/linear-cli/references/` hold the per-resource detail, and the skill's command list is generated from the CLI's own help output by `just skill-docs`, so the two cannot drift far.

## Installation

The CLI first, since the skill only tells the agent how to drive it. Homebrew on macOS or Linux:

```bash
brew install schpet/tap/linear
```

Or pin a version in a project as a dev dependency. The npm package ships prebuilt binaries:

```bash
npm install -D @schpet/linear-cli
npx linear issue list
```

The README also documents a shell installer for macOS and Linux (`https://github.com/schpet/linear-cli/releases/latest/download/linear-installer.sh`), the release binaries page, and a source build with a Rust toolchain:

```bash
cargo install --locked --git https://github.com/schpet/linear-cli linear
```

Then authenticate and configure the repository. Creating the API key needs member access, since guest accounts cannot make one:

```bash
linear auth login
cd my-project-repo
linear config
```

`linear config` writes the project config file, and `docs/authentication.md` covers multi-workspace setups, the `LINEAR_API_KEY` environment variable and the strict workspace selection rules.

The skill installs on its own path. The README gives the skills.sh command for agents other than Claude Code:

```bash
npx skills add schpet/linear-cli
```

Claude Code users get the same skill through the plugin marketplace:

```bash
claude plugin marketplace add schpet/linear-cli
claude plugin install linear-cli@linear-cli
```

For a Hermes profile, copy the one folder. The `Release` skill is the maintainer's own workflow, so it is not part of a user install:

```bash
git clone --depth 1 https://github.com/schpet/linear-cli.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R linear-cli/skills/linear-cli ~/.hermes/profiles/corpusiq/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| linear-cli | 15,194 | Driving the Linear CLI from an agent: query and list issues with filters (`--team`, `--state`, `--assignee`, `--label`, `--updated-after`), start an issue and create its branch, view the current issue as Markdown, open a PR with `gh`, create and update issues, comment and attach files, and fall back to `linear api` for the GraphQL operations no command covers. Declares `Bash(linear:*)` and `Bash(curl:*)` as its allowed tools. |
| Release | 3,892 | The maintainer's release workflow for this repository: review commits since the last release, update the changelog, determine the semver bump, run the tests, then tag and publish. It assumes `changelog`, `svbump`, `jj`, `just` and `jq` are present, so it is a reference for how a release skill is written rather than something to install. |

No indexed listings fall below the threshold; both listings appear above.

The two rows are different in kind. `linear-cli` is the skill you install; `Release` is the project's own tooling that happens to be a skill, which is why the repository publishes two `SKILL.md` files and why the index counts them both. The CLI's exit statuses are documented in the README as a table, 0 for success, 1 for any other failure, 2 for a usage error rejected before anything is sent, 3 for not found, 4 for authentication, 5 for unavailable including rate limiting, and 130 for a cancelled prompt, which is what makes the skill's recipes scriptable rather than just instructive.

## Why This Matters for Hermes Agents

An agent that works on code usually also has to work on the tracker, and the tracker is where a shell agent loses its footing. Without a CLI it drives a browser, retries a web form, or reads a token out of an environment variable and hand-rolls GraphQL. With this CLI the same agent gets one binary with stable subcommands, `--json` output it can parse, and exit codes that distinguish "you are not authenticated" from "that issue does not exist", which is the difference between a retry and a wrong fix.

The branch convention is the quiet win. `linear issue start` creates a branch whose name carries the issue ID, and the CLI then resolves the current issue from that branch, so an agent asked to "finish what I started" has a deterministic way to find out what that is instead of guessing from the commit messages. The jj path works the same way through `Linear-issue` trailers.

For unattended runs, the skill is a bounded surface. It declares exactly two tool patterns, `Bash(linear:*)` and `Bash(curl:*)`, so the agent is not given a general shell to reach the tracker with, and every recipe in it is a command you can run yourself to see what the agent did. Attachments are private by default, and the public-image flag prints a warning because it bypasses workspace access controls.

The last point is maintenance. Because the skill's command list is generated from `linear --help` by `just skill-docs`, a stale instruction is a bug the maintainer can regenerate rather than a drift nobody notices. An operator auditing the skill can compare it against `linear --help` in one command.

## Usage

| You say | What happens |
|---|---|
| "What am I working on?" | Runs `linear issue list` for the unstarted issues assigned to you in the configured team, or `linear issue query --all-teams` across every team, with `--json` when the answer needs parsing. |
| "Start ENG-123" | Runs `linear issue start ENG-123`, which switches to or creates the branch for that issue, so the next commit already carries the ID Linear is watching. |
| "What is this branch about?" | Runs `linear issue view` and prints the current branch's issue as Markdown. |
| "Open a PR for this" | Runs `linear issue pr`, which builds the pull request through the `gh` CLI with the issue title and body preset and the Linear URL appended. |
| "File a bug for the login redirect" | Runs `linear issue create`, interactively or with flags, optionally from a workspace template (`--template "Bug report"`) so the labels and body come from the template instead of the prompt. |
| "Move ENG-123 to in progress and add a comment" | Runs `linear issue update ENG-123 -s started` and `linear issue comment add`, passing only the fields it means to change; the rest stay as they are. |
| "Attach this screenshot to the issue" | Runs `linear issue attach ENG-123 ./screenshot.png`, private to the workspace unless `--public` is passed, which only works for raster images and prints a warning. |

## Verification

Both raw paths below returned 200 on branch main on 2026-11-02:

```bash
for p in skills/linear-cli .claude/skills/release; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/schpet/linear-cli/main/$p/SKILL.md"
done
```

The CLI has to be on `PATH` before the skill is useful, and the skill's own prerequisite check is the same one:

```bash
linear --version
npx @schpet/linear-cli --version
linear auth whoami
```

The first two print the version, and `whoami` names the workspace and user the CLI resolved, which is the fastest way to catch a key that belongs to the wrong workspace. To confirm the install landed with its references intact:

```bash
git clone --depth 1 https://github.com/schpet/linear-cli.git /tmp/linear-cli
ls /tmp/linear-cli/skills/linear-cli/references | wc -l
head -4 /tmp/linear-cli/skills/linear-cli/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/linear-cli
```

The reference count should print 19, `head` should show the `name: linear-cli` frontmatter and the `allowed-tools` line the runtime reads, and the last command should list `SKILL.md`, `SKILL.template.md` and `references`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| linear-cli | Pass | Pass | Warn |
| Release | Pass | Pass | Pass |

`linear-cli` passes the Gen Agent Trust Hub and Socket scans and carries a Snyk warning, and that warning is the one to read before you hand it to an unattended agent: the skill declares `Bash(linear:*)` and `Bash(curl:*)`, which is a wide grant across everything the CLI can do, including writes to issues, comments, documents and attachments, plus outbound `curl` to Linear's GraphQL endpoint. `Release` passes all three and is not part of a user install.

Credentials are handled better than most CLIs of this kind. `linear auth login` stores the API key in the system keyring (macOS Keychain, Linux libsecret, Windows Credential Manager) and keeps only the workspace list and default in `~/.config/linear/credentials.toml`, so the key is not sitting in a dotfile in the repository. Two habits keep it that way: never put `LINEAR_API_KEY` in a project `.env` that is not git-ignored, since the CLI reads that file, and treat `linear auth token`, which prints the resolved key, as a debugging command rather than something to run in a logged session.

The write surface deserves its own decision. An agent with this skill can file issues, change their state, comment and attach files inside a real workspace, and attachments default to private but `--public` uploads them to a URL that anyone, unauthenticated, can open. If the agent runs unattended, decide up front which of those it may do, and prefer scoping its team with `LINEAR_TEAM_ID` over leaving every team reachable.

## Limitations

- Snapshot data, verified 2026-11-02: 19,086 combined installs across 2 indexed listings; 1,033 GitHub stars; ISC; last pushed 2026-10-23. Counts drift over time.
- `Release` is the maintainer's own release workflow, not a user-facing skill. Half the indexed installs in this pack belong to that repository-internal workflow, so read the combined figure as two very different artifacts.
- The skill is a driver for a separate binary. Nothing works until `linear` is installed and authenticated, and the README's key creation requires member access: guest accounts cannot make an API key at all.
- `linear-cli` carries a Snyk warning and declares `Bash(linear:*)` and `Bash(curl:*)`. The sample covers both listings, but a warning is a reason to read the skill, not a clean bill.
- Attachments are private by default, but `--public` uploads raster images to `public.linear.app` where anyone can read them without authentication, and non-image files cannot be made public at all.
- The command list and `references/` are generated from the CLI's help output by `just skill-docs`, so a skill copied alongside an older CLI can describe flags that binary does not have. Check `linear --version` against the release you installed.

## Related

- [Linear Integration - Issue & Project Management Setup](/hermes/skills/catalog/linear-setup)
- [Agent Bridge - Agent Interoperability Setup](/hermes/skills/catalog/agent-bridge-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `linear config` in each repository rather than relying on the global config. The project file is what sets the default team and the sort order, and it is the layer that a per-project agent should be reading.
- Use `--json` on every read the agent performs, and let the model reason over the parsed output. The human-rendered view is for you, the JSON is for the agent.
- Branch on exit status rather than error text. A 4 means the key is missing or rejected and retrying will not help; a 5 means Linear was unreachable and a retry may work, though a create may still have landed.
- Keep the PR body template in the repository and point `LINEAR_PR_TEMPLATE` at it. `linear issue pr` appends the issue URL, so the body stays consistent across the team.
- Read `docs/usage.md` before training anyone on the CLI. It covers the archive behaviour and the bulk forms the README only sketched.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
