import csv
import os
from pathlib import Path

# Resolve file paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

file_path = PROJECT_DIR / "data" / "raw" / "customers.csv"
report_path = PROJECT_DIR / "logs" / "data_quality_report.txt"

# Read environment variable
project_name = os.getenv("PROJECT_NAME", "unknown_project")

# Track data quality
seen_ids = set()
duplicate_ids = []
missing_id_count = 0
valid_records = 0
invalid_records = 0
total_records = 0

# Read and validate CSV records
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_records += 1
        customer_id = row["customer_id"].strip()

        if not customer_id:
            missing_id_count += 1
            invalid_records += 1
            continue

        if customer_id in seen_ids:
            duplicate_ids.append(customer_id)
            invalid_records += 1
        else:
            seen_ids.add(customer_id)
            valid_records += 1

# Create report
report = f"""
CUSTOMER DATA QUALITY REPORT
----------------------------
Project: {project_name}
Total records: {total_records}
Valid records: {valid_records}
Invalid records: {invalid_records}
Unique customer IDs: {len(seen_ids)}
Missing customer IDs: {missing_id_count}
Duplicate IDs: {duplicate_ids}
"""

# Display report
print(report)

# Save report
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(report)

print("Report saved to:", report_path)
