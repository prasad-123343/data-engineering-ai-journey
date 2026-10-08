
-- Day 5 Project: Customer Order Analytics Report

SELECT
    c.customer_id,
    c.customer_name,
    COUNT(co.order_id) AS order_count,
    COALESCE(SUM(co.order_amount), 0) AS total_revenue
FROM customers AS c
LEFT JOIN customer_orders AS co
    ON c.customer_id = co.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_revenue DESC;