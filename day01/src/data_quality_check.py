orders = [
    {"order_id": 101, "customer": "Ravi", "amount": 1200},
    {"order_id": 102, "customer": "Priya", "amount": 800},
    {"order_id": 101, "customer": "Ravi", "amount": 1200},
    {"order_id": 103, "customer": "Arjun", "amount": -500},
    {"order_id": 104, "customer": "Priya", "amount": 2200}
]

# create an empty list to store valid orders
valid_orders = []

# create an empty list to store rejected orders
rejected_orders = []

# Create a way to track order IDs that have already been processed.
processed_order_ids = set() 


# Loop through each order and check whether its order ID is duplicated.

for order in orders:
    if order["order_id"] in processed_order_ids:
        rejected_orders.append(order)
        continue


    processed_order_ids.add(order["order_id"])    

    if order["amount"] < 0:         
        rejected_orders.append(order)
        continue
    valid_orders.append(order)

print("Total Orders:", len(orders))
print("Valid Orders:", len(valid_orders))
print("Rejected Orders:", len(rejected_orders))
print("Valid Order Details:", valid_orders)