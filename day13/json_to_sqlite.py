import json
import sqlite3

# Step 1: Read JSON file
with open("output/valid_posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

print("JSON records loaded:", len(posts))

# Step 2: Connect to SQLite database
connection = sqlite3.connect("posts.db")

# Step 3: Create cursor
cursor = connection.cursor()

# Step 4: Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    userId INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT
)
""")

# Step 5: Prepare records for insertion
records = [
    (
        post["userId"],
        post["id"],
        post["title"],
        post["body"]
    )
    for post in posts
]

# Step 6: Insert records without duplicating existing IDs
cursor.executemany("""
INSERT OR IGNORE INTO posts (userId, id, title, body)
VALUES (?, ?, ?, ?)
""", records)

# Step 7: Save database changes
connection.commit()

# Step 8: Verify inserted records
cursor.execute("SELECT COUNT(*) FROM posts")
total_records = cursor.fetchone()[0]

print("Total records in SQLite:", total_records)

# Step 9: Close connection
connection.close()

print("JSON data successfully loaded into SQLite!")