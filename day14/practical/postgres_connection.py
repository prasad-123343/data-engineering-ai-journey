
import os
import psycopg


def get_orders():
    """Retrieve all orders from PostgreSQL."""

    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "5432")),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:

            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        order_id,
                        customer_id,
                        order_amount,
                        order_status
                    FROM staging.orders
                    ORDER BY order_id;
                """)

                return cur.fetchall()

    except psycopg.Error as error:
        print("Database error:", error)
        return []


def main():
    orders = get_orders()

    print("Orders Retrieved")
    print("----------------")

    for order in orders:
        print(order)

    print("Total records:", len(orders))


if __name__ == "__main__":
    main()
