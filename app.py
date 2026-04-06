import streamlit as st

from scraper.blog_scraper import scrape_blog
from scraper.youtube_scraper import scrape_youtube
from scraper.pubmed_scraper import scrape_pubmed

from utils.chunking import chunk_text
from utils.tagging import extract_tags
from utils.language import detect_language
from scoring.trust_score import calculate_trust_score


def process_content(data):
    text = data.get("content", "")

    data["language"] = detect_language(text)
    data["topic_tags"] = extract_tags(text)
    data["content_chunks"] = chunk_text(text)
    data["region"] = "global"
    data["trust_score"] = calculate_trust_score(data)

    return data


st.set_page_config(page_title="AI Content Trust Analyzer", layout="wide")

st.title("AI Content Trust Analyzer")
st.write("Analyze Blogs, YouTube Videos, and PubMed Articles")

source_type = st.selectbox(
    "Select Source Type",
    ["Blog", "YouTube", "PubMed"]
)

user_input = st.text_input("Enter URL or PubMed ID")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter a valid input")
    else:
        with st.spinner("Processing..."):
            try:
                if source_type == "Blog":
                    data = scrape_blog(user_input)
                elif source_type == "YouTube":
                    data = scrape_youtube(user_input)
                elif source_type == "PubMed":
                    data = scrape_pubmed(user_input)

                result = process_content(data)

                st.success("Analysis Complete")

                st.subheader("Trust Score")
                st.write(result["trust_score"])

                st.subheader("Topic Tags")
                st.write(result["topic_tags"])

                st.subheader("Language")
                st.write(result["language"])

                st.subheader("Author")
                st.write(result.get("author", "Unknown"))

                st.subheader("Published Date")
                st.write(result.get("published_date", "Unknown"))

                st.subheader("Content Preview")
                for chunk in result["content_chunks"][:3]:
                    st.write("- " + chunk)

            except Exception as e:
                st.error(str(e))