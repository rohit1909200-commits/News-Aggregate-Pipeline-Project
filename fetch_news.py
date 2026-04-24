import requests
import pandas as pd

def fetch_news():
    urls = [
        "https://api.spaceflightnewsapi.net/v4/articles",
        "https://api.spaceflightnewsapi.net/v4/blogs",
        "https://api.spaceflightnewsapi.net/v4/reports"
    ]

    news_list = []

    for url in urls:
        try:
            req = requests.get(url)
            
            if req.status_code != 200:
                continue
            data = req.json()
            
            for i in data["results"]:
                news_list.append({
                    "title":i["title"],
                    "source":i["news_site"],
                    "date":i.get("published_at",""),
                    "url":i.get("url","")
                })
        except Exception as e:
            print(f"Error is {e}")
    df = pd.DataFrame(news_list)
    return df