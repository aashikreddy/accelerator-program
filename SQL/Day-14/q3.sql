/*
Problem Description:
The sales operations team wants to analyze high-performing sales representatives who are generating substantial revenue through commissions. 
Write an SQL query to retrieve the employee's name, their job title, their department's name, and their total compensation (calculated as salary plus commission).
Filter the results to include only employees whose job is 'SALESMAN', whose commission is strictly greater than 0, and 
who work in departments located in either 'Chicago' or 'Tempe'. 
Sort the output by the calculated total compensation in descending order.


case=1
output=
employee_name	job_title	department_name	total_compensation
ALLEN	SALESMAN	Sales	1750.00

*/
use fs;
SELECT e.ename AS employee_name, e.job AS job_title, d.dname AS department_name, (e.sal+e.comm) AS total_compensation
FROM emp as e
JOIN dept as d
ON e.deptno = d.deptno
WHERE e.job = 'SALESMAN' AND e.comm > 0 AND d.location IN('Chicago','Tempe')
ORDER BY total_compensation DESC;