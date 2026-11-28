
from datetime import date
from decimal import Decimal


def transform_sales(records, customer_lookup, product_lookup):
    transformed_records = []

    for record in records:

        customer_key = customer_lookup.get(record["customer_id"])
        product_key = product_lookup.get(record["product_id"])

        if customer_key is None:
            raise ValueError(
                f"Unknown customer: {record['customer_id']}"
            )

        if product_key is None:
            raise ValueError(
                f"Unknown product: {record['product_id']}"
            )

        transformed_record = {
            "order_id": int(record["order_id"]),
            "customer_key": customer_key,
            "product_key": product_key,
            "sale_date": date.fromisoformat(record["sale_date"]),
            "quantity": int(record["quantity"]),
            "unit_price": Decimal(record["unit_price"])
        }

        transformed_records.append(transformed_record)

    print(f"Transformed {len(transformed_records)} records.")

    return transformed_records
