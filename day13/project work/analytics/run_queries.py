import sqlite3


def run_sql_queries():

    connection = sqlite3.connect("posts.db")
    cursor = connection.cursor()

    # 1. Total number of posts
    cursor.execute("""
        SELECT COUNT(*)
        FROM posts
    """)

    total_posts = cursor.fetchone()[0]
    print("Total posts:", total_posts)

    # 2. Number of posts per user
    cursor.execute("""
        SELECT userId, COUNT(*)
        FROM posts
        GROUP BY userId
        ORDER BY userId
    """)

    print("\nPosts per user:")

    for row in cursor.fetchall():
        print("User:", row[0], "| Posts:", row[1])

    # 3. Posts with IDs greater than 90
    cursor.execute("""
        SELECT id, title
        FROM posts
        WHERE id > 90
        ORDER BY id
    """)

    print("\nPosts with IDs greater than 90:")

    for row in cursor.fetchall():
        print(row)

    connection.close()