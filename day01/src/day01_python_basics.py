
import json
from pathlib import Path

# Day 1: Python basics for Data Engineering

orders = [
    {"order_id": 101, "customer": "Ravi", "amount": 1200},
    {"order_id": 102, "customer": "Priya", "amount": 800},
    {"order_id": 103, "customer": "Ravi", "amount": 1500},
    {"order_id": 104, "customer": "Arjun", "amount": 500},
    {"order_id": 105, "customer": "Priya", "amount": 2200}
]


# 1. Count orders
def count_orders(orders):
    return len(orders)


# 2. Calculate total revenue
def calculate_total_revenue(orders):
    return sum(order["amount"] for order in orders)


# 3. Calculate average order value
def calculate_average_order_value(orders):
    if not orders:
        return 0

    return calculate_total_revenue(orders) / len(orders)


# 4. Filter orders above a given amount
def filter_large_orders(orders, minimum_amount):
    return [
        order for order in orders
        if order["amount"] > minimum_amount
    ]


# 5. Calculate revenue for each customer
def calculate_customer_revenue(orders):
    customer_revenue = {}

    for order in orders:
        customer = order["customer"]
        amount = order["amount"]

        if customer not in customer_revenue:
            customer_revenue[customer] = 0

        customer_revenue[customer] += amount

    return customer_revenue


# 6. Find the customer with the highest revenue
def find_highest_revenue_customer(customer_revenue):
    if not customer_revenue:
        return None, 0

    highest_customer = None
    highest_revenue = 0

    for customer, revenue in customer_revenue.items():
        if revenue > highest_revenue:
            highest_customer = customer
            highest_revenue = revenue

    return highest_customer, highest_revenue


# 7. Load orders from a JSON file
def load_orders_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    return None


# 8. Run the exercises
if __name__ == "__main__":
    print("Total orders:", count_orders(orders))
    print("Total revenue:", calculate_total_revenue(orders))
    print("Average order value:", calculate_average_order_value(orders))

    print("\nOrders above 1000:")
    for order in filter_large_orders(orders, 1000):
        print(order)

    customer_revenue = calculate_customer_revenue(orders)
    print("\nRevenue by customer:", customer_revenue)

    highest_customer, highest_revenue = (
        find_highest_revenue_customer(customer_revenue)
    )
    print("Highest revenue customer:", highest_customer)
    print("Highest revenue:", highest_revenue)

    json_path = Path(__file__).resolve().parents[1] / "data" / "orders.json"
    json_orders = load_orders_from_json(json_path)

    if json_orders is not None:
        print("\nOrders loaded from JSON:", len(json_orders))
        print("JSON revenue:", calculate_total_revenue(json_orders))
