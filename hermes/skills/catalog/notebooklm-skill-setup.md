---
title: "NotebookLM Skill - Archived Notebook Query Setup"
description: "PleasePrompto/notebooklm-skill: 7.7K installs, archived. Query Google NotebookLM notebooks from Claude Code through browser automation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/notebooklm-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "research", "browser automation", "google"]
---

# NotebookLM Skill - Setup Guide

**Source:** [PleasePrompto/notebooklm-skill](https://www.skills.sh/pleaseprompto/notebooklm-skill) via skills.sh - 7.7K combined installs across 1 indexed listing; snapshot taken Oct 26, 2026
**GitHub:** [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) (ARCHIVED - read-only since September 2026; 7,790 stars; 894 forks; MIT LICENSE in the repo; last pushed 2026-09-10; branch `master`; one `SKILL.md` at the repo root plus Python automation under `scripts/`)
**Category:** Research / Document Q&A
**Quality Tier:** 🟡 Beta (archived and unmaintained: MIT code frozen since 2026-09-10, no fixes or security patches, and both Socket and Snyk return Warn on the only listing)

**This repository is archived.** GitHub marks it read-only, the README opens with a warning that the project is no longer maintained, and the author states that it "may stop working when the upstream services change". Everything below documents what the skill does and what it costs to run it; nothing below should be read as a recommendation to depend on it in production.

The skill is a Claude Code integration for Google NotebookLM, the source-grounded notebook product built on Gemini. Instead of copying answers between a browser tab and the editor, the agent drives a real Chrome window with Patchright, asks the question in the notebook's chat, reads the answer back, and returns it in the session. The design is deliberately stateless: one question, one browser session, one answer, and an injected follow-up prompt that pushes the agent to ask again until the question is actually covered.

It is also a small, readable reference implementation of an awkward problem - keeping a Google session alive across browser launches while looking human enough not to be flagged. `AUTHENTICATION.md` documents the hybrid auth model (persistent browser profile plus explicit cookie injection) and the Playwright bug that forced it. That document is still worth reading even if you never install the skill.

## Installation

```bash
# Install through the skills CLI
npx skills add pleaseprompto/notebooklm-skill
```

The README's own path is a clone into the Claude Code skills directory, because the skill expects to run from there:

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
```

Prerequisites the README and `requirements.txt` state: Python 3.8 or newer, and real Google Chrome. The first run creates a local `.venv` inside the skill folder and installs `patchright==1.55.2` and `python-dotenv==1.0.0`; nothing is installed globally. The README is explicit that Chrome is used instead of Chromium for cross-platform reliability and a consistent browser fingerprint, and `SKILL.md` opens with a rule that scripts must be run through the wrapper so that environment setup happens automatically:

```bash
python scripts/run.py auth_manager.py status
python scripts/run.py auth_manager.py setup
```

`auth_manager.py setup` opens a visible browser window for a manual Google login. That step cannot be scripted around, and the browser must be visible for it to work.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| notebooklm | 7,745 | Query shared Google NotebookLM notebooks from Claude Code with source-grounded answers, keeping a local library of notebook links, names and topics |

No indexed listings fall below the threshold; the single listing appears above. As with any one-listing entry, the 7,745 figure is adoption of the whole repository rather than a per-skill signal, and in this case the count is frozen: GitHub archived the repository in September 2026, so the number reflects installs up to that point.

## Why This Matters for Hermes Agents

The idea worth stealing is the retrieval contract. NotebookLM answers only from documents the user uploaded, so the failure mode is "the notebook does not cover that", not a confident invention. For an agent, that is a much better failure mode than a web search that returns a plausible blog post. A Hermes session doing research over a fixed corpus - a manual, a vendor's PDF set, a private spec - can get a grounded answer with a citation rather than a synthesis of whatever the search engine ranked.

The second transferable piece is the follow-up loop. Every answer ends with an instruction to ask whether that is all that is needed, and `SKILL.md` turns that into a required sequence: stop, compare the answer against the original request, ask again for the gaps, and only then synthesize. Most agent research stops one question too early; encoding "keep asking" in the harness is the fix.

Third, the library model is simple and portable. Notebook links live in `data/library.json` with a name, a description and topics, and the agent picks the notebook by topic before asking anything. That is the minimum viable index for a document Q&A agent, and it needs no vector store.

What does not transfer is the maintenance assumption. The selectors in the scripts are pinned to NotebookLM's UI as it looked in late 2025, the changelog shows the selectors being rewritten once already, and there will be no third rewrite.

## Usage

| You say | What happens |
|---|---|
| "Set up NotebookLM authentication" | Runs `auth_manager.py setup`, opens a visible Chrome window for a manual Google login, and saves the session for later questions |
| "Add this notebook to my library: [link]" | Queries the notebook first to discover its topics, then saves it to `library.json` with the name, description and topics it found |
| "What does my React docs notebook say about hooks?" | Selects the notebook by topic, opens a browser session, asks the question in the notebook chat and returns the answer |
| "Check the Suzuki manual for rear axle torque" | Queries the loaded manual notebook, follows up on each specification, and returns the values the document actually states |
| "Show my NotebookLM notebooks" | Runs `notebook_manager.py list` and reports the saved notebooks with their topics |
| "Clear NotebookLM data" | Runs the cleanup manager, previews what will be removed, and keeps the library unless told otherwise |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -i notebooklm
```

Read the skill and its prerequisites before installing. All four URLs below returned HTTP 200 when checked with `curl` on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/PleasePrompto/notebooklm-skill/master/SKILL.md | head -60
curl -sL https://raw.githubusercontent.com/PleasePrompto/notebooklm-skill/master/README.md | head -40
curl -sL https://raw.githubusercontent.com/PleasePrompto/notebooklm-skill/master/requirements.txt
curl -sL https://raw.githubusercontent.com/PleasePrompto/notebooklm-skill/master/scripts/run.py | head -40
```

Confirm the archived state yourself rather than trusting this page:

```bash
curl -s https://api.github.com/repos/PleasePrompto/notebooklm-skill | grep -E '"archived"|"pushed_at"'
```

Then check the runtime inside the cloned folder. `status` reports whether a saved session exists; `setup` is the only step that needs a human:

```bash
cd ~/.claude/skills/notebooklm
python scripts/run.py auth_manager.py status
.venv/bin/python -m pip show patchright | head -3
```

## Security

skills.sh verdicts for the only indexed skill (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| notebooklm | Pass | Warn | Warn |

Only one listing exists, so only one page could be sampled; the usual two-to-four sample is not possible here. Both warnings are worth reading rather than skipping, because what this skill does is log a real Google account into a browser it controls.

Read from the repository: the scripts drive a visible Chrome instance with a persistent profile under `data/browser_state/`, save the authenticated session to `state.json` and `data/auth_info.json`, and store the notebook library in `data/library.json`. The README states plainly that `data/` holds authentication data and personal notebooks and must never be committed; `.gitignore` covers it. The skill deliberately uses realistic typing speeds, delays and mouse movement to avoid automated-usage detection, and the README's own disclaimer says it cannot guarantee Google will not flag the account and suggests a dedicated Google account for automation. `run.py` creates a virtual environment and installs dependencies on first run, so the first invocation executes package installation code. The skill needs network access and explicitly does not work in a sandboxed web UI. Treat the Google session as the sensitive asset: revoking it means clearing the browser state, and the cleanup manager is the supported path.

## Limitations

- **Archived means no fixes and no security patches.** The repository is read-only as of September 2026 and the last push was 2026-09-10. Any defect you find, including a credential-handling issue, stays unfixed unless you fork it and maintain the fork yourself.
- The README's named alternative is not a live replacement. It points at the author's NotebookLM MCP server (`PleasePrompto/notebooklm-mcp`, 3,440 stars, MIT) as the more feature-rich option, but that repository is also archived, with the same 2026-09-10 last push, verified through the GitHub API on Oct 26, 2026. If you need a maintained NotebookLM integration, this suite does not currently provide one.
- The code is pinned to NotebookLM's UI and nothing has been committed since 2025-11-21 apart from the archive notice. The 1.3.0 changelog entry (2025-11-21) rewrote the CSS selectors, added a wait for the thinking-message element to disappear, and raised timeouts to 120 seconds, which tells you the previous set had already broken. Any NotebookLM UI change after that date is unhandled and will stay unhandled.
- Browser requirements are stated inconsistently. The README requires real Chrome and says Chromium is deliberately avoided, while `SKILL.md`'s manual setup runs `python -m patchright install chromium` and its environment section says Chromium installs automatically. Follow the README and install Chrome.
- Usage is capped and stateless. `SKILL.md` lists a 50 queries per day limit on free Google accounts, each question opens a fresh browser session with no chat context, and notebooks must be shared by link before the skill can read them.
- Snapshot data, verified Oct 26, 2026: 7,745 combined installs across 1 indexed listing; 7,790 GitHub stars and 894 forks; MIT; archived with last push 2026-09-10. Counts drift over time.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup) - a general browser automation CLI for the same class of task.
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup) - the general browser agent to reach for when a specific integration is unmaintained.
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup) - research with citations and no browser session to keep alive.
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup) - an API-based research path that does not depend on a browser session.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Fork before you install. The clone instruction points at the archived upstream, so clone your fork instead and keep the same folder name (`notebooklm`) so the paths in `SKILL.md` still resolve.
- Use a dedicated Google account. The README recommends it, and it is the only way to contain the blast radius if automated usage is flagged.
- Always go through `scripts/run.py`. Calling `ask_question.py` directly fails without the virtual environment, and the wrapper is what installs the pinned Patchright version.
- Expect one question per browser launch and budget for it. Batch related questions into a single well-formed prompt rather than a chain of small ones, since no chat context is carried between runs.
- If a query returns a placeholder like "Reviewing the content", the selector has drifted. That is the exact failure the 1.3.0 fix addressed, and there is no upstream patch for the next one.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
