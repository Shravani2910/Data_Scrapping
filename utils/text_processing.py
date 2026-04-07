# utils/text_processing.py

from utils.language import detect_language
from utils.tagging import extract_tags
from utils.chunking import chunk_text


def process_content(data):
    text = data.get("content", "")

    # Language detection
    data["language"] = detect_language(text)

    # Topic tagging
    data["topic_tags"] = extract_tags(text)

    # Chunking
    data["content_chunks"] = chunk_text(text)

    return data