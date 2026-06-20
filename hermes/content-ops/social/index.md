---
title: Automated Social Publishing
description: Multi-platform social media publishing pipeline — strategy, scheduling, content rotation, engagement tracking, and rate limit handling
---

# Automated Social Publishing

Managing social media across platforms is a scheduling, formatting, and compliance challenge. Each platform has different content formats, optimal posting times, rate limits, and audience expectations. An automated publishing pipeline handles the mechanics so your team focuses on strategy.

This guide covers building a multi-platform social publishing system with Hermes: platform strategies, content rotation, scheduling optimization, engagement tracking, and robust rate limit handling.

## Platform Strategy Matrix

Not every piece of content belongs on every platform. Here's a decision matrix:

| Content Type | LinkedIn | X/Twitter | Instagram | TikTok | Reddit | YouTube |
|---|---|---|---|---|---|---|
| Thought leadership | ✓ Best | ✓ Good | ✗ | ✗ | ✓ Thread | ✗ |
| Product updates | ✓ Good | ✓ Best | ✓ Story | ✗ | ✗ | ✓ Video |
| How-to / Tutorial | ✓ Carousel | ✓ Thread | ✓ Reel | ✓ Best | ✓ Post | ✓ Best |
| Data / Research | ✓ Best | ✓ Thread | ✓ Infographic | ✗ | ✓ Post | ✓ Video |
| Community / Culture | ✗ | ✓ Good | ✓ Best | ✓ Best | ✗ | ✗ |
| Behind the scenes | ✗ | ✗ | ✓ Story | ✓ Best | ✗ | ✓ Short |
| Case studies | ✓ Best | ✓ Thread | ✗ | ✗ | ✗ | ✓ Video |

## Multi-Platform Pipeline

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Content      │───▶│ Platform     │───▶│ Format &     │───▶│ Queue &      │
│ Calendar     │    │ Assignment   │    │ Adapt        │    │ Schedule     │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
                                                                    │
┌──────────────┐    ┌──────────────┐    ┌──────────────┐            │
│ Strategy     │◀───│ Engagement   │◀───│ Publish &    │◀───────────┘
│ Adjustment   │    │ Analysis     │    │ Monitor      │
└──────────────┘    └──────────────┘    └──────────────┘
```

## Hermes X/Twitter Runtime

For Hermes-native X/Twitter workflows, use the
[Hermes Tweet plugin](/hermes/skills/catalog/communication/hermes-tweet/).
Keep reads on `tweet_read`, use `tweet_explore` for endpoint discovery, and
enable account actions only for sessions with an explicit approval step.

## Content Rotation System

A sustainable publishing cadence requires rotating content types to avoid repetition and audience fatigue.

### Weekly Rotation Template

```yaml
content_rotation:
  monday:
    platform: linkedin
    type: thought_leadership
    topic: "{weekly_theme} — industry perspective"
    format: "text_post_with_image"
    time: "08:30"

  tuesday:
    platform: twitter
    type: thread
    topic: "{weekly_theme} — tactical breakdown"
    format: "thread_5_tweets"
    time: "12:00"
    secondary:
      platform: linkedin
      type: repurpose_thread
      time: "14:00"

  wednesday:
    platform: tiktok
    type: short_video
    topic: "{weekly_theme} — quick tip"
    format: "60s_talking_head"
    time: "14:00"
    secondary:
      platform: instagram_reels
      type: cross_post
      time: "16:00"

  thursday:
    platform: linkedin
    type: case_study_or_data
    topic: "{weekly_theme} — real results"
    format: "carousel_or_document"
    time: "08:30"
    secondary:
      platform: twitter
      type: key_stat_thread
      time: "12:00"

  friday:
    platform: all
    type: community_engagement
    topic: "engage_with_audience"
    format: "replies_and_conversations"
    time: "flexible"

  saturday:
    platform: instagram
    type: behind_the_scenes
    topic: "weekly_wrap"
    format: "story_series"
    time: "10:00"

  sunday:
    platform: none
    type: planning
    topic: "next_week_strategy"
    action: "analyze_week_performance"
