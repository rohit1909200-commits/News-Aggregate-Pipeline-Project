import mysql.connector
from config import sql
from summary import generate_summary

def store_news(df):
    temp_config = sql.copy()
    temp_config.pop("database")

    conn = mysql.connector.connect(**temp_config)
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {sql['database']}")
    cursor.execute(f"USE {sql['database']}")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title TEXT,
        source VARCHAR(255),
        date VARCHAR(100),
        url TEXT,
        topic VARCHAR(100),
        sentiment VARCHAR(50),
        urgency VARCHAR(50)
    )
    """)

    cursor.execute("TRUNCATE TABLE news")

    df = df[[
        "title", "source", "date", "url",
        "topic", "sentiment", "urgency"
    ]]

    data = list(df.itertuples(index=False, name=None))

    cursor.executemany("""
    INSERT INTO news (title, source, date, url, topic, sentiment, urgency)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, data)

    conn.commit()
    generate_summary(cursor)

    conn.close()