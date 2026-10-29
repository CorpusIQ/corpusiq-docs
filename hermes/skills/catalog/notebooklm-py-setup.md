---
title: "NotebookLM - Unofficial Gemini Notebook CLI and Skill Setup"
description: "teng-lin/notebooklm-py: 10.0K combined installs. Unofficial Python API and CLI for Google Gemini Notebook, plus a root SKILL.md of agent invariants."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/notebooklm-py-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "notebooklm", "gemini notebook", "research automation"]
---

# NotebookLM - Setup Guide

**Source:** [teng-lin/notebooklm-py](https://www.skills.sh/teng-lin/notebooklm-py) via skills.sh - 10.0K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) - 19968 stars, MIT License, branch main, last pushed 2026-10-29; one `SKILL.md` at the repository root (16 KB) sitting on top of a full Python package, with `src/`, `tests/`, `docs/`, `scripts/` CI audits and GitHub workflows around it

**Category:** Research and document automation: an unofficial Python client and CLI for Google Gemini Notebook, wrapped in one agent-facing skill file

**Quality Tier:** 🟡 Beta - a large, actively maintained project (19968 stars, MIT, real test and CI story) whose publisher is explicitly not Google and whose two Warn verdicts sit on an API surface that can change without notice

notebooklm-py is an unofficial Python client, CLI and agent integration for Google Gemini Notebook, the product Google rebranded from NotebookLM in July 2026. The README is blunt about the position: it drives undocumented Google APIs that can change without notice, it is not affiliated with Google, rate limits apply, and it is aimed at prototypes, research and personal projects. The PyPI package keeps the `notebooklm-py` name even though the product is now called Gemini Notebook, and existing NotebookLM links redirect.

What ships is more than a wrapper. The package exposes a typed async API through `NotebookLMClient`, with namespaces for `notebooks`, `sources`, `chat`, `research`, `artifacts`, `mind_maps`, `notes`, `settings`, `sharing`, `labels` and `collections`, plus a CLI that mirrors it with `--json` envelopes, an MCP server, a REST server and an opt-in Android gRPC backend. Sources can come from URLs, YouTube, PDFs, Word, EPUB, audio, video, images, Google Drive or pasted text. Output covers audio overviews, video overviews, slide decks, infographics, reports, data tables, quizzes, flashcards and mind maps, downloadable as MP3, MP4, PDF, PPTX, PNG, CSV, JSON, Markdown or HTML, including batch downloads the web UI does not offer. The part a Hermes profile actually loads is the root `SKILL.md`, which is written as an operating contract rather than a feature tour: `--json` with retained UUIDs, an explicit `-n` notebook id on every scoped command, a unique `NOTEBOOKLM_PROFILE` per concurrent agent, a `source wait` before any chat or generation, downloads pinned to the exact artifact id, `--run-id` for overlapping research, and confirmation before anything destructive or long-running.

## Installation

Two installs are separate. The library has to exist so the `notebooklm` CLI is on `PATH`; the skill file has to exist so the agent knows the invariants. The README's recommended CLI route, which the SKILL.md also offers for CLI-only use:

```bash
uv tool install "notebooklm-py[browser]"   # or: pipx install "notebooklm-py[browser]"
notebooklm login                           # first run downloads Chromium (~170 MB), then Google sign-in
notebooklm auth check --test --json        # expect "status": "ok"
```

The SKILL.md's own pip form is `pip install "notebooklm-py[browser]"`, with `[cookies]` added for browser-cookie extraction and `[headless]` for unattended runs, both installed into the user's existing environment. On `externally-managed-environment` it explicitly says not to reach for `--break-system-packages` and to use `uv tool` or `pipx` instead. For application code it points at the active project environment and the typed async client.

For the skill itself the repository has a single `SKILL.md` at the root and no skill directory. The package can place it (`notebooklm skill install`, `notebooklm skill package`, `notebooklm skill status --json`), and the README advertises the root file for `npx skills add` discovery, so `npx skills add teng-lin/notebooklm-py` is the marketplace route. Hermes loads skills from named directories, so the predictable route is to create one and fetch the file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/notebooklm
curl -sL -o ~/.hermes/profiles/corpusiq/skills/notebooklm/SKILL.md \
  https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/SKILL.md
```

For unattended work, prefer master-token auth over a copied cookie snapshot. Run `notebooklm login --master-token --account <email>` on a trusted workstation, then deploy `master_token.json` rather than `storage_state.json` into the selected profile, with `NOTEBOOKLM_HOME` selecting the base directory and `NOTEBOOKLM_PROFILE` selecting the profile. In CI, `NOTEBOOKLM_MASTER_TOKEN_JSON` is a transport convention, not a variable the package reads: write its value to the profile's `master_token.json` at mode `0600`, unset it, then run `notebooklm auth refresh` to mint the storage state.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| notebooklm | 9973 | An operating contract for driving Gemini Notebook from an agent: `--json` discovery with retained UUIDs, `-n` pinning on every scoped command, a unique `NOTEBOOKLM_PROFILE` per concurrent run, `source wait` to `ready` before chat or generation, artifact downloads pinned to an exact artifact id, `--run-id` for overlapping deep research, auth preflight via `auth check --test --json`, confirmation gates before destructive, generating or downloading actions, and exit-code-first failure handling. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

The failure mode this skill targets is not missing features, it is a capable tool driven sloppily. Almost everything in the file exists because a naive wrapper assumes the wrong thing: that the newest source is ready when `source add` returns, that the newest artifact is the one you generated, that a second agent will not overwrite the first one's profile, or that a written cookie file means a working session.

Three of its rules are worth copying into any Hermes tool wrapper. The first is identity pinning: keep `.notebook.id`, `.source.id` and `.task_id` from JSON and pass them explicitly, because a positional or latest-wins default is a silent cross-wiring bug when several runs share an account. The second is readiness as an event, not a guess: `source wait` to `ready` before chat, `artifact wait` on the returned task id before download, with exit code 2 reserved for a `source wait` timeout. The third is isolation: one writable `storage_state.json` shared between agents is the defect the per-agent `NOTEBOOKLM_PROFILE=agent-<id>` rule exists to prevent, and a fresh profile has no credentials until you copy a master token into it.

The authorization section is unusually explicit for a community skill. It says the boundary is user intent, not the presence of a CLI prompt, and it names the commands that can act without prompting (`ask --new --json`, `share remove --json`), so "it did not ask me" is never treated as consent. It also separates read-only diagnosis from recovery: inspect first, mutate later.

The economics are the practical reason to care. Gemini does the reading server-side and answers from your sources with citations, so an agent can orchestrate `create`, `source add` and `ask` while spending tokens only on the final synthesis. The flip side is that this is an undocumented API surface with no SLA, so treat the tool as excellent for research pipelines and unreliable as load-bearing production infrastructure.

## Usage

| You say | What happens |
|---|---|
| "Turn these 30 PDFs into a podcast" | The agent creates a notebook, adds each file with `source add ... --json` and keeps every `.source.id`, runs `source wait` on each until `ready`, starts `generate audio`, waits on the returned task id with `artifact wait -n`, then downloads the exact artifact as an m4a. |
| "What do these documents say about churn?" | `notebooklm ask "..." -n <notebook_id> --json` returns an `answer` plus `references[].source_id`, so the reply arrives with citations rather than an unsourced summary. |
| "Research the EV charging market and pull the best sources in" | Deep research starts non-blocking with `source add-research ... --mode deep --no-wait --json`, the run id is retained, and `research wait --run-id ... --import-all` only runs after you approve the import, since it creates sources. |
| "Is my login still good?" | `notebooklm auth check --test --json` must return `.status == "ok"` and `.checks.token_fetch == true`; a read-only diagnosis uses `--passive` so the check cannot heal and persist cookies behind your back. |
| "Make a 20-question quiz on this material" | `generate quiz` runs, the agent waits on the artifact id, and the finished quiz downloads as JSON, Markdown or HTML, a format the web UI does not export. |
| "Draw a mind map of the argument" | `generate mind-map` returns `mind_map`, `note_id` and `kind` as a finished result, so the agent skips `artifact wait` entirely instead of hanging on a task id that never existed. |
| "Delete that test notebook" | The agent asks first, because notebook, source, note, artifact, label and profile deletion are on the confirmation list, and only passes `--yes` after you say so. |

## Verification

The raw skill path below returned 200 when this guide was written, and it is the same file the table row describes:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/SKILL.md
```

After the manual copy, confirm the file landed where Hermes expects it and that the frontmatter name is `notebooklm`, which is how you tell a current copy from a stale one:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/notebooklm/SKILL.md
head -4 ~/.hermes/profiles/corpusiq/skills/notebooklm/SKILL.md
notebooklm skill status --json    # reports installed versions and content_mismatch
```

Then verify the credential path rather than the file on disk. `notebooklm status` reports the selected notebook, not authentication, so the check that matters is `notebooklm auth check --test --json` returning `status: ok` with `token_fetch: true`. A preflight that fails after a successful `login` usually means stale cookies, where `notebooklm auth refresh` or `auth refresh --browser-cookies <browser>` is the documented next step.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| notebooklm | Pass | Warn | Warn |

There is no FAIL anywhere in the sample, so nothing here is flagged as malicious. The two Warns are on Socket and Snyk, and the pack does not carry their per-finding detail, so treat them as a prompt to read the reports rather than a diagnosis. The plausible surface is visible in the repository itself: the tool signs in to a Google account, stores bearer credentials on disk, downloads Chromium for browser automation, and drives undocumented Google endpoints, all of which look like exactly what a code scanner dislikes. Read `docs/security.md` and `docs/auth-cookie-lifecycle.md` before pointing it at an account you care about.

The credential model is the part to review properly. A master token is described in the skill as a durable full-account credential that survives password changes, so a leaked copy is worse than a stale cookie; the file says to use a dedicated account, keep it in a secret store, mode `0600` on disk, and revoke it explicitly if exposed. It also says never to print, log or commit either auth file, and never to share one writable `storage_state.json` across agents. There is no curl-to-bash installer shipped by this repository, but the README does offer `curl -LsSf https://astral.sh/uv/install.sh | sh` as a fallback when `uv` is missing, which is Astral's installer and should be fetched with the same care as any other pipe-to-shell.

## Limitations

- Snapshot data, verified 2026-10-29: 9973 combined installs across 1 indexed listing; 19968 GitHub stars; MIT License; last pushed 2026-10-29. Counts drift over time.
- The library is unofficial and drives undocumented Google APIs, in the author's own words not affiliated with Google, subject to breakage and rate limits, and recommended for prototypes, research and personal projects. Google renamed the product to Gemini Notebook in July 2026, so product naming in docs and links will keep drifting.
- Index and tree do not line up cleanly. The single indexed listing is named `notebooklm` and the tree has no directory of that name, only a root `SKILL.md`, while the owner has 4 rows across other sources (smithery.ai and two sibling repositories) that this guide does not count.
- Single-maintainer risk is real. The MIT copyright is held by one person, the project is a community effort, and the credential and endpoint behaviour it depends on can change on Google's schedule, not the maintainer's.
- The pack's top-level layout line omits `src/`, `tests/` and `uv.lock`, which the clone does contain, so the repository is a real Python package with a test suite and CI workflows rather than a skill-only repo. Guides grounded on that line alone will understate it.
- Warn verdicts from Socket and Snyk are recorded without finding detail in the pack, so the specific triggers are unverified. Re-check the skills.sh security pages before adopting this in a shared or production account.

## Related

- [NotebookLM Skill - Archived Notebook Query Setup](/hermes/skills/catalog/notebooklm-skill-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the SKILL.md's Operating Invariants twice before writing your own wrapper. Retaining `.source.id` and `.task_id` and passing `-n` explicitly is the difference between a pipeline that works and one that silently processes the wrong notebook.
- Put `notebooklm auth check --test --json` at the top of every unattended job and gate on `token_fetch: true`, not on the existence of a cookie file. It is the cheapest failure you can catch.
- For parallel agents, give each one its own `NOTEBOOKLM_PROFILE=agent-<id>` and a master-token copy in that profile. A shared writable `storage_state.json` is the documented way to break both runs.
- Use `--run-id` on every overlapping research job and `-a <artifact_id>` on every download. Latest-wins selection is fine for a human clicking in the UI and wrong for a script that starts two jobs a minute apart.
- Stay on a PyPI release or tag rather than an unreleased `main` checkout, since the package's contract is the installed CLI's own `--help`, not this or any snapshot of the skill file.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
