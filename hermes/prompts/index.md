---
title: "Hermes Agent Prompt Library"
description: Curated Hermes Agent prompt templates for code generation, content creation, data analysis, business operations, research, and creative work. Customization guide, model selection, chaining strategies, and common pitfalls.
category: prompts
tags: [hermes-agent, prompts, prompt-templates, code-generation, content-creation, data-analysis, ai-prompts]
last_updated: 2026-07-08
---

# Hermes Agent Prompt Library  --  Curated AI Prompt Templates

---

## What's Inside

| Collection | File | Use For |
|---|---|---|
| Code Generation | `code-generation.md` | Writing, refactoring, debugging, and reviewing code |
| Content Creation | `content-creation.md` | Blog posts, social media, email, video scripts, SEO |
| Data Analysis | `data-analysis.md` | SQL queries, reporting, visualization, metrics |
| Business Operations | `business-operations.md` | Email, meetings, project planning, task management |
| Research | `research.md` | Competitive analysis, market sizing, tech evaluation |
| Creative | `creative.md` | Brainstorming, naming, design briefs, creative strategy |

---

## How to Customize Prompts

### The Bracket Convention

Every prompt uses `[BRACKETED TEXT]` as a placeholder. Replace these with your specific details before sending the prompt to any model. For example:

**Template:** "Write a [WORD COUNT]-word blog post about [TOPIC] targeting [AUDIENCE]."

**Filled:** "Write a 1200-word blog post about Kubernetes cost optimization targeting DevOps engineers at Series B startups."

The more specific your replacements, the better your output. Vague inputs produce generic results.

### Adding Your Context

Most prompts work better when you add:

1. **Examples of your style.** For emails, paste 2-3 emails you've written that you like. For code, include a function from your codebase that shows your patterns.
2. **Your data schema.** For analysis prompts, include actual table names and column types.
3. **Your constraints.** Mention specific frameworks, brand guidelines, budget limits, or technical requirements.
4. **Your definition of success.** What does "good" look like for this specific output?

### Combining Prompts

These prompts are designed to be chained. Common pipelines include:

- **Code pipeline:** code generation → code review → test generation → documentation
- **Content pipeline:** research prompt → outline → first draft → editing pass
- **Analysis pipeline:** exploratory analysis → anomaly detection → report generation
- **Operations pipeline:** task breakdown → sprint plan → daily standup → weekly recap

---

## Model Selection Guide

Not all prompts work equally well with all models. Here's a general guide:

### Code Generation and Debugging
**Best with:** Claude 3.5 Sonnet, GPT-4o, DeepSeek V3, Gemini 2.5 Pro
**Why:** These models excel at structured reasoning, syntax accuracy, and following detailed technical specifications. For simple boilerplate, smaller local models like CodeLlama or DeepSeek Coder can handle it efficiently.

### Content Creation
**Best with:** Claude 3.5 Sonnet, GPT-4o
**Why:** Strong prose generation, tone control, and brand voice consistency. For high-volume social content, smaller models fine-tuned on your brand voice can be more cost-effective.

### Data Analysis
**Best with:** Claude 3.5 Sonnet (long context for schemas), GPT-4o
**Why:** SQL generation accuracy, ability to reason about complex schemas, and thorough edge-case handling. Provide actual schema definitions  --  don't summarize them.

### Business Operations
**Best with:** Claude 3.5 Sonnet, GPT-4o, Gemini Flash
**Why:** Email and meeting tasks benefit from nuanced understanding of professional context and relationship dynamics. For quick drafts, smaller/faster models work well; for sensitive communications, use a frontier model.

### Research
**Best with:** Claude 3.5 Sonnet (200K context for document analysis), GPT-4o with web search
**Why:** Research tasks often involve synthesizing large amounts of information. Long-context models handle document dumps better. Web-enabled models can pull in current data.

### Creative Work
**Best with:** Claude 3.5 Sonnet, GPT-4, Gemini
**Why:** Creative tasks benefit from models that take interesting "risks" in their outputs. Temperature settings matter  --  try 0.8-1.0 for brainstorming, 0.5-0.7 for refined creative output.

---

## Prompt Chaining Strategies

### Sequential Refinement
Start with a broad prompt, evaluate the output, then follow up with targeted refinements:
1. "Write a blog post about [TOPIC]." → gets a first draft
2. "Make the introduction more personal, add a customer story." → improves specific sections
3. "Shorten everything by 20% and add subheadings." → tightens and structures

### Parallel Generation
For creative tasks, run the same prompt 3-5 times (or ask for 3-5 variants in one prompt) and select the best. Models are non-deterministic  --  different runs produce different ideas.

### Role-Based Chaining
Use different system prompts for different stages:
1. **Researcher** persona: gather facts and outline structure
2. **Writer** persona: draft the content
3. **Editor** persona: review, tighten, improve flow
4. **Fact-checker** persona: verify claims and data

---

## Common Pitfalls and Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Output is too generic | Placeholders too vague | Add specific constraints, examples, audience details |
| Model ignores a key requirement | Buried in long prompt | Put critical requirements at the top or repeat them |
| Code doesn't run | Missing context about environment | Specify language version, framework, dependencies |
| Creative output is bland | Temperature too low | Use temperature 0.8-1.0; ask for "surprising" or "unconventional" ideas |
| Analysis is shallow | Didn't provide schema or data sample | Give the actual structure, not a description of it |
| Email feels robotic | No style examples given | Paste 2-3 examples of your own writing as reference |

---

## Contributing

These prompts are starting points. As you discover effective variations, adapt them to your workflow. The best prompt is the one that consistently produces useful output for your specific context  --  invest in refining it over time.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*


## All Prompts

- [Readme](/docs/hermes/prompts/)
- [business-operations.md](/docs/hermes/prompts/business-operations.html)
- [code-generation.md](/docs/hermes/prompts/code-generation.html)
- [content-creation.md](/docs/hermes/prompts/content-creation.html)
- [creative.md](/docs/hermes/prompts/creative.html)
- [Customer & CRM Prompts](/docs/hermes/prompts/customer-and-crm.html)
- [data-analysis.md](/docs/hermes/prompts/data-analysis.html)
- [Ecommerce Ops](/docs/hermes/prompts/ecommerce-ops.html)
- [Email And Sms](/docs/hermes/prompts/email-and-sms.html)
- [Executive Summary](/docs/hermes/prompts/executive-summary.html)
- [Marketing Roas](/docs/hermes/prompts/marketing-roas.html)
- [Mcp Developer Queries](/docs/hermes/prompts/mcp-developer-queries.html)
- [Multi Source](/docs/hermes/prompts/multi-source.html)
- [Productivity And Files](/docs/hermes/prompts/productivity-and-files.html)
- [research.md](/docs/hermes/prompts/research.html)
- [Revenue And Finance](/docs/hermes/prompts/revenue-and-finance.html)
- [Seo And Content](/docs/hermes/prompts/seo-and-content.html)
