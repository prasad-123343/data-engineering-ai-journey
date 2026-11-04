import json

# Read JSON file
with open("day12/data/orders.json", "r") as file:
    data = json.load(file)

# Access the first order
first_order = data["orders"][0]

print("Order ID:", first_order["order_id"])
print("Customer:", first_order["customer"])
print("Amount:", first_order["amount"])
print("City:", first_order["city"])

# Display all orders
print("\n--- All Orders ---")

for order in data["orders"]:
  print("Order ID:", order["order_id"],
      "| Customer:", order["customer"],
      "| Amount:", order["amount"],
      "| City:", order["city"])


# Calculate total revenue

total_revenue = 0

for order in data["orders"]:
    total_revenue += order["amount"]

print("Total Revenue:", total_revenue)


# Average Order value

total_orders = len(data["orders"])

average_order_value = total_revenue / total_orders

print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)


#Revenue By Customer
revenue_by_customer = {}

for order in data["orders"]:
    customer = order["customer"]
    amount = order["amount"]

    if customer in revenue_by_customer:
        revenue_by_customer[customer] += amount
    else:
        revenue_by_customer[customer] = amount

print("\n--- Revenue by Customer ---")

for customer, revenue in revenue_by_customer.items():
    print(customer + ": " + str(revenue))