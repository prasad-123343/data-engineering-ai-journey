## Customer Order Analytics Report

### 1. Why I used LEFT JOIN

I used `LEFT JOIN` to combine the `customers` and `customer_orders` tables using `customer_id`. This ensures that every customer appears in the report, even if they have not placed any orders. For example, Sita has no orders, but she is still included in the report.

### 2. Purpose of COUNT() and SUM()

I used `COUNT(co.order_id)` to calculate the number of orders for each customer and `SUM(co.order_amount)` to calculate their total revenue. The `GROUP BY` clause groups the records by customer so that the report displays one row per customer.

### 3. Why I used COALESCE()

When a customer has no matching orders, `SUM()` returns `NULL`. I used `COALESCE(SUM(co.order_amount), 0)` to replace that `NULL` value with zero, making the report easier to understand.

### 4. Avoiding double-counting revenue

Joining tables with different levels of detail can multiply rows. For example, one order containing three products may appear three times after joining the order table with order-product details. Summing the order amount after that join could count the same order multiple times. To avoid this, I need to understand the grain of each table and aggregate data at the correct level before joining when necessary.

### Key learning

I learned how to combine related tables, calculate customer-level metrics, include customers without orders, handle missing values, and recognize the risk of double-counting when joining data.
