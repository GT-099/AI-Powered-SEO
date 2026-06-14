# Post by Cyrus Shepard
- URL: https://www.linkedin.com/posts/cyrusshepard_google-posted-further-details-about-the-2mb-activity-7444811173088092160-L_LA
- Date posted: 2026-04-11
- Collected: 2026-06-13

## Content
Shares Google's details about the 2MB fetch limit for Googlebot per URL:
- Googlebot stops fetch at exactly 2MB cutoff
- Renders everything before cutoff as if it were a complete page
- Everything after cutoff is ignored
- External resources (CSS, JS, excluding media/fonts) have their own limits
- Most sites won't hit this limit per Gary Illyes

Practical tip: if content isn't getting indexed on very large pages, check page size.

## Notes
Technical SEO post — relevant for AI-powered content production teams managing
large pages or programmatic content at scale. Content beyond 2MB cutoff is
invisible to Googlebot and therefore to AI Overviews.