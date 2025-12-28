def bengaluru_guard(question: str):
    keywords = [
        "bengaluru", "bangalore", "blr", "silicon valley of india","tourist places"
    ]
    return any(k in question.lower() for k in keywords)


def detect_topic(question: str):
    q = question.lower()

    # ---------------- HISTORY ----------------
    if any(k in q for k in [
        "history", "origin", "founding", "kempegowda",
        "british", "mysore kingdom", "old bangalore"
    ]):
        return "history"

    # ---------------- GEOGRAPHY ----------------
    if any(k in q for k in [
        "geography", "location", "where is",
        "climate", "weather", "altitude",
        "lakes", "topography"
    ]):
        return "geography"

    # ---------------- CULTURE ----------------
    if any(k in q for k in [
        "culture", "festival", "tradition",
        "language", "food", "cuisine",
        "art", "music", "dance", "kannada"
    ]):
        return "culture"

    # ---------------- ECONOMY ----------------
    if any(k in q for k in [
        "economy", "it", "industry",
        "startup", "companies", "tech",
        "software", "business", "employment"
    ]):
        return "economy"

    # ---------------- DEMOGRAPHICS ----------------
    if any(k in q for k in [
        "population", "demographic",
        "people", "census", "literacy",
        "religion", "languages spoken"
    ]):
        return "demographics"

    # ---------------- TOURISM (IMPORTANT FIX) ----------------
    if any(k in q for k in [
        "tourism", "tourist", "tourist places",
        "places to visit", "sightseeing",
        "attractions", "things to see",
        "weekend places", "monuments",
        "parks", "temples", "palace",
        "museums", "churches"
    ]):
        return "tourism"

    return None
