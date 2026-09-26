---
name: social
description: "Create, repurpose, schedule, or review organic social content, short-form video, engagement, and listening. Use content-strategy for the broader plan, ad-creative for paid media, and public-relations for earned media."
metadata:
  version: 2.2.0
---

# Social content

## Before creating content

**Check for product marketing context first.**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Goals
- What's the primary objective? (Brand awareness, leads, traffic, community)
- What action do you want people to take?
- Are you building personal brand, company brand, or both?

### 2. Audience
- Who are you trying to reach?
- What platforms are they most active on?
- What content do they engage with?

### 3. Brand voice
- What's your tone? (Professional, casual, witty, authoritative)
- Any topics to avoid?
- Any specific terminology or style guidelines?

### 4. Resources
- How much time can you dedicate to social?
- Do you have existing content to repurpose?
- Can you create video content?

---

## Platform quick reference

| Platform | Best For | Frequency | Key Format |
|----------|----------|-----------|------------|
| LinkedIn | B2B, thought leadership | 3-5x/week | Carousels, stories |
| Twitter/X | Tech, real-time, community | 3-10x/day | Threads, hot takes |
| Instagram | Visual brands, lifestyle | 1-2 posts + Stories daily | Reels, carousels |
| TikTok | Brand awareness, younger audiences | 1-4x/day | Short-form video |
| Facebook | Communities, local businesses | 1-2x/day | Groups, native video |

For detailed platform strategies, see [references/platforms.md](references/platforms.md).

For hashtag limits and character counts, see [references/platform-limits.md](references/platform-limits.md).

---

## Content pillars framework

Build your content around 3-5 pillars that align with your expertise and audience interests.

### Example for a SaaS founder

| Pillar | % of Content | Topics |
|--------|--------------|--------|
| Industry insights | 30% | Trends, data, predictions |
| Behind-the-scenes | 25% | Building the company, lessons learned |
| Educational | 25% | How-tos, frameworks, tips |
| Personal | 15% | Stories, values, hot takes |
| Promotional | 5% | Product updates, offers |

### Pillar development questions

For each pillar, ask:
1. What unique perspective do you have?
2. What questions does your audience ask?
3. What content has performed well before?
4. What can you create consistently?
5. What aligns with business goals?

---

## Hook formulas

The first line determines whether anyone reads the rest.

### Curiosity hooks
- "I was wrong about [common belief]."
- "The real reason [outcome] happens isn't what you think."
- "[Impressive result], and it only took [surprisingly short time]."

### Story hooks
- "Last week, [unexpected thing] happened."
- "I almost [big mistake/failure]."
- "3 years ago, I [past state]. Today, [current state]."

### Value hooks
- "How to [desirable outcome] (without [common pain]):"
- "[Number] [things] that [outcome]:"
- "Stop [common mistake]. Do this instead:"

### Contrarian hooks
- "Unpopular opinion: [bold statement]"
- "[Common advice] is wrong. Here's why:"
- "I stopped [common practice] and [positive result]."

For post templates and more hooks, see [references/post-templates.md](references/post-templates.md).

**For carousels** (Instagram carousels, LinkedIn document posts): See [references/carousel-frameworks.md](references/carousel-frameworks.md), five slide-by-slide narrative architectures (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough) with framework selection guidance, per-slide copy slots, platform notes, and a production checklist. Pick the framework before writing slides.

---

## Content repurposing system

Turn one piece of content into many. The best social content isn't created from scratch. Extract it from longer-form pillar content and adapt it to each platform.

### Blog post → social content

| Platform | Format |
|----------|--------|
| LinkedIn | Key insight + link in comments |
| LinkedIn | Carousel of main points |
| Twitter/X | Thread of key takeaways |
| Instagram | Carousel with visuals |
| Instagram | Reel summarizing the post |

### Podcast / video → social content

Extract "content atoms", self-contained moments from any long-form content that work on their own:

| Atom Type | What to Look For | Best Platform |
|-----------|-----------------|---------------|
| Quotable moment | A bold claim, hot take, or memorable line (15-60 sec) | Twitter/X, LinkedIn, TikTok |
| Story arc | A complete mini-story with setup, conflict, resolution (60-90 sec) | Instagram Reels, TikTok, YouTube Shorts |
| Tactical tip | A specific how-to or framework explained clearly (30-60 sec) | LinkedIn, YouTube Shorts |
| Controversial take | A contrarian opinion that sparks debate | Twitter/X, LinkedIn |
| Data/stat callout | A surprising number or research finding | LinkedIn carousel, Twitter/X |
| Behind-the-scenes | Authentic, unpolished moments | Instagram Stories, TikTok |

