 # AI-Powered SEO Content Production — Research Project

This repository collects recent content (YouTube transcripts, LinkedIn posts,
blog articles, and newsletters) from 10 active practitioners in AI-powered SEO
content production, for research and analysis purposes.

## Project Topic
AI-Powered SEO Content Production — how practitioners are using AI to create,
optimize, distribute, and measure content for search engines and AI assistive
engines in 2025-2026.

## Why These Experts?
Each expert was selected because they:
- Actively practice AI-powered SEO/content work (not just write about it)
- Have publicly accessible recent content (last 3-6 months)
- Cover a mix of platforms (YouTube, LinkedIn, newsletters, blogs)
- Represent different angles: technical SEO, content strategy, GEO/AEO,
  brand visibility, data research, and AI content production workflows

## The 10 Experts

### 1. Aleyda Solis
- **Role**: Independent SEO Consultant
- **Platforms**: YouTube (Crawling Mondays) + LinkedIn + Blog
- **Why chosen**: Chosen for her practical AI search measurement frameworks
  (prompt libraries, citation tracking) and consistent weekly publishing.
  Her 2026 blog articles on AI search prompt libraries and ecommerce AI
  citation patterns are among the most detailed practitioner guides available.

### 2. Mike King
- **Role**: Founder, iPullRank
- **Platforms**: YouTube (iPullRank) + LinkedIn
- **Why chosen**: Chosen for his "Machine Media" and "Relevance Engineering"
  frameworks that reframe content production around how machines consume
  content. His Inside SEO Week series features real practitioner case studies
  from across the industry.

### 3. Kevin Indig
- **Role**: Growth Advisor
- **Platforms**: LinkedIn + Substack (Growth Memo)
- **Why chosen**: Chosen for the Growth Memo's original data research —
  clickstream studies (846K sessions), job market salary analysis (946 roles),
  and the "intent compression" concept explaining how AI Overviews are
  changing user behavior at a structural level.

### 4. Lily Ray
- **Role**: VP SEO, Amsive
- **Platforms**: LinkedIn
- **Why chosen**: Chosen for her data on the risks of AI content scaling —
  monitoring 220+ sites showed 54% lost 30%+ traffic after scaling AI content.
  Provides a critical counterpoint to naive "publish more AI content" strategies,
  backed by real algorithmic evidence.

### 5. Garrett Sussman
- **Role**: Content Lead, iPullRank
- **Platforms**: LinkedIn + iPullRank Blog
- **Why chosen**: Chosen for his unique organizational perspective on AI search
  programs, grounded in real discovery calls across companies at different AI
  maturity stages. iPullRank's AI Mode clickstream study (100K+ users) is one
  of the most data-rich practitioner pieces in this collection.

### 6. Ross Simmonds
- **Role**: Founder, Foundation Marketing
- **Platforms**: YouTube + LinkedIn + Blog (rosssimmonds.com)
- **Why chosen**: Chosen for his original SERP data (organic now only 49% of
  the page) and Reddit citation analysis (Reddit cited in 74% of AI Overviews
  across 19 brands). His "two internets" and "Create Once, Distribute Forever"
  frameworks directly inform off-site AI content strategy.

### 7. Ryan Law
- **Role**: Director of Content Marketing, Ahrefs
- **Platforms**: LinkedIn + Ahrefs Blog
- **Why chosen**: Chosen because his April 2026 article documenting a complete
  AI content production system built with Claude Code and 23 skill files is the
  most directly relevant practitioner document to this project's exact topic.
  Also published the definitive AI Overviews CTR impact study (58% decline,
  300K keywords) and 1 billion+ data point AI search research.

### 8. Chima Mmeje
- **Role**: Content Strategist, Moz
- **Platforms**: YouTube (Moz Whiteboard Friday) + LinkedIn
- **Why chosen**: Chosen for Moz's original research on query fan-out behavior
  in Google AI Mode, and her practical entity cluster frameworks that directly
  inform how AI-powered content should be structured and organized for maximum
  AI search visibility.

### 9. Cyrus Shepard
- **Role**: Founder, Zyppy SEO
- **Platforms**: LinkedIn + Substack (Zyppy Signal) + YouTube
- **Why chosen**: Chosen for publishing the most comprehensive evidence-based
  AI citation framework available — 23 scored factors derived from 54 studies,
  patents, and case studies. His 400+ site analysis identifying what separates
  Google traffic winners from losers in 2026 is widely referenced across
  the industry.

### 10. Jason Barnard
- **Role**: CEO, Kalicube
- **Platforms**: LinkedIn + jasonbarnard.com + Kalicube
- **Why chosen**: Chosen as the practitioner with the deepest end-to-end
  methodology for AI-powered content production — Kalicube Process, CFP
  (Claim-Frame-Prove), OPIDC, Cascading Signals, and Funnel Query Pathway.
  The only expert in this collection building specifically for AI search since
  2015, before it was called AI search. Google hired Kalicube to teach
  enterprise brands at Google Marketing Live 2026 Asia Pacific.

See `research/sources.md` for the full list with links, last activity dates,
and detailed rationale for each expert.

## What Was Collected

### YouTube Transcripts (12 videos)
- Aleyda Solis: 2 videos (Dec 2025)
- Mike King / iPullRank: 4 videos (March-April 2026, Inside SEO Week series)
- Ross Simmonds: 3 videos (April-June 2026)
- Chima Mmeje: 1 video (Feb 2026, Moz Whiteboard Friday)
- Cyrus Shepard: 2 videos (June 2026)

