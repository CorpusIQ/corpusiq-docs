---
title: "ResumeSkills — AI-Powered Resume Optimization & Job"
description: paramchoudhary's resume skills — ATS optimization, LinkedIn profile enhancement, resume bullet writing, tailoring, cover letters, and tech resume formatting. 13K+ combined installs across 6 skills. Job application engine for AI agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/resumeskills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# ResumeSkills — Setup Guide

**Source:** [paramchoudhary/resumeskills](https://skills.sh/paramchoudhary/resumeskills) (13K+ combined installs)
**GitHub:** [paramchoudhary/resumeskills](https://github.com/paramchoudhary/resumeskills) (1,264 ⭐)
**Category:** Career / Job Applications
**Quality Tier:** 🟢 Production

ResumeSkills provides a complete AI agent toolkit for resume optimization and job applications — ATS (Applicant Tracking System) optimization, LinkedIn profile enhancement, bullet-point writing, job-specific tailoring, cover letter generation, and tech industry resume formatting. For Hermes agents running job application workflows or helping users optimize their career materials, these skills encode the patterns that hiring managers and ATS systems look for.

---

## Installation

```bash
# Core resume optimization
npx skills add paramchoudhary/resumeskills --skill resume-ats-optimizer
npx skills add paramchoudhary/resumeskills --skill resume-tailor

# Content & writing
npx skills add paramchoudhary/resumeskills --skill resume-bullet-writer
npx skills add paramchoudhary/resumeskills --skill cover-letter-generator

# Platform & formatting
npx skills add paramchoudhary/resumeskills --skill linkedin-profile-optimizer
npx skills add paramchoudhary/resumeskills --skill tech-resume-optimizer
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **resume-ats-optimizer** | 2.6K | ATS compatibility — keyword matching, format optimization, section structuring for automated screeners |
| **linkedin-profile-optimizer** | 2.4K | LinkedIn profile enhancement — headline, about section, experience bullet optimization for recruiter search |
| **resume-bullet-writer** | 2.1K | Impact-driven bullet point writing — STAR method, metrics-first, action-verb optimization |
| **resume-tailor** | 1.9K | Job-specific resume tailoring — match skills to JD requirements, reorder experience, highlight relevant projects |
| **cover-letter-generator** | 1.9K | Custom cover letter generation — company research integration, tone matching, narrative construction |
| **tech-resume-optimizer** | 1.8K | Tech industry formatting — skills matrices, project portfolios, GitHub integration, Stack Overflow references |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Resume content** | Current resume (PDF, Word, or Markdown) to optimize from |
| **Job descriptions** | Target job descriptions for tailoring workflows |
| **LinkedIn account** | For profile optimization (read access to current profile) |

---

## Key Capabilities

### ATS Optimizer (2.6K installs)
The most critical job application skill: ensures resumes pass automated screening systems. Covers keyword extraction from job descriptions, resume format compatibility (avoiding tables, images, and columns that break parsers), section heading standardization, and skills-matrix formatting. 75% of resumes are rejected by ATS before a human sees them — this skill targets that failure point directly.

### LinkedIn Profile Optimizer (2.4K installs)
Recruiter-search optimization for LinkedIn: headline keyword strategy (the 220 characters that determine search ranking), About section narrative structure, experience bullet optimization for the LinkedIn content format (different from resume format), skills endorsement strategy, and Open to Work settings configuration.

### Resume Bullet Writer (2.1K installs)
Transforms vague job descriptions into impact-driven bullet points: STAR method (Situation, Task, Action, Result) applied to each experience, metrics-first formatting (leading with numbers), action-verb selection by industry, and achievement quantification. For agents generating resume content — this is the quality engine.

### Resume Tailor (1.9K installs)
Job-specific resume customization: parses job descriptions for required and preferred qualifications, reorders experience sections to surface most relevant roles, adjusts skill emphasis based on JD keywords, and trims irrelevant content. Critical for agents that need to apply to multiple positions without producing identical resumes.

### Cover Letter Generator (1.9K installs)
Custom cover letter generation that goes beyond template filling: company research integration (recent news, product launches, culture), hiring manager research (when available), tone matching to company voice, and narrative construction that connects candidate experience to company needs.

### Tech Resume Optimizer (1.8K installs)
Tech industry-specific optimization: skills matrix formatting (languages, frameworks, tools), project portfolio structuring (GitHub links, live demos, contribution graphs), Stack Overflow/community presence integration, and open-source contribution highlighting. For software engineering and technical roles specifically.

---

## Quick Start

```bash
# 1. Start with the ATS foundation
npx skills add paramchoudhary/resumeskills --skill resume-ats-optimizer
npx skills add paramchoudhary/resumeskills --skill resume-bullet-writer

# 2. Add tailoring for specific applications
npx skills add paramchoudhary/resumeskills --skill resume-tailor
npx skills add paramchoudhary/resumeskills --skill cover-letter-generator

# 3. Verify
npx skills list | grep resumeskills
```

---

## Verification

```bash
# Check installed resume skills
npx skills list | grep paramchoudhary/resumeskills

# Expected output lists each installed skill
```

---

## Notes

- **Complements CorpusIQ job-application-engine**: Our existing `job-application-engine` skill handles the process automation (finding jobs, tracking applications, managing pipeline). ResumeSkills handles the content quality — together they form a complete job application system.
- **ATS is the critical gate**: Without ATS optimization, even the best resume never gets read. The ATS Optimizer skill (2.6K installs) targets this specific failure mode.
- **Tech focus**: The tech-resume-optimizer skill is specifically designed for software engineering roles — directly applicable to Hermes/agent engineering positions.
- **Agent-compatible**: All skills are designed for AI agent execution — they expect structured input (resume text, job descriptions) and produce structured output.
- **Iterative workflow**: The intended workflow is ATS-optimize → tailor for role → bullet-write → generate cover letter → final review. Each skill builds on the output of the previous one.
