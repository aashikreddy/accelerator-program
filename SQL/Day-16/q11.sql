/*

Problem Description:
The business intelligence developer wants to identify high-value breakfast consumers to target with a new morning loyalty campaign.
Write a read-only SQL query to retrieve the customer's full name, email address, and their total lifetime spending across all menu categories.
Filter the output to return only those customers whose cumulative spending specifically on items in the 'Breakfast' category is 
strictly greater than the average breakfast expenditure calculated across all customers who have ordered breakfast.

case=1
output=
customer_name	email	total_lifetime_spending
Priya Singh	priya.singh@yahoo.com	680.00
Arjun Gupta	arjun.gupta@gmail.com	920.00



*/
use fs;
SELECT CONCAT(c.first_name," ",c.last_name) AS customer_name, c.email, SUM(o.total_amount) AS total_lifetime_spending
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
JOIN FoodItems f
ON o.food_id = f.food_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
HAVING SUM( 
            CASE 
            WHEN f.category = 'Breakfast' THEN o.total_amount 
            ELSE 0 
END) > (
        SELECT AVG(breakfast_total) 
        FROM 
        ( SELECT o2.customer_id, SUM(o2.total_amount) AS breakfast_total 
          FROM Orders o2
          JOIN FoodItems f2 
          ON o2.food_id = f2.food_id
          WHERE f2.category = 'Breakfast'
          GROUP BY o2.customer_id
        ) AS BreakFastStats
    )

ORDER BY total_lifetime_spending;
