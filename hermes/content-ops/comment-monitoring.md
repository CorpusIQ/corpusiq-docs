---
title: Cross-Platform Comment Monitoring
description: Automated 5x daily comment and message monitoring across TikTok, Instagram, X, YouTube, and LinkedIn
---

# Cross-Platform Comment Monitoring

Automated monitoring of comments and messages across all active CorpusIQ social platforms. Runs 5x daily via cron.

## Schedule

Cron `fc7d32e3d588` — 5x daily: 8 AM, 11 AM, 2 PM, 5 PM, 8 PM Arizona time.

## Platforms Monitored

| Platform | Method | Frequency |
|----------|--------|-----------|
| TikTok | MCP connector / Postiz | Every run |
| Instagram | Postiz posts:list | Every run |
| X/Twitter | Postiz posts:list | Every run |
| YouTube | Postiz posts:list | Every run |
| LinkedIn Page | Postiz posts:list | Every run |

## Response Rules

- Help-first: answer questions genuinely
- Never reply as CorpusIQ promoting
- Leads/partnerships: flag for Benoit, do not reply
- No em dashes
- Short and human-sounding

## Delivery

Reports to Telegram CorpusIQ Team Topic 2.
Flags urgent items with warning emoji.
