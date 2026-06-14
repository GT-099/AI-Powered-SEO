from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

videos = [
{
    "author": "cyrus-shepard",
    "video_id": "YSvvHN17w10",
    "title": "Why Your Number 1 Rankings Are Failing - Adsy Talks ep 10",
    "published_date": "2026-06-09"
},
{
    "author": "cyrus-shepard",
    "video_id": "9KNHBpnVryo",
    "title": "Google Rankings Multiply AI Citations",
    "published_date": "2026-06-09"
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