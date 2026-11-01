---
title: "Shenzjd Skills - DevOps and AI Image Pack"
description: "wu529778790/shenzjd-skills: 7.9K combined installs. Eight agent skills for Docker CI/CD, dependency audits, git hooks and AI image generation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shenzjd-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "devops", "docker", "image generation"]
---

# Shenzjd Skills - Setup Guide

**Source:** [wu529778790/shenzjd-skills](https://www.skills.sh/wu529778790/shenzjd-skills) via skills.sh - 7.9K combined installs across 16 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [wu529778790/shenzjd-skills](https://github.com/wu529778790/shenzjd-skills) - 4 stars, MIT, branch main, last pushed 2026-09-25; 8 `SKILL.md` files, one per directory at the repository root rather than under a `skills/` folder, several with `templates/` or `scripts/` subfolders, plus a README in English and a `README.zh.md`

**Category:** DevOps pipeline and AI asset generation skills for coding agents, written mostly in Chinese

**Quality Tier:** 🟡 Yellow - Snyk fails two of the three sampled skills (docker-build-deploy and git-hooks-setup, both code E005) while Gen Agent Trust Hub and Socket pass on all three

The README opens with a claim and a coverage map: "7 production-ready AI skill modules. One-line install, covering the core DevOps pipeline and AI image generation." The module table directly below it lists eight, and the tree holds eight skill directories, so the blurb lags its own table by one. The coverage map is the more useful document, because it shows the pack as a chain rather than a list: code, commit, git hooks, commit conventions, build, Docker CI/CD, deployment, then dependencies, security audit, licence compliance, then assets into a GitHub figure bed and out as CDN links, then inspiration into free image generation.

Every skill uses the same shape. The frontmatter description is written as a trigger sentence ("Use when ..."), the body opens with Overview, then When to Use and When NOT to Use, then a numbered Core Pattern carrying shell snippets and template files, then Quick Reference and a Common Mistakes table. The mistake tables are the part that reads as earned rather than generated: `npm audit` exits non-zero when it finds vulnerabilities so the count has to come from `--json`, a pre-commit hook should not run `git add -u` because that sweeps in unstaged work, keyword grep for `token` and `secret` produces mostly false positives so gitleaks or high-confidence patterns are the fallback, and a deploy workflow needs a `${{ github.sha }}` tag alongside `latest` or there is nothing to roll back to.

The bodies are bilingual rather than translated. Step headings, rationale and warnings are Chinese, while the trigger lists, parameter tables and frontmatter descriptions are English, which is why an English-only reader can still route to the right skill. Eight of the sixteen indexed listings have no directory in the tree at all, so the installable surface is half the index and the table below is split accordingly.

## Installation

The README documents both an all-skills install and a per-skill install through the skills CLI:

```bash
npx skills add wu529778790/shenzjd-skills --all -y
npx skills add wu529778790/shenzjd-skills -s docker-build-deploy -y
```

Both forms are quoted from the README, which also repeats the per-skill line for each of the eight directories. Note the flag: this repository uses `-s <skill>`, not `--skill`. If you would rather pin one skill into a Hermes profile without the CLI, copy the directory directly, remembering that the skills sit at the repository root and not under a `skills/` folder:

```bash
git clone --depth 1 https://github.com/wu529778790/shenzjd-skills.git /tmp/shenzjd-skills
cp -r /tmp/shenzjd-skills/docker-build-deploy ~/.hermes/profiles/corpusiq/skills/
```

That clone and copy is our route, not the project's; the README only documents the CLI. Two skills carry prerequisites worth checking before you rely on them. `github-figure-bed` drives the GitHub Contents API through `gh api`, so `gh` has to be installed and authenticated, and its `scripts/setup.sh` walks through login, owner detection and repository creation on first use. `video-cover-packager` shells out to `python3 scripts/add-title.py` to composite cover text over a generated base image, so it needs a Python 3 interpreter on the machine that runs it. `freeimg-hunyuan` installs the Tencent `@cloudbase/node-sdk` into `~/.freeimg-hunyuan/sdk` on its first run, which means node and npm and a network path to the npm registry.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| docker-build-deploy | 1,050 | Generating a multi-stage Node.js Dockerfile plus a GitHub Actions workflow that builds, pushes to GHCR and deploys over SSH, with a ten-row mistake table covering tags, permissions, caching and rollback. |
| dependency-audit | 1,006 | Auditing npm, yarn, pnpm, pip, Go and Cargo dependencies for CVEs, outdated packages and copyleft licences, then writing a severity-ranked report with fix commands. |
| git-hooks-setup | 1,000 | Wiring husky or native git hooks for lint-staged formatting, commitlint message rules and gitleaks secret scanning, with a documented objection to keyword-based secret grep. |
| db-migration-helper | 997 | Diffing model definitions against the live schema and emitting up and down migration SQL for MySQL, PostgreSQL and SQLite, with each change rated for risk. |
| github-profile-beautifier | 570 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| api-doc-generator | 550 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| release-notes-generator | 542 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| performance-profiler | 542 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| token-burner | 538 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| github-figure-bed | 413 | Uploading images to a GitHub repository through `gh api` and getting jsdelivr, jsdmirror or raw links back, with a one-time `setup.sh` that handles login, repository creation and config sync. |
| freeimg-z-image | 224 | Text-to-image through Gitee AI's z-image-turbo at roughly 100 free 2K images a day per token, with width, height, step and negative-prompt control. |
| freeimg-hunyuan | 207 | Text-to-image and image-to-image through Tencent Hunyuan 3.0 on CloudBase, including the free WeChat incentive pack route and four fixed output sizes. |
| video-cover-packager | 151 | Turning one video script or transcript into cover titles, platform titles, per-platform tags and a description, then compositing the chosen title onto generated cover art. |
| diagram-generator | 77 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| freeimg | 11 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |
| hunyuan-image | 9 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |

Eight of these listings have no directory in the tree: the five five-hundred-install names (github-profile-beautifier, api-doc-generator, release-notes-generator, performance-profiler, token-burner) plus diagram-generator, freeimg and hunyuan-image account for 2,839 of the 7,887 installs, or just over a third of the total, and none of them can be installed from this repository.

## Why This Matters for Hermes Agents

Most of an agent's DevOps work is assembly rather than invention: a Dockerfile with the right stage order and a non-root user, a workflow that logs into a registry and deploys over SSH, a pre-commit hook that formats only staged files. Each of those is a solved problem with a handful of common ways to get it wrong, and this pack encodes the wrong ways next to the right ones. That is a better unit of transfer than a tutorial, because the agent can check its own output against the mistake table.

The dependency and migration skills cover the two changes that are hardest to undo. `dependency-audit` separates CVE count, outdated packages and licence risk into three passes and attaches a fix command to each finding, which keeps an upgrade from turning into an unplanned major bump. `db-migration-helper` refuses to emit an up migration without a matching down, and rates column drops and type changes as high risk instead of treating them like any other diff.

The image skills are the unusual half. Both are bring-your-own-token and route to free tiers, one through Gitee AI's serverless API and one through a Tencent CloudBase environment bound to a WeChat incentive resource pack, and both tell the agent to look at the generated file before handing it over. For a profile that produces covers or blog assets, that removes the paid API key as a blocker without pretending the output is finished work.

Two operating notes apply to the pack as a whole. The skill bodies are Chinese, so an English-speaking operator can route work correctly from the frontmatter and the tables but will lose some of the reasoning behind a rule; translate the Common Mistakes table if you plan to rely on it. And because the repository has four stars and was last pushed 2026-09-25, treat the templates as a starting point to review rather than as maintained tooling.

## Usage

| You say | What happens |
|---|---|
| "Containerise this Node app and deploy it to my VPS on every push" | `docker-build-deploy` asks for the container port and env file path, generates the multi-stage Dockerfile and the build-and-push plus SSH deploy workflow, then lists the three secrets to add in GitHub. |
| "Check this repo for vulnerable and abandoned dependencies before we tag a release" | `dependency-audit` detects the package manager from the lockfile, parses audit output for CVE counts by severity, lists outdated majors and copyleft licences, and returns fix commands per finding. |
| "Stop people committing unformatted code and vague commit messages" | `git-hooks-setup` picks husky or native hooks from the project type, writes pre-commit, commit-msg and pre-push hooks, adds a lint-staged config, and wires gitleaks rather than keyword grep. |
| "We added an avatar column to the user model, give me the migration" | `db-migration-helper` pulls the current schema, diffs it against the model, and returns up and down SQL with the change rated and a dry-run preview first. |
| "Upload these three screenshots and give me markdown links" | `github-figure-bed` pushes the files through the Contents API without overwriting same-named files, and returns markdown plus CDN URLs per file. |
| "Make a 16:9 cover for this post, no text in the image" | `freeimg-z-image` generates at 2048 by 1152, checks the result, and leaves the title to be composited later rather than relying on the model to render text. |
| "Package this video script into a title, tags and a cover direction" | `video-cover-packager` produces a brief, three differentiated cover titles, platform titles, tags and a description, and stops for confirmation before any image is generated. |

## Verification

The raw path for the Docker skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} docker-build-deploy\n" \
  https://raw.githubusercontent.com/wu529778790/shenzjd-skills/main/docker-build-deploy/SKILL.md
