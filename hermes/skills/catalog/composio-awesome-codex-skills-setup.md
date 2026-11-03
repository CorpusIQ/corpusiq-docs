---
title: "Awesome Codex Skills - Curated Codex Index"
description: "composio-community/awesome-codex-skills: 25.0K combined installs. A curated Codex skill index with its own installer and 880 SKILL.md directories."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/composio-awesome-codex-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "codex", "curated index", "skill installer"]
---

# Awesome Codex Skills - Setup Guide

**Source:** [composio-community/awesome-codex-skills](https://www.skills.sh/composio-community/awesome-codex-skills) via skills.sh - 25.0K combined installs across 61 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) - 17,150 stars, no LICENSE file in the repository root, branch master, last pushed 2026-07-26; 880 `SKILL.md` files, 48 of them in top-level skill folders and 832 more under `composio-skills/` as connector wrappers

**Category:** Curated index of Codex agent skills: community picks, packs and installable SKILL.md collections

**Quality Tier:** 🟡 Yellow - no LICENSE file in the repository root leaves redistribution terms unstated, and three of the five sampled skills carry Snyk warns even though every Gen Agent Trust Hub and Socket verdict is a Pass

Composio keeps this repository as a curated list rather than a single product, and the framing in the README is literal: a list of practical Codex skills for automating workflows across the Codex CLI and the API. Each entry is one folder with a `SKILL.md` holding `name` and `description` frontmatter, which is what the agent reads before the body is loaded. The listings split into five README sections: development and code tools, productivity and collaboration, communication and writing, data and analysis, and meta and utilities.

The size is the point and also the trap. skills.sh indexes 61 listings for the repository, but the tree carries 880 `SKILL.md` directories, because most of the folders under `composio-skills/` are one-per-service connector wrappers for the Composio tool catalogue rather than individually indexed skills. Twenty two listings clear the 499-install threshold used here, and they are almost entirely the general purpose ones: planning, CI repair, PR comment handling, meeting notes, spreadsheets, themes and MCP server building. The repository also ships its own installer, `skill-installer/scripts/install-skill-from-github.py`, so a skill can be pulled by repository and path instead of cloned by hand.

## Installation

The README's recommended route is the bundled installer, which needs a clone first because the script lives inside the repository:

```bash
git clone https://github.com/ComposioHQ/awesome-codex-skills.git
cd awesome-codex-skills
python skill-installer/scripts/install-skill-from-github.py --repo ComposioHQ/awesome-codex-skills --path meeting-notes-and-actions
```

The installer places the skill in `$CODEX_HOME/skills/<skill-name>`, which defaults to `~/.codex/skills`. The README's manual route is the same operation without the script: copy the skill folder into `$CODEX_HOME/skills/` and restart Codex so the new metadata loads. There is no `npx skills` command documented for this repository, so the CLI route that most of this catalogue's guides use does not apply here.

For Hermes the durable route is the directory copy, because the agent reads skills from the profile skills directory rather than from `$CODEX_HOME`:

```bash
git clone --depth 1 https://github.com/composio-community/awesome-codex-skills.git /tmp/awesome-codex-skills
cp -r /tmp/awesome-codex-skills/theme-factory ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/awesome-codex-skills/mcp-builder ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole folder, not just `SKILL.md`, because the better skills carry their own support files: `scripts/`, `reference/`, `themes/` or `canvas-fonts/`. Note the owner mismatch before pasting the README commands: the README still says `ComposioHQ/awesome-codex-skills`, which redirects to the canonical `composio-community/awesome-codex-skills`, and the clone command works either way.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| theme-factory | 709 | Reusable theme tokens and palettes for generated artifacts, with 10 named theme files under `themes/` ranging from modern-minimalist to midnight-galaxy. |
| spreadsheet-formula-helper | 702 | Writing and debugging spreadsheet formulas, pivots and array formulas. |
| create-plan | 670 | Drafting concise execution plans for coding tasks before any code is written. |
| webapp-testing | 667 | Testing local web applications with Playwright: verifying frontend behaviour, capturing screenshots and reading browser logs, with `scripts/with_server.py` to start a server and run a test command against it. |
| meeting-notes-and-actions | 633 | Turning meeting transcripts into summaries with decisions and owner-tagged action items. |
| content-research-writer | 629 | Researching and drafting content with sourced citations. |
| file-organizer | 591 | Organising, renaming and tidying files to keep a workspace clean. |
| connect | 587 | Connecting the agent to 1,000+ apps through the Composio CLI for real actions in Slack, GitHub, Notion and similar services. |
| gh-fix-ci | 575 | Inspecting failing GitHub Actions checks, summarising the failures and proposing fixes, with `scripts/inspect_pr_checks.py` doing the lookup. |
| support-ticket-triage | 574 | Triaging customer support tickets into categories, priority, next actions and draft replies. |
| mcp-builder | 533 | Building and evaluating MCP servers, with an evaluation harness in `scripts/` and separate reference documents for Node and Python servers. |
| email-draft-polish | 531 | Drafting, rewriting or condensing emails for the right tone and audience. |
| paperjsx | 526 | Generating PPTX, DOCX, XLSX and PDF output from structured JSON through the local `@paperjsx/mcp-server`, with no API key and no network calls. |
| changelog-generator | 526 | Turning commits or summaries into readable changelogs. |
| gh-address-comments | 522 | Addressing review or issue comments on the open PR for the current branch through `gh`, with `scripts/fetch_comments.py`. |
| skill-creator | 519 | Guidance for building Codex skills with progressive disclosure, plus `init_skill.py`, `quick_validate.py` and `package_skill.py`. |
| codebase-migrate | 512 | Running large codebase migrations and multi-file refactors in reviewable batches with CI verification. |
| tailored-resume-generator | 506 | Tailoring a resume to a job description with quantified impact. |
| canvas-design | 506 | Generating structured canvas layouts and design artifacts, with 54 bundled font files and their OFL licence texts under `canvas-fonts/`. |
| lead-research-assistant | 499 | Researching leads and enriching records with firmographic data. |
| connect-apps | 499 | Wiring Composio CLI connections and starting app workflows from the shell. |
| brand-guidelines | 499 | Applying OpenAI and Codex brand colours and typography to artifacts. |

The remaining 39 indexed listings range from 1 to 496 installs.

## Why This Matters for Hermes Agents

A curated index is useful to an agent in a way a single skill pack is not: it is a menu with descriptions and per-item install counts, so the choice of what to add is an evidence question rather than a taste question. The counts here are tightly clustered, with the top listing at 709 and the threshold row at 499, which says more about the index than about quality: everything above the line is in the same band, so the descriptions matter more than the ranking.

The composition is unusual for this catalogue. Most guides here cover one publisher's engineering suite, while this repository is a broad productivity set: meetings, invoices, spreadsheets, resume tailoring, support tickets, changelogs. Those are the tasks a profile like this one actually runs on a schedule, and each has a `SKILL.md` that describes when to trigger rather than a script that has to be wired up.

Two entries carry disproportionate weight. `skill-creator` and the bundled `skill-installer` are meta tooling: the first teaches the skill format with progressive disclosure, the second installs by repository and path. Together they turn the repository into something an agent can extend rather than only consume, which is the difference between a prompt library and a working skills directory.

The rest are ordinary skills with ordinary file footprints, which is the reassuring part. There is no package to install and no build step, and the network-touching entries are explicit about it: `connect` and `connect-apps` route through the Composio CLI, `paperjsx` runs locally with no network calls, and the GitHub entries shell out to `gh`.

## Usage

| You say | What happens |
|---|---|
| "Turn this transcript into notes with owners" | `meeting-notes-and-actions` reads the transcript and returns a summary with the decisions and action items tagged to named owners. |
| "CI is red on my branch, fix it" | `gh-fix-ci` inspects the failing Actions checks, summarises each failure and proposes the fix, using `scripts/inspect_pr_checks.py` for the lookup. |
| "Check this web app still works after the refactor" | `webapp-testing` starts the dev server through `scripts/with_server.py`, drives it with Playwright, and reports what broke with screenshots and console output. |
| "Write a build guide for the MCP server we just shipped" | `mcp-builder` works from its Node and Python reference documents and runs the evaluation harness against the server. |
| "Give these slides a consistent palette" | `theme-factory` applies one of its 10 theme files, or derives tokens from a description, before the artifact is generated. |
| "Review the comments on PR 412" | `gh-address-comments` fetches the unresolved review comments for the current branch and works through them with `gh`. |
| "Polish this email before I send it" | `email-draft-polish` rewrites for tone and length against the stated audience, leaving the substance alone. |

## Verification

The raw path for the top skill returned HTTP 200 on branch master when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} theme-factory\n" \
  https://raw.githubusercontent.com/composio-community/awesome-codex-skills/master/theme-factory/SKILL.md
```

Expect `200`. Note that the branch here is `master`, not `main`, so any URL built from habit will 404. After the copy lands, confirm the skill and its support files arrived:

```bash
ls ~/.hermes/profiles/corpusiq/skills/theme-factory
head -4 ~/.hermes/profiles/corpusiq/skills/theme-factory/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/theme-factory/themes | wc -l
```

The listing should show `SKILL.md` and a `themes` directory, the header should show `name: theme-factory` with a description line, and the theme count should print 10.

## Security

Three of the five sampled skills carry Snyk warns: `invoice-organizer`, `linear` and `googleads-automation`. The repository has no LICENSE file at its root, which is the larger issue for anything being redistributed rather than read.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| theme-factory | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Pass |
| invoice-organizer | Pass | Pass | Warn |
| linear | Pass | Pass | Warn |
| googleads-automation | Pass | Pass | Warn |

Per-directory licences are inconsistent. Nine of the 22 directories in the table above carry their own `LICENSE.txt` or `license.txt`, and the one checked, `webapp-testing/LICENSE.txt`, is Apache License 2.0, while the other 13 carry none and the repository root carries none. Treat the whole thing as source-available until the licence question is settled per skill.

The executable surface is small but real. Several skills ship Python helpers: `webapp-testing/scripts/with_server.py`, `mcp-builder/scripts/evaluation.py` and `connections.py`, `gh-fix-ci/scripts/inspect_pr_checks.py`, `gh-address-comments/scripts/fetch_comments.py`, and three files under `skill-creator/scripts/`. `canvas-design` ships 54 font binaries and 27 OFL licence texts, which is bulk rather than risk, but it is the reason that directory is 83 files. Everything that touches a network does so through a named tool: the Composio CLI for `connect` and `connect-apps`, `gh` for the GitHub skills, and a local MCP server for `paperjsx`.

Credentials belong in the environment, not in a prompt. The Composio route authenticates through the Composio dashboard and the CLI, so the API key lives in that CLI's configuration; the GitHub skills inherit whatever `gh auth` already holds; `linear` works against a Linear API key. None of these skills should be handed a token inline.

## Limitations

- Snapshot data, verified 2026-10-31: 24,951 combined installs across 61 indexed listings; 17,150 GitHub stars; no LICENSE file; last pushed 2026-07-26. Counts drift over time.
- The index covers 61 listings but the tree holds 880 `SKILL.md` directories. The 832 folders under `composio-skills/` are per-service connector wrappers with no individual install counts, so the table above describes the indexed general purpose skills, not the connector catalogue.
- One listing has no matching directory: `youtube-downloader` (484 installs) is indexed, while the tree and README carry `video-downloader` with the description "Download and prepare videos for offline review". The names do not line up, so treat the two as the same skill only after checking the `SKILL.md`.
- The repository is an index, so quality varies by entry. Several README entries point at external repositories (`brooks-lint`, `codebase-recon`, `AuraKit`, `Vibe-Skills`, `polywave`) with their own install commands, and nothing in this repository vendors or reviews them.
- There is no LICENSE file at the repository root and per-skill licences are mixed, so redistribution terms are unresolved for roughly half of the table. The README does not mention licensing at all.
- The README's clone commands still name `ComposioHQ/awesome-codex-skills`, which redirects to the canonical `composio-community` owner, and the install counts sit in a narrow 499 to 709 band, so ordering within the table is not a meaningful quality signal.

## Related

- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)
- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by folder, never by `SKILL.md` alone. The value in `mcp-builder`, `webapp-testing` and `skill-creator` is in `scripts/` and `reference/`, and a lone `SKILL.md` produces an agent that describes work it cannot run.
- Use the bundled installer when you want one skill and the clone route when you want a set. The installer places skills in `$CODEX_HOME/skills`, which Codex reads and Hermes does not, so point Hermes at the profile skills directory instead.
- Start with `skill-creator` if the plan is to write your own skills. It is one of the two sampled entries with clean verdicts everywhere, and it explains the frontmatter and progressive disclosure rules the rest of the repository follows.
- Ignore the install ranking inside this repository. The top row at 709 and the threshold row at 499 are close enough that the difference is noise; pick by the description and by whether the skill ships support files.
- Expect `master` in every raw URL and in every `git clone` instruction you copy, and check the licence of the individual skill directory before mirroring it anywhere public.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
