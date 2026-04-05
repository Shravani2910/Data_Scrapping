from Bio import Entrez

def scrape_pubmed(pubmed_id):
    
    Entrez.email = "your_email@example.com"

    handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    records = Entrez.read(handle)

    article = records['PubmedArticle'][0]
    article_data = article['MedlineCitation']['Article']

    abstract = article_data.get("Abstract", {})
    
    # Convert abstract to string safely
    abstract_text = ""
    if "AbstractText" in abstract:
        abstract_text = " ".join(abstract["AbstractText"])

    return {
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/",
        "source_type": "pubmed",
        "author": str(article_data.get("AuthorList", [])),
        "published_date": str(article_data.get("Journal", {})),
        "content": abstract_text
    }