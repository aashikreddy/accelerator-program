/*
Problem Description:
The HR planning board requires a workspace distribution matrix to analyze operational units. Write a read-only SQL query to find the department number, 
department name, and the sum of salaries from the employee database. Filter the final rows using a multi-layered nested subquery 
inside the HAVING clause so that you only return organizational units whose total active employee headcount is strictly greater than 
the average employee headcount computed across all active departments in the enterprise.

case=1
output=
deptno	dname	total_department_payroll
20	Research	11825.00



*/
use fs;
SELECT d.deptno, d.dname, SUM(e.sal) AS total_department_payroll
FROM dept d
JOIN emp e
ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname
HAVING COUNT(e.empno) > (
                            SELECT AVG(dept_counts.headcount)
                            FROM (
                                    SELECT COUNT(e_sub.empno) AS headcount
                                    FROM emp e_sub
                                    GROUP BY e_sub.deptno
                            ) dept_counts
)