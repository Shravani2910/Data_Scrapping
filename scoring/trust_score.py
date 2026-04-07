def calculate_trust_score(data):
    score = 0

    # --- your existing logic ---
    if data.get("author"):
        score += 0.2

    if data.get("published_date"):
        score += 0.2

    if data.get("source_type") == "pubmed":
        score += 0.3
    elif data.get("source_type") == "blog":
        score += 0.2
    else:
        score += 0.1

    # --- ADD THESE INSIDE FUNCTION ---
    citation_score = 0.2 if data.get("source_type") == "pubmed" else 0.05

    text = " ".join(data.get("topic_tags", [])).lower()
    medical_score = 0.1 if any(word in text for word in ["health", "medical", "disease"]) else 0

    # --- FINAL SCORE ---
    score += citation_score + medical_score

    return round(min(score, 1.0), 2)