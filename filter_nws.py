import string
def process_news(df):
    keywords = {
        "AI": ["ai", "artificial intelligence", "machine learning"],
        "Python": ["python"],
        "Climate": ["climate", "environment", "earth"],
        "Finance": ["finance", "market", "economy"],
        "Space": ["space", "nasa", "rocket", "orbit", "mission", "station"]
    }

    def get_sentiment(title):
        word = title.split()
        
        positive = ["growth", "success", "rise", "increase", "boost", "improve",
        "record", "launch", "advance", "achievement", "safe",
        "surge", "gain", "strong", "win", "progress"]

        negative = ["crash", "loss", "decline", "fall", "drop", "risk",
        "failure", "issue", "delay", "problem", "damage",
        "error", "concern", "cut", "weak", "threat"]

        
        # if any(word in title for word in positive):
        #     return "positive"
        # elif any(word in title for word in negative):
        #     return "negative"
        # else:
        #     return "neutral"
        
        for w in word:
            for p in positive:
                if p in w:
                    return("positive")
                    

            for n in negative:
                if n in w:
                    return("negative")
                    

        return("neutral")

    def get_urgency(title):
        title = title.split()
        
        breaking = ["breaking", "alert", "just in"]
        important = ["launch", "mission", "rocket", "nasa", "spacex", "satellite", "test"]

        if any(word in title for word in breaking):
            return "breaking"
        elif any(word in title for word in important):
            return "important"
        else:
            return "normal"
        
        
    def get_topic(title):
        title = title.lower()

        if any(word in title for word in ["ai", "artificial intelligence", "machine learning"]):
            return "AI"
        elif "python" in title:
            return "Python"
        elif any(word in title for word in ["climate", "environment", "earth"]):
            return "Climate"
        elif any(word in title for word in ["finance", "market", "economy"]):
            return "Finance"
        elif any(word in title for word in ["space", "nasa", "rocket", "orbit", "mission", "station"]):
            return "Space"
        else:
            return "Other"
        
        
        
    

    df["sentiment"] = df["title"].apply(get_sentiment)
    df["urgency"] = df["title"].apply(get_urgency)
    df["topic"] = df["title"].apply(get_topic)

    df = df[df["topic"] != "Other"]

    return df
