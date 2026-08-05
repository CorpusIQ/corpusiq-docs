# Reddit Automation Pipeline

## Overview

CorpusIQ deploys a help-first Reddit presence across 8 high-engagement subreddits targeting USA business operators. The pipeline runs on the DGX Spark Commander host using Playwright Firefox + IPRoyal mobile proxy.

## Architecture

- **Posting**: Postiz CLI, confirmed working on r/SaaS, r/entrepreneur, r/smallbusiness
- **Commenting**: Playwright Firefox + IPRoyal 4G mobile proxy (5 rotating IPs)
- **Anti-detection**: Mobile carrier IPs bypass Reddit JS challenges. Chrome proxy-server is non-functional — Firefox handles proxy auth correctly.
- **Engine**: Python script at scripts/reddit_engine.py — Commander-managed task

## Subreddits

| Subreddit | Subscribers | USA % | Focus |
|-----------|------------|-------|-------|
| r/SaaS | 250K | 75% | B2B software |
| r/dataengineering | 150K | 70% | Data infrastructure |
| r/ecommerce | 300K | 78% | Online retail |
| r/smallbusiness | 800K | 82% | Business ops |
| r/automation | 100K | 72% | Workflow automation |
| r/startups | 1.2M | 70% | Startup ops |
| r/Entrepreneur | 1.5M | 68% | Business owners |
| r/Bookkeeping | 40K | 85% | Finance ops |

## Engagement Rules

### Phase 2: Help-First (current)
- 5 comments per day maximum
- Zero product links
- CorpusIQ mentions only when the tool directly solves the problem
- Help must stand alone — remove the thread and the comment still helps someone

### Content Templates
Three core patterns:
1. Data reconciliation: Explain transaction-level reconciliation
2. AI inability: Explain why AI cannot reach business data
3. Dashboard chaos: Explain metric definition as prerequisite

## Technical Stack

- Browser: Playwright Firefox (headless)
- Proxy: IPRoyal mobile 4G (credential-managed)
- Host: DGX Spark (Commander)
- Cap: 5 comments per day, 30-60 second spacing
- Idempotency: Daily state file tracking posted thread IDs
