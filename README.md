# 🤖 AI Content Trust Analyzer

## 📌 Overview

This project is a multi-source data scraping and trust scoring system that extracts content from blogs, YouTube videos, and PubMed articles, processes it using NLP techniques, and evaluates its reliability.

---

## 🚀 Features

* Multi-source scraping (Blog, YouTube, PubMed)
* Metadata extraction (author, date, etc.)
* Automatic topic tagging
* Language detection
* Content chunking
* Trust score calculation (0–1)
* Streamlit web application

---

## 🧠 Tech Stack

* Python
* BeautifulSoup
* YouTube Transcript API
* Biopython
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
scraper/
utils/
scoring/
output/
app.py
main.py
requirements.txt
```

---

## ⚙️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run scraper

```
python main.py
```

### 3. Run Streamlit app

```
python -m streamlit run app.py
```

---

## 📊 Trust Score Design

The trust score is calculated using multiple factors:

* Author credibility
* Domain authority
* Recency of content
* Content quality
* Source type reliability

The final score is normalized between **0 and 1**.

---

## ⚠️ Edge Cases Handled

* Missing author → penalty applied
* Missing publish date → penalty applied
* No transcript (YouTube) → fallback to description
* Non-English content → processed using language detection
* Long articles → handled using chunking

---

## 🔐 Abuse Prevention

* Low-quality domains are penalized
* Missing medical disclaimers reduce score
* Outdated content receives lower scores
* Suspicious or spam-like content is penalized

---

## 📁 Output

Data is stored in structured JSON files:

* `blogs.json`
* `youtube.json`
* `pubmed.json`

---

## 🌐 Streamlit App

An interactive UI is provided to analyze content in real-time.

https://datascrapping-d2ddirpnaxbs3epudqdhsg.streamlit.app/


---

## ⚡ Limitations

* Some websites block scraping
* Author data may not always be available
* Citation count is approximated
