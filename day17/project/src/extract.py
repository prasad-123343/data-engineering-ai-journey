import csv
from pathlib import Path


def extract_sales(file_path):
    """Read sales records from a CSV file."""

    records = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    print(f"Extracted {len(records)} records.")

    return records