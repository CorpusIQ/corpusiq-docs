# Executive summary prompts

These are the high-leverage, broad-scope prompts. They fire CorpusIQ's
**multi-source skills** — pre-built runbooks that pull from everything you
have connected and synthesize a single answer.

If you only learn one category, learn this one.

---

### "How healthy is my business right now?"

**What this does:** Runs a top-to-bottom snapshot — cash, revenue trend,
wins, risks, this-week priorities.
**Connectors used:** QuickBooks, Shopify (if ecommerce), HubSpot/CRM,
Google Ads, Meta Ads, GA4, Gmail/Outlook, Calendar.
**Behind the scenes:** `executive-snapshot` skill.
**Sample answer shape:** Section headers for cash position, revenue, top
wins, top risks, focus-this-week — each with 2–4 bullets and specific
numbers from your data.

---

### "Give me a one-page business overview."

**What this does:** Same engine as above, formatted for skimming. Good for
forwarding to a co-founder.
**Connectors used:** Whatever you have connected.
**Behind the scenes:** `executive-snapshot`.
**Sample answer shape:** Tighter than the health check — one screen,
no fluff.

---

### "What changed in the business this month?"

**What this does:** Diff-style report — what moved up, what moved down,
what's new on the radar.
**Connectors used:** QuickBooks, Shopify, GA4, ad accounts, CRM.
**Behind the scenes:** `executive-snapshot` with a month-over-month framing.
**Sample answer shape:** Two columns — improvements and regressions —
with the metric, the delta, and a one-line possible cause.

---

### "What should I work on today?"

**What this does:** Ranks the top 3 things to do based on revenue impact,
deadlines, and what's slipping. Cross-references calendar, pipeline,
overdue tasks, and high-value unanswered emails.
**Connectors used:** Calendar, CRM, Email, QuickBooks.
**Behind the scenes:** `today-focus` skill.
**Sample answer shape:** A ranked list of 3 items with reasoning per item
("Follow up with Acme — $42K deal, last touch 11 days ago").

---

### "Good morning. What happened overnight?"

**What this does:** Morning briefing — overnight orders, urgent emails,
today's calendar, one risk flag. Designed for the first prompt of the day.
**Connectors used:** Shopify, Email (Gmail/Outlook), Calendar, QuickBooks.
**Behind the scenes:** `morning-briefing` skill.
**Sample answer shape:** A 5-section briefing — cash, new orders, urgent
inbox items, today's meetings, today's risk.

---

### "Wrap up the day. How did today go?"

**What this does:** End-of-day reflection — what shipped, what moved in
the pipeline, money received, meetings completed, tomorrow's first thing.
**Connectors used:** Calendar, CRM, QuickBooks, Email.
**Behind the scenes:** `day-close` skill.
**Sample answer shape:** A 5-block summary closing the day and seeding
tomorrow.

---

### "Draft a board update for last quarter."

**What this does:** Generates a structured investor/board update —
financial performance, key metrics, wins, risks, asks. Pulls prior updates
from Drive if available to match tone.
**Connectors used:** QuickBooks, Shopify, HubSpot, GA4, Drive.
**Behind the scenes:** `board-update-drafter` skill.
**Sample answer shape:** Standard investor update sections —
financials, KPIs, highlights, lowlights, asks — populated with your
actuals.

---

### "Prepare me for a board meeting."

**What this does:** Same as the board update but front-loads risk Q&A.
Anticipates the awkward questions and gives you the data to answer them.
**Connectors used:** QuickBooks, CRM, ad accounts, Shopify, GA4.
**Behind the scenes:** `board-meeting-prep` skill.
**Sample answer shape:** Update draft + appendix of likely questions
with backing numbers.

---

### "Run a weekly operations review."

**What this does:** Cross-functional health check — SLAs, incidents,
team capacity, supplier issues, bottlenecks. For COOs and ops leads.
**Connectors used:** Monday or Calendar (project mgmt), Email, QuickBooks.
**Behind the scenes:** `weekly-ops-review` skill.
**Sample answer shape:** Section per ops domain with status indicator
and one drill-down bullet each.


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
