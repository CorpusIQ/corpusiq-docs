---
title: "Content Pipeline Blueprint for Hermes Agent"
description: End-to-end Hermes Agent content pipeline blueprint. Research, ideation, drafting, review, publication, and promotion  --  all orchestrated with cron-driven workflows, SEO analysis, and human editorial gates.
category: blueprints
tags: [hermes-agent, blueprint, content-pipeline, content-production, seo, editorial-workflow, publishing]
last_updated: 2026-07-08
---

# Content Pipeline Blueprint  --  Automated Content Production

## Pipeline Stages

```
RESEARCH → DRAFT → REVIEW → PUBLISH → PROMOTE
  (Week 1)  (Week 2) (Week 3) (Week 4)  (Week 4+)
```

Each stage has entry criteria, automated actions, human review gates, and exit criteria. Content only advances when it meets the quality bar at each gate.

## Architecture Overview

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Research │  │ Writing  │  │ Review   │  │  CMS +   │  │ Social + │
│  + SEO    │  │ + Draft  │  │ + Edit   │  │Schedule  │  │  Email   │
└─────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
      │             │             │             │             │
      └─────────────┴──────┬──────┴─────────────┴──────┬──────┘
                           │                           │
                  ┌────────▼────────┐         ┌────────▼────────┐
                  │ Content Tracker │         │ Analytics Loop  │
                  │ (Notion/Sheets) │────────▶│ (Performance)   │
                  └─────────────────┘         └─────────────────┘
```

## Stage 1: Research and Ideation

**Duration:** Week 1 of the production cycle
**Goal:** Produce a validated content brief ready for drafting.

### Step 1.1: Topic Ideation (Monday)

**Automation:** Generate a list of content topics based on multiple inputs:

1. **SEO opportunity scan**  --  query Google Search Console or Ahrefs for keywords where you rank positions 4-20 (striking distance) and have content gaps
2. **Competitor content audit**  --  identify top-performing competitor content and find angles they haven't covered
3. **Customer question mining**  --  scan support tickets, sales calls, and community forums for recurring questions
4. **Internal expertise mapping**  --  cross-reference team expertise with content needs

**Output:** A ranked list of 10-15 topics with source rationale, target keyword, estimated search volume, and difficulty score.

**Cron:** `0 8 * * 1`  --  Monday morning ideation sweep.

### Step 1.2: Content Brief Creation (Tuesday)

For each selected topic, the agent generates a content brief:

```markdown
# Content Brief: [Working Title]

## Target Keyword
- Primary: "[keyword]"  --  Volume: [X]/mo, Difficulty: [X]
- Secondary: "[kw2]", "[kw3]"

## Search Intent
[Informational/Commercial/Transactional]  --  the searcher wants to [describe].

## Outline
1. H1: [Title]
2. H2: [Section 1]
3. H2: [Section 2]
...

## Sources and References
- [Link 1]: [What to extract]
- [Link 2]: [What to extract]

## Competing Content
- [Competitor URL]: [What they do well / what they miss]

## Content Requirements
- Word count: [range]
- Media needed: [images, charts, video embeds]
- Internal links: [pages to link to]
- Authoritative sources to cite: [list]

