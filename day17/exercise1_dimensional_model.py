
"""
Day 17 - Section 7 - Exercise 1
Building a Simple Dimensional Data Model

Objective:
1. Define customer and product dimensions.
2. Define sales fact data.
3. Calculate revenue for each sales record.
4. Calculate total revenue.
5. Calculate revenue by customer.
6. Calculate revenue by product.
7. Generate readable analytical reports.
"""


# ============================================================
# SECTION 1: CUSTOMER DIMENSION
# ============================================================

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


# ============================================================
# SECTION 2: PRODUCT DIMENSION
# ============================================================

products = [
    {
        "product_key": 101,
        "product_id": "P101",
        "product_name": "Laptop",
        "category": "Electronics"
    },
    {
        "product_key": 102,
        "product_id": "P102",
        "product_name": "Mouse",
        "category": "Accessories"
    },
    {
        "product_key": 103,
        "product_id": "P103",
        "product_name": "Keyboard",
        "category": "Accessories"
    },
    {
        "product_key": 104,
        "product_id": "P104",
        "product_name": "Monitor",
        "category": "Electronics"
    }
]


# ============================================================
# SECTION 3: SALES FACT DATA
# Grain: One row per product within an order
# ============================================================

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
    }
]


# ============================================================
# SECTION 4: CREATE DIMENSION LOOKUP DICTIONARIES
# ============================================================

customer_lookup = {
    customer["customer_key"]: customer
    for customer in customers
}

product_lookup = {
    product["product_key"]: product
    for product in products
}


# ============================================================
# SECTION 5: CALCULATE REVENUE FOR EACH SALES RECORD
# ============================================================

def calculate_sales_revenue(sales_records):
    """
    Calculate revenue for every sales record.

    Revenue = Quantity * Unit Price
    """

    for sale in sales_records:
        sale["revenue"] = (
            sale["quantity"] * sale["unit_price"]
        )

    return sales_records


# ============================================================
# SECTION 6: CALCULATE TOTAL REVENUE
# ============================================================

def calculate_total_revenue(sales_records):
    """
    Calculate total revenue across all sales records.
    """

    total_revenue = 0

    for sale in sales_records:
        total_revenue += sale["revenue"]

    return total_revenue


# ============================================================
# SECTION 7: CALCULATE REVENUE BY CUSTOMER
# ============================================================

def calculate_customer_revenue(sales_records):
    """
    Group sales revenue using customer_key.
    """

    customer_revenue = {}

    for sale in sales_records:
        customer_key = sale["customer_key"]
        revenue = sale["revenue"]

        if customer_key not in customer_revenue:
            customer_revenue[customer_key] = 0

        customer_revenue[customer_key] += revenue

    return customer_revenue


# ============================================================
# SECTION 8: CALCULATE REVENUE BY PRODUCT
# ============================================================

def calculate_product_revenue(sales_records):
    """
    Group sales revenue using product_key.
    """

    product_revenue = {}

    for sale in sales_records:
        product_key = sale["product_key"]
        revenue = sale["revenue"]

        if product_key not in product_revenue:
            product_revenue[product_key] = 0

        product_revenue[product_key] += revenue

    return product_revenue


# ============================================================
# SECTION 9: DISPLAY SALES REVENUE REPORT
# ============================================================

def display_sales_report(sales_records):

    print("\n========== SALES REVENUE ==========")

    for sale in sales_records:
        print(
            f"Order ID: {sale['order_id']}, "
            f"Revenue: ₹{sale['revenue']}"
        )


# ============================================================
# SECTION 10: DISPLAY TOTAL REVENUE REPORT
# ============================================================

def display_total_revenue(total_revenue):

    print("\n========== TOTAL REVENUE ==========")

    print(f"Total Revenue: ₹{total_revenue}")


# ============================================================
# SECTION 11: DISPLAY CUSTOMER REVENUE REPORT
# ============================================================

def display_customer_report(customer_revenue):

    print("\n========== CUSTOMER REVENUE REPORT ==========")

    for customer_key, revenue in customer_revenue.items():

        customer = customer_lookup.get(customer_key)

        if customer is None:
            print(f"Unknown customer key: {customer_key}")
            continue

        print(
            f"Customer: {customer['name']}, "
            f"City: {customer['city']}, "
            f"Revenue: ₹{revenue}"
        )


# ============================================================
# SECTION 12: DISPLAY PRODUCT REVENUE REPORT
# ============================================================

def display_product_report(product_revenue):

    print("\n========== PRODUCT REVENUE REPORT ==========")

    for product_key, revenue in product_revenue.items():

        product = product_lookup.get(product_key)

        if product is None:
            print(f"Unknown product key: {product_key}")
            continue

        print(
            f"Product: {product['product_name']}, "
            f"Category: {product['category']}, "
            f"Revenue: ₹{revenue}"
        )


# ============================================================
# SECTION 13: MAIN PROGRAM
# ============================================================

def main():

    # Step 1: Calculate revenue for each sales record
    calculate_sales_revenue(sales)

    # Step 2: Calculate total revenue
    total_revenue = calculate_total_revenue(sales)

    # Step 3: Calculate revenue by customer
    customer_revenue = calculate_customer_revenue(sales)

    # Step 4: Calculate revenue by product
    product_revenue = calculate_product_revenue(sales)

    # Step 5: Display all analytical reports
    display_sales_report(sales)

    display_total_revenue(total_revenue)

    display_customer_report(customer_revenue)

    display_product_report(product_revenue)


# ============================================================
# SECTION 14: PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
