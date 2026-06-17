---
title: Automated Video Production
description: End-to-end video production pipeline — script generation, avatar rendering, post-production, and multi-platform distribution with Hermes
---

# Automated Video Production

Video content dominates engagement metrics across every platform. But producing quality video at scale requires a pipeline that handles scripting, rendering, post-production, and distribution — without human intervention at every step.

This guide covers building an automated video production system with Hermes: tools, pipeline design, script generation strategies, rendering workflows, and platform-specific optimization.

## The Production Pipeline

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Topic   │───▶│  Script  │───▶│  Media   │───▶│  Post-   │───▶│  Publish │
│ Research │    │ Writing  │    │ Creation │    │ Production│    │ & Track  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

Each stage can be automated, but some benefit from human-in-the-loop gates at quality checkpoints.

## Stage 1: Topic Research

Before writing a script, you need to know what to create. The research stage analyzes what's working and identifies opportunities.

### Data Sources

- **YouTube Analytics:** Identify your channel's best-performing topics by watch time, retention, and click-through rate
- **Competitor Analysis:** Track competitor channels for topic gaps and emerging trends
- **Search Trends:** Monitor what your audience is actively searching for
- **Community Feedback:** Analyze comments and engagement for direct audience signals

### Hermes Implementation

```python
def research_video_topics(channel_id: str, competitors: list[str]) -> list[dict]:
    """Research video topics using Hermes tools and knowledge base."""

    # Analyze own channel performance
    own_analytics = hermes_tools.get_youtube_analytics(
        channel_id=channel_id,
        dimensions=["video"],
        metrics=["views", "watchTime", "subscribersGained"]
    )

    # Analyze competitors
    competitor_topics = []
    for competitor in competitors:
        videos = hermes_tools.get_youtube_channel_videos(
            handle=competitor,
            max_results=10
        )
        competitor_topics.extend(videos)

    # Synthesize recommendations
    recommendations = hermes_llm.complete(
        messages=[
            {"role": "system", "content": """Analyze channel performance and competitor data.
            Identify 5 video topic opportunities. For each: topic, estimated performance,
            rationale based on data, suggested format (tutorial, review, commentary, etc.)."""},
            {"role": "user", "content": f"""
            Own performance: {json.dumps(own_analytics)}
            Competitor topics: {json.dumps(competitor_topics)}
            """}
        ],
        tier="premium"
    )

    return recommendations
```

### Scheduling Research

```yaml
# hermes/cron/video_topic_research.yaml
name: video_topic_research
schedule: "0 9 * * 1,4"  # Monday and Thursday
task: video.research.topics
timeout: 600
notify_on: ["failure"]
```

## Stage 2: Script Generation

The script is the foundation. A well-structured script makes the rest of the pipeline predictable.

### Script Structure Template

Every video script should follow a proven structure:

```markdown
# HOOK (0:00-0:15)
[Attention-grabbing opening that states the problem or promise]

# CONTEXT (0:15-0:45)
[Why this topic matters now. Establish credibility.]

# MAIN CONTENT (0:45-5:00)
[Point 1] - [Explanation] - [Example] - [Transition]
[Point 2] - [Explanation] - [Example] - [Transition]
[Point 3] - [Explanation] - [Example] - [Transition]

# RECAP (5:00-5:30)
[Summarize the 3 key takeaways]

# CALL TO ACTION (5:30-6:00)
[What the viewer should do next — subscribe, comment, visit link]
```

### Script Generation with Reflexion

Use Reflexion to ensure script quality before rendering:

```python
def generate_video_script(topic: str, target_duration_seconds: int = 360) -> str:
    """Generate a video script with quality refinement."""

    script = hermes_llm.complete(
        messages=[
            {"role": "system", "content": f"""Write a video script following this structure:
            HOOK (15 sec): Attention-grabbing opening
            CONTEXT (30 sec): Why this matters
            MAIN (80% of time): 3 key points with examples
            RECAP (30 sec): Summarize takeaways
            CTA (15 sec): Clear call to action

            Target duration: {target_duration_seconds} seconds (~{target_duration_seconds // 60} minutes)
            Style: Conversational, engaging, no jargon without explanation.
            Include visual notes [in brackets] for the editor.

            Topic: {topic}"""}
        ],
        tier="standard"
    )

    # Reflexion: Evaluate script quality
    evaluation = hermes_llm.complete(
        messages=[
            {"role": "system", "content": """Evaluate this video script:
            1. Does the hook grab attention in the first 5 seconds?
            2. Is the structure clear (hook → context → points → recap → CTA)?
            3. Are there 3 distinct, actionable points?
            4. Is the language conversational and engaging?
            5. Would this hold viewer attention for the full duration?

            Return PASS or FAIL with specific feedback for each criterion."""},
            {"role": "user", "content": script}
        ],
        tier="lightweight"
    )

    if "FAIL" in evaluation:
        # Refine with feedback
        script = hermes_llm.complete(
            messages=[
                {"role": "system", "content": "Improve this script based on feedback. Keep the same topic and structure."},
                {"role": "user", "content": f"Script: {script}\nFeedback: {evaluation}"}
            ],
            tier="standard"
        )

    return script
```

