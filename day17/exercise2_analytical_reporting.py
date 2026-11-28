
# Day 17 - Exercise 2
# Analytical Reporting with Fact and Dimension Tables
#
# Objectives:
# 1. Calculate revenue by product category.
# 2. Calculate revenue by customer city.
# 3. Find the highest-revenue product.
# 4. Find the highest-revenue customer.
# 5. Validate fact records against dimension tables.

# -----------------------------
# 1. CUSTOMER DIMENSION
# -----------------------------

customers = [
    {
        "customer_key": 1,
        "customer_id": "C101",
        "name": "Alice",
        "city": "Chennai"
    },
    {
        "customer_key": 2,
        "customer_id": "C102",
        "name": "Bob",
        "city": "Bangalore"
    },
    {
        "customer_key": 3,
        "customer_id": "C103",
        "name": "Charlie",
        "city": "Hyderabad"
    }
]


# -----------------------------
# 2. PRODUCT DIMENSION
# -----------------------------

products = [
    {
        "product_key": 101,
        "product_id": "P101",
        "name": "Laptop",
        "category": "Electronics"
    },
    {
        "product_key": 102,
        "product_id": "P102",
        "name": "Mouse",
        "category": "Accessories"
    },
    {
        "product_key": 103,
        "product_id": "P103",
        "name": "Keyboard",
        "category": "Accessories"
    },
    {
        "product_key": 104,
        "product_id": "P104",
        "name": "Monitor",
        "category": "Electronics"
    }
]


# -----------------------------
# 3. SALES FACT TABLE
# Grain: one row per product within an order
# -----------------------------

sales = [
    {
        "order_id": 1001,
        "customer_key": 1,
        "product_key": 101,
        "quantity": 1,
        "unit_price": 50000
    },
    {
        "order_id": 1001,
        "customer_key": 1,
        "product_key": 102,
        "quantity": 2,
        "unit_price": 500
    },
    {
        "order_id": 1002,
        "customer_key": 2,
        "product_key": 103,
        "quantity": 1,
        "unit_price": 1500
    },
    {
        "order_id": 1003,
        "customer_key": 3,
        "product_key": 104,
        "quantity": 2,
        "unit_price": 12000
    },

    # Temporary invalid record for testing validation.
    # Remove this record after confirming the rejection works.
    {
        "order_id": 1004,
        "customer_key": 99,
        "product_key": 101,
        "quantity": 1,
        "unit_price": 50000
    }
]


# -----------------------------
# 4. DIMENSION LOOKUP DICTIONARIES
# -----------------------------

customer_lookup = {
    customer["customer_key"]: customer
    for customer in customers
}

product_lookup = {
    product["product_key"]: product
    for product in products
}


# -----------------------------
# 5. CALCULATE REVENUE
# -----------------------------

def calculate_revenue(sale):
    return sale["quantity"] * sale["unit_price"]


# -----------------------------
# 6. VALIDATE FACT RECORDS
# -----------------------------

def validate_sales_records(sales_records):
    valid_records = []
    rejected_records = []

    for sale in sales_records:
        customer_exists = (
            sale["customer_key"] in customer_lookup
        )

        product_exists = (
            sale["product_key"] in product_lookup
        )

        if customer_exists and product_exists:
            valid_records.append(sale)
        else:
            rejected_records.append(sale)

    return valid_records, rejected_records


def display_validation_report(valid_records, rejected_records):
    total_records = len(valid_records) + len(rejected_records)

    print("\n========== DATA VALIDATION REPORT ==========")
    print("Total records:", total_records)
    print("Valid records:", len(valid_records))
    print("Rejected records:", len(rejected_records))

    if rejected_records:
        print("\nRejected records:")

        for sale in rejected_records:
            print(
                f"Order ID: {sale['order_id']}, "
                f"Customer key: {sale['customer_key']}, "
                f"Product key: {sale['product_key']}"
            )


# -----------------------------
# 7. REVENUE BY PRODUCT CATEGORY
# -----------------------------

def revenue_by_category(valid_sales):
    category_revenue = {}

    for sale in valid_sales:
        product = product_lookup[sale["product_key"]]
        category = product["category"]

        revenue = calculate_revenue(sale)

        category_revenue[category] = (
            category_revenue.get(category, 0) + revenue
        )

    print("\n========== REVENUE BY CATEGORY ==========")

    for category, revenue in category_revenue.items():
        print(f"{category}: ₹{revenue:,.2f}")


# -----------------------------
# 8. REVENUE BY CUSTOMER CITY
# -----------------------------

def revenue_by_city(valid_sales):
    city_revenue = {}

    for sale in valid_sales:
        customer = customer_lookup[sale["customer_key"]]
        city = customer["city"]

        revenue = calculate_revenue(sale)

        city_revenue[city] = (
            city_revenue.get(city, 0) + revenue
        )

    print("\n========== REVENUE BY CITY ==========")

    for city, revenue in city_revenue.items():
        print(f"{city}: ₹{revenue:,.2f}")


# -----------------------------
# 9. REVENUE BY PRODUCT
# -----------------------------

def revenue_by_product(valid_sales):
    product_revenue = {}

    for sale in valid_sales:
        product_key = sale["product_key"]
        revenue = calculate_revenue(sale)

        product_revenue[product_key] = (
            product_revenue.get(product_key, 0) + revenue
        )

    print("\n========== REVENUE BY PRODUCT ==========")

    for product_key, revenue in product_revenue.items():
        product = product_lookup[product_key]

        print(
            f"{product['name']} "
            f"({product['category']}): ₹{revenue:,.2f}"
        )

    return product_revenue


# -----------------------------
# 10. HIGHEST-REVENUE PRODUCT
# -----------------------------

def highest_revenue_product(product_revenue):
    if not product_revenue:
        print("\nNo valid product revenue available.")
        return

    highest_product_key = max(
        product_revenue,
        key=product_revenue.get
    )

    product = product_lookup[highest_product_key]
    revenue = product_revenue[highest_product_key]

    print("\n========== HIGHEST-REVENUE PRODUCT ==========")
    print("Product:", product["name"])
    print("Category:", product["category"])
    print(f"Revenue: ₹{revenue:,.2f}")


# -----------------------------
# 11. HIGHEST-REVENUE CUSTOMER
# -----------------------------

def highest_revenue_customer(valid_sales):
    customer_revenue = {}

    for sale in valid_sales:
        customer_key = sale["customer_key"]
        revenue = calculate_revenue(sale)

        customer_revenue[customer_key] = (
            customer_revenue.get(customer_key, 0) + revenue
        )

    if not customer_revenue:
        print("\nNo valid customer revenue available.")
        return

    highest_customer_key = max(
        customer_revenue,
        key=customer_revenue.get
    )

    customer = customer_lookup[highest_customer_key]
    revenue = customer_revenue[highest_customer_key]

    print("\n========== HIGHEST-REVENUE CUSTOMER ==========")
    print("Customer:", customer["name"])
    print("City:", customer["city"])
    print(f"Revenue: ₹{revenue:,.2f}")


# -----------------------------
# 12. MAIN FUNCTION
# -----------------------------

def main():

    # Validate records before analytical reporting.
    valid_records, rejected_records = validate_sales_records(sales)

    display_validation_report(valid_records, rejected_records)

    # All reports use only validated records.
    revenue_by_category(valid_records)

    revenue_by_city(valid_records)

    product_revenue = revenue_by_product(valid_records)

    highest_revenue_product(product_revenue)

    highest_revenue_customer(valid_records)


# -----------------------------
# 13. PROGRAM ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    main()
