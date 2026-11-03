---
title: "Linear Release - Release Tracking CLI Setup"
description: "linear/linear-release: 15.3K combined installs. An MIT skill that generates Linear Release CI config for GitHub Actions, GitLab CI and CircleCI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linear-release-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "linear", "release tracking", "ci/cd", "deployments"]
---

# Linear Release - Setup Guide

**Source:** [linear/linear-release](https://www.skills.sh/linear/linear-release) via skills.sh - 15.3K combined installs across 1 indexed listing; first documented 2026-11-03 (nightly sweep)

**GitHub:** [linear/linear-release](https://github.com/linear/linear-release) - 70 stars, MIT, branch main, last pushed 2026-10-20; a single skill directory at `skills/linear-release-setup`, shipped beside the TypeScript CLI source in `src/`, six CI templates under `examples/` and a `.env.example` naming the one required variable

**Category:** CI/CD release tracking - generating pipeline configuration that links deployments to Linear releases

**Quality Tier:** 🟢 Green - the sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE

Linear Release is published by Linear itself, not by a third party wrapping its API. The repository holds two things that are easy to confuse: the `@linear/release` CLI, a TypeScript binary that scans commits in CI, finds Linear issue identifiers such as `ENG-123`, and creates or updates releases; and one agent skill, `linear-release-setup`, which generates the CI configuration that calls that CLI.

The skill exists because the CLI's hard part is not the CLI. It is deciding how many release pipelines a project needs, whether each one is continuous or scheduled, what stages a scheduled release moves through, and where the version number comes from. The README says as much: the setup skill "walks you through continuous vs. scheduled pipelines, monorepo path filtering, and more". Every command, flag and environment variable still lives in the README, and the skill says so in its first paragraph, instructing the agent to fetch the README before generating any config and to treat it as the source of truth.

At 126 lines, this is the smallest skill in the catalog and one of the more consequential, because what it produces is a workflow file that will run on every deploy and hold an access key.

## Installation

The README's skills.sh route installs the single skill:

```bash
npx skills add linear/linear-release
```

Once installed, the skill is invoked by name (`/linear-release-setup`), or the agent picks it up from a plain request to set up Linear Release. The README also documents the low-tech route, which is to copy `skills/linear-release-setup/SKILL.md` into the project.

For a Hermes profile the copy is the reliable path, because the skill is one file with no references directory:

```bash
git clone --depth 1 https://github.com/linear/linear-release.git /tmp/linear-release
mkdir -p ~/.hermes/profiles/corpusiq/skills/linear-release-setup
cp /tmp/linear-release/skills/linear-release-setup/SKILL.md \
   ~/.hermes/profiles/corpusiq/skills/linear-release-setup/SKILL.md
```

The skill only writes configuration. To actually track releases, install the CLI as well, either through the official GitHub Action or by downloading the platform binary:

```bash
curl -L https://github.com/linear/linear-release/releases/latest/download/linear-release-linux-x64 -o linear-release
chmod +x linear-release

curl -L https://github.com/linear/linear-release/releases/latest/download/linear-release-darwin-arm64 -o linear-release
```

One access key is required, and it is per pipeline rather than per workspace: `LINEAR_ACCESS_KEY`, created from the pipeline's settings page in Linear. `LINEAR_VCS_PROVIDER` is optional and exists for self-hosted or custom domains where the remote hostname does not identify the provider; when the provider cannot be determined, `sync` exits with code 2 before syncing anything.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| linear-release-setup | 15,255 | Generating CI/CD configuration for Linear Release: GitHub Actions, GitLab CI, CircleCI and other platforms, covering continuous versus scheduled pipelines and monorepo path filtering. |

No indexed listings fall below the threshold; the single listing appears above.

The value in the skill is the interview it runs before it writes anything. Its preflight checks that a release pipeline already exists in Linear (Settings, then Releases), detects the CI platform from `.github/workflows/*.yml`, `.gitlab-ci.yml` or `.circleci/config.yml`, and reads the default branch with `git symbolic-ref refs/remotes/origin/HEAD` rather than assuming `main`.

Then it asks the questions a model cannot answer from the repository. What do you ship, and to whom? Production versus beta, nightly versus dogfood, staging, per-platform builds, per-service splits in a monorepo. For each candidate it applies one test: can these hold different commits at the same time? A yes means a separate pipeline; a no means one pipeline with stages. The skill calls pipeline-versus-stage confusion "the single most common setup mistake" and returns to it three times, including worked calls on TestFlight, staging and per-service monorepos.

Only after that does it write YAML. The generation step also carries the two container facts that break this integration in practice: the prebuilt binary is dynamically linked against glibc, so Alpine and other musl images fail with an opaque "not found", and the job needs `git` plus `curl` present.

## Why This Matters for Hermes Agents

Release tracking is a documentation task that fails silently. If an agent writes a workflow that syncs on deploy but the checkout is shallow, `sync` scans two commits and the release ships with two issues linked; nothing errors, and the release record is quietly wrong. The skill's checklist exists for exactly that class of failure: full clone or `fetch-depth: 0`, `GIT_DEPTH: 0` and `GIT_STRATEGY` not `none` on GitLab, one secret per pipeline, the correct binary platform, glibc base image, correct branch triggers, path filters for monorepos.

The pipeline-versus-stage test is the other reason to hand this to an agent rather than to a template. Templates encode one team's structure; the test generalises. An agent that asks "can these hold different commits at the same time?" gets the right answer on a mobile release train, a web app shipping on merge, and a monorepo with five services, which is more than any of the six example directories can do on their own.

There is also a safety property worth noting. `sync` supports `--dry-run`, which scans commits and calls read-only Linear APIs while skipping the create and update mutations, so an agent can validate its configuration and its access key before anything is written to the release record. That is the right default posture for an agent operating in CI.

## Usage

| You say | What happens |
|---|---|
| "Set up Linear Release for this repo" | The skill detects the CI platform and default branch, asks what ships and to whom, then writes the workflow with the correct clone depth and secret. |
| "We ship iOS to TestFlight before production, how many pipelines?" | Applies the commits test: same build through gates becomes a stage, distinct nightly builds become their own pipeline. |
| "Add release tracking to our monorepo, five services" | Treats each independently shipping service as its own pipeline with path filters, and answers that services are never stages. |
| "Our release should move through code freeze then QA" | Generates a scheduled pipeline calling `sync` to add issues, `update --stage` to move between stages, and `complete` to finish. |
| "Check this workflow before I merge it" | Reviews against the skill's checklist: full clone, glibc image, git and curl present, one secret per pipeline, correct branch triggers. |
| "Prove the access key works without touching releases" | Runs `linear-release sync --dry-run --json`, which scans commits and calls read-only APIs without creating or modifying a release. |
| "Which release does this deploy land in?" | Explains command targeting: a plain `sync` uses the started release on scheduled pipelines, while `--release-version` selects an exact one. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/linear/linear-release/main/skills/linear-release-setup/SKILL.md
```

After a clone, confirm the repository really holds one skill and six templates:

```bash
git clone --depth 1 https://github.com/linear/linear-release.git /tmp/linear-release
ls -d /tmp/linear-release/skills/*/ | wc -l
ls /tmp/linear-release/examples
head -3 /tmp/linear-release/skills/linear-release-setup/SKILL.md
```

The count should print 1, `examples` should list `github-actions-continuous`, `github-actions-scheduled`, `gitlab-ci-continuous`, `gitlab-ci-scheduled`, `circleci-continuous` and `circleci-scheduled`, and `head` should show `name: linear-release-setup` followed by the description the runtime routes on.

On the installed copy and the CLI, two checks settle whether the setup works:

```bash
grep -n "LINEAR_ACCESS_KEY" ~/.hermes/profiles/corpusiq/skills/linear-release-setup/SKILL.md | head -3
LINEAR_ACCESS_KEY=... ./linear-release sync --dry-run --json
```

The grep should show the secret instructions, and the dry run should return a release object or `{"release":null}` on stdout with JSON Lines logs on stderr. If it exits with code 2, the VCS provider could not be determined and `LINEAR_VCS_PROVIDER` needs to be set.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| linear-release-setup | Pass | Pass | Pass |

The single indexed listing passes all three auditors, and the repository is published by Linear, which is the party that owns the API the CLI calls. The skill contains no executable code of its own: it is 126 lines of Markdown instructing an agent to ask questions, fetch the README, and write a workflow file.

Three behaviours deserve attention before production use. First, the skill writes CI configuration, so an agent with write access can change what runs on every deploy; review the generated workflow as you would any code change, and prefer a branch and a pull request over a direct commit. Second, the integration needs a pipeline access key in `LINEAR_ACCESS_KEY`, one per pipeline; the skill tells the user to store it as a CI secret (GitHub repository secrets, GitLab CI/CD variables, CircleCI environment variables) and never needs the value itself. Third, the skill instructs the agent to fetch the README from GitHub at generation time, which is a network call to a pinned public repository but still a fetch: if you run it in a sandbox with no egress, it will fall back to its own memory of the flags.

On the binary side, releases after `v0.16.0` ship a `checksums.txt` asset containing the SHA-256 digest of every executable, and those releases are immutable, so tags, executables and checksums cannot be replaced after publication. Releases through `v0.16.0` predate that integrity contract, so pin a version above it and verify the digest.

## Limitations

- Snapshot data, verified 2026-11-03: 15,255 combined installs across 1 indexed listing; 70 GitHub stars; MIT; last pushed 2026-10-20. Counts drift over time.
- One indexed listing and 70 stars is a small public footprint for a tool this consequential, so the install count reflects Linear's distribution more than community validation.
- The skill generates configuration; it does not run releases, and it deliberately defers every command, flag and environment variable to the README, which means the skill's own detail can lag the CLI.
- A release pipeline has to exist in Linear first. The skill's preflight stops there, and each pipeline has its own access key, so a multi-pipeline setup needs several secrets.
- The prebuilt binary is dynamically linked against glibc. Alpine and other musl images, including `curlimages/curl`, fail with an opaque "not found" error rather than a useful message.
- Shallow clones are the default failure. Without `fetch-depth: 0` on GitHub Actions, or `GIT_DEPTH: 0` and `GIT_STRATEGY` other than `none` on GitLab, `sync` scans almost nothing and links almost no issues.

## Related

- [Linear Integration - Issue & Project Management Setup](/hermes/skills/catalog/linear-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [OpenCLI Skills - Agent CLI with Browser Automation Setup](/hermes/skills/catalog/opencli-skills-setup)
- [Linear CLI - Issue Tracking from the Terminal](/hermes/skills/catalog/linear-cli-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Answer the pipeline question before writing any YAML. If two things can hold different commits at the same time, they are two pipelines; if the same build simply moves through gates, they are stages.
- Always pass `--release-version` in CI on scheduled pipelines. Only `sync` can set a version, and overlapping releases are otherwise targeted by "most recent started", which is not a stable identifier.
- Set `fetch-depth: 0` on the checkout step. This is the single most common cause of a release that completes successfully with no issues linked.
- Run `sync --dry-run --json` once before enabling the workflow. It validates the key, the provider detection and the commit scan without touching the release record.
- Pin a CLI version above `v0.16.0` and verify `checksums.txt`. That is the first release line with a checksum manifest and immutable tags.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
