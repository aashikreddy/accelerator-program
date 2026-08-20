/*
Problem Description:
The operational marketing team wants to find the IDs of customers who have ordered 'Chicken Biryani' AND have ordered 'Mango Lassi', 
but have completely excluded 'Samosa' from their ordering lifetime history. Structure a combination of INTERSECT and EXCEPT clauses 
driven by internal target-matching subqueries to extract this precise segmentation.



case=1
output=
customer_id
4



*/
use fs;
SELECT result.customer_id FROM(
SELECT customer_id
FROM (
        SELECT o.customer_id 
        FROM Orders o 
        JOIN FoodItems f 
        ON o.food_id = f.food_id 
        WHERE f.name ='Chicken Biryani'
) AS BiryaniCustomers

INTERSECT

SELECT customer_id
FROM (
        SELECT o.customer_id 
        FROM Orders o 
        JOIN FoodItems f 
        ON o.food_id = f.food_id 
        WHERE f.name ='Mango Lassi'
) AS LassiCustomers

EXCEPT

SELECT customer_id
FROM (
        SELECT o.customer_id 
        FROM Orders o 
        JOIN FoodItems f 
        ON o.food_id = f.food_id 
        WHERE f.name ='Samosa'
) AS SamosaCustomers
)AS result;
