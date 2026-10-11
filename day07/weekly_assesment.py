
# Day 7: Weekly Data Engineering Assessment
# Objective:
# Validate orders, detect duplicate IDs, separate valid and rejected
# records, record rejection reasons, and calculate data-quality metrics.


# Sample input data
orders = [
    {"order_id": 501, "customer": "Ravi", "amount": "500"},
    {"order_id": 502, "customer": "Priya", "amount": -200},
    {"order_id": 503, "customer": "   ", "amount": "300"},
    {"order_id": 501, "customer": "Ravi", "amount": "500"},
    {"order_id": 504, "customer": "Arjun", "amount": "abc"}
]


# Step 1: Initialize tracking variables
valid_orders = []       # Stores orders that pass every validation rule
rejected_orders = []    # Stores rejected orders and their reasons
processed_order_ids = set()  # Tracks IDs already encountered


# Step 2: Process each order
for order in orders:

    # Reset reasons for every new order
    reasons = []

    # Read the order ID
    order_id = order["order_id"]

    # Step 3: Check for duplicate order IDs
    if order_id in processed_order_ids:
        reasons.append("Duplicate order ID")
    else:
        processed_order_ids.add(order_id)
        print("New order ID:", order_id)

    # Step 4: Validate the customer name
    customer = order.get("customer")

    if customer is None or not isinstance(customer, str):
        reasons.append("Missing or invalid customer")
    else:
        # Remove spaces from the beginning and end
        customer = customer.strip()

        # Reject names that are empty after trimming
        if not customer:
            reasons.append("Missing or blank customer")
        else:
            order["customer"] = customer

    # Step 5: Validate and convert the amount
    amount = order.get("amount")

    if amount is None:
        reasons.append("Missing amount")

    elif isinstance(amount, bool):
        # bool is a subclass of int in Python, so reject it explicitly
        reasons.append("Amount must be numeric")

    else:
        try:
            # Convert integer-like strings, such as "500", to integers
            amount = int(amount)

        except (ValueError, TypeError):
            # Conversion fails for values such as "abc"
            reasons.append("Amount must be a valid integer")

        else:
            # Check that the amount is non-negative
            if amount < 0:
                reasons.append("Amount must be zero or greater")
            else:
                order["amount"] = amount

    # Step 6: Classify the order
    # An order is valid only if no validation errors were found.
    if reasons:
        rejected_orders.append({
            "order": order.copy(),
            "reasons": reasons
        })
    else:
        valid_orders.append(order.copy())


# Step 7: Calculate data-quality metrics
total_orders = len(orders)
valid_count = len(valid_orders)
rejected_count = len(rejected_orders)

# Calculate rejection rate safely, including when there are no orders
rejection_rate = (
    rejected_count / total_orders * 100
    if total_orders > 0
    else 0
)

# Every input order must be either valid or rejected
count_check = total_orders == valid_count + rejected_count


# Step 8: Print the final report
print("\n========== DAY 7 PIPELINE REPORT ==========")

print("Valid orders:", valid_orders)
print("Rejected orders:", rejected_orders)

print("\nTotal orders:", total_orders)
print("Valid count:", valid_count)
print("Rejected count:", rejected_count)
print("Rejection rate:", round(rejection_rate, 2), "%")

print(
    "Count consistency:",
    "PASS" if count_check else "FAIL"
)
