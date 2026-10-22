---
title: "Ruzora MCP - LATAM Engineering Hire With Compliance"
description: "Scores a role, lints job posts against pay-transparency law by location, screens resumes for hidden AI instructions, and requests a vetted LATAM shortlist."
category: Business Operations
stars: n/a (no public repo)
added: 2026-10-22
source: "mcp.so /feed page 1 (card posted 2026-10-22T05:10:17Z)"
relevance: ★★★
tags: [hiring, recruiting, latam, pay-transparency, job-post-compliance, resume-screening, prompt-injection, remote-mcp, mcp-server]
---

# Ruzora MCP

**A hiring server whose most useful tools are the ones that stop a bad post going out: a pay-transparency check by jurisdiction, a job-post linter, and a screen for instructions hidden in a resume.**

```
Server type: Remote (Streamable HTTP) at https://mcp.ruzora.com/mcp
Auth: none for the read and planning tools; a work-email code is required before actions that need a verified buyer
Live check: POST initialize returned HTTP 200 (serverInfo ruzora 1.0.0, protocol 2025-03-26, tools, prompts and resources capabilities); tools/list returned 35 tools
Real call: check_pay_transparency with locations [California, New York] returned three applicable rules with statute citations and source URLs, rules stated as of 2026-10-04
Tools: 35 (role scorecards, pay-transparency, job-post lint, resume triage and injection detection, interview kits, coding assessments, vetted-engineer search, shortlist and project requests)
Pricing: flat monthly rate per engineer, quoted per role; vendor states 40 to 60 percent below a fully loaded US hire, a three-month initial commitment then month to month on 30 days' notice, and a 60-day replacement guarantee
Vendor: Ruzora (ruzora.com), senior software engineers in Latin America
```

## Why This Matters for Operators

Two things changed hiring in the last three years and most tooling has not caught up. The first is that pay-transparency law is now local law: the same job post is compliant in one state, illegal in another, and a range that satisfies one city carries a different effective date in the next. The second is that candidates can now write a resume that reads perfectly to a human and carries hidden instructions to an AI screener.

Both are compliance problems with a computable answer, which is exactly what an MCP server is good for. Neither is solved by a job board.

## What It Actually Does

The hiring pipeline is exposed as discrete steps rather than one opaque run, and the steps are designed to be argued with.

Planning: `build_role_scorecard` turns "we need a senior full-stack dev" into a mission, measurable twelve-month outcomes and must-haves. `calibrate_seniority` works out what level a role really needs by scope rather than years. `compare_hiring_models` returns a neutral twelve-month cost and risk comparison across a US employee, a US contractor, a freelancer, an agency, staff augmentation and an international hire.

Compliance: `check_pay_transparency` takes hiring locations and returns which pay-transparency laws apply, with severity, statute citation, effective date and the source URL. `lint_job_post` takes an existing post and returns a fix list: a missing range where one is required, "US citizens only" phrasing, age, gender or origin language. `write_job_description` generates a post with the compliance check folded in.

Screening: `triage_resumes` scores CVs against the must-haves with evidence, with a blind mode and hidden-text flags. `detect_resume_injection` looks for exactly the attack the AI screener invites: "ignore previous instructions", invisible characters, white-on-white text, metadata tricks. `review_code_sample` gives a plain-English read of a repository or code sample for non-technical hirers, including authorship confidence.

Interviewing: `build_interview_kit`, `developer_interview_questions` for managers who are not engineers, `design_coding_assessment` for tests that still work when candidates have AI, `score_interview_notes` to turn raw notes into an anchored scorecard and a debrief memo, and `plan_reference_check` to verify referees are real.

Supply: `search_vetted_engineers` returns blind profiles of senior engineers in Latin America who passed Ruzora's vetting, `check_market_supply` says whether a stack reads Available or On demand, `request_vetted_shortlist` asks for a shortlist, and `verify_ruzora_badge` checks that a claimed badge is real and current.

