---
title: "Tushare Finance Skill - China Market Data for Agents"
description: "stanleychanh/tushare-finance-skill: 5.2K combined installs. One skill wrapping 220+ Tushare Pro interfaces for A-share, fund, futures and macro data."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tushare-finance-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "china market", "tushare"]
---

# Tushare Finance Skill - Setup Guide

**Source:** [stanleychanh/tushare-finance-skill-for-claude-code](https://www.skills.sh/stanleychanh/tushare-finance-skill-for-claude-code) via skills.sh - 5.2K combined installs across 1 indexed listing; first seen 2026-11-01 (evening sweep)

**GitHub:** [stanleychanh/tushare-finance-skill-for-claude-code](https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code) - 79 stars, MIT, branch master, last pushed 2026-10-26; 1 `SKILL.md` at the repository root, with `QUICK_REFERENCE.md`, `reference/`, `scripts/`, `metadata.json` and `requirements.txt` beside it

**Category:** China market data for agents: 220+ Tushare Pro interfaces covering A-shares, funds, futures and macro

**Quality Tier:** 🟡 Yellow - the sampled skill carries a Socket Fail, which is enough to hold it below green even though the licence is clear and the other two auditors pass

The skill wraps Tushare Pro, the commercial data API most of the Chinese market already uses for A-share prices, financial statements, index data, fund NAVs, futures, bonds and macro series. One skill covers all of it because the surface it exposes is an index rather than a procedure: `reference/` holds 220 per-interface Markdown files scraped from the official documentation, `reference/README.md` maps categories to interface names, and `SKILL.md` tells the agent to find the interface, read its page, then call it through `tushare` in Python.

The packaging follows the OpenClaw skill convention. `SKILL.md` declares `allowed-tools` of `Bash(python:*)` and `Read`, `metadata.json` states the runtime requirement as `python3` plus a `TUSHARE_TOKEN` environment variable, and `requirements.txt` pins `tushare>=1.2.60` and `pandas>=1.5.0`. Results come back as pandas DataFrames, and `scripts/api_client.py` wraps the common calls in a `TushareAPI` class with date normalisation and CSV, JSON or Excel export.

The documentation ships with the skill and updates itself. A GitHub Actions workflow runs every Monday at 10:00 CST, logs into tushare.pro with Playwright, solves the login captcha with ddddocr, crawls the 220 interface pages, compares them by SHA256 and opens a pull request for anything that changed. That is why the `reference/` tree is worth 220 files rather than a link: the agent reads the parameter list locally instead of fetching a page mid-task.

The README, `SKILL.md`, `metadata.json` and every reference page are in Chinese. That is not a problem for the agent, which reads them fine, but it does change how you should phrase requests and where you should look when something goes wrong.

## Installation

ClawHub is the recommended route in the README:

```bash
clawhub install tushare-finance
```

The manual route clones the repository, installs the two runtime dependencies and expects a token in the environment:

```bash
git clone https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code.git
cd Tushare-Finance-Skill-for-Claude-Code
pip install -r requirements.txt
export TUSHARE_TOKEN="your_token_here"
```

The token comes from tushare.pro after registering an account; it is shown in the account centre and is the only credential the skill needs. Nothing else in the repository is configured at install time.

For Hermes, copy the skill into the profile and keep the tree intact, because `SKILL.md` resolves the reference and script paths relatively:

```bash
cd ~/.hermes/profiles/corpusiq/skills
git clone https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code.git tushare-finance
```

That leaves the repository in place at `tushare-finance/`, with `SKILL.md` at its top level, so the relative paths inside the skill resolve without further surgery. If you would rather not keep a git checkout inside the skills directory, clone somewhere else and move the working files across from the clone root:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/tushare-finance
cp -R reference scripts SKILL.md QUICK_REFERENCE.md requirements.txt \
  ~/.hermes/profiles/corpusiq/skills/tushare-finance/
```

Either way the token belongs in the environment the agent runs in, not in the skill directory. Export it in the profile's shell environment or the unit file that starts Hermes, so a repository copy never carries a live credential.

```bash
python -c "import tushare, pandas; print('OK')"
```

That import check is the one the `SKILL.md` asks for first, and it separates a missing dependency from a missing token before you spend a call on the API.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tushare-finance | 5,157 | China market data through Tushare Pro: A-share daily prices and financial statements, index quotes and weights, fund NAVs, futures and options, bonds, HK and US quotes, and macro series such as GDP, CPI, PMI and Shibor, each looked up in the bundled 220-interface reference before the call. |

All 1 indexed listing appears in the table above; the only row is 5,157 installs.

## Why This Matters for Hermes Agents

The hard part of China market data for an agent is not the query syntax, it is the interface name. Tushare exposes hundreds of them, each with its own parameters and its own column set, and a model that guesses produces a plausible function name and a traceback. This skill replaces the guess with a lookup: `reference/README.md` lists the interfaces by category with counts, and each interface has a page with its parameters and return fields. An agent that reads the page first writes a call that works.

The bundled index matters for a second reason. Tushare documentation lives behind a login, so an agent cannot fetch it mid-task without a session, and a web search returns stale blog posts. Here the 220 pages are local Markdown, refreshed weekly by the repository's own crawler, so the parameter list the agent reads is the same one the maintainer last validated.

The output contract is uniform. Every call takes `ts_code` identifiers such as `000001.SZ` and `YYYYMMDD` dates, and returns a pandas DataFrame, which is what makes chained work safe: pull daily bars for a list of codes, compute a metric, export to CSV, and each step is ordinary pandas rather than a bespoke parser per endpoint. `scripts/api_client.py` covers the common shapes directly, with `get_stock_daily`, `get_stock_info`, `get_stock_list`, `get_financial_indicator`, `get_income_statement`, `get_index_daily`, `get_index_weight`, `batch_query` and `export_data`.

The honesty is in the constraints. `TushareAPI` refuses to initialise without a token and tells the caller where to get one, rather than failing later inside an HTTP call. That one check turns a confusing empty result into a clear instruction, which is the behaviour you want from a skill an unattended cron might invoke.

## Usage

| You say | What happens |
|---|---|
| "Pull Ping An Bank daily bars for 2024" | The skill opens the daily-quote interface page, then calls `api.get_stock_daily("000001.SZ", "2024-01-01", "2024-12-31")` and returns a DataFrame with the date format normalised to `YYYYMMDD`. |
| "Compare three bank stocks over the same window" | It uses `batch_query` with the code list, keeping one frame per code or a concatenated frame, instead of issuing three separate tool turns. |
| "What did the income statement look like last year" | It reads the corresponding interface page for the parameter names, then calls `pro.income(ts_code=..., start_date=..., end_date=...)` directly or through `get_income_statement`. |
| "Show the Shanghai composite index for 2024" | It calls `get_index_daily` for `000001.SH`, and can pull index weights with `get_index_weight` when the question is about constituents rather than the level. |
| "Save that table as a spreadsheet" | It calls `export_data` with `format="excel"` for `.xlsx` or `format="csv"` for a flat file, writing next to the project rather than into the skill directory. |
| "Which interface gives ETF minute bars" | It searches the bundled index and interface pages for the matching endpoint and answers with the interface name and its parameters before writing any code. |
| "Add GDP and CPI to the macro sheet" | It looks up the macro category, calls the GDP and CPI interfaces, and appends both frames to the existing export. |

## Verification

Four paths in the repository returned 200 on the `master` branch when this guide was written. The branch matters: a raw URL with `main` in it will fail here.

```bash
for p in SKILL.md QUICK_REFERENCE.md reference/README.md scripts/api_client.py; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/master/$p"
done
```

The two files to read first are the skill definition and the fast reference, because one sets the data-fetch procedure and the other is the shortcut list for the most common interfaces.

- https://raw.githubusercontent.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/master/SKILL.md
- https://raw.githubusercontent.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/master/QUICK_REFERENCE.md

After the copy, confirm the tree is complete. The per-interface directory should hold 220 pages, and `find` should count 221 Markdown files once `reference/README.md` is included:

```bash
find ~/.hermes/profiles/corpusiq/skills/tushare-finance/reference -name '*.md' | wc -l
ls ~/.hermes/profiles/corpusiq/skills/tushare-finance/scripts
```

Then check the token without printing it, and make one small call that proves the credential works:

```bash
test -n "$TUSHARE_TOKEN" && echo "token set"
python -c "from scripts.api_client import TushareAPI; print(TushareAPI().get_stock_info('000001.SZ'))"
```

That second command has to run from the skill directory, since `scripts` is imported as a local package. A `ValueError` mentioning `TUSHARE_TOKEN` means the environment did not reach the process; an authentication error from the API means the token is present but not accepted.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tushare-finance | Pass | Fail | Pass |

The Socket Fail is the finding that sets the tier, and it is the one to read on skills.sh before this goes anywhere near an unattended job. Gen Agent Trust Hub and Snyk both pass, so the sample is split rather than unanimously bad, but a Socket Fail on a skill that executes Python through `Bash(python:*)` deserves a look at the specific rule that fired.

The most likely candidate sits in the repository's tooling rather than its data path. `scripts/crawl_docs.py` drives Playwright through a login on tushare.pro, fills the account credentials from `TUSHARE_ACCOUNT` and `TUSHARE_PASSWORD`, and solves the captcha with ddddocr before crawling 220 pages. That workflow runs in GitHub Actions on the maintainer's repository with repository secrets, not on your machine, and it is not invoked by `SKILL.md`. It is still the part of the codebase that handles a password and bypasses a bot check, and scanners tend to notice.

The data path is narrower. `scripts/api_client.py` reads `TUSHARE_TOKEN` from the environment or takes it as an argument, raises before any network call when it is missing, and passes it to `ts.pro_api`. No token is written to disk, and the only endpoint the client reaches is Tushare itself through that library, with `export_data` writing to the path you name.

The permission surface is the other item to weigh. `SKILL.md` declares `allowed-tools` of `Bash(python:*)` and `Read`, which is broad: any Python the agent writes can run under it. If your Hermes profile enforces tool approval, that is the setting that decides what this becomes, and a skill is not a sandbox.

Treat the bundled reference pages as untrusted text. They are scraped copies of a third-party site committed to the repository, so an agent that reads 220 pages to find an interface is reading text nobody audited. Ask for a specific interface by name where you can, rather than letting the agent page through the whole directory.

## Limitations

- Snapshot data, verified 2026-11-01: 5,157 combined installs across 1 indexed listing; 79 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- One skill, not a suite. The 220 entries under `reference/` are documentation pages for interfaces, not separate skills, so the entire capability arrives as a single listing with a single set of trigger phrases.
- Everything is written in Chinese: `README.md`, `SKILL.md`, the skill description in its frontmatter, `QUICK_REFERENCE.md` and all 220 interface pages. Requests phrased in English usually route correctly once the description is loaded, but expect Chinese parameter names and Chinese error text in the returned pages.
- The licence metadata disagrees with itself. The LICENSE file is MIT, which the pack reflects, while the README badge and `metadata.json` both declare Apache-2.0. Follow the LICENSE file and fix the other two before redistributing.
- The README advertises a command line tool and batch export, but `scripts/` holds only `api_client.py` and `crawl_docs.py`. The `__main__` block in `api_client.py` is a two-call demo, not an argument parser, so the CLI route is the README's ambition rather than shipped code.
- The dependency pins drift between files. `requirements.txt` asks for `tushare>=1.2.60` and `pandas>=1.5.0`, while `metadata.json` asks for `tushare>=1.3.0`, `pandas>=2.0.0` and `openpyxl>=3.1.0`. Excel export needs `openpyxl`, and `requirements.txt` does not install it, so `pip install -r requirements.txt` then `format="excel"` will fail until you add it.

## Related

- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Wind Skills - Financial Terminal Research Cluster Setup](/hermes/skills/catalog/wind-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the interface name before the code. The bundled index answers "which endpoint gives futures daily bars" in one read, and the agent stops inventing method names.
- Quote `ts_code` values in full, `000001.SZ` and `600000.SH`, with the exchange suffix. The suffix is what disambiguates Shanghai from Shenzhen, and a bare six-digit code returns nothing useful.
- Keep the date format explicit. The client normalises `YYYY-MM-DD` to `YYYYMMDD`, but the raw `pro.*` calls do not, so mixed formats inside one session produce silently empty frames.
- Use `batch_query` or a single `pro.daily(trade_date=...)` call instead of a loop over codes. It is one request against the API instead of dozens, which matters when request count is metered.
- Put the token in the process environment for scheduled runs and rotate it like any other key. A cron that reads the token from a file inside the skill directory is one `git add` away from a leak.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
