
import json
import os


# --------------------------------------------------
# STEP 1: Define file paths
# --------------------------------------------------

INPUT_FILE = "day12/data/orders_test.json"

OUTPUT_FOLDER = "day12/output"

VALID_FILE = os.path.join(
    OUTPUT_FOLDER,
    "valid_orders.json"
)

REJECTED_FILE = os.path.join(
    OUTPUT_FOLDER,
    "rejected_orders.json"
)


# --------------------------------------------------
# STEP 2: Read JSON input
# --------------------------------------------------

def read_json_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("JSON file loaded successfully.")

        return data

    except FileNotFoundError:
        print("Error: Input file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


# --------------------------------------------------
# STEP 3: Validate individual orders
# --------------------------------------------------

def validate_order(order, processed_order_ids):

    # Check whether the record is a dictionary

    if not isinstance(order, dict):
        return False, "Order must be a JSON object"

    # Check order ID

    order_id = order.get("order_id")

    if (
        not isinstance(order_id, int)
        or isinstance(order_id, bool)
    ):
        return False, "Missing or invalid order_id"

    # Check duplicate order ID

    if order_id in processed_order_ids:
        return False, "Duplicate order_id"

    # Reserve the ID before checking other fields.
    # This prevents a later record from reusing it.

    processed_order_ids.add(order_id)

    # Check customer

    customer = order.get("customer")

    if not isinstance(customer, str) or not customer.strip():
        return False, "Missing or invalid customer"

    # Check amount

    amount = order.get("amount")

    if (
        not isinstance(amount, int)
        or isinstance(amount, bool)
    ):
        return False, "Amount must be an integer"

    if amount <= 0:
        return False, "Amount must be greater than zero"

    # Check city

    city = order.get("city")

    if not isinstance(city, str) or not city.strip():
        return False, "Missing or invalid city"

    return True, "Valid order"


# --------------------------------------------------
# STEP 4: Process all orders
# --------------------------------------------------

def process_orders(orders):

    valid_orders = []
    rejected_orders = []

    processed_order_ids = set()

    for order in orders:

        is_valid, reason = validate_order(
            order,
            processed_order_ids
        )

        if is_valid:

            valid_orders.append(order)

        else:

            rejected_record = {
                "order": order,
                "rejection_reason": reason
            }

            rejected_orders.append(rejected_record)

    return valid_orders, rejected_orders


# --------------------------------------------------
# STEP 5: Save JSON output files
# --------------------------------------------------

def save_json_file(file_path, data):

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )


# --------------------------------------------------
# STEP 6: Generate processing summary
# --------------------------------------------------

def generate_summary(
    total_orders,
    valid_orders,
    rejected_orders
):

    total_revenue = sum(
        order["amount"]
        for order in valid_orders
    )

    print("\n========== PIPELINE SUMMARY ==========")

    print(f"Total Orders: {total_orders}")

    print(f"Valid Orders: {len(valid_orders)}")

    print(f"Rejected Orders: {len(rejected_orders)}")

    print(f"Total Valid Revenue: {total_revenue}")

    print("\n========== VALID ORDER DETAILS ==========")

    for order in valid_orders:

        print(
            f"Order ID: {order['order_id']} | "
            f"Customer: {order['customer']} | "
            f"Amount: {order['amount']}"
        )

    print("\n========== REJECTED ORDER DETAILS ==========")

    for record in rejected_orders:

        order = record["order"]

        print(
            f"Order ID: {order.get('order_id', 'Unknown')} | "
            f"Reason: {record['rejection_reason']}"
        )


# --------------------------------------------------
# STEP 7: Main pipeline execution
# --------------------------------------------------

def main():

    print("Starting JSON Data Pipeline...\n")

    # Read input data

    data = read_json_file(INPUT_FILE)

    if data is None:
        return

    # Extract orders

    orders = data.get("orders")

    if not isinstance(orders, list):
        print("Error: JSON must contain an orders list.")
        return

    total_orders = len(orders)

    print(f"Total records received: {total_orders}")

    # Validate and process orders

    valid_orders, rejected_orders = process_orders(orders)

    # Create output directory if it does not exist

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Save valid and rejected records

    save_json_file(
        VALID_FILE,
        {"orders": valid_orders}
    )

    save_json_file(
        REJECTED_FILE,
        {"rejected_orders": rejected_orders}
    )

    # Display summary

    generate_summary(
        total_orders,
        valid_orders,
        rejected_orders
    )

    print("\nOutput files saved successfully.")

    print(f"Valid records: {VALID_FILE}")

    print(f"Rejected records: {REJECTED_FILE}")

    print("\nJSON Data Pipeline Completed.")


# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()