## Installation

```bash
claude mcp add --transport http ruzora https://mcp.ruzora.com/mcp
```

No sign-in is required for the planning and compliance tools. Actions that need a verified buyer use a two-step email code, `verify_work_email` then `confirm_work_email`, so no password or account is handed to the client.

## Configuration

```json
{
  "mcpServers": {
    "ruzora": {
      "type": "http",
      "url": "https://mcp.ruzora.com/mcp"
    }
  }
}
```

## What a Pay-Transparency Call Actually Returns

`check_pay_transparency` with locations California and New York returned three rules, each with a label rather than a verdict:

```json
{
  "severity": "high",
  "label": "Applies",
  "title": "California",
  "fix": "Cal. Lab. Code § 432.3 (as amended by SB 642, effective 2026-01-01), since 2023-01-01"
}
```

and for New York State, `N.Y. Lab. Law § 194-b` with a note that the law covers employers with four or more employees and that the headcount was not supplied, so that test is the operator's to confirm. New York City came back as `May apply`, explaining that the city law also applies if the role is performed there.

The response also carries `notes: ["Rules as of 2026-10-04."]`, source URLs for each statute, and an explicit disclaimer that this is general information rather than legal advice. That last part is the reason the tool is useful: it produces a checkable citation and a date, not an opinion.

## Business Relevance

- **Founders hiring their first engineer abroad** get a cost and risk comparison before a recruiter call, and a scorecard that makes the interview loop defensible.
- **HR and operations leads** get pay-transparency checks by jurisdiction with citations, so the post is right the first time.
- **Anyone screening at volume** gets a resume-injection check, which is the cheapest protection against an AI screener being talked into a hire.
- **Non-technical managers** get interview kits and code-sample reviews written for their level of technical knowledge.
- **Agencies and studios** can scope a build through the software-factory path with a fixed-price model rather than an hourly estimate.

## Integration with CorpusIQ

The natural pairing is evidence before the hire. CorpusIQ can summarise what the business actually does from its connected systems, which is the raw material a role scorecard needs, and it can pull the way the team is already working out of the project and CRM connectors so the scorecard describes the job that exists rather than the job in the job description.

After the hire lands, the same connectors answer the question the shortlist cannot: whether the work the role was created for is being done.

## Limitations

- The vendor is also the supplier. Ruzora sells engineers, so its comparisons and scorecards are produced by a party with a position; the citations are checkable, the conclusion is not neutral.
- Pay-transparency data is stated as of a fixed date and covers US jurisdictions in the example returned. Non-US roles need their own check.
- No rate card. Pricing is per role and quoted, with a three-month initial commitment, so this is not a try-it-and-walk-away tool.
- The supply side is Latin America only, which is a real constraint for roles that require US-person status or a presence in another region.
- Several actions require a verified work email, which means an individual cannot run the full shortlist flow from a throwaway address.

## FAQ

### Is there a free tier?

There is no subscription to try. The planning, compliance, screening and interview tools are callable without sign-in and without an account, which is where most of the value sits; the placement itself is a quoted engagement with a three-month commitment.

### Can it check a job post I already wrote?

Yes. `lint_job_post` takes the text and returns a fix list, and `check_pay_transparency` takes the locations. Run both before publishing and the post is either compliant or carries a specific reason why it is not.

### Why does a hiring server care about prompt injection?

Because resume screening is now commonly done by an AI reading untrusted text. `detect_resume_injection` exists to catch hidden instructions and invisible characters aimed at that reader, which is a category of attack most screening tools do not look for at all.

### Is the compliance output legal advice?

No, and the response says so. It returns the statute, the effective date and a source link so that a human can confirm.

## See Also

- [Veritahire MCP](/hermes/mcp/servers/external/veritahire-mcp)
- [OpenHire MCP](/hermes/mcp/servers/external/openhire-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
