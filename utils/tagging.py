from sklearn.feature_extraction.text import TfidfVectorizer

def extract_tags(text):
    if not text or len(text.strip()) < 50:
        return ["general"]

    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=5)
        X = vectorizer.fit_transform([text])
        return vectorizer.get_feature_names_out().tolist()
    except:
        return ["general"]