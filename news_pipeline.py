import requests
import sqlite3
import datetime
import string


conn = sqlite3.connect("news.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    title TEXT,
    source TEXT,
    date TEXT,
    url TEXT,
    topic TEXT,
    sentiment TEXT,
    urgency TEXT
)
""")

def fetch_news():
    urls = [
        "https://api.spaceflightnewsapi.net/v4/articles",
        "https://api.spaceflightnewsapi.net/v4/blogs",
        "https://api.spaceflightnewsapi.net/v4/reports"
    ]

    all_news = []

    for url in urls:
        response = requests.get(url)
        data = response.json()

        for item in data["results"]:
            news = {
                "title": item["title"],
                "source": item["news_site"],
                "date": item["published_at"],
                "url": item["url"]
            }
            all_news.append(news)

    return all_news

def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

def remove_duplicates(news_list):
    seen = set()
    unique_news = []

    for news in news_list:
        norm_title = normalize(news["title"])

        if norm_title not in seen:
            seen.add(norm_title)
            unique_news.append(news)

    return unique_news


KEYWORDS = {
    "AI": ["ai", "artificial intelligence"],
    "Python": ["python"],
    "Climate": ["climate", "environment"],
    "Finance": ["finance", "stock", "market"]
}

def get_topic(title):
    title = title.lower()

    for topic, words in KEYWORDS.items():
        for word in words:
            if word in title:
                return topic

    return "Other"

def get_sentiment(title):
    title = title.lower()

    if "good" in title or "growth" in title:
        return "positive"
    elif "bad" in title or "crash" in title:
        return "negative"
    else:
        return "neutral"

def get_urgency(title):
    title = title.lower()

    if "breaking" in title:
        return "breaking"
    elif "important" in title:
        return "important"
    else:
        return "normal"

def process_news(news_list):
    processed = []

    for news in news_list:
        topic = get_topic(news["title"])

        if topic != "Other":
            news["topic"] = topic
            news["sentiment"] = get_sentiment(news["title"])
            news["urgency"] = get_urgency(news["title"])
            processed.append(news)

    return processed


def store_news(news_list):
    for news in news_list:
        cursor.execute("""
        SELECT * FROM news WHERE title = ?
        """, (news["title"],))

        if cursor.fetchone() is None:
            cursor.execute("""
            INSERT INTO news VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                news["title"],
                news["source"],
                news["date"],
                news["url"],
                news["topic"],
                news["sentiment"],
                news["urgency"]
            ))

    conn.commit()


def generate_summary():
    file = open("Daily_Summary.txt", "w")

    cursor.execute("SELECT * FROM news")
    rows = cursor.fetchall()

    for row in rows:
        file.write(f"Title: {row[0]}\n")
        file.write(f"Source: {row[1]}\n")
        file.write(f"Topic: {row[4]}\n")
        file.write(f"Sentiment: {row[5]}\n")
        file.write(f"Urgency: {row[6]}\n")
        file.write("-" * 40 + "\n")

    file.close()


raw_data = fetch_news()              
clean_data = remove_duplicates(raw_data)  
final_data = process_news(clean_data)   

store_news(final_data)
generate_summary()

print("Pipeline completed!")