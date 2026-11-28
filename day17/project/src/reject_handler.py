
import csv
from pathlib import Path



def save_rejected_records(rejected_records):
    """Save rejected records and their validation errors to CSV."""

    if not rejected_records:
        print("No rejected records to save.")
        return

    project_dir = Path(__file__).resolve().parent.parent
    rejected_file = project_dir / "data" / "rejected_sales.csv"

    fieldnames = [
        "order_id",
        "customer_id",
        "product_id",
        "sale_date",
        "quantity",
        "unit_price",
        "rejection_reason"
    ]

    with open(
        rejected_file,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in rejected_records:
            record = item["record"]

            writer.writerow({
                **record,
                "rejection_reason": "; ".join(item["errors"])
            })

    print(f"Saved {len(rejected_records)} rejected records.")
    print(f"Rejected file: {rejected_file}")
