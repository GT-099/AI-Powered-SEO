from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

videos = [
     {
        "author": "ross-simmonds",
        "video_id": "axTH6nKDUY4",
        "title": "Keynote Speaker Demo Reel - Content, SEO and AI That Drive Pipeline",
        "published_date": "2026-04-15"
    },
    {
        "author": "ross-simmonds",
        "video_id": "MFx3FYW58Ls",
        "title": "Your Old SEO Strategy Is Outdated - ROGEO Proves It",
        "published_date": "2026-05-06"
    },
    {
        "author": "ross-simmonds",
        "video_id": "Rnsy-aEEOgs",
        "title": "The Rise of the Fractional CMO - How AI Is Creating a 5M Marketing Opportunity",
        "published_date": "2026-06-05"
    },
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text).strip('-')
    return text

for video in videos:
    author = video["author"]
    video_id = video["video_id"]
    title = video["title"]
    date = video["published_date"]

    folder = f"research/youtube-transcripts/{author}"
    os.makedirs(folder, exist_ok=True)

    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        full_text = " ".join([snippet.text for snippet in fetched])

        slug = slugify(title)
        filename = f"{date}-{slug}.md"
        filepath = os.path.join(folder, filename)

        content = f"""# {title}
- Author: {author}
- URL: https://www.youtube.com/watch?v={video_id}
- Published: {date}
- Collected: 2026-06-13

## Transcript

{full_text}
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"OK Saved: {filepath}")

    except Exception as e:
        print(f"FAILED for {title} ({video_id}): {e}")