---
title: Research Prompts for Hermes Agent — Competitive Analysis & Market Intelligence
description: Hermes Agent research prompts for competitive analysis, market sizing, technology evaluation, trend reports, and structured investigation. Replace bracketed text with your research parameters and data sources.
category: prompts
tags: [hermes-agent, prompts, research, competitive-analysis, market-sizing, technology-evaluation, trend-reports]
last_updated: 2026-06-16
---

# Research Prompts — Competitive Analysis & Market Intelligence

---

## Competitive Analysis

### Competitor Deep-Dive

```
Conduct a structured competitive analysis of [COMPETITOR NAME] in [INDUSTRY/MARKET].

Research dimensions:
1. Company overview: founding year, headquarters, funding, employee count, leadership
2. Product: feature set, differentiators, pricing model, user experience strengths and weaknesses
3. Market position: target customer, market share estimate, growth trajectory
4. Go-to-market: primary channels, content strategy, sales motion (self-serve vs sales-led)
5. Strengths: what they do better than alternatives
6. Weaknesses: gaps, customer complaints, churn signals
7. Recent moves: last 6 months of product launches, partnerships, pricing changes

Sources to consider: website, G2/Capterra reviews, LinkedIn, Crunchbase, press releases, job postings.

Format as an actionable brief. For each weakness identified, note whether it's an opportunity for us to exploit.
```

### Competitive Landscape Map

```
Map the competitive landscape for [MARKET/PRODUCT CATEGORY].

Analyze [N] competitors: [LIST NAMES IF KNOWN]

Create a positioning matrix with these axes:
- X-axis: [DIMENSION 1 — e.g., Ease of Use / Power]
- Y-axis: [DIMENSION 2 — e.g., SMB Focus / Enterprise Focus]

For each competitor:
- Bubble size proportional to [REVENUE/USER BASE/MARKET SHARE]
- Primary customer segment
- Price point: [FREE/FREEMIUM/$XX-YY/MONTH/ENTERPRISE]
- Key differentiator (one sentence)
- Where they're vulnerable

Identify whitespace on the matrix — where are the underserved customer needs?
```

### Feature Comparison Matrix

```
Create a feature comparison matrix for [PRODUCT CATEGORY].

Competitors: [LIST 3-6 COMPETITORS]
Feature categories:
1. [CORE FEATURE AREA 1]
2. [CORE FEATURE AREA 2]
3. [INTEGRATIONS/ECOSYSTEM]
4. [SECURITY/COMPLIANCE]
5. [PRICING/MONETIZATION]

Use a table format: Features as rows, competitors as columns. Mark each cell: ✓ (full support), ◐ (partial/limited), ✗ (not available), ? (unclear).

Below the table: highlight the 3 biggest feature gaps in the market and our relative position on each.
```

---

## Market Sizing

### TAM/SAM/SOM Analysis

```
Estimate the TAM, SAM, and SOM for [PRODUCT/SERVICE] in [GEOGRAPHY/INDUSTRY].

Product description: [1-2 SENTENCES]
Target customer: [WHO BUYS THIS]

Provide:
1. TAM (Total Addressable Market): Top-down estimate using industry reports and government data
   - Methodology and assumptions
   - Source citations
   - Dollar figure with confidence range

2. SAM (Serviceable Addressable Market): TAM filtered by our target segment and geography
   - Filters applied (company size, industry, budget, etc.)
   - Resulting figure

3. SOM (Serviceable Obtainable Market): Realistic share we can capture in [YEAR]
   - Assumptions about penetration rate and competition
   - Resulting revenue estimate

Note: if specific data isn't available, state your assumptions clearly and provide a sensitivity range.
```

### Market Trends Report

```
Synthesize a market trends report on [TOPIC/INDUSTRY] for the next [TIME HORIZON].

Structure:
1. Executive summary: 3 most important shifts happening right now
2. Trend 1: [NAME] — driving factors, evidence, implications
3. Trend 2: [NAME] — driving factors, evidence, implications
4. Trend 3: [NAME] — driving factors, evidence, implications
5. Wildcards: low-probability high-impact events to watch
6. Implications: what this means for [OUR BUSINESS/INVESTMENT THESIS]

Each trend should include:
- Supporting data points from recent reports or news
- Companies or products exemplifying the trend
- Contrarian view (what would prove this trend wrong)
- Recommended action

Cite specific sources with dates. Flag any contradictory signals.
```

---

## Technology Evaluation

### Tool/Framework Selection

```
Evaluate [CANDIDATE TOOLS/FRAMEWORKS] for [USE CASE].

Context:
- Team size and skills: [DESCRIBE]
- Scale requirements: [USERS/REQUESTS/DATA VOLUME]
- Budget constraints: [RANGE]
- Timeline: [WHEN DECISION NEEDED]

Evaluation criteria with weights (must sum to 100%):
1. Functional fit: [%] — does it solve the core problem?
2. Learning curve: [%] — time to team proficiency
3. Community/ecosystem: [%] — available libraries, support, hiring pool
4. Performance: [%] — latency, throughput, resource usage
5. Cost: [%] — licensing, hosting, operational
6. Future-proofing: [%] — roadmap, vendor stability, migration ease

Score each candidate 1-5 per criterion. Provide weighted total and a narrative recommendation.
Include a "what would make us switch later" section.
```

### Build vs Buy Analysis

```
Analyze whether we should build or buy a solution for [PROBLEM DESCRIPTION].

Internal build estimate:
- Engineering effort: [PERSON-MONTHS]
- Ongoing maintenance: [HOURS/MONTH]
- Opportunity cost: [WHAT ELSE THE TEAM COULD BUILD]

Buy options:
- Vendor 1: [NAME] at [$XX/MONTH] — pros/cons
- Vendor 2: [NAME] at [$XX/MONTH] — pros/cons

Decision framework:
1. Core vs context: is this differentiating for our business?
2. Time to value: when does each option deliver?
3. Total cost over [3-YEAR] horizon (build: eng cost + infra; buy: license + integration)
4. Flexibility risk: what if requirements change?
5. Vendor risk: what if they raise prices, get acquired, or shut down?

Provide a clear recommendation with the decisive factor highlighted.
```

---

## Research Synthesis

### Literature Review Summary

```
Synthesize findings from these [N] sources on [TOPIC]:

[LIST OR DESCRIBE SOURCES]

Output:
1. Consensus findings (things most sources agree on)
2. Points of disagreement or debate
3. Gaps — questions none of the sources adequately address
4. Key quotes (max 5, with attribution)
5. Recommended follow-up research questions

Keep total output to [N] words. Prioritize actionable insights over comprehensive summary.
```

### SWOT Analysis

```
Generate a SWOT analysis for [COMPANY/PRODUCT/INITIATIVE].

Context: [1-2 PARAGRAPHS OF BACKGROUND]

Format:
- Strengths (internal, positive): [4-6 items] — what advantages do we have?
- Weaknesses (internal, negative): [4-6 items] — where are we vulnerable?
- Opportunities (external, positive): [4-6 items] — what trends or gaps can we exploit?
- Threats (external, negative): [4-6 items] — what external forces could harm us?

For each quadrant, prioritize by impact and likelihood. 
Then provide a TOWS cross-analysis:
- How do we use strengths to exploit opportunities?
- How do we use strengths to counter threats?
- How do we fix weaknesses to pursue opportunities?
- How do we fix weaknesses to survive threats?
```
