/*
Problem Description:
The HR systems division requires a comprehensive analytics list showing distinct employee tracks who meet high-profile administrative conditions. 
The report needs to display employees who are either working in top salary tiers (Grade 4 or 5) within a department located in 'Chicago', 
or are direct supervisors tracking subordinates who make less than 1500 base salary. Use structural analytical subqueries combined with
a UNION clause to compile these distinct operational groups together.

case=1
output=
empno	ename	classification_reason
7698	BLAKE	High Salary Tier in Chicago
7902	FORD	Manages Underpaid Subordinates
7698	BLAKE	Manages Underpaid Subordinates
7788	SCOTT	Manages Underpaid Subordinates
7782	CLARK	Manages Underpaid Subordinates



*/
use fs;
SELECT e.empno, e.ename, 'High Salary Tier in Chicago' AS classification_reason
FROM emp e
WHERE e.deptno IN (
                    SELECT d.deptno 
                    FROM dept d 
                    WHERE d.location = 'Chicago') 
                    AND EXISTS(
                    SELECT 1
                    FROM salgrade s 
                    WHERE e.sal BETWEEN s.losal AND s.hisal 
                    AND s.grade IN (4,5)
)

UNION

SELECT m.empno, m.ename, 'Manages Underpaid Subordinates' AS classification_reason
FROM emp m
WHERE EXISTS( 
                SELECT 1
                FROM emp sub
                WHERE sub.mgr = m.empno 
                AND sub.sal < 1500
);
