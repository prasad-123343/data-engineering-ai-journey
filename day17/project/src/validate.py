
from datetime import datetime
from decimal import Decimal, InvalidOperation


def validate_sales(records):
    valid_records = []
    rejected_records = []

    for record in records:
        errors = []

        # Check required fields
        required_fields = [
            "order_id",
            "customer_id",
            "product_id",
            "sale_date",
            "quantity",
            "unit_price"
        ]

        for field in required_fields:
            if not record.get(field) or not record[field].strip():
                errors.append(f"{field} is missing")

        # Validate date
        if record.get("sale_date", "").strip():
            try:
                datetime.strptime(record["sale_date"], "%Y-%m-%d")
            except ValueError:
                errors.append("Invalid sale_date format")

        # Validate quantity
        try:
            quantity = int(record["quantity"])
            if quantity <= 0:
                errors.append("Quantity must be greater than zero")
        except (ValueError, TypeError):
            errors.append("Quantity must be an integer")

        # Validate unit price
        try:
            unit_price = Decimal(record["unit_price"])
            if not unit_price.is_finite() or unit_price < 0:
                errors.append("Unit price must be non-negative")
        except (InvalidOperation, ValueError, TypeError):
            errors.append("Unit price must be numeric")

        if errors:
            rejected_records.append({
                "record": record,
                "errors": errors
            })
        else:
            valid_records.append(record)

    print(f"Valid records: {len(valid_records)}")
    print(f"Rejected records: {len(rejected_records)}")

    return valid_records, rejected_records
