import csv
import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

csv_file = PROJECT_DIR / "data" / "raw" / "customers.csv"
db_file = PROJECT_DIR / "data" / "customers.db"

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
)
""")

with open(csv_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT OR IGNORE INTO customers
            (customer_id, name, city)
            VALUES (?, ?, ?)
        """, (
            row["customer_id"],
            row["name"],
            row["city"]
        ))

connection.commit()
connection.close()

print("Customer staging table created and loaded successfully.")
