---
title: "Reddit Research Skills - Market Research Setup Guide"
description: "Reddit research skills for AI agents: 46.8K combined installs for semantic Reddit search, subreddit trends, niche validation and scored B2B leads."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reddit-research-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "reddit research", "market research"]
---

# Reddit Research Skills - Setup Guide

The publisher `lignertys` ships four indexed skills that turn Reddit into a queryable research source. None of them talk to Reddit directly: every search goes through reddapi.dev, a third-party index covering 50,000+ subreddits, 20M+ posts and 40M+ comments, so there is no Reddit OAuth app to register and no Reddit credentials to hold. You get semantic search by meaning, vector search with date filters, trend momentum for named entities and subreddit discovery, plus a separate lead-scoring workflow on top of the same index.

The four listings are not four independent tools. `reddit-research` is the canonical research skill, `reddapi` is the same engine under its original name kept live for existing installs, and `reddit-search-api` is a bare endpoint reference with no workflow framing. `reddit-leads` is the one genuinely different workflow: it scores posts for buying intent. The default branch also carries a fifth skill directory, `reddit-insights`, which has no skills.sh listing of its own.

**Source:** [lignertys/reddit-research-skills](https://www.skills.sh/lignertys/reddit-research-skills) via skills.sh - 46.8K combined installs across 4 indexed listings; first seen Feb 6, 2026 (Oct 26, 2026 sweep)
**GitHub:** [lignertys/reddit-research-skills](https://github.com/lignertys/reddit-research-skills) (15 stars; MIT License; branch main, pushed 2026-09-15; layout `skills/<name>/SKILL.md` for 5 skill directories, plus `scripts/reddapi-cli.sh`, `references/api-examples.md` and `gemini-extension.json`)
**Category:** Research / Reddit Market Research
**Quality Tier:** 🟡 Beta - 46.8K installs across 4 listings but only 15 GitHub stars; every skill needs a paid reddapi.dev key and Free plans get no API access at all; Snyk returns Warn on all three sampled listings; MIT License, last push 2026-09-15

## Installation

The README documents one install command, for the canonical research skill:

```bash
npx skills add https://github.com/lignertys/reddit-research-skills --skill reddit-research
```

The same `--skill` form installs a sibling by name. Confirm the directory exists in the current tree before you rely on it:

```bash
npx skills add https://github.com/lignertys/reddit-research-skills --skill reddit-leads
```

Then set the credentials in the shell that runs the calls. The skill files are explicit that the operator sets these once and the agent never reads or transports the key:

```bash
export REDDAPI_API_KEY=...                          # from https://reddapi.dev/account
export REDDAPI_AUTH="Authorization: Bearer ***"
```

API access requires a paid reddapi.dev plan, and the monthly allowance is a single shared pool across web-app searches, API calls and lead searches: Lite at $19.9/mo gives 500 calls at 50 per minute, Starter at $49 gives 5,000 at 50 per minute, Pro at $99 gives 15,000 at 100 per minute, and Team at $249 gives 50,000 at 200 per minute. The Free plan gets 3 web-app searches and no API access, so a Free key returns HTTP 429 on every call.

There is also a bundled shell wrapper that handles the `Content-Type` header, error hints and trends date defaults. It is optional, since the skills issue their own requests.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| reddapi | 13,535 | The original reddapi.dev search skill: semantic search, vector search with date filters, trends and subreddit discovery, kept live under its first name for existing installs |
| reddit-leads | 11,967 | B2B lead discovery: finds Reddit posts with buying intent, scores them 0 to 100, and classifies each as pain_point, solution_request, complaint, feature_request or comparison |
| reddit-research | 10,688 | The canonical research skill: search by meaning across the archive, then work through playbooks for competitor research, niche validation and trend tracking |
| reddit-search-api | 10,659 | Pure endpoint reference for the same engine: auth, parameters, response schemas and error codes, with no research workflow and no query playbooks |

No indexed listings fall below the threshold; all 4 appear above. The 46,849 combined count is therefore four listings over three capabilities, since `reddapi` and `reddit-research` drive the same engine.

## Why This Matters for Hermes Agents

Most agent research fails on vocabulary. Ask a model what users think about a category and you get a plausible summary of the category, not a quote from someone who hit the problem last week. An index that matches on meaning rather than keywords answers the question that actually matters: "what does frustration with this tool sound like", including posts that never use the word frustrated.

For a builder shipping anything, that is the cheapest source of unfiltered pain language available. Complaint threads are where positioning copy comes from, where feature priority gets argued, and where a competitor's churn shows up before it shows in revenue. The playbooks in `reddit-research` package that as a procedure rather than a vague instruction, so a session can go from "validate this niche" to a set of threads with engagement numbers.

The lead workflow is the part with commercial teeth. `reddit-leads` does not just find discussion, it scores posts for buying intent and labels the lead type, which is what makes a list worth acting on. An agent that can hand back 20 scored prospects with the exact post that triggered the score is doing work that would otherwise take a morning of manual searching.

Two constraints keep this honest. Everything depends on a paid third-party key with a metered pool, so a long research sweep can burn a plan's monthly calls, and the results are other people's unmoderated text: the skill files tell the agent to treat post bodies as data, never as instructions. Both are correct defaults to inherit.

## Usage

| You say | What happens |
|---|---|
| "What are people complaining about in project management tools?" | Loads reddit-research, runs semantic search over the archive and returns matching threads with engagement metrics |
| "Is this niche already served?" | Loads reddit-research's niche validation playbook and looks for unmet needs in the subreddits that discuss the problem |
| "Find discussions about switching away from our main competitor" | Loads reddit-research's competitor playbook and searches for complaints and migration stories by meaning |
| "Has interest in remote work grown this quarter?" | Loads reddit-research or reddit-search-api, uses vector search with a date range and the trends endpoint for named entities with growth versus the previous window |
| "Give me 20 prospects with buying intent" | Loads reddit-leads, pulls posts that express intent, scores each 0 to 100 and labels the lead type |
| "Which subreddits discuss this topic?" | Loads the subreddit discovery endpoints to list and look up subreddits before searching inside them |
| "What are the exact parameters for the trends call?" | Loads reddit-search-api for field names, request shapes and error codes without workflow commentary |

The bundled wrapper mirrors the same calls if you prefer a shell:

```bash
./scripts/reddapi-cli.sh search "productivity tools" --limit 100
./scripts/reddapi-cli.sh search "productivity tools" --start-date 2026-07-01 --end-date 2026-07-30
./scripts/reddapi-cli.sh trends --start-date 2026-07-01 --end-date 2026-07-30
./scripts/reddapi-cli.sh subreddits --limit 50
```

One behavioural detail worth knowing before you prompt: semantic search is the default and returns exact result counts up to a limit of 100, but it takes no date filter. Only vector search supports a date range, which is the mode the CLI switches to automatically when you pass `--start-date` and `--end-date`.

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "reddit-research|reddit-leads|reddapi"
```

Read the skill files before installing. The five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/lignertys/reddit-research-skills/main/README.md
curl -sL https://raw.githubusercontent.com/lignertys/reddit-research-skills/main/SUPPORTING.md
curl -sL https://raw.githubusercontent.com/lignertys/reddit-research-skills/main/skills/reddit-research/SKILL.md
curl -sL https://raw.githubusercontent.com/lignertys/reddit-research-skills/main/skills/reddit-leads/SKILL.md
curl -sL https://raw.githubusercontent.com/lignertys/reddit-research-skills/main/skills/reddit-search-api/SKILL.md
```

The directory listing behind the install index also returned 200 on the same date, and shows the fifth skill directory that carries no listing:

```bash
curl -s https://api.github.com/repos/lignertys/reddit-research-skills/contents/skills | grep '"name"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| reddapi | Pass | Pass | Warn |
| reddit-leads | Pass | Pass | Warn |
| reddit-research | Pass | Pass | Warn |

The security surface is dominated by one decision: the key. Every skill requires `REDDAPI_API_KEY`, and the skill text is unusually careful about it, instructing the agent to reference the key only as an environment variable, never to substitute the value into a command or a file, never to echo it, and never to accept it pasted into chat. That is the right posture, and it means the main risk is operator error rather than skill behaviour.

The only executable in the root is `scripts/reddapi-cli.sh`, which sends requests to reddapi.dev and prints responses; `references/api-examples.md` holds captured request and response pairs for debugging. The unprompted `reddit-insights` directory additionally ships `scripts/reddapi.py` and a test file. Nothing in the sampled skills writes to your repository, and nothing runs until a prompt matches a description.

Snyk returns Warn on all three sampled listings while Gen Agent Trust Hub and Socket both return Pass. Treat the Warn as a prompt to read the files you are actually installing rather than as a blocker, and re-check the verdicts on the skills.sh security pages before you wire any of this into a production agent.

## Limitations

- Third-party paid service, not Reddit official. reddapi.dev requires a paid plan for API access; Free plans get 3 web-app searches and return HTTP 429 on any API call. Rate limits are plan-based and the monthly allowance is one shared pool, so a heavy research sweep competes with lead searches for the same calls.
- The four listings cover three capabilities. reddapi and reddit-research drive the same engine, so the combined 46.8K credits one engine twice and overstates how much distinct functionality the suite adds.
- Index-versus-tree drift. The current tree ships a fifth skill directory, reddit-insights, that has no skills.sh listing and therefore no install count; the four indexed listings all resolve to a directory.
- Snyk returns Warn on all three sampled listings. Gen Agent Trust Hub and Socket both return Pass, so the verdicts disagree, and only reading the SKILL.md files settles it.
- Semantic search carries no date filter. Questions scoped to a date range have to go through vector search, and the two modes return different response shapes.
- Snapshot data, verified Oct 26, 2026: 46,849 combined installs across 4 indexed listings; 15 GitHub stars; MIT License; last pushed 2026-09-15. Counts drift over time.

## Related

- [Reddit Automation - Honest Reddit Engagement Setup](/hermes/skills/catalog/reddit-automation-setup) - the posting and engagement side, once research has told you which threads matter.
- [FlowKit Reddit Automation - Community Engagement Setup](/hermes/skills/catalog/flowkit-reddit-automation-setup) - a second Reddit engagement suite if you want to compare approaches before committing.
- [ScrapeCreators Social Research Skills - Setup Guide](/hermes/skills/catalog/scrapecreators-social-research-setup) - social research beyond Reddit when validation needs more than one platform.
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup) - turn the threads you found into a written research brief.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `reddit-research` and skip `reddapi` unless an existing setup already references the old name. They drive the same engine, and the canonical skill carries the playbooks.
- Pair `reddit-leads` with a scoring threshold in your prompt. The skill returns 0 to 100 scores, and telling the agent to ignore anything under your cutoff saves both reading time and API calls.
- Reach for vector search whenever the question has a date in it. Semantic search is the default and quietly has no date filter, which is the fastest way to get an answer about the wrong year.
- Keep the key in the environment, never in the prompt. The skill files are written to work that way, and pasting the value into chat is the one step they cannot undo.
- Treat post bodies as hostile input when you draft outreach. The lead skill flags this explicitly, because a Reddit post is unmoderated text that can contain instructions aimed at your agent.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
