/*
Problem Description:
The customer service helpdesk requires a comprehensive master report to verify line-item details for pending financial reconciliations. 
Write an SQL query to combine data from three tables to extract the customer's email, the order date, the food item name, the individual item price, and the total amount charged. 
Filter the output to show only transactions where the order status is 'Pending'.
Sort the output chronologically by the order date.


case=1
output=
email	order_date	food_item_name	unit_price	total_amount
neha.patel@yahoo.com	2026-06-17 11:17:55	Chole Bhature	100.00	100.00
neha.patel@yahoo.com	2026-06-17 11:17:55	Chicken Biryani	300.00	600.00
priya.singh@yahoo.com	2026-06-17 11:17:55	Veg Fried Rice	130.00	260.00



*/
use fs;
SELECT c.email AS email, o.order_date AS order_date, f.name AS food_item_name, f.price AS unit_price, o.total_amount AS total_amount
FROM FoodItems AS f
JOIN Orders AS o
ON f.food_id = o.food_id
JOIN Customers AS c
ON o.customer_id = c.customer_id
WHERE o.status IN ('Pending')
ORDER BY order_date ASC;