/*
Problem Description:
The strategic analysis team requires a list of department numbers where the average employee salary is strictly greater than the company-wide average salary.
Additionally, these departments must also employ at least one worker who ranks among the highest-paid individuals in the company (specifically,
those earning a salary greater than or equal to the second-highest salary found in the entire organization). Write an SQL query using nested table 
derivatives, multi-level metrics, and an INTERSECT operator block to join these matching criteria groups cleanly without modifying any structural data.

case=1
output=
deptno
40




*/
use fs;
SELECT deptno
FROM (
        SELECT e.deptno 
        FROM emp e 
        GROUP BY e.deptno 
        HAVING AVG(e.sal) > (
                                SELECT AVG(sal) 
                                FROM emp
)) AS high_avg_depts

INTERSECT

SELECT deptno
FROM emp e
WHERE sal >= (
                SELECT MAX(sal) 
                FROM emp 
                WHERE sal < (
                                SELECT MAX(sal) 
                                FROM emp 
));