### LinkedIn Posts (45 posts total)
- Aleyda Solis: 3 posts
- Mike King: 2 posts
- Kevin Indig: 5 posts
- Lily Ray: 5 posts
- Garrett Sussman: 5 posts
- Ross Simmonds: 6 posts
- Ryan Law: 4 posts
- Chima Mmeje: 3 posts
- Cyrus Shepard: 6 posts
- Jason Barnard: 6 posts

### Articles, Newsletters and Other Content
- Aleyda Solis: 2 blog articles (aleydasolis.com, May-June 2026)
- Kevin Indig: Growth Memo newsletter index (6 articles, Jan-May 2026)
- Garrett Sussman: iPullRank blog article + articles index (2025-2026)
- Ross Simmonds: 1 blog article + website overview (rosssimmonds.com)
- Ryan Law: 2 Ahrefs articles including full Claude Code content system
  breakdown (April 2026)
- Chima Mmeje: Moz Whiteboard Friday 2026 summary
- Cyrus Shepard: Zyppy Signal newsletter index (3 articles, March-May 2026)
- Jason Barnard: Kalicube website overview + 12 Strategy Sandbox articles
  (May-June 2026)

## How Content Was Collected

- **YouTube transcripts**: collected using the `youtube-transcript-api` Python
  library via a custom `fetch_transcripts.py` script, run through Claude Code.
  The script fetches transcripts by video ID and saves each as a structured
  markdown file with title, URL, author, and date metadata.
- **LinkedIn posts**: manually collected from each expert's public LinkedIn
  profile (LinkedIn has no free public API). Raw post text, URLs, and dates
  were formatted into markdown files using Claude Code.
- **Articles and newsletters**: fetched from public URLs and summarized into
  structured markdown files organized by author in `/research/other/`.
- **Reposts excluded**: only original content authored by each expert was
  collected — reposts without substantial added commentary were skipped.
## Repository Structure
research/

├── sources.md                     # Master list of all 10 experts

├── youtube-transcripts/           # Transcripts organized by author

│   ├── aleyda-solis/

│   ├── mike-king/

│   ├── ross-simmonds/

│   ├── chima-mmeje/

│   └── cyrus-shepard/

├── linkedin-posts/                # Posts organized by author

│   ├── aleyda-solis/

│   ├── mike-king/

│   ├── kevin-indig/

│   ├── lily-ray/

│   ├── garrett-sussman/

│   ├── ross-simmonds/

│   ├── ryan-law/

│   ├── chima-mmeje/

│   ├── cyrus-shepard/

│   └── jason-barnard/

└── other/                         # Articles, newsletters, website summaries

├── aleyda-solis/

├── kevin-indig/

├── garrett-sussman/

├── ross-simmonds/

├── ryan-law/

├── chima-mmeje/

├── cyrus-shepard/

└── jason-barnard/
## How Content Was Collected
- **YouTube transcripts**: fetched using `youtube-transcript-api` Python library
  via `fetch_transcripts.py` script in the root of this repo
- **LinkedIn posts**: manually collected from each expert's LinkedIn profile,
  formatted into markdown
- **Articles and newsletters**: fetched and summarized from public URLs,
  organized by author in `/research/other/`
- **Reposts were excluded**: only original content authored by each expert
  was collected

## Key Themes Across the Research
1. **AI Overviews are reducing organic CTR** — Ryan Law (58% CTR drop),
   Cyrus Shepard (branded search declining), Lily Ray (54% of AI content
   sites losing 30%+ traffic)
2. **Traditional SEO fundamentals still drive AI citations** — Cyrus Shepard's
   23-factor analysis, Ryan Law's 1B data point Ahrefs studies
3. **Off-site content now matters as much as on-site** — Ross Simmonds,
   Garrett Sussman (Reddit, YouTube, reviews dominate AI citations)
4. **Content quantity is the wrong goal** — Ryan Law, Jason Barnard, Lily Ray
   all argue against scaling AI content without quality/strategy
5. **New measurement frameworks needed** — Kevin Indig (intent compression),
   Jason Barnard (Funnel Query Pathway, Topical Answer Adoption),
   Cyrus Shepard (AI Citation Ranking Factors)
6. **Entity clarity before content** — Jason Barnard (annotation-first),
   Chima Mmeje (entity clusters, query fan-out)

## Tools Used
- Python (`youtube-transcript-api`) for transcript collection
- Git/GitHub for version control and incremental commits
- Cursor (IDE) for file creation and editing

## Status
✅ Collection complete — all 10 experts fully documented.

## How This Research Supports a Playbook

The collected material is strong enough to support a full AI-powered SEO content
production playbook. Specifically:

- **Content production workflow**: Ryan Law's Claude Code system (23 skill files,
  6-12 minute article generation) provides a replicable technical blueprint
- **Citation strategy**: Cyrus Shepard's 23 AI citation factors + Ross Simmonds'
  Reddit/off-site data provide the targeting framework
- **Measurement**: Jason Barnard's Funnel Query Pathway + Kevin Indig's
  intent compression research provide the measurement methodology
- **Risk management**: Lily Ray's 220-site study + Garrett Sussman's AI Mode
  clickstream data provide the guardrails against common failure patterns
- **Brand positioning**: Jason Barnard's CFP (Claim-Frame-Prove) and Chima
  Mmeje's entity cluster frameworks provide the content structure methodology