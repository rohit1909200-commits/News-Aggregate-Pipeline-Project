def generate_summary(cursor):
    cursor.execute("SELECT title, source, topic, sentiment, urgency FROM news")
    rows = cursor.fetchall()

    with open("Summary.txt", "w") as f:
        for r in rows:
            f.write(f"Title: {r[0]}\n")
            f.write(f"Source: {r[1]}\n")
            f.write(f"Topic: {r[2]}\n")
            f.write(f"Sentiment: {r[3]}\n")
            f.write(f"Urgency: {r[4]}\n")
            f.write("--" * 40 + "\n")