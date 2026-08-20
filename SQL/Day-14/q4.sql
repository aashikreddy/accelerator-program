/*
Problem Description:
The restaurant finance team wants to audit the total revenue generated from high-value food items.
Write an SQL query to find the food item name, its category, and the total revenue generated from it (calculated as the sum of the total amount across all orders).
Only include items belonging to the 'Main Course' or 'Breakfast' categories where the item has been ordered a total quantity of more than 2 times. 
Sort the results by total revenue in descending order.

case=1
output=
food_item_name	category	total_revenue
Chicken Biryani	Main Course	900.00
Masala Dosa	Breakfast	600.00
Veg Fried Rice	Main Course	390.00
Chole Bhature	Breakfast	300.00

*/
use fs;
SELECT f.name as food_item_name, f.category AS category, SUM(o.total_amount) AS total_revenue
FROM FoodItems AS f
JOIN Orders AS o
ON f.food_id = o.food_id
WHERE f.category IN ('Main Course','Breakfast')
GROUP BY f.food_id
HAVING SUM(o.quantity) > 2
ORDER BY total_revenue DESC;