def calculate_trust_score(data):
    score = 0

    # Author credibility
    if data['author'] and data['author'] != "Unknown":
        score += 0.25

    # Domain authority
    if any(x in data['source_url'] for x in ["edu", "gov", "nih"]):
        score += 0.25

    # Recency
    if "2023" in data['published_date'] or "2024" in data['published_date']:
        score += 0.2

    # Source type boost
    if data['source_type'] == "pubmed":
        score += 0.2

    # Content quality heuristic
    if len(data.get("content_chunks", [])) > 5:
        score += 0.1

    return round(min(score, 1.0), 2)