import sqlite3

# Connect to database
connection = sqlite3.connect("posts.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    userId INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT
)
""")

# Save changes
connection.commit()

print("Database connected successfully!")
print("Posts table created successfully!")

# Close connection
connection.close()