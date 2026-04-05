from youtube_transcript_api import YouTubeTranscriptApi

def scrape_youtube(url):
    video_id = url.split("v=")[-1]

    transcript = ""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t['text'] for t in transcript_list])
    except:
        transcript = "Transcript not available"

    return {
        "source_url": url,
        "source_type": "youtube",
        "author": "Unknown",
        "published_date": "Unknown",
        "content": transcript
    }