### Platform-Specific Scripts

Different platforms demand different script styles:

| Platform | Duration | Style | Hook Strategy |
|---|---|---|---|
| YouTube | 5-20 min | Educational, in-depth | Problem statement or bold claim |
| TikTok | 15-60 sec | Fast-paced, trend-driven | Immediate visual hook |
| Instagram Reels | 30-90 sec | Visual, lifestyle | Pattern interrupt |
| LinkedIn Video | 1-3 min | Professional, insight-driven | Data point or counterintuitive take |
| YouTube Shorts | 15-60 sec | Quick tip or reaction | Text overlay with bold statement |

## Stage 3: Media Creation / Avatar Rendering

### Option A: HeyGen Avatar Videos

For talking-head style content without filming:

```python
def create_avatar_video(script: str, output_path: str) -> str:
    """Generate an AI avatar video using HeyGen."""

    # Prepare the script for HeyGen
    segments = parse_script_to_segments(script)  # Split by visual cues

    # Generate avatar video
    video = heygen_client.create_video(
        avatar_id="default_professional",
        voice_id="natural_male_1",
        background="#1a1a2e",  # Dark tech background
        script=segments,
        resolution="1080p",
        output_format="mp4"
    )

    # Download and store
    video_url = video.download(output_path)
    return video_url
```

**Best practices for avatar videos:**
- Keep segments under 90 seconds (avatar attention fatigue)
- Insert B-roll or screen recordings between avatar segments (2-3 per video)
- Use captions — 85% of social video is watched without sound
- Test voice/avatar combinations for audience preference

### Option B: Remotion Programmatic Video

For data-driven, code-generated videos:

```typescript
// Remotion composition for data visualization videos
import { Composition, useCurrentFrame, useVideoConfig } from 'remotion';

const DataVideo: React.FC<{data: ChartData}> = ({data}) => {
    const frame = useCurrentFrame();
    const {fps} = useVideoConfig();
    const seconds = frame / fps;

    return (
        <div style={{background: '#0f0f23', color: 'white', padding: 40}}>
            <h1 style={{opacity: Math.min(seconds, 1)}}>{data.title}</h1>
            <AnimatedChart
                data={data.values}
                progress={Math.min(seconds / 3, 1)}
            />
            <p style={{opacity: Math.max(0, Math.min(seconds - 2, 1))}}>
                {data.insight}
            </p>
        </div>
    );
};
```

Remotion excels for: data visualizations, text animations, screen recordings with overlays, and any video where content is parameterized.

### Option C: FFmpeg Assembly

For compositing existing assets:

```bash
# Assemble intro + main content + outro with transitions
ffmpeg \
  -i intro.mp4 \
  -i content.mp4 \
  -i outro.mp4 \
  -filter_complex "
    [0:v]scale=1920:1080,setdar=16/9[v0];
    [1:v]scale=1920:1080,setdar=16/9[v1];
    [2:v]scale=1920:1080,setdar=16/9[v2];
    [v0][v1]xfade=transition=fade:duration=1:offset=4[f0];
    [f0][v2]xfade=transition=fade:duration=1:offset=304[f1]
  " \
  -map "[f1]" \
  -c:v libx264 -preset medium -crf 23 \
  -c:a aac -b:a 128k \
  final_video.mp4
```

## Stage 4: Post-Production

### Automated Caption Generation

```python
def generate_captions(video_path: str) -> str:
    """Generate and burn captions into the video."""

    # Extract audio and transcribe
    transcript = hermes_tools.transcribe_audio(video_path)

    # Generate SRT subtitle file with timing
    srt_content = format_as_srt(transcript)

    # Burn captions into video using FFmpeg
    captioned_path = video_path.replace(".mp4", "_captioned.mp4")
    subprocess.run([
        "ffmpeg", "-i", video_path,
        "-vf", f"subtitles={srt_path}:force_style='FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3'",
        "-c:a", "copy",
        captioned_path
    ])

    return captioned_path
```

### Thumbnail Generation

Thumbnails drive click-through rate. Automate A/B thumbnail testing:

```python
def generate_thumbnails(video_title: str, script: str) -> list[str]:
    """Generate multiple thumbnail options for A/B testing."""

    thumbnails = []

    for style in ["bold_text", "face_reaction", "comparison", "question"]:
        thumbnail = hermes_tools.generate_image(
            prompt=f"""YouTube thumbnail in {style} style.
            Title: {video_title}
            Key visual: {script[:200]}
            Requirements: High contrast, readable text, 1280x720, compelling.
            No clickbait. Professional but eye-catching.""",
            dimensions="1280x720"
        )
        thumbnails.append(thumbnail)

    return thumbnails
```

