
import csv

valid_orders = []
rejected_orders = []
processed_order_ids = set()

# 1. Read the CSV file and validate records
with open(
    "day11/data/orders.csv",
    "r",
    encoding="utf-8-sig",
    newline=""
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_id = row["order_id"].strip()
        customer = row["customer"].strip()
        amount = row["amount"].strip()

        # Check whether customer is missing
        if not customer:
            rejected_orders.append(row)
            continue

        # Check whether amount is missing
        if not amount:
            rejected_orders.append(row)
            continue

        # Convert amount to an integer
        try:
            amount = int(amount)
        except ValueError:
            rejected_orders.append(row)
            continue

        # Reject negative amounts
        if amount < 0:
            rejected_orders.append(row)
            continue

        # Check for duplicate order IDs
        if order_id in processed_order_ids:
            rejected_orders.append(row)
            continue

        # Remember the accepted order ID
        processed_order_ids.add(order_id)

        # Store the validated and transformed record
        row["order_id"] = order_id
        row["customer"] = customer
        row["amount"] = amount
        valid_orders.append(row)


# 2. Display validation results
print("Total input orders:", len(valid_orders) + len(rejected_orders))
print("Valid orders:", len(valid_orders))
print("Rejected orders:", len(rejected_orders))


# 3. Calculate total revenue from valid orders
total_revenue = 0

for order in valid_orders:
    total_revenue += order["amount"]


# 4. Calculate revenue by customer
revenue_by_customer = {}

for order in valid_orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in revenue_by_customer:
        revenue_by_customer[customer] += amount
    else:
        revenue_by_customer[customer] = amount


# 5. Display valid records
print("\nValid records:")

for order in valid_orders:
    print(order)


# 6. Display rejected records
print("\nRejected records:")

for order in rejected_orders:
    print(order)


# 7. Display transformation results
print("\n--- Transformation Summary ---")
print("Total revenue:", total_revenue)
print("Revenue by customer:", revenue_by_customer)
