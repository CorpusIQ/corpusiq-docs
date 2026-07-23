---
title: SERP Downloaders — Universal Content & Media Downloader Skills for Hermes
description: Download content from Instagram, TikTok, Vimeo, Bilibili, Unsplash, and SERP images. 6.6K+ combined installs across 6 platform-specific downloader skills.
---

# SERP Downloaders — Setup Guide

**Source:** [serpdownloaders/skills](https://skills.sh/serpdownloaders/skills) (6.6K+ combined installs)
**Category:** Research / Content Acquisition
**Quality Tier:** 🔵 Community

A collection of platform-specific content downloader skills for research, competitive analysis, and content repurposing. Download images and videos from Instagram, TikTok, Vimeo, Bilibili, Unsplash, and Google Images. Useful for Hermes agents conducting market research, competitor content analysis, and content curation.

---

## Installation

```bash
npx skills add serpdownloaders/skills --skill instagram-downloader
npx skills add serpdownloaders/skills --skill tiktok-video-downloader
npx skills add serpdownloaders/skills --skill vimeo-video-downloader
npx skills add serpdownloaders/skills --skill bilibili-downloader
npx skills add serpdownloaders/skills --skill unsplash-downloader
npx skills add serpdownloaders/skills --skill serp-image-downloader
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **instagram-downloader** | 1.1K | Download Instagram posts, reels, stories, and profile data |
| **serp-image-downloader** | 1.1K | Bulk download images from Google/Bing image search results |
| **bilibili-downloader** | 1.1K | Download Bilibili videos with subtitles and metadata |
| **tiktok-video-downloader** | 1.1K | Download TikTok videos without watermarks |
| **unsplash-downloader** | 1.1K | Search and download high-res stock photos from Unsplash |
| **vimeo-video-downloader** | 1.1K | Download Vimeo videos with quality selection |

---

## Quick Start

```bash
# Download competitor Instagram content for analysis
npx skills use serpdownloaders/skills@instagram-downloader

# Gather stock images for content creation
npx skills use serpdownloaders/skills@unsplash-downloader

# Download TikTok videos for competitive research
npx skills use serpdownloaders/skills@tiktok-video-downloader
```

---

## Verification

```bash
npx skills list | grep serpdownloaders
```

---

## Notes

- All skills have uniform 1.1K installs — installed as a bundle
- Instagram and TikTok downloaders useful for competitor content analysis
- Unsplash downloader integrates with content creation workflows
- Quality tier 🔵 Community: 6.6K+ combined installs
