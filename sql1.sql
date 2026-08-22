create database company1;
use company1;
create table employee(
emp_no int primary key,
emp_name varchar(20),
emp_role varchar(40),
emp_join_date date,
report_to int,
emp_salary int,
emp_bonus int,
emp_dept_id int,
emp_blood_grp varchar(3),
emp_type varchar(20),
emp_gender varchar(10),
emp_DOB date
);
insert into employee values (1123,"jay","frontend developer",'2003-08-08',1734,45000,5000,1,"AB+","FULL_TIME","FEMALE",'2014-06-13');
insert into employee values 
(1124,"ajay","backend developer",'2003-07-18',1734,55000,5500,1,"B+","FULL_TIME","MALE",'2010-06-13'),
(1133,"vijay","sql developer",'2005-10-28',1737,54000,4500,1,"O+","PART_TIME","MALE",'2004-05-25'),
(1135,"vijaya","Testing",'2001-02-16',1744,80000,6200,1,"B-","FULL_TIME","FEMALE",'2005-05-30'),
(1178,"yash","HR",'2000-01-10',1776,76000,8000,1,"O-","PART_TIME","MALE",'2004-11-14');
select * from employee;

