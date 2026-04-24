import pandas as pd

def clean_news(df):
    df["title"] = df["title"].str.lower()
    df["title"] = df["title"].str.replace(",","")
    df["title"] = df["title"].str.strip()

    return df

