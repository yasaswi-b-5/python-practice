Write a query to display the employee name and their managers name.
use employee;
Write a query to display the employee name, employee salary, and manager name.
Write a query to display the employee name, salary, and department name.
Write a query to display all employees along with their department details.
Write a query to display the employee name, job, salary, and location for employees working in department 20.
Write a query to display only the employees who have a matching department in the DEPT table.
Write a query to display the employee name, department name, and location, sorted by employee salary in descending order.
Write a query to display employees whose department location is DALLAS.

Write a query to display the top 2 employees from each department based on salary.
SELECT *FROM (SELECT e.*,ROW_NUMBER() OVER PARTITION BY DEPTNO ORDER BY SAL DESC) AS rn FROM EMPLOYEE e) x WHERE rn <= 2;
Write a query to display employees whose salary is higher than the previous employee but lower than the next employee.
select ename,department_name location from employee order by (sal) desc
alter table employee add department_name varchar(45);
SELECT* FROM EMPLOYEE;
UPDATE employee
SET department_name = CASE EMPNO
    WHEN 7369 THEN 'Manual testing'
    WHEN 7499 THEN 'frontend developer'
    WHEN 7521 THEN 'backend developer'
    WHEN 7566 THEN 'QA testing'
    WHEN 7654 THEN 'ai engineer'
    WHEN 7698 THEN 'full stack developer'
    WHEN 7782 THEN 'Manual testing'
    WHEN 7788 THEN 'frontend developer'
    WHEN 7839 THEN 'backend developer'
    WHEN 7844 THEN 'QA testing'
    WHEN 7876 THEN 'ai engineer'
    WHEN 7900 THEN 'full stack developer'
    WHEN 7902 THEN 'Manual testing'
    WHEN 7934 THEN 'frontend developer'
END
WHERE EMPNO IN
(7369,7499,7521,7566,7654,7698,7782,7788,7839,7844,7876,7900,7902,7934);


SELECT e.ENAME AS Employee_Name,
       m.ENAME AS Manager_Name
FROM EMPLOYEE e
LEFT JOIN EMPLOYEE m
ON e.MGR = m.EMPNO;
select ename as empname ,emp_salary as sal from employee e left employee m on e.mgr=m.empno;
select ename,sal from employee;
select employee,deptno from employee;
select ename,job,sal,loc from employee where deptno=20;
select ename from employee where loc=dallas;
SELECT *FROM (SELECT e.*,
           LAG(SAL) OVER (ORDER BY EMPNO) AS previous_salary,
           LEAD(SAL) OVER (ORDER BY EMPNO) AS next_salary
    FROM EMPLOYEE e
) x
WHERE SAL > previous_salary
  AND SAL < next_salary;