```

### Content Type Distribution

A healthy content mix prevents audience burnout:

- **40% Educational:** Tutorials, how-tos, insights, frameworks
- **30% Engaging:** Questions, polls, community spotlights, conversations
- **20% Promotional:** Product updates, case studies, results, offers
- **10% Cultural:** Behind the scenes, team stories, values, humor

Monitor engagement by type. If educational content underperforms, your audience might want more actionable content. If promotional content drives unfollows, pull back.

## Scheduling Engine

### Optimal Post Time Calculation

```python
def calculate_schedule(content_calendar: list[dict], audience_data: dict) -> list[dict]:
    """
    Calculate optimal posting times based on platform analytics.

    Returns calendar with precise times assigned.
    """
    platform_times = {
        "linkedin": _best_times(audience_data["linkedin"], business_hours=True),
        "twitter": _best_times(audience_data["twitter"], spread_across_day=True),
        "instagram": _best_times(audience_data["instagram"], visual_peak=True),
        "tiktok": _best_times(audience_data["tiktok"], evening_preferred=True),
        "reddit": _best_times(audience_data["reddit"], morning_preferred=True),
    }

    scheduled = []
    for item in content_calendar:
        platform = item["platform"]
        item["scheduled_time"] = platform_times[platform].pop(0)
        scheduled.append(item)

    return scheduled

def _best_times(data: dict, **preferences) -> list[str]:
    """Rank posting hours by historical engagement."""
    hourly_engagement = {}

    for entry in data.get("hourly_engagement", []):
        score = (
            entry["avg_impressions"] * 0.3 +
            entry["avg_engagement_rate"] * 0.5 +
            entry["avg_click_rate"] * 0.2
        )
        hourly_engagement[entry["hour"]] = score

    # Apply preferences
    if preferences.get("business_hours"):
        hourly_engagement = {h: s for h, s in hourly_engagement.items()
                            if 8 <= h <= 18}

    # Sort by score descending
    ranked = sorted(hourly_engagement.items(), key=lambda x: x[1], reverse=True)

    # Return top slot for each day
    return [f"{day}T{hour:02d}:00" for day in ["Mon","Tue","Wed","Thu","Fri"]
            for hour, _ in [ranked[0]]]  # Simplified — real impl per-day
```

### Hermes Cron Integration

```yaml
# hermes/cron/social_publish.yaml
name: social_publish_hourly
schedule: "0 * * * *"  # Every hour
task: social.publish.queued_posts
params:
  dry_run: false
  platforms: [linkedin, twitter, instagram, tiktok]
timeout: 300
notify_on: ["failure"]

# Weekly content planning
name: social_content_planning
schedule: "0 14 * * 5"  # Friday 2pm
task: social.plan.next_week
params:
  analyze_last_week: true
  generate_briefs: true
timeout: 1800
notify_on: ["complete"]
```

## Rate Limit Handling

Every platform has rate limits. Hitting them can cause temporary bans or account restrictions. Your pipeline must respect them proactively.

### Platform Rate Limits

| Platform | Post Limit | Read Limit | Notes |
|---|---|---|---|
| LinkedIn | 100 posts/day (company), 10/day (personal) | 100K requests/day | API access tier matters |
| X/Twitter | 50 posts/day (free), 100 (basic) | Varies by endpoint | 15-min windows on writes |
| Instagram | 25 posts/day (business) | 200 calls/hour | Stories have separate limits |
| TikTok | 20 videos/day | Varies | Creator vs business account |
| Reddit | 1 post per 10 min (new accounts) | 60 requests/min | Karma-gated |
| YouTube | 100 videos/day (verified) | 10K units/day | Quota cost per operation |

### Rate Limit Manager

```python
import time
from collections import defaultdict
from datetime import datetime, timedelta

