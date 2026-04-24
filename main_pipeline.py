from fetch_news import fetch_news
from transform import clean_news
from filter_nws import process_news
from dat_in_sql import store_news

def run_pipeline():
    print("Start of News Pipeline")

    df = fetch_news()

    df = clean_news(df)
    print("Cleaned data")

    df = process_news(df)

    store_news(df)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()