
import csv

valid_orders = []
rejected_orders = []
processed_order_ids = set()

# Read and validate orders
with open(
    "day11/data/orders.csv",
    "r",
    encoding="utf-8-sig",
    newline=""
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = row["customer"].strip()
        amount_text = row["amount"].strip()
        reason = ""
        amount = None

        # 1. Check missing customer
        if not customer:
            reason = "Missing customer"

        # 2. Check missing amount
        elif not amount_text:
            reason = "Missing amount"

        # 3. Check whether amount is an integer
        else:
            try:
                amount = int(amount_text)
            except ValueError:
                reason = "Amount is not an integer"

        # 4. Check negative amount only after successful conversion
        if not reason and amount is not None and amount < 0:
            reason = "Negative amount"

        # 5. Check duplicate order ID
        if not reason and row["order_id"] in processed_order_ids:
            reason = "Duplicate order ID"

        # Reject invalid records and save their reasons
        if reason:
            rejected_record = row.copy()
            rejected_record["rejection_reason"] = reason
            rejected_orders.append(rejected_record)
            continue

        # Store valid records
        row["customer"] = customer
        row["amount"] = amount
        valid_orders.append(row)
        processed_order_ids.add(row["order_id"])


# Calculate total revenue
total_revenue = 0

for order in valid_orders:
    total_revenue += order["amount"]

print("Total revenue:", total_revenue)


# Calculate revenue by customer
revenue_by_customer = {}

for order in valid_orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in revenue_by_customer:
        revenue_by_customer[customer] += amount
    else:
        revenue_by_customer[customer] = amount

print("Revenue by customer:", revenue_by_customer)


# Save rejected records to a CSV file
output_path = "day11/data/rejected_orders.csv"

fieldnames = [
    "order_id",
    "customer",
    "amount",
    "city",
    "rejection_reason"
]

with open(
    output_path,
    "w",
    encoding="utf-8",
    newline=""
) as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rejected_orders)


# Print record counts
print("Valid orders:", len(valid_orders))
print("Rejected orders:", len(rejected_orders))
print("Rejected records saved to:", output_path)