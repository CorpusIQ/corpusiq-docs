---
title: "Education Agent Skills - 165 Teaching Skills"
description: "garethmanning/education-agent-skills on skills.sh: 20.1K combined installs; 165 evidence-grounded skills for planning, assessment and feedback."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/education-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "education", "lesson planning", "assessment", "curriculum design"]
---

# Education Agent Skills - Setup Guide

**Source:** [garethmanning/education-agent-skills](https://www.skills.sh/garethmanning/education-agent-skills) via skills.sh - 20,064 combined installs across 149 indexed listings; first seen 2026-11-08
**GitHub:** 966 stars, LICENSE in the repository root (CC BY-SA 4.0 per the README, GitHub reports NOASSERTION), `main` branch, last pushed 2026-11-03, 165 SKILL.md directories across 20 domain folders
**Category:** Education for agents: lesson planning, assessment, curriculum design, feedback and student-facing study support
**Quality Tier:** 🟢 Production - CC BY-SA 4.0 terms stated in the README, 966 stars, Pass on all three scanners for every sampled skill, and a repository that publishes its own format-verification receipt.

The library is one educator's attempt to give agents a defensible pedagogy instead of a prompt collection. Gareth Manning spent 20 years in international schools across 27 countries and built 165 skills across 20 domains: retrieval practice, spacing, cognitive load, backwards design, rubric construction, assessment validity, vocabulary tiering, historical thinking, UDL auditing, and 13 student-facing study skills that run live during a study session rather than producing a plan for a teacher.

What makes it usable by an agent rather than only readable by a human is the file format. Every `SKILL.md` opens with a YAML header that carries a `skill_id`, a `domain`, an `evidence_strength` rating, named evidence sources, typed input and output schemas, and a `chains_well_with` list. A skill such as `retrieval-practice-generator` declares the topic, year group, question count and known misconceptions it needs, then promises questions, a spacing recommendation, answer notes and a teacher script. That structure is what lets Hermes hand one skill's output to the next without the teacher restating context.

## Installation

The README does not offer a single install command for the whole library. It documents five local routes and is explicit about which ones were actually exercised. Start from the v3.1.0 release page, then pick the route that matches your client.

For Hermes, the README's own commands are a tap plus a per-skill install, and it recommends installing selected skills rather than all 165:

```bash
hermes skills tap add GarethManning/education-agent-skills
hermes skills install \
  GarethManning/education-agent-skills/skills/original-frameworks/learning-target-authoring-guide \
  --category education --yes
```

Swap the path for any other skill, for example `skills/memory-learning-science/spaced-practice-scheduler`. The README reports that Hermes v0.18.0 (2026.7.1) listed all 165 portable skills and read selected main files, metadata and a moved example in an isolated local profile. Hub installation, updates and model invocation were not tested in that check, so treat the two commands above as documented but not end-to-end verified.

For Claude Code 2.1.275 and later, the README gives the command recommended by the tested 2.1.307 validator:

```text
/plugin install education-agent-skills --marketplace GarethManning/education-agent-skills
```

Claude 2.1.307 passed local manifest validation with advisory warnings; installation and session activation were not tested. For Claude CoWork, the plugin import is the repository URL itself: `https://github.com/GarethManning/education-agent-skills`.

For OpenAI Codex, clone the repository and register it as a local marketplace:

```bash
git clone https://github.com/GarethManning/education-agent-skills.git
cd education-agent-skills
codex plugin marketplace add "$PWD"
codex plugin add education-agent-skills@education-agent-skills
codex plugin list --marketplace education-agent-skills --json
```

Registration and installation are separate steps. Codex CLI 0.163.0-alpha.11.1 passed isolated registration, installation and listing with 165 source skills and their resources; actual model activation and desktop refresh were not tested. Start a new session after installing. For one or two skills, the README also allows a plain copy:

```bash
mkdir -p ~/.codex/skills
cp -r skills/<domain>/<skill-name> ~/.codex/skills/
```

For any other Agent Skills client, download the portable ZIP from the v3.1.0 release, extract it, and copy each folder from `agent-skills/<skill-name>/` into the client's skills directory, keeping `references/` and other included files intact. The portable edition uses standard frontmatter and passes the official validator; the canonical `skills/` tree keeps the richer education metadata and is not claimed to pass strict validation. Clients requiring strict standard frontmatter should copy from `agent-skills/`, not from `skills/`.

There is also a no-setup route: open any `SKILL.md` under `skills/`, copy the prompt block, paste it into any model, and fill in the fields. That works with no account, key or dependency.

## What It Provides

The threshold for this guide is 146 installs, which puts 24 of the 149 indexed listings in the table:

| Skill | Installs | Use For |
|---|---|---|
| retrieval-practice-generator | 219 | Free recall, cued recall and recognition questions calibrated to year group and time since teaching |
| backwards-design-unit-planner | 212 | Planning a unit from desired outcomes through assessment evidence to activities |
| cognitive-load-analyser | 207 | Finding load problems in a task and naming specific design fixes |
| spaced-practice-scheduler | 192 | Building a spaced retrieval schedule for a topic list and a term |
| curriculum-knowledge-architecture-designer | 189 | Mapping the epistemic structure of a subject to inform sequencing |
| assessment-validity-checker | 180 | Auditing an assessment for construct validity, reliability and objective alignment |
| worked-example-fading-designer | 178 | Fading a worked example into independent practice for novices |
| learning-progression-builder | 178 | Building prerequisite-to-mastery steps for a target skill |
| criterion-referenced-rubric-generator | 177 | Rubrics with descriptive performance levels for general curriculum use |
| study-strategy-selector | 173 | Matching revision techniques to material type, goal and student habits |
| scope-and-sequence-designer | 169 | Vertical and horizontal coherence across a programme or year |
| competency-unpacker | 167 | Turning a broad standard into assessable success criteria |
| ai-hallucination-fact-check-protocol | 166 | Extending SIFT with AI-specific hallucination checks for student fact-checking |
| formative-assessment-loop-designer | 160 | Assessment loops where each student response drives the next move |
| dual-coding-designer | 158 | Adding a visual complement to verbal content for encoding |
| hinge-question-designer | 154 | Diagnostic mid-lesson questions that decide whether to move on |
| explicit-instruction-sequence-builder | 153 | Modelling, guided practice and independent work in one sequence |
| lesson-opening-designer | 149 | Openings that activate prior knowledge and connect to the last lesson |
| error-analysis-protocol | 149 | Diagnosing the root cause behind a pattern of mistakes |
| erroneous-example-designer | 149 | Deliberately flawed examples that train error detection |
| differentiation-adapter | 149 | Adapting a task for SEND, EAL, gifted, ADHD, dyslexia or anxiety needs |
| adaptive-hint-sequence-designer | 149 | Cascading hints that reveal progressively without giving the answer |
| progressive-hint-ladder | 146 | Graduated help from conceptual nudge to procedural step, with reflection first |
| interleaving-unit-planner | 146 | Converting a blocked sequence into mixed practice across related topics |

The remaining 125 indexed listings range from 117 to 145 installs.

The tail is not filler. It includes `feedback-quality-analyser` (142), `udl-lesson-auditor` (141), `teach-back-evaluator` (141), `gap-analysis-from-student-work` (141), `curriculum-crosswalk` (135), `single-point-rubric-designer` (134), `self-explanation-prompt-designer` (130), `three-part-lesson-designer` (125), `historical-source-adapter` (126) and `perspective-taking-designer` (117). Install counts here track discovery, not usefulness, and a teacher who needs Montessori three-part lessons or Reggio documentation will find the skill they want well below the threshold.

The 20 domains cover a wider range than the table suggests. Domains 1 to 19 are teacher and designer facing: memory and learning science, self-regulated learning, explicit instruction, questioning and dialogue, literacy and critical thinking, EAL and language development, curriculum and assessment, wellbeing and motivation, professional learning, global and cross-cultural pedagogies, environmental and experiential learning, AI learning science, AI literacy, Montessori and alternative approaches, original frameworks, curriculum alignment, historical thinking, systems thinking, and inclusive design. Domain 20 is different in kind: 13 student-facing skills such as `retrieve-first-gate`, `explain-first-interrogator`, `transfer-bridge` and `weekly-agency-review` that shape how the agent responds to a learner mid-session.

Two design choices are worth knowing before you install. The library deliberately excludes approaches without empirical support, and documents the exclusions (learning styles and VAK among them) in a separate file. It also separates evidence ratings into strong, moderate, emerging and original, and labels the last group as practitioner frameworks rather than research-backed method. That labelling is unusual in a skill library and it is the main reason the content is safe to put in front of teachers.

## Why This Matters for Hermes Agents

Hermes is good at producing a plausible lesson plan and bad at knowing what a defensible one contains. The gap is not tone or formatting, it is pedagogy: which question type produces retention, when a worked example should fade, what makes a rubric criterion-referenced rather than a grading scale. Each of these is a written judgement that a skill file can supply and an agent cannot derive from the prompt alone.

The typed schemas are the practical reason to prefer this library over pasting blog advice into a system prompt. Because `retrieval-practice-generator` declares required fields (topic, student level, question count) and optional context (time since learning, known misconceptions), Hermes has somewhere to put the details a teacher volunteers and a reason to ask for the ones missing. Skills also declare `chains_well_with`, so a unit request can move from `backwards-design-unit-planner` to `spaced-practice-scheduler` to `retrieval-practice-generator` without the teacher re-explaining the class.

The evidence metadata makes output checkable. A skill states the studies behind it and, in several cases, the limits of the analogy: the retrieval skill names Rowland's 2014 effect size, and the spacing skill describes expanding intervals as a scheduling heuristic rather than a measured optimum for a specific class. An agent that carries those caveats into its answer is less likely to present a heuristic as a law.

The student-facing domain changes what is possible in a tutoring loop. `unassisted-evidence-checkpoint` and `confidence-calibration-check` exist to separate supported performance from independent performance, which is exactly the distinction an agent otherwise blurs when it helps too eagerly. If you are building anything that claims to teach rather than draft, those skills matter more than the popular planning ones.

The honest counterweight: these are prompt files, not validated interventions. The README says directly that the prompts have not been empirically validated as AI interventions, and format compliance says nothing about whether a given model follows them on a given day. Install them as structured expertise, not as a guarantee of learning gains.

## Usage

| You say | What happens |
|---|---|
| "I'm planning a six week Year 9 cells unit, three lessons a week" | Runs `backwards-design-unit-planner` for outcomes and evidence, then `spaced-practice-scheduler` for review slots and `retrieval-practice-generator` for the questions |
| "Is this assessment any good before I print it?" | `assessment-validity-checker` audits construct validity, reliability and alignment to the stated objectives, and names the weakest item type |
| "My class keeps making the same mistake with fractions" | `error-analysis-protocol` diagnoses the likely root cause, then `erroneous-example-designer` builds flawed examples for error spotting |
| "Build a rubric for the Year 10 lab report" | `criterion-referenced-rubric-generator` produces descriptive levels; `single-point-rubric-designer` if you want one criterion with open evidence columns |
| "I don't get this at all, just explain it" (student) | `retrieve-first-gate` asks for a free recall attempt and a confidence rating before any explanation, then `progressive-hint-ladder` supplies graduated hints |
| "I think I understand this chapter" (student) | `teach-back-evaluator` has the learner teach it to a curious novice persona, then `transfer-bridge` tests near and far transfer |
| "A student used AI for this essay, can it be checked?" | `ai-output-critical-audit-designer` applies Ennis's six critical thinking standards, with `ai-claim-checker` for the learner's own verification habit |

## Verification

The default branch is `main`, and the tree has 20 domain folders under `skills/`. This raw path returned 200:

```bash
curl -fsSL https://raw.githubusercontent.com/GarethManning/education-agent-skills/main/skills/memory-learning-science/retrieval-practice-generator/SKILL.md | head -20
```

It should open with `---`, then `# AGENT SKILLS STANDARD FIELDS (v2)`, `name: retrieval-practice-generator`, a description scoped to retrieval questions at varied difficulty, and further down `skill_id: "memory-learning-science/retrieval-practice-generator"` with `evidence_strength: "strong"`. The extended header is the tell that you are reading the canonical tree rather than the portable edition.

Count the skills after cloning, because the number you see quoted and the number on disk should agree:

```bash
find skills -name SKILL.md | wc -l
```

That should print 165, spread over the 20 domain directories. If it prints a different number, the library has changed since this snapshot and the install counts in this guide are stale too.

After installing into Hermes, confirm the copy is complete rather than only present: the skill folder should contain `SKILL.md`, and any `references/` or policy files the source folder had should be there as well. A folder with only `SKILL.md` will still load, but a skill whose body points at a missing reference will behave worse than no skill at all.

For the plugin routes, the check is the client's own list command. Codex has one in the README (`codex plugin list --marketplace education-agent-skills --json`); Claude has no equivalent documented, which is part of why the Claude route is the least verified of the five.

## Security

skills.sh verdicts for five sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| retrieval-practice-generator | Pass | Pass | Pass |
| worked-example-to-problem-solving-transition-designer | Pass | Pass | Pass |
| udl-barrier-anticipator | Pass | Pass | Pass |
| metacognitive-monitoring-ai-contexts | Pass | Pass | Pass |
| perspective-taking-designer | Pass | Pass | Pass |

The repository publishes its own format-verification receipt dated 22 October 2026, which records 165 of 165 portable skills passing `skills-ref` 0.1.0 at a pinned commit. Read that as what it is: format compatibility is not a certification of teaching quality, and the README says so in the same paragraph.

The install itself is low risk. Skills are markdown prompt files with optional references, no install hooks, no postinstall script, and no network calls of their own. Nothing in the library asks for credentials. The repository does ship an MCP server under `mcp-server/` for people who want tool-based discovery, but that is a separate component you build and run yourself, not something the skills need.

Two real surfaces remain. First, output correctness: these skills make an agent more fluent and more confident about pedagogy, and a plausible rubric or a confidently cited study is harder to challenge than an obviously weak answer. Spot-check citations against the sources before a school adopts any output. Second, licence obligations: CC BY-SA 4.0 is share-alike, so adapted skill text redistributed in your product carries the licence with it. If you are building a commercial tutor, read the licence before you ship modified prompts.

Student-facing skills deserve their own review. They are designed to run during a session with a learner, and the ones that withhold help (`retrieve-first-gate`, `unassisted-evidence-checkpoint`, `stuck-and-error-diagnosis-coach`) change the tone of the interaction deliberately. Test them against your own safeguarding and age-appropriateness rules, and do not route a child's session through a model configuration you have not reviewed.

## Limitations

- Snapshot data, verified 2026-11-08: 20,064 combined installs across 149 indexed listings; 966 GitHub stars; CC BY-SA 4.0 per the README (GitHub reports NOASSERTION); last pushed 2026-11-03. Counts drift over time.
- The repository holds 165 SKILL.md directories against 149 indexed listings on skills.sh, so 16 skills have no install data at all and the combined figure understates the library's reach. The gap also means the table above ranks only the indexed subset.
- The library-operated public MCP service was retired with v3.1.0 and public signup is no longer offered. Local install is the supported route; a client that only accepts a remote connector needs an endpoint you operate, and old credentials do not migrate.
- The prompts have not been empirically validated as AI interventions, and the evidence ratings describe the research behind a technique, not the behaviour of a model following the prompt. Client versions and activation behaviour vary, as the README states.
- Only some client routes were exercised. Codex registration, installation and listing were tested; Claude passed manifest validation but not installation or session activation; Hermes listing was tested but not hub installation or invocation.
- CC BY-SA 4.0 is share-alike. Internal classroom use is straightforward, but redistributing adapted skill text inside a commercial product obliges you to licence the derivative on the same terms.

## Related

- [Math via Code - Hermes Agent Skill Setup Guide](/hermes/skills/catalog/math-via-code-setup)
- [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install a starter pack, not all 165. Skills load into the model's context when matched, and a curated set of ten produces sharper matching than a full library where six near-duplicate hint and feedback skills compete.
- Read the `chains_well_with` block before writing your own orchestration. The library already declares the intended sequence, and following it avoids pairing two skills that both expect to generate the assessment.
- Use the portable edition for strict clients and the canonical tree for your own tooling. The `skills/` folders carry typed schemas and evidence metadata that `agent-skills/` flattens into `references/education.json`.
- When a skill asks for student level or time since learning, answer it precisely. Difficulty calibration in the retrieval and spacing skills depends on those two fields, and a vague answer collapses the output to generic revision advice.
- Pair a planning skill with its student-facing counterpart. `formative-assessment-loop-designer` produces the teacher side; `confidence-calibration-check` and `unassisted-evidence-checkpoint` produce the evidence that tells you whether the loop worked.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
