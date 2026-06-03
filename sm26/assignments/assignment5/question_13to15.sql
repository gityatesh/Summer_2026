CREATE TABLE employees (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department VARCHAR(50)
);

INSERT INTO employees ( name, salary, department) VALUES
( 'Rahul', 50000, 'IT'),
( 'Aman', 70000, 'HR'),
( 'Neha', 60000, 'IT'),
( 'Priya', 80000, 'Finance'),
( 'Rohit', 65000, 'HR'),
( 'Karan', 55000, 'IT'),
( 'Simran', 90000, 'Finance'),
( 'Arjun', 72000, 'Sales'),
( 'Mehak', 68000, 'HR'),
( 'Varun', 75000, 'Sales');

--question 13
--using inner join
select e.id, e.name, e.department, e.salary from employees e
inner join (
    SELECT department, avg(salary) from employees
    group by department
) d
on department.e = department.d
where salary.e>average_salary.d

--question 14
--using rank()
SELECT department, avg(salary) as average_salary, rank() over (order by average_salary desc) as rank
from employees
group by department
;

--question 15
INSERT INTo employees
( name, salary, department) 
VALUES
('yash', '85000','ai'),
('riya', '92000', 'ai')

SELECT department, avg(salary) as average_salary, rank() over (order by average_salary desc) as rank
from employees
group by department
;

--using rank() we can see ai has the highest average salary