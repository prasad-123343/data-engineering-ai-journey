import os
import psycopg


def get_connection():
    """Create a connection to PostgreSQL."""

    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=10,
    )


def get_orders():
    """Retrieve all orders from PostgreSQL."""

    query = """
        SELECT
            order_id,
            customer_id,
            order_amount,
            order_status
        FROM staging.orders
        ORDER BY order_id;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()


def get_customer_revenue():
    """Retrieve completed order revenue for each customer."""

    query = """
        SELECT
            c.customer_id,
            c.customer_name,
            COUNT(o.order_id) AS completed_orders,
            COALESCE(SUM(o.order_amount), 0) AS completed_revenue
        FROM staging.customers AS c
        LEFT JOIN staging.orders AS o
            ON c.customer_id = o.customer_id
            AND o.order_status = 'completed'
        GROUP BY c.customer_id, c.customer_name
        ORDER BY c.customer_id;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
