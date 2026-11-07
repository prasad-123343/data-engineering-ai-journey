import json
import sqlite3
from pathlib import Path


def load_to_sqlite():

    output_file = Path("output") / "valid_posts.json"
    database_file = Path("posts.db")

    with open(output_file, "r", encoding="utf-8") as file:
        posts = json.load(file)

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title TEXT,
            body TEXT
        )
    """)

    cursor.executemany("""
        INSERT OR IGNORE INTO posts (id, userId, title, body)
        VALUES (?, ?, ?, ?)
    """, [
        (post["id"], post["userId"], post["title"], post["body"])
        for post in posts
    ])

    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM posts")
    total_records = cursor.fetchone()[0]

    print("Records read from JSON:", len(posts))
    print("Total records in SQLite:", total_records)

    connection.close()