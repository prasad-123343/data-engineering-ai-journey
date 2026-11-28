
import os
import psycopg


def get_connection():
    """Create a PostgreSQL connection using environment variables."""

    password = os.getenv("DB_PASSWORD")

    if not password:
        raise ValueError(
            "DB_PASSWORD environment variable is not configured."
        )

    connection = psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "data_analytics"),
        user=os.getenv("DB_USER", "postgres"),
        password=password
    )

    return connection


def get_dimension_lookups():
    """Retrieve customer and product dimension key mappings."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT customer_id, customer_key
                FROM dim_customers
            """)

            customer_lookup = {
                customer_id: customer_key
                for customer_id, customer_key in cursor.fetchall()
            }

            cursor.execute("""
                SELECT product_id, product_key
                FROM dim_products
            """)

            product_lookup = {
                product_id: product_key
                for product_id, product_key in cursor.fetchall()
            }

        return customer_lookup, product_lookup

    finally:
        connection.close()