class RateLimitManager:
    """Tracks and enforces per-platform rate limits."""

    def __init__(self):
        self.windows = defaultdict(list)  # platform -> list of timestamps

    def can_post(self, platform: str) -> bool:
        """Check if posting is allowed right now."""
        limits = {
            "linkedin": {"max_per_hour": 10, "max_per_day": 100},
            "twitter": {"max_per_15min": 10, "max_per_3hours": 50},
            "instagram": {"max_per_hour": 5, "max_per_day": 25},
            "tiktok": {"max_per_hour": 3, "max_per_day": 20},
            "reddit": {"max_per_10min": 1, "max_per_hour": 5},
        }

        platform_limits = limits.get(platform, {"max_per_hour": 5})
        now = datetime.now()

        for window_name, limit in platform_limits.items():
            minutes = int(window_name.split("per_")[1].replace("min", "").replace("hour", ""))
            if "hour" in window_name:
                minutes *= 60

            window_start = now - timedelta(minutes=minutes)
            count_in_window = sum(
                1 for ts in self.windows[platform]
                if ts > window_start
            )

            if count_in_window >= limit:
                return False

        return True

    def record_post(self, platform: str):
        """Record a successful post."""
        self.windows[platform].append(datetime.now())

        # Cleanup old entries (older than 24 hours)
        cutoff = datetime.now() - timedelta(hours=24)
        self.windows[platform] = [
            ts for ts in self.windows[platform] if ts > cutoff
        ]

    def wait_until_available(self, platform: str, timeout_seconds: int = 3600):
        """Block until the platform accepts posts, or timeout."""
        start = datetime.now()
        while not self.can_post(platform):
            if (datetime.now() - start).seconds > timeout_seconds:
                raise TimeoutError(f"Rate limit timeout for {platform}")
            time.sleep(60)  # Check every minute
```

### Handling Rate Limit 429s

```python
def post_with_retry(platform: str, content: dict, max_retries: int = 5) -> dict:
    """Post content with exponential backoff on rate limits."""

    rate_limiter = RateLimitManager()

    for attempt in range(max_retries):
        if not rate_limiter.can_post(platform):
            wait_time = min(60 * (2 ** attempt), 3600)  # Cap at 1 hour
            time.sleep(wait_time)
            continue

        try:
            result = publish_to_platform(platform, content)
            rate_limiter.record_post(platform)
            return {"status": "published", "result": result}

        except RateLimitError as e:
            retry_after = int(e.headers.get("Retry-After", 60))
            time.sleep(retry_after + 5)  # Add buffer

        except PlatformError as e:
            if attempt == max_retries - 1:
                return {"status": "failed", "error": str(e), "attempts": attempt + 1}
            time.sleep(30 * (attempt + 1))

    return {"status": "failed", "error": "Max retries exceeded"}
```

## Engagement Tracking

### Real-Time Monitoring

```python
def track_post_engagement(post_id: str, platform: str, duration_hours: int = 24):
    """Track post engagement for a specified duration."""

    checkpoints = [1, 2, 4, 8, 24]  # Hours to check
    checkpoint_idx = 0
    start_time = datetime.now()

    while checkpoint_idx < len(checkpoints):
        target_hour = checkpoints[checkpoint_idx]
        elapsed = (datetime.now() - start_time).total_seconds() / 3600

        if elapsed >= target_hour:
            metrics = fetch_platform_metrics(platform, post_id)

            # Compare against benchmarks
            benchmark = get_benchmark(platform, metrics.get("content_type"))
            performance = {
                "post_id": post_id,
                "hour": target_hour,
                "metrics": metrics,
                "vs_benchmark": {
                    k: f"{(metrics[k] / benchmark[k] - 1) * 100:+.1f}%"
                    for k in metrics if k in benchmark
                }
            }

            # Alert on underperformance
            if target_hour == 4 and _is_underperforming(metrics, benchmark):
                hermes_tools.send_alert(
                    "content-ops",
                    f"⚠️ Post {post_id} on {platform} underperforming at 4h mark"
                )

            checkpoint_idx += 1

        time.sleep(300)  # Check every 5 minutes
