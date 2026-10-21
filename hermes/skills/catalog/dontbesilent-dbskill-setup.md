---
title: "Dontbesilent dbskill - 35-Skill Business Toolkit Setup"
description: "dontbesilent2025/dbskill: 725.5K combined installs across 44 listings. 35 Chinese business diagnosis, content and decision skills behind a router."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dontbesilent-dbskill-setup/"
robots: "index,follow"
last_updated: "2026-10-21"
tags: ["hermes skill", "agent skill", "skill setup", "business diagnosis", "content operations", "chinese"]
---

# Dontbesilent dbskill - Setup Guide

**Source:** [dontbesilent2025/dbskill](https://www.skills.sh/dontbesilent2025/dbskill) via skills.sh - 725.5K combined installs across 44 indexed listings; first seen Jul 4, 2026
**GitHub:** [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) (10,831 stars; README and LICENSE state CC BY-NC 4.0 while the GitHub API reports NOASSERTION; pushed 2026-10-19; version 3.0.1; repo layout: 35 directories under `skills/`, each holding its own SKILL.md, plus a `.claude-plugin/marketplace.json` declaring 35 plugin entries)
**Category:** Business Operations / Content and Decision Support
**Quality Tier:** 🟡 Beta - 10.8K-star Chinese business and content toolkit with a router entry; sampled verdicts are two clean Pass triples and one MEDIUM Snyk third-party-content warning; the CC BY-NC 4.0 license rules out commercial use without the author's permission

dbskill is a Chinese-language business toolbox built by the writer [@dontbesilent](https://x.com/dontbesilent). It turns 16,152 of his public posts into 4,176 knowledge atoms and then wraps them as 35 agent skills, so the agent is applying a specific operator's method rather than general advice. Every skill answers one recurring small-business question: is this business problem real, which peer is worth copying, why did this customer not renew, will this post get flagged, what is the first thing to do tomorrow.

What separates it from most large skill packs is the router. `/dbs` is a dispatcher: it reads the outcome you want, picks the smallest set of skills that reaches it, and tells you the arrangement before running anything. The README documents six arrangements, from single-skill use through sequential chains to parallel comparison. Every skill also saves and restores state through `dbs-save` and `dbs-restore` into `~/.dbs/`, which is what lets a diagnosis continue across sessions instead of restarting from zero.

## Installation

```bash
# Install the whole suite globally through the Skills CLI
npx -y skills add dontbesilent2025/dbskill -g --all

# Install to a single agent instead (drop --all and pick from the prompt)
npx -y skills add dontbesilent2025/dbskill -g
```

```bash
# Or use the Claude Code plugin marketplace
claude plugin marketplace add dontbesilent2025/dbskill
claude plugin install dbs@dontbesilent-skills

# A single skill from the same marketplace
claude plugin install dbs-diagnosis@dontbesilent-skills
```

Plugin installs prefix commands with `dbs:`, so the entry point becomes `/dbs:dbs` and a skill becomes `/dbs:dbs-diagnosis`. Skills CLI installs use the short form, `/dbs` and `/dbs-diagnosis`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| dbs | 29,768 | Router: reads the goal, picks and orders the skills, states the plan first, and resolves three-digit codes handed out in the author's videos |
| dbs-content | 29,079 | Turns an already-decided topic into a content plan: format, platform, structure, argument, expression |
| dbs-diagnosis | 28,928 | Decides whether one complaint is a real business problem or runs a full business checkup, ending in tomorrow's first action |
| dbs-benchmark | 28,886 | Five-filter search for peers worth imitating, then extracts their acquisition, conversion and delivery mechanics |
| dbs-deconstruct | 28,787 | Splits a vague business concept apart, clarifying boundaries and catching mixed-up terms |
| dbs-action | 28,002 | Diagnoses why you know what to do and still do not do it, then names today's single step |
| dbs-hook | 27,292 | Diagnoses the opening of a short video and rewrites it to cut early drop-off |
| dbs-ai-check | 26,296 | Flags AI writing tells in copy, reporting only by default and rewriting item by item on request |
| dbs-chatroom | 25,999 | Simulated multi-expert discussion of one topic, closing with a summary of where the experts disagreed |
| dbs-chatroom-austrian | 25,880 | The same discussion run from the Hayek and Mises Austrian-economics viewpoint |
| dbs-xhs-title | 25,775 | Selects from 75 validated Xiaohongshu title formulas and generates titles for a given post |
| dbs-agent-migration | 25,236 | Audits project rule files, finds the real source of truth, unifies naming and generates bridges so one project works across Claude Code, Codex, Grok and generic agents |
| dbs-report | 24,649 | Merges several saved diagnoses into one deliverable Markdown report |
| dbs-save | 24,617 | Saves the current conclusions and next step to `~/.dbs/` so a later session can continue |
| dbs-restore | 24,609 | Reloads the most recent save and resumes an unfinished diagnosis |
| dbs-goal | 24,491 | Turns a vague wish into targets with constraints, boundaries and acceptance criteria |
| dbs-learning | 23,356 | Breaks a subject into a sequence of learning articles, adjusting depth and angle per response |
| dbs-good-question | 23,052 | Rewrites a fuzzy question into a specification an agent can reason over, and judges how much of it is automatable |
| dbs-decision | 22,370 | Opens a local decision ledger for long-horizon business, career or investment calls, then backfills outcomes and reviews |
| dbs-content-system | 21,206 | Rebuilds old drafts, posts, topics and course notes into a reusable content asset with a topic map |
| dbs-slowisfast | 19,216 | Separates the steps where speed is expensive from the steps where friction pays, and designs a compounding path |
| dbs-resonate | 18,080 | Finds where a finished draft fails to land with its audience, with line-level cuts and rewrites |
| dbs-spread | 18,058 | Explains why an existing piece resonated or was shared: mechanism, stance, audience motive |
| dbs-wechat-html | 17,514 | Converts Markdown into WeChat Official Account HTML across 15 built-in styles |
| dbs-script-flow | 16,804 | Checks a short-video script's transitions and spoken flow and marks where viewers will leave |
| dbs-update | 15,350 | Updates the official package while preserving user archives and removing retired skills |
| dbs-knowledge | 14,066 | Turns a local folder into a knowledge base an agent can search and maintain, with navigation, version checks and a health check |
| dbs-standard-answer | 12,032 | Researches the theory and the historical cases first, then answers with a conditional standard answer |
| dbs-content-risk-check | 9,476 | Sentence-level moderation risk check before publishing, naming the smallest safe edit |
| dbs-bridge | 8,982 | Symlinks any skill directory into Claude Code and Codex skill folders so one source stays in sync across agents |
| dbs-skill-cleaner | 8,673 | Audits installed skills for ad funnelling, hidden commercial intent, task hijacking, suspicious external calls and sensitive data reads |
| dbs-jtbd | 8,485 | Jobs to Be Done analysis of why a customer chooses or abandons a product |
| dbs-install-skill | 7,748 | Installs one skill or a whole set into Hermes Agent, Claude Code, Codex, WorkBuddy, Grok, Kiro, Qwen Code and Cline, then cleans duplicate entries |
| dbs-skill-maker | 7,215 | Builds or repairs a skill: plan first, then prove the change on a real task |
| dbs-video-extract | 6,383 | Pulls post and account data plus transcripts from Douyin, Xiaohongshu and WeChat Channels links, filing them as Markdown; needs TikHub and Qingdou credentials |
| dbs-theory-grounding | 5,281 | Checks the claims in a course or deck against credible theory and names the source |
| dbs-content-value | 3,234 | Judges who a topic attracts, whether the opening holds, and its likely reach and commercial value |
| dbs-title-cover-intro | 1,970 | Writes titles, cover text and openings for Xiaohongshu, Bilibili, Douyin and WeChat Channels |
| dbs-video-navigation | 1,931 | Chapters a local video and exports a navigation-bar MP4 plus a timeline for the editor |
| chatroom-austrian | 1,886 | Bare-name alias listing for the Austrian-economics chatroom skill |
| dbs-human-dispatch | 1,800 | Assigns a task to a staff member or collaborator, agrees a deadline, then verifies the reported result |
| dbskill-upgrade | 1,748 | Older upgrade entry point, superseded by dbs-update |
| dbs-plain-writing | 699 | Writes or checks product and feature documentation in fact order under ASD-STE100 clear-writing rules, with no marketing hooks |
| dbs-unblock | 628 | Execution-block self-check that separates a knowledge gap from a willingness gap |

All 44 indexed listings clear the 500-install threshold, so every row is in the table above. Eight of them (dbs-hook, dbs-xhs-title, dbs-agent-migration, dbs-slowisfast, dbs-skill-cleaner, dbs-bridge, dbs-unblock, dbskill-upgrade) carry installs but have no directory in the current `skills/` tree; their descriptions were read from the last commit that contained them.

## Why This Matters for Hermes Agents

Most business-skill packs are prompt libraries: a hundred ways to ask for a marketing plan. dbskill is closer to a method with a scheduler, which is the part an agent actually needs. The router decides the sequence before spending tokens, the skills hand each other intermediate artifacts, and `dbs-save` plus `dbs-restore` give a Hermes agent continuity that its own context window does not. That combination turns a multi-session diagnostic conversation into something you can resume by name.

The second reason is breadth of judgment rather than breadth of topics. Several skills encode decisions agents usually get wrong: `dbs-skill-cleaner` audits installed skills for ad funnelling and hidden commercial intent, `dbs-content-risk-check` runs a sentence-level platform moderation check before publishing, and `dbs-install-skill` explicitly lists Hermes Agent among its install targets. If you run a local skill library, the cleaner and the bridge are the two worth installing even if you never touch the content skills.

The third is the corpus. The knowledge base ships as data (`atoms.jsonl`, 4,176 atoms distilled from 16,152 public posts) alongside the skills, so retrieval can be grounded in a named body of work instead of the model's aggregate. Read the non-commercial license first: this is a method you can study and run for yourself, not a package to resell or embed in a paid product.

## Usage

| You say | What happens |
|---|---|
| "/dbs <your situation and question>" | The router picks a diagnosis path, states the arrangement, then runs the checkup and returns tomorrow's first action. Prompts are written in Chinese, for example: /dbs 我的少儿编程课续费率很低，先查产品、定价还是客户匹配 |
| "/dbs-diagnosis <one problem plus your numbers>" | Runs the single-problem branch: confirms whether the complaint is the real problem and what to verify next. Example in Chinese: /dbs-diagnosis 客单价 3,000，最近 10 个咨询里 6 个说贵 |
| "/dbs-benchmark find peers worth copying" | Applies the five filters, discards peers whose differences make the comparison noise, and extracts their acquisition and delivery moves. |
| "/dbs-content then /dbs-content-risk-check on the draft" | Produces the plan, then checks the finished draft sentence by sentence for platform risk with the minimum edit for each hit. |
| "/dbs-ai-check, then paste the copy" | Reports AI writing tells without rewriting, then asks about intent before changing anything. |
| "/dbs-save, then /dbs-restore next week" | Writes the conclusions and next step to `~/.dbs/`, and reloads them in a fresh session. |
| "/dbs-skill-cleaner audit my local skills" | Scans installed skills for advertising, hidden commercial intent, task hijacking and sensitive data reads, reporting only. |
| "/dbs-install-skill install this pack into Hermes Agent" | Installs a single skill or a whole set across the supported agents and removes duplicate entry points. |

## Verification

Confirm what the CLI installed:

```bash
npx skills list | grep -i dbs
```

Review the router and the installer before running either. Both URLs below returned 200 when checked on Oct 21, 2026:

```bash
curl -sL https://raw.githubusercontent.com/dontbesilent2025/dbskill/main/skills/dbs/SKILL.md
curl -sL https://raw.githubusercontent.com/dontbesilent2025/dbskill/main/skills/dbs-install-skill/SKILL.md
```

Check that the archive directory was created after the first `/dbs-save`:

```bash
ls -la ~/.dbs/
```

## Security

skills.sh verdicts for sampled skills (verified Oct 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dbs | Pass | Pass | Warn |
| dbs-diagnosis | Pass | Pass | Pass |
| dbs-install-skill | Pass | Pass | Pass |

The one warning is specific and worth reading. Snyk's audit of `dbs` (Oct 18, 2026) rates risk MEDIUM under W011, third-party content exposure with an indirect prompt-injection risk, because the router fetches numbered prompt catalogs from a GitHub repository by way of raw.githubusercontent.com, and repository contributors can change those files. That is the same exposure class as any skill that reads remote content: the agent is executing material it did not author. If you use the numbered video codes, pin the source or skip that feature. The two other sampled skills are clean on all three scanners, and no sampled verdict indicates malware.

The non-commercial license is the harder constraint. CC BY-NC 4.0 permits personal study, research and non-commercial use with attribution; commercial use requires written permission from the author.

## Limitations

- The suite is Chinese-first. The README ships English, Japanese, Korean and Traditional Chinese translations, but skill instructions and knowledge packs are written in Chinese, so the agent reads and answers in Chinese unless you add your own translation layer.
- Eight indexed listings have no counterpart in the current `skills/` tree, including three with more than 19,000 installs (dbs-hook, dbs-xhs-title, dbs-agent-migration, dbs-slowisfast). They may return in a later release; the install index outruns the repo today.
- The advertised skill count drifts inside the project itself: the README says 34 skills, `marketplace.json` describes 34 current plus 2 compatibility and 1 update entry, and the tree holds 35 SKILL.md files. Count your installed skills instead of trusting any of the three.
- License is CC BY-NC 4.0 per the README and LICENSE file, while the GitHub API reports NOASSERTION. Treat it as non-commercial until the author says otherwise, and do not ship it inside a paid product.
- `dbs-video-extract` needs third-party credentials (TikHub, Qingdou) and sends platform links to those services; skip it if your data cannot leave the machine.
- The bundled corpus (books, `知识库/atoms.jsonl`, per-skill knowledge packs) is repository reference material, not part of the install, so retrieval over it needs its own pipeline.
- Snapshot data, verified Oct 21, 2026: 725,537 combined installs across 44 indexed listings; 10,831 GitHub stars; CC BY-NC 4.0; last pushed 2026-10-19. Counts drift over time.

## Related

- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - a Western planning framework that pairs with the content skills here.
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup) - copywriting and paid-acquisition skills to complement the diagnosis side.
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup) - background for reading and editing what dbs-skill-maker produces.
- [find-skills - Skill Discovery Tool Setup](/hermes/skills/catalog/find-skills-setup) - how this suite was found, and how to keep finding successors.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/dbs` rather than a named skill. The router is the product; picking skills by hand is how you end up with three overlapping answers.
- Run `/dbs-save` at the end of every session. Continuity into the next session is the difference between a one-off answer and an actual diagnosis.
- Install `dbs-skill-cleaner` on its own even if you skip the rest. Auditing local skills for hidden commercial intent is cheap insurance for any agent library.
- Give the diagnosis skills real numbers (price, headcount, conversion, churn) in the first message. The method asks for evidence, and a number-free prompt returns a number-free answer.
- Use `dbs-plain-writing` on your own product docs. It applies ASD-STE100 rules and strips marketing framing, which is a useful counterweight to content-tuned models.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