```

Expect `200`. After the clone, confirm that the tree really holds eight skills, and that the entry you plan to install is one of them:

```bash
find /tmp/shenzjd-skills -maxdepth 2 -name SKILL.md | wc -l
head -6 /tmp/shenzjd-skills/docker-build-deploy/SKILL.md
ls /tmp/shenzjd-skills/docker-build-deploy
```

The count should print 8, the header should show `name: docker-build-deploy` followed by a `description:` trigger sentence, and the directory listing should show the `templates/` folder that the Core Pattern refers to. Any of the five five-hundred-install names from the table above will fail that find, which is the cheapest way to confirm the index-versus-tree gap.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| docker-build-deploy | Pass | Pass | Fail |
| dependency-audit | Pass | Pass | Pass |
| git-hooks-setup | Pass | Pass | Fail |

This is not a passive pack, and the two failures sit on the two skills that write executable code into a repository. `docker-build-deploy` emits `.github/workflows/*.yml` containing an SSH private key read from a secret, a registry login and a remote `docker` sequence; `git-hooks-setup` writes `.git/hooks/pre-commit` and `pre-push` shell scripts and can add a gitleaks invocation, so both change what runs automatically on a developer's machine or on every push. Snyk reports code E005 on each of them, and the trustworthy reading is narrow: the two skills whose output executes are the two the scanner objects to, and the one skill that only reports has no finding.

The wider attack surface is credential handling and network egress rather than the skill documents. Three skills keep local configuration in home-directory files: `freeimg-z-image` and `freeimg-hunyuan` store API tokens in mode 600 `config.env` files and instruct the agent not to echo them, while `github-figure-bed` caches owner, repository, branch and CDN settings in `~/.config/github-figure-bed/config.env`. That is the right instinct for token handling, and it still means a local secret store per skill. `freeimg-hunyuan` runs an npm install of the Tencent CloudBase SDK into a home directory on first use, so its trust model includes the npm registry, and `github-figure-bed` reads configuration from the target repository's `.img.shenzjd.com/config.json`, so an upload target you do not control can influence branch, directory and CDN settings. Review the generated workflow and hook files before committing them, keep the `gh` token narrowly scoped, and treat any skill that writes a deploy pipeline as a review item rather than a one-click action. MIT licensing imposes no further obligation.

## Limitations

- Snapshot data, verified 2026-11-01: 7,887 combined installs across 16 indexed listings; 4 GitHub stars; MIT; last pushed 2026-09-25. Counts drift over time.
- Eight of the sixteen listings have no directory in the tree: github-profile-beautifier, api-doc-generator, release-notes-generator, performance-profiler, token-burner, diagram-generator, freeimg and hunyuan-image carry 2,839 installs between them and cannot be installed from this repository.
- The README's own blurb says seven skills while its table and the tree both hold eight, so read the directory listing rather than the summary line when counting what you have.
- Skill bodies are largely Chinese with English frontmatter and trigger lists. The parameters and mistake tables survive translation; the reasoning behind a rule may not.
- Four stars and a last push in late September 2026 mean thin community review. The Docker and hook templates are worth reading in full before they run against a production repository, particularly the Snyk-flagged pair.
- Some skills assume a Node.js project. `docker-build-deploy` states outright that Node.js is the only project type it supports today, and the hook generator decides between husky and native hooks from JavaScript lockfiles.

## Related

- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Linux Systemd Setup](/hermes/skills/catalog/linux-systemd-setup)
- [Vps Server Management Setup](/hermes/skills/catalog/vps-server-management-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time. `dependency-audit` and `db-migration-helper` are self-contained and useful immediately, while the deploy and hook skills rewrite files that execute, and mixing all eight into a profile makes it hard to tell which one produced a change.
- Keep the Common Mistakes table next to the output. When `docker-build-deploy` returns a workflow, ask it to check the result against those ten rows, including the `packages: write` permission and the dual `latest` plus sha tag, since both are easy to omit and expensive to discover in production.
- Run `dependency-audit` in report mode before any upgrade. The `--fix` flag exists, but the skill's own guidance is that major bumps need to be applied and tested one at a time, so let it produce commands and decide yourself which to run.
- Do not let the model render cover text. Both image skills and `video-cover-packager` converge on the same conclusion: generate a text-free base image and composite the title with `scripts/add-title.py`, because CJK glyphs in generated images come out corrupted.
- Verify the eight-directory tree before installing anything from the index. The five most-installed listings after the core four do not exist in the repository, and a copy step aimed at `github-profile-beautifier` will silently produce nothing.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
