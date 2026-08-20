/*
Topic: Chained CTEs across Non-Equi Joins

Statement: Categorize employees by salary grade, compute total salary spent per grade, and list grades accounting for more than ₹5,000 in salary payout. Display grade, employee_count, and total_grade_sal.

case=1
output=

grade	employee_count	total_grade_sal
1	8	9750.00
3	7	17375.00
2	10	21175.00
4	6	19275.00


*/
use fs;
WITH employee_cat AS (
SELECT s.grade, COUNT(e.empno) AS employee_count, SUM(e.sal) AS total_grade_sal
FROM salgrade s
JOIN emp e
ON e.sal BETWEEN s.losal AND s.hisal
GROUP BY s.grade
HAVING SUM(e.sal) > 5000
)
SELECT *
FROM employee_cat;