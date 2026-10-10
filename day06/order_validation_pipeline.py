
"""
Day 6: Data Validation and Pipeline Reliability
Purpose:
1. Validate incoming order records.
2. Separate accepted and rejected records.
3. Record rejection reasons.
4. Prevent duplicate order processing.
5. Log pipeline events.
6. Check pipeline counts and calculate rejection rate.
"""

import logging


# ============================================================
# SECTION 1: CONFIGURE LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# SECTION 2: SAMPLE INPUT DATA
# ============================================================

# This represents raw data received from an external source.
# Change individual values to test different failure scenarios.

orders = [
    {"order_id": 101, "customer": "Ravi", "amount": 500},
    {"order_id": 102, "customer": "Priya", "amount": -200},
    {"order_id": 103, "customer": "", "amount": 300}
]


# ============================================================
# SECTION 3: VALIDATE AND CLEAN ONE ORDER
# ============================================================

def validate_order(order, processed_order_ids):
    """
    Validate one order.

    Returns:
        cleaned_order: cleaned record, or None if invalid
        reasons: list of validation errors
    """

    cleaned_order = dict(order)
    reasons = []

    # Step 1: Validate the order ID.
    order_id = cleaned_order.get("order_id")

    if order_id is None or order_id == "":
        reasons.append("Missing order ID")
    elif not isinstance(order_id, (int, str)) or isinstance(order_id, bool):
        reasons.append("Order ID must be an integer or string")
    elif isinstance(order_id, str) and not order_id.strip():
        reasons.append("Order ID cannot be blank")
    elif order_id in processed_order_ids:
        reasons.append("Duplicate order ID")

    # Step 2: Validate and clean the customer name.
    customer = cleaned_order.get("customer")

    if not isinstance(customer, str) or not customer.strip():
        reasons.append("Missing or blank customer")
    else:
        cleaned_order["customer"] = customer.strip()

    # Step 3: Validate and convert the amount.
    amount = cleaned_order.get("amount")

    if amount is None:
        reasons.append("Missing amount")

    elif isinstance(amount, bool):
        # bool is a subclass of int in Python, so reject it explicitly.
        reasons.append("Amount must be numeric")

    elif isinstance(amount, int):
        # Integer amounts are already in the required format.
        pass

    elif isinstance(amount, float):
        # Do not silently convert 500.5 to 500.
        if not amount.is_integer():
            reasons.append("Amount must be a whole number")
        else:
            cleaned_order["amount"] = int(amount)

    elif isinstance(amount, str):
        # Accept integer strings such as "500" or "-200".
        try:
            cleaned_order["amount"] = int(amount.strip())
        except ValueError:
            reasons.append("Amount must be a valid whole number")

    else:
        reasons.append("Amount must be numeric")

    # Step 4: Reject negative amounts.
    # Run this check only if conversion produced a valid integer.
    cleaned_amount = cleaned_order.get("amount")

    if (
        isinstance(cleaned_amount, int)
        and not isinstance(cleaned_amount, bool)
        and cleaned_amount < 0
    ):
        reasons.append("Amount must be zero or greater")

    # Return the cleaned record only when no validation errors exist.
    if reasons:
        return None, reasons

    return cleaned_order, []


# ============================================================
# SECTION 4: PROCESS ALL ORDERS
# ============================================================

def process_orders(raw_orders):
    """
    Process raw orders and separate accepted from rejected records.

    The processed_order_ids set prevents an accepted order ID
    from being accepted again during the same pipeline run.
    """

    valid_orders = []
    rejected_orders = []
    processed_order_ids = set()

    for order in raw_orders:

        # Validate the current record.
        cleaned_order, reasons = validate_order(
            order,
            processed_order_ids
        )

        if reasons:
            # Preserve the original input and its rejection reasons.
            rejected_orders.append({
                "order": dict(order),
                "reasons": reasons
            })

            logger.warning(
                "Order rejected: %s",
                reasons
            )

        else:
            # Record the ID only after the order is accepted.
            processed_order_ids.add(cleaned_order["order_id"])
            valid_orders.append(cleaned_order)

            logger.info(
                "Order accepted: %s",
                cleaned_order["order_id"]
            )

    return valid_orders, rejected_orders


# ============================================================
# SECTION 5: CHECK PIPELINE COUNTS
# ============================================================

def check_pipeline_counts(raw_orders, valid_orders, rejected_orders):
    """
    Check that every input order is accounted for.
    """

    total_orders = len(raw_orders)
    valid_count = len(valid_orders)
    rejected_count = len(rejected_orders)

    if total_orders == valid_count + rejected_count:
        logger.info("Pipeline count check: PASS")
        return True

    logger.error("Pipeline count check: FAIL")
    return False


# ============================================================
# SECTION 6: CALCULATE REJECTION RATE
# ============================================================

def calculate_rejection_rate(raw_orders, rejected_orders):
    """
    Calculate the percentage of input records that were rejected.
    """

    total_orders = len(raw_orders)

    # Avoid division by zero when the input is empty.
    if total_orders == 0:
        return 0.0

    return len(rejected_orders) / total_orders * 100


# ============================================================
# SECTION 7: PRINT THE PIPELINE REPORT
# ============================================================

def print_report(raw_orders, valid_orders, rejected_orders):
    """
    Display the final pipeline results.
    """

    print("\n========== DAY 6 PIPELINE REPORT ==========")

    print("Total orders:", len(raw_orders))
    print("Valid order count:", len(valid_orders))
    print("Rejected order count:", len(rejected_orders))

    print("\nValid orders:")
    print(valid_orders)

    print("\nRejected orders:")
    print(rejected_orders)

    count_check = check_pipeline_counts(
        raw_orders,
        valid_orders,
        rejected_orders
    )

    print("\nPipeline count check:", "PASS" if count_check else "FAIL")

    rejection_rate = calculate_rejection_rate(
        raw_orders,
        rejected_orders
    )

    print("Rejection rate:", round(rejection_rate, 2), "%")


# ============================================================
# SECTION 8: MAIN PROGRAM
# ============================================================

def main():
    """
    Run the pipeline from input through validation and reporting.
    """

    logger.info("Pipeline started")

    valid_orders, rejected_orders = process_orders(orders)

    print_report(
        orders,
        valid_orders,
        rejected_orders
    )

    logger.info("Pipeline finished")


# ============================================================
# SECTION 9: PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()