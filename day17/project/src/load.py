
from src.database import get_connection


def load_sales(records):
    """Load transformed sales records safely into PostgreSQL."""

    if not records:
        print("No records to load.")
        return

    connection = get_connection()

    inserted_count = 0
    skipped_count = 0

    try:
        with connection.cursor() as cursor:

            date_lookup_query = """
                SELECT date_key
                FROM dim_date
                WHERE full_date = %s
            """

            insert_query = """
                INSERT INTO fact_sales (
                    order_id,
                    customer_key,
                    product_key,
                    sale_date,
                    date_key,
                    quantity,
                    unit_price
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id, product_key)
                DO NOTHING
                RETURNING sale_id
            """

            for record in records:

                # Verify that the date exists in dim_date
                cursor.execute(
                    date_lookup_query,
                    (record["sale_date"],)
                )

                date_result = cursor.fetchone()

                if date_result is None:
                    raise ValueError(
                        f"Date not found in dim_date: "
                        f"{record['sale_date']}"
                    )

                date_key = date_result[0]

                # Insert the sales record
                cursor.execute(
                    insert_query,
                    (
                        record["order_id"],
                        record["customer_key"],
                        record["product_key"],
                        record["sale_date"],
                        date_key,
                        record["quantity"],
                        record["unit_price"]
                    )
                )

                inserted_row = cursor.fetchone()

                if inserted_row is not None:
                    inserted_count += 1
                else:
                    skipped_count += 1

        connection.commit()

        print("Sales loading completed.")
        print(f"Records received: {len(records)}")
        print(f"Records inserted: {inserted_count}")
        print(f"Duplicate records skipped: {skipped_count}")

    except Exception:
        connection.rollback()
        print("Loading failed. Transaction rolled back.")
        raise

    finally:
        connection.close()
