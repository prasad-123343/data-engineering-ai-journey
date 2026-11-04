
import json

# ------------------------------------------------
# STEP 1: Read JSON file
# ------------------------------------------------

with open("day12/data/orders_test.json", "r") as file:
    data = json.load(file)


# ------------------------------------------------
# STEP 2: Create storage containers
# ------------------------------------------------

valid_orders = []
rejected_orders = []

processed_order_ids = set()


# ------------------------------------------------
# STEP 3: Validate each order
# ------------------------------------------------

for order in data["orders"]:

    reason = None

    # Validation 1: Check whether order_id exists

    if "order_id" not in order:
        reason = "Missing order_id"

    # Validation 2: Check duplicate order_id

    elif order["order_id"] in processed_order_ids:
        reason = "Duplicate order_id"

    else:
        processed_order_ids.add(order["order_id"])

    # Validation 3: Check customer

    if reason is None:
        customer = order.get("customer")

        if not isinstance(customer, str) or not customer.strip():
            reason = "Missing or invalid customer"

    # Validation 4: Check amount

    if reason is None:
        amount = order.get("amount")

        if isinstance(amount, bool) or not isinstance(amount, int):
            reason = "Amount must be an integer"

        elif amount <= 0:
            reason = "Amount must be greater than zero"

    # Validation 5: Check city

    if reason is None:
        city = order.get("city")

        if not isinstance(city, str) or not city.strip():
            reason = "Missing or invalid city"

    # ------------------------------------------------
    # STEP 4: Separate valid and rejected records
    # ------------------------------------------------

    if reason is None:
        valid_orders.append(order)

    else:
        rejected_orders.append({
            "order": order,
            "reason": reason
        })


# ------------------------------------------------
# STEP 5: Display validation summary
# ------------------------------------------------

print("========== DATA QUALITY REPORT ==========")

print("Total Orders:", len(data["orders"]))
print("Valid Orders:", len(valid_orders))
print("Rejected Orders:", len(rejected_orders))


# ------------------------------------------------
# STEP 6: Display valid records
# ------------------------------------------------

print("\n========== VALID ORDERS ==========")

for order in valid_orders:
    print(order)


# ------------------------------------------------
# STEP 7: Display rejected records
# ------------------------------------------------

print("\n========== REJECTED ORDERS ==========")

for rejected in rejected_orders:

    print("Order:", rejected["order"])
    print("Reason:", rejected["reason"])
    print("-----------------------------------")


# ------------------------------------------------
# STEP 8: Calculate revenue from valid orders
# ------------------------------------------------

total_revenue = 0

for order in valid_orders:
    total_revenue += order["amount"]

print("\n========== VALID DATA SUMMARY ==========")

print("Total Valid Revenue:", total_revenue)
