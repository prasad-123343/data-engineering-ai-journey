orders = [
    {
        "order_id": 201,
        "customer": "Ravi",
        "price": 200,
        "quantity": 2
    },
    {
        "order_id": 202,
        "customer": "Priya",
        "quantity": 3
    },
    {
        "order_id": 203,
        "customer": "Arjun",
        "price": "unknown",
        "quantity": 1
    }
]



def validate_order(order):
    required_fields = [
        "order_id",
        "customer",
        "price",
        "quantity"
    ]
    if not isinstance(order, dict):
         return False, "Order must be a dictionary"
    # 1. Check required fields first
    for field in required_fields:
        if field not in order:
            return False, f"Missing required field: {field}"

    # 2. Validate customer name
    if not isinstance(order["customer"], str) or not order["customer"].strip():
        return False, "Customer name cannot be empty"

    # 3. Validate order_id
    if type(order["order_id"]) is not int:
        return False, "Order ID must be an integer"

    # 4. Validate price
    price = order["price"]

    if type(price) not in (int, float):
        return False, "Price must be numeric"

    if price < 0:
        return False, "Price cannot be negative"

    # 5. Validate quantity
    quantity = order["quantity"]

    if type(quantity) is not int:
        return False, "Quantity must be an integer"

    if quantity <= 0:
        return False, "Quantity must be a positive integer"

    return True, "Valid order"


def process_orders(orders):
    valid_orders = []
    rejected_orders = []

    for order in orders:
        is_valid, reason = validate_order(order)

        if is_valid:
            valid_orders.append(order)
        else:
            rejected_orders.append({
                "order": order,
                "reason": reason
            })

    return valid_orders, rejected_orders



valid_orders, rejected_orders = process_orders(orders)

print("Valid orders:")
print(valid_orders)

print("\nRejected orders:")
for rejected in rejected_orders:
    print(rejected["order"])
    print("Reason:", rejected["reason"])