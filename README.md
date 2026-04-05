# 📊 Multi-Source Data Scraping & Trust Scoring System

## 🚀 Project Overview

This project implements a multi-source data scraping pipeline that extracts structured content from blogs, YouTube videos, and PubMed articles. It enriches the data with metadata, performs topic tagging, and assigns a trust score based on reliability factors.

---

## 🧠 Features

* Scrapes data from:

  * Blogs (HTML parsing)
  * YouTube (transcripts)
  * PubMed (scientific articles)
* Extracts metadata:

  * Author
  * Published date
  * Content
* NLP Processing:

  * Language detection
  * Topic tagging (TF-IDF)
  * Content chunking
* Trust Scoring System (0–1 scale)

---

## 🏗️ Project Structure

```
project/
├── scraper/
├── scoring/
├── utils/
├── output/
├── main.py
```

---

## ⚙️ Tech Stack

* Python
* BeautifulSoup
* YouTube Transcript API
* Biopython (PubMed API)
* Scikit-learn (TF-IDF)
* Langdetect

---

## 📊 Trust Score Logic

The trust score is calculated using:

* Author credibility
* Domain authority (.edu, .gov, PubMed)
* Recency of content
* Source type (scientific vs general)
* Content quality

Final score is normalized between **0 and 1**.

---

## ⚠️ Edge Cases Handled

* Missing metadata
* No transcript available
* Non-English content
* Large content chunking
* Empty or low-quality text

---

## 🛡️ Abuse Prevention

* Penalizes low-authority domains
* Rewards verified sources (PubMed)
* Recency-based decay
* Handles missing or fake metadata

---

## ▶️ How to Run

```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python main.py
```

---

## 📁 Output

Generated file:

```
output/scraped_data.json
```

Contains structured data from all sources.

---

## 🚧 Limitations

* Some websites block scraping
* YouTube metadata is limited
* Basic trust scoring (heuristic-based)

---

## 🌟 Future Improvements

* Use LLMs for advanced tagging
* Integrate domain authority APIs
* Improve author credibility scoring
* Add database storage (MongoDB)

---

## 👩‍💻 Author

Shravani 