## Success Metrics
- Primary: [organic traffic / conversions / social shares]
- Target: [specific number]
```

**Human Gate:** Content strategist reviews briefs on Wednesday. Approves 2-4 for the current cycle. Brief goes through automated quality check: is the keyword in the title? Is competitive analysis included? Are sources credible?

### Step 1.3: SME Outreach (Wednesday-Thursday)

If the topic requires subject matter expert input:
1. Agent identifies the best internal SME based on role and expertise tags
2. Drafts an interview request: context on the content, 3-5 specific questions, requested response format
3. Calendar check: suggests 2-3 meeting times or offers async option
4. Follows up after 2 business days if no response

**Cron:** `0 10 * * 3`  --  Wednesday SME matching.

## Stage 2: Drafting

**Duration:** Week 2
**Goal:** Produce a complete first draft from the approved brief.

### Step 2.1: First Draft Generation (Monday-Tuesday)

The agent generates the first draft using content creation prompts (see `prompts/content-creation.md`) with the brief as input.

**Drafting prompt structure:**
1. Feed the content brief as context
2. Include brand voice guidelines and style reference examples
3. Generate sections one at a time for better coherence, or all at once if using a long-context model
4. Include placeholder markers for: `[INSERT CHART: X vs Y comparison]`, `[INSERT QUOTE FROM SME]`, `[INSERT SCREENSHOT: feature dashboard]`

**Quality checks applied automatically:**
- Word count within range?
- All H2s from the brief covered?
- Primary keyword in H1 and first 100 words?
- Readability score (Flesch-Kincaid) within target?
- No competitor brand mentions?

### Step 2.2: Visual Asset Brief (Wednesday)

Based on the draft's placeholder markers:
1. Generate visual asset briefs for each needed image/chart/screenshot
2. Specify dimensions, format, what the visual should communicate
3. Add to design queue (Notion task, Figma request, or similar)
4. For data visualizations: generate the chart using the data from research

**Cron:** `0 9 * * 3`  --  Wednesday asset brief generation.

### Step 2.3: Internal Link and SEO Optimization (Thursday)

1. Scan the draft for internal linking opportunities  --  match phrases to existing content
2. Insert internal links with optimized anchor text
3. Generate meta title and description (2-3 variants for A/B testing)
4. Verify keyword density, header hierarchy, image alt text placeholders

**Cron:** `0 10 * * 4`  --  Thursday SEO pass.

## Stage 3: Review

**Duration:** Week 3
**Goal:** Human-edited, polished content ready for publication.

### Step 3.1: Automated Pre-Review (Monday)

Before human review, run automated checks:
- Grammar and spelling (via language tool)
- Factual claim verification (flag unsupported claims)
- Brand consistency (correct product names, no outdated references)
- Link validity (no broken internal or external links)
- Inclusive language check

**Output:** Annotated draft with issues flagged by severity. Blockers must be fixed before human review.

### Step 3.2: Human Review (Tuesday-Thursday)

The draft goes to the editor with a review package:
1. The annotated draft with automated flags
2. The original content brief for reference
3. A review checklist (generated for this specific piece)
4. Reviewer guidelines with stage-appropriate focus areas

**Review Checklist Template:**
- [ ] Title is compelling and accurate
- [ ] Introduction hooks the reader within 3 sentences
- [ ] Each section delivers on its heading promise
- [ ] Facts and statistics are attributed
- [ ] Call-to-action is clear and contextual
- [ ] Tone matches brand guidelines
- [ ] No jargon without explanation

### Step 3.3: Revision Incorporation (Friday)

Agent incorporates editor feedback:
1. Parses review comments into discrete changes
2. Applies straightforward edits automatically
3. Flags changes that need editorial judgment for re-review
4. Regenerates sections that need substantial rewrites

**Cron:** `0 9 * * 5`  --  Friday revision processing.

## Stage 4: Publish

**Duration:** Week 4, Day 1-2
**Goal:** Published content with all assets in place.

### Step 4.1: Pre-Publication Checklist (Monday)

Automated pre-flight checks:
- [ ] All images uploaded and have alt text
- [ ] Meta title and description set
- [ ] Canonical URL configured
- [ ] Schema markup applied (Article, HowTo, or FAQ as appropriate)
- [ ] Social sharing image specified (Open Graph)
- [ ] Internal redirects created if replacing old content
- [ ] UTM parameters on outbound links
- [ ] Mobile rendering verified

### Step 4.2: Publication

Content is published to the CMS. The agent:
1. Verifies the live URL resolves correctly
2. Submits to Google Search Console for indexing (URL Inspection → Request Indexing)
3. Updates the sitemap if necessary
4. Creates a "published" entry in the content tracker with publication date and URL

**Cron:** `0 8 * * 2`  --  Tuesday publication window.

## Stage 5: Promote

**Duration:** Ongoing from publication
**Goal:** Maximize reach and measure performance.

### Step 5.1: Social Media Distribution (Day of Publication)

Generate and schedule social promotion:
1. 3-5 tweet variants highlighting different angles
2. LinkedIn post with professional framing
3. Short-form video script if the topic suits visual explanation
4. Relevant community posts (Reddit, Slack communities, Discord)

**Cron:** `0 10 * * 2`  --  publication day social push.

### Step 5.2: Email Newsletter Inclusion

Add to the next newsletter issue:
1. Generate newsletter teaser (2-3 sentences with link)
2. Segment for relevance: which subscriber segments should see this?
3. A/B test subject line if the content is a major piece

### Step 5.3: Performance Tracking (Ongoing)

**7-Day Check:**
- Traffic, engagement metrics, social shares
- Search rankings for target keyword
- Any indexing issues?

**30-Day Check:**
- Organic traffic trajectory
- Keyword position changes
- Conversion events attributed to this content
- Backlinks acquired

**90-Day Check:**
- Full performance review against targets
- Update recommendation: needs refresh, optimization, or is evergreen-stable?
- Content decay detection: traffic dropping > 20% → flag for refresh

**Cron:** `0 8 * * 1`  --  weekly content performance sweep.

## Full Cron Schedule

| Time | Stage | Task | Cron |
|---|---|---|---|
| Mon 08:00 | Research | Topic ideation sweep | `0 8 * * 1` |
| Wed 10:00 | Research | SME matching and outreach | `0 10 * * 3` |
| Wed 09:00 | Drafting | Visual asset brief generation | `0 9 * * 3` |
| Thu 10:00 | Drafting | SEO optimization pass | `0 10 * * 4` |
| Fri 09:00 | Review | Revision incorporation | `0 9 * * 5` |
| Tue 08:00 | Publish | Publication and verification | `0 8 * * 2` |
| Tue 10:00 | Promote | Social media distribution | `0 10 * * 2` |
| Mon 08:00 | Promote | Weekly performance sweep | `0 8 * * 1` |

## Content Tracker Schema

Maintain a content tracker (in Notion, Airtable, or Google Sheets) with these fields:

| Field | Type | Purpose |
|---|---|---|
| Title | Text | Working title (updates through stages) |
| Status | Select | Ideation → Brief → Draft → Review → Scheduled → Published |
| Target Keyword | Text | Primary SEO keyword |
| Stage Entered | Date | When content entered current stage |
| Assigned Writer | Person | Who's drafting |
| Assigned Editor | Person | Who's reviewing |
| Word Count | Number | Current draft length |
| Published URL | URL | Live link after publication |
| 30-Day Traffic | Number | Organic traffic at 30 days |
| Performance Status | Select | On Track / Below Target / Needs Refresh |

## Implementation Notes

### The Human Gates Are Non-Negotiable
This pipeline automates everything it can  --  but the review gate must remain human. Content quality degrades without editorial judgment. The automation's job is to make the human reviewer maximally efficient, not to replace them.

### Content Calendar Management
Run a monthly planning session where the agent proposes the next month's content calendar based on pipeline capacity and strategic priorities. Lock the calendar at least 2 weeks before production starts.

### Repurposing
Every published piece should generate derivative content:
- Blog post → Twitter thread → LinkedIn carousel → newsletter mention
- Webinar → blog summary → YouTube clip → podcast episode
- Case study → sales enablement deck → social proof snippet → ad creative

Build this into the promote stage so it's systematic, not ad-hoc.

### Extending
- Connect **YouTube** for video content production tracking
- Integrate **Ahrefs/Semrush** for automated keyword position tracking
- Add **social listening** to detect when your content is discussed but not linked
- Connect **GA4** for conversion attribution by content piece

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