### Quality Checklist

Automated post-production checks:

- [ ] Audio levels normalized (-14 LUFS for YouTube)
- [ ] Captions present and synchronized
- [ ] No black frames at start or end
- [ ] Resolution matches target (1080p or 4K)
- [ ] File size optimized (<2GB for YouTube, <500MB for social)
- [ ] End screen elements positioned correctly

## Stage 5: Distribution

### Multi-Platform Publishing

```yaml
# hermes/content/video_distribution.yaml
videos:
  - platform: youtube
    title_template: "{topic}: {hook_summary}"
    description_template: |
      {full_description}

      🔗 Links mentioned:
      {links}

      ⏱ Timestamps:
      {timestamps}

      #hashtag1 #hashtag2 #hashtag3
    tags: [tag1, tag2, tag3, tag4, tag5]
    category: "Science & Technology"
    privacy: "private"  # Start private, review, then public
    schedule: "optimal_time"  # Based on audience analytics

  - platform: tiktok
    clip_duration: 60  # Extract best 60 seconds
    caption: "{hook} — full video on YouTube 🔗"
    hashtags: [fyp, viral_topic, niche_hashtag]
    schedule: "+2h"  # 2 hours after YouTube

  - platform: instagram_reels
    clip_duration: 90
    caption: "{topic} — watch the full breakdown 👆 link in bio"
    schedule: "+4h"
```

### Cross-Platform Content Strategy

Don't upload the same video everywhere. Adapt:

1. **YouTube:** Full video (5-20 min). The canonical version.
2. **TikTok:** Best 60 seconds extracted. Hook-first, fast-paced edit.
3. **Instagram Reels:** Best 90 seconds. More polished visual style.
4. **YouTube Shorts:** 60-second vertical clip with YouTube-native CTAs.
5. **LinkedIn:** 2-3 minute professional cut. Business-focused framing.
6. **Twitter/X:** 2-minute clip with thread context.

### Scheduling Optimization

Post times matter. Analyze your audience data:

```python
def get_optimal_post_time(platform: str, channel_id: str) -> str:
    """Determine best posting time based on historical engagement data."""

    analytics = hermes_tools.get_youtube_analytics(
        channel_id=channel_id,
        dimensions=["dayOfWeek", "hour"],
        metrics=["views", "averageViewDuration"]
    )

    # Find the day-hour combination with highest engagement
    best_slot = max(analytics, key=lambda x: x["views"] * x["averageViewDuration"])

    return f"{best_slot['dayOfWeek']} at {best_slot['hour']}:00"
```

### Performance Tracking

Automate post-publish monitoring:

```python
def track_video_performance(video_id: str, platforms: list[str]):
    """Track video performance for the first 72 hours."""

    # Schedule hourly checks for the first 24 hours
    for hour in range(1, 73):
        metrics = {}

        if "youtube" in platforms:
            yt_data = hermes_tools.get_youtube_video_analytics(video_id)
            metrics["youtube"] = {
                "views": yt_data["views"],
                "watch_time": yt_data["estimatedMinutesWatched"],
                "retention": yt_data["averageViewDuration"],
                "ctr": yt_data.get("clickThroughRate", 0)
            }

        # Alert on anomalies
        if hour == 24 and metrics["youtube"]["ctr"] < 0.04:
            hermes_tools.send_alert(
                channel="content-ops",
                message=f"⚠️ Video {video_id} CTR below 4% at 24h. Consider thumbnail change."
            )

        time.sleep(3600)  # Check hourly
```

## Tools Summary

| Tool | Purpose | Cost Model |
|---|---|---|
| HeyGen | AI avatar video generation | Per-minute credits |
| Remotion | Programmatic React-based video | Self-hosted (compute only) |
| FFmpeg | Video processing, captions, assembly | Free, self-hosted |
| YouTube API | Publishing, analytics | Free (with quota limits) |
| TikTok API | Publishing, analytics | Free (with approval) |
| Instagram Graph API | Reels publishing | Free |
| OpenAI Whisper | Audio transcription | Pay-per-minute |
| FAL / DALL-E | Thumbnail generation | Pay-per-image |

## Common Issues

**Avatar uncanny valley:** Mix avatar segments with screen recordings, B-roll, or graphics. Pure avatar for 10 minutes loses viewers.

**Script too long for rendering:** Always render a 30-second test segment first. Catching a bad voice or avatar choice early saves hours of rendering.

**Platform rejects video:** Check codec, resolution, and duration requirements before uploading. YouTube accepts almost anything; TikTok and Reels are stricter.

**Caption timing drift:** Transcribe audio first, then align captions to the transcript timing rather than predicting timing from script alone.

---

*Next: [Social Publishing](/hermes/content-ops/social/) · [Engagement](/hermes/content-ops/engagement/) · [Outputs & Results](/hermes/outputs/)*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
