create database company1;
use company1;
create table employee(
emp_dept_id int,
emp_dept_name varchar,
emp_location varchar(30),
emp_head_id int,
);
desc employee;
insert into employee values 
(1,"Development","Hyderabad",1738),
(2,"Testing","Banglore",1182),
(3,"Devops","Chennai",1846),
(4,"Cybersecurity","Pune",1344),
(5,"Human Resources","Delhi",1068)
select * from employee;
ALTER TABLE employee
RENAME TO department;
