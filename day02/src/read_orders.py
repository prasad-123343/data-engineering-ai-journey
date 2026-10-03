
import json


# Step 1: Load orders from JSON
def load_orders(filename):
    try:
        with open(filename, "r") as file:
            orders = json.load(file)

        if not isinstance(orders, list):
            print("Error: JSON must contain a list of orders.")
            return None

        return orders

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON.")
        return None


# Step 2: Validate each order
def validate_order(order):
    if not isinstance(order, dict):
        return False, "Order must be a dictionary"

    if not isinstance(order.get("customer"), str) or not order["customer"].strip():
        return False, "Customer name is missing"

    if type(order.get("price")) not in (int, float):
        return False, "Price must be numeric"

    if order["price"] < 0:
        return False, "Price cannot be negative"

    if type(order.get("quantity")) is not int:
        return False, "Quantity must be an integer"

    if order["quantity"] <= 0:
        return False, "Quantity must be positive"

    return True, "Valid order"


# Step 3: Separate valid and invalid orders
def separate_orders(orders):
    valid_orders = []
    invalid_orders = []

    for order in orders:
        is_valid, message = validate_order(order)

        if is_valid:
            valid_orders.append(order)
        else:
            invalid_orders.append((order, message))

    return valid_orders, invalid_orders


# Step 4: Analyze revenue from valid orders
def analyze_customer_revenue(orders):
    customer_revenue = {}

    for order in orders:
        customer = order["customer"]
        total = order["price"] * order["quantity"]

        if customer in customer_revenue:
            customer_revenue[customer] += total
        else:
            customer_revenue[customer] = total

    if not customer_revenue:
        return {
            "customer_revenue": {},
            "highest_revenue_customer": None,
            "high_revenue_customers": {},
            "count_high_revenue_customers": 0
        }

    highest_customer = max(
        customer_revenue,
        key=customer_revenue.get
    )

    highest_amount = customer_revenue[highest_customer]

    high_revenue_customers = {
        customer: revenue
        for customer, revenue in customer_revenue.items()
        if revenue > 1500
    }

    return {
        "customer_revenue": customer_revenue,
        "highest_revenue_customer": (highest_customer, highest_amount),
        "high_revenue_customers": high_revenue_customers,
        "count_high_revenue_customers": len(high_revenue_customers)
    }


# Step 5: Run the pipeline
orders = load_orders("orders.json")

if orders is not None:
    valid_orders, invalid_orders = separate_orders(orders)

    print("\n--- Data Validation Report ---")
    print("Total orders:", len(orders))
    print("Valid orders:", len(valid_orders))
    print("Invalid orders:", len(invalid_orders))

    print("\n--- Invalid Records ---")
    for order, reason in invalid_orders:
        print("Order:", order, "| Reason:", reason)

    result = analyze_customer_revenue(valid_orders)

    print("\n--- Validated Revenue Report ---")
    print("Customer revenue:", result["customer_revenue"])
    print("Highest revenue customer:", result["highest_revenue_customer"])
    print("High revenue customers:", result["high_revenue_customers"])
    print("Count:", result["count_high_revenue_customers"])
    print(
        "Total valid revenue:",
        sum(result["customer_revenue"].values())
    )