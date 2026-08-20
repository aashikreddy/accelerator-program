/*
Problem Description:
An enterprise HR metrics developer needs to flag anomalous salaries where individuals out-earn the localized aggregate averages. 
Write a read-only SQL query to extract the employee name, department name, location, and salary from the emp and dept tables. 
The query must use nested subqueries to filter and return only those employees whose salary is strictly greater than the average 
salary of the entire department that holds the maximum aggregate payroll budget across the company.  

case=1
output=
employee_name	department_name	location	salary
JONES	Research	Dallas	2975.00
BLAKE	Sales	Chicago	2850.00
CLARK	Accounting	New York	2450.00
SCOTT	Research	Dallas	3000.00
KEVIN	Operations	Boston	5000.00
FORD	Research	Dallas	3000.00



*/
use fs;
SELECT e.ename AS employee_name, d.dname AS department_name, d.location AS location, e.sal AS salary
FROM emp e
JOIN dept d
On e.deptno = d.deptno
WHERE e.sal > (
                SELECT AVG(e2.sal) 
                FROM emp e2 
                WHERE e2.deptno = (
                                    SELECT deptno 
                                    FROM (
                                    SELECT deptno, SUM(sal) as total_payroll
                                    FROM emp
                                    GROUP BY deptno
                                    ORDER BY total_payroll DESC
                                    LIMIT 1
                                    ) AS top_dept
                                    
                                )
);

