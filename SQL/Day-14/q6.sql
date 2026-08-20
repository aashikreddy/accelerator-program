/*

Problem Description:
The customer relationship team wants to follow up with users who have orders currently delayed in the preparation phase. 
Write an SQL query to extract the customer's full name (first name and last name combined), their phone number, the name of the food item ordered, and the order date.
Limit the records to orders where the status is exactly 'Preparing' and the food item price is greater than 100. 
Sort the final list chronologically by the order date.

case=1
output=
customer_full_name	phone	food_item_name	order_date
Arjun Gupta	9876501234	Paneer Butter Masala	2026-06-17 11:17:55
Priya Singh	8765432109	Masala Dosa	2026-06-17 11:17:55


*/

use fs;
SELECT CONCAT(c.first_name ,' ' , c.last_name) AS customer_full_name ,c.phone AS phone, f.name AS food_item_name, o.order_date AS order_date
FROM Customers AS c
INNER JOIN Orders AS o
ON c.customer_id = o.customer_id
INNER JOIN FoodItems AS f
On o.food_id = f.food_id
WHERE o.status = 'Preparing' AND f.price > 100
ORDER BY order_date;


