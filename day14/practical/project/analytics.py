
from decimal import Decimal


def calculate_order_metrics(orders):
    """Calculate overall order and revenue metrics."""

    total_orders = len(orders)

    completed_orders = [
        order for order in orders
        if order[3] == "completed"
    ]

    cancelled_orders = [
        order for order in orders
        if order[3] == "cancelled"
    ]

    total_revenue = sum(
        (order[2] for order in orders),
        Decimal("0.00")
    )

    completed_revenue = sum(
        (order[2] for order in completed_orders),
        Decimal("0.00")
    )

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else Decimal("0.00")
    )

    return {
        "total_orders": total_orders,
        "completed_orders": len(completed_orders),
        "cancelled_orders": len(cancelled_orders),
        "total_revenue": total_revenue,
        "completed_revenue": completed_revenue,
        "average_order_value": average_order_value
    }


def print_report(metrics, customer_revenue):
    """Display the analytics report."""

    print("\nORDER ANALYTICS REPORT")
    print("=" * 35)

    print("Total orders:", metrics["total_orders"])
    print("Completed orders:", metrics["completed_orders"])
    print("Cancelled orders:", metrics["cancelled_orders"])
    print("Total revenue:", metrics["total_revenue"])
    print("Completed sales revenue:", metrics["completed_revenue"])
    print("Average order value:", metrics["average_order_value"])

    print("\nCUSTOMER REVENUE SUMMARY")
    print("=" * 45)

    for customer in customer_revenue:
        customer_id, name, order_count, revenue = customer

        print(
            f"Customer: {name} | "
            f"ID: {customer_id} | "
            f"Completed orders: {order_count} | "
            f"Revenue: {revenue}"
        )