**Podcast repurposing workflow.**
1. **Get transcript.** Use Whisper, Descript, or your podcast host's transcription
2. **Mark timestamps.** Flag the 5-10 best moments while listening or scanning transcript
3. **Extract clips.** Pull video/audio clips for each moment (Descript, Opus Clip, or manual)
4. **Write standalone captions.** Each clip needs context; don't assume the viewer heard the rest
5. **Add subtitles.** Most social video is watched without sound
6. **Schedule across 1-2 weeks.** Spread a single episode across multiple posts

Per episode, aim for the following:
- 3-5 short video clips or audiograms (15-60 sec) for Reels/TikTok/Shorts
- 1-2 LinkedIn text posts from key insights
- 1 Twitter/X thread of takeaways
- 1 carousel summarizing the main framework or list
- 1 newsletter section or blog post from the best segment

### Webinar / live event → social content

| Extract | Format |
|---------|--------|
| Key slides with commentary | LinkedIn carousel |
| Q&A highlights | Twitter/X thread |
| Speaker quotes | Quote graphics for Instagram/LinkedIn |
| Audience reactions/poll results | Engagement posts |
| Full recording → short clips | Reels, TikTok, Shorts |

### Newsletter → social content

| Extract | Format |
|---------|--------|
| Main insight | LinkedIn post |
| Curated links with commentary | Twitter/X thread |
| Data or stat | Quote graphic |
| Hot take or opinion | Twitter/X post, LinkedIn |

### Repurposing workflow

