/*
Problem 3 (Medium): Food Category Revenue Distribution
Topic: CTEs & Multi-table Joins

Statement: Analyze sales by category. Write a CTE that sums total order amounts per category across all delivered orders and shows categories generating over ₹500. Display category and total_revenue.

case=1
output=

category	total_revenue
Main Course	730.00
Breakfast	560.00


*/
use fs;
WITH category_total AS (
SELECT f.category , SUM(o.total_amount) AS total_revenue
FROM FoodItems f
JOIN Orders o
ON f.food_id = o.food_id
WHERE o.status = 'Delivered'
GROUP BY f.category
HAVING SUM(o.total_amount) > 500
)
SELECT *
FROM category_total
