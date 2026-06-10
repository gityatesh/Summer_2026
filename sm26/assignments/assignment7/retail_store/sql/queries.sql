-- Query 1: Customer Spending Ranking (Joins the tables and calculates totals)
SELECT c.customer_name, SUM(t.amount) AS total_spent
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

-- Query 2: Total Sales by Category
SELECT category, SUM(amount) AS total_sales
FROM transactions
GROUP BY category
ORDER BY total_sales DESC;