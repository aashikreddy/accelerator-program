
/*
Problem Description:
The marketing division wants to identify dominant menu items that hold a high market share within their menu sections to create focused combos. 
Write a read-only SQL query to calculate the food item name, category, and total revenue pool for successfully processed rows. Use an advanced 
correlated subquery inside the HAVING clause to filter the final dataset to show only those individual food items whose cumulative sales account 
for more than 35% of the entire revenue generated within that product's parent menu category.


case=1
output=
food_item_name	category	item_total_revenue
Chicken Biryani	Main Course	900.00
Masala Dosa	Breakfast	600.00
Mango Lassi	Beverages	360.00
Gulab Jamun	Desserts	350.00
Samosa	Snacks	270.00
Butter Naan	Breads	240.00



*/
use fs;
SELECT f.name AS food_item_name, f.category, SUM(o.total_amount) AS item_total_revenue
FROM FoodItems f
JOIN Orders o
ON f.food_id = o.food_id
GROUP BY f.food_id, f.name, f.category
HAVING SUM(o.total_amount) > 0.35 * (
                                        SELECT SUM(o_sub.total_amount)
                                        FROM Orders o_sub
                                        JOIN FoodItems f_sub 
                                        ON o_sub.food_id = f_sub.food_id
                                        WHERE f_sub.category = f.category
)
ORDER BY item_total_revenue DESC;