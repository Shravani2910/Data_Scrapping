import requests
from bs4 import BeautifulSoup

def scrape_blog(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.title.text
    paragraphs = [p.text for p in soup.find_all('p')]

    return {
        "source_url": url,
        "source_type": "blog",
        "author": "Unknown",  # improve later
        "published_date": "Unknown",
        "content": " ".join(paragraphs)
    }