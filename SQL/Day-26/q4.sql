/*
Problem : Category Product Launch Pioneer

The food platform operation team is analyzing product launch performance 
across different culinary categories. For each category (e.g., Main Course, Breakfast, Snacks), 
they need to identify the very first item ordered historically on the platform. 
This will help assess initial category traction and order timing patterns.

case=1
output=
order_id	category	food_item	order_date
20	Beverages	Mango Lassi	2026-06-17 11:17:55
3	Breads	Butter Naan	2026-06-17 11:17:55
4	Breakfast	Masala Dosa	2026-06-17 11:17:55
2	Desserts	Gulab Jamun	2026-06-17 11:17:55
11	Main Course	Chicken Biryani	2026-06-17 11:17:55
15	Snacks	Samosa	2026-06-17 11:17:55



*/
use fs;
WITH Ranked AS (
SELECT f.food_id, o.order_id, f.category, f.name AS food_item, o.order_date, ROW_NUMBER() OVER(PARTITION BY f.category ORDER BY o.order_date ASC) AS rnk
FROM FoodItems f
JOIN Orders o
ON f.food_id = o.food_id
-- GROUP BY o.order_id, f.category, 
)
SELECT order_id, category, food_item, order_date
FROM Ranked
WHERE rnk = 1;