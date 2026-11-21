
import logging
import psycopg

from database import get_orders, get_customer_revenue
from analytics import calculate_order_metrics, print_report


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """Run the order analytics pipeline."""

    logger.info("Starting order analytics pipeline")

    try:
        orders = get_orders()
        logger.info("Retrieved %d orders", len(orders))

        customer_revenue = get_customer_revenue()
        logger.info(
            "Retrieved %d customer summaries",
            len(customer_revenue)
        )

        metrics = calculate_order_metrics(orders)
        print_report(metrics, customer_revenue)

        logger.info("Pipeline completed successfully")

    except psycopg.Error:
        logger.exception("Database operation failed")
        raise

    except Exception:
        logger.exception("Unexpected pipeline failure")
        raise


if __name__ == "__main__":
    main()
