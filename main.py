import json
import os

from scraper.blog_scraper import scrape_blog
from scraper.youtube_scraper import scrape_youtube
from scraper.pubmed_scraper import scrape_pubmed

from utils.text_processing import process_content
from scoring.trust_score import calculate_trust_score


def main():
    
    blog_urls = [
        "https://machinelearningmastery.com/what-is-machine-learning/",
        "https://www.analyticsvidhya.com/blog/",
        "https://towardsdatascience.com/"
    ]

    youtube_urls = [
        "https://www.youtube.com/watch?v=aircAruvnKk",
        "https://www.youtube.com/watch?v=7eh4d6sabA0"
    ]

    pubmed_ids = [
        "31452104"
    ]


    all_data = []

    for url in blog_urls:
        try:
            data = scrape_blog(url)
            data = process_content(data)
            data["trust_score"] = calculate_trust_score(data)

            all_data.append(data)
            print(f"✅ Blog processed: {url}")

        except Exception as e:
            print(f"❌ Blog failed: {url} | Error: {e}")

   
    for url in youtube_urls:
        try:
            data = scrape_youtube(url)
            data = process_content(data)
            data["trust_score"] = calculate_trust_score(data)

            all_data.append(data)
            print(f"✅ YouTube processed: {url}")

        except Exception as e:
            print(f"❌ YouTube failed: {url} | Error: {e}")

    for pmid in pubmed_ids:
        try:
            data = scrape_pubmed(pmid)
            data = process_content(data)
            data["trust_score"] = calculate_trust_score(data)

            all_data.append(data)
            print(f"✅ PubMed processed: {pmid}")

        except Exception as e:
            print(f"❌ PubMed failed: {pmid} | Error: {e}")

    os.makedirs("output", exist_ok=True)

    blogs = []
    youtube = []
    pubmed = []

    for item in all_data:
        if item.get("source_type") == "blog":
            blogs.append(item)
        elif item.get("source_type") == "youtube":
            youtube.append(item)
        elif item.get("source_type") == "pubmed":
            pubmed.append(item)

    with open("output/blogs.json", "w") as f:
        json.dump(blogs, f, indent=4)

    with open("output/youtube.json", "w") as f:
        json.dump(youtube, f, indent=4)

    with open("output/pubmed.json", "w") as f:
        json.dump(pubmed, f, indent=4)

    print("\n✅ All data saved in output folder!")


if __name__ == "__main__":
    main()