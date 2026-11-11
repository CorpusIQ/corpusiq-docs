---
title: "Anthropic Healthcare Skills - Clinical Workflow Suite Setup"
description: "Anthropic's healthcare plugin: 2.3K combined installs across 10 listings, with skills for FHIR, prior authorization, ICD-10 and clinical notes"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anthropic-healthcare-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "healthcare", "fhir", "prior authorization", "clinical data"]
---

# Anthropic Healthcare Skills - Setup Guide

**Source:** [anthropics/healthcare](https://www.skills.sh/anthropics/healthcare) via skills.sh - 2.3K combined installs across 10 indexed listings (2,256 exact); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 443 stars, no LICENSE file (the README states Anthropic's terms of service), `main` branch, last pushed 2026-08-27, 11 `SKILL.md` files under `plugins/healthcare/skills/<name>/`
**Category:** Healthcare operations: clinical data extraction, coding, claims review, FHIR integration, contract questions
**Quality Tier:** 🟡 Mixed - an official Anthropic publisher with a clean plugin layout and seven connected MCP servers, but one sampled skill carries a Fail verdict and the repository ships no open-source license.

This is Anthropic's own healthcare package, published the way Anthropic packages its vertical work: one plugin that bundles skills, subagents, workflow pipelines and a `.mcp.json` that wires up hosted servers so nothing has to be installed by hand. The README's opening line states the design intent directly, that skills load only when relevant so the bundle stays cheap in context.

The subject matter spans the four seats in a healthcare organisation. For payers there is prior authorization review and a fraud, waste and abuse screen over claims. For providers there is clinical note extraction with span-level provenance, ICD-10-CM coding, and CPT plus HCPCS procedure coding. For pharma there is clinical trial protocol generation. Across all of them sit document extraction, contract question answering with verified citations, and a FHIR skill that connects to a hospital's R4 server, which the README names as Epic, Oracle Health, MEDITECH, athenahealth or any SMART-on-FHIR endpoint.

The connected servers are the part that changes what an agent can answer. CMS Coverage, ICD10 Codes, NPI Registry, Clinical Trials and PubMed are hosted endpoints requiring no setup. The Contracts Analyzer and FHIR servers ship with the plugin as local stdio processes, because they touch customer data.

## Installation

The README's quick start is two commands inside Claude Code, which adds the repository as a plugin marketplace and installs the single bundled plugin:

```bash
/plugin marketplace add anthropics/healthcare
/plugin install healthcare@healthcare
```

The README documents that the v1 per-skill and per-server plugins still install as deprecated aliases that resolve into this one bundle, naming `prior-auth-review`, `fhir-developer`, `clinical-trial-protocol`, `cms-coverage`, `icd10-codes`, `npi-registry` and `pubmed`, and states the aliases will be removed in a future release. Install `healthcare@healthcare` rather than the aliases.

For a Hermes profile or any agent without the plugin marketplace, copy the skill directories in. Keep the folder names intact, because the skills reference their own supporting files by relative path:

```bash
git clone https://github.com/anthropics/healthcare
cp -R healthcare/plugins/healthcare/skills/* ~/.hermes/profiles/corpusiq/skills/
```

That copy carries the skill folders only. The `.mcp.json` wiring lives at `plugins/healthcare/.mcp.json` and has to be added as MCP server configuration separately if you want the hosted servers, since copying skill directories does not register any server.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fhir-developer-skill | 674 | FHIR API development guidance for building healthcare endpoints, the highest-installed skill in the family |
| clinical-trial-protocol-skill | 459 | Generating clinical trial protocols for medical devices or drugs |
| prior-auth-review-skill | 351 | Automating payer review of prior authorization requests |
| icd10-cm-skill | 130 | Extracting billable ICD-10-CM diagnosis codes from a clinical note the way a professional coder builds the claim |
| clinical-note-extract-skill | 122 | Extracting structured data from clinical notes with span-level provenance and null-safety |
| contracts | 112 | Answering a question across a corpus of contract documents with verified citations |
| fhir | 106 | Connecting to a hospital FHIR R4 server, pulling a patient's clinical data and notes, then extracting structured findings |
| doc-extract | 106 | Extracting plain text from PDF, DOCX, XLSX, PPTX, RTF, markdown or HTML |
| fraud-detection | 100 | Screening a Medicare or Medicaid claims corpus for fraud, waste and abuse and producing ranked, cited investigation referrals |

The remaining 1 indexed listing is procedure-coding (96 installs), which assigns CPT and HCPCS Level II codes from clinical documentation.

Two naming details matter when you go looking for files. The install index carries suffixed names such as `fhir-developer-skill` and `prior-auth-review-skill`, while the tree directories are shorter: `plugins/healthcare/skills/fhir-developer/` and `plugins/healthcare/skills/prior-auth/`. The index also carries both `fhir` and `fhir-developer-skill` as separate listings, which are separate skills rather than duplicates, one for reading a live server and one for building against the API.

## Why This Matters for Hermes Agents

Healthcare is the vertical where a confident wrong answer is most expensive, and the failure mode of a general agent is specific: it will produce a plausible ICD-10 code, a plausible coverage rule or a plausible citation that never existed. What this package changes is the grounding. Codes come from the ICD10 Codes server, coverage rules from CMS Coverage, provider identity from the NPI Registry, and contract answers are required to carry verified citations.

The extraction skills carry a design decision worth copying into your own skills. `clinical-note-extract` promises span-level provenance, meaning every extracted field points back at the text it came from, and null-safety, meaning an absent field is reported absent rather than filled. Those two properties are what make extracted clinical data reviewable by a human instead of trusted on faith.

The coding skills encode process, not lookup. The README describes both `icd10-cm` and `procedure-coding` as working the way a professional coder builds the claim, which means sequencing and specificity rules rather than a keyword match to a code table. For an agent supporting a billing or revenue-cycle team, that distinction is the difference between a suggestion and a liability.

The FHIR skill is the integration surface. A hospital's R4 server is where the actual patient record lives, and the skill covers the practical path: connect to a SMART-on-FHIR endpoint, pull clinical data and notes, then extract structured findings. Pair it with `fhir-developer-skill` and an agent can both read a live server and help build endpoints against the same spec.

Scope discipline is the last reason it belongs in a catalog. Ten skills, each with a narrow trigger, is a much smaller attack and error surface than one large healthcare prompt, and the plugin structure keeps the load cost proportional to the question asked.

## Usage

| You say | What happens |
|---|---|
| "Extract the diagnoses and medications from this discharge note" | Applies the clinical note extraction pattern, returns structured fields with span-level provenance, and reports absent fields as absent rather than guessing |
| "What ICD-10-CM codes does this encounter support" | Builds the claim the way a coder would, drawing codes from the ICD10 server rather than from model recall |
| "Do these claims look like fraud, waste or abuse" | Screens the claims corpus and returns ranked referrals with citations an SIU team can act on |
| "What does our payer policy say about this prior authorization" | Runs the payer review path over the request and checks coverage rules against the CMS Coverage server |
| "Pull this patient's FHIR record from the hospital and summarize the findings" | Connects to the R4 endpoint, retrieves clinical data and notes, then extracts structured findings |
| "Which of our contracts allow this termination clause" | Answers across the contract corpus with verified citations back to the specific document |
| "What is this provider's NPI and enrollment status" | Queries the NPI Registry server instead of guessing an identifier |

## Verification

Each skill sits at `plugins/healthcare/skills/<name>/SKILL.md`, where the directory name is the shorter tree name and not the install index name. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/anthropics/healthcare/main/plugins/healthcare/skills/fhir-developer/SKILL.md | head -5
```

It should open with YAML frontmatter carrying a `name` and `description` field. To confirm the bundle arrives complete, list the skill directories after install and check that all ten are present:

```bash
ls ~/.hermes/profiles/corpusiq/skills/ | grep -E 'fhir|prior-auth|icd10|clinical|contracts|doc-extract|fraud|procedure-coding'
```

If the hosted servers are part of what you want, check the MCP configuration separately, because the skill copy does not register them:

```bash
cat healthcare/plugins/healthcare/.mcp.json
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fhir-developer-skill | Pass | Pass | Pass |
| clinical-trial-protocol-skill | Fail | Warn | Pass |
| prior-auth-review-skill | Pass | Pass | Warn |
| icd10-cm-skill | Pass | Pass | Pass |
| clinical-note-extract-skill | Pass | Pass | Warn |
| contracts | Pass | Pass | Warn |
| fhir | Pass | Pass | Fail |
| doc-extract | Pass | Pass | Warn |
| fraud-detection | Pass | Pass | Pass |

The mixed result is the reason this guide is not rated green. Nine of the nine sampled skills pass the trust-hub check except `clinical-trial-protocol-skill`, which carries its only Fail in the sample, and `fhir` carries a Snyk Fail while `prior-auth-review-skill` carries a Snyk Warn. Read the individual security page on skills.sh for any skill you plan to run in production rather than treating a family verdict as uniform.

The larger security question is data, not code. These skills handle protected health information, and the FHIR and Contracts Analyzer servers are the local processes that reach a hospital's systems. That traffic stays between your agent and the endpoint you configure, and the hosted servers see the queries sent to them. Treat the whole package as regulated-data tooling: point it only at systems you are authorised to query, and keep the audit trail of what was asked.

## Limitations

- Snapshot data, verified 2026-11-11: 2,256 combined installs across 10 indexed listings; 443 GitHub stars; no LICENSE file, README states Anthropic's terms of service; last pushed 2026-08-27. Counts drift over time.
- No open-source license. The README's license section says the code is provided under Anthropic's terms of service, so check those terms before redistributing or embedding any part of the package.
- The package assumes Claude Code for the documented path. Other agents can load the skills as plain markdown, but the plugin marketplace commands, the workflow pipelines and the `.mcp.json` wiring are Claude Code shapes and need manual equivalent setup elsewhere.
- The hosted servers are an external dependency you do not control. If `hcls.mcp.claude.com` or `pubmed.mcp.claude.com` changes availability or terms, the skills that rely on them degrade even though the local files are unchanged.
- Install-index drift. The index names skills with suffixes (`fhir-developer-skill`, `prior-auth-review-skill`) while the tree uses shorter directories (`fhir-developer`, `prior-auth`), so a file lookup by index name fails.
- Clinical output needs a professional read. The coding and fraud skills model how a coder or investigator works; they do not replace the compliance review, the coding audit or the investigator.

## Related

- [Claude for Legal Skills - Anthropic Legal Workflow Suite Setup](/hermes/skills/catalog/claude-for-legal-skills-setup)
- [LinkFox Skills - IP, Legal and Trade Data Setup](/hermes/skills/catalog/linkfox-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the single `healthcare@healthcare` plugin, not the v1 aliases. The README marks every alias as deprecated and says they will be removed.
- Ask for provenance whenever you extract. The clinical note skill is built to return span-level evidence, and requesting it explicitly turns a summary into something an auditor can check.
- Treat absent as absent. The null-safety behaviour is the feature you want when a field is missing, so phrase requests as "extract if present, otherwise say missing" rather than letting a model fill the gap.
- Keep coding and coverage answers on the servers. If a response cites a code or a rule without the ICD10 or CMS Coverage server being reachable, the answer came from model memory and should be verified before it reaches a claim.
- Separate the read path from the write path in your own setup. Nothing in this package files anything, and keeping it that way means a mistake produces a wrong suggestion rather than a wrong submission.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
