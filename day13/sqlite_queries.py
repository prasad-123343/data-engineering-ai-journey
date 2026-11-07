import sqlite3

connection = sqlite3.connect("posts.db")
cursor = connection.cursor()

# Query 1: Total number of posts
cursor.execute("SELECT COUNT(*) FROM posts")
print("Total posts:", cursor.fetchone()[0])

# Query 2: Posts belonging to user 5
cursor.execute("""
SELECT id, title
FROM posts
WHERE userId = 5
""")

print("\nPosts belonging to user 5:")

for row in cursor.fetchall():
    print(row)

# Query 3: Count posts by user
cursor.execute("""
SELECT userId, COUNT(*)
FROM posts
GROUP BY userId
ORDER BY userId
""")

print("\nPost count by user:")

for row in cursor.fetchall():
    print(row)

connection.close()