
# Day 17 - Exercise 3
# Data Quality and Validation Pipeline


# --------------------------------
# 1. SOURCE SALES DATA
# --------------------------------

sales = [
    {
        "order_id": 1001,
        "customer_id": "C101",
        "product_id": "P101",
        "quantity": 2,
        "unit_price": 500
    },
    {
        "order_id": 1002,
        "customer_id": "C102",
        "product_id": "P102",
        "quantity": 0,
        "unit_price": 1000
    },
    {
        "order_id": 1003,
        "customer_id": "C103",
        "product_id": "P103",
        "quantity": -2,
        "unit_price": 200
    },
    {
        "order_id": 1004,
        "customer_id": "C104",
        "product_id": "P104",
        "quantity": 3,
        "unit_price": -100
    },
    {
        "order_id": 1005,
        "customer_id": "C105",
        "product_id": "P105",
        "quantity": 1,
        "unit_price": 750
    },
    {
        "order_id": 1006,
        "customer_id": "",
        "product_id": "P106",
        "quantity": 2,
        "unit_price": 500
    },
    {
        "order_id": 1007,
        "customer_id": "C107",
        "product_id": "P107",
        "quantity": "three",
        "unit_price": 500
    },
    {
        "order_id": 1008,
        "customer_id": "C108",
        "product_id": "P108",
        "quantity": 2,
        "unit_price": "five hundred"
    }
]


# --------------------------------
# 2. DISPLAY SOURCE DATA
# --------------------------------

def display_sales_data(sales_records):

    print("\n========== SOURCE SALES DATA ==========")

    for sale in sales_records:
        print(sale)


# --------------------------------
# 3. VALIDATE SALES RECORDS
# --------------------------------

def validate_sales_records(sales_records):

    valid_records = []
    rejected_records = []

    for sale in sales_records:

        errors = []

        # Check required fields
        required_fields = [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "unit_price"
        ]

        for field in required_fields:

            if (
                field not in sale
                or sale[field] is None
                or sale[field] == ""
            ):
                errors.append(f"{field} is missing")

        # Validate quantity
        quantity = sale.get("quantity")

        if quantity is not None and quantity != "":

            if type(quantity) is not int:
                errors.append("Quantity must be an integer")

            elif quantity <= 0:
                errors.append(
                    "Quantity must be greater than zero"
                )

        # Validate unit price
        unit_price = sale.get("unit_price")

        if unit_price is not None and unit_price != "":

            if type(unit_price) not in (int, float):
                errors.append("Unit price must be numeric")

            elif unit_price < 0:
                errors.append(
                    "Unit price cannot be negative"
                )

        # Separate valid and rejected records
        if errors:

            rejected_records.append({
                "record": sale,
                "errors": errors
            })

        else:
            valid_records.append(sale)

    return valid_records, rejected_records


# --------------------------------
# 4. DISPLAY VALIDATION REPORT
# --------------------------------

def display_validation_report(
    valid_records,
    rejected_records
):

    total_records = len(valid_records) + len(rejected_records)

    print("\n========== VALIDATION SUMMARY ==========")

    print("Total records:", total_records)
    print("Valid records:", len(valid_records))
    print("Rejected records:", len(rejected_records))

    # Display valid records
    print("\n========== VALID RECORDS ==========")

    for record in valid_records:
        print(record)

    # Display rejected records and reasons
    print("\n========== REJECTED RECORDS ==========")

    for rejected in rejected_records:

        print("\nRecord:", rejected["record"])

        for error in rejected["errors"]:
            print("Reason:", error)


# --------------------------------
# 5. CALCULATE DATA QUALITY METRICS
# --------------------------------

def calculate_data_quality_metrics(
    total_records,
    valid_records,
    rejected_records
):

    if total_records == 0:
        print("\nNo records available for analysis.")
        return

    success_rate = (
        valid_records / total_records
    ) * 100

    rejection_rate = (
        rejected_records / total_records
    ) * 100

    print("\n========== DATA QUALITY METRICS ==========")

    print("Total records:", total_records)
    print("Valid records:", valid_records)
    print("Rejected records:", rejected_records)

    print(f"Success rate: {success_rate:.2f}%")
    print(f"Rejection rate: {rejection_rate:.2f}%")


# --------------------------------
# 6. ANALYZE REJECTION REASONS
# --------------------------------

def analyze_rejection_reasons(rejected_records):

    rejection_counts = {}

    for rejected in rejected_records:

        for error in rejected["errors"]:

            rejection_counts[error] = (
                rejection_counts.get(error, 0) + 1
            )

    print("\n========== REJECTION REASON ANALYSIS ==========")

    if not rejection_counts:
        print("No rejected records. All records passed validation.")
        return

    for reason, count in rejection_counts.items():

        print(f"{reason}: {count} record(s)")


# --------------------------------
# 7. MAIN FUNCTION
# --------------------------------

def main():

    # Display original source data
    display_sales_data(sales)

    # Validate source records
    valid_records, rejected_records = validate_sales_records(
        sales
    )

    # Display validation results
    display_validation_report(
        valid_records,
        rejected_records
    )

    # Calculate data quality metrics
    calculate_data_quality_metrics(
        len(sales),
        len(valid_records),
        len(rejected_records)
    )

    # Analyze rejection reasons
    analyze_rejection_reasons(rejected_records)


# --------------------------------
# 8. PROGRAM ENTRY POINT
# --------------------------------

if __name__ == "__main__":
    main()

