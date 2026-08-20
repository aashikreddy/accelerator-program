/*
Problem 1 (Medium): High-Value Customers with Delivered Orders
Topic: CTEs & Aggregation Filtering

Statement: The operations team wants to identify top-spending customers using only completed orders. Write a query with a CTE to aggregate total spending for Delivered status orders, then filter for customers who spent more than ₹500. Display customer_id, first_name, and Delivered_Spent.



case=1
output=
case=1
output=
customer_id	first_name	Delivered_Spent
1	Amit	730.00
3	Rahul	610.00
5	Arjun	670.00

*/
use fs;
WITH high_value_customers AS (
SELECT c.customer_id, c.first_name, SUM(o.total_amount) AS Delivered_Spent
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Delivered'
GROUP BY c.customer_id
HAVING SUM(o.total_amount) > 500
)
SELECT *
FROM high_value_customers;