/*
Problem Description:
The organizational analysts want to check the distribution of specific clerical and administrative roles across standard corporate branches.
Write an SQL query to find the employee's name, their job, their department number, and the department name.
Filter the rows to include only those employees whose job role is exactly 'CLERK' and whose department is not located in 'New York'. 
Sort the results alphabetically by the employee's name.


case=1
output=
employee_name	job	deptno	department_name
JAMES	CLERK	20	Research
KEVIN	CLERK	20	Research
SMITH	CLERK	20	Research


*/
use fs;
SELECT e.ename AS employee_name, e.job AS job, e.deptno AS deptno, d.dname AS department_name
FROM emp AS e
JOIN dept AS d
ON e.deptno = d.deptno
WHERE e.job = 'CLERK' AND d.location NOT IN ('New York')
ORDER BY e.ename;
