/*
Problem Description:
The senior menu performance analyst wants to find high-velocity food items that consistently drive strong transactional volume within their food groups.
Write a read-only SQL query to retrieve the food item name, category, and total quantities sold across all successfully processed transactions.

Filter the output using a correlated subquery inside the HAVING clause to return only those individual food items whose cumulative quantity sold
is strictly greater than the average individual quantity ordered for any single transaction within that exact same food category.



case=1
output=
food_item_name	category	total_quantity_sold
Samosa	Snacks	9
Butter Naan	Breads	6
Masala Dosa	Breakfast	3
Dal Tadka	Main Course	2



*/
use fs;
SELECT 
    f.name AS food_item_name,
    f.category,
    SUM(o.quantity) AS total_quantity_sold
FROM 
    FoodItems f
JOIN 
    Orders o ON f.food_id = o.food_id
WHERE 
    o.status = 'Delivered'
GROUP BY 
    f.food_id,
    f.name,
    f.category
HAVING 
    SUM(o.quantity) > (
        SELECT 
            AVG(o_sub.quantity)
        FROM 
            Orders o_sub
        JOIN 
            FoodItems f_sub ON o_sub.food_id = f_sub.food_id
        WHERE 
            f_sub.category = f.category
            AND o_sub.status = 'Delivered'
    )
ORDER BY 
    total_quantity_sold DESC;