1. **Create pillar content** (blog, video, podcast, webinar, newsletter)
2. **Extract content atoms** (5-10 per piece, quotes, stories, tips, data)
3. **Adapt to each platform** (format, length, and tone)
4. **Write standalone captions** (each post must work without context)
5. **Schedule across the week** (spread distribution, don't dump all at once)
6. **Update and reshare** (evergreen content can repeat every 3-6 months)

---

## Content calendar structure

### Weekly planning template

| Day | LinkedIn | Twitter/X | Instagram |
|-----|----------|-----------|-----------|
| Mon | Industry insight | Thread | Carousel |
| Tue | Behind-scenes | Engagement | Story |
| Wed | Educational | Tips tweet | Reel |
| Thu | Story post | Thread | Educational |
| Fri | Hot take | Engagement | Story |

### Batching strategy (2-3 hours weekly)

1. Review content pillar topics
2. Write 5 LinkedIn posts
3. Write 3 Twitter threads + daily tweets
4. Create Instagram carousel + Reel ideas
5. Schedule everything
6. Leave room for real-time engagement

---

## Engagement strategy

### Daily engagement routine (30 min)

1. Respond to all comments on your posts (5 min)
2. Comment on 5-10 posts from target accounts (15 min)
3. Share/repost with added insight (5 min)
4. Send 2-3 DMs to new connections (5 min)

**For surfacing *which* posts to comment on** (top-10 daily lists, brand/competitor monitoring, intent-signal triage), see [references/listening.md](references/listening.md). Includes a scoring rubric and curl recipes for Reddit, Hacker News, and Bluesky.

### Quality comments

- Add new insight, not just "Great post!"
- Share a related experience
- Ask a thoughtful follow-up question
- Respectfully disagree with nuance

### Building relationships

- Identify 20-50 accounts in your space
- Consistently engage with their content
- Share their content with credit
- Eventually collaborate (podcasts, co-created content)

---

## Analytics & optimization

### Metrics that matter

**Awareness.** Impressions, Reach, Follower growth rate

**Engagement.** Engagement rate, Comments (higher value than likes), Shares/reposts, Saves

**Conversion.** Link clicks, Profile visits, DMs received, Leads attributed

### Weekly review

- Top 3 performing posts (why did they work?)
- Bottom 3 posts (what can you learn?)
- Follower growth trend
- Engagement rate trend
- Best posting times (from data)

### Optimization actions

**If engagement is low.**
- Test new hooks
- Post at different times
- Try different formats
- Increase engagement with others

**If reach is declining.**
- Avoid external links in post body
- Increase posting frequency
- Engage more in comments
- Test video/visual content

---

## Content ideas by situation

### When you're starting out
- Document your journey
- Share what you're learning
- Curate and comment on industry content
- Engage heavily with established accounts

### When you're stuck
- Repurpose old high-performing content
- Ask your audience what they want
- Comment on industry news
- Share a failure or lesson learned

---

## Scheduling best practices

### When to schedule vs. post live

**Schedule.** Core content posts, Threads, Carousels, Evergreen content

**Post live.** Real-time commentary, Responses to news/trends, Engagement with others

### Queue management

- Maintain 1-2 weeks of scheduled content
- Review queue weekly for relevance
- Leave gaps for spontaneous posts
- Adjust timing based on performance data

---

## Reverse engineering viral content

Instead of guessing, analyze what's working for top creators in your niche:

1. **Find creators.** 10-20 accounts with high engagement
2. **Collect data.** 500+ posts for analysis
3. **Analyze patterns.** Hooks, formats, CTAs that work
4. **Codify playbook.** Document repeatable patterns
5. **Layer your voice.** Apply patterns with authenticity
6. **Convert.** Bridge attention to business results

For the complete framework, see [references/reverse-engineering.md](references/reverse-engineering.md).

---

## Short-form video (TikTok, reels, shorts)

Short-form video is the highest-reach format on every major platform. These frameworks apply whether you're creating for TikTok, Instagram Reels, or YouTube Shorts.

### Platform specs

| Platform | Optimal Length | Aspect Ratio | Key Difference |
|----------|---------------|--------------|----------------|
| TikTok | 15-60 sec | 9:16 | Trending sounds, unpolished/authentic feel |
| Reels | 15-30 sec | 9:16 | Polished content, rewards saves/shares |
| Shorts | 30-60 sec | 9:16 | YouTube SEO applies, searchable titles |

### The 3-second rule

You have 3 seconds to stop the scroll. Every video needs three simultaneous hooks:

```
[VISUAL HOOK] + [VERBAL HOOK] + [TEXT OVERLAY]
```

All three should hit in the first second.

### Video structures

**Problem-Solution (15-30 sec).**
```
[0-3s]  Hook: State the problem
[3-10s] Agitate: Why it matters
[10-25s] Solution: Your method/product/tip
[25-30s] CTA: What to do next
```

**List Format (30-60 sec).**
```
[0-3s]  Hook: "X things that [outcome]"
[3-50s] Items: One every 5-8 seconds
[50-60s] CTA
```

**Tutorial (30-60 sec).**
```
[0-3s]  Hook: Show the end result first
[3-8s]  Overview: "Here's how..."
[8-50s] Steps: Quick, clear instructions
[50-60s] Result + CTA
```

### Caption & subtitle best practices

Captions increase watch time by 25-40%. Most social video is watched without sound.

- **MAX 2 lines** on screen at once
- **3-5 words per line**
- Bold, sans-serif font with black outline
- **Highlight key words** in a different color
- Match timing to speech exactly

Tools: CapCut (free), Descript, Captions.ai, Premiere Pro

### Content ideas by type

| Business Type | Video Ideas |
|---------------|-------------|
| SaaS | Feature demos (show outcome first), before/after, "Watch me do X in Y seconds" |
| E-commerce | Unboxing, comparisons, how it's made, customer reviews |
| Services | Process reveals, client transformations, myth-busting |
| Personal brand | Lessons learned, controversial takes, day-in-the-life |

### Common mistakes

1. **Slow hooks.** Don't build up to the point
2. **No text overlay.** Many watch without sound
3. **Poor audio.** Bad audio kills retention instantly
4. **Too long.** If it can be shorter, make it shorter
5. **No CTA.** Tell viewers what to do
6. **Ignoring comments.** Engagement in first hour matters

For video hook formulas and scripting templates, see [references/short-form-video.md](references/short-form-video.md).

---

## Task-specific questions

1. What platform(s) are you focusing on?
2. What's your current posting frequency?
3. Do you have existing content to repurpose?
4. What content has performed well in the past?
5. How much time can you dedicate weekly?
6. Are you building personal brand, company brand, or both?

---

## Related skills

- **copywriting.** For longer-form content that feeds social
- **launch.** For coordinating social with launches
- **emails.** For nurturing social audience via email
- **marketing-psychology.** For understanding what drives engagement

Complete the task only when each deliverable names its platform, audience, goal, format, call to action when needed, and success metric. Mark assumptions where brand voice, source material, or performance data is missing.