```

### Engagement Benchmarks (per platform)

```yaml
benchmarks:
  linkedin:
    text_post:
      impression_to_engagement: 0.02    # 2% engagement rate
      click_through_rate: 0.015
      comment_rate: 0.005
    carousel:
      impression_to_engagement: 0.04
      click_through_rate: 0.03
      save_rate: 0.02

  twitter:
    single_tweet:
      impression_to_engagement: 0.01
      retweet_rate: 0.003
      like_rate: 0.02
    thread:
      impression_to_engagement: 0.03
      retweet_rate: 0.01
      reply_rate: 0.01

  instagram:
    reel:
      impression_to_engagement: 0.05
      share_rate: 0.02
      save_rate: 0.03
    carousel:
      impression_to_engagement: 0.04
      save_rate: 0.05
    story:
      tap_forward_rate: 0.15   # Lower is better
      tap_back_rate: 0.05
      exit_rate: 0.10
```

### Weekly Performance Report

```python
def generate_weekly_report(start_date: str) -> dict:
    """Generate a weekly social media performance report."""

    platforms = ["linkedin", "twitter", "instagram", "tiktok"]
    report = {}

    for platform in platforms:
        posts = fetch_posts_in_range(platform, start_date, days=7)
        metrics = aggregate_metrics(posts)

        report[platform] = {
            "total_posts": len(posts),
            "total_impressions": metrics["impressions"],
            "total_engagements": metrics["engagements"],
            "avg_engagement_rate": metrics["engagement_rate"],
            "top_post": max(posts, key=lambda p: p["engagement_rate"]),
            "worst_post": min(posts, key=lambda p: p["engagement_rate"]),
            "follower_change": metrics["follower_change"],
        }

    # Cross-platform insights
    best_platform = max(report.items(), key=lambda x: x[1]["avg_engagement_rate"])
    report["insights"] = {
        "best_platform": best_platform[0],
        "best_content_type": _identify_best_content_type(report),
        "recommendation": _generate_strategy_recommendation(report),
    }

    return report
```

## Content Calendar Management

### Google Sheets / Notion Integration

Store your content calendar in a tool your team can review:

```python
def sync_content_calendar():
    """Sync the content calendar between Hermes and a reviewable source."""

    # Fetch next week's plan from Notion
    calendar = hermes_tools.notion_query_database(
        database_id="content_calendar",
        filter={"property": "Week", "date": {"equals": next_week_start()}}
    )

    # Let team review and modify
    for item in calendar:
        if item["Status"] == "needs_review":
            hermes_tools.send_alert(
                "content-ops",
                f"📋 Content item ready for review: {item['Title']} for {item['Platform']}"
            )

    # Once approved, queue for publishing
    approved = [item for item in calendar if item["Status"] == "approved"]
    for item in approved:
        queue_post(item)
```

## Emergency Content Pauses

Sometimes you need to pause all scheduled content — product issues, PR situations, or world events:

```python
def emergency_pause_all(reason: str):
    """Immediately pause all scheduled social media posts."""

    # Cancel all queued posts
    queued = hermes_tools.cron_list(filter="social_publish")
    for job in queued:
        hermes_tools.cron_pause(job["id"])

    # Log the reason
    hermes_tools.send_alert(
        "content-ops",
        f"🚨 EMERGENCY PAUSE: All social publishing paused.\nReason: {reason}\n"
        f"Review and manually resume when appropriate."
    )

    # Create a review task
    hermes_tools.create_task(
        title="Review paused social content",
        description=f"All social publishing paused due to: {reason}",
        priority="high"
    )
```

## Production Checklist

Before deploying your social publishing pipeline:

- [ ] Rate limit manager tested against each platform's actual limits
- [ ] Content queue with at least 48 hours of buffer
- [ ] Emergency pause mechanism tested and documented
- [ ] Platform API credentials rotated on schedule
- [ ] Content approval workflow for high-risk posts (promotional, controversial topics)
- [ ] Engagement monitoring with anomaly detection
- [ ] Weekly automated performance reports
- [ ] A/B testing framework for post formats and times
- [ ] Backup publishing method (manual) documented
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
