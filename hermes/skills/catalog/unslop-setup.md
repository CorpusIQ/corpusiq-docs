---
title: "Unslop - De-AI Writing Skill for Agents"
description: "theclaymethod/unslop on skills.sh: 5.6K combined installs across 1 listing; flags AI writing tells and rewrites drafts with voice mimicry."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/unslop-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "writing", "editing", "ai detection"]
---

# Unslop - Setup Guide

**Source:** [theclaymethod/unslop](https://www.skills.sh/theclaymethod/unslop) via skills.sh - 5.6K combined installs across 1 indexed listing; first seen 2026-11-07 (Nov 7 2026 morning sweep)
**GitHub:** 982 stars, no license file at the repository root, branch `main`, last pushed 2026-09-07, one skill at the repository root (`./SKILL.md`) rather than under `skills/`
**Category:** Editing for agents: flags formulaic AI tells, rebuilds drafts under preservation gates and mimics a taught voice
**Quality Tier:** 🟡 Yellow - 982 stars and a serious eval suite, but there is no LICENSE file at the root, Gen Agent Trust Hub returns Fail, and the project's own benchmark result is a no-ship.

Unslop is a writing skill built the way a tooling project is built: a root `SKILL.md`, a `scripts/` directory of standalone Python scanners, an `evals/` suite with a documented benchmark, and `docs/` covering product reasoning. It targets the specific texture of AI-generated prose rather than general quality, and it does so through four commands that separate diagnosis from repair.

The unusual part is the disclosure. The README states plainly that the latest independent public result is a no-ship: the skill improved detection recall and repair over the baseline model it was compared against, but did not meet its own precision, damage or whole-document safety bar. A skill that publishes its failing benchmark is easier to evaluate than one that only publishes claims.

## Installation

The README recommends the skills CLI and documents four invocations, from a single agent to every detected agent:

```bash
npx skills add theclaymethod/unslop -g -a claude-code
npx skills add theclaymethod/unslop -g -a claude-code -a cursor -a codex
npx skills add theclaymethod/unslop -g
npx skills add theclaymethod/unslop --list
```

The `--list` form shows what is available before anything is written to disk, and the bare `-g` form installs to every agent the CLI detects.

The manual route clones the repository and symlinks it into place, with an optional slash-command link:

```bash
git clone https://github.com/theclaymethod/unslop.git ~/dev/unslop
ln -s ~/dev/unslop ~/.claude/skills/unslop
ln -s ~/dev/unslop/SKILL.md ~/.claude/commands/unslop.md
```

Because the skill is the repository root, the symlink points at the directory rather than a subdirectory. The Python scripts run on their own with no third-party dependencies, Python 3.8 or newer and the standard library only, so they can be called from CI or a pre-publish check without loading the skill at all.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| unslop | 5,624 | Four-command editing flow: teach a voice, flag AI tells, rewrite under preservation gates, or mimic the taught voice |

No indexed listings fall below the threshold.

The four commands split the work cleanly. `teach` distills writing samples into a reusable voice under `.unslop/voice/<name>/`. `cleanup` flags AI tells as reviewable suggestions and changes nothing on its own. `rewrite` diagnoses a draft and rebuilds it under the guards, and is the default. `mimic` drafts or rewrites in a taught voice, then has to clear every removal gate.

Behind the commands sit three detection layers. A phrase scanner carries the tells by family: throat-clearing openers, emphasis crutches, significance inflation, negative parallelism, self-answering questions, cliffhanger fragments, vague attribution, business jargon, chatbot residue and em-dash overuse, each marked hard or soft. A structure scanner catches document-shape tells such as uniform sentence rhythm, staccato one-line paragraphs and moralizing codas. A silhouette scanner catches arrangement tells. Every contextual pattern ships with a false-positive row proving the literal sense survives, which is why construction, legal and medical usage does not trip it.

What gets protected is documented just as carefully: register hedges in legal and scientific text, literal domain vocabulary, quoted examples and code fences, and facts with magnitude awareness, so `$47.3M` cannot become `$47.3 billion` and `150 km` cannot become `150 miles`.

## Why This Matters for Hermes Agents

Agents write in a recognizable register, and readers have learned to spot it. The value of this skill is not that it removes particular words; it is that it encodes the constraint an agent normally lacks, which is that the edit must not damage the content.

That constraint is the design center. `cleanup` proposes and changes nothing, `rewrite` runs preservation checks, and `validate_preservation.py --strict` turns a dropped hedge into a hard failure. For documentation, contracts or anything regulated, an editor that silently removes "does not establish causation" is worse than no editor, and the guards are aimed at exactly that failure.

The second value is voice. `teach` builds a stylometric profile from samples, and `mimic` then writes inside it while still passing the removal gates. For a team that publishes under one byline, that is a way to keep generated drafts consistent without hand-editing every paragraph.

The third is that the scanners are usable without the skill. They are standard-library Python that read stdin, so a pre-publish check on a docs tree or a CI step on marketing copy is a shell pipeline rather than an integration. The README also notes the phrase catalog is partly derived from Wikipedia's guide to signs of AI writing, with a sync script that diffs against that page.

The honest caveat is the benchmark. The project's own latest independent result is a no-ship against its precision and safety bar, so treat this as a strong review aid, not an autonomous rewriter for text you will not read.

## Usage

| You say | What happens |
|---|---|
| "Does this read like AI wrote it?" | `cleanup` returns the flagged tells as suggestions with severity, and leaves the file untouched |
| "Rewrite this post so it sounds human" | `rewrite` diagnoses first, then reconstructs the draft and runs the preservation checks |
| "Keep the numbers exactly as they are" | The fact and magnitude guards block numeric, date and unit drift during the rewrite |
| "Write the next post in my voice" | `mimic` drafts inside the profile built by `teach`, then clears the removal gates |
| "Scan this docs folder in CI" | Run `python3 scripts/banned_phrase_scan.py` and `structure_scan.py` over each file without loading the skill |
| "This is legal text, be careful" | `validate_preservation.py --strict` treats a dropped hedge or negation as a hard failure |

## Verification

Read the skill before installing, since it is the whole product. This path returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/theclaymethod/unslop/main/SKILL.md | head -30
```

Expect YAML frontmatter naming the skill, then the audit and two-pass rewrite flow. Because the file sits at the repository root, there is no `skills/unslop/` directory to look for; a raw URL with a `skills/` segment returns 404.

After install, confirm the skill is where your agent scans, then run one scanner directly from the clone to prove the scripts work without any agent in the loop:

```bash
ls .agents/skills/unslop/SKILL.md
printf "Here's the thing: the data tells a story.\n" | python3 ~/dev/unslop/scripts/banned_phrase_scan.py
```

The first command confirms placement. The second should return `total_violations: 2` with one `throat_clearing` hit and one `false_agency` hit, both marked `hard`. Run it from the clone rather than from a copied single file, because the scanner imports a sibling module (`_lang.py`) that lives in the same `scripts/` directory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unslop | Fail | Warn | Pass |

This is the weakest verdict set in the batch and it deserves attention rather than dismissal. Snyk passes, which fits a repository of markdown plus standard-library Python with no dependencies. Gen Agent Trust Hub returns Fail and Socket returns Warn, on a project that also publishes its own no-ship benchmark result and ships a `.github/` workflow set that runs evaluations.

The practical reading is that the flags are a prompt to inspect what you install, not a verdict on whether the writing advice is good. Everything the skill runs is visible: `SKILL.md`, `references/`, and the scripts under `scripts/`, all plain Python. Read `scripts/` before wiring the skill into any pipeline that writes files, and prefer the `cleanup` mode, which changes nothing, for first runs.

Licensing is inconsistent between sources: the README's closing section says "Licensed MIT", while the GitHub repository has no LICENSE file at the root. Treat it as MIT by declaration only until a LICENSE file appears, and do not redistribute the text in a commercial product on that basis alone.

## Limitations

- Snapshot data, verified 2026-11-07: 5,624 combined installs across 1 indexed listing; 982 GitHub stars; no license file; last pushed 2026-09-07. Counts drift over time.
- Gen Agent Trust Hub returns Fail and Socket returns Warn on the sampled skill. Snyk passes. Read the repository's scripts before adopting it.
- The README claims MIT while the repository has no LICENSE file. Licensing is declared in prose, not granted in the repository.
- The project's latest independent benchmark result is a no-ship: recall and repair improved over the baseline, but precision, collateral damage and whole-document safety did not clear the bar. The README says so directly, and it also warns that a clean scan proves nothing about authorship.
- English only. Non-English input gets cheap detection and a decline, and the scanners return a non-English flag and stop, so it is useless for multilingual copy.
- The skill lives at the repository root rather than under `skills/`, so installs and raw URLs that assume a `skills/unslop/` directory fail. The install dump reports the listing name as the root path for the same reason.

## Related

- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [Stop Slop - AI-Prose Pattern Cleaner Setup](/hermes/skills/catalog/stop-slop-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `cleanup`, not `rewrite`. Seeing the flagged tells on an unmodified draft teaches you what the gates are protecting.
- Run `validate_preservation.py --strict` on anything regulated. It converts "please keep the hedges" into a failure you cannot miss.
- Build the voice profile from your own published writing, not from a model's output. A profile trained on generated text reproduces the register you are trying to remove.
- Use the scanners as a CI gate on docs and marketing copy. They read stdin, need no API key and add no dependency to the build.
- Read `evals/CORE-RESULTS.md` before trusting the rewrite path. The failure modes listed there are the ones you will hit.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
