---
title: "Codex Claude Academic Skills - Chinese Research Suite"
description: "zlanqing/codex-claude-academic-skills: 3.3K combined installs across 24 listings, Chinese-first paper writing, academic Office files and MATLAB work"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codex-claude-academic-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "academic", "research", "chinese"]
---

# Codex Claude Academic Skills - Setup Guide

**Source:** [zlanqing/codex-claude-academic-skills](https://www.skills.sh/zlanqing/codex-claude-academic-skills) via skills.sh - 3.3K combined installs across 24 indexed listings; first seen Nov 11, 2026
**GitHub:** 5,928 stars, MIT license, `main` branch, last pushed 2026-05-14, 24 `SKILL.md` files: three top-level skills and 21 reference skills nested under the scientific toolkit
**Category:** Academic writing and research computing for Chinese-language researchers
**Quality Tier:** 🟡 Established - the most-starred repository in this batch by an order of magnitude, with three coherent top-level skills, held back by Chinese-first output, install instructions that still carry placeholder usernames and a tree that has not moved since May 2026.

Three skills that chain. `research-writing-skill` drafts, revises and polishes paper sections, handles the rebuttal and peer-review response, and plans an argument from a vague idea to an outline. `office-academic-skill` produces and edits Word and PowerPoint artefacts: literature reading reports, group meeting slides, proposal, mid-term and defence decks. `scientific-toolkit-skill` runs the computation and the figures: MATLAB and Octave simulation, Python scientific stack, signal processing, statistics, machine learning and publication plots.

The README documents the intended chain explicitly. A paper goes toolkit (analysis and figures), then writing (method and experiment sections), then Office (defence slides). A literature review goes PDF to Word report, then group meeting deck. A simulation study goes toolkit, then writing.

The domain is specific: optoelectronic information science and engineering. The toolkit's references name BOTDR and BOTDA, Brillouin gain spectrum fitting, self-phase modulation, dispersion, noise and deconvolution, plus spectroscopy, detector data, sensor time series, calibration and uncertainty. That specificity is the reason to install it rather than a general academic skill: a model that knows the domain's standard figures and error budget is doing something a generic writing skill cannot.

Under the toolkit sit 21 reference skills, each carrying its own `SKILL.md` and install count, from `citation-management` and `literature-review` to `sympy`, `statsmodels`, `seaborn` and `timesfm-forecasting`. Those are where the index's 24 listings come from; the README markets three.

## Installation

The README's install block uses a placeholder repository path instead of the real one, so clone the repository and copy the folders:

```bash
git clone https://github.com/zlanqing/codex-claude-academic-skills.git
cp -r codex-claude-academic-skills/research-writing-skill ~/.claude/skills/
cp -r codex-claude-academic-skills/office-academic-skill ~/.claude/skills/
cp -r codex-claude-academic-skills/scientific-toolkit-skill ~/.claude/skills/
```

For Codex, the same copy with the Codex skills directory:

```bash
cp -r codex-claude-academic-skills/research-writing-skill ~/.codex/skills/
cp -r codex-claude-academic-skills/office-academic-skill ~/.codex/skills/
cp -r codex-claude-academic-skills/scientific-toolkit-skill ~/.codex/skills/
```

The README also documents a plugin route and a `--plugin-url` route for Codex. Both are written with the placeholder username, so substitute `zlanqing` before running them. Copying the folders is the version that works as written.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| office-academic-skill | 971 | Word and PowerPoint artefacts: reading reports, group meeting slides, proposal, mid-term and defence decks. |
| research-writing-skill | 964 | Paper sections, revision and polishing, rebuttal and peer-review responses, argument planning. |
| scientific-toolkit-skill | 885 | MATLAB, Octave and Python research computing with the domain references and figure templates. |

The remaining 21 indexed listings range from 21 to 24 installs: the reference skills nested inside `scientific-toolkit-skill`, each installable on its own.

## Why This Matters for Hermes Agents

Academic work is a long chain of small format decisions: which section gets a numbered heading, how a figure caption is written, how a reviewer's objection is answered without conceding the result. A general model handles the prose and improvises the rest. This suite encodes the rest for a Chinese-language context that most published skill libraries ignore entirely.

The reference skills are the more portable half. `citation-management`, `literature-review`, `statistical-analysis` and `scientific-visualization` are not China-specific, and they sit inside the toolkit where an agent can load them individually. If the top-level writing skills do not fit your conventions, the 21 references still might.

The specific domain knowledge is the differentiator. Brillouin sensing and optoelectronic measurement have a standard set of plots, a standard uncertainty treatment and a standard way of presenting a fitted spectrum. Getting the figure right is most of the credibility of a paper in that field.

The star count suggests the repository is being used well beyond its install numbers, which is worth noting when you weigh 971 installs against a competing skill that nobody starred.

## Usage

| You say | What happens |
|---|---|
| "Draft the methods section from these experiment notes" | Loads `research-writing-skill` and drafts in the paper's section order from the notes. |
| "Turn this PDF into a reading report" | Loads `office-academic-skill` and produces a Word report with the standard section layout. |
| "Build my group meeting slides for this week" | Loads `office-academic-skill` and produces the deck skeleton with figures and speaking notes. |
| "Fit this Brillouin gain spectrum and plot the result" | Loads `scientific-toolkit-skill` and applies the domain fitting routine with a publication figure. |
| "Answer these reviewer comments" | Loads `research-writing-skill` and drafts a point-by-point rebuttal in the response format. |
| "Run the statistics and make the figures" | Loads `scientific-toolkit-skill` with `statistical-analysis` and `seaborn` from the references. |
| "Collect the citations for this paragraph" | Loads `citation-management` from the toolkit references and formats the entries for the target journal. |

## Verification

Confirm both top-level skills are reachable on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/zlanqing/codex-claude-academic-skills/main/research-writing-skill/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zlanqing/codex-claude-academic-skills/main/scientific-toolkit-skill/SKILL.md
```

Check the nested references survived the copy, since the toolkit expects them under `references/scientific-skills/`:

```bash
ls ~/.claude/skills/scientific-toolkit-skill/references/scientific-skills | head
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| office-academic-skill | Pass | Pass | Pass |
| research-writing-skill | Pass | Pass | Pass |
| scientific-toolkit-skill | Pass | Warn | Pass |
| citation-management | Pass | Pass | Pass |
| statistical-analysis | Pass | Pass | Pass |

The Socket Warn on the toolkit is the expected shape for a skill that installs scientific Python packages and shells out to MATLAB or Octave. Treat what it installs as code, not as text: pin the package versions, and run it in an environment you can throw away. The writing and Office skills are instruction files and carry no execution risk beyond the documents you feed them.

## Limitations

- Snapshot data, verified 2026-11-12: 3,272 combined installs across 24 indexed listings; 5,928 GitHub stars; MIT license; last pushed 2026-05-14. Counts drift over time.
- The install instructions in the README still carry a placeholder repository path in the clone, plugin and `--plugin-url` commands. They fail as written; substitute `zlanqing` or use the copy route above.
- The skills write Chinese by default. Prompts, section conventions and reviewer responses assume a Chinese-language manuscript.
- The tree has not moved since May 2026. Package installs inside `scientific-toolkit-skill` follow whatever the README pins today, which is not the same as a lockfile.
- Twenty-one of the 24 listings are nested reference skills rather than top-level installs. Removing the toolkit removes them all.
- The domain focus is narrow by design. If your field is not optoelectronics or a neighbouring measurement discipline, the toolkit's references are less relevant than the general Python ones.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy all three folders. The three skills pass work to each other, and a lone `research-writing-skill` loses the figure and statistics context the other two provide.
- Check `references/scientific-skills/` after installation. The toolkit degrades quietly if the nested references did not come along.
- Pin the Python and MATLAB versions before the first run. A domain fitting routine that depends on an unpinned library is a reproducibility problem waiting for a deadline.
- Use `citation-management` on one paragraph first. Citation formatting is where a wrong reference style is most expensive to fix later.
- Hand the writing skill your own outline rather than an empty page. It polishes structure you already committed to and invents structure when you give it none.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
