---
title: "NotebookLM nblm Skill - Source-Grounded Answers"
description: "magicseek/nblm: 6.3K combined installs. One skill that drives NotebookLM through a browser for cited answers, plus podcasts, slides and folder sync."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/magicseek-nblm-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "notebooklm", "notebook lm", "rag", "browser automation"]
---

# NotebookLM nblm - Setup Guide

**Source:** [magicseek/nblm](https://www.skills.sh/magicseek/nblm) via skills.sh - 6.3K combined installs across 1 indexed listing; first documented 2026-11-02 (evening sweep)

**GitHub:** [magicseek/nblm](https://github.com/magicseek/nblm) - 34 stars, MIT license, branch main, last pushed 2026-02-28; a single `SKILL.md` at the repository root rather than under `skills/`, 8 slash-command files in `commands/`, 3 reference pages, 18 Python modules in `scripts/` plus 3 under `scripts/zlibrary/`, and 14 test files

**Category:** NotebookLM access for agents: document-grounded question answering, notebook library management, source sync and media generation

**Quality Tier:** 🟡 Yellow - the single indexed listing draws a Socket Fail and a Snyk Warn even though Gen Agent Trust Hub passes, the code is MIT and the Python suite carries 14 tests

`nblm` is a one-skill repository from magicseek that turns Google NotebookLM into a tool an agent can call from the terminal. It is a real program, not a prompt: a `SKILL.md` of 621 lines that routes roughly 40 subcommands, an entry point (`scripts/run.py`) that builds a virtual environment and installs dependencies on first use, a browser daemon from `agent-browser` pinned at 0.5.0, an async NotebookLM client through `notebooklm-py`, Google authentication stored per account, a Z-Library downloader with an EPUB converter, and a test suite of 14 files covering the auth, watchdog, sync and source paths.

The architecture is hybrid by design. API calls handle what NotebookLM exposes (create, rename, list, add sources, ask, generate media); a headless browser handles what it does not (Google login, file uploads, Z-Library pulls). The README draws that split in one diagram, and the `SKILL.md` turns it into routing rules an agent follows, including a mandatory follow-up loop: every answer comes back ending with "EXTREMELY IMPORTANT: Is that ALL you need to know?", and the agent is told to stop, compare the answer to the request, and ask again before it answers the user.

## Installation

The README recommends the `add-skill` CLI, which is a different entry point from the `skills` CLI used elsewhere in this catalog:

```bash
npx add-skill magicseek/nblm
```

It can be scoped to one agent or installed globally, and the README shows both:

```bash
npx add-skill magicseek/nblm -a claude-code
npx add-skill magicseek/nblm --global
npx add-skill magicseek/nblm -a claude-code -a cursor -a opencode
```

Where symlinks from that CLI misbehave, the README offers a platform-specific route that clones the repository and generates the agent files directly:

```bash
git clone https://github.com/magicseek/nblm ~/.nblm
python ~/.nblm/scripts/run.py init --ai claude
```

For a Hermes profile the manual install copies the repository contents into the skills directory, because the skill is the repository root rather than a folder inside it:

```bash
git clone --depth 1 https://github.com/magicseek/nblm.git /tmp/nblm
mkdir -p ~/.hermes/profiles/corpusiq/skills/nblm
cp -R /tmp/nblm/SKILL.md /tmp/nblm/commands /tmp/nblm/references /tmp/nblm/scripts \
      /tmp/nblm/requirements.txt /tmp/nblm/package.json \
      ~/.hermes/profiles/corpusiq/skills/nblm/
```

Copy the scripts with the skill. `SKILL.md` routes every command through `python scripts/run.py`, and that wrapper is what creates the `.venv`, installs from `requirements.txt` and runs `npm install` for the browser daemon. A copy holding only the Markdown looks installed and fails on the first command.

You need Python 3.8 or newer and Node.js. On first use the wrapper builds the environment and starts the `agent-browser` daemon, which stops after 10 minutes idle. Google authentication is one-time and opens a visible browser window:

```bash
python scripts/run.py auth_manager.py setup
```

If Playwright browsers are missing the README says to run `npm run install-browsers` in the skill folder. Each notebook you query must be shared as "Anyone with link" on notebooklm.google.com before `/nblm add` can read it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nblm | 6,322 | Asking a NotebookLM notebook a question from the terminal and getting a document-grounded answer with citations: `ask` against the active notebook or a named id or URL, source listing and full source text, uploads of a file or a whole folder with state tracking, URL, YouTube and pasted-text sources, a Z-Library pull, multi-account Google auth with switching, notebook create, rename, delete, summary and describe, audio deep dives, briefs and debates with `--length SHORT` or `--length LONG`, slide decks as PDF, infographics as PNG, and a media list and delete surface for the generated artifacts. |

All 1 indexed listings clear the threshold and appear in the table above.

The skill text is backed by three reference pages (`api_reference.md`, `troubleshooting.md`, `usage_patterns.md`) and one Markdown file per slash command in `commands/`. The routing table in `SKILL.md` is the important part: every command maps to an explicit `python scripts/run.py <module> <action>` call, so an agent does not have to guess a CLI shape, and the `$ARGUMENTS` block tells it to ask the user whether an upload goes to the active notebook or a new one instead of picking silently.

## Why This Matters for Hermes Agents

A model answering from memory invents citations. Routing the same question into NotebookLM changes the job from recall to retrieval: the answer is constrained to documents someone uploaded, and it comes back with source references. That is the difference between an agent that can draft a claim and an agent that can defend one, and it is why a browser-automation skill of this size has 6.3K installs behind a single listing.

The second reason is durability across an agent's own documents. Notebooks are a library the agent can grow: add a repo, sync a folder of specs, pull a paper, and the same question surface keeps working. The folder sync tracks file hashes, so a re-run adds new files, deletes and re-uploads modified ones and skips the rest, which is the behaviour you want from a nightly job rather than a manual upload ritual.

The third is that the follow-up loop is written down as procedure rather than left to taste. Each answer is independent, with no session memory, so a single question usually returns part of what a user asked for. The skill instructs the agent to compare the answer against the original request, identify the gaps and ask again before synthesising, which is exactly the discipline that turns a retrieval call into a usable answer.

The costs are real and worth stating: every query is a browser session against a Google account with a free-tier limit of roughly 50 queries a day, so this is a research tool rather than a hot path in a production loop.

## Usage

| You say | What happens |
|---|---|
| "Ask my notebook what the contract says about termination" | Runs the question against the active notebook, returns the document-grounded answer with its citations, then asks a follow-up if the answer left part of the request uncovered. |
| "Add this NotebookLM link to my library" | Fetches the title from the NotebookLM API, queries the notebook to generate a description and topics, and stores it locally without asking you to type metadata. |
| "Sync this folder of PDFs into the research notebook" | Runs a dry-run plan first, then adds new files, deletes and re-uploads changed ones and skips unchanged ones, printing a ready count as NotebookLM finishes processing each source. |
| "Turn that notebook into a podcast" | Generates a deep-dive audio artifact, with `--length` and `--instructions`, polls the task id, and downloads the MP3 once generation completes. |
| "Make a slide deck out of the findings" | Generates a detailed deck or presenter slides as a PDF and downloads it to a path you name. |
| "Which Google account is this using?" | Lists the accounts in the credential index, shows which one is active, and can switch by index or email. |
| "That answer was thin, push further" | Re-queries with the missing context carried in the question, because each call is independent and no previous answer is remembered. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02. Note that it is at the repository root, not under `skills/`:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/magicseek/nblm/main/SKILL.md
```

After a clone, confirm the skill and its support directories arrived together:

```bash
git clone --depth 1 https://github.com/magicseek/nblm.git /tmp/nblm
find /tmp/nblm -name SKILL.md | wc -l
ls /tmp/nblm/commands | wc -l
ls /tmp/nblm/references | wc -l
head -3 /tmp/nblm/SKILL.md
```

The first count should print 1 and it should be the root file, the second 8, the third 3, and `head` should show `name: nblm` with the description the runtime routes on. On the installed copy, the wrapper is the real smoke test:

```bash
cd ~/.hermes/profiles/corpusiq/skills/nblm
python scripts/run.py auth_manager.py status
```

That call builds the virtual environment on first run and prints auth and library state. If it fails, the problem is the environment rather than the skill, and the `SKILL.md` troubleshooting table names the usual causes: `ModuleNotFoundError` from calling a script directly instead of through `run.py`, `DAEMON_UNAVAILABLE` from a missing Node install, and `AUTH_REQUIRED` from an expired login.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nblm | Pass | Fail | Warn |

This is the most invasive skill class in this catalog: it drives a real browser against a logged-in Google account, and it holds the resulting credentials on disk. The tree is honest about that. Authentication lives in a `data/` directory the `.gitignore` covers, the login flow forces a visible browser window because the Google sign-in is a manual step, and the material is MIT licensed so the code can be read before it runs. What it cannot fix is the dependency surface: `package.json` pins `agent-browser` at 0.5.0 and `requirements.txt` pulls `patchright`, an anti-detection fork of Playwright, alongside `notebooklm-py` and `ebooklib`. A scanner that flags automation and stealth primitives will flag this, and the pack does not record which rule fired. Read the Socket report before you install into a profile that holds other credentials.

Two operational cautions follow. Run it against a dedicated Google account rather than a primary one, since the session, the rate limit and any account-level flag all attach to that login. And decide about the Z-Library path deliberately: `upload-zlib` downloads copyrighted books from zlib mirrors through `scripts/zlibrary/`, which is a legal question for you and not a technical one for the skill.

The generated artifacts deserve a second look too. Podcasts, slides and infographics are produced from whatever documents you upload, so the risk of leaking internal material lives in the notebook, not in this repository.

## Limitations

- Snapshot data, verified 2026-11-02: 6,322 combined installs across 1 indexed listing; 34 GitHub stars; MIT; last pushed 2026-02-28. Counts drift over time.
- Socket returns a Fail and Snyk a Warn on the only sampled listing, with no cause recorded in the pack. The code is readable, but the verdict is not clean.
- The skill automates the NotebookLM web UI for login and uploads, and the last commit is roughly eight months before this snapshot. A UI change upstream breaks selectors faster than a commit cadence like that can follow, and the troubleshooting table already lists `ELEMENT_NOT_FOUND` as a routine failure.
- Free Google accounts are limited to about 50 queries a day, and the answer is to add another account rather than to wait. Every query is a fresh browser session with a few seconds of overhead and no memory of the previous answer.
- The instructions contradict themselves in two places, both visible in the clone. The smart-add section says never to specify `--name`, `--description` or `--topics`, while the script reference marks `--description` and `--topics` as required. The data storage section names `~/.claude/skills/notebooklm/data/`, a path from before the rename, while the README says data lives in the skill's own `data/` directory. Trust `run.py` and the README.
- The `SKILL.md` is 621 lines of routing table plus extended documentation, which is a lot of context for one skill. Load it, but expect the reference pages to carry the detail.

## Related

- [NotebookLM Skill - Archived Notebook Query Setup](/hermes/skills/catalog/notebooklm-skill-setup)
- [JEO Skills - Presentation and Document Suite](/hermes/skills/catalog/jeo-skills-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)
- [NotebookLM - Unofficial Gemini Notebook CLI and Skill Setup](/hermes/skills/catalog/notebooklm-py-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always call through `python scripts/run.py <module> <action>`. The wrapper builds and activates the virtual environment; the scripts fail with `ModuleNotFoundError` when called directly, and that failure looks like a broken install.
- Check `auth_manager.py status` before any batch of questions. An expired login surfaces as a failed query rather than an auth error, which costs a debugging round.
- Put `--dry-run` on every folder sync first. It prints the plan (new, modified, skipped) without touching NotebookLM, which is the cheapest way to catch a path that would upload 400 files.
- Activate the notebook you are working in, then omit `--notebook-id`. The skill defaults to the active notebook, and a long id typed once is a transaction lost to a typo.
- Ask one question per call and expect to follow up. The skill is explicit that answers are independent; a compound question returns the first half and the follow-up loop is how you get the rest.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
