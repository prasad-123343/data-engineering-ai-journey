
# orders = [
#     {"customer": "Ravi", "amount": 500},
#     {"customer": "Mahesh", "amount": 1000},
#     {"customer": "Ravi", "amount": 750},
#     {"customer": "Priya", "amount": 600}
# ]

# customer_report = {}

# for order in orders:
#     customer = order["customer"]
#     amount = order["amount"]

#     if customer not in customer_report:
#         customer_report[customer] = {
#             "order_count": 0,
#             "total_revenue": 0
#         }

#     customer_report[customer]["order_count"] += 1
#     customer_report[customer]["total_revenue"] += amount

# print(customer_report)







# # Exercise 2: Validate incoming orders and record rejection reasons

# validation_orders = [
#     {"customer": "Ravi", "amount": 500},
#     {"customer": "Mahesh", "amount": None},
#     {"customer": "Ravi", "amount": 750},
#     {"customer": "Priya", "amount": -100}
# ]

# valid_orders = []
# rejected_orders = []

# for order in validation_orders:
#     amount = order["amount"]

#     if amount is None or amount < 0:
#         if amount is None:
#             reason = "missing_amount"
#         else:
#             reason = "negative_amount"

#         rejected_orders.append({
#             "order": order,
#             "reason": reason
#         })

#     else:
#         valid_orders.append(order)

# print("Valid orders:", len(valid_orders))
# print("Rejected orders:", len(rejected_orders))

# print("Valid records:", valid_orders)
# print("Rejected records:", rejected_orders)





# # Exercise 3  - avoid duplicate orders


# # Exercise 3: Detect duplicate orders

# duplicate_orders = [
#     {"order_id": 101, "customer": "Ravi", "amount": 500},
#     {"order_id": 102, "customer": "Priya", "amount": 600},
#     {"order_id": 101, "customer": "Ravi", "amount": 500}
# ]

# processed_order_ids = set()
# unique_orders = []
# duplicate_records = []

# for order in duplicate_orders:
#     order_id = order["order_id"]

#     if order_id not in processed_order_ids:
#         processed_order_ids.add(order_id)
#         unique_orders.append(order)
#     else:
#         duplicate_records.append(order)

# print("Unique orders:", len(unique_orders))
# print("Duplicate orders:", len(duplicate_records))
# print("Accepted records:", unique_orders)
# print("Duplicate records:", duplicate_records)




# # Exercise 4: Handle missing customer data

# customer_orders = [
#     {"order_id": 201, "customer": "Ravi", "amount": 500},
#     {"order_id": 202, "customer": "", "amount": 300},
#     {"order_id": 203, "customer": "Priya", "amount": 600}
# ]

# valid_customer_orders = []
# rejected_customer_orders = []

# for order in customer_orders:
#     customer = order["customer"]

#     if customer is None or customer.strip() == "":
#         rejected_customer_orders.append({
#             "order" :order,
#             "reason": "missing_customer"

#         })
#     else:
#         valid_customer_orders.append(order)

# print("Valid customer orders:", len(valid_customer_orders))
# print("Rejected customer orders:", len(rejected_customer_orders))
# print("Valid records:", valid_customer_orders)
# print("Rejected records:", rejected_customer_orders)







orders_to_process = [
    {"order_id": 301, "customer": "Ravi", "amount": 500},
    {"order_id": 302, "customer": None, "amount": 300},
    {"order_id": 301, "customer": "Ravi", "amount": 500},
    {"order_id": 303, "customer": "Priya", "amount": -100},
    {"order_id": 304, "customer": "Mahesh", "amount": 700},
    {"order_id": 305, "customer": "   ", "amount": 200}
]

accepted_orders = []
rejected_orders = []
processed_order_ids = set()

total_revenue = 0

for order in orders_to_process:

    order_id = order["order_id"]
    customer = order["customer"]
    amount = order["amount"]

    # Check for duplicate order ID
    if order_id in processed_order_ids:
        rejected_orders.append({
            "order": order,
            "reason": "Duplicate order ID"
        })
        continue

    # Mark order ID as processed
    processed_order_ids.add(order_id)

    # Check customer name
    if customer is None or customer.strip() == "":
        rejected_orders.append({
            "order": order,
            "reason": "Missing or empty customer name"
        })
        continue

    # Check amount
    if amount is None or amount < 0:
        rejected_orders.append({
            "order": order,
            "reason": "Missing or negative amount"
        })
        continue

    # Accept the order
    accepted_orders.append(order)
    total_revenue += amount


# Final report
print("Accepted orders:", len(accepted_orders))
print("Total revenue:", total_revenue)

print("\nAccepted orders:")
for order in accepted_orders:
    print(order)

print("\nRejected orders:")
for rejected in rejected_orders:
    print(rejected)