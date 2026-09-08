USE EMPLOYEE;
.Write a query to display employee name, salary, previous salary, and next salary.
 SELECT EMPNO, ENAME, SAL,
        LAG(SAL) OVER (ORDER BY EMPNO) AS DIFF_PREVIOUS,
        LEAD(SAL) OVER (ORDER BY EMPNO) AS DIFF_NEXT
FROM EMP
2.Write a query to display the salary difference from the previous employee and next employee.

3.Write a query to find the highest-paid employee from every department.

4.Write a query to find the second-highest-paid employee from every department.
5.Write a query to find the third-highest-paid employee from every department.
6.Write a query to display the top 2 employees from each department based on salary.
7.Write a query to display employees whose salary is higher than the previous employee but lower than the next employee.
8.Write a query to display the overall salary rank and department-wise salary rank of every employee.
 
-
SELECT
 *FROM (SELECT EMPNO, ENAME, SAL, DEPTNO RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) AS R FROM EMPLOYEE) X WHERE R = 1;



SELECT *FROM (SELECT EMPNO, ENAME, SAL, DEPTNO,DENSE_RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) AS R FROM EMPLOYEE) X WHERE R = 2;


SELECT *FROM (SELECT EMPNO, ENAME, SAL, DEPTNO,DENSE_RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) AS R FROM EMPLOYEE) X WHERE R = 3;


SELECT * FROM (SELECT EMPNO, ENAME, SAL, DEPTNO,ROW_NUMBER() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) AS R FROM EMPLOYEE) X WHERE R <= 2;


SELECT *FROM (SELECT EMPNO, ENAME, SAL,
           LAG(SAL) OVER (ORDER BY EMPNO) AS PREV_SAL,
           LEAD(SAL) OVER (ORDER BY EMPNO) AS NEXT_SAL
    FROM EMPLOYEE) X WHERE SAL > PREV_SAL AND SAL < NEXT_SAL;