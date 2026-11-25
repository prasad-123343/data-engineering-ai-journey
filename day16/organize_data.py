import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).parent

RAW_FILE = PROJECT_DIR / "data_lake" / "raw" / "customers.csv"

PROCESSED_FILE = PROJECT_DIR / "data_lake" / "processed" / "customers.csv"

REJECTED_FILE = PROJECT_DIR / "data_lake" / "processed" / "rejected_customers.csv"


valid_records = []
rejected_records = []

with open(RAW_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if (
            row["customer_id"].strip()
            and row["name"].strip()
            and row["city"].strip()
        ):
            valid_records.append(row)
        else:
            rejected_records.append(row)

with open(PROCESSED_FILE, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["customer_id", "name", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(valid_records)



with open(REJECTED_FILE, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["customer_id", "name", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rejected_records)


total_records = len(valid_records) + len(rejected_records)

print("\nDATA QUALITY SUMMARY")
print("--------------------")
print("Total records:", total_records)
print("Valid records:", len(valid_records))
print("Rejected records:", len(rejected_records))

if total_records > 0:
    success_rate = (len(valid_records) / total_records) * 100
    print(f"Success rate: {success_rate:.2f}%")