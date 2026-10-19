# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(levelname)s: %(message)s"
# )

# logging.debug("Checking the input")
# logging.info("Pipeline started")
# logging.warning("Order 202 was rejected")
# logging.error("A database write failed")




import logging
import math 

logging.basicConfig(
    level=logging.info,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

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
    if not isinstance(order, dict):
        return False, "Order must be a dictionary"

    required_fields = [
        "order_id",
        "customer",
        "price",
        "quantity"
    ]

    for field in required_fields:
        if field not in order:
            return False, f"Missing required field: {field}"

    if not isinstance(order["customer"], str):
        return False, "Customer must be text"

    if not order["customer"].strip():
        return False, "Customer cannot be empty"

    if type(order["order_id"]) is not int:
        return False, "Order ID must be an integer"

    if order["order_id"] <= 0:
        return False, "Order ID must be positive"

    price = order["price"]

    if type(price) not in (int, float):
        return False, "Price must be numeric"

    if not math.isfinite(price):
        return False, "Price must be finite"

    if price < 0:
        return False, "Price cannot be negative"

    quantity = order["quantity"]

    if type(quantity) is not int or quantity <= 0:
        return False, "Quantity must be a positive integer"

    return True, "Valid order"


def process_orders(orders):
    valid_orders = []
    rejected_orders = []

    logging.info("Pipeline started")
    logging.info("Orders received: %d", len(orders))

    for order in orders:
        order_id = (
            order.get("order_id", "unknown")
            if isinstance(order, dict)
            else "unknown"
        )

        logging.debug("Validating order %s", order_id)

        is_valid, reason = validate_order(order)

        if is_valid:
            total = order["price"] * order["quantity"]

            valid_orders.append({
                **order,
                "total": total
            })

            logging.info(
                "Order %s accepted; total=%s",
                order_id,
                total
            )
        else:
            rejected_orders.append({
                "order_id": order_id,
                "reason": reason
            })

            logging.warning(
                "Order %s rejected: %s",
                order_id,
                reason
            )

    logging.info("Valid orders: %d", len(valid_orders))
    logging.info("Rejected orders: %d", len(rejected_orders))
    logging.info("Pipeline finished")

    return valid_orders, rejected_orders


valid_orders, rejected_orders = process_orders(orders)

print("\nValid orders:")
print(valid_orders)

print("\nRejected orders:")
print(rejected_orders)