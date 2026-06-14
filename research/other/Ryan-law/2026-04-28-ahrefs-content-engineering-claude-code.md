# How I Do Content Engineering with Claude Code
- Author: Ryan Law (Director of Content Marketing, Ahrefs)
- Source: Ahrefs Blog
- URL: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
- Published: 2026-04-28
- Collected: 2026-06-13

## Summary
Detailed walkthrough of how Ryan Law built a high-quality AI content automation
system for the Ahrefs blog using Claude Code and 23 custom skill files. The system
generates publish-ready article drafts in 6-12 minutes. As of April 2026, around
15 articles have been published and 30+ updated using this process.

## The 7-Step Content Engineering Process

### 1. Mimic Human Workflows by Chaining Editorial Skills
23 skill files correspond to different parts of the Ahrefs editorial process —
keyword research, topic gap analysis, structural outlining, drafting, and more.
Each skill file includes Markdown-formatted instructions for Claude, best-practice
examples, and formatting instructions. A master skill (blog-pipeline) chains them
all together sequentially, taking a keyword idea through to a nearly finished article.

### 2. Output Every Step for Iteration and Troubleshooting
Every step of the process produces its own output file (e.g., outlines saved to
an outlines folder). This allows diagnosis of exactly where the process went wrong
if an article is bad, and enables restarting from the last good stage.

### 3. Create Test Cases for Recursive Self-Improvement
Uses Anthropic's skill-creator skill to test each stage both with and without skill
file guidance. The LLM reviews outputs and suggests improvements to skill files.
Helps keep skill files short and effective — long bloated skill files make guidance
less likely to be correctly applied.

### 4. Give LLMs Great Data from Great Sources
Claude has access to Ahrefs MCP — pulls real keyword metrics, parent topics,
long-tail variations, questions reports, and SERP overviews directly from Ahrefs
instead of hallucinating SEO data. Skill files mandate specific data sources:
competitor data (top-ranking article analysis), deep research (trusted news/research
sources), and Ahrefs product feature documentation.

### 5. Front-Load Human Direction
A context parameter in the blog-pipeline skill allows high-level human direction
at the START of the process (e.g., "take a 'steal your competitors' best content'
angle, feature Keywords Explorer's Content Gap tool heavily"). Small expert direction
at the start is vastly more effective than lots of editing at the end.

### 6. Build Interactive Previews for Review and Editing
Each generated article is automatically turned into an Ahrefs-style HTML preview
that opens in Chrome for review. Experimenting with interactive previews that allow
accepting/declining updates and leaving inline comments for Claude to action.

### 7. Fork and Personalise
Each team member is encouraged to fork the repo and use Claude Code to modify the
process to their unique specifications — different styles, data sources, and workflows.
Goal: everyone has their own personalised content copilot.

## Key Caveats
- AI content is not good by default — this process works because it mirrors existing
  human editorial process built from decades of content marketing experience
- Only used on topics Ryan understands well enough to validate claims and correct
  misinformation
- No plans to "scale content" — used to maintain an evergreen library, not publish
  thousands of articles
- Goal: automate drudgery, free human effort for research, thought leadership,
  webinars, and system-building

## Tools Used
- Claude Code (primary AI agent)
- Ahrefs MCP (real SEO data integration)
- 23 custom skill files (Markdown-formatted editorial process documentation)
- GitHub (version control for skill files and content pipeline)

## Why This Source Is Relevant
The single most directly relevant article in this research collection — a practitioner
(Director of Content Marketing at a major SEO tool) documenting his exact AI-powered
SEO content production system in detail, including the tools, architecture, caveats,
and philosophy. The "front-load human direction" and "no scaling" principles are
particularly important counterpoints to naive AI content scaling approaches.

## Related Articles by Ryan Law
- AI Content Wasn't Good Enough. Now It Is. (2026-03-16):
  https://ahrefs.com/blog/ai-content-wasnt-good-enough-now-it-is/
- My Complete AI Content Process for Ahrefs (2025-08):
  https://ahrefs.com/blog/my-complete-ai-content-process-for-ahrefs/
- Update: AI Overviews Reduce Clicks by 58% (2026-02-04):
  https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/
- 74% of New Webpages Include AI Content (2025-05-19):
  https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/