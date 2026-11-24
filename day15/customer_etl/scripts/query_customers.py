import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

db_file = PROJECT_DIR / "data" / "customers.db"

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# Retrieve all customer records
cursor.execute("""
    SELECT
        COUNT(*) AS total_records,
        COUNT(DISTINCT customer_id) AS unique_customer_ids,
        SUM(CASE WHEN name IS NULL OR TRIM(name) = '' THEN 1 ELSE 0 END) AS missing_names,
        SUM(CASE WHEN city IS NULL OR TRIM(city) = '' THEN 1 ELSE 0 END) AS missing_cities
    FROM customers
""")

print("CUSTOMER DATA QUALITY CHECK")
print("---------------------------")
print(cursor.fetchone())



connection.close()
