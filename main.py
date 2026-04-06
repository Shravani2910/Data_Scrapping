from scraper.blog_scraper import scrape_blog
from scraper.youtube_scraper import scrape_youtube
from scraper.pubmed_scraper import scrape_pubmed

from utils.chunking import chunk_text
from utils.tagging import extract_tags
from utils.language import detect_language
from scoring.trust_score import calculate_trust_score

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import json
import json
import os

os.makedirs("output", exist_ok=True)

blogs = []
youtube = []
pubmed = []

for item in all_data:
    if item["source_type"] == "blog":
        blogs.append(item)
    elif item["source_type"] == "youtube":
        youtube.append(item)
    elif item["source_type"] == "pubmed":
        pubmed.append(item)

with open("output/blogs.json", "w") as f:
    json.dump(blogs, f, indent=4)

with open("output/youtube.json", "w") as f:
    json.dump(youtube, f, indent=4)

with open("output/pubmed.json", "w") as f:
    json.dump(pubmed, f, indent=4)

print("✅ Data saved in separate files")

def process_content(data):
    """
    Enrich scraped data with:
    - language
    - topic tags
    - content chunks
    - trust score
    """
    text = data.get("content", "")

    # Language detection
    data["language"] = detect_language(text)

    # Topic tagging
    data["topic_tags"] = extract_tags(text)

    # Content chunking
    data["content_chunks"] = chunk_text(text)

    # Region 
    data["region"] = "global"

    # Trust score
    data["trust_score"] = calculate_trust_score(data)
    data.pop("content", None)

    return data


def main():
    results = []

    blog_urls = [
    "https://machinelearningmastery.com/what-is-machine-learning/",
    "https://www.analyticsvidhya.com/blog/" ]
    for url in blog_urls:
        try:
            data = scrape_blog(url)
            processed = process_content(data)
            results.append(processed)
            print(f"✅ Blog processed: {url}")
        except Exception as e:
            print(f"❌ Blog failed: {url} | Error: {e}")


    youtube_urls = [
        "https://www.youtube.com/watch?v=aircAruvnKk",
        "https://www.youtube.com/watch?v=7eh4d6sabA0"
    ]

    for url in youtube_urls:
        try:
            data = scrape_youtube(url)
            processed = process_content(data)
            results.append(processed)
            print(f"✅ YouTube processed: {url}")
        except Exception as e:
            print(f"❌ YouTube failed: {url} | Error: {e}")

    pubmed_ids = ["31452104"]

    for pid in pubmed_ids:
        try:
            data = scrape_pubmed(pid)
            processed = process_content(data)
            results.append(processed)
            print(f"✅ PubMed processed: {pid}")
        except Exception as e:
            print(f"PubMed failed: {pid} | Error: {e}")

    try:
        with open("output/scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)

        print("\n All data saved to output/scraped_data.json")
    except Exception as e:
        print(f"Failed to save file: {e}")


if __name__ == "__main__":
    main()