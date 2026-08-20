/*
Problem Description:
The financial compensation auditor needs to verify leadership pay distributions inside organizational units.
Write a read-only SQL query to select the employee number, employee name, department number, salary, and corresponding salary grade 
tier from the emp and salgrade tables. The logic must use a correlated subquery to filter and return only those individuals
whose personal grade is strictly higher than the average salary grade tier computed across their specific department node

case=1
output=
empno	ename	deptno	sal	grade
7782	CLARK	10	2450.00	4
7499	ALLEN	10	1600.00	3
7782	CLARK	10	2450.00	3
7566	JONES	20	2975.00	4
7788	SCOTT	20	3000.00	4
7902	FORD	20	3000.00	4
7566	JONES	20	2975.00	3
7788	SCOTT	20	3000.00	3
7902	FORD	20	3000.00	3
7698	BLAKE	30	2850.00	4
7698	BLAKE	30	2850.00	3
7844	KEVIN	30	1500.00	3
7839	KEVIN	40	5000.00	6
7839	KEVIN	40	5000.00	5
7839	KEVIN	40	5000.00	4



*/
use fs;
SELECT 
    e.empno,
    e.ename,
    e.deptno,
    e.sal,
    s.grade
FROM 
    emp e
JOIN 
    salgrade s 
    ON e.sal BETWEEN s.losal AND s.hisal
WHERE 
    s.grade > (
        SELECT AVG(s_sub.grade)
        FROM emp e_sub
        JOIN salgrade s_sub 
            ON e_sub.sal BETWEEN s_sub.losal AND s_sub.hisal
        WHERE e_sub.deptno = e.deptno
    )
ORDER BY 
    e.deptno ASC,
    s.grade DESC,
    e.empno ASC;