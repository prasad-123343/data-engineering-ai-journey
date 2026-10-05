import csv


# STEP 1: Read orders from the CSV file
def read_orders(file_path):
    orders = []

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            orders.append(row)

    return orders


# STEP 2: Convert CSV values from strings to Python data types
def convert_orders(row):
    try:
        order_id = int(row["order_id"])
        customer = row["customer"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        return {
            "order_id": order_id,
            "customer": customer,
            "price": price,
            "quantity": quantity
        }, ""

    except ValueError:
        return row, "Invalid numeric value"


# STEP 3: Validate the converted order
def validate_order(order):
    if order["customer"] == "":
        return False, "Customer is empty"

    if order["price"] < 0:
        return False, "Price is negative"

    if order["quantity"] <= 0:
        return False, "Quantity is invalid"

    if order["order_id"] <= 0:
        return False, "Order ID is invalid"

    return True, ""


# STEP 4: Write valid orders to a CSV file
def write_orders(file_path, orders):
    fieldnames = ["order_id", "customer", "price", "quantity"]

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(orders)


# STEP 5: Write invalid orders and rejection reasons to a CSV file
def write_invalid_orders(file_path, orders):
    fieldnames = ["order_id", "customer", "price", "quantity", "reason"]

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(orders)


# STEP 6: Run the complete CSV data pipeline
def main():

    # 6.1 Read the raw CSV data
    orders = read_orders("day03/data/orders.csv")

    # 6.2 Create lists for successfully converted
    #     and conversion-failed records
    converted_orders = []
    conversion_invalid_orders = []

    # 6.3 Convert each CSV record
    for order in orders:
        converted_order, conversion_reason = convert_orders(order)

        if conversion_reason != "":
            order["reason"] = conversion_reason
            conversion_invalid_orders.append(order)
        else:
            converted_orders.append(converted_order)

    # 6.4 Create lists for valid and invalid orders
    valid_orders = []
    invalid_orders = conversion_invalid_orders.copy()

    # 6.5 Validate every successfully converted order
    for order in converted_orders:
        is_valid, reason = validate_order(order)

        if is_valid:
            valid_orders.append(order)
        else:
            order["reason"] = reason
            invalid_orders.append(order)

    # 6.6 Calculate total revenue from valid orders only
    total_revenue = 0

    for order in valid_orders:
        revenue = order["price"] * order["quantity"]
        total_revenue = total_revenue + revenue

    # 6.7 Display pipeline results
    print("Valid orders:")
    print(valid_orders)

    print("Invalid orders:")
    print(invalid_orders)

    print("Total revenue: " + str(total_revenue))

    # 6.8 Write valid orders to the output CSV
    write_orders(
        "day03/output/valid_orders.csv",
        valid_orders
    )

    # 6.9 Write invalid orders to the output CSV
    write_invalid_orders(
        "day03/output/invalid_orders.csv",
        invalid_orders
    )


# STEP 7: Start the pipeline when this file is executed directly
if __name__ == "__main__":
    main()